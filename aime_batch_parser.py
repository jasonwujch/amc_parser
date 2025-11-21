#!/usr/bin/env python3
"""
AIME Batch Parser - Parse AIME problems from ArtOfProblemSolving.com
Handles both AIME I and AIME II variants (2010-2025)
"""

import requests
from bs4 import BeautifulSoup, NavigableString
import re
from pathlib import Path
import time
import random

def fetch_page_content(url, retry_count=5):
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
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
        }

        session = requests.Session()

        try:
            if attempt > 0:
                # Exponential backoff: 5, 10, 20, 40, 80 seconds
                delay = min(5 * (2 ** attempt), 80) + random.uniform(0, 5)
                print(f"  Retry {attempt + 1}/{retry_count} after {delay:.1f}s delay...")
                time.sleep(delay)

            response = session.get(url, headers=headers, timeout=30, allow_redirects=True)

            if response.status_code == 200:
                # Accept valid HTML responses
                if len(response.text) > 5000:  # Real pages are large
                    return response.text
                else:
                    print(f"  Got 200 but page too small ({len(response.text)} bytes) (attempt {attempt + 1}/{retry_count})")
                    continue
            elif response.status_code == 403:
                print(f"  Received 403 Forbidden (attempt {attempt + 1}/{retry_count})")
                continue
            elif response.status_code == 503:
                print(f"  Received 503 Service Unavailable (attempt {attempt + 1}/{retry_count})")
                continue
            else:
                print(f"  Received {response.status_code} (attempt {attempt + 1}/{retry_count})")
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

    # Find the main content - use class_ parameter for proper matching
    content_div = soup.find('div', class_='mw-parser-output')
    if not content_div:
        content_div = soup.find('div', {'id': 'mw-content-text'})
    if not content_div:
        # Try finding by partial class match
        for div in soup.find_all('div'):
            classes = div.get('class', [])
            if classes and 'mw-parser-output' in classes:
                content_div = div
                break

    if not content_div:
        print("  Could not find main content div")
        if 'please verify' in html_content.lower() or 'captcha' in html_content.lower():
            print("  Detected anti-bot protection page")
        return None

    # Verify this is actually a problem page
    if 'Problem 1' not in html_content:
        print("  Page doesn't contain 'Problem 1' - may not be the correct page")
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
                        # AIME doesn't have answer choices like AMC, so just add text
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

        if ('copyrighted' in line.lower() or
            'AMC_logo.png' in line or
            'AIME_logo.png' in line):
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

def parse_aime_variant(year, variant):
    """Parse AIME problems for a specific year and variant (I or II)."""
    url = f"https://artofproblemsolving.com/wiki/index.php/{year}_AIME_{variant}_Problems"
    name = f"{year} AIME {variant}"

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
    output_dir = Path("data/raw/AIME")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{name}.md"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    print(f"  Saved {name} problems to {output_path}")

    # Quick stats
    lines = cleaned_content.split('\n')
    problems = [line for line in lines if line.startswith('Problem ')]
    print(f"    Found {len(problems)} problems, {len(lines)} total lines")

    return True

def main():
    """Parse AIME problems from 2010 to 2025."""
    print("=" * 60)
    print("AIME Batch Parser")
    print("Parsing AIME I and AIME II from 2010 to 2025")
    print("=" * 60)

    success_count = 0
    failed_items = []

    # Years to parse: 2010-2025
    start_year = 2010
    end_year = 2025

    # Wait for any rate limiting to clear
    print("\nWaiting 15s for rate limit to clear...")
    time.sleep(15)

    # Test connection first
    print("\nTesting connection...")
    if parse_aime_variant(2024, 'I'):
        success_count += 1
        print("  Connection successful!")
    else:
        print("  Initial test failed, waiting 30s before continuing...")
        time.sleep(30)

    print("\n" + "-" * 40)
    print("Starting full download...")
    print("-" * 40)

    # Parse all years
    for year in range(end_year, start_year - 1, -1):
        for variant in ['I', 'II']:
            # Skip if already parsed in test
            if year == 2024 and variant == 'I':
                continue

            try:
                # Longer delays to avoid rate limiting
                delay = random.uniform(8, 15)
                print(f"  Waiting {delay:.1f}s before next request...")
                time.sleep(delay)

                if parse_aime_variant(year, variant):
                    success_count += 1
                else:
                    failed_items.append(f"{year} AIME {variant}")
            except Exception as e:
                print(f"  Error parsing {year} AIME {variant}: {e}")
                failed_items.append(f"{year} AIME {variant}")

    print("\n" + "=" * 60)
    print(f"Completed! Successfully parsed {success_count} AIME exams.")
    if failed_items:
        print(f"\nFailed items ({len(failed_items)}):")
        for item in failed_items:
            print(f"  - {item}")
    else:
        print("All items parsed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
