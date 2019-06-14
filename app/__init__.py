import os
from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_argon2 import Argon2
from flask_heroku import Heroku
from flask_login import LoginManager


# App config and database init
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
heroku = Heroku(app)


# Password hashing
argon2 = Argon2(app)


# Login config
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# Json data loading and config
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_data = os.path.join(SITE_ROOT, "static/data", "tokensData.json")
token_data = json.load(open(json_data))


# Import routes after app has been init
from app import routes
