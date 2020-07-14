from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import InputRequired, Length


class Phonebook(FlaskForm):
    """ Phonebook """
    name = wtforms.StringField('name_label', validators=[
                               InputRequired(message='Name required'), Length(min=2, max=50)])
    email = wtforms.StringField('email_label')
    phone = wtforms.IntegerField('phone_label')
    adress = wtforms.StringField('adress_label')
    submit_button = wtforms.SubmitField('Add Contact')
