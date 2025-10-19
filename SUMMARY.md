# Extraction Summary

## Overview
Successfully extracted all app information from the README.md file and created a new document (`apps_without_links.md`) containing app names, descriptions, and tags **without any links**.

## Results

### Statistics
- **Total apps extracted:** 1,195
- **Total categories:** 83
- **Output file size:** 9,816 lines (181 KB)
- **No URLs or links:** Verified ✓

### What's Included in Output

For each of the 1,195 applications, the following information was extracted:

1. **App Name** - Clear, bold heading
2. **Category** - Organized under category headers (e.g., Analytics, Automation, Wikis)
3. **Description** - Clean, readable description without any hyperlinks
4. **Tags** - Including:
   - License information (MIT, GPL-3.0, Apache-2.0, etc.)
   - Platform/Language tags (Docker, Python, PHP, Nodejs, etc.)
   - Warning indicators (⚠) where applicable

### Most Common Licenses
- MIT: 323 apps
- AGPL-3.0: 276 apps
- GPL-3.0: 225 apps
- Apache-2.0: 128 apps
- GPL-2.0: 98 apps

### Most Common Platforms/Languages
- PHP: 153 apps
- Docker: 144 apps
- Nodejs: 65 apps
- Nodejs/Docker: 59 apps
- Python: 58 apps
- Go/Docker: 45 apps

## Files Created

1. **apps_without_links.md** - The main output document with all extracted information
2. **extract_apps.py** - Python script used to perform the extraction
3. **EXTRACTION.md** - Technical documentation about the extraction process
4. **SUMMARY.md** - This file, providing an overview of results

## Sample Entry

Here's how each app appears in the output document:

```
**Plausible Analytics**

Description: Simple, lightweight and privacy-friendly web analytics

Tags: AGPL-3.0, Elixir

---
```

## Note on GitHub Stars

GitHub star counts are **not included** in the output because:
- Star counts are not present in the README.md source file
- Fetching them requires GitHub API authentication
- API rate limits prevent unauthenticated bulk requests

To add star counts in the future, you would need to:
1. Obtain a GitHub API token
2. Modify the script to use authenticated requests
3. Re-run the extraction

## Verification

✓ All 1,195 apps successfully extracted
✓ All descriptions cleaned (no links remaining)
✓ Zero URLs found in output document
✓ Zero markdown links found in output document
✓ Organized by 83 categories
✓ All tags preserved from original README

## Usage

The generated `apps_without_links.md` file can now be used for:
- Offline reference without hyperlinks
- Text processing and analysis
- Database import
- Documentation
- Search and filtering
- Any other purpose requiring link-free content
