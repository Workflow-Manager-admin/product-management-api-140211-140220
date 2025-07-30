from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from ..schemas.product_schema import ProductSchema
from ..services.product_service import (
    get_all_products, get_product_by_id, create_product,
    update_product, delete_product
)

blp = Blueprint(
    "Products",
    __name__,
    url_prefix="/products",
    description="Operations on products"
)


@blp.route("/")
class ProductsList(MethodView):
    # PUBLIC_INTERFACE
    @blp.response(200, ProductSchema(many=True))
    def get(self):
        """
        List all products.
        """
        products = get_all_products()
        return products

    # PUBLIC_INTERFACE
    @blp.arguments(ProductSchema)
    @blp.response(201, ProductSchema)
    def post(self, product_data):
        """
        Create a new product.
        """
        try:
            product = create_product(product_data)
        except SQLAlchemyError as e:
            abort(400, message=f"Database error: {str(e)}")
        return product


@blp.route("/<int:product_id>")
class ProductResource(MethodView):
    # PUBLIC_INTERFACE
    @blp.response(200, ProductSchema)
    def get(self, product_id):
        """
        Get a product by ID.
        """
        product = get_product_by_id(product_id)
        if not product:
            abort(404, message="Product not found")
        return product

    # PUBLIC_INTERFACE
    @blp.arguments(ProductSchema)
    @blp.response(200, ProductSchema)
    def put(self, product_data, product_id):
        """
        Update a product by ID.
        """
        product = get_product_by_id(product_id)
        if not product:
            abort(404, message="Product not found")
        try:
            updated = update_product(product, product_data)
        except SQLAlchemyError as e:
            abort(400, message=f"Database error: {str(e)}")
        return updated

    # PUBLIC_INTERFACE
    def delete(self, product_id):
        """
        Delete a product by ID.
        """
        product = get_product_by_id(product_id)
        if not product:
            abort(404, message="Product not found")
        try:
            delete_product(product)
        except SQLAlchemyError as e:
            abort(400, message=f"Database error: {str(e)}")
        return {"message": "Product deleted."}
