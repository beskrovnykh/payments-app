from flask_restplus import Namespace, fields


class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer', {
        'name': fields.String(required=True, description='customer name')
    })


class PaymentDto:
    api = Namespace('payment', description='payment related operations')
    payment = api.model('payment', {
        'id': fields.Integer(required=True, description='payment id'),
        'customer': fields.String(required=True, description='customer name', attribute="customer.name"),
        'amount': fields.Integer(required=True, description='amount of payment'),
        'paydate': fields.Date(required=True, description='payment date')
    })
