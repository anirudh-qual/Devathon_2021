
let cards = document.getElementsByClassName("card");
let i = 0;


let t = setInterval(() => {
    if (i < cards.length)
        cards[i].style.opacity = 1;
    i++;
    if (i >= cards.length) { clearInterval(t); }
}, 100);
var t2 = 0;

function search(searchbar) {
    let str = searchbar.value;
    let t2 = setTimeout(() => {
        console.log(str);
        i = 0;
        while (i < cards.length) {
            if (!cards[i].innerHTML.includes(str)) {
                cards[i].style.opacity = 0;
                cards[i].style.display = "none";
            }
            else {
                cards[i].style.opacity = 1;
                cards[i].style.display = "flex";
            }
            i++;
        }
    }, 0);
}