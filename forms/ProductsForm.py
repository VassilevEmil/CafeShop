from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired
from models.Product import Category, ProductType


class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Add Category')


class ProductTypeForm(FlaskForm):
        name = StringField('Product Type Name', validators=[DataRequired()])
        category_id = SelectField('Category', coerce=int)
        submit = SubmitField('Add Product Type')

        def populate_choices(self):
            self.category_id.choices = [(category.id, category.name) for category in Category.query.all()]

class ProductForm(FlaskForm):
        name = StringField('Product Name', validators=[DataRequired()])
        price = DecimalField('Price', validators=[DataRequired()])
        category_id = SelectField('Category', coerce=int)
        type_id = SelectField('Product Type', coerce=int)
        submit = SubmitField('Add Product')

        def populate_choices(self):
            self.category_id.choices = [(category.id, category.name) for category in Category.query.all()]
            self.type_id.choices = [(product_type.id, product_type.name) for product_type in ProductType.query.all()]