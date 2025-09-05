document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('pre').forEach(pre => {
    if (pre.querySelector('.copy-btn')) return;

    pre.classList.add('code-copy-wrapper');

    const button = document.createElement('button');
    button.className = 'copy-btn';
    button.type = 'button';
    button.innerText = 'Copy';

    button.addEventListener('click', async () => {
      try {
        const code = pre.querySelector('code');
        const text = code ? code.innerText : pre.innerText;

        await navigator.clipboard.writeText(text);
        button.innerText = 'Copied!';
        setTimeout(() => {
          button.innerText = 'Copy';
        }, 1500);
      } catch (err) {
        console.error('Failed to copy', err);
      }
    });

    pre.style.position = 'relative';
    pre.appendChild(button);
  });
});
