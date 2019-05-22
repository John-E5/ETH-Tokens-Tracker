from flask import render_template, url_for, redirect, flash, request
from app import app, db, argon2
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required

# Index
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


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
        flash('Your account has been created, You can now login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and argon2.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful, Please check email and password')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return render_template('home.html')


@app.route('/profile_page')
@login_required
def profile_page():
    return render_template('profile_page.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/add_token')
def add_token():
    return render_template('add_token.html')


@app.route('/manage_token')
def manage_token():
    return render_template('manage_token.html')


@app.route('/edit_token')
def edit_token():
    return render_template('edit_token.html')


@app.route('/portfolio_stats')
def portfolio_stats():
    return render_template('portfolio_stats.html')

