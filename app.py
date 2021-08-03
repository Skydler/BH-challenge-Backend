from flask import Flask, request
from flask_restful import Resource, Api
from models.product import Product

app = Flask(__name__)
api = Api(app)

products = []
scheduled_emails = []


class ProductResource(Resource):
    def post(self):
        data = request.form
        prod = Product(
            customer_id=data["customer_id"],
            product_name=data["product_name"],
            domain=data["domain"],
            start_date=data["start_date"],
            duration_months=data["duration_months"],
        )
        products.append(prod)
        self._schedule_emails(prod)
        return "", 201

    def delete(self):
        data = request.form
        product = [
            prod
            for prod in products
            if prod.customer_id == data["customer_id"]
            and prod.product_name == data["product_name"]
            and prod.domain == data["domain"]
        ]
        products.remove(product[0])
        return "", 204

    def _schedule_emails(product):
        pass


class Email(Resource):
    def get(self):
        return scheduled_emails


api.add_resource(ProductResource, "/product")
api.add_resource(Email, "/email_schedule")

if __name__ == "__main__":
    app.run(debug=True)
