#!/usr/bin/env python3
"""Debug script for Problem 16 parsing issue."""

import requests
from bs4 import BeautifulSoup, NavigableString
import re

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

def debug_problem16():
    url = "https://artofproblemsolving.com/wiki/index.php/2023_AMC_8_Problems"
    
    print("Fetching webpage content...")
    html_content = fetch_page_content(url)
    
    if not html_content:
        print("Failed to fetch webpage content")
        return
    
    soup = BeautifulSoup(html_content, 'html.parser')
    content_div = soup.find('div', {'class': 'mw-parser-output'}) or soup.find('div', {'id': 'mw-content-text'})
    
    # Find Problem 16 header
    problem_headers = content_div.find_all(['h2', 'h3'])
    
    for header in problem_headers:
        header_text = header.get_text().strip()
        problem_match = re.match(r'Problem (\d+)', header_text)
        if problem_match and problem_match.group(1) == '16':
            print(f"\nFound Problem 16 header: {header_text}")
            
            # Now examine all content after this header
            current = header.next_sibling
            paragraph_count = 0
            
            while current:
                if hasattr(current, 'name'):
                    # Stop if we hit another problem header
                    if current.name in ['h2', 'h3']:
                        next_header_text = current.get_text().strip()
                        if re.match(r'Problem \d+', next_header_text):
                            print(f"\nStopped at next problem: {next_header_text}")
                            break
                    
                    # Process paragraphs
                    if current.name == 'p':
                        paragraph_count += 1
                        print(f"\n=== PARAGRAPH {paragraph_count} ===")
                        print(f"Raw HTML: {str(current)[:200]}...")
                        
                        paragraph_text = current.get_text().strip()
                        print(f"Text content: {paragraph_text}")
                        
                        # Check for images
                        images = current.find_all('img')
                        if images:
                            print(f"Found {len(images)} images:")
                            for i, img in enumerate(images):
                                src = img.get('src', '')
                                alt = img.get('alt', '')
                                print(f"  Image {i+1}: src='{src[:50]}...', alt='{alt[:50]}...'")
                                
                                # Check if LaTeX
                                is_latex = ('latex' in img.get('class', []) or 
                                          (src and 'latex.artofproblemsolving.com' in src))
                                print(f"    LaTeX? {is_latex}")
                        
                        # Check for links containing images
                        links_with_images = current.find_all('a')
                        for link in links_with_images:
                            img_in_link = link.find('img')
                            if img_in_link:
                                src = img_in_link.get('src', '')
                                alt = img_in_link.get('alt', '')
                                print(f"  Link->Image: src='{src[:50]}...', alt='{alt[:50]}...'")
                                
                                is_latex = ('latex' in img_in_link.get('class', []) or 
                                          (src and 'latex.artofproblemsolving.com' in src))
                                print(f"    LaTeX? {is_latex}")
                        
                current = current.next_sibling
            
            break
    else:
        print("Problem 16 not found!")

if __name__ == "__main__":
    debug_problem16()