from __init__ import login_manager, app, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import os
from sqlalchemy.orm import relationship
from sqlalchemy.exc import IntegrityError
import pandas as pd


@login_manager.user_loader
def load_user(account_id):
    return Account.query.get(account_id)


class Account(db.Model, UserMixin):
    __tablename__ = 'accounts'

    account_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    favorites = db.relationship('Favorite', backref='Account', uselist=True, lazy='dynamic')

    def __init__(self, firstname, lastname, email, username, password):
        self.first_name = firstname
        self.last_name = lastname
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class House(db.Model, UserMixin):
    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(256), index=True)
    city = db.Column(db.String(64), index=True, nullable=True)
    state = db.Column(db.String(8), index=True, nullable=True)
    zip = db.Column(db.Integer, index=True, nullable=True)
    latitude = db.Column(db.Float, index=True, nullable=True)
    longitude = db.Column(db.Float, index=True, nullable=True)
    price = db.Column(db.Integer, index=True, nullable=True)
    bathrooms = db.Column(db.Float, index=True, nullable=True)
    bedrooms = db.Column(db.Integer, index=True, nullable=True)
    livingarea = db.Column(db.Integer, index=True, nullable=True)
    homeType = db.Column(db.String(64), index=True, nullable=True)
    priceEstimate = db.Column(db.Integer, index=True, nullable=True)
    rentEstimate = db.Column(db.Integer, index=True, nullable=True)
    imgSRC = db.Column(db.String, index=True, nullable=True)
    favorites = db.relationship('Favorite', backref='House', uselist=True, lazy='dynamic')

    def __init__(self, address, city, state, zip, latitude, longitude, price, bathrooms, bedrooms, livingarea, homeType, priceEstimate, rentEstimate, imgSRC):
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.latitude = latitude
        self.longitude = longitude
        self.price = price
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.livingarea = livingarea
        self.homeType = homeType
        self.priceEstimate = priceEstimate
        self.rentEstimate = rentEstimate
        self.imgSRC = imgSRC
    
    def all_details(self):
        return {
            'id': self.id,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'price': self.price,
            'bathrooms': self.bathrooms,
            'bedrooms': self.bedrooms,
            'livingarea': self.livingarea,
            'homeType': self.homeType,
            'priceEstimate': self.priceEstimate,
            'rentEstimate': self.rentEstimate,
            'imgSRC': self.imgSRC
        }
    
    def few_details(self):
        return {
            'id': self.id,
            'address': self.address,
            'price': self.price,
            'livingarea': self.livingarea,
            'bathrooms': self.bathrooms,
            'bedrooms': self.bedrooms,
            'imgSRC': self.imgSRC
        }
    

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'))
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))

    def __init__(self, account_id, house_id):
        self.account_id = account_id
        self.house_id = house_id
