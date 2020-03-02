from app.main.model.payment import Payment
from app.main.model.customer import Customer


def get_all_payments():
    return Payment.query.all()


def get_payments_by_customer_name(customer_name):
    return Payment.query.join(Customer).filter(Customer.name == customer_name).all()
