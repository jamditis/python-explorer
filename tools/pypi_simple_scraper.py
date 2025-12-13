#!/usr/bin/env python3
"""
PyPI Library Scraper - Simple Version
Uses requests and BeautifulSoup to scrape PyPI search results
"""

import json
import time
import requests
from bs4 import BeautifulSoup

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
    "plotting charts",
    "devops docker kubernetes",
    "monitoring logging",
    "cache redis",
    "queue kafka",
    "serverless lambda"
]

def scrape_pypi_search(query, max_pages=2):
    """Scrape PyPI search results for a given query"""
    libraries = []
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })

    print(f"\n🔍 Searching PyPI for: '{query}'")

    for page_num in range(1, max_pages + 1):
        url = f"https://pypi.org/search/?q={query.replace(' ', '+')}&page={page_num}"

        try:
            response = session.get(url, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

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

            # Rate limiting - be respectful to PyPI
            time.sleep(2)

        except Exception as e:
            print(f"  ❌ Error loading page {page_num}: {e}")
            break

    return libraries

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
    if any(word in desc or word in query for word in ['django', 'flask', 'fastapi', 'web framework', 'wsgi', 'asgi', 'pyramid', 'bottle', 'tornado']):
        return 'Web Frameworks'
    elif any(word in desc or word in query for word in ['pandas', 'numpy', 'data analysis', 'dataframe', 'polars']):
        return 'Data Analysis'
    elif any(word in desc or word in query for word in ['machine learning', 'ml', 'scikit', 'xgboost', 'lightgbm']):
        return 'Machine Learning'
    elif any(word in desc or word in query for word in ['deep learning', 'neural network', 'tensorflow', 'pytorch', 'keras']):
        return 'Deep Learning'
    elif any(word in desc or word in query for word in ['plot', 'chart', 'visualization', 'graph', 'matplotlib', 'seaborn', 'plotly', 'bokeh']):
        return 'Data Visualization'
    elif any(word in desc or word in query for word in ['nlp', 'natural language', 'text processing', 'spacy', 'nltk', 'transformer']):
        return 'Natural Language Processing'
    elif any(word in desc or word in query for word in ['computer vision', 'image processing', 'opencv', 'pillow', 'image']):
        return 'Computer Vision'
    elif any(word in desc or word in query for word in ['scraping', 'scraper', 'crawler', 'beautiful soup', 'scrapy']):
        return 'Web Scraping'
    elif any(word in desc or word in query for word in ['automation', 'automate', 'selenium', 'robot']):
        return 'Automation'
    elif any(word in desc or word in query for word in ['gui', 'interface', 'tkinter', 'qt', 'kivy', 'wxpython']):
        return 'GUI Development'
    elif any(word in desc or word in query for word in ['test', 'pytest', 'unittest', 'testing']):
        return 'Testing'
    elif any(word in desc or word in query for word in ['orm', 'database', 'sqlalchemy', 'sql']):
        return 'ORM'
    elif any(word in desc or word in query for word in ['api', 'rest', 'graphql']):
        return 'RESTful API'
    elif any(word in desc or word in query for word in ['cli', 'command line', 'terminal', 'argparse', 'click']):
        return 'Command-line Tools'
    elif any(word in desc or word in query for word in ['video', 'movie', 'ffmpeg']):
        return 'Video Processing'
    elif any(word in desc or word in query for word in ['game', 'pygame']):
        return 'Game Development'
    elif any(word in desc or word in query for word in ['pdf', 'reportlab']):
        return 'PDF Processing'
    elif any(word in desc or word in query for word in ['excel', 'spreadsheet', 'openpyxl']):
        return 'Spreadsheet Processing'
    elif any(word in desc or word in query for word in ['security', 'cryptography', 'encryption']):
        return 'Security'
    elif any(word in desc or word in query for word in ['devops', 'docker', 'kubernetes', 'ansible']):
        return 'DevOps'
    elif any(word in desc or word in query for word in ['http', 'requests', 'client', 'httpx']):
        return 'HTTP Clients'
    elif any(word in desc or word in query for word in ['queue', 'celery', 'task', 'job']):
        return 'Task Queues'
    elif any(word in desc or word in query for word in ['schedule', 'cron', 'timer']):
        return 'Job Scheduler'
    else:
        return 'Utilities'

def main():
    """Main scraper execution"""
    print("=" * 60)
    print("PyPI Library Scraper (Simple Version)")
    print("=" * 60)

    all_libraries = []

    # Scrape each search query
    for i, query in enumerate(SEARCH_QUERIES, 1):
        print(f"\n[{i}/{len(SEARCH_QUERIES)}]", end=" ")
        libs = scrape_pypi_search(query, max_pages=2)
        all_libraries.extend(libs)

        # Rate limiting between queries
        time.sleep(3)

    print(f"\n\n📊 Total libraries found: {len(all_libraries)}")

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
        f.write(f"Total unique libraries: {len(unique_libraries)}\n\n")

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
    main()
