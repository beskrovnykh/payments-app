# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from app.main.controller.customer_controller import api as customer_ns
from app.main.controller.payment_controller import api as payment_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK PAYMENTS REST API',
          version='1.0',
          description='Sample REST service for passing the hiring process'
          )

api.add_namespace(customer_ns, path='/customer')
api.add_namespace(payment_ns, path='/payment')
