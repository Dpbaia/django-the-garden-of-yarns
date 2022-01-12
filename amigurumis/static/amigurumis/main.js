// document.addEventListener('keydown', (event) => {
//     let detailpage = document.getElementById("slideshow")
//     let keyName = event.key;
//     if(detailpage){
//         if (keyName == "ArrowRight") 
//             console.log(keyName);
//         else if (keyName == "ArrowLeft") 
//             console.log(keyName);
//     }
// });


// When you click on the image in the details page, it amplifies on the 
function changeImage(param) {
    document.getElementById("slideshow").src = param.src;
    document.querySelector(".img-active").classList.remove("img-active");
    param.classList.add("img-active");
} 

// When you click on the arrow, you go to the next or previous 

function rightArrowChangeImage(){
    // Get the current active image
    let currentStep = document.querySelector(".img-active").parentElement.classList[0]
    // Find its step number
    let nextStep = parseInt(currentStep) + 1
    // Get the next step
    let nextElementParent = document.querySelector(`.\\3${nextStep}`);
    // Substitute with the new value 
    if(nextElementParent){
        let nextElement = nextElementParent.firstElementChild
        document.querySelector(".img-active").classList.remove("img-active");
        nextElement.classList.add("img-active");
        document.getElementById("slideshow").src = nextElement.src;
    } else {
        let nextElement = document.querySelector(".\\31").firstElementChild;
        document.querySelector(".img-active").classList.remove("img-active");
        nextElement.classList.add("img-active");
        document.getElementById("slideshow").src = nextElement.src;
    }
}

function leftArrowChangeImage(){
    // Get the current active image
    let currentStep = document.querySelector(".img-active").parentElement.classList[0]
    // Find its step number
    let nextStep = parseInt(currentStep) - 1
    // Get the next step
    let nextElementParent = document.querySelector(`.\\3${nextStep}`);
    // Substitute with the new value 
    if(nextElementParent){
        let nextElement = nextElementParent.firstElementChild
        document.querySelector(".img-active").classList.remove("img-active");
        nextElement.classList.add("img-active");
        document.getElementById("slideshow").src = nextElement.src;
    } else {
        let numberImgSlide = document.getElementsByClassName("img-slide").length
        let nextElement = document.querySelector(`.\\3${numberImgSlide}`).firstElementChild;
        document.querySelector(".img-active").classList.remove("img-active");
        nextElement.classList.add("img-active");
        document.getElementById("slideshow").src = nextElement.src;
    }
}