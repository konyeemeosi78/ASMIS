"""
models.py
"""

from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    """Database fields connection"""
    id = db.Column(db.Integer, primary_key=True)  # primary key is required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    role = db.Column(db.String(100))

class Document_repository(db.Model):
    """Database fields connection"""
    __tablename__ = 'document_repository'
    fileID = db.Column(db.Integer, primary_key=True)  # primary key is required by SQLAlchemy
    filename = db.Column(db.String(100), unique=True)
    uploaded = db.Column(db.Date)
    classification = db.Column(db.Integer)
    owner = db.Column(db.Integer)
