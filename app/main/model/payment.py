from app.main import db


class Payment(db.Model):

    """Payment model for storing payment related details in database"""
    __tablename__ = "payment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    paydate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return "<Payment id: '{0}', customer: {1}, amount: {2}, paydate: {3}>"\
            .format(self.id, self.customer, self.amount, self.paydate)
