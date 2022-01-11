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
    console.log(currentStep);
    // Find its step number
    let nextstep = parseInt(currentStep) + 1
    console.log(nextstep);
    // Get the next step
    // Substitute with the new value 
    document.querySelector(".img-active").classList.remove("img-active"); 
}