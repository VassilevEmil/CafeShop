from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'), nullable=False)

    # Remove the 'orders' relationship
    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, category_id={self.category_id}, type_id={self.type_id})"

class Category(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), unique=True)
        products = db.relationship('Product', backref='category', lazy=True)

        def __repr__(self):
            return f"Category(id={self.id}, name={self.name})"

class ProductType(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), unique=True)
        category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
        category = db.relationship('Category', backref='product_types', lazy=True)
        products = db.relationship('Product', backref='product_type', lazy=True)

        def __repr__(self):
            return f"ProductType(id={self.id}, name={self.name}, category_id={self.category_id})"


