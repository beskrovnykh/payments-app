from flask import request
from flask_restplus import Resource

from app.main.util.dto import CustomerDto
from app.main.service.customer_service import save_customer, get_all_customers

api = CustomerDto.api
_customer = CustomerDto.customer


@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_registered_customers')
    @api.marshal_list_with(_customer, envelope='data')
    def get(self):
        """List all registered customers"""
        return get_all_customers()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new customer')
    @api.expect(_customer, validate=True)
    def post(self):
        """Create a new Customer """
        data = request.json
        return save_customer(data=data)
