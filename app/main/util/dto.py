from flask_restplus import Namespace, fields


class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer', {
        'name': fields.String(required=True, description='customer name')
    })
