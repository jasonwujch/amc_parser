#!/usr/bin/env python3
"""
AMC8 Answer Key Parser - Parse AMC8 answer keys from ArtOfProblemSolving.com
Handles AMC 8 (1999-2025) - 25 problems per contest with A-E answers
"""

import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path
import time
import random
import json

# Configuration
START_YEAR = 1999
END_YEAR = 2025
PROBLEMS_PER_CONTEST = 25

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
                if len(response.text) > 1000:  # Answer key pages are smaller than problem pages
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
    """Extract answer key from the HTML content. AMC8 answers are A-E."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the main content div
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

    # Method 2: Look for list items with "Problem X: answer" format
    if len(answers) < PROBLEMS_PER_CONTEST:
        answers = []
        for li in content_div.find_all('li'):
            text = li.get_text().strip()
            # Look for patterns like "1. A" or "Problem 1: A" or just letters
            match = re.search(r'(?:Problem\s+\d+[:\s]+)?([A-Ea-e])(?:\s|$)', text)
            if match:
                answers.append(match.group(1).upper())

    # Method 3: Parse from paragraphs or text content
    if len(answers) < PROBLEMS_PER_CONTEST:
        answers = []
        text = content_div.get_text()
        # Look for numbered list pattern: "1. A" or "1) A" etc
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
                    if text in ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']:
                        answers.append(text.upper())

    # Method 5: Look for any sequence of 25 letters that look like answers
    if len(answers) < PROBLEMS_PER_CONTEST:
        answers = []
        text = content_div.get_text()
        # Find all standalone A-E letters
        all_letters = re.findall(r'\b([A-Ea-e])\b', text)
        # Filter to just letters that could be answers
        potential_answers = [l.upper() for l in all_letters if l.upper() in 'ABCDE']
        # Try to find a sequence of 25 answers
        if len(potential_answers) >= PROBLEMS_PER_CONTEST:
            answers = potential_answers[:PROBLEMS_PER_CONTEST]

    if len(answers) == PROBLEMS_PER_CONTEST:
        return answers
    elif len(answers) > 0:
        print(f"  Warning: Found {len(answers)} answers instead of expected {PROBLEMS_PER_CONTEST}")
        return answers if len(answers) >= 20 else None

    return None


def parse_amc8_answers(year):
    """Parse AMC8 answer key for a specific year."""
    url = f"https://artofproblemsolving.com/wiki/index.php/{year}_AMC_8_Answer_Key"
    name = f"{year} AMC 8"

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
    """Parse AMC8 answer keys from 1999 to 2025."""
    print("=" * 60)
    print("AMC8 Answer Key Parser")
    print(f"Parsing AMC 8 answer keys from {START_YEAR} to {END_YEAR}")
    print("=" * 60)

    all_answers = {}
    success_count = 0
    failed_items = []

    # Wait for any rate limiting to clear
    print("\nWaiting 10s for rate limit to clear...")
    time.sleep(10)

    # Parse all years
    for year in range(START_YEAR, END_YEAR + 1):
        try:
            # Delays to avoid rate limiting
            delay = random.uniform(3, 6)
            print(f"  Waiting {delay:.1f}s before next request...")
            time.sleep(delay)

            answers = parse_amc8_answers(year)

            if answers:
                key = f"{year} AMC 8"
                all_answers[key] = answers
                success_count += 1
            else:
                failed_items.append(f"{year} AMC 8")

        except Exception as e:
            print(f"  Error parsing {year} AMC 8: {e}")
            failed_items.append(f"{year} AMC 8")

    # Save all answers to a JSON file
    output_dir = Path("data/raw/AMC8_Answers")
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
    print(f"Completed! Successfully parsed {success_count} AMC 8 answer keys.")
    print(f"Total problems with answers: {success_count * PROBLEMS_PER_CONTEST}")

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
