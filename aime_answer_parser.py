#!/usr/bin/env python3
"""
AIME Answer Key Parser - Parse AIME answer keys from ArtOfProblemSolving.com
Handles both AIME I and AIME II variants (2010-2025)
"""

import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path
import time
import random
import json

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
    """Extract answer key from the HTML content."""
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
            # Extract numeric answer (could be just a number or have additional text)
            match = re.match(r'^(\d+)', text)
            if match:
                answers.append(match.group(1))

    # Method 2: Look for list items with "Problem X: answer" format
    if len(answers) < 15:
        answers = []
        for li in content_div.find_all('li'):
            text = li.get_text().strip()
            # Look for patterns like "1. 600" or "Problem 1: 600" or just numbers
            match = re.search(r'(?:Problem\s+\d+[:\s]+)?(\d{1,3})(?:\s|$)', text)
            if match:
                answers.append(match.group(1))

    # Method 3: Parse from paragraphs or text content
    if len(answers) < 15:
        answers = []
        text = content_div.get_text()
        # Look for numbered list pattern: "1. 600" or "1) 600" etc
        matches = re.findall(r'(?:^|\n)\s*\d+[.):\s]+(\d{1,3})(?:\s|$|\n)', text)
        if matches:
            answers = matches

    # Method 4: Look for table format
    if len(answers) < 15:
        answers = []
        tables = content_div.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all(['td', 'th'])
                for cell in cells:
                    text = cell.get_text().strip()
                    if text.isdigit() and len(text) <= 3:
                        answers.append(text)

    # Method 5: Look for any sequence of 15 numbers that look like answers
    if len(answers) < 15:
        answers = []
        text = content_div.get_text()
        # Find all standalone 1-3 digit numbers
        all_nums = re.findall(r'\b(\d{1,3})\b', text)
        # Filter to just numbers that could be answers (0-999)
        potential_answers = [n for n in all_nums if int(n) >= 0 and int(n) <= 999]
        # Try to find a sequence of 15 answers
        if len(potential_answers) >= 15:
            # Skip initial numbers that might be problem numbers (1-15)
            for start_idx in range(len(potential_answers) - 14):
                candidate = potential_answers[start_idx:start_idx + 15]
                # Check if this looks like a valid answer sequence (not just 1-15)
                if not all(int(candidate[i]) == i + 1 for i in range(15)):
                    answers = candidate
                    break

    if len(answers) == 15:
        return answers
    elif len(answers) > 0:
        print(f"  Warning: Found {len(answers)} answers instead of expected 15")
        return answers if len(answers) >= 10 else None

    return None


def parse_aime_answers(year, variant):
    """Parse AIME answer key for a specific year and variant (I or II)."""
    url = f"https://artofproblemsolving.com/wiki/index.php/{year}_AIME_{variant}_Answer_Key"
    name = f"{year} AIME {variant}"

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
    """Parse AIME answer keys from 2010 to 2025."""
    print("=" * 60)
    print("AIME Answer Key Parser")
    print("Parsing AIME I and AIME II answer keys from 2010 to 2025")
    print("=" * 60)

    all_answers = {}
    success_count = 0
    failed_items = []

    # Years to parse: 2010-2025
    start_year = 2010
    end_year = 2025

    # Wait for any rate limiting to clear
    print("\nWaiting 10s for rate limit to clear...")
    time.sleep(10)

    # Parse all years
    for year in range(start_year, end_year + 1):
        for variant in ['I', 'II']:
            try:
                # Delays to avoid rate limiting
                delay = random.uniform(5, 10)
                print(f"  Waiting {delay:.1f}s before next request...")
                time.sleep(delay)

                answers = parse_aime_answers(year, variant)

                if answers:
                    key = f"{year} AIME {variant}"
                    all_answers[key] = answers
                    success_count += 1
                else:
                    failed_items.append(f"{year} AIME {variant}")

            except Exception as e:
                print(f"  Error parsing {year} AIME {variant}: {e}")
                failed_items.append(f"{year} AIME {variant}")

    # Save all answers to a JSON file
    output_dir = Path("data/raw/AIME_Answers")
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
    print(f"Completed! Successfully parsed {success_count} AIME answer keys.")
    print(f"Total problems with answers: {success_count * 15}")

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
