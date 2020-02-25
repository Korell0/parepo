let modal = document.getElementById("myModal");

// Get the button that opens the modal
let btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0];

console.log(modal);
console.log(btn);
console.log(span);

btn.addEventListener("click",function() {
  modal.style.display = "block";
});

span.addEventListener("click",function() {
  modal.style.display = "none";
});
