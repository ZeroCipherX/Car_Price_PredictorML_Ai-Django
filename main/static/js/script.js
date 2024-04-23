// Track whether the About Us section is visible
let aboutSectionVisible = false;

// Function to show or hide the About Us section
function showAboutSection() {
    const aboutSection = document.getElementById('aboutSection');

    // Toggle visibility
    aboutSectionVisible = !aboutSectionVisible;
    aboutSection.style.display = aboutSectionVisible ? 'block' : 'none';

    if (aboutSectionVisible) {
        const image = document.querySelector('.about-section img');
        image.style.display = 'block'; // Make the image visible

        const aboutText = document.querySelector('.about-section .about-text');
        aboutText.style.opacity = 1;
    } else {
        const image = document.querySelector('.about-section img');
        image.style.display = 'none'; // Hide the image when the About Us section is hidden
    }
}

// Function to show the home page
function showHomePage() {
    const aboutSection = document.getElementById('aboutSection');
    aboutSection.style.display = 'none';
    window.scrollTo({ top: 0, behavior: 'smooth' });
    aboutSectionVisible = false;
}

// Ensuring this code runs after the DOM has fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Ensure the popup is hidden initially
    document.getElementById('carPopup').style.display = 'none';
});
