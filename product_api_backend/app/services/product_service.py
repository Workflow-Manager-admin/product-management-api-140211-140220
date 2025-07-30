from ..models.product import Product
from ..db import db

# PUBLIC_INTERFACE
def get_all_products():
    """Retrieve all products from database."""
    return Product.query.all()

# PUBLIC_INTERFACE
def get_product_by_id(product_id):
    """Retrieve a single product by its ID."""
    return Product.query.get(product_id)

# PUBLIC_INTERFACE
def create_product(data):
    """Create a new product with validated data."""
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return product

# PUBLIC_INTERFACE
def update_product(product, data):
    """Update the product with validated data."""
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return product

# PUBLIC_INTERFACE
def delete_product(product):
    """Delete the given product."""
    db.session.delete(product)
    db.session.commit()
