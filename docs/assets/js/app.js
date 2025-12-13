// Main Application Logic
import { rawLibraries, domainMap } from '../data/libraries.js';
import { initCharts } from './charts.js';
import { initComparator } from './comparator.js';
import { openModal, closeModal, copyInstall } from './modal.js';
import { initNaturalSearch } from './natural-search.js';

// Process raw libraries into full objects
export const libraries = rawLibraries.map((lib, index) => {
    let dom = "Utilities";
    for (const [key, value] of Object.entries(domainMap)) {
        if (key === lib.c) { dom = value; break; }
    }

    // Generate popularity score
    let basePop = 60;
    if (lib.d.toLowerCase().includes("very widely used") || lib.d.toLowerCase().includes("extremely popular")) basePop = 95;
    else if (lib.d.toLowerCase().includes("widely used")) basePop = 85;
    else if (lib.d.toLowerCase().includes("niche")) basePop = 45;

    const randomVar = Math.floor(Math.random() * 10);

    return {
        id: `lib_${index}`,
        name: lib.n,
        category: lib.c,
        domain: dom,
        description: lib.d,
        popularity: Math.min(basePop + randomVar, 100),
        install: `pip install ${lib.n.toLowerCase().replace(/\s+/g, '-').replace(/[()]/g, '')}`,
        snippet: `import ${lib.n.toLowerCase().split(/[ .]/)[0].replace(/[()]/g, '')}\n# Initializing ${lib.n}...`,
        link: lib.l
    };
});

// Application state
export const state = {
    search: "",
    activeCategories: [],
    sortBy: "relevance"
};

// Fuse.js instance for fuzzy search
let fuse = null;

// DOM References
let grid, filterList, searchInput, filterSearch, activeFiltersContainer;

// Initialize application
export function init() {
    // Get DOM references
    grid = document.getElementById('grid');
    filterList = document.getElementById('categoryList');
    searchInput = document.getElementById('searchInput');
    filterSearch = document.getElementById('filterSearch');
    activeFiltersContainer = document.getElementById('activeFilters');

    if (!grid || !searchInput) {
        console.error('Required DOM elements not found');
        return;
    }

    // Initialize Fuse.js for fuzzy search
    fuse = new Fuse(libraries, {
        keys: [
            { name: 'name', weight: 0.4 },
            { name: 'description', weight: 0.3 },
            { name: 'domain', weight: 0.2 },
            { name: 'category', weight: 0.1 }
        ],
        threshold: 0.4,
        includeScore: true,
        minMatchCharLength: 2
    });

    renderFilters();
    renderGrid();

    // initCharts only if chart canvases exist
    if (document.getElementById('domainChart')) {
        initCharts(libraries);
    }
    updateStats();

    // initComparator only if selects exist
    if (document.getElementById('compSelect1')) {
        initComparator(libraries);
    }

    initNaturalSearch(handleNaturalSearch);

    searchInput.addEventListener('input', (e) => {
        state.search = e.target.value.toLowerCase();
        renderGrid();
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
    });

    filterSearch.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        const labels = filterList.querySelectorAll('label');
        labels.forEach(label => {
            const text = label.textContent.toLowerCase();
            label.style.display = text.includes(term) ? 'flex' : 'none';
        });
    });

    // Make functions globally accessible
    window.toggleFilter = toggleFilter;
    window.resetFilters = resetFilters;
    window.scrollToSection = scrollToSection;
    window.openModal = (id) => openModal(id, libraries);
    window.closeModal = closeModal;
    window.copyInstall = copyInstall;
    window.filterJournalismLibs = filterJournalismLibs;
    window.generateRequirementsTxt = generateRequirementsTxt;
}

function updateStats() {
    document.getElementById('totalCount').innerText = libraries.length;
    document.getElementById('categoryCount').innerText = [...new Set(libraries.map(l => l.category))].length;
}

function renderFilters() {
    if (!filterList) return;

    const categories = [...new Set(libraries.map(l => l.category))].sort();

    filterList.innerHTML = categories.map(cat => `
        <label class="flex items-center space-x-3 p-2 rounded-sm hover:bg-white/5 cursor-pointer transition-colors group border-l-2 border-transparent hover:border-acid">
            <input type="checkbox" value="${cat}" onchange="toggleFilter('${cat}')"
                   class="cyber-checkbox appearance-none">
            <span class="text-[10px] text-gray-500 group-hover:text-chrome font-mono uppercase truncate">${cat}</span>
            <span class="text-[10px] text-gray-600 ml-auto">${libraries.filter(l => l.category === cat).length}</span>
        </label>
    `).join('');
}

function toggleFilter(cat) {
    if (state.activeCategories.includes(cat)) {
        state.activeCategories = state.activeCategories.filter(c => c !== cat);
    } else {
        state.activeCategories.push(cat);
    }
    renderActiveFilters();
    renderGrid();
}

