import pandas as pd, numpy as np, csv, requests, re, seaborn as sns, sys, operator, app.utils.data as data
from statistics import mean
from app.utils.urls import *
from app.utils.helpers import *



##########
## TODO ##
##########

# Pace projections are under construction


def games_subset(json_data, n):
    # Get Regular Season ("R" gametype) games that are "Final"
    # Return just game ID to then make a call to the game endpoint
    # Sorted by most recent, splicing 'n' games
    return sorted([x['games'][0]['gamePk'] for x in (y for y in json_data['dates']) if x['games'][0]['status']['abstractGameState'] == "Final" and x['games'][0]['gameType'] == "R"])[-n:]


def pace():
    pass
    
def xPace(df):

    df['h_opp_pace'] = np.nan
    df['a_opp_pace'] = np.nan
    df['team'] = df['team'].fillna('mean')
    print(df)
    for team in df['team']:
        print(team)
        continue
        if team != 'mean':
            x_away = []
            x_home = []
            tmp_a = []
            tmp_h = []
            for x in x_away:
                tmp_a.append(df.loc[df['team'] == x, 'pace_a'].item())
            for x in x_home:
                tmp_h.append(df.loc[df['team'] == x, 'pace_h'].item())
            ix = df.index[df['team'] == team]

            df.loc[df['team'] == team, 'a_opp_pace'] = mean(tmp_a)
            df.loc[df['team'] == team, 'h_opp_pace'] = mean(tmp_h)


    df.a_opp_pace = df.a_opp_pace.round(2)
    df.h_opp_pace = df.h_opp_pace.round(2)
    df = df[['team', 'cf/60_h', 'cf/60_a', 'ca/60_h', 'ca/60_a', 'pace_h', 'h_opp_pace', 'pace_a', 'a_opp_pace']]
    return df
