// Library comparison functionality

export function initComparator(libraries) {
    const select1 = document.getElementById('compSelect1');
    const select2 = document.getElementById('compSelect2');

    const sortedLibs = [...libraries].sort((a,b) => a.name.localeCompare(b.name));
    const options = sortedLibs.map(l => `<option value="${l.id}">${l.name}</option>`).join('');

    const defOpt = `<option value="">[ SELECT_ENTITY ]</option>`;
    select1.innerHTML = defOpt + options;
    select2.innerHTML = defOpt + options;

    const updateComp = () => {
        const l1 = libraries.find(l => l.id === select1.value);
        const l2 = libraries.find(l => l.id === select2.value);
        const output = document.getElementById('compareOutput');

        if (!l1 || !l2) {
            output.innerHTML = `[ AWAITING_SELECTION ]`;
            return;
        }

        output.innerHTML = `
            <div class="w-full overflow-x-auto">
                <table class="w-full text-xs font-mono text-left border-collapse">
                    <thead>
                        <tr class="border-b border-white/10">
                            <th class="py-2 text-gray-500 font-normal w-1/4">METRIC</th>
                            <th class="py-2 text-acid w-1/3">${l1.name}</th>
                            <th class="py-2 text-signal w-1/3">${l2.name}</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-white/5">
                        <tr>
                            <td class="py-3 text-gray-500">DOMAIN</td>
                            <td class="py-3 text-chrome">${l1.domain}</td>
                            <td class="py-3 text-chrome">${l2.domain}</td>
                        </tr>
                        <tr>
                            <td class="py-3 text-gray-500">CATEGORY</td>
                            <td class="py-3 text-gray-400">${l1.category}</td>
                            <td class="py-3 text-gray-400">${l2.category}</td>
                        </tr>
                        <tr>
                            <td class="py-3 text-gray-500">IMPACT</td>
                            <td class="py-3">
                                <div class="w-24 h-1 bg-gray-800">
                                    <div class="bg-acid h-full" style="width: ${l1.popularity}%"></div>
                                </div>
                            </td>
                            <td class="py-3">
                                <div class="w-24 h-1 bg-gray-800">
                                    <div class="bg-signal h-full" style="width: ${l2.popularity}%"></div>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        `;
    };

    select1.addEventListener('change', updateComp);
    select2.addEventListener('change', updateComp);
}
