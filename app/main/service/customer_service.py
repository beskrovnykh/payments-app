from app.main import db
from app.main.model.customer import Customer


def save_customer(data):
    customer = Customer.query.filter_by(name=data['name']).first()
    if not customer:
        new_customer = Customer(
            name=data['name']
        )
        save_changes(new_customer)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Customer already exists. Please Log in.',
        }
        return response_object, 409


def get_all_customers():
    return Customer.query.all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
