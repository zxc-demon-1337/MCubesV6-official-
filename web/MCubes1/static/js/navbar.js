document.querySelectorAll('.video-wrapper').forEach(card => {
  const video = card.querySelector('video');
  if (!video) return;

  let isPlaying = false;

  // Начало нажатия — внутри карточки
  card.addEventListener('mousedown', (e) => {
    if (e.button !== 0) return; // только левая кнопка мыши
    if (isPlaying) return; // уже играет — не дублировать

    video.play().catch(console.warn);
    isPlaying = true;
  });

  // Отпускание — в любом месте страницы
  const handleMouseUp = () => {
    if (isPlaying) {
      video.pause();
      video.currentTime = 0;
      isPlaying = false;
    }
  };

  // Добавляем обработчик на весь документ
  document.addEventListener('mouseup', handleMouseUp);
});
