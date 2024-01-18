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
    
