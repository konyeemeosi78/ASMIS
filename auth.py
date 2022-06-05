"""
auth.py
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from .models import User

# from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    """Render login page"""
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    """User login"""
    email = request.form.get('email')
    password = request.form.get('password')
    otp_token = request.form.get('otp_token')
    # additional field required

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    # added support for otp check
    if not user or not check_password_hash(user.password, password) \
            or not User.verify_totp(otp_token, user.otp_secret):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # Reload page if user not exist or wrong password
        # check if user has admin role
    if user.role == 'Disabled':
        flash('Access denied You are not authorized to access this page.')
        return redirect(url_for('auth.login'))  # Reload page if user is disabled

    # if the above check passes, then we know the user has the right credentials
    login_user(user)
    return redirect(url_for('main.profile'))


@auth.route('/logout')
@login_required
def logout():
    """Logout and Redirect to main page"""
    logout_user()
    return redirect(url_for('main.index'))
