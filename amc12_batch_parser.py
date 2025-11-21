#!/usr/bin/env python3
"""
AMC 12 Batch Parser - Parse AMC 12 problems from ArtOfProblemSolving.com
Handles both A and B variants (2002-present) and single version (2000-2001)
"""

import requests
from bs4 import BeautifulSoup, NavigableString
import re
from pathlib import Path
import time
import os
import random

def fetch_page_content(url, retry_count=3):
    """Fetch the webpage content with retry logic."""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0'
    ]
    
    for attempt in range(retry_count):
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://artofproblemsolving.com/wiki/index.php/AMC_12_Problems_and_Solutions'
        }
        
        session = requests.Session()
        
        try:
            # Add random delay to appear more human-like
            if attempt > 0:
                delay = random.uniform(5, 10)
                print(f"  Retry {attempt + 1}/{retry_count} after {delay:.1f}s delay...")
                time.sleep(delay)
            
            response = session.get(url, headers=headers, timeout=30, allow_redirects=True)
            
            if response.status_code == 200:
                return response.text
            elif response.status_code == 403:
                print(f"  Received 403 Forbidden (attempt {attempt + 1}/{retry_count})")
                continue
            else:
                response.raise_for_status()
                
        except requests.RequestException as e:
            print(f"  Error on attempt {attempt + 1}: {e}")
            if attempt == retry_count - 1:
                print(f"  Failed after {retry_count} attempts for URL: {url}")
        
        finally:
            session.close()
    
    return None

