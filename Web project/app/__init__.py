import sys
import os
from flask import Flask, session, g
from app.config import Config
from app.extensions import db, migrate, login_manager
from app.models import UserModel
from flask_login import LoginManager

# Create the Flask app instance
app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)  # Initialize Flask-Login here

# Import routes module to register routes
from app import routes



if __name__ == '__main__':
    # Print all registered routes
    for rule in app.url_map.iter_rules():
        print(rule)
    # Run the app in debug mode
    app.run(debug=True)
