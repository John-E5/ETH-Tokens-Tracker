from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_argon2 import Argon2
from flask_login import LoginManager

app = Flask(__name__)

