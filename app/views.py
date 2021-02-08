from flask import render_template
import pandas as pd, app.modules.odds as odds, app.modules.nhl.pace as pace

from app import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/odds/')
def vegas():
    df = odds.return_tm_totals('NHL')
    return render_template('odds.html', tables=[df])

# Under construction
# @app.route('/nhl/', defaults={'leaf': 'dfs', 'leaf': 'lines'})
@app.route('/nhl/')
def nhl_home():
    return render_template('coming-soon.html')


@app.route('/nhl/stats/')
def nhl_stats():
    df = pace.pace()
    return render_template('nhl-stats.html', tables=[df])