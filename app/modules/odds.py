#!/usr/bin/env python3
import requests, json, sys, os, sqlite3
sys.path.append('..')
import app.utils.urls as urls, app.utils.helpers as helpers, app.utils.data as data
import pandas as pd, numpy as np, seaborn as sns
import datetime as dt



def return_market(sport_key, region, mkt):
    if region == 'eu':
        sites_list = data.EU_SITES
    elif region == 'us':
        sites_list = data.US_SITES
    elif region == 'uk':
        sites_list = data.UK_SITES
    dd = helpers.return_alt(data.SPORTS, sport_key, 'sport_data')
    url = urls.get_odds_url(sport_key, region, mkt)
    response = requests.get(url)
    if response.status_code is 200:
        data_dict = response.json()
        remaining = response.headers['x-requests-remaining']
        if int(remaining) < 500:
            msg = "|  Beware! only {} calls left for the month!  |".format(remaining)
            border = len(msg) * "="
            print("\n{BORDER}\n{MSG}\n{BORDER}\n".format(
                BORDER = border,
                MSG = msg
            ))
        odds_dict, counter, site_index, game_counter = {}, 1, 0, 0
        upcoming, contains_pinnacle, contains_secondary = True, False, False
        for game in data_dict['data']:
            game_date = dt.datetime.fromtimestamp(game['commence_time']).date()
            gid = int(helpers.game_ids(3, game_date, game_counter)) # create our own IDs here
            h_team = game['home_team']
            for team in game['teams']:
                if team != h_team:
                    a_team = team
                    a_index = game['teams'].index(team)
                else:
                    h_index = game['teams'].index(team)
            for site in game['sites']:
                if 'pinnacle' in site['site_key']:
                    site_idx = game['sites'].index(site)
                    site_n = site['site_key']
                    break
                elif site['site_key'] in sites_list:
                    site_idx = game['sites'].index(site)
                    site_n = site['site_key']
                    break
                else:
                    site_idx = None
            for team in game['teams']:
                if team == h_team:
                    opp = a_team
                elif team == a_team:
                    opp = h_team
                tm_idx = game['teams'].index(team)
                if site_idx is not None:
                    if mkt == 'h2h':
                        odds = helpers.convert_odds(game['sites'][site_idx]['odds'][mkt][tm_idx])
                    elif mkt == 'spreads':
                        odds = game['sites'][site_idx]['odds'][mkt]['points'][tm_idx]
                    elif mkt == 'totals':
                        odds = game['sites'][site_idx]['odds'][mkt]['points'][0]
                elif site_idx == None:
                    odds = 0
                odds_dict[counter] = {
                    'game_id': gid,
                    'team': team,
                    'opp': opp,
                    '{}'.format(mkt): odds
                }
                counter += 1
            game_counter += 1
        df_odds = pd.DataFrame.from_dict(odds_dict, orient='index')
        return df_odds
    else:
        # Return empty dataframe if api call unsuccessful
        return pd.DataFrame

def return_tm_totals(sport, *args):
    tm_totals, counter, arg_df, slate_df, slate_arg = {}, 1, 0, None, True
    sport_key = data.SPORTS[sport]['odds_key']
    default_spreads, default_h2h = ['NBA', 'NFL', 'NCAAB', 'NCAAF'], ['NHL', 'MLB']
    markets, regions = ['h2h', 'spreads'], ['us', 'eu', 'uk']
    region = 'eu' # Set Default
    if sport in default_h2h:
        mkt = 'h2h' # Set Default
    elif sport in default_spreads:
        mkt = 'spreads' # Set Default
    for arg in args:
        if isinstance(arg, pd.DataFrame):
            slate_df = arg
        elif arg in regions:
            region = arg
        elif arg in markets:
            mkt = arg
    if slate_df is None:
        slate_arg = False
        slate_df = pd.DataFrame()
    df = pd.merge(
        return_market(sport_key, region, mkt),
        return_market(sport_key, region, 'totals'),
        on = ['game_id', 'team', 'opp']
    )
    if slate_arg:
        df = slate_df.merge(df, how='left', on=['team', 'opp'])
    else:
        df = df[(df != 0).all(1)]
    for index, row in df.iterrows():
        if sport_key == 'americanfootball_nfl' or sport_key == 'basketball_nba' or sport_key == 'basketball_ncaab' or sport_key == 'americanfootball_ncaaf':
            t = helpers.spreads_team_total(float(row['spreads']), float(row['totals']))
        else:
            t = helpers.team_total(float(row['h2h']), float(row['totals']))

        tm_totals[counter] = {
            'team': row['team'],
            'tm_total': t
        }
        counter += 1
    tm_totals = pd.DataFrame.from_dict(tm_totals, orient='index')
    df_odds = df.merge(tm_totals, how='left', on=['team'])
    df_odds = df_odds[['game_id', 'team', 'opp', mkt, 'totals', 'tm_total']]
    df_odds = df_odds.sort_values(by=['game_id'])


    styles = [
        dict(
            selector="tr:hover",
            props=[("background-color", "#d9d9d9")]
        ),
        dict(
            selector="th",
            props=[
                ("text-align", "center"),
                ("margin-left", "10px")
            ]
        ),
    ]

    cm = sns.light_palette("green", as_cmap=True)
    df_final = df_odds.style.background_gradient(
        cmap=cm,
        axis=0,
        subset=(pd.IndexSlice[2:], df_odds.select_dtypes(float).columns)
    ).set_precision(2).hide_index().hide_columns(['game_id']).set_table_styles(styles).render()

    return df_final




# Used for testing. Read a csv file into dataframe instead of continuing to make API calls
def testing():

    styles = [
        dict(
            selector="tr:hover",
            props=[("background-color", "#d9d9d9")]
        ),
        dict(
            selector="th",
            props=[
                ("text-align", "center"),
                ("margin-left", "10px")
            ]
        ),
    ]

    df_initial = pd.read_csv("dataframe.csv")
    cm = sns.light_palette("green", as_cmap=True)
    df = df_initial.style.background_gradient(
        cmap=cm,
        axis=0,
        subset=(pd.IndexSlice[2:], df_initial.select_dtypes(float).columns)
    ).set_precision(2).hide_index().hide_columns(['game_id']).set_table_styles(styles).render()
    return df