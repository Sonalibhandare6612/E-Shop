var notify = document.getElementById('notify');
var count = 0;

function addedToCart(){
    count = count + 1;
    notify.innerHTML = count;
};