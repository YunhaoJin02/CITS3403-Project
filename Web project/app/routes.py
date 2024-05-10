from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.forms import LoginForm, StaffLoginForm
from app.models import UserModel
from app.extensions import mail
from flask_mail import Message
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user
from flask_login import login_user
from app.forms import RegistrationForm




# Home Page
# - Renders welcome_page.html
@app.route('/')
@app.route('/index')
def welcome():
    return render_template('welcome_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    customer_login_form = LoginForm()
    staff_login_form = StaffLoginForm()
    
    if request.method == 'POST':
        if customer_login_form.validate_on_submit():
            username = customer_login_form.username.data
            password = customer_login_form.password.data
            
            user = UserModel.query.filter_by(username=username).first()
            if user is None or not user.check_password(password):
                flash('Invalid username or password.', 'error')
                return redirect(url_for('login'))
            
            # Logic for successful customer login
            flash('Customer login successful!')
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        
        elif staff_login_form.validate_on_submit():
            # Logic for staff login
            staff_username = staff_login_form.username.data
            staff_password = staff_login_form.password.data

            staff = StaffModel.query.filter_by(username=staff_username).first()
            if staff is None or not staff.check_password(staff_password):
                flash('Invalid staff username or password.', 'error')
                return redirect(url_for('login'))
            
            # Logic for successful staff login
            flash('Staff login successful!')
            login_user(staff)
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)

    return render_template('login.html', form=customer_login_form, staff_form=staff_login_form)

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Use UserModel instead of User
        user = UserModel(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('sign_up.html', title='Register', form=form)

# Forgot Password Page
# - Renders forgot_password.html
@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')


# Additional routes go here

# Example of event page route
@app.route('/event', methods=['GET'])
def event_page():
    return render_template('event_page.html')

#Logout route
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", title='Home Page', posts=posts)
