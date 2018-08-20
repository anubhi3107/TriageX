from datetime import datetime
from logging import DEBUG

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.logger.setLevel(DEBUG)

test_data = []


def store_data(url, ruleset):
    test_data.append(dict(
        test_url=url,
        test_ruleset=ruleset,
        date=datetime.utcnow()))


@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == "POST":
        url = request.form['Test_url']
        ruleset = request.form['Rule_set']
        store_data(url, ruleset)
        app.logger.debug('stored url: ' + url)
        app.logger.debug(request.data)
        return "Submitted"
    return render_template('index.html')


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
