// ============================================================
// OBSERVER PATTERN — PRESENTATION SCRIPT
// SSC0124 - APOO | Rafael Feltrim
// ============================================================

let currentSlide = 1;

function getSlides() {
    return Array.from(document.querySelectorAll('.slide'));
}

document.addEventListener('DOMContentLoaded', () => {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (prevBtn) {
        prevBtn.addEventListener('click', () => changeSlide(-1));
    }
    if (nextBtn) {
        nextBtn.addEventListener('click', () => changeSlide(1));
    }

    document.querySelectorAll('.code-tab[data-tab]').forEach((tabBtn) => {
        tabBtn.addEventListener('click', () => {
            const tabId = tabBtn.getAttribute('data-tab');
            if (tabId) {
                showTab(tabId, tabBtn);
            }
        });
    });

    updateProgress();
    updateCounter();
});

document.addEventListener('keydown', (e) => {
    const target = e.target;
    const isFormField =
        target instanceof Element &&
        Boolean(target.closest('input, textarea, select, [contenteditable="true"]'));
    if (isFormField) return;

    const isInteractive =
        target instanceof Element &&
        Boolean(target.closest('button, a, [role="button"]'));
    if (e.key === ' ' && isInteractive) return;

    const totalSlides = getSlides().length;
    if (totalSlides === 0) return;

    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
        e.preventDefault();
        changeSlide(1);
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault();
        changeSlide(-1);
    } else if (e.key === 'Home') {
        e.preventDefault();
        goToSlide(1);
    } else if (e.key === 'End') {
        e.preventDefault();
        goToSlide(totalSlides);
    }
});

function changeSlide(direction) {
    const totalSlides = getSlides().length;
    if (totalSlides === 0) return;
    const newSlide = currentSlide + direction;
    if (newSlide < 1 || newSlide > totalSlides) return;
    goToSlide(newSlide);
}

function goToSlide(slideNum) {
    const slides = getSlides();
    if (slideNum === currentSlide || slideNum < 1 || slideNum > slides.length) return;

    const newSlide = slides[slideNum - 1];
    if (!newSlide) return;

    slides.forEach((s) => {
        s.classList.remove('active');
    });

    // Force reflow for fade animation
    void newSlide.offsetWidth;
    newSlide.classList.add('active');

    currentSlide = slideNum;
    updateProgress();
    updateCounter();
}

function updateProgress() {
    const progressBar = document.getElementById('progressBar');
    const totalSlides = getSlides().length;
    if (!progressBar || totalSlides === 0) return;
    const progress = (currentSlide / totalSlides) * 100;
    progressBar.style.width = `${progress}%`;
}

function updateCounter() {
    const totalSlides = getSlides().length;
    const counter = document.getElementById('slideCounter');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (counter) {
        counter.textContent = `${currentSlide} / ${totalSlides}`;
    }
    if (prevBtn) {
        prevBtn.disabled = currentSlide <= 1;
    }
    if (nextBtn) {
        nextBtn.disabled = totalSlides === 0 || currentSlide >= totalSlides;
    }
}

// Code tabs
function showTab(tabId, btn) {
    if (!btn) return;
    const container = btn.closest('.code-container');
    if (!container) return;
    const targetTab = document.getElementById(tabId);
    if (!targetTab) return;

    container.querySelectorAll('.code-content').forEach((c) => c.classList.add('hidden'));
    container.querySelectorAll('.code-tab').forEach((t) => t.classList.remove('active'));
    targetTab.classList.remove('hidden');
    btn.classList.add('active');
}
