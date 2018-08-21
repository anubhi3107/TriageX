from datetime import datetime
from logging import DEBUG
from jsonschema import validate
from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)
app.logger.setLevel(DEBUG)

test_data = []


def store_data(data):
    testdata = {}
    testdata.update({"test_url" : data["Test_url"]})
    if data["Rule_set"]!="":
        testdata.update({"rule_set": data["Rule_Set"]})
    test_data.append(testdata)
    app.logger.debug(test_data)


def is_valid_json(json):
    schema = """
    {
      "$schema": "http://json-schema.org/schema#",
      "required": [
        "Automation",
        "Product"
      ],
      "type": "object",
      "properties": {
        "Product": {
          "required": [
            "Api",
            "Ui"
          ],
          "type": "object",
          "properties": {
            "Api": {
              "type": ["object", "array"]
            },
            "Ui": {
              "type": ["object", "array"]
            }
          }
        },
        "Automation": {
          "required": [
            "Api",
            "Ui"
          ],
          "type": "object",
          "properties": {
            "Api": {
              "type": ["object", "array"]
            },
            "Ui": {
              "type": ["object", "array"]
            }
          }
        }
      }
    }
    """
    validate(json, schema)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data =request.json
        # TODO: Add rule set validation here
        store_data(data)
        app.logger.debug(data)
        return "Submitted"
    return render_template('index.html')


@app.route('/update', methods=['GET', 'POST'])
def update():
    app.logger.debug(request.json);
    return "Submitted"




@app.route('/ruleset')
def ruleset():
    return render_template('ruleset.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == "POST":
        return "Submitted"
    return render_template('feedback.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error():
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
