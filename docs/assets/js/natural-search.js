// Natural Language Search Interface

export const searchTemplates = {
    "I have": {
        options: [
            { value: "csv", label: "CSV files", searches: ["csv", "pandas", "data"] },
            { value: "excel", label: "Excel spreadsheets", searches: ["excel", "pandas", "spreadsheet"] },
            { value: "json", label: "JSON data", searches: ["json", "api", "data"] },
            { value: "images", label: "Images", searches: ["image", "photo", "picture"] },
            { value: "pdf", label: "PDF files", searches: ["pdf", "document"] },
            { value: "database", label: "A database", searches: ["database", "sql", "data"] },
            { value: "api", label: "An API to work with", searches: ["api", "rest", "http"] },
            { value: "website", label: "A website to scrape", searches: ["scraping", "web", "html"] },
            { value: "text", label: "Text data", searches: ["text", "nlp", "language"] },
            { value: "video", label: "Video files", searches: ["video", "media", "stream"] }
        ],
        nextTemplate: "and want to"
    },
    "and want to": {
        options: [
            { value: "analyze", label: "Analyze it", searches: ["analysis", "analyze", "explore"] },
            { value: "visualize", label: "Visualize it", searches: ["visualization", "chart", "plot"] },
            { value: "clean", label: "Clean it", searches: ["clean", "validation", "parse"] },
            { value: "transform", label: "Transform it", searches: ["transform", "convert", "process"] },
            { value: "automate", label: "Automate processing", searches: ["automation", "task", "schedule"] },
            { value: "extract", label: "Extract data from it", searches: ["extract", "scrape", "parse"] },
            { value: "generate", label: "Generate reports", searches: ["generate", "report", "document"] },
            { value: "predict", label: "Make predictions", searches: ["machine learning", "prediction", "model"] },
            { value: "classify", label: "Classify it", searches: ["classification", "machine learning", "categorize"] },
            { value: "search", label: "Search through it", searches: ["search", "query", "index"] }
        ]
    },
    "I want to": {
        options: [
            { value: "build-web", label: "Build a web application", searches: ["web", "framework", "application"] },
            { value: "build-api", label: "Build an API", searches: ["api", "rest", "fastapi"] },
            { value: "scrape-web", label: "Scrape websites", searches: ["scraping", "web", "extract"] },
            { value: "analyze-data", label: "Analyze data", searches: ["data analysis", "pandas", "statistics"] },
            { value: "visualize", label: "Create visualizations", searches: ["visualization", "chart", "graph"] },
            { value: "ml", label: "Do machine learning", searches: ["machine learning", "model", "train"] },
            { value: "nlp", label: "Process text/language", searches: ["nlp", "text", "language"] },
            { value: "cv", label: "Process images/video", searches: ["image", "video", "computer vision"] },
            { value: "automate", label: "Automate tasks", searches: ["automation", "task", "workflow"] },
            { value: "test", label: "Test my code", searches: ["testing", "test", "unittest"] },
            { value: "gui", label: "Build a desktop app", searches: ["gui", "desktop", "interface"] },
            { value: "game", label: "Make a game", searches: ["game", "graphics", "pygame"] },
            { value: "work-files", label: "Work with files", searches: ["file", "document", "io"] },
            { value: "database", label: "Work with databases", searches: ["database", "sql", "orm"] },
            { value: "deploy", label: "Deploy applications", searches: ["deploy", "docker", "server"] }
        ]
    }
};

export const quickSearches = [
    { label: "Web Development", icon: "globe", search: "web framework" },
    { label: "Data Science", icon: "bar-chart", search: "data analysis" },
    { label: "Machine Learning", icon: "brain", search: "machine learning" },
    { label: "Web Scraping", icon: "download", search: "scraping" },
    { label: "Automation", icon: "zap", search: "automation" },
    { label: "APIs", icon: "cloud", search: "api" },
    { label: "Testing", icon: "check-circle", search: "testing" },
    { label: "Visualization", icon: "pie-chart", search: "visualization" }
];

