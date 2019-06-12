from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SelectField, FloatField
from wtforms.ext.dateutil.fields import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from app import token_data


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, Please choose another.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken, Please choose another.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken, Please choose another.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken, Please choose another.')


class AddTokenForm(FlaskForm):
    tokens = SelectField('Choose Token', validators=[DataRequired()],
                         choices=[(token['symbol'], token['name']) for token in token_data['tokens']])
    token_amount = FloatField('Amount', validators=[DataRequired()])
    token_price = FloatField('Price', validators=[DataRequired()])
    buy_date = DateField('Date', display_format='%Y-%m-%d', validators=[DataRequired()])


class UpdateTokenForm(FlaskForm):
    tokens = StringField('Token')
    token_amount = FloatField('Amount', validators=[DataRequired()])
    token_price = FloatField('Price', validators=[DataRequired()])
    buy_date = DateField('Date', display_format='%Y-%m-%d', validators=[DataRequired()])