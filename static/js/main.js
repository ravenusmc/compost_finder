//This file will handle all of the javascript code for the program

//This function will change the background image to dirt 
function changeBackgroundImage() {
  let target = document.getElementById('signUpMain');
  let targetTwo = document.getElementById('signupSubHeading');
  target.style.backgroundImage = "url('/static/img/dirt.jpg')";
  targetTwo.innerHTML = '...Into compost!';
}

//This function will change the background image back to trash on the 
//sign up page
function changeImageBack() {
  let target = document.getElementById('signUpMain');
  let targetTwo = document.getElementById('signupSubHeading');

  target.style.backgroundImage = "url('/static/img/trash.jpg')";
  targetTwo.innerHTML = '';
}