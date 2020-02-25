let alive_cards = document.getElementsByClassName("alive_card");
let dead_cards = document.getElementsByClassName("dead_card");


for ( let card of alive_cards)
        card.addEventListener("mouseover",function () {
        card.style.backgroundColor="green"
    });
for ( let card of alive_cards)
        card.addEventListener("mouseout",function () {
        card.style.backgroundColor="white"
    });

for ( let card of dead_cards)
        card.addEventListener("mouseover",function () {
        card.style.backgroundColor="black";
        card.style.color="white"
    });
for ( let card of dead_cards)
        card.addEventListener("mouseout",function () {
        card.style.backgroundColor="white";
        card.style.color="black"
    });
