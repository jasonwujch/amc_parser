#!/usr/bin/env python3
"""
AMC 8 Solutions Parser
Systematically parses all solution pages for AMC 8 problems and saves them to structured directories.
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

def extract_solution_content(paragraph):
    """Extract content from a solution paragraph, handling mixed text and elements."""
    if not paragraph:
        return ""
    
    # Check if this paragraph contains only a link (like "See also", "External links", etc.)
    if len(paragraph.contents) == 1 and paragraph.find('a'):
        link = paragraph.find('a')
        if link:
            link_text = link.get_text().strip()
            # Skip navigation links but keep solution-relevant links
            if link_text in ['See also', 'External links', 'Edit this page', 'Discussion']:
                return ""
            return link_text
    
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
                    # Check if this is a LaTeX image
                    is_latex = ('latex' in element.get('class', []) or 
                              (src and 'latex.artofproblemsolving.com' in src))
                    
                    if is_latex:
                        # LaTeX image - use alt text as LaTeX content
                        content_parts.append(alt_text)
                    elif alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                        # ASY diagram - add with proper spacing
                        content_parts.append(f"\n\n{alt_text}\n")
                    else:
                        # Regular image - convert to markdown format
                        if src:
                            if src.startswith('//'):
                                full_url = 'https:' + src
                            elif src.startswith('/'):
                                full_url = 'https://artofproblemsolving.com' + src
                            else:
                                full_url = src
                            content_parts.append(f"\n\n![]({full_url})\n")
                        else:
                            content_parts.append(f"\n\n![]({alt_text})\n")
            
            elif element.name == 'a':
                img_in_link = element.find('img')
                if img_in_link:
                    alt_text = img_in_link.get('alt', '')
                    src = img_in_link.get('src', '')
                    
                    if alt_text:
                        # Check if this is a LaTeX image
                        is_latex = ('latex' in img_in_link.get('class', []) or 
                                  (src and 'latex.artofproblemsolving.com' in src))
                        
                        if is_latex:
                            # LaTeX image - use alt text as LaTeX content
                            content_parts.append(alt_text)
                        elif alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
                            # ASY diagram - add with proper spacing
                            content_parts.append(f"\n\n{alt_text}\n")
                        else:
                            # Regular image - convert to markdown format
                            if src:
                                if src.startswith('//'):
                                    full_url = 'https:' + src
                                elif src.startswith('/'):
                                    full_url = 'https://artofproblemsolving.com' + src
                                else:
                                    full_url = src
                                content_parts.append(f"\n\n![]({full_url})\n")
                            else:
                                content_parts.append(f"\n\n![]({alt_text})\n")
                else:
                    # Regular link text
                    link_text = element.get_text().strip()
                    if link_text:
                        content_parts.append(link_text)
            
            elif element.name in ['strong', 'b', 'em', 'i', 'u']:
                # Preserve text formatting
                text = element.get_text().strip()
                if text:
                    content_parts.append(text)
            
            else:
                # Other elements - extract text content
                text = element.get_text().strip()
                if text:
                    content_parts.append(text)
    
    # Join content and clean up spacing
    content = ' '.join(content_parts)
    content = re.sub(r'\s+', ' ', content)
    return content.strip()

def parse_solution_page(html_content, problem_num, year):
    """Parse a solution page and extract all solution content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the main content
    content_div = soup.find('div', {'class': 'mw-parser-output'}) or soup.find('div', {'id': 'mw-content-text'})
    if not content_div:
        print(f"Could not find main content div for Problem {problem_num}")
        return None
    
    solution_content = []
    solution_content.append(f"# {year} AMC 8 Problem {problem_num}\n")
    
    # First add the Problem section
    solution_content.append("## Problem")
    
    # Look for solution sections - they're typically organized by headers or by direct content
    current_solution = []
    solution_count = 0
    problem_section_added = False
    
    # Process all paragraphs and headers
    for element in content_div.find_all(['p', 'h2', 'h3', 'h4', 'div']):
        if element.name in ['h2', 'h3', 'h4']:
            header_text = element.get_text().strip()
            
            # Skip navigation headers
            if header_text in ['Contents', 'Navigation', 'See also', 'External links']:
                continue
                
            # If we find a solution-related header, finalize previous content
            if 'solution' in header_text.lower() or header_text.startswith('Solution'):
                if current_solution and problem_section_added:
                    solution_content.append('\n'.join(current_solution))
                    solution_content.append("")  # Add blank line between sections
                elif current_solution and not problem_section_added:
                    # This was problem content, add it to problem section
                    solution_content.extend(current_solution)
                    solution_content.append("")
                    problem_section_added = True
                
                solution_count += 1
                current_solution = [f"## {header_text}"]
                
            elif header_text and current_solution:
                # Other headers within a section
                current_solution.append(f"### {header_text}")
        
        elif element.name == 'p':
            paragraph_content = extract_solution_content(element)
            if paragraph_content:
                if not current_solution and solution_count == 0 and not problem_section_added:
                    # First content without a header - this is problem content
                    current_solution = [paragraph_content]
                elif not current_solution and solution_count == 0 and problem_section_added:
                    # First solution content without a header - assume it's Solution 1
                    solution_count = 1
                    current_solution = ["## Solution 1", paragraph_content]
                else:
                    current_solution.append(paragraph_content)
        
        elif element.name == 'div':
            # Handle special divs (like math displays)
            div_content = extract_solution_content(element)
            if div_content and current_solution:
                current_solution.append(div_content)
    
    # Add the final content
    if current_solution:
        if not problem_section_added:
            # This was problem content
            solution_content.extend(current_solution)
            solution_content.append("")
        else:
            # This was solution content
            solution_content.append('\n'.join(current_solution))
    
    # If no solutions found, add all remaining content as one solution
    if solution_count == 0 and problem_section_added:
        solution_content.append("## Solution")
        for element in content_div.find_all('p'):
            paragraph_content = extract_solution_content(element)
            if paragraph_content:
                solution_content.append(paragraph_content)
    
    return '\n\n'.join(solution_content)

