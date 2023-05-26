const menuBtn = document.querySelector("#menu-btn")
const closeBtn = document.querySelector("#close-btn")
const menu = document.querySelector(".nav_items")

// opn nav menu
menuBtn.addEventListener("click", () => {
    menu.style.display = "block";
    menuBtn.style.display = "none";
    closeBtn.style.display = "inline-block";
});

// close nav menu
closeBtn.addEventListener("click", () => {
    menu.style.display = "none";
    menuBtn.display = "inline-block";
    closeBtn.style.display = " " ;
})