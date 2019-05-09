import os
from flask import render_template, url_for, redirect, flash, request
from app import app


# Index
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    return render_template('home.html')


@app.route('/profile_page')
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

