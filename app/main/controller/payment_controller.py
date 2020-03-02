import flask
from flask_restplus import Resource

from app.main.util.dto import PaymentDto
from app.main.service.payment_service import get_all_payments, get_payments_by_customer_name

api = PaymentDto.api
_payment = PaymentDto.payment


@api.route("")
class PaymentList(Resource):
    @api.marshal_list_with(_payment, envelope='data')
    @api.param('name', description='Customer name', type='string')
    def get(self):
        """List all payments"""
        name = flask.request.args.get("name")
        if not name:
            return get_all_payments()
        else:
            return get_payments_by_customer_name(name)
