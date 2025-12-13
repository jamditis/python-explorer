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
    const filtered = libraries.filter(lib => {
        const matchSearch = lib.name.toLowerCase().includes(state.search) ||
                            lib.description.toLowerCase().includes(state.search) ||
                            lib.domain.toLowerCase().includes(state.search);
        const matchCat = state.activeCategories.length === 0 || state.activeCategories.includes(lib.category);
        return matchSearch && matchCat;
    });

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

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', init);
