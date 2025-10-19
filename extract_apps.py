#!/usr/bin/env python3
"""
Extract app information from README.md and create a document without links.
Extracts: App names, star amounts (from GitHub API), descriptions, and tags.
"""

import re
import json
import time
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

def extract_github_repo(url):
    """Extract GitHub repository owner and name from URL."""
    match = re.search(r'github\.com/([^/]+)/([^/\)]+)', url)
    if match:
        owner = match.group(1)
        repo = match.group(2)
        return owner, repo
    return None, None

def get_github_stars(owner, repo, token=None):
    """Fetch star count from GitHub API."""
    if not owner or not repo:
        return None
    
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}"
        headers = {'User-Agent': 'awesome-selfhosted-extractor'}
        if token:
            headers['Authorization'] = f'token {token}'
        
        req = Request(url, headers=headers)
        with urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data.get('stargazers_count', 0)
    except (HTTPError, URLError, Exception) as e:
        print(f"Warning: Could not fetch stars for {owner}/{repo}: {e}")
        return None

def parse_readme(filename):
    """Parse README.md and extract app information."""
    apps = []
    current_category = None
    
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.rstrip()
        
        # Detect category headers (### Header)
        if line.startswith('### '):
            current_category = line[4:].strip()
            continue
        
        # Match app entries starting with "- ["
        if line.startswith('- [') and current_category:
            # Parse the app entry
            # Format: - [App Name](URL) `⚠` - Description. ([Demo](URL), [Source Code](URL)) `License` `Tags`
            
            # Extract app name
            name_match = re.match(r'- \[([^\]]+)\]', line)
            if not name_match:
                continue
            
            app_name = name_match.group(1)
            
            # Extract description (text after the first ") -" or ") `⚠` -")
            desc_match = re.search(r'\) (?:`⚠` )?- (.+)', line)
            
            if desc_match:
                description = desc_match.group(1).strip()
                # Remove all parenthetical content (links like [Demo](...), [Source Code](...))
                description = re.sub(r'\s*\([^)]*\)', '', description)
                # Remove all bracketed links like [Demo]
                description = re.sub(r'\s*\[[^\]]*\]', '', description)
                # Remove all backtick tags at the end
                description = re.sub(r'\s*`[^`]*`.*$', '', description)
                # Remove trailing periods, commas, and parentheses
                description = description.rstrip('.,)').strip()
            else:
                description = ""
            
            # Extract tags (backtick-enclosed items at the end)
            tags = re.findall(r'`([^`]+)`', line)
            
            # Extract GitHub source code URL
            source_match = re.search(r'\[Source Code\]\(([^)]+)\)', line)
            github_url = source_match.group(1) if source_match else None
            
            # Get GitHub stars if available
            # Note: Disabled due to API rate limits
            stars = None
            # if github_url:
            #     owner, repo = extract_github_repo(github_url)
            #     if owner and repo:
            #         stars = get_github_stars(owner, repo)
            #         time.sleep(0.1)  # Rate limiting
            
            apps.append({
                'name': app_name,
                'category': current_category,
                'description': description,
                'tags': tags,
                'stars': stars
            })
    
    return apps

def create_output_document(apps, output_filename):
    """Create output document with extracted information."""
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write("# Awesome Self-Hosted Applications\n\n")
        f.write("This document contains app names, descriptions, and tags extracted from the README.\n")
        f.write("No links are included in this document.\n\n")
        f.write("Note: GitHub star counts are not included due to API rate limits. ")
        f.write("To get star counts, you would need to use a GitHub API token or fetch them separately.\n\n")
        f.write("---\n\n")
        
        current_category = None
        for app in apps:
            # Write category header if changed
            if app['category'] != current_category:
                current_category = app['category']
                f.write(f"\n## {current_category}\n\n")
            
            # Write app information
            f.write(f"**{app['name']}**\n\n")
            
            if app['description']:
                f.write(f"Description: {app['description']}\n\n")
            
            if app['stars'] is not None:
                f.write(f"GitHub Stars: {app['stars']:,}\n\n")
            
            if app['tags']:
                f.write(f"Tags: {', '.join(app['tags'])}\n\n")
            
            f.write("---\n\n")

def main():
    """Main function."""
    print("Extracting app information from README.md...")
    apps = parse_readme('README.md')
    print(f"Found {len(apps)} apps")
    
    print("\nCreating output document...")
    create_output_document(apps, 'apps_without_links.md')
    print("Output saved to apps_without_links.md")
    
    # Print summary statistics
    apps_with_stars = sum(1 for app in apps if app['stars'] is not None)
    print(f"\nSummary:")
    print(f"- Total apps: {len(apps)}")
    print(f"- Apps with GitHub stars: {apps_with_stars}")
    print(f"- Apps without GitHub stars: {len(apps) - apps_with_stars}")

if __name__ == '__main__':
    main()
