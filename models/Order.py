from datetime import datetime

from app import db

# Association table for the many-to-many relationship between orders and products

order_product = db.Table(
    'order_product', db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    via_customer_id = db.Column(db.Integer, db.ForeignKey('via_customer.id'), nullable=False)

    # this line here defines a relationship between VIACustomer and Order tables
    # it establishes a one-to-many relationship
    # the backref param creates a virtual attribute 'orders' on viacustomer class
    via_customer = db.relationship('VIACustomer', backref=db.backref('orders', lazy=True))
    payment_id = db.Column(db.Integer, db.ForeignKey('credit_card.id'), nullable=False)

    # useList indicates this relationship should not return a list of results
    payment = db.relationship('CreditCard', backref=db.backref('order', uselist=False))
    products = db.relationship('Product', secondary=order_product, backref=db.backref('orders', lazy='dynamic'))
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Define the foreign key constraint within the table definition
    __table_args__ = (
        db.ForeignKeyConstraint(['via_customer_id'], ['via_customer.id'], name='fk_order_via_customer_id'),
    )

    # this method provides a human readable string representation
    def __repr__(self):
        return f"Order(id={self.id}, via_customer={self.via_customer_id}, payment={self.payment_id}, order_date={self.order_date})"
