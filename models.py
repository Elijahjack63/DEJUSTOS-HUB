# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database import db
import json


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    notes = db.Column(db.Text)
    items = db.Column(db.Text, nullable=False)  # store JSON string
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, customer, items, total):
        self.customer_name = f"{customer.get('firstName', '')} {customer.get('lastName', '')}"
        self.phone = customer.get('phone')
        self.email = customer.get('email')
        self.city = customer.get('city')
        self.state = customer.get('state')
        self.notes = customer.get('notes')
        self.items = json.dumps(items)
        self.total = total


class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500), nullable=True)  # kept for backward compatibility
    images = db.Column(db.Text, nullable=True)  # store multiple images as a JSON string
    stock = db.Column(db.Integer, default=0)
    is_popular = db.Column(db.Boolean, default=False)


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_url": self.image_url,
            "images": json.loads(self.images) if self.images else [],  # return as list
            "category": self.category,
            "stock": self.stock,
            'is_popular': self.is_popular
        }


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


