# Flask Imports
from flask import render_template, url_for, redirect, flash, Blueprint
from flask_login import login_user, current_user, logout_user, login_required


# App Imports
from app import db, bcrypt
from app.users.forms import RegistrationForm, LoginForm, UpdateProfileForm
from app.models import User

# Set users blueprint
users = Blueprint('users', __name__)


# Registration
@users.route('/register', methods=['GET', 'POST'])
def register():
    """ register route """
    if current_user.is_authenticated:
        return redirect(url_for('tokens.dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created, You can now login!', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


# Login
@users.route('/login', methods=['GET', 'POST'])
def login():
    """ Login route """
    if current_user.is_authenticated:
        return redirect(url_for('tokens.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash('You are now logged in!', 'success')
            return redirect(url_for('tokens.dashboard'))
        else:
            flash('Login Unsuccessful, Please check email and password', 'error')

    return render_template('login.html', form=form)


# Logout
@users.route('/logout')
def logout():
    """ Logout route """
    logout_user()

    return render_template('home.html')


# Profile Page
@users.route('/profile_page', methods=['GET', 'POST'])
@login_required
def profile_page():
    """ Profile page route """
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Profile Updated', 'success')
        return redirect(url_for('users.profile_page'))

    return render_template('profile_page.html', form=form)

