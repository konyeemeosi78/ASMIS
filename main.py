"""
main.py
"""

from flask import Blueprint, render_template, request, send_file, flash
from flask_login import login_required, current_user
from .models import Document
from . import db
from io import BytesIO
from cryptography.fernet import Fernet


main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Index page"""
    return render_template('index.html')
    #generates index page


@main.route('/profile')
@login_required
def profile():
    """User profile page (login required)"""
    return render_template('profile.html', name=current_user.name)
    #generates user profile page following login


@main.route('/upload')
@login_required
def upload():
    """Upload page (login required)"""
    return render_template('upload.html')
    #generates file upload page


@main.route('/upload', methods=['POST'])
def upload_post():
    """Upload File"""
    file = request.files['file']
    role = request.form.get('role')
    file_key = Fernet.generate_key()
    cipher_suite = Fernet(file_key)
    encrypted_data = cipher_suite.encrypt(file.read())
    #Fernet encryption key generated for uploaded file

    fileupload = Document(filename=file.filename, data=encrypted_data, role=role, key=file_key)
    db.session.add(fileupload)
    db.session.commit()
    flash('File Uploaded')
    return render_template('upload.html')
    #Confirmation page of file uploaded


@main.route('/download')
@login_required
def download():
    """Download page (login required), display file listing results in a table"""
    documents = Document.query.filter_by(role=current_user.role).order_by(Document.fileid).all()
    return render_template('download.html', documents=documents)
    #Generated download page following authentication of user


@main.route('/download', methods=['POST'])
def download_post():
    """display file listing results in a table"""
    fileid = request.form.get('download_id')
    file = Document.query.filter_by(fileid=fileid).first()
    cipher_suite = Fernet(file.key)
    decrypted_data = cipher_suite.decrypt(file.data)
    return send_file(BytesIO(decrypted_data), attachment_filename=file.filename, as_attachment=True)
    #Decryption of file in downloading
