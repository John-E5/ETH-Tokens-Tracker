import os
from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_toastr import Toastr
from flask_heroku import Heroku
from app.config import Config


heroku = Heroku()
# App config and database init
db = SQLAlchemy()

# Password hashing
bcrypt = Bcrypt()

# Login config
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Json data loading and config
json_data = os.path.join(Config.SITE_ROOT, "static/data", "tokensData.json")
token_data = json.load(open(json_data))


toastr = Toastr()

# Import routes after app has been init


def create_app(config_class=Config):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)
    heroku.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    toastr.init_app(app)

    from app.users.routes import users
    from app.tokens.routes import tokens
    from app.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(tokens)
    app.register_blueprint(main)

    return app
