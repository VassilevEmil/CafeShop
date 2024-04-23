from flask import render_template, request, session, redirect, url_for
from app import app, db
from models import Product, CreditCard, VIACustomer, Order


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        # Get the list of product IDs selected by the user
        product_ids = request.form.getlist('product_ids')
        # creating list
        products = []

        # Initialize total price
        total_price = 0
        # Iterate over the selected product IDs and retrieve the corresponding product and quantity
        for product_id in product_ids:
            # Product
            product = Product.query.get_or_404(product_id)
            # Get the quantity for this product
            quantity = int(request.form.get(f'quantity_{product_id}', 1))
            products.append([quantity,product]);
            # Calculate the subtotal for this product and add it to the total price
            subtotal = product.price * quantity
            total_price += subtotal

        # Store the updated cart back into the session

        # After adding items to the cart, redirect the user to the cart confirmation page
        return render_template('cartConfirmation.html', products=products,total_price=total_price)

    # Handle other HTTP methods if needed
    return redirect(url_for('index'))


@app.route('/process_payment', methods=['POST'])
def process_payment():
    if request.method == 'POST':
        # Retrieve payment form data
        card_number = request.form['card_number']
        expiration_date = request.form['expiration_date']
        cvv = request.form['cvv']

        # Assuming CreditCard is chosen as the payment method, create a new CreditCard object
        credit_card = CreditCard(card_number=card_number, expiry_date=expiration_date, cvv=cvv)

        # Save the credit card to the database
        db.session.add(credit_card)
        db.session.commit()
        name = request.form['name']
        address = request.form['address']
        via_card_number = request.form['via_card_number']

        via_student = VIACustomer(name=name,address=address,via_card_number=via_card_number)
        db.session.add(via_student)
        db.session.commit()

        # Retrieve order form data (assuming products are passed as JSON)
        product_ids = request.form.getlist('products[]')  # Retrieve as a list of product IDs

        print(product_ids)

        # Retrieve the actual products from the database using the IDs
        products = Product.query.filter(Product.id.in_(product_ids)).all()

        # Create a new Order object
        order = Order(via_customer=via_student, payment=credit_card)
        order.products.extend(products)
        # Save the order to the database
        db.session.add(order)
        db.session.commit()
        # Add entries to the order_product association table



        # Redirect the user to a payment success page
        return render_template('paymentSuccess.html')

    # Handle other HTTP methods if needed
    return redirect(url_for('index'))