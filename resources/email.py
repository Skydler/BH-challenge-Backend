from flask_restful import Resource, marshal_with, fields
from utils import utils

email_fields = {
    "customer_id": fields.String,
    "product_name": fields.String,
    "domain": fields.String,
    "email_date": fields.DateTime(dt_format="iso8601"),
}


class Email(Resource):
    @marshal_with(email_fields)
    def get(self):
        products = utils.read_data()
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
