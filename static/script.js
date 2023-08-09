document.addEventListener('DOMContentLoaded', function() {
  const button = document.getElementById('color-change-button');

  button.addEventListener('click', function() {
      button.classList.add('clicked');
  });
});
