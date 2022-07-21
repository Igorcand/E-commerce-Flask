from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, IntegerField, TextAreaField, DecimalField, SubmitField
from flask_wtf import Form
from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf import FlaskForm
from .models import Register


class CustomerRegisterForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25), validators.DataRequired()])
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password',[validators.DataRequired()])

    country = StringField('Country', [validators.DataRequired()])
    state = StringField('State', [validators.DataRequired()])
    city = StringField('City', [validators.DataRequired()])
    contact = StringField('Contat', [validators.DataRequired()])
    address = StringField('address', [validators.DataRequired()])
    zipcode = StringField('Zip code', [validators.DataRequired()])

    profile = FileField('Profile', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])

    submit = SubmitField('Register')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError('This username is already in use!')
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError('This email address is already in use!')

class CustomerLoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
