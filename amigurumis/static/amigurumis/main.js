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


// When you click on the image in the details page, it amplifies on the slideshow
function changeImage(param) {
    document.getElementById("slideshow").src = param.src;
    document.querySelector(".img-active").classList.remove("img-active");
    param.classList.add("img-active");
} 



// When you click on the arrow, you go to the next or previous 

// General Logic //


// Determining who's the next element 
function arrowChangeImage(nextElementParent, numberImgSlide){
    if(nextElementParent){
        // If there IS an immediate next or previous one
        let nextElement = nextElementParent.firstElementChild
        changeImage(nextElement)
    } else if (numberImgSlide){
        // If there isn't and we're going backwards
        let nextElement = document.querySelector(`.\\3${numberImgSlide}`).firstElementChild;
        changeImage(nextElement)
    } else {
        // If there isn't, and we're going forwards
        let nextElement = document.querySelector(".\\31").firstElementChild;
        changeImage(nextElement)
    }
}

// Determines which direction clicking is going

function rightArrowChangeImage(){
    // Get the current active image
    let currentStep = document.querySelector(".img-active").parentElement.classList[0]
    // Find its step number
    let nextStep = parseInt(currentStep) + 1
    // Get the next step
    let nextElementParent = document.querySelector(`.\\3${nextStep}`);
    // Substitute with the new value 
    arrowChangeImage(nextElementParent);
}

function leftArrowChangeImage(){
    // Get the current active image
    let currentStep = document.querySelector(".img-active").parentElement.classList[0]
    // Find its step number
    let nextStep = parseInt(currentStep) - 1
    // Get the next step
    let nextElementParent = document.querySelector(`.\\3${nextStep}`);
    // Substitute with the new value 
    let numberImgSlide = document.getElementsByClassName("img-slide").length
    arrowChangeImage(nextElementParent, numberImgSlide)
}


