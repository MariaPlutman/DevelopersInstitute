import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'raiksdafciaewsbnrifdanjneqw'



from . import views