#!/usr/bin/env python3
"""
AMC10 Answer Key Parser - Parse AMC10 answer keys from ArtOfProblemSolving.com
Handles AMC 10A and 10B variants (2002-2025), including 2021 Fall variants
Answers are letters A-E (multiple choice)
"""

import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path
import time
import random
import json

# Configuration
START_YEAR = 2002
END_YEAR = 2025
PROBLEMS_PER_CONTEST = 25

def get_contest_variants(year):
    """Get the list of contest variants for a given year."""
    if year == 2021:
        return ['A', 'B', 'Fall_A', 'Fall_B']
    else:
        return ['A', 'B']

def get_url_for_variant(year, variant):
    """Get the answer key URL for a specific contest variant."""
    if variant.startswith('Fall_'):
        letter = variant.replace('Fall_', '')
        return f"https://artofproblemsolving.com/wiki/index.php/{year}_Fall_AMC_10{letter}_Answer_Key"
    else:
        return f"https://artofproblemsolving.com/wiki/index.php/{year}_AMC_10{variant}_Answer_Key"

def get_display_name(year, variant):
    """Get the display name for a contest variant."""
    if variant.startswith('Fall_'):
        letter = variant.replace('Fall_', '')
        return f"{year} Fall AMC 10{letter}"
    else:
        return f"{year} AMC 10{variant}"

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
                delay = min(5 * (2 ** attempt), 80) + random.uniform(0, 5)
                print(f"  Retry {attempt + 1}/{retry_count} after {delay:.1f}s delay...")
                time.sleep(delay)

            response = session.get(url, headers=headers, timeout=30, allow_redirects=True)

            if response.status_code == 200:
                if len(response.text) > 1000:
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


def extract_answers(html_content):
    """Extract answer key from the HTML content. Answers are letters A-E."""
    soup = BeautifulSoup(html_content, 'html.parser')

    content_div = soup.find('div', class_='mw-parser-output')
    if not content_div:
        content_div = soup.find('div', {'id': 'mw-content-text'})
    if not content_div:
        for div in soup.find_all('div'):
            classes = div.get('class', [])
            if classes and 'mw-parser-output' in classes:
                content_div = div
                break

    if not content_div:
        print("  Could not find main content div")
        return None

    answers = []

    # Method 1: Look for ordered list (ol) with answers
    ol = content_div.find('ol')
    if ol:
        for li in ol.find_all('li'):
            text = li.get_text().strip()
            # Extract letter answer (A-E)
            match = re.match(r'^([A-Ea-e])\b', text)
            if match:
                answers.append(match.group(1).upper())

    # Method 2: Look for list items with various formats
    if len(answers) < PROBLEMS_PER_CONTEST:
        answers = []
        for li in content_div.find_all('li'):
            text = li.get_text().strip()
            # Look for patterns like "1. A" or "Problem 1: B" or just "A"
            match = re.search(r'(?:Problem\s+\d+[:\s]+)?([A-Ea-e])(?:\s|$)', text)
            if match:
                answers.append(match.group(1).upper())

    # Method 3: Parse from paragraphs or text content
    if len(answers) < PROBLEMS_PER_CONTEST:
        answers = []
        text = content_div.get_text()
        # Look for numbered list pattern: "1. A" or "1) B" etc
        matches = re.findall(r'(?:^|\n)\s*\d+[.):\s]+([A-Ea-e])(?:\s|$|\n)', text)
        if matches:
            answers = [m.upper() for m in matches]

    # Method 4: Look for table format
    if len(answers) < PROBLEMS_PER_CONTEST:
        answers = []
        tables = content_div.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all(['td', 'th'])
                for cell in cells:
                    text = cell.get_text().strip()
                    if text.upper() in ['A', 'B', 'C', 'D', 'E']:
                        answers.append(text.upper())

    # Method 5: Look for any sequence of letters that look like answers
    if len(answers) < PROBLEMS_PER_CONTEST:
        answers = []
        text = content_div.get_text()
        # Find all standalone letters A-E
        all_letters = re.findall(r'\b([A-Ea-e])\b', text)
        potential_answers = [l.upper() for l in all_letters if l.upper() in ['A', 'B', 'C', 'D', 'E']]
        # Try to find a sequence of 25 answers
        if len(potential_answers) >= PROBLEMS_PER_CONTEST:
            # Skip problem numbering references, try to find actual answers
            for start_idx in range(len(potential_answers) - PROBLEMS_PER_CONTEST + 1):
                candidate = potential_answers[start_idx:start_idx + PROBLEMS_PER_CONTEST]
                # Check variety - real answers should have mix of letters
                if len(set(candidate)) >= 3:  # At least 3 different letters
                    answers = candidate
                    break

    if len(answers) == PROBLEMS_PER_CONTEST:
        return answers
    elif len(answers) > 0:
        print(f"  Warning: Found {len(answers)} answers instead of expected {PROBLEMS_PER_CONTEST}")
        return answers if len(answers) >= 20 else None

    return None


