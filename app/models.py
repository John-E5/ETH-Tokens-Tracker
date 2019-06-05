from datetime import date
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_tokens = db.relationship('UsersTokens', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class UsersTokens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tokens = db.Column(db.String(100))
    token_amount = db.Column(db.Float())
    token_price = db.Column(db.Float())
    buy_date = db.Column(db.DateTime, nullable=False, default=date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"UsersTokens('{self.tokens}', '{self.token_amount}', '{self.token_price}', '{self.buy_date}')"
