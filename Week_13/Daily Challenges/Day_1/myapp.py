from flask import Flask, render_template
from my_forms import *

app = Flask(__name__)
app.secret_key = 'replace later'


@app.route("/", methods=['GET', 'POST'])
def index():
    phone_form = Phonebook()

    return render_template('index.html', form=phone_form)


if __name__ == "__main__":
    app.run(debug=True)
