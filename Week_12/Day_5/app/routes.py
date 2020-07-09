import flask
from wtforms import SelectField
from flask_wtf import FlaskForm
from app import app


class Form(FlaskForm):
    country = SelectField('country', choices=[])


@app.route("/")
def home_page():
    form = Form()
    return flask.render_template('home.html', form=form)


@app.route("/")
def main_page():
    return flask.render_template('main.html')