def clean_solution_content(content):
    """Clean up the solution content."""
    if not content:
        return None
    
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip lines that are clearly navigation or metadata
        if (line.strip() in ['Navigation', 'Contents', 'See also', 'External links', 'Edit this page'] or
            'AMC_logo.png' in line or
            'navigation' in line.lower()):
            continue
        
        # Clean up HTML entities
        line = line.replace('&nbsp;', ' ')
        line = line.replace('&amp;', '&')
        line = line.replace('&lt;', '<')
        line = line.replace('&gt;', '>')
        
        # Clean up spacing
        line = re.sub(r'\s+', ' ', line)
        
        cleaned_lines.append(line)
    
    # Join and normalize blank lines
    result = '\n'.join(cleaned_lines)
    result = re.sub(r'\n\s*\n\s*\n', '\n\n', result)
    
    return result

def create_directory_structure(base_path, year):
    """Create the directory structure for solutions."""
    solutions_dir = Path(base_path) / f"AMC8/{year} AMC 8/solutions"
    solutions_dir.mkdir(parents=True, exist_ok=True)
    return solutions_dir

def parse_all_solutions(year):
    """Parse all solution pages for a given year."""
    base_url = f"https://artofproblemsolving.com/wiki/index.php/{year}_AMC_8_Problems/Problem_"
    
    # Create directory structure
    solutions_dir = create_directory_structure("data/raw", year)
    
    print(f"Parsing {year} AMC 8 solutions...")
    print(f"Solutions will be saved to: {solutions_dir}")
    
    success_count = 0
    failed_problems = []
    
    for problem_num in range(1, 26):  # Problems 1-25
        print(f"\nProcessing Problem {problem_num}...")
        
        # Construct solution page URL
        solution_url = f"{base_url}{problem_num}"
        
        # Fetch solution page
        html_content = fetch_page_content(solution_url)
        if not html_content:
            print(f"Failed to fetch Problem {problem_num} solution page")
            failed_problems.append(problem_num)
            continue
        
        # Parse solution content
        solution_content = parse_solution_page(html_content, problem_num, year)
        if not solution_content:
            print(f"Failed to parse Problem {problem_num} solution")
            failed_problems.append(problem_num)
            continue
        
        # Clean content
        cleaned_content = clean_solution_content(solution_content)
        if not cleaned_content:
            print(f"No valid content found for Problem {problem_num}")
            failed_problems.append(problem_num)
            continue
        
        # Save solution file directly in solutions directory
        solution_file = solutions_dir / f"{year}_amc_8_solution_p{problem_num}.md"
        with open(solution_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"✓ Saved solution to {solution_file}")
        success_count += 1
        
        # Be respectful to the server
        time.sleep(1)
    
    print(f"\n=== Summary ===")
    print(f"Successfully parsed: {success_count}/25 solutions")
    if failed_problems:
        print(f"Failed problems: {failed_problems}")
    else:
        print("All solutions parsed successfully!")
    
    return success_count, failed_problems

def parse_multiple_years(start_year, end_year):
    """Parse solutions for multiple years."""
    total_success = 0
    total_problems = 0
    year_summaries = []
    
    for year in range(start_year, end_year + 1):
        print(f"\n{'='*50}")
        print(f"Starting {year} AMC 8")
        print(f"{'='*50}")
        
        success_count, failed_problems = parse_all_solutions(year)
        total_success += success_count
        total_problems += 25
        
        year_summaries.append({
            'year': year,
            'success': success_count,
            'failed': failed_problems
        })
        
        # Brief pause between years
        print(f"\nCompleted {year}. Pausing before next year...")
        time.sleep(2)
    
    # Overall summary
    print(f"\n{'='*60}")
    print(f"OVERALL SUMMARY ({start_year}-{end_year})")
    print(f"{'='*60}")
    print(f"Total problems parsed: {total_success}/{total_problems}")
    print(f"Success rate: {total_success/total_problems*100:.1f}%")
    
    print(f"\nYear-by-year breakdown:")
    for summary in year_summaries:
        year = summary['year']
        success = summary['success']
        failed = summary['failed']
        status = "✅" if success == 25 else f"⚠️ ({len(failed)} failed)"
        print(f"  {year}: {success}/25 {status}")
        if failed:
            print(f"    Failed problems: {failed}")

def main():
    """Main function to parse AMC 8 solutions for all years 1999-2024."""
    print("AMC 8 Solution Parser - Multi-Year Edition")
    print("This will parse solutions for AMC 8 from 1999 to 2024")
    
    parse_multiple_years(1999, 2024)

if __name__ == "__main__":
    main()