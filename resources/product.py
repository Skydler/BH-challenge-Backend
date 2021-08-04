from flask_restful import Resource, reqparse, inputs
from models.product import Product
from utils import utils

delete_parser = reqparse.RequestParser()
delete_parser.add_argument("customer_id")
delete_parser.add_argument("product_name")
delete_parser.add_argument("domain")

post_parser = delete_parser.copy()
post_parser.add_argument("start_date", type=inputs.date)
post_parser.add_argument("duration_months", type=int)


class ProductResource(Resource):
    def post(self):
        args = post_parser.parse_args(strict=True)

        prod = Product(
            customer_id=args["customer_id"],
            product_name=args["product_name"],
            domain=args["domain"],
            start_date=args["start_date"],
            duration_months=int(args["duration_months"]),
        )

        products = utils.read_data()
        products.append(prod)
        utils.write_data(products)
        return "", 201

    def delete(self):
        args = delete_parser.parse_args(strict=True)
        products = utils.read_data()

        product = [
            prod
            for prod in products
            if prod.customer_id == args["customer_id"]
            and prod.product_name == args["product_name"]
            and prod.domain == args["domain"]
        ]
        if product:
            products.remove(product[0])
            utils.write_data(products)
            return "", 204
        else:
            return "Product not found", 404
