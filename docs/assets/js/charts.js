// Chart.js visualizations

let domainChart = null;
let popularityChart = null;

export function initCharts(libraries) {
    Chart.defaults.color = '#666';
    Chart.defaults.font.family = "'Share Tech Mono', monospace";

    const domains = {};
    libraries.forEach(l => domains[l.domain] = (domains[l.domain] || 0) + 1);

    // Domain distribution pie chart
    domainChart = new Chart(document.getElementById('domainChart'), {
        type: 'doughnut',
        data: {
            labels: Object.keys(domains),
            datasets: [{
                data: Object.values(domains),
                backgroundColor: ['#ccff00', '#ff2a2a', '#00f0ff', '#e5e5e5', '#444', '#777'],
                borderWidth: 0,
                hoverOffset: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'right', labels: { boxWidth: 10, usePointStyle: true, font: {size: 10} } }
            },
            cutout: '70%'
        }
    });

    // Top libraries popularity chart
    const topLibs = [...libraries].sort((a,b) => b.popularity - a.popularity).slice(0, 10);
    popularityChart = new Chart(document.getElementById('popularityChart'), {
        type: 'bar',
        data: {
            labels: topLibs.map(l => l.name),
            datasets: [{
                label: 'IMPACT_SCORE',
                data: topLibs.map(l => l.popularity),
                backgroundColor: '#ccff00',
                barThickness: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { color: '#222' },
                    ticks: { color: '#666', font: {size: 10} }
                },
                x: {
                    grid: { display: false },
                    ticks: { color: '#888', font: {size: 10} }
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });
}

export function updateCharts(filteredLibraries) {
    if (!domainChart || !popularityChart) return;

    // Update domain distribution with filtered data
    const domains = {};
    filteredLibraries.forEach(l => domains[l.domain] = (domains[l.domain] || 0) + 1);

    domainChart.data.labels = Object.keys(domains);
    domainChart.data.datasets[0].data = Object.values(domains);
    domainChart.update();

    // Update popularity chart with filtered data
    const topLibs = [...filteredLibraries].sort((a,b) => b.popularity - a.popularity).slice(0, 10);
    popularityChart.data.labels = topLibs.map(l => l.name);
    popularityChart.data.datasets[0].data = topLibs.map(l => l.popularity);
    popularityChart.update();
}
