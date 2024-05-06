document.addEventListener('DOMContentLoaded', function () {

    const canvas = document.getElementById('smokeCanvas');
    const ctx = canvas.getContext('2d');

    // Resize the canvas to fill browser window dynamically
    window.addEventListener('resize', resizeCanvas, false);
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resizeCanvas();

    const particles = [];

    function addParticle(x, y) {
        particles.push({
            x: x,
            y: y,
            size: 10,
            life: 1,
            decay: Math.random() * 0.01 + 0.015
        });
    }

    document.addEventListener('mousemove', function (e) {
        addParticle(e.clientX, e.clientY);
    });


    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        particles.forEach((particle, index) => {
            particle.life -= particle.decay;
            particle.size += 0.5;

            ctx.globalAlpha = particle.life;
            ctx.fillStyle = `rgba(255, ${Math.round(255 * (1 - particle.life))}, 0, ${particle.life})`; // Yellow to orange fire
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            ctx.fill();

            if (particle.life <= 0) {
                particles.splice(index, 1);
            }
        });

        requestAnimationFrame(animate);
    }
    animate();
});


