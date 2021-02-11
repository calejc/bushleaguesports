import sys, os
from dotenv import load_dotenv
from enum import Enum
# DIR = os.path.expanduser('~/Dropbox/code/python/flask/dfs') 
# load_dotenv(os.path.join(DIR, '.env'))


# Urls for use in all clients




#-------------------------------------------------------#
NHL_BASE = 'nhl.com'
NHL_SHIFTS = '/stats/rest/shiftcharts?cayenneExp=gameId={GAME_ID}'
#-------------------------------------------------------#
# https://gitlab.com/dword4/nhlapi/blob/master/stats-api.md#people
NHL_API_BASE = 'https://statsapi.web.nhl.com/api/v1'
NHL_API_TEAMS = '/teams/{TEAM_ID}'
NHL_API_STATS = '/stats'
NHL_API_STAT_TYPES = '/statTypes'
NHL_API_CONFIG = '/configurations' # Lists all endpoint return options
NHL_API_SCHEDULE = '/schedule'
NHL_API_GAME = '/game/{GAME_ID}'
NHL_API_GAME_LIVE = '/feed/live'
NHL_API_GAME_BOXSCORE = '/boxscore' 
NHL_API_GAME_LINESCORE = '/linescore'
NHL_API_GAME_CONTENT = '/content' # Media => videos, pictures of various plays
NHL_API_TEAM_ROSTER = '/teams?expand=team.roster'
class NHL_API_MODIFIERS(Enum):
    TEAM_ID = 'teamId'
    START_DATE = 'startDate'
    END_DATE = 'endDate'
    SEASON = 'season'
    DATE = 'date'
    GAME_TYPE = 'gameType'
    EXPAND = 'expand'
class NHL_API_EXPAND_VALUES(Enum):
    TEAM_ROSTER = 'team.roster'
#-------------------------------------------------------#
DK_API_BASE = 'https://api.draftkings.com'
DK_DRAFTGROUPS_PATH = '/draftgroups/v1/'
DK_SPORTS = '/sites/US-DK/sports/v1/sports?format=json'
#-------------------------------------------------------#
DK_SPORTSBOOK_BASE = 'https://sportsbook.draftkings.com/api/odds/v1'
DK_SPORTSBOOK_LEAGUES = '/leagues'
#-------------------------------------------------------#
NST_BASE = 'http://www.naturalstattrick.com'
NST_TEAM_TABLE = '/teamtable.php?fromseason=20192020&thruseason=20192020&stype=2&sit={SITUATION}&score={SCORE}&rate=y&team=all&loc={LOCATION}&gpf={GPF}&fd={START_DATE}&td={END_DATE}'
NST_LINE_TOOL = '/linestats.php?fromseason=20192020&thruseason=20192020&stype=2&sit=5v5&score=all&rate=y&team=BOS&vteam=ALL&view=wowy&loc=B&gpfilt=gpteam&fd=2019-10-02&td=2020-04-04&tgp=5&strict=incl&p1={PLAYER_ONE}&p2={PLAYER_TWO}&p3={PLAYER_THREE}&p4={PLAYER_FOUR}&p5={PLAYER_FIVE}'
#-------------------------------------------------------#
LWL_BASE = 'https://leftwinglock.com'
LWL_LOGIN = '/forum/index.php?login/login'
LWL_LINES_BASE = '/line-combinations'
LWL_TEAM_PARAM = '/{TEAM_SLUG}/?team={TEAM_SLUG}&strength={STRENGTH}&gametype={GAMETYPE}'
#-------------------------------------------------------#
ODDS_API_BASE = 'https://api.the-odds-api.com/v3'
ODDS_API_SPORTS = '/sports/?apiKey={API_KEY}&all=1'
ODDS_API_ODDS = '/odds/?apiKey={API_KEY}&sport={SPORT}&region={REGION}&mkt={MARKET}'
#-------------------------------------------------------#
NBA_API_BASE = 'http://data.nba.net'
NBA_TEAMS = '/prod/v2/2019/teams.json'
NBA_ENDPOINTS = '/prod/v2/today.json'
#-------------------------------------------------------#
MLB_API_BASE = 'https://statsapi.mlb.com/api/v1'
MLB_API_TEAMS = '/teams'
#-------------------------------------------------------#



# ---------------- #
#   Misc Helpers   #
# ---------------- #
# Unpack url modifiers to concat onto URL string
def format_query_params(args):
    return '?'+''.join(["{}={}&".format(k,v) for (k,v) in (arg for arg in args)]) if isinstance(args, list) else ''



# --------------------- #
#    Draftkings URLs    #
# --------------------- #
def upcoming_draft_groups_url():
    return '{DK_API_BASE}{DK_DRAFTGROUPS_PATH}'.format(
        DK_API_BASE = DK_API_BASE,
        DK_DRAFTGROUPS_PATH = DK_DRAFTGROUPS_PATH
    )

def draft_group_url(draft_group_id):
    return "{DK_API_BASE}{DK_DRAFTGROUPS_PATH}/{draft_group_id}".format(
        DK_API_BASE = DK_API_BASE,
        DK_DRAFTGROUPS_PATH = DK_DRAFTGROUPS_PATH,
        draft_group_id=draft_group_id
    )

