import flask

from . import forms
from . import app
import json


@app.route("/", methods=("GET", "POST"))
def index():
    form = forms.SignUpForm()

    if form.is_submitted():
        result = flask.request.form
        with open('data.json', 'r+') as f:
            json.dump(result, f, indent=4)

    return flask.render_template("signup.html", form=form, title='Register')
