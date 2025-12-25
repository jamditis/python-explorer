---
name: codebase-navigator
description: Expert knowledge for understanding Python Explorer's architecture, finding code locations, and making targeted modifications. Use when orienting to the codebase or planning changes.
---

# CODEBASE NAVIGATOR

## When to Activate

- First time working on this project
- Finding where to make specific changes
- Understanding how components connect
- Planning architectural modifications
- Debugging cross-module issues

## Project Map

```
/home/user/python-explorer/
├── /docs                          # GitHub Pages root (deployed)
│   ├── index.html                # Entry point (1400+ lines)
│   ├── /assets
│   │   ├── /js
│   │   │   ├── app.js            # Core logic (489 lines)
│   │   │   ├── charts.js         # Chart.js (110 lines)
│   │   │   ├── modal.js          # Detail modal (59 lines)
│   │   │   ├── comparator.js     # Compare tool (67 lines)
│   │   │   └── natural-search.js # NLP interface (174 lines)
│   │   ├── /data
│   │   │   ├── libraries.js      # Library database (382 lines)
│   │   │   └── collections.js    # Curated sets
│   │   └── /css
│   │       └── styles.css        # Custom styles
│   └── /guides                   # Educational content
│
├── /tools                         # Python scripts
│   ├── extract_from_awesome.py   # Parse awesome-python
│   ├── integrate_libraries.py    # Find new libraries
│   └── *.json                    # Batch data files
│
├── .clinerules                    # Development rules
├── .clinerules-lessons            # Lessons learned
└── CLAUDE.md                      # Project documentation
```

## Module Responsibilities

### app.js — Core Application

**Owns**: State, rendering, filtering, event handling

```javascript
// Key exports
export const libraries;      // Processed library array
export const state;          // Application state
export const domainColors;   // Color mapping

// Key functions
init()                    // Bootstrap app
renderGrid()             // Main rendering
renderFilters()          // Category sidebar
toggleFilter()           // Category toggle
filterByCollection()     // Collection filter
filterJournalismLibs()   // Journalism filter
generateRequirementsTxt()// Export pip requirements
```

**Change here for**: Search logic, filter behavior, grid rendering, state management

### charts.js — Visualizations

**Owns**: Chart.js initialization and updates

```javascript
// Key functions
initCharts(libraries)         // Create both charts
updateCharts(filteredLibs)    // Update with new data
```

**Change here for**: Chart appearance, new chart types, data aggregation

### modal.js — Detail View

**Owns**: Library detail popup

```javascript
// Key functions
openModal(id, libraries)  // Open with library data
closeModal()              // Close popup
copyInstall()             // Copy pip command
```

**Change here for**: Modal content, layout, copy behavior

### comparator.js — Comparison Tool

**Owns**: Side-by-side library comparison

```javascript
// Key functions
initComparator(libraries) // Setup dropdowns and handlers
```

**Change here for**: Comparison metrics, table layout

### natural-search.js — Guided Search

**Owns**: "I have" / "I want to" interface

```javascript
// Key exports
export const searchTemplates;   // Search options
export const quickSearches;     // Quick buttons

// Key functions
initNaturalSearch(callback)  // Setup UI
```

**Change here for**: Search templates, quick search buttons

### libraries.js — Data Layer

**Owns**: Raw library data and domain mapping

```javascript
// Key exports
export const rawLibraries;  // Array of {n,c,d,l}
export const domainMap;     // Category → Domain
```

**Change here for**: Library entries, category mapping

### collections.js — Curated Sets

**Owns**: Featured collection definitions

```javascript
// Key exports
export const collections;  // Array of collection objects
```

**Change here for**: Collections, themes, library groupings

## Data Flow

```
User Interaction
       ↓
Event Handler (app.js)
       ↓
State Update
       ↓
renderGrid() ─────────→ updateCharts()
       ↓                      ↓
DOM Update           Chart.js Update
       ↓
lucide.createIcons()
```

## Finding Code by Feature

### Search Functionality

- **Input handler**: `app.js:107-111`
- **Fuse.js config**: `app.js:65-75`
- **Fuzzy matching**: `app.js:347-355`

### Category Filters

- **Checkbox rendering**: `app.js:renderFilters()`
- **Toggle handler**: `app.js:toggleFilter()`
- **Filter application**: `app.js:357-362`

### Journalism Toolkit

- **Filter function**: `app.js:filterJournalismLibs()`
- **Tag matching**: Direct `includes('[JOURNALISM]')`
- **Tag stripping**: `app.js:375`, `modal.js:20`

### Collections

- **Rendering**: `app.js:renderCollections()`
- **Accordion toggle**: `app.js:toggleAccordion()`
- **Filter handler**: `app.js:filterByCollection()`

### Charts

- **Initialization**: `charts.js:initCharts()`
- **Update trigger**: `app.js:renderGrid()` → `updateCharts()`
- **Domain aggregation**: `charts.js:11-12`, `85-86`

### Modal

- **Open trigger**: Grid card onclick → `openModal()`
- **Data population**: `modal.js:18-27`
- **Close handlers**: `modal.js:36-42`, `55`

## Color System

### Defined in app.js

```javascript
export const domainColors = {
    "Web": "#ccff00",           // acid
    "Data Science": "#00f0ff",  // ice
    "Machine Learning": "#ff2a2a", // signal
    // ...
};
```

### Applied in

- **Grid cards**: `app.js:378-400`
- **Charts**: `charts.js:21`, `56`
- **Collections**: `app.js:148-158`

## State Management

### State Object Location

`app.js:48-54`

### State Clearing Locations

| Location | Clears |
|----------|--------|
| `app.js:110-111` | collection, journalism (on search) |
| `app.js:302-303` | collection, journalism (on category) |
| `app.js:218-220` | search, categories, journalism (on collection) |
| `app.js:426-429` | search, categories, collection (on journalism) |

## External Dependencies

All loaded via CDN in index.html:

- **TailwindCSS**: Styling
- **Chart.js**: Visualizations
- **Fuse.js**: Fuzzy search
- **Lucide**: Icons
- **Google Fonts**: Typography

## Common Modification Patterns

### Adding a New Filter Type

1. Add state property in `app.js:48-54`
2. Add clearing logic in other filter handlers
3. Add filter logic in `renderGrid()`
4. Create UI element in index.html
5. Add event handler
6. Test all combinations

### Adding a New Chart

1. Add canvas element in index.html
2. Initialize in `charts.js:initCharts()`
3. Update in `charts.js:updateCharts()`
4. Ensure correct data aggregation

### Adding Library Fields

1. Add field to `libraries.js` entries
2. Process in `app.js:10-35` if computed
3. Display in `modal.js:openModal()`
4. Update grid card template if needed

## Development Workflow

```bash
# Start local server
python3 -m http.server 3000

# Access site
open http://localhost:3000/docs/index.html

# Hard refresh after JS changes
Cmd+Shift+R (Mac) / Ctrl+Shift+R (Windows)
```

## Quick Reference

| Task | File | Function/Line |
|------|------|---------------|
| Add library | libraries.js | rawLibraries array |
| Add collection | collections.js | collections array |
| Change search | app.js | Fuse config, renderGrid |
| Change filters | app.js | toggleFilter, renderGrid |
| Change charts | charts.js | initCharts, updateCharts |
| Change modal | modal.js | openModal |
| Change comparison | comparator.js | initComparator |
| Change NLP search | natural-search.js | searchTemplates |

---
**Version**: 1.0
**Last Updated**: 2025-12-25
