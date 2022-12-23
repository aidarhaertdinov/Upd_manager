from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum
from app import db

class Permissions(Enum):
    MODERATE = "MODERATE"
    ADMIN = "ADMIN"
    USER = "USER"
class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(70), unique=True)
    password = db.Column(db.Text)
    permission = db.Column(db.Enum(Permissions))
    def __init__(self, name, password, permission=Permissions.USER):
        self.user_name = name
        self.hash_password(password)
        self.permission = permission

    def __repr__(self):
        return '<User %r>' % self.id

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def can(self, perm):
        return self.permission is not None and self.permission == perm

    def to_json(self):
        return {'id': self.id,
                'user_name': self.user_name,
                'permission': self.permission.value}
    @staticmethod
    def from_json(_dict: dict):
        return User(name=_dict.get('user_name'),
                    password=_dict.get('password'),
                    permission=Permissions.__getitem__(_dict.get('permission')))


class Order(db.Model):
    __table_args__ = {'extend_existing': True}
    id_order = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    date = db.Column(db.Text)
    seller = db.Column(db.String(100))
    group = db.relationship('ProductLine', backref='order', lazy='dynamic')

    def __init__(self, number, date, seller):
        self.number = number
        self.date = date
        self.seller = seller


class ProductLine (db.Model):
    __table_args__ = {'extend_existing': True}
    id_product_line = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    unit_of_measurement = db.Column(db.String(10))
    quantity = db.Column(db.Float)
    price = db.Column(db.Float)
    cost_without_tax = db.Column(db.Float)
    tax_rate = db.Column(db.Float)
    tax_amount = db.Column(db.Float)
    cost_with_tax = db.Column(db.Float)
    id_order = db.Column(db.Integer, db.ForeignKey('order.id_order'))

    def __init__(self, product_name, unit_of_measurement, quantity, price,
                 cost_without_tax, tax_rate, tax_amount, cost_with_tax):
        self.product_name = product_name
        self.unit_of_measurement = unit_of_measurement
        self.quantity = quantity
        self.price = price
        self.cost_without_tax = cost_without_tax
        self.tax_rate = tax_rate
        self.tax_amount = tax_amount
        self.cost_with_tax = cost_with_tax

    # def __repr__(self):
    #     return f"{self.product_name}, {self.unit_of_measurement}, {self.quantity}, {self.price}, {self.cost_without_tax}," \
    #            f" {self.tax_rate}, {self.tax_amount}, {self.cost_with_tax}"