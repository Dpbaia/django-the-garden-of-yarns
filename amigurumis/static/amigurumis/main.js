console.log('It works!');

function changeImage(param) {
    document.getElementById("slideshow").src = param.src;
    document.querySelector(".img-active").classList.remove("img-active");
    param.classList.add("img-active");
} 