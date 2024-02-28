
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    product = db.relationship('Product', backref='author', lazy='dynamic')
    def __repr__(self):
        return f'User {self.username}'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(4000))
    description= db.Column(db.String(10000))
    stock= db.Column(db.Integer)

    def __repr__(self):
        return f'Product: {self.product_name}'
    
