from app.main.model.customer import Customer


def get_all_customers():
    return Customer.query.all()
