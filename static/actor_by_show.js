let actors = document.getElementsByClassName("actor_name");
let shows = document.getElementsByClassName("shows");

for (const show of shows) {
    show.addEventListener("mouseover", function () {
        const show_id = show.dataset.showid;
        for (let actor of actors) {
            if (show_id === actor.dataset.actorid) {
                actor.style.backgroundColor = "yellow"
            }
        }
        console.log(show_id);


    })
}
for (const show of shows) {
    show.addEventListener("mouseout", function () {
        const show_id = show.dataset.showid;
        for (let actor of actors) {
            if (show_id === actor.dataset.actorid) {
                actor.style.backgroundColor = "white"
            }
        }
        console.log(show_id);


    })
}

for (const actor of actors) {
    actor.addEventListener("mouseover", function () {
        const actor_id = actor.dataset.actorid;
        for (let show of shows) {
            if (actor_id === show.dataset.showid) {
                show.style.backgroundColor = "yellow"
            }
        }
    })
}
for (const actor of actors) {
    actor.addEventListener("mouseout", function () {
        const actor_id = actor.dataset.actorid;
        for (let show of shows) {
            if (actor_id === show.dataset.showid) {
                show.style.backgroundColor = "white"
            }
        }
    })}



