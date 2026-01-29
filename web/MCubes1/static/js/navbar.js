// Создаём и добавляем стили
const style = document.createElement('style');
style.textContent = `

  .video-wrapper.playing {
    border-color: #00ff6f;
  }
`;
document.head.appendChild(style);

// Оборачиваем основной код в обработчик загрузки DOM
document.addEventListener('DOMContentLoaded', () => {
  // Основной функционал видео
  document.querySelectorAll('.video-wrapper').forEach(card => {
    const video = card.querySelector('video');
    if (!video) return;

    let isPlaying = false;
    let playTimeout = null;
    let resetTimeout = null;

    // Запуск/остановка видео по клику
    card.addEventListener('click', () => {
      // Очищаем предыдущий таймаут запуска, если он есть
      if (playTimeout) {
        clearTimeout(playTimeout);
        playTimeout = null;
        card.classList.remove('playing');
      }

      // Очищаем таймаут сброса, если он есть
      if (resetTimeout) {
        clearTimeout(resetTimeout);
        resetTimeout = null;
      }

      if (isPlaying) {
        video.pause();
        video.currentTime = 0;
        isPlaying = false;
        card.classList.remove('playing');
      } else {
        // Добавляем класс сразу для визуальной обратной связи
        card.classList.add('playing');
        
        // Задержка 1 секунда перед запуском
        playTimeout = setTimeout(() => {
          video.play().catch(console.warn);
          isPlaying = true;
          playTimeout = null;
        }, 1);
      }
    });

    // Обработчик окончания видео
    video.addEventListener('ended', () => {
      resetTimeout = setTimeout(() => {
        video.currentTime = 0;
        isPlaying = false;
        card.classList.remove('playing');
        resetTimeout = null;
      }, 2000);
    });

    // Проверка видимости видео (остановка при 50% за экраном)
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.intersectionRatio < 0.5 && isPlaying) {
          video.pause();
          video.currentTime = 0;
          isPlaying = false;
          card.classList.remove('playing');
          // Отменяем таймаут, если видео ушло за экран
          if (playTimeout) {
            clearTimeout(playTimeout);
            playTimeout = null;
          }
          if (resetTimeout) {
            clearTimeout(resetTimeout);
            resetTimeout = null;
          }
        }
      });
    }, { threshold: [0.5] });

    observer.observe(card);
  });
});