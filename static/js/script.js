button_pressed =  document.getElementById("press-btn"); 

button_pressed.addEventListener("click", myFunction);

function myFunction() {
	$.ajax({
			url: "/foo",
            success: function(){
            	console.log('said');
            },
            error: ()=>{
            	console.log('an error occured');
            }
      });

	console.log('lol');
}