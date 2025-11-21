#!/usr/bin/env python3
"""
Test script to check if we can access AMC12 pages on AoPS
"""

import requests
import time
import random

def test_access():
    """Test if we can access AoPS AMC12 pages."""
    
    test_urls = [
        "https://artofproblemsolving.com/wiki/index.php/AMC_12_Problems_and_Solutions",
        "https://artofproblemsolving.com/wiki/index.php/2023_AMC_12A_Problems",
        "https://artofproblemsolving.com/wiki/index.php/2023_AMC_12B_Problems"
    ]
    
    user_agents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    
    for url in test_urls:
        print(f"\nTesting: {url}")
        
        for ua in user_agents:
            headers = {
                'User-Agent': ua,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            
            try:
                print(f"  Trying with UA: {ua[:50]}...")
                response = requests.get(url, headers=headers, timeout=10)
                print(f"    Status: {response.status_code}")
                
                if response.status_code == 200:
                    print(f"    ✓ SUCCESS! Content length: {len(response.text)}")
                    # Check if we got actual content
                    if "AMC" in response.text and "Problem" in response.text:
                        print("    ✓ Valid AMC content found!")
                        return True
                elif response.status_code == 403:
                    print("    ✗ 403 Forbidden")
                else:
                    print(f"    Status: {response.status_code}")
                    
            except Exception as e:
                print(f"    Error: {e}")
            
            # Small delay between attempts
            time.sleep(2)
    
    return False

if __name__ == "__main__":
    print("Testing access to AoPS AMC12 pages...")
    print("=" * 50)
    
    if test_access():
        print("\n✓ Successfully accessed AoPS! The AMC12 parser should work.")
    else:
        print("\n✗ Unable to access AoPS. The site may be blocking automated requests.")
        print("\nPossible solutions:")
        print("1. Try running from a different network")
        print("2. Use a browser automation tool like Selenium")
        print("3. Manually download the pages")
        print("4. Use a proxy or VPN service")