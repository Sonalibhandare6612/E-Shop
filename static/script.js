
// Add click event listener to all like buttons
const likeButtons = document.querySelectorAll('.likeButton');

likeButtons.forEach(likeButton => {
  likeButton.addEventListener('click', function() {
    // Get the card ID from the data attribute
    const cardId = likeButton.getAttribute('data-card-id');
    
    // Toggle the 'clicked' class to apply the color change for the specific button
    likeButton.classList.toggle('clicked');
    console.log("reached");
    
    // You can also send an AJAX request here to update the like status on the server
    // Example using fetch:
    // fetch(`/update-like/${cardId}/`)
    //   .then(response => response.json())
    //   .then(data => console.log(data));
  });
});

