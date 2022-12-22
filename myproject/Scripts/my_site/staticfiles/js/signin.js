function validate()
{
   
    alert("login succeded");
    window.open("home_registred.html");

}


 var modal = document.getElementById('signin');
      
      window.onclick = function(event) {
          if (event.target == modal) {
              modal.style.display = "none";
          }
      }