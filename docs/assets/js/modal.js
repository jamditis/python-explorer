// Modal functionality

const modal = document.getElementById('modalOverlay');
const mTitle = document.getElementById('mTitle');
const mDesc = document.getElementById('mDesc');
const mInstall = document.getElementById('mInstall');
const mSnippet = document.getElementById('mSnippet');
const mIcon = document.getElementById('mIcon');
const mDomain = document.getElementById('mDomain');
const mCategory = document.getElementById('mCategory');
const mBestFor = document.getElementById('mBestFor');
const mLink = document.getElementById('mLink');

export function openModal(id, libraries) {
    const lib = libraries.find(l => l.id === id);
    if (!lib) return;

    mTitle.innerText = lib.name.toUpperCase();
    // Remove [JOURNALISM] tag from description display
    mDesc.innerText = lib.description.replace(/\[JOURNALISM\]\s*/g, '');
    mInstall.innerText = lib.install;
    mSnippet.innerText = lib.snippet;
    mIcon.innerText = lib.domain.substring(0,3).toUpperCase();
    mDomain.innerText = lib.domain.toUpperCase();
    mCategory.innerText = lib.category.toUpperCase();
    mBestFor.innerText = `OPTIMIZED FOR: ${lib.category.toUpperCase()} OPERATIONS.`;
    mLink.href = lib.link;

    modal.classList.remove('hidden');
    requestAnimationFrame(() => {
        modal.classList.add('open');
    });
    document.body.style.overflow = 'hidden';
}

export function closeModal() {
    modal.classList.remove('open');
    setTimeout(() => {
        modal.classList.add('hidden');
        document.body.style.overflow = '';
    }, 300);
}

export function copyInstall() {
    const text = mInstall.innerText;
    navigator.clipboard.writeText(text);
    const btnText = document.getElementById('copyBtnText');
    const original = btnText.innerText;
    btnText.innerText = "COPIED";
    setTimeout(() => btnText.innerText = original, 2000);
}

// Close modal when clicking outside
modal.addEventListener('click', (e) => {
    if (e.target === document.querySelector('#modalOverlay .absolute')) {
        closeModal();
    }
});
