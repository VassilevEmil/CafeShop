from flask import render_template
from app import app
from models import Product


@app.route('/')
def index():
    # Retrieve products from the database
    products = Product.query.all()
    return render_template('Index.html', products=products)
