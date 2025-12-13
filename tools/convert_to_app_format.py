#!/usr/bin/env python3
"""
Convert awesome_python_libraries.json to the app's libraries.js format
"""

import json

# Load the extracted libraries
with open('awesome_python_libraries.json', 'r', encoding='utf-8') as f:
    libraries = json.load(f)

print(f"Loaded {len(libraries)} libraries")

# Convert to app format (n, c, d, l)
app_format = []
for lib in libraries:
    # Clean description
    desc = lib['description'].replace('"', '\\"').replace('\n', ' ')
    if len(desc) > 150:
        desc = desc[:147] + "..."

    # Use app_category if available, otherwise category
    category = lib.get('app_category', lib.get('category', 'Utilities'))

    app_format.append({
        'n': lib['name'],
        'c': category,
        'd': desc,
        'l': lib['url']
    })

print(f"Converted {len(app_format)} libraries")

# Generate JavaScript code
js_code = "// Python Libraries Data\n"
js_code += "// Auto-generated from awesome-python collection\n\n"
js_code += "export const rawLibraries = [\n"

for i, lib in enumerate(app_format):
    comma = "," if i < len(app_format) - 1 else ""
    js_code += f'    {{ n: "{lib["n"]}", c: "{lib["c"]}", d: "{lib["d"]}", l: "{lib["l"]}" }}{comma}\n'

js_code += "];\n\n"

# Add domain mapping
js_code += """// Domain mapping for categorization
export const domainMap = {
    "Web Frameworks": "Web", "HTTP Clients": "Web", "Web Content Extracting": "Web",
    "Web Crawling": "Web", "WebSocket": "Web", "WSGI Servers": "Web",
    "RESTful API": "Web", "ASGI Servers": "Web",

    "Data Analysis": "Data Science", "Science": "Data Science",
    "Data Visualization": "Data Science", "Machine Learning": "Data Science",
    "Deep Learning": "Data Science", "Natural Language Processing": "Data Science",
    "Computer Vision": "Data Science",

    "Data Engineering": "Data Engineering", "ORM": "Data Engineering",
    "Database": "Data Engineering", "Database Drivers": "Data Engineering",
    "Distributed Computing": "Data Engineering", "Task Queues": "Data Engineering",

    "Job Scheduler": "DevOps", "DevOps Tools": "DevOps",
    "Build Tools": "DevOps", "Processes": "DevOps",

    "GUI Development": "Interface", "Game Development": "Interface",

    "Image Processing": "Media", "Video": "Media", "Audio": "Media",
    "Design": "Media",

    "Testing": "Development Tools", "Code Analysis": "Development Tools",
    "Debugging Tools": "Development Tools", "Logging": "Development Tools",
    "Command-line Tools": "Development Tools",

    "Security": "Security", "Cryptography": "Security", "Authentication": "Security",

    "Utilities": "Utilities"
};
"""

# Save to file
output_file = 'assets/data/libraries.js'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(js_code)

print(f"\n✅ Saved {len(app_format)} libraries to {output_file}")

# Print stats by category
categories = {}
for lib in app_format:
    cat = lib['c']
    categories[cat] = categories.get(cat, 0) + 1

print(f"\n📊 Libraries by Category:")
for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
    print(f"   {cat}: {count}")

print(f"\nTotal: {len(app_format)} libraries")