def extract_paragraph_content_inline(paragraph):
    """Extract content from a paragraph, handling mixed text and images properly."""
    # Check if this paragraph contains only a Solution link
    if len(paragraph.contents) == 1 and paragraph.find('a'):
        link = paragraph.find('a')
        if link and link.get_text().strip() == 'Solution':
            return "Solution"
    
    # Check if paragraph contains both text and images
    has_regular_images = False
    has_asy = False
    has_text = False
    
    for element in paragraph.contents:
        if isinstance(element, NavigableString):
            if str(element).strip():
                has_text = True
        elif hasattr(element, 'name'):
            if element.name == 'img':
                alt_text = element.get('alt', '')
                if alt_text and alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                    has_asy = True
                elif not ('latex' in element.get('class', [])):
                    has_regular_images = True
            elif element.name == 'a' and element.find('img'):
                img = element.find('img')
                alt_text = img.get('alt', '')
                if alt_text and alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                    has_asy = True
                elif not ('latex' in img.get('class', [])):
                    has_regular_images = True
    
    # If paragraph has ASY, return it immediately on its own lines with extra spacing
    if has_asy:
        for element in paragraph.contents:
            if hasattr(element, 'name'):
                if element.name == 'img':
                    alt_text = element.get('alt', '')
                    if alt_text and alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                        return f"\n\n{alt_text}\n"
                elif element.name == 'a' and element.find('img'):
                    img = element.find('img')
                    alt_text = img.get('alt', '')
                    if alt_text and alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                        return f"\n\n{alt_text}\n"
    
    # If paragraph has text + regular images, separate them
    if has_text and has_regular_images:
        text_parts = []
        image_parts = []
        
        for element in paragraph.contents:
            if isinstance(element, NavigableString):
                text = str(element).strip()
                if text:
                    text_parts.append(text)
            elif hasattr(element, 'name'):
                if element.name == 'img':
                    alt_text = element.get('alt', '')
                    src = element.get('src', '')
                    
                    if alt_text:
                        is_latex = ('latex' in element.get('class', []) or 
                                  (src and 'latex.artofproblemsolving.com' in src))
                        
                        if is_latex:
                            text_parts.append(alt_text)
                        else:
                            if src:
                                if src.startswith('//'):
                                    full_url = 'https:' + src
                                elif src.startswith('/'):
                                    full_url = 'https://artofproblemsolving.com' + src
                                else:
                                    full_url = src
                                image_parts.append(f"![]({full_url})")
                            else:
                                image_parts.append(f"![]({alt_text})")
                elif element.name == 'a':
                    img_in_link = element.find('img')
                    if img_in_link:
                        alt_text = img_in_link.get('alt', '')
                        src = img_in_link.get('src', '')
                        
                        if alt_text:
                            is_latex = ('latex' in img_in_link.get('class', []) or 
                                      (src and 'latex.artofproblemsolving.com' in src))
                            
                            if is_latex:
                                text_parts.append(alt_text)
                            else:
                                if src:
                                    if src.startswith('//'):
                                        full_url = 'https:' + src
                                    elif src.startswith('/'):
                                        full_url = 'https://artofproblemsolving.com' + src
                                    else:
                                        full_url = src
                                    image_parts.append(f"![]({full_url})")
                                else:
                                    image_parts.append(f"![]({alt_text})")
                    else:
                        link_text = element.get_text().strip()
                        if link_text and link_text != 'Solution':
                            text_parts.append(link_text)
                else:
                    text = element.get_text().strip()
                    if text:
                        text_parts.append(text)
        
        result_parts = []
        if text_parts:
            text_content = ' '.join(text_parts)
            text_content = re.sub(r'\s+', ' ', text_content)
            result_parts.append(text_content.strip())
        
        for image in image_parts:
            result_parts.append(image)
        
        return '\n\n'.join(result_parts)
    
    # If paragraph has only regular images, process them
    if has_regular_images and not has_text:
        for element in paragraph.contents:
            if hasattr(element, 'name'):
                if element.name == 'img':
                    alt_text = element.get('alt', '')
                    src = element.get('src', '')
                    
                    if alt_text:
                        is_latex = ('latex' in element.get('class', []) or 
                                  (src and 'latex.artofproblemsolving.com' in src))
                        
                        if is_latex:
                            return alt_text
                        else:
                            if src:
                                if src.startswith('//'):
                                    full_url = 'https:' + src
                                elif src.startswith('/'):
                                    full_url = 'https://artofproblemsolving.com' + src
                                else:
                                    full_url = src
                                return f"\n\n![]({full_url})\n"
                            else:
                                return f"\n\n![]({alt_text})\n"
                elif element.name == 'a' and element.find('img'):
                    img = element.find('img')
                    alt_text = img.get('alt', '')
                    src = img.get('src', '')
                    
                    if alt_text:
                        is_latex = ('latex' in img.get('class', []) or 
                                  (src and 'latex.artofproblemsolving.com' in src))
                        
                        if is_latex:
                            return alt_text
                        else:
                            if src:
                                if src.startswith('//'):
                                    full_url = 'https:' + src
                                elif src.startswith('/'):
                                    full_url = 'https://artofproblemsolving.com' + src
                                else:
                                    full_url = src
                                return f"\n\n![]({full_url})\n"
                            else:
                                return f"\n\n![]({alt_text})\n"
    
    # Default processing for other cases
    content_parts = []
    for element in paragraph.contents:
        if isinstance(element, NavigableString):
            text = str(element).strip()
            if text:
                content_parts.append(text)
        elif hasattr(element, 'name'):
            if element.name == 'img':
                alt_text = element.get('alt', '')
                src = element.get('src', '')
                
                if alt_text:
                    is_latex = ('latex' in element.get('class', []) or 
                              (src and 'latex.artofproblemsolving.com' in src))
                    
                    if is_latex:
                        content_parts.append(alt_text)
            elif element.name == 'a':
                img_in_link = element.find('img')
                if img_in_link:
                    alt_text = img_in_link.get('alt', '')
                    src = img_in_link.get('src', '')
                    
                    if alt_text:
                        is_latex = ('latex' in img_in_link.get('class', []) or 
                                  (src and 'latex.artofproblemsolving.com' in src))
                        
                        if is_latex:
                            content_parts.append(alt_text)
                else:
                    link_text = element.get_text().strip()
                    if link_text and link_text != 'Solution':
                        content_parts.append(link_text)
            elif element.name == 'br':
                content_parts.append(' ')
            else:
                text = element.get_text().strip()
                if text:
                    content_parts.append(text)
    
    content = ' '.join(content_parts)
    content = re.sub(r'\s+', ' ', content)
    return content.strip()

