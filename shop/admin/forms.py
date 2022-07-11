from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError

from flask_wtf import FlaskForm, Form

#WTFForm is a flexible form validarion and rendering library for Python, we can use to simplify the usabity of HTML form. Including a verifying on password and confirming password, validation if on field email is a real email

class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')