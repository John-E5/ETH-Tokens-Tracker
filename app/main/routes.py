# Flask Imports
from flask import render_template, Blueprint
from flask_login import current_user, login_required


# App Imports
from app import db, token_data
from app.models import UsersTokens

# Pygal
import pygal
from pygal.style import DarkGreenBlueStyle

main = Blueprint('main', __name__)


# Index
@main.route('/')
@main.route('/home')
def index():
    token_image = [(token['image']) for token in token_data['tokens']]
    return render_template('home.html', token_image=token_image)


@main.route('/portfolio_stats')
@login_required
def portfolio_stats():

    # Load data
    user_token = dict(db.session.query(UsersTokens.tokens, UsersTokens.token_amount).filter_by(user=current_user).all())

    # Piechart
    pie_graph = pygal.Pie(width=500, height=500, style=DarkGreenBlueStyle)
    for name, amount in user_token.items():
        pie_graph.add(name, amount)
    pie_graph = pie_graph.render_data_uri()

    # Barchart
    bar_graph = pygal.Bar(width=500, height=500, style=DarkGreenBlueStyle)
    for name, amount in user_token.items():
        bar_graph.add(name, amount)
    bar_graph = bar_graph.render_data_uri()

    # Treemap
    tree_map = pygal.Treemap(width=900, height=400, style=DarkGreenBlueStyle)
    for name, amount in user_token.items():
        tree_map.add(name, amount)
    tree_map = tree_map.render_data_uri()

    return render_template('portfolio_stats.html', pie_graph=pie_graph, bar_graph=bar_graph, tree_map=tree_map)

