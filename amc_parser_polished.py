#!/usr/bin/env python3
"""
AMC 8 Problems Parser - Polished Final Version

This script creates output that closely matches the manual copy-paste result
by properly handling text flow and LaTeX formatting.
"""

import requests
from bs4 import BeautifulSoup, NavigableString
import re
from pathlib import Path

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
    has_answer_choices = False
    
    for element in paragraph.contents:
        if isinstance(element, NavigableString):
            if str(element).strip():
                has_text = True
        elif hasattr(element, 'name'):
            if element.name == 'img':
                alt_text = element.get('alt', '')
                if alt_text and alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                    has_asy = True
                elif alt_text and '\\textbf{(' in alt_text and ('qquad' in alt_text or 'text{ ' in alt_text):
                    has_answer_choices = True
                elif not ('latex' in element.get('class', [])):
                    has_regular_images = True
            elif element.name == 'a' and element.find('img'):
                img = element.find('img')
                alt_text = img.get('alt', '')
                if alt_text and alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                    has_asy = True
                elif alt_text and '\\textbf{(' in alt_text and ('qquad' in alt_text or 'text{ ' in alt_text):
                    has_answer_choices = True
                elif not ('latex' in img.get('class', [])):
                    has_regular_images = True
    
    # Special case: if paragraph has ASY + text + answer choices, split them up
    if has_asy and (has_text or has_answer_choices):
        result_parts = []
        
        # First, extract all non-ASY content
        text_parts = []
        answer_parts = []
        asy_parts = []
        
        for element in paragraph.contents:
            if isinstance(element, NavigableString):
                text = str(element).strip()
                if text:
                    text_parts.append(text)
            elif hasattr(element, 'name'):
                if element.name == 'img':
                    alt_text = element.get('alt', '')
                    src = element.get('src', '')
                    
                    if alt_text and alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                        asy_parts.append(f"\n\n{alt_text}\n")
                    elif alt_text and '\\textbf{(' in alt_text and ('qquad' in alt_text or 'text{ ' in alt_text):
                        answer_parts.append(alt_text)
                    elif alt_text:
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
                                result_parts.append(f"![]({full_url})")
                            else:
                                result_parts.append(f"![]({alt_text})")
                elif element.name == 'a':
                    img_in_link = element.find('img')
                    if img_in_link:
                        alt_text = img_in_link.get('alt', '')
                        src = img_in_link.get('src', '')
                        
                        if alt_text and alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                            asy_parts.append(f"\n\n{alt_text}\n")
                        elif alt_text and '\\textbf{(' in alt_text and ('qquad' in alt_text or 'text{ ' in alt_text):
                            answer_parts.append(alt_text)
                        elif alt_text:
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
                                    result_parts.append(f"![]({full_url})")
                                else:
                                    result_parts.append(f"![]({alt_text})")
                    else:
                        text = element.get_text().strip()
                        if text:
                            text_parts.append(text)
        
        # Return special format indicating this needs to be split
        return {
            'type': 'complex_mixed',
            'text': ' '.join(text_parts) if text_parts else '',
            'asy': asy_parts,
            'answers': answer_parts,
            'images': result_parts
        }
    
    # If paragraph has ASY only, return it immediately on its own lines with extra spacing
    if has_asy and not has_text and not has_answer_choices:
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
                    
                    # Handle complex mixed content (Problem 16 type case)
                    if isinstance(paragraph_content, dict) and paragraph_content.get('type') == 'complex_mixed':
                        # Flush any buffered text first
                        if current_text_parts:
                            problem_lines.append(' '.join(current_text_parts))
                            current_text_parts = []
                        
                        # Add the problem statement text
                        if paragraph_content['text']:
                            problem_lines.append(paragraph_content['text'])
                        
                        # Add ASY diagrams
                        for asy in paragraph_content['asy']:
                            problem_lines.append(asy.strip())
                        
                        # Add answer choices with proper spacing
                        if paragraph_content['answers']:
                            problem_lines.append("")
                            # Join all answer choices on one line
                            problem_lines.append(' '.join(paragraph_content['answers']))
                        
                        # Add any images
                        for img in paragraph_content['images']:
                            problem_lines.append(img)
                    
                    elif paragraph_content.strip() == 'Solution':
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
                        # Check if this looks like answer choices (multi-choice format)
                        if '\\textbf{(' in paragraph_content and 'qquad' in paragraph_content:
                            # Answer choices - flush buffer and add on new line
                            if current_text_parts:
                                problem_lines.append(' '.join(current_text_parts))
                                current_text_parts = []
                            problem_lines.append("")
                            problem_lines.append(paragraph_content)
                        # Check if this is a single answer choice (Problem 16 format)
                        elif '\\textbf{(' in paragraph_content and 'text{ ' in paragraph_content:
                            # Single answer choice - add to buffer to collect with others
                            current_text_parts.append(paragraph_content)
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

def main():
    url = "https://artofproblemsolving.com/wiki/index.php/2023_AMC_8_Problems"
    sample_path = "data/raw/AMC8/2023 AMC 8.md"
    
    print("Fetching webpage content...")
    html_content = fetch_page_content(url)
    
    if not html_content:
        print("Failed to fetch webpage content")
        return
    
    print("Extracting problems with polished formatting...")
    problems_content = extract_problems_polished(html_content)
    
    if problems_content:
        cleaned_content = clean_final_output(problems_content)
        
        # Save the result
        output_path = Path("amc8_2023_debug.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"Polished content saved to {output_path}")
        
        # Quick comparison
        try:
            with open(sample_path, 'r', encoding='utf-8') as f:
                sample_content = f.read()
            
            gen_lines = cleaned_content.split('\n')
            sample_lines = sample_content.split('\n')
            
            print(f"Generated: {len(gen_lines)} lines")
            print(f"Sample: {len(sample_lines)} lines")
            
            # Check structure similarity by looking at Problem headers
            gen_problems = [line for line in gen_lines if line.startswith('Problem ')]
            sample_problems = [line for line in sample_lines if line.startswith('Problem ')]
            
            print(f"Problems found - Generated: {len(gen_problems)}, Sample: {len(sample_problems)}")
            
        except FileNotFoundError:
            print("Sample file not found for comparison")
        
        # Show preview
        print(f"\nFirst 1000 characters:\n{cleaned_content[:1000]}...")
        
    else:
        print("Failed to extract content")

if __name__ == "__main__":
    main()