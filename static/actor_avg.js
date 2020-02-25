let avg_btns = document.querySelectorAll(".actor_avg");

for (let btns of avg_btns){
    btns.addEventListener("mousedown",function () {
    let show_avg = this.dataset.avgrate;
    if ( event.button === 0){
        console.log(show_avg);
        let new_avg = parseFloat(show_avg) + 0.1;
        console.log(new_avg);
        this.innerHTML = new_avg.toPrecision(2);
        this.dataset.avgrate = new_avg.toPrecision(2);
    }
    if ( event.button === 2){
        event.preventDefault();
        console.log(show_avg);
        let new_avg = parseFloat(show_avg - 0.1).toPrecision(2);
        this.innerHTML = new_avg;
        this.dataset.avgrate = new_avg;
    }

 },false)
}