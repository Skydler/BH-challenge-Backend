from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

products = []
scheduled_emails = []


if __name__ == "__main__":
    app.run(debug=True)
