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
@app.route('/nhl/', defaults={'leaf': 'dfs', 'leaf': 'stats', 'leaf': 'lines'})
@app.route('/nhl/<string:leaf>')
def nhl_home(leaf):
    return render_template('coming-soon.html')


@app.route('/nhl/stats/')
def nhl_stats():
    return render_template('nhl-stats')
