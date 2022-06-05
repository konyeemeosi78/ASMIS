"""
models.py
"""
import onetimepass
from flask_login import UserMixin
#from __init__ import db
from . import db

class User(UserMixin, db.Model):
    """Database fields connection"""
    id = db.Column(db.Integer, primary_key=True)  # primary key is required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    role = db.Column(db.String(100))
    otp_secret = db.Column(db.String(16))    

    @staticmethod
    def verify_totp(token, otp_secret):
        """function to verify the user provided and the secret code stored."""
        return onetimepass.valid_totp(token, otp_secret)

class Document(db.Model):
    """Database fields connection"""
    fileid = db.Column(db.Integer, primary_key=True)  # primary key is required by SQLAlchemy
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    role = db.Column(db.String(100))
