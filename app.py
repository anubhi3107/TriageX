import os
from logging import DEBUG
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json
from flask import Flask, render_template, request,redirect, url_for, make_response, Response, flash
from tempfile import NamedTemporaryFile
import shutil
import csv

FLAG=0
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['json'])
app = Flask(__name__)
app.secret_key = "super secret key"
app.logger.setLevel(DEBUG)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
test_data =[]


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def uploaded_file(filename):
    file = json.loads(open(filename).read())
    if is_valid_json(file):
       return redirect(url_for('index'))
    else:
        if os.path.exists("Ruleset.json"):
            os.remove("Ruleset.json")
        return redirect(url_for('upload'))


def is_valid_json(rulejson):
    schema = json.loads(open("schema.json").read())
    try:
        validate(rulejson, schema)
        return True
    except ValidationError:
        return False


def update_ruleset(data):
    ruleset = json.loads(open('Ruleset.json').read())
    if data["errorCodeType"] == "list":
        ruleset[data["errorLabel"]][data["errorType"]].append(data["errorThread"])
        app.logger.debug(ruleset)
    else:
        ruleset[data["errorLabel"]][data["errorType"]].update({data["errorCode"] : data["errorThread"]})
    app.logger.debug(ruleset)


def update_csv(data):
    filename = 'train.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    id = data["build_id"]
    test_name = data["test_name"]
    error_thread = data["errorThread"]
    error_type = data["errorType"]
    label = data["errorLabel"]
    fields = ['ID','test_name','duration','status','errorstack','ErrorType','Label']

    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['ID']==id and row['test_name']==test_name:
                row['errorstack'], row['ErrorType'], row['Label'] = error_thread, error_type, label
            row = { 'ID': row['ID'], 'test_name': row['test_name'], 'duration': row['duration'], 'status': row['status'],
                    'errorstack': row['errorstack'], 'ErrorType': row['ErrorType'], 'Label': row['Label']}
            writer.writerow(row)
    shutil.move(tempfile.name, filename)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global FLAG
    if request.method == "POST":
        testdata = {}
        testdata.update({"test_url":request.form["test_url"]})
        is_auth = request.form.getlist("reqAuth")
        if len(is_auth) != 0:
            testdata.update({"username": request.form["username"], "password": request.form["password"]})
        app.logger.debug(testdata)
        app.logger.debug(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],"Ruleset.json")))
        if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],"Ruleset.json")):
            app.logger.debug("Redirecting to upload ruleset")
            flash("Please upload ruleset first", "warning")
            return redirect(url_for('upload'))
        FLAG = 1
        return redirect(url_for('submit'))
    return render_template('index.html', show_flag=FLAG)


@app.route('/update', methods=['GET', 'POST'])
def update():
    app.logger.debug(request.json);
    return redirect(url_for('Submitted.html'))


@app.route('/ruleset')
def ruleset():
    return render_template('ruleset.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == "POST":
        update_ruleset(request.form)
        update_csv(request.form)
        return redirect(url_for('Submitted.html'))
    return render_template('feedback.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    app.logger.debug("the request method for upload is " + request.method)
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        app.logger.debug(file)
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.filename = "Ruleset.json"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            uploaded_file("Ruleset.json")
            return redirect(url_for('index'))
    app.logger.debug("inside upload")
    return render_template('upload.html')

@app.route('/submit')
def submit():
    return render_template('Submitted.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error():
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)