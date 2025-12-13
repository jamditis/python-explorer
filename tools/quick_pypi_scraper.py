#!/usr/bin/env python3
"""
Quick PyPI Scraper - Downloads HTML pages directly with curl
"""

import json
import subprocess
from bs4 import BeautifulSoup

# Top categories to search
SEARCHES = [
    "web+framework", "data+analysis", "machine+learning", "visualization",
    "testing", "automation", "scraping", "async", "api", "database"
]

def download_page(query, page=1):
    """Download a PyPI search page using curl"""
    url = f"https://pypi.org/search/?q={query}&page={page}"
    try:
        result = subprocess.run(
            ['curl', '-s', '-L', url],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def parse_libraries(html):
    """Extract libraries from HTML"""
    soup = BeautifulSoup(html, 'html.parser')
    libs = []

    for snippet in soup.find_all('a', class_='package-snippet'):
        try:
            name_elem = snippet.find('span', class_='package-snippet__name')
            desc_elem = snippet.find('p', class_='package-snippet__description')

            if name_elem:
                name = name_elem.text.strip()
                desc = desc_elem.text.strip() if desc_elem else "No description"

                libs.append({
                    'name': name,
                    'description': desc,
                    'url': f"https://pypi.org/project/{name}/"
                })
        except:
            continue

    return libs

def main():
    print("Quick PyPI Scraper")
    print("=" * 50)

    all_libs = []

    for query in SEARCHES:
        print(f"\nSearching: {query.replace('+', ' ')}")
        html = download_page(query, page=1)

        if html:
            libs = parse_libraries(html)
            print(f"  Found {len(libs)} libraries")
            all_libs.extend(libs)

    # Deduplicate
    seen = set()
    unique = []
    for lib in all_libs:
        if lib['name'].lower() not in seen:
            seen.add(lib['name'].lower())
            unique.append(lib)

    print(f"\nTotal unique libraries: {len(unique)}")

    # Save
    with open('quick_results.json', 'w') as f:
        json.dump(unique, f, indent=2)

    print(f"Saved to quick_results.json")

    # Show sample
    print("\nSample libraries found:")
    for lib in unique[:10]:
        print(f"  - {lib['name']}: {lib['description'][:60]}...")

if __name__ == "__main__":
    main()