def draftables_url(draft_group_id):
    return "{DK_API_BASE}{DK_DRAFTGROUPS_PATH}draftgroups/{draft_group_id}/draftables".format(
        DK_API_BASE = DK_API_BASE,
        DK_DRAFTGROUPS_PATH = DK_DRAFTGROUPS_PATH,
        draft_group_id=draft_group_id
    )

def dk_sports_url():
    return '{DK_API_BASE}{DK_SPORTS}'.format(
        DK_API_BASE = DK_API_BASE,
        DK_SPORTS = DK_SPORTS
    )


# --------------------------- #
#    NaturalStatTrick URLs    #
# --------------------------- #
def nst_team_url(sit, score, loc, gpf, start_date, end_date):
    url = "{NST_BASE}{NST_TEAM_TABLE}".format(
        NST_BASE = NST_BASE,
        NST_TEAM_TABLE = NST_TEAM_TABLE
    )
    return url.format(
        SITUATION = sit,
        SCORE = score,
        LOCATION = loc,
        GPF = gpf,
        START_DATE = start_date,
        END_DATE = end_date
    )

def nst_line_url(p1, p2, p3, p4, p5):
    url = '{NST_BASE}{NST_LINE_TOOL}'.format(
        NST_BASE = NST_BASE,
        NST_LINE_TOOL = NST_LINE_TOOL
    )
    return url.format(
        PLAYER_ONE = p1,
        PLAYER_TWO = p2,
        PLAYER_THREE = p3,
        PLAYER_FOUR = p4,
        PLAYER_FIVE = p5
    )



# ------------------ #
#    NHL API URLs    #
# ------------------ #
def nhl_schedule_url(**kwargs):
    modifiers = format_query_params(kwargs.get("modifiers", ""))
    base_url = "{NHL_API_BASE}{NHL_API_SCHEDULE}".format(
        NHL_API_BASE = NHL_API_BASE,
        NHL_API_SCHEDULE = NHL_API_SCHEDULE
    )
    return base_url + modifiers

def shiftcharts_url(gameId):
    url = '{NHL_BASE}{NHL_SHIFTS}'.format(
        NHL_BASE = NHL_BASE,
        NHL_SHIFTS = NHL_SHIFTS
    )
    return url.format(
        GAME_ID = gameId
    )

def nhl_teams_url(**kwargs):
    teamId = kwargs.get("teamId", '')
    url = '{NHL_API_BASE}{NHL_API_TEAMS}'.format(
        NHL_API_BASE = NHL_API_BASE,
        NHL_API_TEAMS = NHL_API_TEAMS
    )
    return url.format(
        TEAM_ID = teamId
    )

def nhl_stat_types_url(teamId):
    return '{NHL_API_BASE}{NHL_API_STAT_TYPES}'.format(
        NHL_API_BASE = NHL_API_BASE,
        NHL_API_STAT_TYPES = NHL_API_STAT_TYPES
    )

def nhl_team_stats_url(teamId):
    url = '{NHL_API_BASE}{NHL_API_TEAMS}{NHL_API_STATS}'.format(
        NHL_API_BASE = NHL_API_BASE,
        NHL_API_TEAMS = NHL_API_TEAMS,
        NHL_API_STATS = NHL_API_STATS
    )
    return url.format(
        TEAM_ID = teamId
    )

def rosters_url():
    return '{NHL_API_BASE}{NHL_API_TEAM_ROSTER}'.format(
        NHL_API_BASE = NHL_API_BASE,
        NHL_API_TEAM_ROSTER = NHL_API_TEAM_ROSTER
    )


# ----------------------- #
#    LeftWingLock URLs    #
# ----------------------- #
def lwl_login_url():
    return '{LWL_BASE}{LWL_LOGIN}'.format(
        LWL_BASE = LWL_BASE,
        LWL_LOGIN = LWL_LOGIN
    )


def lwl_lines_url(team_slug, strength, gametype):
    url = '{LWL_BASE}{LWL_LINES_BASE}{LWL_TEAM_PARAM}'.format(
        LWL_BASE = LWL_BASE,
        LWL_LINES_BASE = LWL_LINES_BASE,
        LWL_TEAM_PARAM = LWL_TEAM_PARAM
    )
    return url.format(
        TEAM_SLUG = team_slug,
        STRENGTH = strength,
        GAMETYPE = gametype
    )


# ------------------- #
#    Odds API URLs    #
# ------------------- #
def get_odds_url(sport, region, market):
    url = '{ODDS_API_BASE}{ODDS_API_ODDS}'.format(
        ODDS_API_BASE = ODDS_API_BASE,
        ODDS_API_ODDS = ODDS_API_ODDS
    )
    return url.format(
        API_KEY = os.environ.get('OP_API_KEY'),
        SPORT = sport,
        REGION = region,
        MARKET = market
    )


# ------------------ #
#    NBA API URLs    #
# ------------------ #
def nba_teams_url():
    return '{NBA_API_BASE}{NBA_TEAMS}'.format(
        NBA_API_BASE = NBA_API_BASE,
        NBA_TEAMS = NBA_TEAMS
    )


# ------------------ #
#    MLB API URLs    #
# ------------------ #
def mlb_teams_url():
    return '{MLB_API_BASE}{MLB_API_TEAMS}'.format(
        MLB_API_BASE=MLB_API_BASE,
        MLB_API_TEAMS=MLB_API_TEAMS
    )





##################################################
