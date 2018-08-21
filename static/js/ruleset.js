var data1 =
{
  "Product": {
    "Ui": {
      "Error_code_1": "Error_string_1",
      "Error_code_2": "Error_string_2"
    },
    "Api": {
      "Error_code_3": "Error_string_3",
      "Error_code_4": "Error_string_4"
    }
  },
  "Automation": {
    "Ui": {
      "Error_code_5": "Error_string_5",
      "Error_code_6": "Error_string_6"
    },
    "Api": {
      "Error_code_7": "Error_string_7",
      "Error_code_8": "Error_string_8"
    }
  }
};
var data2=
{
   "Product": {
    "Ui": ["Errror_string_a", "Error_string_b"],
    "Api": ["Errror_string_c", "Error_string_d"]
  },
  "Automation": {
    "Ui": ["Errror_string_e", "Error_string_f"],
    "Api": ["Errror_string_g", "Error_string_h"]
  }
};
document.getElementById("json1").innerHTML = JSON.stringify(data1, undefined, 2);
document.getElementById("json2").innerHTML = JSON.stringify(data2, undefined, 2);


