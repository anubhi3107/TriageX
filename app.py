from datetime import datetime
from flask import Flask, render_template, url_for, request
from logging import DEBUG
app = Flask(__name__)
app.logger.setLevel(DEBUG)

test_data = []


def store_data(url, ruleset):
	test_data.append(dict(
			test_url =  url,
			test_ruleset = ruleset,
			date = datetime.utcnow() ))


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		url = request.form['Test_url']
		ruleset = request.form['Rule_set']
		store_data(url, ruleset)
		app.logger.debug('stored url: ' + url)
	return render_template('index.html')


@app.route('/ruleset')
def ruleset():
	return render_template('ruleset.html')


if __name__ == "__main__":
	app.run(debug=True)
