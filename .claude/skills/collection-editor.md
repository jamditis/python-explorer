---
name: collection-editor
description: Expert knowledge for creating and editing curated library collections in Python Explorer. Use when modifying docs/assets/data/collections.js.
---

# COLLECTION EDITOR

## When to Activate

- Creating new themed collections
- Adding/removing libraries from collections
- Fixing broken collection references
- Reorganizing collection content
- Choosing appropriate collection styling

## Mental Model

Think like a **museum curator** assembling themed exhibits. Collections should:
- Tell a story (cohesive theme)
- Guide discovery (help users find related tools)
- Stay focused (4-8 libraries, not everything)
- Look consistent (follow naming/styling conventions)

## Collection Schema

```javascript
{
    "name": "COLLECTION NAME",       // ALL CAPS required
    "description": "Brief context.",  // Sentence case
    "icon": "lucide-icon-name",      // From Lucide Icons
    "color": "acid|ice|signal",      // Domain color
    "libraries": ["lib1", "lib2"]    // Exact library names
}
```

## Styling Rules

### Name Format

**Always ALL CAPS:**
```javascript
"name": "DATA JOURNALISM TOOLKIT"    // Correct
"name": "Data Journalism Toolkit"    // WRONG - title case
"name": "data journalism toolkit"    // WRONG - lowercase
```

### Colors

| Color | Hex | Use For |
|-------|-----|---------|
| acid | #ccff00 | Web, Automation, Desktop, UI |
| ice | #00f0ff | Data Science, ML, Visualization |
| signal | #ff2a2a | DevOps, Production, Real-time |

### Icons (Lucide)

Current collections use:
- `newspaper` - Journalism
- `graduation-cap` - Beginners
- `video` - Media
- `bot` - Automation
- `brain` - AI/ML
- `server` - DevOps
- `bar-chart-3` - Visualization
- `monitor` - Desktop
- `flask-conical` - Science
- `map-pin` - Geographic

Browse more: https://lucide.dev/icons/

## Current Collections

1. DATA JOURNALISM TOOLKIT (acid) - 8 libraries
2. BEGINNER-FRIENDLY STARTERS (ice) - 8 libraries
3. VIDEO & MEDIA PROCESSING (signal) - 7 libraries
4. WEB SCRAPING & AUTOMATION (acid) - 7 libraries
5. AI & MACHINE LEARNING (ice) - 8 libraries
6. PRODUCTION-READY DEVOPS (signal) - 8 libraries
7. DATA VISUALIZATION MASTERS (ice) - 8 libraries
8. DESKTOP APP DEVELOPMENT (acid) - 8 libraries
9. SCIENTIFIC COMPUTING (signal) - 8 libraries
10. GEOGRAPHIC & LOCATION TOOLS (ice) - 4 libraries

## Creating a Collection

### Step 1: Define Theme

Clear, cohesive theme that helps users discover related tools.

### Step 2: Select Libraries

```javascript
// Library names must match EXACTLY (case-sensitive)
"libraries": [
    "pandas",           // Correct
    "Pandas",           // WRONG - case mismatch
    "pandas library"    // WRONG - not the n field value
]
```

### Step 3: Choose Styling

Match color to primary domain of included libraries.

### Step 4: Add to Array

```javascript
// In docs/assets/data/collections.js
export const collections = [
    // ... existing collections
    {
        "name": "NEW COLLECTION NAME",
        "description": "What this collection helps with.",
        "icon": "icon-name",
        "color": "acid",
        "libraries": ["lib1", "lib2", "lib3", "lib4"]
    }
];
```

## Validation

### Verify Library Names

```javascript
// All library names must exist in rawLibraries
const validNames = new Set(rawLibraries.map(lib => lib.n));
const invalid = collection.libraries.filter(name => !validNames.has(name));
```

### Size Guidelines

- **Minimum**: 4 libraries (meaningful collection)
- **Optimal**: 6-8 libraries (fits UI well)
- **Maximum**: 10 libraries (avoid overwhelming)

## UI Behavior

### Accordion Display

- Collections show in accordion pattern
- One expanded at a time
- Shows first 8 libraries, "+X more" for overflow
- "View all X libraries" button filters grid

### Filter Integration

When collection selected:
```javascript
state.activeCollection = collection.name;
state.search = "";              // Cleared
state.activeCategories = [];    // Cleared
state.journalismFilter = false; // Cleared
```

## Anti-Patterns

| Don't | Do |
|-------|-----|
| Use title case in name | ALL CAPS only |
| Include 20+ libraries | Keep focused (4-8) |
| Invent color values | Use acid, ice, or signal |
| Use non-existent icons | Check Lucide docs |
| Reference wrong library names | Match n field exactly |

## Troubleshooting

### Collection Shows 0 Libraries

- Library names don't match (case-sensitive!)
- Check n field in libraries.js vs collection array

### Wrong Color Appearing

- Invalid color value
- Must be exactly: "acid", "ice", or "signal"

### Icon Not Showing

- Invalid Lucide icon name
- Call `lucide.createIcons()` after render

## Suggested New Collections

Based on library analysis:

| Name | Theme | Potential Libraries |
|------|-------|---------------------|
| API DEVELOPMENT | Building APIs | FastAPI, Flask, Django REST, Pydantic |
| DATABASE ESSENTIALS | Data persistence | SQLAlchemy, Peewee, Redis-py, PyMongo |
| TESTING TOOLKIT | Quality assurance | pytest, hypothesis, coverage, mock |
| CLI POWER TOOLS | Command-line apps | Click, Typer, Rich, Prompt Toolkit |

## File Location

- **Collections data**: `/docs/assets/data/collections.js`
- **Rendering logic**: `/docs/assets/js/app.js` (renderCollections)
- **Filter logic**: `/docs/assets/js/app.js` (filterByCollection)

---
**Version**: 1.0
**Last Updated**: 2025-12-25
