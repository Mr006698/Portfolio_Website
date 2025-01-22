from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, validators

class ContactForm(FlaskForm):
    name = StringField(label='name',
                       validators=[validators.DataRequired()],
                       render_kw={'placeholder': 'name'})
    
    email = EmailField(label='email',
                       validators=[validators.DataRequired(), validators.Email()],
                       render_kw={'placeholder': 'email'})
    
    message = TextAreaField(label='message',
                            validators=[validators.DataRequired()],
                            render_kw={'placeholder': 'message'})
    
    submit = SubmitField(label='Send Message', render_kw={'form': 'contact-form'})
