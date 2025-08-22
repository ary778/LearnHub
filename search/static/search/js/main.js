// static/search/js/main.js

document.addEventListener('DOMContentLoaded', () => {

    // --- 1. tsParticles Animation ---
    // This creates the interactive particle background
    tsParticles.load("particles-js", {
        fpsLimit: 60,
        interactivity: {
            events: {
                onHover: {
                    enable: true,
                    mode: "repulse",
                },
                resize: true,
            },
            modes: {
                repulse: {
                    distance: 100,
                    duration: 0.4,
                },
            },
        },
        particles: {
            color: {
                value: "#a0a0b5", // Color of the particles
            },
            links: {
                color: "#505070", // Color of the lines connecting particles
                distance: 150,
                enable: true,
                opacity: 0.5,
                width: 1,
            },
            collisions: {
                enable: true,
            },
            move: {
                direction: "none",
                enable: true,
                outModes: {
                    default: "bounce",
                },
                random: false,
                speed: 1, // Speed of particle movement
                straight: false,
            },
            number: {
                density: {
                    enable: true,
                    area: 800,
                },
                value: 80, // Number of particles
            },
            opacity: {
                value: 0.5,
            },
            shape: {
                type: "circle",
            },
            size: {
                value: { min: 1, max: 5 },
            },
        },
        detectRetina: true,
    });

    // --- 2. Typed.js Animation ---
    // This creates the dynamic typing effect in the hero section
    const typed = new Typed('#typed-element', {
        strings: [
            'Data Structures',
            'Quantum Physics',
            'Machine Learning',
            'Web Development',
            'Game Theory',
            'Blockchain',
            'History of Rome',
        ],
        typeSpeed: 50,
        backSpeed: 30,
        backDelay: 1500,
        loop: true,
        smartBackspace: true,
    });

    // --- 3. Card Fade-in for Results Page ---
    // This logic remains for the results page
    const cards = document.querySelectorAll('.result-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 50);
    });

});