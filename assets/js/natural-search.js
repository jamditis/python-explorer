// Natural Language Search Interface

export const searchTemplates = {
    "I have": {
        options: [
            { value: "csv", label: "CSV files", searches: ["pandas", "csv", "data analysis"] },
            { value: "excel", label: "Excel spreadsheets", searches: ["openpyxl", "pandas", "xlrd"] },
            { value: "json", label: "JSON data", searches: ["json", "requests", "api"] },
            { value: "images", label: "Images", searches: ["pillow", "opencv", "image processing"] },
            { value: "pdf", label: "PDF files", searches: ["pypdf", "reportlab", "pdf"] },
            { value: "database", label: "A database", searches: ["sqlalchemy", "orm", "database"] },
            { value: "api", label: "An API", searches: ["requests", "http", "api"] },
            { value: "website", label: "A website to scrape", searches: ["beautiful soup", "scrapy", "selenium"] },
            { value: "text", label: "Text data", searches: ["nlp", "spacy", "text processing"] },
            { value: "video", label: "Video files", searches: ["opencv", "video", "ffmpeg"] }
        ],
        nextTemplate: "and want to"
    },
    "and want to": {
        options: [
            { value: "analyze", label: "Analyze it", searches: ["pandas", "numpy", "data analysis"] },
            { value: "visualize", label: "Visualize it", searches: ["matplotlib", "plotly", "seaborn"] },
            { value: "clean", label: "Clean it", searches: ["pandas", "data validation"] },
            { value: "transform", label: "Transform it", searches: ["pandas", "data engineering"] },
            { value: "automate", label: "Automate processing", searches: ["automation", "celery", "airflow"] },
            { value: "extract", label: "Extract data from it", searches: ["scraping", "parsing", "extraction"] },
            { value: "generate", label: "Generate reports", searches: ["reportlab", "jinja", "documentation"] },
            { value: "predict", label: "Make predictions", searches: ["machine learning", "scikit", "tensorflow"] },
            { value: "classify", label: "Classify it", searches: ["machine learning", "classification"] },
            { value: "search", label: "Search through it", searches: ["search", "indexing", "elasticsearch"] }
        ]
    },
    "I want to": {
        options: [
            { value: "build-web", label: "Build a web application", searches: ["flask", "django", "fastapi"] },
            { value: "build-api", label: "Build an API", searches: ["fastapi", "flask", "rest"] },
            { value: "scrape-web", label: "Scrape websites", searches: ["beautiful soup", "scrapy", "selenium"] },
            { value: "analyze-data", label: "Analyze data", searches: ["pandas", "numpy", "data analysis"] },
            { value: "visualize", label: "Create visualizations", searches: ["matplotlib", "plotly", "dash"] },
            { value: "ml", label: "Do machine learning", searches: ["scikit", "tensorflow", "pytorch"] },
            { value: "nlp", label: "Process text/language", searches: ["spacy", "nltk", "nlp"] },
            { value: "cv", label: "Process images/video", searches: ["opencv", "pillow", "computer vision"] },
            { value: "automate", label: "Automate tasks", searches: ["selenium", "automation", "schedule"] },
            { value: "test", label: "Test my code", searches: ["pytest", "unittest", "testing"] },
            { value: "gui", label: "Build a desktop app", searches: ["tkinter", "pyqt", "gui"] },
            { value: "game", label: "Make a game", searches: ["pygame", "game development"] },
            { value: "work-files", label: "Work with files", searches: ["pathlib", "file manipulation", "pdf"] },
            { value: "database", label: "Work with databases", searches: ["sqlalchemy", "database", "orm"] },
            { value: "deploy", label: "Deploy applications", searches: ["docker", "devops", "deployment"] }
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
            // Direct "I want to" search
            const choice = searchTemplates['I want to'].options.find(opt => opt.value === e.target.value);
            if (choice) {
                executeSearch(choice.searches[0], searchCallback);
            }
        } else if (currentTemplate === 'I have') {
            // Combined "I have...want to..." search
            const firstChoice = searchTemplates['I have'].options.find(opt => opt.value === dropdown1.value);
            const secondChoice = searchTemplates['and want to'].options.find(opt => opt.value === e.target.value);

            if (firstChoice && secondChoice) {
                const combinedSearches = [...new Set([...firstChoice.searches, ...secondChoice.searches])];
                executeSearch(combinedSearches[0], searchCallback);
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
