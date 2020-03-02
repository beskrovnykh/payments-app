from app.main import db
from app.main.model.payment import Payment


class Customer(db.Model):

    """Customer model for storing customer related details in database"""
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    payments = db.relationship(Payment, backref='customer', lazy=True)

    def __repr__(self):
        return "<Customer id: {0}, name: '{1}'>".format(self.id, self.name)