def extract_problems_polished(html_content):
    """Extract problems with polished formatting."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the main content
    content_div = soup.find('div', {'class': 'mw-parser-output'}) or soup.find('div', {'id': 'mw-content-text'})
    if not content_div:
        print("Could not find main content div")
        return None
    
    problems_content = []
    
    # Find all problem headers
    problem_headers = content_div.find_all(['h2', 'h3'])
    
    for header in problem_headers:
        header_text = header.get_text().strip()
        
        # Check if this is a problem header
        problem_match = re.match(r'Problem (\d+)', header_text)
        if not problem_match:
            continue
            
        problem_num = problem_match.group(1)
        problem_lines = [f"Problem {problem_num}"]
        
        # Collect all content for this problem
        current_text_parts = []
        solution_found = False
        
        current = header.next_sibling
        while current:
            if hasattr(current, 'name'):
                # Stop if we hit another problem header
                if current.name in ['h2', 'h3']:
                    next_header_text = current.get_text().strip()
                    if re.match(r'Problem \d+', next_header_text):
                        break
                
                # Process paragraphs
                if current.name == 'p':
                    paragraph_content = extract_paragraph_content_inline(current)
                    
                    if paragraph_content.strip() == 'Solution':
                        if current_text_parts:
                            problem_lines.append(' '.join(current_text_parts))
                            current_text_parts = []
                        
                        if not solution_found:
                            problem_lines.append("")
                            problem_lines.append("Solution")
                            solution_found = True
                            
                    elif paragraph_content.startswith('\n\n[asy]'):
                        if current_text_parts:
                            problem_lines.append(' '.join(current_text_parts))
                            current_text_parts = []
                        problem_lines.append(paragraph_content.strip())
                        
                    elif paragraph_content.startswith('\n\n![]'):
                        if current_text_parts:
                            problem_lines.append(' '.join(current_text_parts))
                            current_text_parts = []
                        problem_lines.append(paragraph_content.strip())
                        
                    elif '\n\n![](' in paragraph_content:
                        if current_text_parts:
                            problem_lines.append(' '.join(current_text_parts))
                            current_text_parts = []
                        
                        parts = paragraph_content.split('\n\n')
                        for part in parts:
                            if part.strip():
                                problem_lines.append(part.strip())
                        
                    elif paragraph_content.strip():
                        if '\\textbf{(' in paragraph_content and 'qquad' in paragraph_content:
                            if current_text_parts:
                                problem_lines.append(' '.join(current_text_parts))
                                current_text_parts = []
                            problem_lines.append("")
                            problem_lines.append(paragraph_content)
                        else:
                            current_text_parts.append(paragraph_content)
                        
            current = current.next_sibling
        
        if current_text_parts:
            problem_lines.append(' '.join(current_text_parts))
        
        if not solution_found:
            problem_lines.append("")
            problem_lines.append("Solution")
            
        problem_lines.append("")
        
        problems_content.append('\n'.join(problem_lines))
    
    return '\n'.join(problems_content)

def clean_final_output(content):
    """Final cleaning and formatting."""
    if not content:
        return None
    
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        
        if ('copyrighted © by the Mathematical Association of America' in line or
            'AMC_logo.png' in line):
            continue
        
        line = line.replace('&nbsp;', ' ')
        line = line.replace('&amp;', '&')
        line = line.replace('&lt;', '<')
        line = line.replace('&gt;', '>')
        
        line = re.sub(r'\s+', ' ', line)
        
        cleaned_lines.append(line)
    
    result = '\n'.join(cleaned_lines)
    result = re.sub(r'\n\s*\n\s*\n', '\n\n', result)
    
    return result

def parse_amc12_variant(year, variant=None):
    """Parse AMC 12 problems for a specific year and variant (A or B)."""
    # Construct URL based on year and variant
    if variant:
        url = f"https://artofproblemsolving.com/wiki/index.php/{year}_AMC_12{variant}_Problems"
        name = f"{year} AMC 12{variant}"
    else:
        # For 2000-2001, there's only one version
        url = f"https://artofproblemsolving.com/wiki/index.php/{year}_AMC_12_Problems"
        name = f"{year} AMC 12"
    
    print(f"\nFetching {name} problems...")
    html_content = fetch_page_content(url)
    
    if not html_content:
        print(f"  Failed to fetch {name} problems")
        return False
    
    print(f"  Extracting problems for {name}...")
    problems_content = extract_problems_polished(html_content)
    
    if not problems_content:
        print(f"  Failed to extract problems for {name}")
        return False
    
    cleaned_content = clean_final_output(problems_content)
    
    if not cleaned_content:
        print(f"  Failed to clean content for {name}")
        return False
    
    # Save the result
    output_dir = Path("data/raw/AMC12")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{name}.md"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"  ✓ Saved {name} problems to {output_path}")
    
    # Quick stats
    lines = cleaned_content.split('\n')
    problems = [line for line in lines if line.startswith('Problem ')]
    print(f"    Found {len(problems)} problems, {len(lines)} total lines")
    
    return True

def main():
    """Parse AMC 12 problems with improved error handling."""
    print("=" * 60)
    print("AMC 12 Batch Parser")
    print("=" * 60)
    print("\nThis script will download AMC 12 problems from AoPS.")
    print("Note: The website may block automated requests.")
    print("The script includes retry logic and delays.\n")
    
    success_count = 0
    failed_items = []
    
    # Current year (adjust as needed)
    current_year = 2024
    
    # Start with a small test
    print("Testing connection with recent exams...")
    test_years = [(2024, 'A'), (2024, 'B'), (2023, 'A')]
    
    for year, variant in test_years:
        if parse_amc12_variant(year, variant):
            success_count += 1
            print(f"  ✓ Successfully parsed {year} AMC 12{variant}")
            break
        else:
            failed_items.append(f"{year} AMC 12{variant}")
            print(f"  ✗ Failed to parse {year} AMC 12{variant}")
    
    if success_count == 0:
        print("\n⚠ Unable to connect to AoPS. The website may be blocking requests.")
        print("Try:")
        print("  1. Running the script later")
        print("  2. Using a VPN or proxy")
        print("  3. Downloading pages manually")
        return
    
    print("\n" + "-" * 40)
    print("Connection successful! Continuing with full download...")
    print("-" * 40)
    
    # Parse years with A and B variants (2002-present)
    print("\nParsing AMC 12A and 12B (2002-2024)...")
    for year in range(current_year, 2001, -1):
        for variant in ['A', 'B']:
            try:
                # Add longer delay between requests to avoid blocking
                delay = random.uniform(3, 7)
                print(f"  Waiting {delay:.1f}s before next request...")
                time.sleep(delay)
                
                if parse_amc12_variant(year, variant):
                    success_count += 1
                else:
                    failed_items.append(f"{year} AMC 12{variant}")
            except Exception as e:
                print(f"  Error parsing {year} AMC 12{variant}: {e}")
                failed_items.append(f"{year} AMC 12{variant}")
    
    # Parse years with single version (2000-2001)
    print("\nParsing AMC 12 (2000-2001, single version)...")
    for year in range(2001, 1999, -1):
        try:
            delay = random.uniform(3, 7)
            print(f"  Waiting {delay:.1f}s before next request...")
            time.sleep(delay)
            
            if parse_amc12_variant(year):
                success_count += 1
            else:
                failed_items.append(f"{year} AMC 12")
        except Exception as e:
            print(f"  Error parsing {year} AMC 12: {e}")
            failed_items.append(f"{year} AMC 12")
    
    print("\n" + "=" * 60)
    print(f"Completed! Successfully parsed {success_count} AMC 12 exams.")
    if failed_items:
        print(f"\nFailed items ({len(failed_items)}):")
        for item in failed_items[:10]:  # Show first 10 failures
            print(f"  - {item}")
        if len(failed_items) > 10:
            print(f"  ... and {len(failed_items) - 10} more")
    else:
        print("All items parsed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()