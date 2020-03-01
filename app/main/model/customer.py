from app.main import db


class Customer(db.Model):

    """Customer model for storing customer related details in database"""
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return "<Customer '{}'>".format(self.name)
