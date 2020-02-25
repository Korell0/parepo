let trailerbtns = document.querySelectorAll(".show_trailer");
let modal = document.getElementById("myModal");
let span = document.getElementsByClassName("close")[0];

console.log(modal);
console.log(trailerbtns);



// trailerbtns.addEventListener("click",function () {
//         modal.style.display = "block";});


for (let btn of trailerbtns){
    btn.addEventListener("click",function () {
        modal.style.display = "block";

    })
}

span.addEventListener("click",function() {
  modal.style.display = "none";
});