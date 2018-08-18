var data =
     {
  "Product": {
    "Ui": {
      "Issue_name_1": "",
      "Issue_name_2": ""
    },
    "Api": {
      "Issue_name_1": "",
      "Issue_name_2": ""
    }
  },
  "Automation": {
    "Ui": {
      "Issue_name_1": "",
      "Issue_name_2": ""
    },
    "Api": {
      "Issue_name_1": "",
      "Issue_name_2": ""
    }
  }
};
document.getElementById("json").innerHTML = JSON.stringify(data, undefined, 2);

