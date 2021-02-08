#!/usr/bin/env python3
from bs4 import BeautifulSoup
import pandas as pd, numpy as np, csv, requests, re, seaborn as sns
from statistics import mean

def scrape(list, homeAway, range):
        url = "http://www.naturalstattrick.com/teamtable.php?fromseason=20202021&thruseason=20202021&stype=2&sit=ev&score=all&rate=y&team=all&loc={}&gpf={}&fd=&td=".format(homeAway, range)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        table = soup.find('table', {'id': 'teams'})
        tbody = table.find('tbody')
        for tr in tbody.find_all('tr'):
            team = [td for td in tr.find_all('td')[1]]
            cf60 = [td for td in tr.find_all('td')[10]]
            ca60 = [td for td in tr.find_all('td')[11]]

            new_data = team + cf60 + ca60
            list.append(new_data)
        return list

def pace():
    tmp_home = []
    tmp_away = []


    # Create initial dataframes with cf/ca for h/a splits
    # '410' for full season. '10' for last 10 games
    data_home = pd.DataFrame(scrape(tmp_home, "H", "410"), columns=['team', 'cf/60_h', 'ca/60_h'])
    data_away = pd.DataFrame(scrape(tmp_away, "A", "410"), columns=['team', 'cf/60_a', 'ca/60_a'])

    # Convert rates to numeric objects
    cols_h = ['cf/60_h', 'ca/60_h']
    cols_a = ['cf/60_a', 'ca/60_a']
    for col in cols_h:
        data_home[col] = pd.to_numeric(data_home[col])
    for col in cols_a:
        data_away[col] = pd.to_numeric(data_away[col])

    # Calculate pace
    data_home['pace_h'] = data_home['cf/60_h'] + data_home['ca/60_h']
    data_away['pace_a'] = data_away['cf/60_a'] + data_away['ca/60_a']

    # Merge home and away dataframes into one total dataframe
    df = pd.merge(data_home, data_away, on='team', how='left')


    # Convert pace stat to numeric and calculate the mean of all columns
    cols = ['pace_h', 'pace_a']
    for col in cols:
        df[col] = pd.to_numeric(df[col])

    df_cols = ['cf/60_h', 'cf/60_a', 'ca/60_h', 'ca/60_a', 'pace_h', 'pace_a']
    df.loc['mean'] = df.mean().round(2)
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
    df_final = df.style.background_gradient(
        cmap=cm,
        axis=0,
        subset=(pd.IndexSlice[2:], df.select_dtypes(float).columns)
    ).set_precision(2).hide_index().set_table_styles(styles).render()
    return df_final

    # TODO:
    # Calculate pace over expectation based on opponents
    # xPace(df)
    
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