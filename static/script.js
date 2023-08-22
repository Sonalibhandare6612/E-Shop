var itemsInCart = 0;
var notify = document.getElementById('notify');
function addedToCart(){
    itemsInCart = itemsInCart + 1
    notify.inert = itemsInCart
}