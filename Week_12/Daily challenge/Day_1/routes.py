import flask
from Day_1 import app


@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/CV")
def my_cv():
    return flask.render_template('CV.html')
