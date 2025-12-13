# Python Explorer

![Python Explorer](style/og-image.png)

> A cyberpunk-styled interactive directory of Python libraries for developers

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://jamditis.github.io/python-explorer)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🎯 Overview

Python Explorer is a comprehensive, searchable catalog of Python libraries across multiple domains including Web Development, Data Science, Machine Learning, Automation, and more. Features a distinctive cyberpunk aesthetic with real-time filtering, visual analytics, and side-by-side library comparison.

## ✨ Features

### 🔍 Intelligent Search
- **Fuzzy Search** - Find libraries even with typos or partial matches using Fuse.js
- **AI-Enhanced Descriptions** - Every library has a plain-language, beginner-friendly description
- **Real-time Filtering** - Instant results by name, description, or domain
- **Category Filtering** - Multi-select filtering across all 23 categories

### 📰 Journalism & Media Toolkit
- **Curated Collection** - 39 libraries specifically tagged for journalism and media work
- **One-Click Access** - Dedicated section highlighting tools for data journalism, web scraping, visualization, and content management
- **Requirements Export** - Download a ready-to-use requirements.txt for journalism projects

### 🔧 Developer Tools
- **345 Python Libraries** - Comprehensive collection from awesome-python
- **Requirements.txt Generator** - Export any filtered set of libraries as a pip requirements file
- **Interactive Charts** - Visual analytics showing domain distribution and popularity
- **Side-by-Side Comparison** - Compare libraries to choose the best tool for your needs
- **Clean Cards** - Easy-to-read library information at a glance

### 🎨 Design & UX
- **Cyberpunk Aesthetic** - Distinctive AMDITIS design system with acid green accents
- **Beginner-Friendly** - Natural language interface removes technical barriers
- **Responsive Design** - Works seamlessly on desktop and mobile
- **Zero Build Process** - Pure HTML/CSS/JS with ES6 modules

## 🚀 Quick Start

### Option 1: View Online
Visit the [live demo](https://jamditis.github.io/python-explorer)

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/jamditis/python-explorer.git
cd python-explorer

# Start a local server
python3 -m http.server 3000

# Open http://localhost:3000
```

## 📁 Project Structure

```
python-explorer/
├── index.html                 # Main application (NEW: Natural language UI)
├── index-v2.html             # Alternative version (Advanced UI)
├── assets/
│   ├── css/
│   │   └── styles.css         # Custom cyberpunk styles
│   ├── js/
│   │   ├── app.js            # Main application logic
│   │   ├── natural-search.js # Natural language search engine
│   │   ├── charts.js         # Chart.js visualizations
│   │   ├── comparator.js     # Library comparison tool
│   │   └── modal.js          # Modal functionality
│   └── data/
│       └── libraries.js       # Library data (ES6 module)
├── style/
│   └── amditis-design-library.html  # Design system reference
└── tools/
    ├── extract_from_awesome.py       # Extract libs from awesome-python
    ├── integrate_libraries.py        # Integration helper
    └── pypi_simple_scraper.py        # PyPI scraper (experimental)
```

## 🎨 Design System

Python Explorer uses the **AMDITIS Design Library** with:

- **Primary**: Acid Green (#ccff00) - Actions, highlights
- **Secondary**: Signal Red (#ff2a2a) - Warnings, comparisons
- **Tertiary**: Ice Blue (#00f0ff) - Info, links
- **Typography**: Chakra Petch (display), Share Tech Mono (code)
- **Effects**: CRT scanlines, glitch text, notched corners

## 🛠️ Adding New Libraries

### Method 1: Manual Addition

Edit `assets/data/libraries.js`:

```javascript
{
  n: "LibraryName",
  c: "Category",
  d: "Description text...",
  l: "https://link-to-docs.com/"
}
```

### Method 2: Import from awesome-python

```bash
# Extract libraries from awesome-python collection
python3 tools/extract_from_awesome.py

# Generate integration snippets
python3 tools/integrate_libraries.py

# Copy from new_libraries_snippet.txt to assets/data/libraries.js
```

## 📊 Tech Stack

- **Frontend**: Vanilla JavaScript (ES6 Modules)
- **Search**: Fuse.js 7.0.0 (fuzzy matching)
- **Styling**: TailwindCSS CDN + Custom CSS
- **Charts**: Chart.js 3.9.1
- **Icons**: Lucide Icons
- **Fonts**: Google Fonts (Chakra Petch, Share Tech Mono)
- **AI Enhancement**: Claude Code (description generation)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Data Sources

Library data curated from:
- [awesome-python](https://github.com/vinta/awesome-python) - Comprehensive Python resource list
- Manual curation and categorization

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**James Amditis**
- GitHub: [@jamditis](https://github.com/jamditis)
- Email: jamditis@gmail.com

## 🙏 Acknowledgments

- [awesome-python](https://github.com/vinta/awesome-python) for the comprehensive library collection
- [TailwindCSS](https://tailwindcss.com/) for the utility-first CSS framework
- [Chart.js](https://www.chartjs.org/) for beautiful charts
- [Lucide](https://lucide.dev/) for the icon set

---

<p align="center">
  Made with 💚 by <a href="https://github.com/jamditis">@jamditis</a>
</p>
