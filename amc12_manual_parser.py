#!/usr/bin/env python3
"""
AMC 12 Manual Parser - Parse locally saved HTML files
Instructions:
1. Manually save AMC 12 problem pages from AoPS to data/html/AMC12/
2. Run this script to parse them into markdown format
"""

from bs4 import BeautifulSoup, NavigableString
import re
from pathlib import Path
import os

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

def parse_html_file(html_path, output_name):
    """Parse a single HTML file."""
    print(f"Processing {html_path.name}...")
    
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        print(f"  Error reading file: {e}")
        return False
    
    problems_content = extract_problems_polished(html_content)
    
    if not problems_content:
        print(f"  Failed to extract problems")
        return False
    
    cleaned_content = clean_final_output(problems_content)
    
    if not cleaned_content:
        print(f"  Failed to clean content")
        return False
    
    # Save the result
    output_dir = Path("data/raw/AMC12")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{output_name}.md"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"  ✓ Saved to {output_path}")
    
    # Quick stats
    lines = cleaned_content.split('\n')
    problems = [line for line in lines if line.startswith('Problem ')]
    print(f"    Found {len(problems)} problems, {len(lines)} total lines")
    
    return True

def main():
    """Parse locally saved AMC 12 HTML files."""
    print("=" * 60)
    print("AMC 12 Manual Parser")
    print("=" * 60)
    print("\nInstructions:")
    print("1. Create directory: data/html/AMC12/")
    print("2. Save AMC 12 problem pages from AoPS as HTML files:")
    print("   - Name format: YYYY_AMC_12X.html (e.g., 2024_AMC_12A.html)")
    print("   - Or: YYYY_AMC_12.html for single versions (2000-2001)")
    print("3. Run this script to parse them\n")
    
    # Check for HTML directory
    html_dir = Path("data/html/AMC12")
    
    if not html_dir.exists():
        print(f"Creating directory: {html_dir}")
        html_dir.mkdir(parents=True, exist_ok=True)
        print("\nPlease save HTML files to this directory and run again.")
        print("\nExample URLs to save:")
        print("  https://artofproblemsolving.com/wiki/index.php/2024_AMC_12A_Problems")
        print("  https://artofproblemsolving.com/wiki/index.php/2024_AMC_12B_Problems")
        print("  https://artofproblemsolving.com/wiki/index.php/2023_AMC_12A_Problems")
        print("  https://artofproblemsolving.com/wiki/index.php/2023_AMC_12B_Problems")
        print("\nSave as: 2024_AMC_12A.html, 2024_AMC_12B.html, etc.")
        return
    
    # Find all HTML files
    html_files = list(html_dir.glob("*.html"))
    
    if not html_files:
        print(f"No HTML files found in {html_dir}")
        print("\nPlease save AMC 12 problem pages as HTML files.")
        print("\nExample process:")
        print("1. Open https://artofproblemsolving.com/wiki/index.php/2024_AMC_12A_Problems")
        print("2. Save page as HTML (Ctrl+S or Cmd+S)")
        print("3. Save to: data/html/AMC12/2024_AMC_12A.html")
        return
    
    print(f"Found {len(html_files)} HTML file(s) to process\n")
    
    success_count = 0
    failed_files = []
    
    for html_file in sorted(html_files):
        # Extract year and variant from filename
        filename = html_file.stem  # e.g., "2024_AMC_12A"
        
        # Parse the file
        if parse_html_file(html_file, filename):
            success_count += 1
        else:
            failed_files.append(html_file.name)
    
    print("\n" + "=" * 60)
    print(f"Completed! Successfully parsed {success_count}/{len(html_files)} files.")
    
    if failed_files:
        print(f"\nFailed files:")
        for file in failed_files:
            print(f"  - {file}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()