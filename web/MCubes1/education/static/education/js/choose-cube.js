document.querySelectorAll('.cube-card').forEach(card => {
  const layers = card.querySelectorAll('[data-depth]');
  
  let currentX = 0;
  let currentY = 0;
  let targetX = 0;
  let targetY = 0;

  const maxTilt = 15;
  const scale = 1.05;
  const easing = 0.1;

  function animate() {
    currentX += (targetX - currentX) * easing;
    currentY += (targetY - currentY) * easing;

    card.style.transform = `
      perspective(1000px)
      rotateX(${currentY}deg)
      rotateY(${currentX}deg)
      scale(${scale})
    `;

    layers.forEach(layer => {
      const depth = layer.dataset.depth;
      layer.style.transform = `
        translateX(${currentX * depth * 10}px)
        translateY(${currentY * depth * 10}px)
        translateZ(${depth * 50}px)
      `;
    });

    requestAnimationFrame(animate);
  }

  animate();
  
  function curve(v) {
  return Math.sign(v) * Math.pow(Math.abs(v), 1.5);
}

  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    let x = (e.clientX - rect.left) / rect.width - 0.5;
    let y = (e.clientY - rect.top) / rect.height - 0.5;

    x = curve(x * 2);
    y = curve(y * 2);
    
    targetX = x * maxTilt;
    targetY = -y * maxTilt;
  });

  card.addEventListener('mouseleave', () => {
    targetX = 0;
    targetY = 0;
  });
});
