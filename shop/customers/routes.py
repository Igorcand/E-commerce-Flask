from flask import current_app, render_template, session, request, redirect, url_for, flash
from shop import db, app, photos
from shop.customers.forms import CustomerRegisterForm
import secrets, os

@app.route('/customer/register', methods=['GET', 'POST'])
def customer_register():
    form = CustomerRegisterForm(request.form)
    return render_template('customer/register.html', form=form)