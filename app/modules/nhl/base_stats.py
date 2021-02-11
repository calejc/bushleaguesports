import pandas as pd, numpy as np, csv, requests, re, sys, operator, app.utils.data as data
from statistics import mean
from app.utils.urls import *
from app.utils.helpers import *



def season_stats(*args):
    teamIds = [return_alt(data.NHL_TEAMS, team,'nhl_id') for team in data.NHL_TEAMS]
    teamUrls = [nhl_team_stats_url(teamId = tid) for tid in teamIds]
    
    stats = []
    for team in teamUrls:
        teamData = ([d['splits'][0] for d in (y for y in call_api(team)['stats']) if d['type']['displayName'] == "statsSingleSeason"])
        teamStats = teamData[0]['stat']
        teamStats['team'] = return_alt(data.NHL_TEAMS, teamData[0]['team']['id'], 'nhl_abbreviation')
        stats.append(teamStats)
    
    df = pd.DataFrame.from_dict(stats)
    df.set_index('team', inplace=True)


    # Remove unwanted data
    keys = ['winScoreFirst', 'winOppScoreFirst', 'winLeadFirstPer', 'winLeadSecondPer', 'winOutshootOpp', 'winOutshotByOpp', 'wins', 'losses', 'ot', 'pts', 'ptPctg', 'faceOffsTaken', 'faceOffsWon', 'faceOffsLost', 'faceOffWinPercentage', 'savePctg', 'evGGARatio']

    df.drop(columns=keys, inplace=True)

    # Add pace and fenwick
    df['fen'] = df['shotsPerGame'] - df['shotsAllowed']
    df['pace'] = df['shotsPerGame'] + df['shotsAllowed']

    renames = {
        'gamesPlayed': 'GP', 
        'goalsPerGame' : 'gf/g', 
        'goalsAgainstPerGame': 'ga/g', 
        'powerPlayPercentage' : 'pp%', 
        'powerPlayGoals' : 'ppGF', 
        'powerPlayGoalsAgainst' : 'ppGA', 
        'powerPlayOpportunities' : 'pp', 
        'penaltyKillPercentage' : 'pk%', 
        'shotsPerGame' : 'sh/g', 
        'shotsAllowed' : 'sa/g', 
        'shootingPctg' : 'sh%'
    }
    df.rename(columns=renames, inplace=True)

    # columns to be of integer type
    int_cols = ['GP', 'pp', 'ppGF', 'ppGA']
    for col in df.columns:
        if col in int_cols:
            df[col] = df[col].astype(int)
        else:
            df[col] = df[col].astype(float).round(2)
    return df
