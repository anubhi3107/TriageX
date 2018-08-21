window.addEventListener("load", function () {
  function sendData() {
    var XHR = new XMLHttpRequest();

    // Bind the FormData object and the form element
    var myForm = document.getElementById('urlForm');
    console.log("here");
    var formData = new FormData(myForm),
    result = {};
    for (var entry of formData.entries())
    {
        result[entry[0]] = entry[1];
    }
    result = JSON.stringify(result)
    console.log(result);

    // Define what happens on successful data submission
    XHR.addEventListener("load", function(event) {
      alert(event.target.responseText);
    });

    // Define what happens in case of error
    XHR.addEventListener("error", function(event) {
      alert('Oops! Something went wrong.');
    });

    // Set up our request
    XHR.open("POST", "http://127.0.0.1:5000/");
    XHR.setRequestHeader("Content-Type", "application/json")
    // The data sent is what the user provided in the form
    console.log("sending");
    XHR.send(result);
  }

  // Access the form element...
  var form = document.getElementById("urlForm");

  // ...and take over its submit event.
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    sendData();
  });
});

//function sendData(){
//        event.preventDefault();
//        var myForm = document.getElementById('urlForm');
//        console.log("here");
//        var formData = new FormData(myForm),
//        result = {};
//        for (var entry of formData.entries())
//        {
//            result[entry[0]] = entry[1];
//        }
//        result = JSON.stringify(result)
//        console.log(result);
//        var xhr = new XMLHttpRequest();
//        xhr.onreadystatechange = function(){
//            if (xhr.readyState == 4 && xhr.status == "200") {
//                xhr.open("POST", "http://127.0.0.1:5000/");
//                console.log("sending");
//		        console.log(result);
//		        xhr.send(result);
//        }
//        else {
//	        console.log(xhr.readyState);
//	        console.log(xhr.status);
//		    console.error(formData);
//	    }
//        };
//}