from flask import render_template, session, request, redirect, url_for, flash
from shop import db, app 
from shop.products.models import Brand, Category
from shop.products.forms import Addproducts


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method=='POST':
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f'The brand {getbrand} was added to your database', 'success')
        return redirect(url_for('addbrand'))

    
    return render_template('products/addbrand.html', brands='brands')

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method=='POST':
        getcat = request.form.get('category')
        category = Category(name=getcat)
        db.session.add(category)
        db.session.commit()
        flash(f'The category {getcat} was added to your database', 'success')
        return redirect(url_for('addcat'))

    
    return render_template('products/addbrand.html')



@app.route('/addproduct', methods=['POST','GET'])
def addproduct():
    form = Addproducts(request.form)
    return render_template('products/addproduct.html', title='Add product page', form=form)
