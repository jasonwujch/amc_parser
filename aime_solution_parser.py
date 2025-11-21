#!/usr/bin/env python3
"""
AIME Solutions Parser
- Parses solutions for AIME I and II (2010-2025)
- Smart resume: checks existing files and skips them
- Progress tracking
"""

import requests
from bs4 import BeautifulSoup, NavigableString
import re
from pathlib import Path
import time

# Configuration
START_YEAR = 2010
END_YEAR = 2025
PROBLEMS_PER_CONTEST = 15
VARIANTS = ['I', 'II']

def fetch_page_content(url, max_retries=3):
    """Fetch the webpage content with retry logic."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** (attempt + 1)  # 2, 4 seconds
                print(f"  Retry {attempt + 1}/{max_retries} after {wait_time}s: {e}")
                time.sleep(wait_time)
            else:
                print(f"  Error fetching page after {max_retries} attempts: {e}")
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

def parse_solution_page(html_content, problem_num, year, variant):
    """Parse a solution page and extract all solution content."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the main content
    content_div = soup.find('div', {'class': 'mw-parser-output'}) or soup.find('div', {'id': 'mw-content-text'})
    if not content_div:
        print(f"  Could not find main content div for Problem {problem_num}")
        return None

    solution_content = []
    solution_content.append(f"# {year} AIME {variant} Problem {problem_num}\n")

    # First add the Problem section
    solution_content.append("## Problem")

    # Look for solution sections - they're typically organized by headers or by direct content
    current_solution = []
    solution_count = 0
    problem_section_added = False

    # Process all paragraphs and headers
    for element in content_div.find_all(['p', 'h2', 'h3', 'h4', 'div', 'ul', 'ol']):
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

        elif element.name in ['ul', 'ol']:
            # Handle lists (common in AIME solutions)
            list_items = []
            for li in element.find_all('li', recursive=False):
                li_content = extract_solution_content(li)
                if li_content:
                    prefix = "-" if element.name == 'ul' else "1."
                    list_items.append(f"{prefix} {li_content}")
            if list_items and current_solution:
                current_solution.extend(list_items)

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
            'AIME_logo.png' in line or
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

def create_directory_structure(base_path, year, variant):
    """Create the directory structure for solutions."""
    solutions_dir = Path(base_path) / f"AIME/{year} AIME {variant}/solutions"
    solutions_dir.mkdir(parents=True, exist_ok=True)
    return solutions_dir

def check_existing_files(base_path):
    """Check which solution files already exist."""
    existing_files = {}
    aime_dir = Path(base_path) / "AIME"

    if not aime_dir.exists():
        return existing_files

    for year_dir in aime_dir.iterdir():
        if year_dir.is_dir() and "AIME" in year_dir.name:
            # Extract year and variant from directory name like "2010 AIME I"
            match = re.match(r'(\d{4}) AIME (I{1,2})', year_dir.name)
            if match:
                year = int(match.group(1))
                variant = match.group(2)
                key = (year, variant)

                solutions_dir = year_dir / "solutions"

                if solutions_dir.exists():
                    existing_files[key] = set()
                    for solution_file in solutions_dir.glob(f"{year}_aime_{variant.lower()}_solution_p*.md"):
                        # Extract problem number from filename
                        problem_match = re.search(r'p(\d+)\.md$', solution_file.name)
                        if problem_match:
                            problem_num = int(problem_match.group(1))
                            existing_files[key].add(problem_num)

    return existing_files

def analyze_progress(existing_files):
    """Analyze current progress and determine what needs to be done."""
    print("=== CURRENT PROGRESS ANALYSIS ===")

    total_existing = 0
    total_missing = 0
    incomplete_contests = []
    missing_contests = []

    for year in range(START_YEAR, END_YEAR + 1):
        for variant in VARIANTS:
            key = (year, variant)
            contest_name = f"{year} AIME {variant}"

            if key in existing_files:
                existing_count = len(existing_files[key])
                missing_count = PROBLEMS_PER_CONTEST - existing_count
                total_existing += existing_count
                total_missing += missing_count

                if existing_count == PROBLEMS_PER_CONTEST:
                    print(f"  {contest_name}: Complete ({PROBLEMS_PER_CONTEST}/{PROBLEMS_PER_CONTEST})")
                else:
                    print(f"  {contest_name}: Incomplete ({existing_count}/{PROBLEMS_PER_CONTEST})")
                    missing_problems = set(range(1, PROBLEMS_PER_CONTEST + 1)) - existing_files[key]
                    incomplete_contests.append((year, variant, missing_problems))
            else:
                print(f"  {contest_name}: Not started (0/{PROBLEMS_PER_CONTEST})")
                total_missing += PROBLEMS_PER_CONTEST
                missing_contests.append((year, variant))

    total_problems = (END_YEAR - START_YEAR + 1) * len(VARIANTS) * PROBLEMS_PER_CONTEST
    print(f"\nOVERALL SUMMARY:")
    print(f"  Total existing: {total_existing}/{total_problems}")
    print(f"  Total missing: {total_missing}")
    if total_existing + total_missing > 0:
        print(f"  Completion: {total_existing/(total_existing+total_missing)*100:.1f}%")

    return incomplete_contests, missing_contests

