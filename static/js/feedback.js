function toggleVisibility(cb)
 {
  var error_code = document.getElementById("ecode");

  if(cb.value=="list")
  {
    error_code.style.display = "none";
    document.getElementById("errorCode").required = false;
  }
  else{
    error_code.style.display = "block";
    document.getElementById("errorCode").required = true;
  }
 }
