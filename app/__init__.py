from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_argon2 import Argon2
from flask_login import LoginManager

app = Flask(__name__, template_folder='templates')
app.config['SECERT_KEY'] = '00ef221052a3fbe6fea58db709b5a93b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from app import routes