def parse_missing_problems(year, variant, missing_problems, base_path):
    """Parse only the missing problems for a given contest."""
    base_url = f"https://artofproblemsolving.com/wiki/index.php/{year}_AIME_{variant}_Problems/Problem_"
    solutions_dir = create_directory_structure(base_path, year, variant)

    print(f"\nParsing {year} AIME {variant} ({len(missing_problems)} problems)")

    success_count = 0
    failed_problems = []

    for problem_num in sorted(missing_problems):
        solution_file = solutions_dir / f"{year}_aime_{variant.lower()}_solution_p{problem_num}.md"

        # Double check if file exists
        if solution_file.exists():
            print(f"  Skipping Problem {problem_num} (already exists)")
            continue

        # Construct solution page URL
        solution_url = f"{base_url}{problem_num}"

        # Fetch solution page
        html_content = fetch_page_content(solution_url)
        if not html_content:
            print(f"  Failed to fetch Problem {problem_num}")
            failed_problems.append(problem_num)
            continue

        # Parse solution content
        solution_content = parse_solution_page(html_content, problem_num, year, variant)
        if not solution_content:
            print(f"  Failed to parse Problem {problem_num}")
            failed_problems.append(problem_num)
            continue

        # Clean content
        cleaned_content = clean_solution_content(solution_content)
        if not cleaned_content:
            print(f"  No valid content for Problem {problem_num}")
            failed_problems.append(problem_num)
            continue

        # Save solution file
        with open(solution_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print(f"  Saved Problem {problem_num}")
        success_count += 1

        # Be respectful to the server
        time.sleep(0.5)

    return success_count, failed_problems

def parse_complete_contest(year, variant, base_path):
    """Parse all 15 problems for a contest that hasn't been started."""
    return parse_missing_problems(year, variant, set(range(1, PROBLEMS_PER_CONTEST + 1)), base_path)

def main():
    """Main function with smart resume capability."""
    print("AIME Solution Parser")
    print(f"Years: {START_YEAR}-{END_YEAR} | Variants: {', '.join(VARIANTS)}")
    print(f"Total contests: {(END_YEAR - START_YEAR + 1) * len(VARIANTS)}")
    print(f"Total problems: {(END_YEAR - START_YEAR + 1) * len(VARIANTS) * PROBLEMS_PER_CONTEST}")
    print("\nAnalyzing existing files...\n")

    base_path = "data/raw"
    existing_files = check_existing_files(base_path)
    incomplete_contests, missing_contests = analyze_progress(existing_files)

    if not incomplete_contests and not missing_contests:
        print("\nAll AIME solutions are already complete!")
        return

    print(f"\nWORK TO BE DONE:")
    if incomplete_contests:
        print(f"  Incomplete contests: {len(incomplete_contests)}")
    if missing_contests:
        print(f"  Missing contests: {len(missing_contests)}")

    print("\nStarting parsing...\n")

    total_success = 0
    total_attempted = 0
    all_failed = []

    # First, complete incomplete contests
    for year, variant, missing_problems in incomplete_contests:
        success_count, failed_problems = parse_missing_problems(year, variant, missing_problems, base_path)
        total_success += success_count
        total_attempted += len(missing_problems)
        if failed_problems:
            all_failed.extend([(year, variant, p) for p in failed_problems])
        time.sleep(1)

    # Then, start missing contests
    for year, variant in missing_contests:
        success_count, failed_problems = parse_complete_contest(year, variant, base_path)
        total_success += success_count
        total_attempted += PROBLEMS_PER_CONTEST
        if failed_problems:
            all_failed.extend([(year, variant, p) for p in failed_problems])
        time.sleep(1)

    print(f"\n{'='*60}")
    print(f"FINAL SUMMARY")
    print(f"{'='*60}")
    print(f"Total problems attempted: {total_attempted}")
    print(f"Total problems successfully parsed: {total_success}")
    if total_attempted > 0:
        print(f"Success rate: {total_success/total_attempted*100:.1f}%")

    if all_failed:
        print(f"\nFailed problems ({len(all_failed)}):")
        for year, variant, prob in all_failed:
            print(f"  - {year} AIME {variant} Problem {prob}")
    else:
        print("\nAll AIME solutions parsed successfully!")

if __name__ == "__main__":
    main()