function renderActiveFilters() {
    activeFiltersContainer.innerHTML = state.activeCategories.map(cat => `
        <button onclick="toggleFilter('${cat}')" class="inline-flex items-center gap-1 px-2 py-1 bg-acidDim border border-acid text-acid text-[10px] font-mono hover:bg-acid hover:text-black transition-colors">
            [x] ${cat}
        </button>
    `).join('');

    document.querySelectorAll('#categoryList input').forEach(input => {
        input.checked = state.activeCategories.includes(input.value);
    });
}

function resetFilters() {
    state.activeCategories = [];
    state.search = "";
    searchInput.value = "";
    renderActiveFilters();
    renderGrid();
}

function renderGrid() {
    let filtered;

    // Use fuzzy search if there's a search term, otherwise show all
    if (state.search.trim()) {
        const fuseResults = fuse.search(state.search);
        filtered = fuseResults.map(result => result.item);
    } else {
        filtered = libraries;
    }

    // Apply category filter
    if (state.activeCategories.length > 0) {
        filtered = filtered.filter(lib => state.activeCategories.includes(lib.category));
    }

    document.getElementById('resultCount').innerText = `[ RESULTS: ${filtered.length} ]`;

    if (filtered.length === 0) {
        grid.innerHTML = '';
        document.getElementById('noResults').classList.remove('hidden');
        return;
    }

    document.getElementById('noResults').classList.add('hidden');

    grid.innerHTML = filtered.map(lib => `
        <div onclick="openModal('${lib.id}')" class="bg-panel border-2 border-white/10 p-5 relative group hover:border-acid transition-all cursor-pointer flex flex-col min-h-[240px]">
            <div class="absolute inset-0 bg-acid/5 opacity-0 group-hover:opacity-100 transition-opacity z-0"></div>

            <div class="relative z-10 flex flex-col h-full">
                <!-- Header -->
                <div class="flex items-start gap-3 mb-4">
                    <div class="w-10 h-10 flex-shrink-0 bg-acid/10 border border-acid/30 flex items-center justify-center">
                        <i data-lucide="package" class="w-5 h-5 text-acid"></i>
                    </div>
                    <div class="flex-1 min-w-0">
                        <h4 class="font-display text-base text-chrome group-hover:text-acid transition-colors truncate">${lib.name}</h4>
                        <div class="text-[10px] text-gray-600 font-mono uppercase mt-1">${lib.domain}</div>
                    </div>
                </div>

                <!-- Description - takes available space -->
                <div class="flex-1 mb-4">
                    <p class="text-sm font-mono text-gray-400 leading-relaxed line-clamp-3">${lib.description}</p>
                </div>

                <!-- Footer - always at bottom -->
                <div class="pt-3 border-t border-white/10 flex items-center justify-between gap-2">
                    <span class="text-xs text-gray-600 font-mono truncate">${lib.category}</span>
                    <div class="flex items-center gap-1 text-xs text-acid opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">
                        <span>Details</span>
                        <i data-lucide="arrow-right" class="w-3 h-3"></i>
                    </div>
                </div>
            </div>
        </div>
    `).join('');

    lucide.createIcons();
}

function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}

function handleNaturalSearch(searchTerm) {
    state.search = searchTerm.toLowerCase();
    searchInput.value = searchTerm;
    renderGrid();
}

function filterJournalismLibs() {
    // Filter to show only journalism-tagged libraries
    state.search = "[JOURNALISM]";
    searchInput.value = "";
    state.activeCategories = [];
    renderActiveFilters();
    renderGrid();

    // Scroll to explorer section
    scrollToSection('explorer');
}

function generateRequirementsTxt(type = 'all') {
    let libsToExport;

    if (type === 'journalism') {
        // Export journalism libraries
        libsToExport = libraries.filter(lib => lib.description.includes('[JOURNALISM]'));
    } else if (type === 'current') {
        // Export currently filtered/visible libraries
        let filtered;
        if (state.search.trim()) {
            const fuseResults = fuse.search(state.search);
            filtered = fuseResults.map(result => result.item);
        } else {
            filtered = libraries;
        }
        if (state.activeCategories.length > 0) {
            filtered = filtered.filter(lib => state.activeCategories.includes(lib.category));
        }
        libsToExport = filtered;
    } else {
        // Export all libraries
        libsToExport = libraries;
    }

    // Generate requirements.txt content
    const requirements = libsToExport
        .map(lib => {
            // Convert library name to package name (lowercase, remove special chars)
            const packageName = lib.name.toLowerCase()
                .replace(/\s+/g, '-')
                .replace(/[()]/g, '')
                .replace(/\./g, '-');
            return packageName;
        })
        .sort()
        .join('\n');

    // Create downloadable file
    const blob = new Blob([requirements], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = type === 'journalism' ? 'journalism-requirements.txt' : 'requirements.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    console.log(`Generated requirements.txt with ${libsToExport.length} libraries`);
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', init);
