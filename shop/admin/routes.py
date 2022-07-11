from flask import render_template, session, request, redirect, url_for, flash

from shop import app, db, bcrypt
from shop.admin.forms import RegistrationForm
from shop.admin.models import User

@app.route('/')
def home():
    return render_template('admin/index.html', title='Admin Page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm(request.form)
    #this is a result of sended form, with all information
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome, {form.name.data}. Thanks for registring', 'success')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title='Registration page')