def parse_amc10_answers(year, variant):
    """Parse AMC10 answer key for a specific year and variant."""
    url = get_url_for_variant(year, variant)
    name = get_display_name(year, variant)

    print(f"\nFetching {name} answer key...")
    html_content = fetch_page_content(url)

    if not html_content:
        print(f"  Failed to fetch {name} answer key")
        return None

    print(f"  Extracting answers for {name}...")
    answers = extract_answers(html_content)

    if not answers:
        print(f"  Failed to extract answers for {name}")
        return None

    print(f"  Found {len(answers)} answers: {', '.join(answers[:5])}...")
    return answers


def main():
    """Parse AMC10 answer keys from 2002 to 2025."""
    print("=" * 60)
    print("AMC10 Answer Key Parser")
    print(f"Parsing AMC 10A and 10B answer keys from {START_YEAR} to {END_YEAR}")
    print("(Including 2021 Fall variants)")
    print("=" * 60)

    all_answers = {}
    success_count = 0
    failed_items = []

    # Wait for rate limiting to clear
    print("\nWaiting 10s for rate limit to clear...")
    time.sleep(10)

    # Parse all years
    for year in range(START_YEAR, END_YEAR + 1):
        variants = get_contest_variants(year)
        for variant in variants:
            try:
                delay = random.uniform(5, 10)
                print(f"  Waiting {delay:.1f}s before next request...")
                time.sleep(delay)

                answers = parse_amc10_answers(year, variant)

                if answers:
                    name = get_display_name(year, variant)
                    all_answers[name] = answers
                    success_count += 1
                else:
                    failed_items.append(get_display_name(year, variant))

            except Exception as e:
                print(f"  Error parsing {get_display_name(year, variant)}: {e}")
                failed_items.append(get_display_name(year, variant))

    # Save all answers to files
    output_dir = Path("data/raw/AMC10_Answers")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save as JSON
    json_path = output_dir / "all_answers.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(all_answers, f, indent=2)
    print(f"\nSaved all answers to {json_path}")

    # Also save individual markdown files for each exam
    for name, answers in all_answers.items():
        md_path = output_dir / f"{name} Answers.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# {name} Answer Key\n\n")
            for i, ans in enumerate(answers, 1):
                f.write(f"{i}. {ans}\n")

    print("\n" + "=" * 60)
    print(f"Completed! Successfully parsed {success_count} AMC10 answer keys.")
    print(f"Total problems with answers: {sum(len(a) for a in all_answers.values())}")

    if failed_items:
        print(f"\nFailed items ({len(failed_items)}):")
        for item in failed_items:
            print(f"  - {item}")
    else:
        print("All items parsed successfully!")
    print("=" * 60)

    return all_answers


if __name__ == "__main__":
    main()
