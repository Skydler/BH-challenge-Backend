from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields
from models.product import Product
from datetime import datetime

app = Flask(__name__)
api = Api(app)

products = []


class ProductResource(Resource):
    def post(self):
        data = request.form

        start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")
        prod = Product(
            customer_id=data["customer_id"],
            product_name=data["product_name"],
            domain=data["domain"],
            start_date=start_date,
            duration_months=int(data["duration_months"]),
        )
        products.append(prod)
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
        if product:
            products.remove(product[0])
            return "", 204
        else:
            return "Product not found", 404


email_fields = {
    "customer_id": fields.String,
    "product_name": fields.String,
    "domain": fields.String,
    "email_date": fields.DateTime(dt_format="iso8601"),
}


class Email(Resource):
    @marshal_with(email_fields)
    def get(self):
        emails = []
        for prod in products:
            for email_date in prod.scheduled_emails:
                emails.append(
                    {
                        "customer_id": prod.customer_id,
                        "product_name": prod.product_name,
                        "domain": prod.domain,
                        "email_date": email_date,
                    }
                )
        sorted_emails = sorted(emails, key=lambda x: x["email_date"])
        return sorted_emails


api.add_resource(ProductResource, "/product")
api.add_resource(Email, "/email_schedule")

if __name__ == "__main__":
    app.run(debug=True)
