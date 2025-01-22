from flask import Flask, render_template, redirect, url_for, flash, request
from datetime import date
import smtplib
from email.message import EmailMessage
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


@app.route('/', methods=['POST', 'GET'])
def index() -> str:
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        send_email(contact_form)
        return redirect(url_for('index'))
    
    return render_template('index.html', form=contact_form, year=date.today().strftime('%Y'))


@app.route('/projects')
def projects() -> str:
    #return render_template('projects.html')
    pass


if __name__ == '__main__':
    app.run(debug=True)
    pass
