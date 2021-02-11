import requests, os, sys, math, seaborn as sns, pandas as pd
sys.path.append("..")
import datetime as dt, app.utils.data as data


def call_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_error:
        print("Other error occurred:\t{http_error}".format(
            http_error=http_error
        ))
        sys.exit()
    except Exception as error:
        print("Other error occurred:\t{error}".format(
            error=error
        ))
        sys.exit()
    else:
        return response.json()


def style_df(df, **kwargs):
    styles = kwargs.get("styles", data.Styles.DEFAULT)
    cm = sns.light_palette("green", as_cmap=True)
    return df.style.background_gradient(
        cmap=cm,
        axis=0,
        subset=(pd.IndexSlice[2:], df.select_dtypes(float).columns)
    ).set_precision(2).hide_index().set_table_styles(styles).render()

def parse_link(link):
    to_replace = ['=', '%20', '&']
    for item in to_replace:
        link = link.replace("{}".format(item), " ", 1)
    link = link.split()
    name = link[1] + " " + link[2]
    return name


def return_slug(team):
    team = team.replace('.', '')
    team = team.replace(' ', '-')
    return team.lower()

# Must pass in todays_date as a datetime.date object
def return_date(todays_date, days):
    start_date = todays_date - dt.timedelta(days=days)
    return start_date

# Convert decimal odds to traditional american odds
def convert_odds(decimal):
    american_odds = 0
    if decimal >= 2:
        american_odds = (decimal - 1) * 100
    elif decimal <= 2:
        american_odds = (-100)/(decimal - 1)
    return round(american_odds, 0)

# Return implied team totals for moneyline odds
# Using Bill James' Pythagorean Expectation
def team_total(odds, game_total):
    if odds < 0:
        wp = odds/(odds-100)
    elif odds > 0:
        wp = 100/(odds+100)
    else:
        wp = 1
    team_total = game_total / (((math.sqrt(1-wp))*(1 / math.sqrt(wp))) + 1)
    if odds == 0:
        team_total = 0
    return round(team_total, 2)

def spreads_team_total(spread, game_total):
    if spread < 0:
        tm_total = ((game_total - (-1 * spread)) / 2) + (-1 * spread)
    elif spread > 0:
        tm_total = (game_total - spread) / 2
    elif spread == 0:
        tm_total = 0
    return round(tm_total, 2)

def return_alt(d, value, requested_alt):
    for k, v in d.items():
        if isinstance(v, dict):
            p = return_alt(v, value, requested_alt)
            if p:
                return d[k][requested_alt]
        elif v == value:
            return k

def strip_datetime(value):
    tmp = value.replace('T', ' ')[:19]
    return dt.datetime.strptime(tmp, '%Y-%m-%d %H:%M:%S')

def strip_date(date):
    return date.replace('-', '')[2:]

def game_ids(sportId, date, counter):
    y = strip_date(str(date))
    if counter < 10:
        x = '0' + str(counter)
    else:
        x = str(counter)
    id = str(sportId) + y + x
    return id

# Check if a value exists in dict. Using to get home-and-homes
def check_value(data, value):
    tmp = []
    for ele in data.values():
        if isinstance(ele,dict):
            for k, v in ele.items():
                if isinstance(v, dict):
                    for ke, va in v.items():
                        tmp.append(va)
                else:
                    tmp.append(v)
    if value in tmp:
        return True
    else:
        return False

# To find opponent
def check(data, value, team):
    for key in data.values():
        if key['game_id'] == value and key['team'] != team:
            return key['team']

# Returns the next slate by getting the slate ID with "min" time
def return_dgid_from_ts(data, ts):
    for key in data.values():
        if key['start'] == ts:
            return key['id']


# Search dict for certain value,
# Returning the key for that key-value pair
def return_key(data, value):
    for k, v in data.items():
        if v == value:
            return k

# Locate nested keys

def find(key, dictionary):
    for k, v in dictionary.iteritems():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result


# Check if *keys (nested) exists in `element` (dict).
def keys_exists(element, *keys):
    if not isinstance(element, dict):
        raise AttributeError('keys_exists() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError('keys_exists() expects at least two arguments, one given.')

    _element = element
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True
