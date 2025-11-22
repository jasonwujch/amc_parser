# AMC8 Wiki Images Download Report

## Summary

Systematically scanned all AMC8 problem markdown files (1999-2025) for embedded wiki image URLs and attempted to download them.

**Date:** November 22, 2025
**Total markdown files scanned:** 26
**Total image URLs found:** 6
**Successfully downloaded:** 2
**Failed downloads:** 4

## Download Results

### ✅ Successfully Downloaded (2 images)

1. **2025 AMC 8 - Problem 2**
   - URL: `https://wiki-images.artofproblemsolving.com//d/de/Mathh.PNG`
   - Local path: `data/raw/AMC8/wiki_images/2025_AMC_8/d/de/Mathh.PNG`
   - Size: 9.8 KB
   - Type: PNG image (304 x 85, 8-bit colormap)
   - Status: ✓ Downloaded successfully

2. **2025 AMC 8 - Problem 8**
   - URL: `https://wiki-images.artofproblemsolving.com//5/54/Amc8_2025_prob8.PNG`
   - Local path: `data/raw/AMC8/wiki_images/2025_AMC_8/5/54/Amc8_2025_prob8.PNG`
   - Size: 6.8 KB
   - Type: PNG image (410 x 157, 8-bit colormap)
   - Status: ✓ Downloaded successfully

### ❌ Failed Downloads (4 images)

All failed downloads returned HTTP 522 (CloudFlare timeout) or 503 (Service Unavailable) errors after multiple retry attempts.

1. **2004 AMC 8 - Problem 23**
   - URL: `https://wiki-images.artofproblemsolving.com//f/f5/AMC8200423.gif`
   - Error: HTTP 522 - Server timeout
   - Attempts: 5 retries with exponential backoff (failed all)

2. **2019 AMC 8 - Problem 5 (Image 1)**
   - URL: `https://wiki-images.artofproblemsolving.com//thumb/5/56/2019_AMC_8_-4_Image_1.png/900px-2019_AMC_8_-4_Image_1.png`
   - Error: HTTP 522 - Server timeout
   - Attempts: 5 retries with exponential backoff (failed all)

3. **2019 AMC 8 - Problem 5 (Image 2)**
   - URL: `https://wiki-images.artofproblemsolving.com//thumb/6/63/2019_AMC_8_-4_Image_2.png/600px-2019_AMC_8_-4_Image_2.png`
   - Error: HTTP 522 - Server timeout
   - Attempts: 5 retries with exponential backoff (failed all)

4. **2025 AMC 8 - Problem 2 (second image)**
   - URL: `https://wiki-images.artofproblemsolving.com//3/38/Amc8_2025_prob_2_pic.PNG`
   - Error: HTTP 503/522 - Service Unavailable / Server timeout
   - Attempts: 5 retries with exponential backoff (failed all)

## Directory Structure

Downloaded images maintain the same directory structure as ASY images:

```
data/raw/AMC8/wiki_images/
├── manifest.txt
├── 2004_AMC_8/
│   └── f/f5/ (empty - download failed)
├── 2019_AMC_8/
│   └── thumb/... (empty - downloads failed)
└── 2025_AMC_8/
    ├── d/de/Mathh.PNG (✓)
    └── 5/54/Amc8_2025_prob8.PNG (✓)
```

## Years with No Embedded Wiki Images

The following AMC8 years (21 total) had no markdown-style image URLs in their problem files:
- 1999, 2000, 2001, 2002, 2003, 2005, 2006, 2007, 2008, 2009
- 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2020
- 2022, 2023, 2024

**Note:** These years may still have ASY-generated images, but no external wiki images embedded in the markdown.

## Recommendations

1. **Retry Failed Downloads:** The 4 failed images returned server errors (522/503), suggesting temporary server issues or rate limiting. These can be retried later.

2. **Alternative Sources:** For failed downloads, consider:
   - Checking if the images are available in the problem's solutions directory
   - Looking for alternative URLs on the Art of Problem Solving wiki
   - Checking if these problems have ASY code that could generate the images instead

3. **Script Location:** The download script is available at:
   - `download_amc8_images.py`
   - Can be re-run to retry failed downloads
   - Automatically skips already downloaded files

## Technical Details

- **Download Method:** Python requests library with retry logic
- **Retry Strategy:** Exponential backoff (1s, 2s, 4s, 8s, 16s)
- **Max Attempts:** 5 per image
- **User Agent:** Mozilla/5.0 (to avoid bot blocking)
- **Timeout:** 30 seconds per request
- **Inter-request Delay:** 1 second (to be polite to server)
