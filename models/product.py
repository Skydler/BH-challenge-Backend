from datetime import timedelta


class Product:
    def __init__(self, customer_id, product_name, domain, start_date, duration_months):
        self.customer_id = customer_id
        self.product_name = product_name
        self.domain = domain
        self.start_date = start_date
        self.duration_months = duration_months

        self.scheduled_emails = []
        self._calculate_email_schedule()

    def _calculate_email_schedule(self):
        duration_days = self.duration_months * 30  # Assuming a month has 30 days
        expiration_date = self.start_date + timedelta(days=duration_days)

        if self.product_name == "domain":
            self.scheduled_emails.append(expiration_date - timedelta(days=2))
        elif self.product_name == "hosting":
            self.scheduled_emails.append(expiration_date - timedelta(days=3))
            self.scheduled_emails.append(self.start_date + timedelta(days=1))
        elif self.product_name == "pdomain":
            self.scheduled_emails.append(expiration_date - timedelta(days=2))
            self.scheduled_emails.append(expiration_date - timedelta(days=9))
