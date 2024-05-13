from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.forms import LoginForm, StaffLoginForm
from app.models import UserModel, QuestionModel, AnswerModel
from flask_mail import Message
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user
from flask_login import login_user
from app.forms import RegistrationForm, QuestionForm, AnswerForm
from app.decorators import login_required



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

# Example of event page route
@app.route('/event', methods=['GET'])
def event_page():
    return render_template('event_page.html')

@app.route('/forum_page')
def forum_page():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template('forums.html', questions=questions)

@app.route('/question/<int:question_id>')
def question_details(question_id):
    # 从数据库获取指定 ID 的问题
    question = QuestionModel.query.get_or_404(question_id)
    return render_template('question_details.html', question=question)

@app.route('/edit_question/<int:question_id>', methods=['GET', 'POST'])
def edit_question(question_id):
    question = QuestionModel.query.get_or_404(question_id)
    if request.method == 'POST':
        # 更新问题逻辑
        question.title = request.form['title']
        question.content = request.form['content']
        db.session.commit()
        return redirect(url_for('question_details', question_id=question_id))
    return render_template('edit_question.html', question=question)

@app.route('/delete_question/<int:question_id>', methods=['POST'])
def delete_question(question_id):
    question = QuestionModel.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    flash('问题已成功删除。')
    return redirect(url_for('index'))  # 假设你有一个名为 'index' 的路由作为删除后的重定向目标

@app.route("/public_question", methods=['GET', 'POST'])
@login_required
def forum_p_page():
    form = QuestionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=current_user)
            db.session.add(question)
            db.session.commit()
            flash('问题成功发布！')
            return redirect('/')
        else:
            for fieldName, errorMessages in form.errors.items():
                for err in errorMessages:
                    flash(f"错误在 {fieldName}: {err}")
    return render_template('public_question.html', form=form)

@app.route("/answer/public", methods = ['POST'])
@login_required
def public_answer():
    form =AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content = content , question_id= question_id, author_id = current_user.id )
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("question_details", question_id = question_id))
    else:
        print(form.errors)
        return redirect(url_for("question_details", question_id=request.form.get("question_id")))


