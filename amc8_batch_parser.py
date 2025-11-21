#!/usr/bin/env python3
"""
AMC 8 Batch Parser - Parse AMC 8 problems from 2024 to 1999
"""

import requests
from bs4 import BeautifulSoup, NavigableString
import re
from pathlib import Path
import time
import os

def fetch_page_content(url):
    """Fetch the webpage content."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
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
                        return f"\n\n{alt_text}\n"  # ASY block with proper spacing
                elif element.name == 'a' and element.find('img'):
                    img = element.find('img')
                    alt_text = img.get('alt', '')
                    if alt_text and alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                        return f"\n\n{alt_text}\n"  # ASY block with proper spacing
    
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
                        # Check if this is a LaTeX image (by URL or class)
                        is_latex = ('latex' in element.get('class', []) or 
                                  (src and 'latex.artofproblemsolving.com' in src))
                        
                        if is_latex:
                            # LaTeX image - use alt text as LaTeX content
                            text_parts.append(alt_text)
                        else:
                            # Regular image - convert to markdown format
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
                            # Check if this is a LaTeX image (by URL or class)
                            is_latex = ('latex' in img_in_link.get('class', []) or 
                                      (src and 'latex.artofproblemsolving.com' in src))
                            
                            if is_latex:
                                # LaTeX image - use alt text as LaTeX content
                                text_parts.append(alt_text)
                            else:
                                # Regular image - convert to markdown format
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
        
        # Combine text and images on separate lines
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
                        # Check if this is a LaTeX image (by URL or class)
                        is_latex = ('latex' in element.get('class', []) or 
                                  (src and 'latex.artofproblemsolving.com' in src))
                        
                        if is_latex:
                            # LaTeX image - return as LaTeX content
                            return alt_text
                        else:
                            # Regular image - return as markdown
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
                        # Check if this is a LaTeX image (by URL or class)
                        is_latex = ('latex' in img.get('class', []) or 
                                  (src and 'latex.artofproblemsolving.com' in src))
                        
                        if is_latex:
                            # LaTeX image - return as LaTeX content
                            return alt_text
                        else:
                            # Regular image - return as markdown
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
                    # Check if this is a LaTeX image (by URL or class)
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
                        # Check if this is a LaTeX image (by URL or class)
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
        current_text_parts = []  # Buffer for text that should be on same line
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
                        # Flush any buffered text first
                        if current_text_parts:
                            problem_lines.append(' '.join(current_text_parts))
                            current_text_parts = []
                        
                        if not solution_found:
                            problem_lines.append("")
                            problem_lines.append("Solution")
                            solution_found = True
                            
                    elif paragraph_content.startswith('\n\n[asy]'):
                        # ASY diagram - flush text buffer first, then add ASY
                        if current_text_parts:
                            problem_lines.append(' '.join(current_text_parts))
                            current_text_parts = []
                        problem_lines.append(paragraph_content.strip())
                        
                    elif paragraph_content.startswith('\n\n![]'):
                        # Standalone image - flush text buffer first, then add image
                        if current_text_parts:
                            problem_lines.append(' '.join(current_text_parts))
                            current_text_parts = []
                        problem_lines.append(paragraph_content.strip())
                        
                    elif '\n\n![](' in paragraph_content:
                        # Mixed content with text and images - split them
                        if current_text_parts:
                            problem_lines.append(' '.join(current_text_parts))
                            current_text_parts = []
                        
                        # Split by double newlines and add each part
                        parts = paragraph_content.split('\n\n')
                        for part in parts:
                            if part.strip():
                                problem_lines.append(part.strip())
                        
                    elif paragraph_content.strip():
                        # Check if this looks like answer choices
                        if '\\textbf{(' in paragraph_content and 'qquad' in paragraph_content:
                            # Answer choices - flush buffer and add on new line
                            if current_text_parts:
                                problem_lines.append(' '.join(current_text_parts))
                                current_text_parts = []
                            problem_lines.append("")
                            problem_lines.append(paragraph_content)
                        else:
                            # Regular text - add to buffer for potential joining
                            current_text_parts.append(paragraph_content)
                        
            current = current.next_sibling
        
        # Flush any remaining text
        if current_text_parts:
            problem_lines.append(' '.join(current_text_parts))
        
        # Add Solution marker if not found
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
        
        # Filter out copyright footer content
        if ('copyrighted © by the Mathematical Association of America' in line or
            'AMC_logo.png' in line):
            continue
        
        # Clean up HTML entities
        line = line.replace('&nbsp;', ' ')
        line = line.replace('&amp;', '&')
        line = line.replace('&lt;', '<')
        line = line.replace('&gt;', '>')
        
        # Clean up spacing
        line = re.sub(r'\s+', ' ', line)
        
        cleaned_lines.append(line)
    
    # Join and then split again to handle blank line normalization
    result = '\n'.join(cleaned_lines)
    
    # Clean up excessive blank lines
    result = re.sub(r'\n\s*\n\s*\n', '\n\n', result)
    
    return result

def parse_year(year):
    """Parse AMC 8 problems for a specific year."""
    url = f"https://artofproblemsolving.com/wiki/index.php/{year}_AMC_8_Problems"
    
    print(f"Fetching {year} AMC 8 problems...")
    html_content = fetch_page_content(url)
    
    if not html_content:
        print(f"Failed to fetch {year} AMC 8 problems")
        return False
    
    print(f"Extracting problems for {year}...")
    problems_content = extract_problems_polished(html_content)
    
    if not problems_content:
        print(f"Failed to extract problems for {year}")
        return False
    
    cleaned_content = clean_final_output(problems_content)
    
    if not cleaned_content:
        print(f"Failed to clean content for {year}")
        return False
    
    # Save the result
    output_dir = Path("data/raw/AMC8")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{year} AMC 8.md"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"Saved {year} AMC 8 problems to {output_path}")
    
    # Quick stats
    lines = cleaned_content.split('\n')
    problems = [line for line in lines if line.startswith('Problem ')]
    print(f"  Found {len(problems)} problems, {len(lines)} total lines")
    
    return True

def main():
    """Parse AMC 8 problems from 2025 to 1999."""
    print("Starting AMC 8 batch parsing from 2025 to 1999...")

    success_count = 0
    failed_years = []

    # Parse from 2025 down to 1999
    for year in range(2025, 1998, -1):
        try:
            if parse_year(year):
                success_count += 1
            else:
                failed_years.append(year)
        except Exception as e:
            print(f"Error parsing {year}: {e}")
            failed_years.append(year)
        
        # Be nice to the server
        time.sleep(1)
    
    print(f"\nCompleted! Successfully parsed {success_count} years.")
    if failed_years:
        print(f"Failed years: {failed_years}")
    else:
        print("All years parsed successfully!")

if __name__ == "__main__":
    main()