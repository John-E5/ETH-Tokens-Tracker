# Flask Imports
from flask import render_template, url_for, redirect, flash, request, Blueprint
from flask_login import current_user, login_required


# App Imports
from app import db, token_data
from app.tokens.forms import AddTokenForm, UpdateTokenForm
from app.models import UsersTokens

tokens = Blueprint('tokens', __name__)

# Dashboard
@tokens.route('/dashboard')
@login_required
def dashboard():
    page = request.args.get('page', 1, type=int)
    users_token = UsersTokens.query.filter_by(user=current_user).order_by(UsersTokens.buy_date).paginate(page=page, per_page=6)

    return render_template('dashboard.html', users_token=users_token)


# Add new token and commit to database
@tokens.route('/token/new', methods=['GET', 'POST'])
@login_required
def add_token():

    form = AddTokenForm()
    if form.validate_on_submit():
        token = UsersTokens(tokens=form.tokens.data,
                            token_amount=form.token_amount.data,
                            token_price=form.token_price.data,
                            buy_date=form.buy_date.data,
                            user=current_user)
        db.session.add(token)
        db.session.commit()
        flash('Token Added')
        return redirect(url_for('tokens.dashboard'))

    return render_template('add_token.html', form=form, token_data=token_data)


# Token
@tokens.route('/token/<int:id>')
@login_required
def token(id):
    token = UsersTokens.query.get_or_404(id)

    return render_template('token.html', token=token)


# Edit Token
@tokens.route('/edit_token/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_token(id):
    token = UsersTokens.query.get_or_404(id)

    form = UpdateTokenForm()
    if form.validate_on_submit():
        token.token_amount = form.token_amount.data
        token.token_price = form.token_price.data
        token.buy_date = form.buy_date.data
        db.session.commit()
        flash('Token Updated')
        return redirect(url_for('tokens.dashboard', id=token.id))

    elif request.method == 'GET':
        form.tokens.data = token.tokens
        form.token_amount.data = token.token_amount
        form.token_price.data = token.token_price
        form.buy_date.data = token.buy_date

    return render_template('edit_token.html', form=form)


# Delete Token
@tokens.route('/dashboard/<int:id>/delete_token')
@login_required
def delete_token(id):
    token = UsersTokens.query.get_or_404(id)
    db.session.delete(token)
    db.session.commit()
    flash('Token Deleted')

    return redirect(url_for('tokens.dashboard'))

