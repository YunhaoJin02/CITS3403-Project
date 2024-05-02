import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, render_template
from app.extensions import db, migrate
from app.config import Config

from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp




app = Flask(__name__, template_folder='templates')
app.config.from_object(Config) 

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)

from app.models import UserModel

@app.route("/")
def welcome():
    return render_template("welcome_page.html")


if __name__ == '__main__':
    app.run(debug=True)