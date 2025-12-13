# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Python Explorer** is a modular static web application that provides an interactive directory of Python libraries across various domains (Web, Data Science, Machine Learning, DevOps, Automation, Design, Media, Visualization). Built with vanilla JavaScript ES6 modules, TailwindCSS CDN, and Chart.js.

## Architecture

### Modular Structure (Recommended: index-v2.html)
- **Separation of concerns** - HTML, CSS, and JS properly separated
- **ES6 Modules** - JavaScript split into logical modules (app.js, charts.js, comparator.js, modal.js)
- **No build process** - Direct ES6 module imports, works in modern browsers
- **External data** - Library data in separate file (assets/data/libraries.js)
- **CDN dependencies** - TailwindCSS, Chart.js, Lucide icons, Google Fonts

### File Structure
```
assets/
  css/styles.css      - Custom cyberpunk styles and animations
  js/
    app.js           - Main application logic, state management, grid rendering
    charts.js        - Chart.js initialization for analytics dashboard
    comparator.js    - Side-by-side library comparison functionality
    modal.js         - Library detail modal
  data/
    libraries.js     - Python libraries data array (exported as ES6 module)
```

### Legacy Version (index.html)
- **Single-file** - All code embedded in one HTML file
- **Kept for reference** - Original monolithic version
- **Use index-v2.html** for new development

### Data Structure
The application uses a hardcoded array of library objects (`rawLibraries`) embedded in the JavaScript. Each library has:
- `n`: Name
- `c`: Category (e.g., "Web Frameworks", "Data Analysis")
- `d`: Description
- `l`: Link to documentation/repository

At runtime, this is processed into a richer structure with:
- `domain`: Higher-level grouping (Web, Data Science, etc.) mapped via `domainMap`
- `popularity`: Calculated score (60-100 range) based on description keywords
- `install`: Generated pip install command
- `snippet`: Basic import code example

### Key Components

**State Management** (line ~627):
```javascript
let state = {
    search: "",              // Global search term
    activeCategories: [],    // Selected category filters
    sortBy: "relevance"      // Sort mode (not fully implemented)
}
```

**Main Functions**:
- `renderGrid()` (~719): Filters and displays library cards based on state
- `renderFilters()` (~676): Generates category checkboxes in sidebar
- `initCharts()` (~771): Creates Chart.js visualizations (domain distribution pie chart, popularity bar chart)
- `initComparator()` (~833): Powers side-by-side library comparison tool
- `openModal(id)` (~910): Shows detailed library information in modal overlay

### UI Features
- **Global search**: Filters by name, description, or domain (keyboard shortcut: `/`)
- **Category filters**: Multi-select sidebar with live counts
- **Dashboard**: Visual analytics with Chart.js (domain distribution, top frameworks)
- **Comparison matrix**: Side-by-side library comparison tool
- **Modal system**: Detailed view with install instructions and code snippets

### Design System
Custom cyberpunk aesthetic with:
- **Color Palette**:
  - `acid` (#ccff00) - primary accent
  - `signal` (#ff2a2a) - secondary accent
  - `ice` (#00f0ff) - tertiary accent
  - `void`/`panel`/`surface` - dark backgrounds
- **Custom Elements**: Notched corners (clip-path), CRT scanline overlay, glitch text animations
- **Typography**: "Chakra Petch" display font, "Share Tech Mono" monospace

## Development

### Local Development
```bash
# Serve the application locally
python3 -m http.server 3000

# Then open http://localhost:3000/index-v2.html
```

### Testing Changes
Modular structure allows targeted updates:
1. **Styling changes**: Edit `assets/css/styles.css`
2. **Data updates**: Edit `assets/data/libraries.js`
3. **Logic changes**: Edit relevant JS module in `assets/js/`
4. Refresh browser to see changes (browsers cache ES6 modules, may need hard refresh)

### Adding New Libraries

#### Option 1: Manual Addition
Edit `assets/data/libraries.js` and add entries to the `rawLibraries` array:
```javascript
{
    n: "LibraryName",
    c: "Category Name",  // Must match existing category or update domainMap
    d: "Description text",
    l: "https://link-to-docs.com/"
}
```

Update `domainMap` (line ~498) if adding a new category to assign it to a domain.

#### Option 2: Bulk Import from awesome-python
Use the provided Python tools:
```bash
# Extract all libraries from awesome-python-collection.md
python3 tools/extract_from_awesome.py

# Compare with existing and generate integration snippets
python3 tools/integrate_libraries.py

# Review integration_report.md for recommendations
# Copy from new_libraries_snippet.txt to assets/data/libraries.js
```

### Modifying UI Behavior
- **Search logic**: `assets/js/app.js` - `renderGrid()` function
- **Filter behavior**: `assets/js/app.js` - `toggleFilter()` and `renderActiveFilters()`
- **Modal content**: `assets/js/modal.js` - `openModal()` function
- **Chart configuration**: `assets/js/charts.js` - `initCharts()` function
- **Comparison tool**: `assets/js/comparator.js` - `initComparator()` function

## Data Source

The project includes `awesome-python-collection.md` - a curated list of Python libraries from the [awesome-python](https://github.com/vinta/awesome-python) repository. This serves as a reference but is **not dynamically loaded** by the application. The `assets/data/libraries.js` contains a manually curated subset of libraries.

## Tools

### Python Utilities (in root directory)
- **extract_from_awesome.py** - Parses awesome-python-collection.md and extracts library data
- **integrate_libraries.py** - Compares extracted data with existing libraries, generates integration snippets
- **pypi_simple_scraper.py** - Experimental PyPI scraper (requires requests, beautifulsoup4)

### Workflow for Adding Libraries
1. Run `extract_from_awesome.py` to parse the awesome-python markdown
2. Run `integrate_libraries.py` to identify new libraries
3. Review `integration_report.md` for recommended additions
4. Copy relevant entries from `new_libraries_snippet.txt`
5. Paste into `assets/data/libraries.js` rawLibraries array

## Deployment

### GitHub Pages
This project is designed for GitHub Pages deployment:

1. Rename `index-v2.html` to `index.html` (or configure GitHub Pages to use index-v2.html)
2. Push to `gh-pages` branch or configure from main branch
3. No build process required - works immediately

### Integration with jamditis/tools
To add as a tool in the existing tools repository:
- Ensure design consistency with AMDITIS design library (already implemented)
- Create entry point following tools repo conventions
- Add navigation link in tools repo index

## Notes

- **Browser compatibility**: Requires ES6 module support (all modern browsers)
- **Dependencies**: All loaded from CDNs - requires internet connection
- **No backend**: Purely client-side application
- **Performance**: Handles 300+ libraries without performance issues
- **Module caching**: Browsers cache ES6 modules aggressively; use hard refresh (Cmd+Shift+R) during development
