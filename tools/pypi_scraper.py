#!/usr/bin/env python3
"""
PyPI Library Scraper
Scrapes PyPI search results to discover Python libraries across various categories
"""

import asyncio
import json
import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import time

# Categories to search on PyPI
SEARCH_QUERIES = [
    "web framework",
    "data analysis",
    "machine learning",
    "deep learning",
    "automation",
    "web scraping",
    "data visualization",
    "testing",
    "GUI",
    "image processing",
    "video processing",
    "NLP natural language",
    "computer vision",
    "database ORM",
    "API framework",
    "async asynchronous",
    "CLI command line",
    "authentication",
    "security cryptography",
    "file processing",
    "HTTP client",
    "task queue",
    "scheduling",
    "PDF",
    "Excel spreadsheet",
    "scientific computing",
    "networking",
    "game development",
    "3D graphics",
    "plotting charts"
]

async def scrape_pypi_search(query, max_pages=3):
    """Scrape PyPI search results for a given query"""
    libraries = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print(f"\n🔍 Searching PyPI for: '{query}'")

        for page_num in range(1, max_pages + 1):
            url = f"https://pypi.org/search/?q={query.replace(' ', '+')}&page={page_num}"

            try:
                await page.goto(url, wait_until="networkidle", timeout=30000)
                await page.wait_for_selector('.package-snippet', timeout=10000)

                # Get page content
                content = await page.content()
                soup = BeautifulSoup(content, 'html.parser')

                # Find all package snippets
                snippets = soup.find_all('a', class_='package-snippet')

                if not snippets:
                    print(f"  ⚠️  No results on page {page_num}")
                    break

                print(f"  📄 Page {page_num}: Found {len(snippets)} packages")

                for snippet in snippets:
                    try:
                        # Extract package name
                        name_elem = snippet.find('span', class_='package-snippet__name')
                        if not name_elem:
                            continue
                        name = name_elem.text.strip()

                        # Extract description
                        desc_elem = snippet.find('p', class_='package-snippet__description')
                        description = desc_elem.text.strip() if desc_elem else "No description available"

                        # Extract version
                        version_elem = snippet.find('span', class_='package-snippet__version')
                        version = version_elem.text.strip() if version_elem else "unknown"

                        # Extract created date
                        created_elem = snippet.find('span', class_='package-snippet__created')
                        created = created_elem.text.strip() if created_elem else "unknown"

                        # Build package URL
                        package_url = f"https://pypi.org/project/{name}/"

                        libraries.append({
                            'name': name,
                            'description': description,
                            'version': version,
                            'created': created,
                            'url': package_url,
                            'search_query': query
                        })

                    except Exception as e:
                        print(f"    ⚠️  Error parsing snippet: {e}")
                        continue

                # Small delay between pages
                await asyncio.sleep(1)

            except Exception as e:
                print(f"  ❌ Error loading page {page_num}: {e}")
                break

        await browser.close()

    return libraries

