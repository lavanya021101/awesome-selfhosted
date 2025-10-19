# App Information Extraction

This document explains the extraction process used to create `apps_without_links.md` from the main `README.md`.

## What Was Extracted

The script `extract_apps.py` parses the README.md file and extracts the following information for each application:

1. **App Name** - The name of the application
2. **Category** - The category under which the app is listed (e.g., Analytics, Automation, etc.)
3. **Description** - A brief description of what the app does
4. **Tags** - Technology tags including:
   - License type (e.g., MIT, GPL-3.0, Apache-2.0)
   - Platform/language tags (e.g., Docker, Python, Nodejs, PHP)
   - Warning flags (⚠) if applicable

## Output Format

The extracted information is saved in `apps_without_links.md` with:
- All 1195 applications organized by category
- Clean descriptions without any hyperlinks
- Tags listed clearly for each app
- No URLs or clickable links

## About GitHub Stars

GitHub star counts are **not included** in the output document because:
- The star counts are not present in the README.md file itself
- Fetching them from the GitHub API requires authentication and is subject to rate limits
- To include star counts, you would need to:
  1. Obtain a GitHub API token
  2. Modify the script to use the token for authentication
  3. Re-run the extraction with star fetching enabled

## Running the Extraction

To extract the information yourself:

```bash
python3 extract_apps.py
```

This will:
1. Parse README.md
2. Extract all app information
3. Generate `apps_without_links.md`
4. Display a summary of extracted apps

## Script Details

The extraction script uses regular expressions to:
- Identify category headers (lines starting with `###`)
- Parse app entries (lines starting with `- [`)
- Extract app names from markdown links
- Clean descriptions by removing all links and parenthetical references
- Collect all backtick-enclosed tags

The script is designed to handle various formats in the README including:
- Apps with demo links
- Apps with source code links
- Apps with warning indicators (⚠)
- Apps with multiple tags and complex descriptions
