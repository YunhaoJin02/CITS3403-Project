from flask import render_template, request, redirect, url_for, flash
from app import app
from app.forms import LoginForm

# Home Page
# - Renders welcome_page.html
@app.route('/')
@app.route('/index')
def welcome():
    return render_template('welcome_page.html')


# Login Page
# - Renders login.html
# - Receives login credentials
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('welcome'))
    return render_template('login.html', title='Log In', form=form )

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


@app.route('/event')
def event():
    return render_template('event_page.html')


@app.route('/event_detail')
def event_detail():
    return render_template('event_detail.html')

@app.route('/cats')
def cats():
    return render_template('cats_page.html')

@app.route('/dogs')
def dogs():
    return render_template('dogs_page.html')

@app.route('/other_pets')
def other_pets():
    return render_template('other_pets_page.html')
