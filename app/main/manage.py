import unittest
from datetime import datetime

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model.customer import Customer
from app.main.model.payment import Payment

from app.main.model import customer
from app.main.model import payment

app = create_app('test')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    db.session.add(Customer(id=1, name="Иван"))
    db.session.add(Customer(id=2, name="Владимир"))
    db.session.add(Customer(id=3, name="Ольга"))
    db.session.add(Customer(id=4, name="Frank"))
    db.session.add(Payment(id=101, customer_id=1, amount=1000, paydate=to_date("2017-05-06")))
    db.session.add(Payment(id=102, customer_id=2, amount=500, paydate=to_date("2018-04-12")))
    db.session.add(Payment(id=103, customer_id=1, amount=100, paydate=to_date("2018-05-06")))
    db.session.add(Payment(id=104, customer_id=1, amount=750, paydate=to_date("2018-06-07")))
    db.session.add(Payment(id=105, customer_id=2, amount=100, paydate=to_date("2018-07-06")))
    db.session.add(Payment(id=106, customer_id=3, amount=5, paydate=to_date("2018-07-12")))
    db.session.add(Payment(id=107, customer_id=2, amount=200, paydate=to_date("2018-08-06")))
    db.session.add(Payment(id=108, customer_id=3, amount=3, paydate=to_date("2018-09-22")))
    db.session.add(Payment(id=109, customer_id=1, amount=500, paydate=to_date("2018-10-09")))
    db.session.add(Payment(id=110, customer_id=4, amount=15, paydate=to_date("2018-10-15")))
    db.session.add(Payment(id=111, customer_id=4, amount=17, paydate=to_date("2019-01-16")))
    db.session.commit()


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


def to_date(data_str):
    return datetime.strptime(data_str, "%Y-%m-%d").date()


if __name__ == '__main__':
    manager.run()
