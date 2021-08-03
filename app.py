from flask import Flask
from flask_restful import Resource, Api
from models.product import Product

app = Flask(__name__)
api = Api(app)

products = []
scheduled_emails = []


class ProductResource(Resource):
    def post(self):
        pass

    def delete(self):
        pass


class Email(Resource):
    def get(self):
        return scheduled_emails


api.add_resource(ProductResource, "/product")
api.add_resource(Email, "/email_schedule")

if __name__ == "__main__":
    app.run(debug=True)
