from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, IntegerField, TextAreaField, DecimalField
from flask_wtf import Form
from flask_wtf.file import FileAllowed, FileField, FileRequired

#WTFForm is a flexible form validarion and rendering library for Python, we can use to simplify the usabity of HTML form. Including a verifying on password and confirming password, validation if on field email is a real email

class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
    color = TextAreaField('Color', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

