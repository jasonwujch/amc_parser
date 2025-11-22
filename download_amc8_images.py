#!/usr/bin/env python3
"""
Script to scan AMC8 markdown files and download embedded images.
Maintains the same directory structure as asy_images.
"""

import re
import os
from pathlib import Path
from collections import defaultdict
import time
import requests
from urllib.parse import urlparse

# Base directories
AMC8_DIR = Path("/home/user/amc_parser/data/raw/AMC8")
IMAGES_DIR = AMC8_DIR / "wiki_images"

def extract_image_urls(markdown_file):
    """
    Extract all markdown image URLs from a file.
    Returns list of tuples: (problem_number, url)
    """
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by problems
    problems = re.split(r'^Problem (\d+)$', content, flags=re.MULTILINE)

    image_urls = []
    current_problem = None

    for i, section in enumerate(problems):
        if i % 2 == 1:  # This is a problem number
            current_problem = int(section)
        elif current_problem is not None:  # This is problem content
            # Find all markdown image URLs: ![](url)
            urls = re.findall(r'!\[\]\((https?://[^\)]+)\)', section)
            for url in urls:
                image_urls.append((current_problem, url))

    return image_urls

def get_filename_from_url(url):
    """Extract filename from URL, preserving directory structure."""
    # Parse the URL to get the path component
    parsed = urlparse(url)
    # Get the path without leading slash
    path = parsed.path.lstrip('/')
    # Return just the path part (preserves subdirectories)
    return path

def download_image(url, save_path, max_retries=5):
    """Download image from URL to save_path with retry logic."""
    # Create directory if it doesn't exist
    save_path.parent.mkdir(parents=True, exist_ok=True)

    # If file already exists, skip
    if save_path.exists():
        print(f"  ⚠ File already exists, skipping")
        return True

    session = requests.Session()

    for attempt in range(max_retries):
        try:
            # Add headers to appear more like a regular browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }

            # Download the image with timeout
            response = session.get(url, headers=headers, timeout=30, allow_redirects=True)
            response.raise_for_status()

            # Write to file
            with open(save_path, 'wb') as out_file:
                out_file.write(response.content)

            return True

        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s, 8s, 16s
                print(f"  ⚠ Attempt {attempt + 1} failed: {e}")
                print(f"  ⏳ Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
            else:
                print(f"  ✗ All {max_retries} attempts failed: {e}")
                return False

    return False

def main():
    # Find all AMC8 markdown files
    markdown_files = sorted(AMC8_DIR.glob("*.md"))

    print(f"Found {len(markdown_files)} AMC8 markdown files")

    # Track all images to download
    all_images = []

    # Process each markdown file
    for md_file in markdown_files:
        # Extract year from filename (e.g., "2025 AMC 8.md" -> "2025")
        year_match = re.match(r'(\d{4})\s+AMC\s+8\.md', md_file.name)
        if not year_match:
            print(f"Warning: Could not parse year from {md_file.name}")
            continue

        year = year_match.group(1)
        contest_name = f"{year}_AMC_8"

        # Extract image URLs from this file
        image_urls = extract_image_urls(md_file)

        if image_urls:
            print(f"\n{contest_name}: Found {len(image_urls)} images")
            for prob_num, url in image_urls:
                print(f"  Problem {prob_num:02d}: {url}")
                all_images.append((contest_name, prob_num, url))
        else:
            print(f"{contest_name}: No images found")

    print(f"\n{'='*80}")
    print(f"Total images found: {len(all_images)}")
    print(f"{'='*80}\n")

    # Download all images
    successful = 0
    failed = 0

    for i, (contest_name, prob_num, url) in enumerate(all_images):
        # Get the filename from URL (preserves path structure)
        url_path = get_filename_from_url(url)

        # Create save path: data/raw/AMC8/wiki_images/{YEAR_AMC_8}/{url_path}
        save_path = IMAGES_DIR / contest_name / url_path

        print(f"\n[{i+1}/{len(all_images)}] Downloading {url}")
        print(f"  -> {save_path}")

        if download_image(url, save_path):
            successful += 1
            print(f"  ✓ Success")
        else:
            failed += 1
            print(f"  ✗ Failed")

        # Small delay between downloads to be polite to the server
        if i < len(all_images) - 1:
            time.sleep(1)

    print(f"\n{'='*80}")
    print(f"Download Summary:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total: {len(all_images)}")
    print(f"{'='*80}\n")

    # Create a manifest file similar to asy_images
    manifest_path = IMAGES_DIR / "manifest.txt"
    with open(manifest_path, 'w', encoding='utf-8') as f:
        f.write(f"AMC8 Wiki Images Manifest\n")
        f.write(f"{'='*80}\n\n")
        f.write(f"Total images: {len(all_images)}\n")
        f.write(f"Successful downloads: {successful}\n")
        f.write(f"Failed downloads: {failed}\n\n")
        f.write(f"{'='*80}\n\n")

        by_contest = defaultdict(list)
        for contest_name, prob_num, url in all_images:
            by_contest[contest_name].append((prob_num, url))

        for contest_name in sorted(by_contest.keys()):
            f.write(f"\n{contest_name}:\n")
            for prob_num, url in sorted(by_contest[contest_name]):
                f.write(f"  Problem {prob_num:02d}: {url}\n")

    print(f"Manifest written to: {manifest_path}")

if __name__ == "__main__":
    main()
