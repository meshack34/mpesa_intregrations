window.addEventListener("load", function() {
    let navbarHeight = document.querySelector("header").offsetHeight;
    document.querySelector(".offer-section").style.paddingTop = navbarHeight + "px";
});
