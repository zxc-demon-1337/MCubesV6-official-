
document.querySelectorAll('.card-button').forEach(div => {
  div.addEventListener('click', (e) => {
    const url = div.getAttribute('data-href');
    if (url) {
      // Открыть в текущей вкладке
      window.location.href = url;

      // ИЛИ открыть в новой вкладке (если нужно):
      // window.open(url, '_blank', 'noopener,noreferrer');
    }
  });
});