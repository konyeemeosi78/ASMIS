"""Reads files from document_repository table and displays them in a list
(Filtered by classification = 1 to show how to specify what is displayed."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import DocumentRepository


app = Flask(__name__)

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


# DB name and path details for connection
DB_NAME = 'sql5495299'

app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://sql5495299:hz7bDRYNPh@sql5.\
freesqldatabase.com:3306/sql5495299"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# this variable, db, will be used for all SQLAlchemy commands

db = SQLAlchemy(app)

# db.Model is required - don't change it

# import DocumentRepository class (table) from models.py


# routes

@app.route('/')
def index():
    """display file listing results in a table"""
    try:
        document_repository = DocumentRepository.query.\
            filter_by(classification=1).\
            order_by(DocumentRepository.filename).all()
        doc_text = '<ul><lh>File Name</lh>'
        for doc in document_repository:
            doc_text += '<li>' + doc.filename + '</li>'
        doc_text += '</ul>'
        return doc_text
    except Exception as exc:
        # exc holds description of the error
        error_text = "<p>The error:<br>" + str(exc) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run(debug=True)
