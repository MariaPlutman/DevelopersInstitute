from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.mail.ru'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'plutman00@mail.ru'
app.config['MAIL_PASSWORD'] = '112233Mary'
app.config['MAIL_DEFAULT_SENDER'] = (
    'Maria from DevelopersInstitute', 'plutman00@mail.ru')
app.config['MAIL_MAX_EMAILS'] = None
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII ATTACHMENTS'] = False

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('Hey There', recipients=[
                  'plutman00@mail.ru'])
    # msg.add_recipient('ibraham.derik@andyes.net')
    msg.body = '<b>This is a test email sent from Maria\'s app. You don\'t need to reply.</b>'

    with app.open_resource('cat.jpeg') as cat:
        msg.attach('cat.jpeg', 'image/jpeg', cat.read())

    mail.send(msg)

    # msg = Message(subject='',
    #               recipients=[],
    #               body='',
    #               html='',
    #               sender='',
    #               cc=[],
    #               bcc=[],
    #               attachments=[],
    #               reply_to=[],
    #               date='date',
    #               charset='',
    #               extra_headers={'': ''},
    #               mail_options=[],
    #               rcpt_options=[]
    #               )

    return 'Message has been sent!'


# @app.route('/bulk')
# def bulk():
#     users = [{'name': 'Maria', 'email': 'email@email.com'}]
#     with mail.connect() as conn:
#         for user in users:
#             msg = Message('Bulk!', recipients=[user['email']])
#             conn.send(msg)


if __name__ == '__main__':
    app.run()
