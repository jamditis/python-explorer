# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Python Explorer** is a modular static web application that provides an interactive directory of Python libraries across various domains (Web, Data Science, Machine Learning, DevOps, Automation, Design, Media, Visualization). Built with vanilla JavaScript ES6 modules, TailwindCSS CDN, Chart.js, and Fuse.js for fuzzy search.

**Live Site**: https://jamditis.github.io/python-explorer/
**Repository**: https://github.com/jamditis/python-explorer

## Quick Start

### Local Development
```bash
python3 -m http.server 3000
# Open http://localhost:3000/docs/index.html
```

### Key Files to Know
- `docs/index.html` - Main entry point (deployed to GitHub Pages)
- `docs/assets/js/app.js` - Core application logic and state management
- `docs/assets/js/charts.js` - Dynamic Chart.js visualizations
- `docs/assets/data/libraries.js` - Main library database (345+ entries)
- `docs/assets/data/collections.js` - Curated featured collections
- `.clinerules` - Comprehensive development rules and patterns
- `.clinerules-lessons` - Lessons learned during development

**IMPORTANT**: Always read `.clinerules` and `.clinerules-lessons` before making changes!

## Architecture

### GitHub Pages Structure
- **All public files live in `/docs`** for GitHub Pages deployment
- Entry point: `docs/index.html`
- No build process - static ES6 modules served directly
- Works immediately on push to main branch

### ES6 Module System
JavaScript split into logical modules:
- `app.js` - State management, grid rendering, filtering, search
- `charts.js` - Chart.js initialization and dynamic updates
- `comparator.js` - Side-by-side library comparison
- `modal.js` - Library detail modal with install instructions
- `natural-search.js` - Natural language search processing

### Data Files
- `libraries.js` - Array of 345+ libraries with metadata
- `collections.js` - 10 curated collections (e.g., "DATA JOURNALISM TOOLKIT")

## Design System

### Color Palette & Domain Mapping
```javascript
// Primary colors
acid: #ccff00    (yellow/lime)
signal: #ff2a2a  (red)
ice: #00f0ff     (cyan)
chrome: #e5e5e5  (light gray)

// Domain-to-color mapping
Web → acid
Data Science → ice
Machine Learning → signal
DevOps → signal
Visualization → ice
```

**Color coding is applied to:**
- Library card borders and icons
- Chart bars
- Hover states
- Domain labels

### Typography Rules
- **ALL CAPS**: Section headers, subheads, buttons, labels
  - Examples: "PYTHON_ECOSYSTEM", "FEATURED COLLECTIONS", "BROWSE THE ECOSYSTEM"
- **Sentence case**: Body text, descriptions
- **NEVER title case**: Don't Use This Style

### Design Constraints
- ❌ **NO custom cursors** - Always use browser defaults
- ✅ Subtle effects (CRT scanline max opacity: 0.12)
- ✅ High contrast for accessibility
- ✅ Notched corners via clip-path
- ✅ Color-coded visual hierarchy

## State Management

### Application State Object
```javascript
state = {
    search: "",              // Global search term (fuzzy search via Fuse.js)
    activeCategories: [],    // Multi-select category filters
    sortBy: "relevance",     // Sort mode
    journalismFilter: false, // Special journalism toolkit filter
    activeCollection: null   // Currently selected featured collection
}
```

### Critical State Rules
When changing filters, **always clear conflicting state**:

```javascript
// Search input changes
state.search = newValue;
state.activeCollection = null;
state.journalismFilter = false;

// Category filter toggles
state.activeCategories.push(category);
state.activeCollection = null;
state.journalismFilter = false;

// Journalism filter activates
state.journalismFilter = true;
state.search = "";
state.activeCollection = null;
state.activeCategories = [];
```

## Data Structure

### Raw Library Format
```javascript
{
    n: "LibraryName",           // Name
    c: "Category Name",         // Category (maps to domain)
    d: "Description [JOURNALISM]", // Description (may contain hidden tags)
    l: "https://link.com/"      // Documentation/repo link
}
```

### Runtime Enhancement
Processed at runtime to add:
- `domain` - Higher-level grouping (Web, Data Science, etc.)
- `popularity` - Calculated score (60-100)
- `install` - Generated pip install command
- `snippet` - Basic import example
- `id` - Unique identifier

### Hidden Tags
- Use `[JOURNALISM]` in descriptions for filtering
- **MUST strip tags before displaying to users**:
  ```javascript
  const cleanDescription = lib.description.replace(/\[JOURNALISM\]\s*/g, '');
  ```
- Tags exist only for internal filtering logic

## Key Features

### Filtering System
1. **Fuzzy Search** (Fuse.js) - Threshold 0.4, searches name/description/domain/category
2. **Category Filters** - Multi-select checkboxes in sidebar
3. **Featured Collections** - Accordion-style curated sets
4. **Journalism Toolkit** - Direct tag matching (NOT fuzzy search)

### Dynamic Charts
- **Domain Distribution** - Doughnut chart showing library counts by domain
- **Category Breakdown** - Color-coded bar chart of top 10 categories
- **Updates automatically** when filters change via `updateCharts(filteredLibraries)`