export function initNaturalSearch(searchCallback) {
    const template1 = document.getElementById('searchTemplate1');
    const template2 = document.getElementById('searchTemplate2');
    const dropdown1Container = document.getElementById('dropdown1Container');
    const dropdown2Container = document.getElementById('dropdown2Container');
    const dropdown1 = document.getElementById('dropdown1');
    const dropdown2 = document.getElementById('dropdown2');
    const quickSearchButtons = document.getElementById('quickSearchButtons');

    // Check if all elements exist (only needed for natural search page)
    if (!template1 || !template2 || !dropdown1 || !dropdown2 || !quickSearchButtons) {
        return; // Silently skip if natural search elements don't exist
    }

    let currentTemplate = null;

    // Initialize template selection
    template1.addEventListener('click', () => selectTemplate('I have', template1, template2));
    template2.addEventListener('click', () => selectTemplate('I want to', template1, template2));

    function selectTemplate(templateName, activeBtn, inactiveBtn) {
        currentTemplate = templateName;
        activeBtn.classList.add('bg-acid', 'text-black', 'border-acid');
        activeBtn.classList.remove('bg-transparent', 'text-gray-400', 'border-white/20');
        inactiveBtn.classList.remove('bg-acid', 'text-black', 'border-acid');
        inactiveBtn.classList.add('bg-transparent', 'text-gray-400', 'border-white/20');

        if (templateName === 'I have') {
            dropdown1Container.classList.remove('hidden');
            dropdown2Container.classList.add('hidden');
            document.getElementById('dropdown2Label').textContent = 'and want to';
            populateDropdown(dropdown1, searchTemplates['I have'].options);
            dropdown2.innerHTML = '<option value="">Select...</option>';
        } else {
            dropdown1Container.classList.add('hidden');
            dropdown2Container.classList.remove('hidden');
            document.getElementById('dropdown2Label').textContent = 'I want to';
            populateDropdown(dropdown2, searchTemplates['I want to'].options);
        }
    }

    function populateDropdown(dropdown, options) {
        dropdown.innerHTML = '<option value="">Select...</option>' +
            options.map(opt => `<option value="${opt.value}">${opt.label}</option>`).join('');
    }

    // Handle first dropdown change
    dropdown1.addEventListener('change', (e) => {
        if (!e.target.value) {
            dropdown2Container.classList.add('hidden');
            return;
        }

        dropdown2Container.classList.remove('hidden');
        populateDropdown(dropdown2, searchTemplates['and want to'].options);
    });

    // Unified handler for dropdown2 changes
    dropdown2.addEventListener('change', (e) => {
        if (!e.target.value) return;

        if (currentTemplate === 'I want to') {
            // Direct "I want to" search - try all search terms
            const choice = searchTemplates['I want to'].options.find(opt => opt.value === e.target.value);
            if (choice) {
                // Join all search terms with OR logic for better results
                const searchTerm = choice.searches.join(' ');
                executeSearch(searchTerm, searchCallback);
            }
        } else if (currentTemplate === 'I have') {
            // Combined "I have...want to..." search
            const firstChoice = searchTemplates['I have'].options.find(opt => opt.value === dropdown1.value);
            const secondChoice = searchTemplates['and want to'].options.find(opt => opt.value === e.target.value);

            if (firstChoice && secondChoice) {
                // Prioritize second choice (action) but include data type context
                // This gives better results: e.g., "analyze pandas" vs just "analyze"
                const primaryTerm = secondChoice.searches[0];
                const contextTerm = firstChoice.searches[0];
                const searchTerm = `${primaryTerm} ${contextTerm}`;
                executeSearch(searchTerm, searchCallback);
            }
        }
    });

    // Quick search buttons
    quickSearchButtons.innerHTML = quickSearches.map(qs => `
        <button onclick="window.quickSearch('${qs.search}')"
                class="flex items-center gap-2 px-4 py-2 bg-surface border border-white/20 text-gray-300 text-xs font-mono hover:border-acid hover:text-acid transition-all group">
            <i data-lucide="${qs.icon}" class="w-3 h-3 text-gray-500 group-hover:text-acid"></i>
            ${qs.label}
        </button>
    `).join('');

    lucide.createIcons();

    // Expose quick search globally
    window.quickSearch = (search) => executeSearch(search, searchCallback);

    // Default selection
    selectTemplate('I want to', template2, template1);
}

function executeSearch(searchTerm, callback) {
    callback(searchTerm);

    // Scroll to results
    document.getElementById('explorer')?.scrollIntoView({ behavior: 'smooth' });
}
