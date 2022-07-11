from flask import render_template, session, request, redirect, url_for, flash

from shop import app, db
from shop.admin.forms import RegistrationForm

@app.route('/')
def home():
    return 'Home page of your shop'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm(request.form)
    #this is a result of sended form, with all information
    if request.method == 'POST' and form.validate():
        flash('thanks for registring')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title='Registration page')