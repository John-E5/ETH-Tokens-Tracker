from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField
from wtforms.ext.dateutil.fields import DateField
from wtforms.validators import DataRequired, NumberRange
from app import token_data


class AddTokenForm(FlaskForm):
    tokens = SelectField('Choose Token', validators=[DataRequired()],
                         choices=[(token['symbol'], token['name']) for token in token_data['tokens']])
    token_amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    token_price = FloatField('Price', validators=[DataRequired()])
    buy_date = DateField('Date', display_format='%Y-%m-%d', validators=[DataRequired()])


class UpdateTokenForm(FlaskForm):
    tokens = StringField('Token')
    token_amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    token_price = FloatField('Price', validators=[DataRequired()])
    buy_date = DateField('Date', display_format='%Y-%m-%d', validators=[DataRequired()])