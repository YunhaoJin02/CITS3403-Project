from flask import render_template, request, redirect, url_for, flash
from app import app
from app import UserModel
from .extensions import mail
from flask_mail import Message


# Home Page
# - Renders welcome_page.html
@app.route('/')
@app.route('/index')
def welcome():
    return render_template('welcome_page.html')


# Login Page
# - Renders login.html
@app.route('/login')
def login():
    
    return render_template('login.html')


# Sign Up Page
# - Renders sign_up.html
@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


# Forgot Password Page
# - Renders forgot_password.html
@app.route('/forgot_password')
def forgot_password():
    
    return render_template('forgot_password.html')





