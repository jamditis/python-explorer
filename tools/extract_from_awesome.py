#!/usr/bin/env python3
"""
Extract libraries from awesome-python-collection.md
This is more reliable than scraping PyPI
"""

import re
import json

def extract_libraries_from_markdown(md_file='awesome-python-collection.md'):
    """Parse the awesome-python markdown file"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    libraries = []
    current_category = None

    # Split by lines
    lines = content.split('\n')

    for line in lines:
        # Detect category headers (## Category Name)
        if line.startswith('## '):
            current_category = line[3:].strip()
            continue

        # Skip if no category yet
        if not current_category:
            continue

        # Extract library entries (bullet points with links)
        # Format: - [LibraryName](url) - Description
        match = re.match(r'-\s+\[([^\]]+)\]\(([^\)]+)\)\s+-\s+(.+)', line)
        if match:
            name = match.group(1).strip()
            url = match.group(2).strip()
            description = match.group(3).strip()

            libraries.append({
                'name': name,
                'url': url,
                'description': description,
                'category': current_category
            })

    return libraries

def categorize_for_app(category):
    """Map awesome-python categories to our app categories"""
    mapping = {
        # Web
        'Web Frameworks': 'Web Frameworks',
        'ASGI Servers': 'Web Frameworks',
        'WSGI Servers': 'Web Frameworks',
        'RESTful API': 'RESTful API',
        'WebSocket': 'WebSocket',
        'HTTP Clients': 'HTTP Clients',
        'Web Content Extracting': 'Web Content Extracting',
        'Web Crawling': 'Web Crawling',

        # Data Science
        'Data Analysis': 'Data Analysis',
        'Data Validation': 'Data Analysis',
        'Data Visualization': 'Data Visualization',
        'Science': 'Science',
        'Machine Learning': 'Machine Learning',
        'Deep Learning': 'Deep Learning',
        'Natural Language Processing': 'Natural Language Processing',
        'Computer Vision': 'Computer Vision',

        # Data Engineering
        'Database': 'Database',
        'Database Drivers': 'Database',
        'ORM': 'ORM',
        'Data Engineering': 'Data Engineering',
        'Distributed Computing': 'Distributed Computing',
        'Task Queues': 'Task Queues',

        # DevOps & Automation
        'DevOps Tools': 'DevOps Tools',
        'Job Scheduler': 'Job Scheduler',
        'Build Tools': 'Build Tools',
        'Processes': 'Processes',

        # Development Tools
        'Testing': 'Testing',
        'Code Analysis': 'Code Analysis',
        'Debugging Tools': 'Debugging Tools',
        'Logging': 'Logging',
        'Command-line Interface Development': 'Command-line Tools',
        'Command-line Tools': 'Command-line Tools',

        # GUI & Design
        'GUI Development': 'GUI Development',
        'Game Development': 'Game Development',
        'Image Processing': 'Image Processing',
        'Video': 'Video',
        'Audio': 'Audio',

        # Utilities
        'File Manipulation': 'Utilities',
        'Date and Time': 'Utilities',
        'Text Processing': 'Utilities',
        'Specific Formats Processing': 'Utilities',
        'Configuration Files': 'Utilities',
        'Caching': 'Utilities',
        'Email': 'Utilities',
        'Internationalization': 'Utilities',
        'Serialization': 'Utilities',
        'Cryptography': 'Security',
        'Authentication': 'Security',
    }

    return mapping.get(category, 'Utilities')

def main():
    print("=" * 60)
    print("Awesome Python Library Extractor")
    print("=" * 60)

    print("\n📖 Reading awesome-python-collection.md...")
    libraries = extract_libraries_from_markdown()
    print(f"   Found {len(libraries)} libraries")

    # Categorize for our app
    for lib in libraries:
        lib['app_category'] = categorize_for_app(lib['category'])

    # Get category stats
    categories = {}
    for lib in libraries:
        cat = lib['app_category']
        categories[cat] = categories.get(cat, 0) + 1

    print(f"\n📊 Category Breakdown:")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"   {cat}: {count}")

    # Save full data
    with open('awesome_python_libraries.json', 'w', encoding='utf-8') as f:
        json.dump(libraries, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Saved awesome_python_libraries.json")

    # Generate HTML snippet format
    snippet_libs = []
    for lib in libraries[:200]:  # Top 200 most relevant
        # Clean description
        desc = lib['description'].replace('"', '\\"')
        if len(desc) > 120:
            desc = desc[:117] + "..."

        snippet_libs.append({
            'n': lib['name'],
            'c': lib['app_category'],
            'd': desc,
            'l': lib['url']
        })

    with open('libraries_for_html.json', 'w', encoding='utf-8') as f:
        json.dump(snippet_libs, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved libraries_for_html.json (top 200)")

    # Generate ready-to-paste JavaScript
    js_entries = []
    for lib in snippet_libs:
        js_entries.append(
            f'{{ n: "{lib["n"]}", c: "{lib["c"]}", d: "{lib["d"]}", l: "{lib["l"]}" }}'
        )

    with open('libraries_snippet.txt', 'w', encoding='utf-8') as f:
        f.write("// Add these to rawLibraries array in index.html:\n\n")
        f.write(",\n            ".join(js_entries))

    print(f"✅ Saved libraries_snippet.txt (ready to paste)")

    print("\n🎉 Extraction complete!")
    print(f"\n📋 Next steps:")
    print("   1. Review awesome_python_libraries.json")
    print("   2. Copy content from libraries_snippet.txt")
    print("   3. Paste into rawLibraries array in index.html")

if __name__ == "__main__":
    main()
