function updateRule(){
        var myForm = document.getElementById('updateForm');
        console.log("here");
        event.preventDefault();
        var formData = new FormData(myForm),
        result = {};
        for (var entry of formData.entries())
        {
            result[entry[0]] = entry[1];
        }
        result = JSON.stringify(result)
        console.log(result);
        var XHR = newXMLHttpRequest()
        XHR.open("POST", "http://127.0.0.1:5000/");
        if (xhr.readsyState == 4 && xhr.status == "200") {
		    console.log(result);
		    XHR.send(result);
	    } else {
		    console.error(formData);
	    }
}