async def get_package_details(package_name):
    """Get detailed information about a specific package"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        url = f"https://pypi.org/project/{package_name}/"

        try:
            await page.goto(url, wait_until="networkidle", timeout=30000)
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')

            # Extract GitHub stars or other metrics if available
            details = {
                'name': package_name,
                'url': url
            }

            # Try to find project links
            sidebar = soup.find('div', class_='sidebar-section')
            if sidebar:
                links = sidebar.find_all('a')
                for link in links:
                    href = link.get('href', '')
                    if 'github.com' in href:
                        details['github'] = href
                    elif 'docs' in href or 'documentation' in href:
                        details['docs'] = href

            await browser.close()
            return details

        except Exception as e:
            print(f"  ❌ Error getting details for {package_name}: {e}")
            await browser.close()
            return None

def deduplicate_libraries(libraries):
    """Remove duplicate libraries based on name"""
    seen = set()
    unique = []

    for lib in libraries:
        name_lower = lib['name'].lower()
        if name_lower not in seen:
            seen.add(name_lower)
            unique.append(lib)

    return unique

def categorize_library(library):
    """Attempt to categorize a library based on its description and search query"""
    desc = library['description'].lower()
    query = library['search_query'].lower()

    # Category mapping based on keywords
    if any(word in desc or word in query for word in ['django', 'flask', 'fastapi', 'web framework', 'wsgi', 'asgi']):
        return 'Web Frameworks'
    elif any(word in desc or word in query for word in ['pandas', 'numpy', 'data analysis', 'dataframe']):
        return 'Data Analysis'
    elif any(word in desc or word in query for word in ['machine learning', 'ml', 'scikit', 'xgboost']):
        return 'Machine Learning'
    elif any(word in desc or word in query for word in ['deep learning', 'neural network', 'tensorflow', 'pytorch', 'keras']):
        return 'Deep Learning'
    elif any(word in desc or word in query for word in ['plot', 'chart', 'visualization', 'graph']):
        return 'Data Visualization'
    elif any(word in desc or word in query for word in ['nlp', 'natural language', 'text processing', 'spacy']):
        return 'Natural Language Processing'
    elif any(word in desc or word in query for word in ['computer vision', 'image processing', 'opencv', 'pillow']):
        return 'Computer Vision'
    elif any(word in desc or word in query for word in ['scraping', 'scraper', 'crawler', 'beautiful soup']):
        return 'Web Scraping'
    elif any(word in desc or word in query for word in ['automation', 'automate', 'selenium']):
        return 'Automation'
    elif any(word in desc or word in query for word in ['gui', 'interface', 'tkinter', 'qt']):
        return 'GUI Development'
    elif any(word in desc or word in query for word in ['test', 'pytest', 'unittest']):
        return 'Testing'
    elif any(word in desc or word in query for word in ['orm', 'database', 'sqlalchemy']):
        return 'ORM'
    elif any(word in desc or word in query for word in ['api', 'rest', 'graphql']):
        return 'RESTful API'
    elif any(word in desc or word in query for word in ['cli', 'command line', 'terminal']):
        return 'Command-line Tools'
    else:
        return 'Utilities'

async def main():
    """Main scraper execution"""
    print("=" * 60)
    print("PyPI Library Scraper")
    print("=" * 60)

    all_libraries = []

    # Scrape each search query
    for query in SEARCH_QUERIES:
        libs = await scrape_pypi_search(query, max_pages=2)
        all_libraries.extend(libs)

        # Rate limiting
        await asyncio.sleep(2)

    print(f"\n📊 Total libraries found: {len(all_libraries)}")

    # Deduplicate
    unique_libraries = deduplicate_libraries(all_libraries)
    print(f"📊 Unique libraries: {len(unique_libraries)}")

    # Categorize
    for lib in unique_libraries:
        lib['category'] = categorize_library(lib)

    # Sort by name
    unique_libraries.sort(key=lambda x: x['name'].lower())

    # Save to JSON
    output_file = 'pypi_libraries.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unique_libraries, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Saved {len(unique_libraries)} libraries to {output_file}")

    # Print category breakdown
    categories = {}
    for lib in unique_libraries:
        cat = lib['category']
        categories[cat] = categories.get(cat, 0) + 1

    print("\n📁 Category Breakdown:")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count}")

    # Save a formatted version for easy review
    output_md = 'pypi_libraries.md'
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write("# PyPI Libraries Found\n\n")

        current_category = None
        for lib in sorted(unique_libraries, key=lambda x: (x['category'], x['name'].lower())):
            if lib['category'] != current_category:
                current_category = lib['category']
                f.write(f"\n## {current_category}\n\n")

            f.write(f"### {lib['name']}\n")
            f.write(f"- **Description**: {lib['description']}\n")
            f.write(f"- **URL**: {lib['url']}\n")
            f.write(f"- **Version**: {lib['version']}\n\n")

    print(f"✅ Saved formatted report to {output_md}")

    print("\n🎉 Scraping complete!")

if __name__ == "__main__":
    asyncio.run(main())
