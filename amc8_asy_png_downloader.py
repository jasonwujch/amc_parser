#!/usr/bin/env python3
"""
AMC8 ASY PNG Downloader - Download PNG images for Asymptote diagrams
Downloads rendered PNG images for all [asy]...[/asy] blocks from AMC8 problems.
Covers AMC 8 from 1999-2025.
"""

import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path
import time
import random
import hashlib
import json

# Configuration
START_YEAR = 1999
END_YEAR = 2025

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
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
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
                if len(response.text) > 5000:
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


def download_image(url, output_path, retry_count=3):
    """Download an image file."""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    ]

    for attempt in range(retry_count):
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'image/webp,image/png,image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

        try:
            if attempt > 0:
                delay = min(2 * (2 ** attempt), 20) + random.uniform(0, 2)
                print(f"    Retry download {attempt + 1}/{retry_count} after {delay:.1f}s...")
                time.sleep(delay)

            response = requests.get(url, headers=headers, timeout=30)

            if response.status_code == 200:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                return True
            else:
                print(f"    Download failed with status {response.status_code}")

        except requests.RequestException as e:
            print(f"    Download error on attempt {attempt + 1}: {e}")

    return False


def extract_asy_images(html_content, year):
    """Extract ASY block PNG URLs from the HTML content."""
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
        return []

    asy_images = []

    # Find all problem headers to determine which problem each ASY belongs to
    problem_headers = content_div.find_all(['h2', 'h3'])
    problem_sections = []

    for header in problem_headers:
        header_text = header.get_text().strip()
        problem_match = re.match(r'Problem (\d+)', header_text)
        if problem_match:
            problem_num = int(problem_match.group(1))
            problem_sections.append((problem_num, header))

    # Find all images with ASY blocks
    all_imgs = content_div.find_all('img')

    for img in all_imgs:
        alt_text = img.get('alt', '')
        src = img.get('src', '')

        if alt_text and alt_text.startswith('[asy]') and alt_text.endswith('[/asy]'):
            # Normalize the URL
            if src.startswith('//'):
                full_url = 'https:' + src
            elif src.startswith('/'):
                full_url = 'https://artofproblemsolving.com' + src
            else:
                full_url = src

            # Determine which problem this ASY belongs to
            problem_num = None

            # Find the problem this image belongs to by checking parent elements
            current = img
            while current:
                # Check previous siblings and parents for problem headers
                prev = current.find_previous(['h2', 'h3'])
                if prev:
                    prev_text = prev.get_text().strip()
                    match = re.match(r'Problem (\d+)', prev_text)
                    if match:
                        problem_num = int(match.group(1))
                        break
                current = current.parent
                if current == content_div:
                    break

            if problem_num is None:
                # Default to problem 1 if we can't determine
                problem_num = 1

            # Create a hash of the ASY code for unique identification
            asy_hash = hashlib.md5(alt_text.encode()).hexdigest()[:8]

            asy_images.append({
                'year': year,
                'problem': problem_num,
                'url': full_url,
                'asy_code': alt_text,
                'asy_hash': asy_hash
            })

    return asy_images


def download_asy_images_for_contest(year, output_base_dir, existing_manifest):
    """Download ASY PNG images for a specific AMC8 contest."""
    url = f"https://artofproblemsolving.com/wiki/index.php/{year}_AMC_8_Problems"
    contest_name = f"{year} AMC 8"

    print(f"\nProcessing {contest_name}...")

    # Check if we already have all images for this contest
    contest_key = f"{year}_AMC_8"
    if contest_key in existing_manifest and existing_manifest[contest_key].get('complete', False):
        print(f"  Skipping - already downloaded")
        return existing_manifest.get(contest_key, {}).get('images', [])

    html_content = fetch_page_content(url)

    if not html_content:
        print(f"  Failed to fetch {contest_name}")
        return []

    print(f"  Extracting ASY images...")
    asy_images = extract_asy_images(html_content, year)

    if not asy_images:
        print(f"  No ASY images found in {contest_name}")
        return []

    print(f"  Found {len(asy_images)} ASY images")

    # Create output directory
    output_dir = output_base_dir / f"{year}_AMC_8"
    output_dir.mkdir(parents=True, exist_ok=True)

    downloaded_images = []

    # Track ASY images per problem for numbering
    problem_asy_counts = {}

    for asy_info in asy_images:
        problem_num = asy_info['problem']

        # Count ASY images per problem for proper numbering
        if problem_num not in problem_asy_counts:
            problem_asy_counts[problem_num] = 0
        problem_asy_counts[problem_num] += 1
        asy_index = problem_asy_counts[problem_num]

        # Create filename
        filename = f"p{problem_num:02d}_asy{asy_index}.png"
        output_path = output_dir / filename

        # Skip if already downloaded
        if output_path.exists():
            print(f"    Skipping {filename} - already exists")
            downloaded_images.append({
                'filename': filename,
                'problem': problem_num,
                'asy_index': asy_index,
                'asy_hash': asy_info['asy_hash'],
                'url': asy_info['url']
            })
            continue

        print(f"    Downloading {filename}...")

        # Small delay between downloads
        time.sleep(random.uniform(0.5, 1.5))

        if download_image(asy_info['url'], output_path):
            print(f"    Saved {filename}")
            downloaded_images.append({
                'filename': filename,
                'problem': problem_num,
                'asy_index': asy_index,
                'asy_hash': asy_info['asy_hash'],
                'url': asy_info['url']
            })
        else:
            print(f"    Failed to download {filename}")

    return downloaded_images


def main():
    """Download ASY PNG images for all AMC8 contests 1999-2025."""
    print("=" * 60)
    print("AMC8 ASY PNG Downloader")
    print(f"Downloading PNG images for ASY blocks from {START_YEAR}-{END_YEAR}")
    print("=" * 60)

    output_base_dir = Path("data/raw/AMC8/asy_images")
    output_base_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = output_base_dir / "manifest.json"

    # Load existing manifest if it exists
    existing_manifest = {}
    if manifest_path.exists():
        with open(manifest_path, 'r') as f:
            existing_manifest = json.load(f)
        print(f"\nLoaded existing manifest with {len(existing_manifest)} contests")

    # Wait for rate limiting to clear
    print("\nWaiting 10s for rate limit to clear...")
    time.sleep(10)

    total_images = 0
    results = {}

    for year in range(END_YEAR, START_YEAR - 1, -1):
        contest_key = f"{year}_AMC_8"

        try:
            # Delay between contests
            delay = random.uniform(3, 6)
            print(f"\n  Waiting {delay:.1f}s before next contest...")
            time.sleep(delay)

            images = download_asy_images_for_contest(
                year, output_base_dir, existing_manifest
            )

            results[contest_key] = {
                'images': images,
                'count': len(images),
                'complete': True
            }
            total_images += len(images)

        except Exception as e:
            print(f"  Error processing {year} AMC 8: {e}")
            results[contest_key] = {
                'images': [],
                'count': 0,
                'complete': False,
                'error': str(e)
            }

    # Save manifest
    with open(manifest_path, 'w') as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 60)
    print(f"Download complete!")
    print(f"Total ASY images downloaded: {total_images}")
    print(f"Manifest saved to: {manifest_path}")
    print("=" * 60)

    # Print summary
    print("\nSummary by contest:")
    for contest_key in sorted(results.keys(), reverse=True):
        info = results[contest_key]
        status = "+" if info['complete'] else "x"
        print(f"  {status} {contest_key}: {info['count']} images")


if __name__ == "__main__":
    main()
