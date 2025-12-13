#!/usr/bin/env python3
"""
Library Integration Tool
Helps compare and integrate newly discovered libraries with existing ones
"""

import json
import re

def load_existing_libraries_from_html(html_file='index.html'):
    """Extract existing libraries from index.html"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the rawLibraries array
    match = re.search(r'const rawLibraries = \[(.*?)\];', content, re.DOTALL)
    if not match:
        print("❌ Could not find rawLibraries array in HTML")
        return []

    array_content = match.group(1)

    # Parse library objects
    existing = []
    pattern = r'\{\s*n:\s*"([^"]+)",\s*c:\s*"([^"]+)",\s*d:\s*"([^"]+)",\s*l:\s*"([^"]+)"\s*\}'

    for match in re.finditer(pattern, array_content):
        existing.append({
            'name': match.group(1),
            'category': match.group(2),
            'description': match.group(3),
            'link': match.group(4)
        })

    return existing

def find_new_libraries(existing, discovered_file='awesome_python_libraries.json'):
    """Find libraries that aren't in the existing collection"""
    try:
        with open(discovered_file, 'r', encoding='utf-8') as f:
            discovered = json.load(f)
    except FileNotFoundError:
        print(f"❌ {discovered_file} not found. Run extract_from_awesome.py first!")
        return []

    # Create set of existing library names (lowercase for comparison)
    existing_names = {lib['name'].lower() for lib in existing}

    # Find new libraries
    new_libs = []
    for lib in discovered:
        if lib['name'].lower() not in existing_names:
            new_libs.append(lib)

    return new_libs

def generate_html_snippet(libraries):
    """Generate HTML snippet for adding to index.html"""
    snippet = []

    for lib in libraries:
        # Clean up the description for HTML
        desc = lib['description'].replace('"', '\\"')

        # Truncate long descriptions
        if len(desc) > 150:
            desc = desc[:147] + "..."

        # Use app_category if available, otherwise category
        category = lib.get('app_category', lib.get('category', 'Utilities'))

        snippet.append(
            f'{{ n: "{lib["name"]}", c: "{category}", d: "{desc}", l: "{lib["url"]}" }},'
        )

    return "\n            ".join(snippet)

def main():
    """Main integration process"""
    print("=" * 60)
    print("Library Integration Tool")
    print("=" * 60)

    # Load existing libraries
    print("\n📖 Loading existing libraries from index.html...")
    existing = load_existing_libraries_from_html()
    print(f"   Found {len(existing)} existing libraries")

    # Load discovered libraries
    print("\n🔍 Loading discovered libraries from PyPI...")
    new_libs = find_new_libraries(existing)
    print(f"   Found {len(new_libs)} new libraries not in current collection")

    if not new_libs:
        print("\n✅ No new libraries to add! Your collection is comprehensive.")
        return

    # Group by category
    by_category = {}
    for lib in new_libs:
        cat = lib.get('app_category', lib.get('category', 'Utilities'))
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(lib)

    # Print summary
    print("\n📊 New Libraries by Category:")
    for cat in sorted(by_category.keys()):
        print(f"   {cat}: {len(by_category[cat])}")

    # Generate output files
    print("\n📝 Generating integration files...")

    # 1. Full JSON of new libraries
    with open('new_libraries.json', 'w', encoding='utf-8') as f:
        json.dump(new_libs, f, indent=2, ensure_ascii=False)
    print("   ✅ Saved new_libraries.json")

    # 2. HTML snippet for easy copy-paste
    snippet = generate_html_snippet(new_libs[:50])  # Top 50 for manageability
    with open('new_libraries_snippet.txt', 'w', encoding='utf-8') as f:
        f.write("// Add these to the rawLibraries array in index.html:\n\n")
        f.write(snippet)
    print("   ✅ Saved new_libraries_snippet.txt (top 50 libraries)")

    # 3. Detailed report
    with open('integration_report.md', 'w', encoding='utf-8') as f:
        f.write("# Library Integration Report\n\n")
        f.write(f"**Existing Libraries**: {len(existing)}\n")
        f.write(f"**Newly Discovered**: {len(new_libs)}\n\n")

        f.write("## Recommended Additions\n\n")
        f.write("These are popular/well-known libraries that should be considered:\n\n")

        # Highlight some recommendations
        recommendations = []
        keywords = ['popular', 'widely', 'standard', 'official', 'production']

        for lib in new_libs:
            desc_lower = lib['description'].lower()
            if any(kw in desc_lower for kw in keywords):
                recommendations.append(lib)

        for lib in recommendations[:20]:
            f.write(f"### {lib['name']}\n")
            f.write(f"- **Category**: {lib['category']}\n")
            f.write(f"- **Description**: {lib['description']}\n")
            f.write(f"- **URL**: {lib['url']}\n\n")

        f.write("\n## All New Libraries by Category\n\n")

        for cat in sorted(by_category.keys()):
            f.write(f"\n### {cat} ({len(by_category[cat])})\n\n")
            for lib in sorted(by_category[cat], key=lambda x: x['name']):
                f.write(f"- **{lib['name']}**: {lib['description']}\n")

    print("   ✅ Saved integration_report.md")

    print("\n🎉 Integration files generated!")
    print("\n📋 Next steps:")
    print("   1. Review integration_report.md for recommended additions")
    print("   2. Copy relevant entries from new_libraries_snippet.txt")
    print("   3. Paste into the rawLibraries array in index.html")
    print("   4. Refresh your browser to see the new libraries")

if __name__ == "__main__":
    main()
