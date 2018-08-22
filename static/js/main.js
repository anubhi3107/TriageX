function toggleVisibility(cb)
 {
  var ele = document.getElementById("auth-div");
  if(cb.checked==true)
  {
    ele.style.display = "block";
    document.getElementById("email").required = true;
    document.getElementById("pwd").required = true;
  }
  else{
    ele.style.display = "none";
    document.getElementById("email").required = false;
    document.getElementById("pwd").required = false;
  }
 }
