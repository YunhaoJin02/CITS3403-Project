from app.extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from sqlalchemy import Column, DateTime

class UserModel(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # Storing the hashed password
    email = db.Column(db.String(100), nullable=False, unique=True)

    # Method to set the password hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Method to check the password hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define a function to get user by ID (required by Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))

class QuestionModel(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default = datetime.now)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship(UserModel, backref="questions")

