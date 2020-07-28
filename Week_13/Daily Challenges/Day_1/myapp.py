from flask import Flask, render_template, request, redirect, url_for, flash
from my_forms import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://azogfiityrdmyg:f4dd1214b8f3396bf1f31558b390c9beac4693446f8611ea9f020e076275ff47@ec2-52-31-233-101.eu-west-1.compute.amazonaws.com:5432/dc7gsap0a4b1m1'
db = SQLAlchemy(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    phone_form = Phonebook()
    if phone_form.validate_on_submit():
        name = phone_form.name.data
        email = phone_form.email.data
        phone = phone_form.phone.data
        address = phone_form.adress.data

        user = User(name=name, email=email, phone=phone, adress=adress)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB!"
    return render_template('index.html', form=phone_form)


if __name__ == "__main__":
    app.run(debug=True)
