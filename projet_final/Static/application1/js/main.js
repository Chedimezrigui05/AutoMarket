// main.js - AutoMarket

// Mettre en évidence le lien actif dans la navigation
document.addEventListener('DOMContentLoaded', function () {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.style.backgroundColor = 'rgba(37, 99, 235, 0.35)';
            link.style.borderRadius = '8px';
        }
    });
});
