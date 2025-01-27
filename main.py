from flask import Flask, render_template
from datetime import date
import smtplib
from email.message import EmailMessage
# from twilio.rest import Client
import os

from contact_form import ContactForm

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_KEY')

# Send email message
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
def send_email(form: ContactForm) -> None:

    with smtplib.SMTP(EMAIL_HOST) as connection:
        msg = EmailMessage()
        msg.set_content(f'Message From: {form.name.data}\nEmail: {form.email.data}\n\n{form.message.data}')
        msg['Subject'] = f'Code-Alchemy Message From: {form.name.data}'
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = EMAIL_HOST_USER
        connection.starttls()
        connection.login(user=EMAIL_HOST_USER, password=EMAIL_HOST_PASSWORD)
        connection.send_message(msg)


# # Send SMS message
# TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
# TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
# TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
# WHATSAPP_PHONE_NUMBER = os.environ.get('WHATSAPP_PHONE_NUMBER')

# def send_sms(form: ContactForm) -> None:
#     account_sid = TWILIO_ACCOUNT_SID
#     auth_token = TWILIO_AUTH_TOKEN
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#         body=f'Message From: {form.name.data}\nEmail: {form.email.data}\n\n{form.message.data}',
#         from_=TWILIO_PHONE_NUMBER,
#         to=WHATSAPP_PHONE_NUMBER
#     )

#     print(message.status)


# Index route
@app.route('/')
def index() -> str:
    contact_form = ContactForm()
    return render_template('index.html', form=contact_form, year=date.today().strftime('%Y'))


@app.route('/submit', methods=['POST'])
def submit() -> str:
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        send_email(contact_form)
        #send_sms(contact_form)
        pass

    return('Message Sent')


@app.route('/projects')
def projects() -> str:
    #return render_template('projects.html')
    pass


if __name__ == '__main__':
    app.run(debug=True)
    