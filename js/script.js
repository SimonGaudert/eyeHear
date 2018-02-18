button_pressed =  document.getElementById("press-btn"); 

button_pressed.addEventListener("click", myFunction);

function myFunction() {
   exec('python /testAPI.py')
}