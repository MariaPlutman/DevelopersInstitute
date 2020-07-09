import flask
import flask_wtf
import wtforms as wtf
from wtforms import validators as valid


class SignUpForm(flask_wtf.FlaskForm):
    firstname = wtf.StringField(
        "First Name", validators=[valid.DataRequired()])
    lastname = wtf.StringField(
        "Last Name", validators=[valid.DataRequired()])
    submit = wtf.SubmitField("Register")