### User Actions
- **Browse ecosystem** - Scrolls to explorer grid
- **Submit library** - Links to GitHub issue creation
- **View toolkit** - Filters journalism-tagged libraries
- **Export requirements.txt** - Downloads pip requirements for filtered set
- **Compare libraries** - Side-by-side comparison tool

## Development Patterns

### Adding New Libraries

#### Manual Addition
Edit `docs/assets/data/libraries.js`:
```javascript
{
    n: "NewLibrary",
    c: "Existing Category",  // Must exist in domainMap
    d: "Brief description of what it does.",
    l: "https://docs.url/"
}
```

Add `[JOURNALISM]` tag if relevant for journalism/media work.

#### Bulk Import
```bash
python3 tools/extract_from_awesome.py
python3 tools/integrate_libraries.py
# Review integration_report.md
# Copy from new_libraries_snippet.txt to libraries.js
```

### Creating New Collections
Edit `docs/assets/data/collections.js`:
```javascript
{
    "name": "COLLECTION NAME",  // ALL CAPS
    "description": "Brief description.",
    "icon": "lucide-icon-name",
    "color": "acid|ice|signal",
    "libraries": ["lib1", "lib2", "lib3"]
}
```

### Modifying UI
- **Search logic**: `docs/assets/js/app.js` → `renderGrid()`
- **Filter toggles**: `docs/assets/js/app.js` → `toggleFilter()`
- **Chart config**: `docs/assets/js/charts.js` → `initCharts()` and `updateCharts()`
- **Modal content**: `docs/assets/js/modal.js` → `openModal()`

### Updating Charts
Charts MUST update with filtered data:
```javascript
function renderGrid() {
    // ... filtering logic ...
    updateCharts(filtered);  // Always call this!
}
```

## Common Pitfalls (Read .clinerules-lessons for details)

1. ❌ Don't use fuzzy search for tag-based filtering
2. ❌ Don't show `[JOURNALISM]` tags to users
3. ❌ Don't forget to clear conflicting state flags
4. ❌ Don't use title case for headings
5. ❌ Don't create static charts that don't update
6. ❌ Don't hardcode colors - use domain color mapping
7. ❌ Don't skip `target="_blank" rel="noopener noreferrer"` on external links
8. ❌ Don't forget hard refresh (Cmd+Shift+R) when testing ES6 module changes

## Dependencies (All CDN)

- **TailwindCSS 3.x** - Utility-first CSS framework
- **Chart.js** - Data visualization
- **Fuse.js** - Fuzzy search
- **Lucide Icons** - Icon library
- **Google Fonts** - Chakra Petch (display), Share Tech Mono (monospace)

## Git Workflow

### Commit Format
```
Brief imperative summary

- Bullet point changes
- Another change
- More details

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Deployment
- Push directly to `main` branch
- GitHub Pages automatically deploys from `/docs`
- Changes go live within 1-2 minutes

## External Links

- **Submit Library**: https://github.com/jamditis/python-explorer/issues/new
- **awesome-python source**: https://github.com/vinta/awesome-python

## Testing Checklist

Before pushing changes:

- [ ] Test all filter combinations (search + categories + collections + journalism)
- [ ] Verify charts update when filters change
- [ ] Check that `[JOURNALISM]` tags are hidden from users
- [ ] Confirm color coding appears correctly
- [ ] Test on mobile (responsive design)
- [ ] Hard refresh to clear module cache
- [ ] Verify external links open in new tab with security attributes
- [ ] Check that ALL CAPS is used for section headers
- [ ] Ensure descriptions use sentence case

## Performance Notes

- Handles 345+ libraries smoothly
- Fuzzy search is efficient with threshold 0.4
- Charts update without full page re-render
- No build step = fast deployment
- Aggressive browser caching of ES6 modules (use hard refresh in dev)

## Accessibility

- High contrast color scheme (WCAG AA compliant)
- Semantic HTML structure
- Keyboard navigation (/ key opens search)
- Clear focus states
- Screen reader friendly labels

## Content Guidelines

### Writing Descriptions
- Beginner-friendly language
- Focus on practical use cases
- 1-3 sentences maximum
- Avoid marketing fluff
- No superlatives ("best", "amazing", etc.)

### Disclaimer
Project maintains disclaimer that Joe Amditis does not endorse any libraries - this is purely an exploration tool.

## Next Steps / TODO

Potential future enhancements (see `.clinerules-lessons` for full list):
- Library version tracking
- "Recently updated" filter
- URL-based saved filter states
- Library comparison matrix expansion
- Community ratings/reviews
- Analytics tracking (most viewed domains)
- "Related libraries" suggestions

## Support

For issues or feature requests:
- Create GitHub issue: https://github.com/jamditis/python-explorer/issues/new
- Review `.clinerules` for development patterns
- Check `.clinerules-lessons` for common solutions

## Project Stats

- **345+ libraries** across 9 domains
- **10 curated collections** including journalism toolkit
- **Zero build process** - pure static site
- **Mobile responsive** via TailwindCSS
- **Fast load times** - CDN dependencies only
- **Active development** - continuously updated

---

**Remember**: Always read `.clinerules` and `.clinerules-lessons` before making changes. They contain critical patterns and lessons learned that will save you time and prevent bugs!
