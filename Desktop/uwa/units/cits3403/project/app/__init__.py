import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, render_template
from app.extensions import db, migrate, mail
from app.config import Config
from app.models import UserModel



app = Flask(__name__, template_folder='templates')
app.config.from_object(Config) 

db.init_app(app)
mail.init_app(app)
migrate.init_app(app, db)



if __name__ == '__main__':
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True)
