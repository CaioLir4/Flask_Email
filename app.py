from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações de e-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'caio02gomeslira@gmail.com'
app.config['MAIL_PASSWORD'] = 'peen hofa htif koxc'
app.config['MAIL_DEFAULT_SENDER'] = 'seu_email@gmail.com'

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    recipient = request.form['email']
    subject = request.form['subject']
    body = request.form['body']

    msg = Message(subject, recipients=[recipient])
    msg.body = body

    try:
        mail.send(msg)
        return 'Email enviado com sucesso!'
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
