from flask import render_template, redirect, url_for, flash, request
from models import Product, Order
from app import app, db
from forms import *


@app.route('/admin/add_category', methods=['GET', 'POST'])
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))  # Redirect to the admin dashboard or wherever you want
    return render_template('admin/addCategory.html', form=form)


@app.route('/admin/add_product_type', methods=['GET', 'POST'])
def add_product_type():
    form = ProductTypeForm()
    form.populate_choices()  # Populate the dropdown menu for selecting category
    if form.validate_on_submit():
        product_type = ProductType(name=form.name.data, category_id=form.category_id.data)
        db.session.add(product_type)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))  # Rediret to the admin dashboard or wherever you want
    return render_template('admin/addProductType.html', form=form)


@app.route('/admin/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    form.populate_choices()
    if form.validate_on_submit():
        # Create and add product to the database
        product = Product(
            name=form.name.data,
            price=form.price.data,
            category_id=form.category_id.data,
            type_id=form.type_id.data
            # Add more fields as needed
        )
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/addProduct.html', form=form)


@app.route('/admin/dashboard')
def admin_dashboard():
    # Fetch data for the admin dashboard
    products = Product.query.all()
    products_category = ProductsForm.Category.query.all()
    products_type = ProductsForm.ProductType.query.all()
    orders = Order.query.all()

    # Pass the fetched data to the template
    return render_template('admin/dashboard.html', products=products, categories=products_category,
                           product_types=products_type, orders=orders)


@app.route('/admin/delete_product/<int:product_id>', methods=['GET', 'POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/delete_product.html', product=product)


@app.route('/admin/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    form.populate_choices()
    if form.validate_on_submit():
        form.populate_obj(product)
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/addProduct.html', form=form)
