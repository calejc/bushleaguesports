from flask import render_template, redirect
import pandas as pd, app.modules.odds as odds
from app.modules.nhl.base_stats import *

from app import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/odds/')
def vegas():
    df = odds.return_tm_totals('NHL')
    return render_template('odds.html', table=df)

# Under construction
@app.route('/nhl/', defaults={'leaf': 'dfs', 'leaf': 'lines', 'leaf': 'splits', 'leaf': 'advanced'})
@app.route('/nhl/<string:leaf>')
def nhl_home(leaf):
    return redirect('/nhl/stats')


@app.route('/nhl/stats/')
def nhl_stats():
    df = season_stats()
    return render_template('nhl-stats.html', table=df)
