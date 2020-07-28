from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import InputRequired, Length, ValidationError
from models import User


class Phonebook(FlaskForm):
    name = wtforms.StringField('name_label', validators=[
                               InputRequired(message='Name required'), Length(min=2, max=50)])
    email = wtforms.StringField('email_label')
    phone = wtforms.StringField('phone_label')
    adress = wtforms.StringField('adress_label')
    submit_button = wtforms.SubmitField('Add Contact')

    def validate_email(self, email):
        user_email = User.query.filter_by(email=email).first()
        if user_email:
            raise ValidationError(
                "This email already exists. Select anothe one.")

    def validate_phone(self, phone):
        user_phone = User.query.filter_by(phone=phone).first()
        if user_phone:
            raise ValidationError(
                "This phone already exists. Select anothe one.")


class SearchInput(FlaskForm):
    name = wtforms.StringField('name_label')
    number = wtforms.StringField('phone_label')
    submit = wtforms.SubmitField('search_label')
