---
name: library-manager
description: Expert knowledge for adding, editing, and validating Python library entries in the Python Explorer database. Use when modifying docs/assets/data/libraries.js.
---

# LIBRARY MANAGER

## When to Activate

- Adding new libraries to the database
- Editing existing library entries
- Bulk importing libraries from external sources
- Validating library data integrity
- Troubleshooting library display issues

## Mental Model

Think like a **data curator** maintaining a beginner-friendly library catalog. Every entry must be:
- Discoverable (correct category mapping)
- Accessible (clear descriptions)
- Accurate (working links, real packages)
- Clean (no internal metadata leaking to users)

## Data Structure

### Source Format (libraries.js)

```javascript
{
    n: "LibraryName",           // Exact name (case-sensitive)
    c: "Category Name",         // Must exist in domainMap
    d: "Description text",      // 1-3 sentences, beginner-friendly
    l: "https://docs.url/"      // Documentation or repo URL
}
```

### Runtime Enhancement

Libraries are enhanced at runtime in app.js:
- `domain` - Mapped from category via domainMap
- `popularity` - Calculated score (60-100)
- `install` - Generated: `pip install {name.toLowerCase()}`
- `snippet` - Generated: `import {module_name}`
- `id` - Unique identifier

## Valid Categories

Categories **must** match domainMap keys exactly:

| Domain | Categories |
|--------|------------|
| Web | Web Frameworks, HTTP Clients, Web Content Extracting, Web Crawling, WebSocket, WSGI Servers, RESTful API, ASGI Servers |
| Data Science | Data Analysis, Data Visualization, Science, Machine Learning, Deep Learning, Natural Language Processing, Computer Vision |
| Data Engineering | Data Engineering, ORM, Database, Database Drivers, Distributed Computing, Task Queues |
| DevOps | Job Scheduler, DevOps Tools, Build Tools, Processes |
| Interface | GUI Development, Game Development |
| Media | Image Processing, Video, Audio, Design |
| Development Tools | Testing, Code Analysis, Debugging Tools, Logging, Command-line Tools |
| Security | Security, Cryptography, Authentication |
| Utilities | Utilities (catch-all) |

## Adding a Library

### Single Entry

```javascript
// In docs/assets/data/libraries.js, add to rawLibraries array:
{
    n: "pandas",
    c: "Data Analysis",
    d: "Makes it easy to work with spreadsheet-like data—sort, filter, analyze, and create charts all in code.",
    l: "http://pandas.pydata.org/"
}
```

### Checklist

- [ ] Name is exact (case-sensitive, matches PyPI)
- [ ] Category exists in domainMap
- [ ] Description is beginner-friendly (no jargon)
- [ ] Description is 1-3 sentences max
- [ ] URL works and is HTTPS preferred
- [ ] No duplicate (case-insensitive check)

## Hidden Tags

### Journalism Tag

Add `[JOURNALISM]` suffix for journalism/media-relevant libraries:

```javascript
d: "Description text. [JOURNALISM]"
```

**Rules:**
- Tag appears in source data ONLY
- Always stripped before display
- Use for: data journalism, scraping, document processing, visualization, media handling
- 39 libraries currently tagged

**Never show tags to users.** Stripping happens in:
- `app.js:375` (grid cards)
- `modal.js:20` (detail modal)

## Validation Patterns

### Check for Duplicates

```javascript
const exists = rawLibraries.some(lib =>
    lib.n.toLowerCase() === newLib.n.toLowerCase()
);
```

### Verify Category

```javascript
const validCategory = Object.keys(domainMap).includes(newLib.c);
```

### Description Length

Target: 50-150 characters, beginner-friendly

## Bulk Import Process

1. Use `tools/extract_from_awesome.py` to generate JSON
2. Use `tools/integrate_libraries.py` to find new libraries
3. Review `integration_report.md`
4. Copy from `new_libraries_snippet.txt` to libraries.js
5. Add journalism tags manually where relevant
6. Test with hard refresh (Cmd+Shift+R)

## Anti-Patterns

| Don't | Do |
|-------|-----|
| Invent categories | Use exact domainMap keys |
| Use marketing language | Write like you're explaining to a friend |
| Include `[JOURNALISM]` in display | Strip before rendering |
| Assume pip package name | Verify on PyPI |
| Forget duplicate check | Case-insensitive comparison |

## Troubleshooting

### Library Not Appearing

1. Check category exists in domainMap
2. Hard refresh browser (Cmd+Shift+R)
3. Check for JavaScript syntax errors in console
4. Verify array comma placement

### Wrong Domain Color

- Category doesn't map to expected domain
- Check domainMap in libraries.js

### Fuzzy Search Not Finding

- Description too short
- Fuse.js threshold is 0.4 (needs 60% match)

## File Locations

- **Library data**: `/docs/assets/data/libraries.js`
- **Domain mapping**: Same file, `domainMap` export
- **Processing app.js**: `/docs/assets/js/app.js` (lines 10-35)
- **Import tools**: `/tools/*.py`

---
**Version**: 1.0
**Last Updated**: 2025-12-25
