#!/usr/bin/env python3
"""
Generate enhanced plain language descriptions for all Python libraries.
This script extracts library data and creates prompts for AI enhancement.
"""

import json
import re

def extract_libraries_from_js(filepath):
    """Extract library objects from the libraries.js file."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Find all library objects using regex
    # Pattern: { n: "name", c: "category", d: "description", l: "link" }
    pattern = r'\{\s*n:\s*"([^"]+)",\s*c:\s*"([^"]+)",\s*d:\s*"([^"]+)",\s*l:\s*"([^"]+)"\s*\}'
    matches = re.findall(pattern, content)

    libraries = []
    for match in matches:
        libraries.append({
            'name': match[0],
            'category': match[1],
            'description': match[2],
            'link': match[3]
        })

    return libraries

def create_batch_file(libraries, batch_num, batch_size=50):
    """Create a JSON file with a batch of libraries for processing."""
    start_idx = batch_num * batch_size
    end_idx = min(start_idx + batch_size, len(libraries))
    batch = libraries[start_idx:end_idx]

    filename = f'batch_{batch_num + 1}_libs.json'
    with open(filename, 'w') as f:
        json.dump(batch, f, indent=2)

    print(f"Created {filename} with {len(batch)} libraries (#{start_idx + 1} to #{end_idx})")
    return filename

def main():
    # Extract all libraries
    libraries = extract_libraries_from_js('../assets/data/libraries.js')
    print(f"Extracted {len(libraries)} libraries from libraries.js")

    # Create batch files (50 libraries each)
    batch_size = 50
    num_batches = (len(libraries) + batch_size - 1) // batch_size

    print(f"\nCreating {num_batches} batch files...")
    batch_files = []
    for i in range(num_batches):
        filename = create_batch_file(libraries, i, batch_size)
        batch_files.append(filename)

    print(f"\n✓ Created {len(batch_files)} batch files:")
    for bf in batch_files:
        print(f"  - {bf}")

    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("="*60)
    print("1. Process each batch file with AI to generate better descriptions")
    print("2. Merge enhanced descriptions back into libraries.js")
    print("3. Test the updated descriptions in the app")
    print("\nBatch files are ready for processing!")

if __name__ == '__main__':
    main()
