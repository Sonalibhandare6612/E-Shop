// Add event listener to the button
const likeButton = document.getElementById('likeButton');
likeButton.addEventListener('click', function() {
  // Toggle the 'clicked' class to apply the color change
  likeButton.classList.toggle('clicked');
});
