# Flask Imports
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, current_user, logout_user, login_required


# App Imports
from app import app, db, argon2, token_data
from app.forms import RegistrationForm, LoginForm, UpdateProfileForm, AddTokenForm, UpdateTokenForm
from app.models import User, UsersTokens


# Index
@app.route('/')
@app.route('/home')
def index():
    token_image = [(token['image']) for token in token_data['tokens']]
    return render_template('home.html', token_image=token_image)


# Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = argon2.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and argon2.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful, Please check email and password')

    return render_template('login.html', form=form)


# Logout
@app.route('/logout')
def logout():
    logout_user()

    return render_template('home.html')


# Profile Page
@app.route('/profile_page', methods=['GET', 'POST'])
@login_required
def profile_page():

    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('profile_page'))

    return render_template('profile_page.html', form=form)


# Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    page = request.args.get('page', 1, type=int)
    users_token = UsersTokens.query.order_by(UsersTokens.buy_date).paginate(page=page, per_page=6)

    return render_template('dashboard.html', users_token=users_token)


# Add new token and commit to database
@app.route('/token/new', methods=['GET', 'POST'])
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
        return redirect(url_for('dashboard'))

    return render_template('add_token.html', form=form, token_data=token_data)


# Token
@app.route('/token/<int:id>')
@login_required
def token(id):
    token = UsersTokens.query.get_or_404(id)

    return render_template('token.html', token=token)


# Edit Token
@app.route('/edit_token/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_token(id):
    token = UsersTokens.query.get_or_404(id)

    form = UpdateTokenForm()
    if form.validate_on_submit():
        token.token_amount = form.token_amount.data
        token.token_price = form.token_price.data
        token.buy_date = form.buy_date.data
        db.session.commit()
        return redirect(url_for('dashboard', id=token.id))

    elif request.method == 'GET':
        form.tokens.data = token.tokens
        form.token_amount.data = token.token_amount
        form.token_price.data = token.token_price
        form.buy_date.data = token.buy_date

    return render_template('edit_token.html', form=form)


# Delete Token
@app.route('/dashboard/<int:id>/delete_token')
@login_required
def delete_token(id):
    token = UsersTokens.query.get_or_404(id)
    db.session.delete(token)
    db.session.commit()
    flash('Token Deleted')

    return redirect(url_for('dashboard'))


@app.route('/portfolio_stats')
def portfolio_stats():
    return render_template('portfolio_stats.html')

