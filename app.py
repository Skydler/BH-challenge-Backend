from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.email import Email
from resources.product import ProductResource
from utils import utils

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(ProductResource, "/product")
api.add_resource(Email, "/email_schedule")

if __name__ == "__main__":
    utils.write_data([])  # Used to intialize or restart the "database" on each run
    app.run(debug=True)
