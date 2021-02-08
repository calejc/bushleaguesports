from enum import Enum

# Data


# ---------------------------------- #
#    NaturalStatTrick data classes   #
# ---------------------------------- #
class nst_sit(Enum):
    ALL_STRENGTHS = 'all'
    EVEN_STRENGTH = 'ev'
    FULL_STRENGTH = '5v5'
    FULL_ADJUSTED = 'sva' # Score and venue adjusted
    POWERPLAY = 'pp'
    FIVE_ON_FOUR_PP = '5v4'
    PENALTYKILL = 'pk'
    FOUR_ON_FIVE_PK = '4v5'
    WITH_EMPTY_NET = 'enf'
    AGAINST_EMPTY_NET = 'ena'

class nst_score(Enum):
    ALL_SCORES = 'all'
    TIED = 'tied'
    LEADING = 'u'
    TRAILING = 'd'
    WITHIN_ONE = 'w1'
    UP_ONE = 'u1'
    DOWN_ONE = 'd1'

class nst_rate(Enum):
    RATES = 'y'
    COUNTS = 'n'

class nst_loc(Enum):
    HOME_AND_AWAY = 'B'
    HOME = 'H'
    AWAY = 'A'

class nst_gpf(Enum):
    FULL_SEASON = '410'
    LAST_TEN = '10'



# ------------------------------- #
#    LeftWingLock data classes    #
# ------------------------------- #
class lwl_strengths(Enum):
    EV = 'EV'
    PP = 'PP'
    PK = 'SH'

class lwl_gametypes(Enum):
    GAMEDAY = 'GD'
    MOST_RECENT = '1'
    LAST_3 = '3'


# -------------------------------- #
#    DraftkingsAPI data classes    #
# -------------------------------- #
CLASSIC_IDS = (1, 72, 122, 98, 70, 94, 125, 21)
SHOWDOWN_IDS = []



# -------------------------- #
#    NHL_API data classes    #
# -------------------------- #




# ---------------- #
#    Odds sites    #
# ---------------- #
US_SITES = ('pointsbetus', 'betonlineag', 'bookmaker', 'mybookieag', 'intertops', 'betfair', 'lowvig')
UK_SITES = ('mybookieag', 'betfair', 'willhill', 'paddypower')
EU_SITES = ('betonlineag', 'bookmaker', 'mybookieag', 'intertops', 'betfair', 'pinnacle')


# ---------------------------------------- #
#    All Team Ids, Names, Abbreviations    #
# ---------------------------------------- #

# --------- #
#    NHL    #
# --------- #
NHL_TEAMS = {
    'NJD': {
     'dk_abbreviation': 'NJ',
     'dk_team_id': 4964,
     'nhl_id': 1,
     'name': 'New Jersey Devils',
     'secondary_name': 'New Jersey Devils',
     'slug': 'new-jersey-devils',
     'nhl_abbreviation': 'NJD',
     'nst_abbreviation': 'N.J',
    },
    'NYI': {
     'dk_abbreviation': 'NYI',
     'dk_team_id': 4965,
     'nhl_id': 2,
     'name': 'New York Islanders',
     'secondary_name': 'New York Islanders',
     'slug': 'new-york-islanders',
     'nhl_abbreviation': 'NYI',
     'nst_abbreviation': 'NYI',
    },
    'NYR': {
     'dk_abbreviation': 'NYR',
     'dk_team_id': 4966,
     'nhl_id': 3,
     'name': 'New York Rangers',
     'secondary_name': 'New York Rangers',
     'slug': 'new-york-rangers',
     'nhl_abbreviation': 'NYR',
     'nst_abbreviation': 'NYR',
    },
    'PHI': {
     'dk_abbreviation': 'PHI',
     'dk_team_id': 4968,
     'nhl_id': 4,
     'name': 'Philadelphia Flyers',
     'secondary_name': 'Philadelphia Flyers',
     'slug': 'philadelphia-flyers',
     'nhl_abbreviation': 'PHI',
     'nst_abbreviation': 'PHI',
    },
    'PIT': {
     'dk_abbreviation': 'PIT',
     'dk_team_id': 4969,
     'nhl_id': 5,
     'name': 'Pittsburgh Penguins',
     'secondary_name': 'Pittsburgh Penguins',
     'slug': 'pittsburgh-penguins',
     'nhl_abbreviation': 'PIT',
     'nst_abbreviation': 'PIT',
    },
    'BOS': {
     'dk_abbreviation': 'BOS',
     'dk_team_id': 4954,
     'nhl_id': 6,
     'name': 'Boston Bruins',
     'secondary_name': 'Boston Bruins',
     'slug': 'boston-bruins',
     'nhl_abbreviation': 'BOS',
     'nst_abbreviation': 'BOS',
    },
    'BUF': {
     'dk_abbreviation': 'BUF',
     'dk_team_id': 4955,
     'nhl_id': 7,
     'name': 'Buffalo Sabres',
     'secondary_name': 'Buffalo Sabres',
     'slug': 'buffalo-sabres',
     'nhl_abbreviation': 'BUF',
     'nst_abbreviation': 'BUF',
    },
    'MTL': {
     'dk_abbreviation': 'MON',
     'dk_team_id': 4963,
     'nhl_id': 8,
     'name': 'Montréal Canadiens',
     'secondary_name': 'Montreal Canadiens',
     'slug': 'montreal-canadiens',
     'nhl_abbreviation': 'MTL',
     'nst_abbreviation': 'MTL',
    },
    'OTT': {
     'dk_abbreviation': 'OTT',
     'dk_team_id': 4967,
     'nhl_id': 9,
     'name': 'Ottawa Senators',
     'secondary_name': 'Ottawa Senators',
     'slug': 'ottawa-senators',
     'nhl_abbreviation': 'OTT',
     'nst_abbreviation': 'OTT',
    },
    'TOR': {
     'dk_abbreviation': 'TOR',
     'dk_team_id': 4974,
     'nhl_id': 10,
     'name': 'Toronto Maple Leafs',
     'secondary_name': 'Toronto Maple Leafs',
     'slug': 'toronto-maple-leafs',
     'nhl_abbreviation': 'TOR',
     'nst_abbreviation': 'TOR',
    },
    'CAR': {
     'dk_abbreviation': 'CAR',
     'dk_team_id': 4960,
     'nhl_id': 12,
     'name': 'Carolina Hurricanes',
     'secondary_name': 'Carolina Hurricanes',
     'slug': 'carolina-hurricanes',
     'nhl_abbreviation': 'CAR',
     'nst_abbreviation': 'CAR',
    },
    'FLA': {
     'dk_abbreviation': 'FLA',
     'dk_team_id': 4979,
     'nhl_id': 13,
     'name': 'Florida Panthers',
     'secondary_name': 'Florida Panthers',
     'slug': 'florida-panthers',
     'nhl_abbreviation': 'FLA',
     'nst_abbreviation': 'FLA',
    },
    'TBL': {
     'dk_abbreviation': 'TB',
     'dk_team_id': 4973,
     'nhl_id': 14,
     'name': 'Tampa Bay Lightning',
     'secondary_name': 'Tampa Bay Lightning',
     'slug': 'tampa-bay-lightning',
     'nhl_abbreviation': 'TBL',
     'nst_abbreviation': 'T.B',
    },
    'WSH': {
     'dk_abbreviation': 'WAS',
     'dk_team_id': 4976,
     'nhl_id': 15,
     'name': 'Washington Capitals',
     'secondary_name': 'Washington Capitals',
     'slug': 'washington-capitals',
     'nhl_abbreviation': 'WSH',
     'nst_abbreviation': 'WSH',
    },
    'CHI': {
     'dk_abbreviation': 'CHI',
     'dk_team_id': 4957,
     'nhl_id': 16,
     'name': 'Chicago Blackhawks',
     'secondary_name': 'Chicago Blackhawks',
     'slug': 'chicago-blackhawks',
     'nhl_abbreviation': 'CHI',
     'nst_abbreviation': 'CHI',
    },
    'DET': {
     'dk_abbreviation': 'DET',
     'dk_team_id': 4958,
     'nhl_id': 17,
     'name': 'Detroit Red Wings',
     'secondary_name': 'Detroit Red Wings',
     'slug': 'detroit-red-wings',
     'nhl_abbreviation': 'DET',
     'nst_abbreviation': 'DET',
    },
    'NSH': {
     'dk_abbreviation': 'NSH',
     'dk_team_id': 4980,
     'nhl_id': 18,
     'name': 'Nashville Predators',
     'secondary_name': 'Nashville Predators',
     'slug': 'nashville-predators',
     'nhl_abbreviation': 'NSH',
     'nst_abbreviation': 'NSH',
    },
    'STL': {
     'dk_abbreviation': 'STL',
     'dk_team_id': 4972,
     'nhl_id': 19,
     'name': 'St. Louis Blues',
     'secondary_name': 'St Louis Blues',
     'slug': 'st-louis-blues',
     'nhl_abbreviation': 'STL',
     'nst_abbreviation': 'STL',
    },
    'CGY': {
     'dk_abbreviation': 'CGY',
     'dk_team_id': 4956,
     'nhl_id': 20,
     'name': 'Calgary Flames',
     'secondary_name': 'Calgary Flames',
     'slug': 'calgary-flames',
     'nhl_abbreviation': 'CGY',
     'nst_abbreviation': 'CGY',
    },
    'COL': {
     'dk_abbreviation': 'COL',
     'dk_team_id': 4970,
     'nhl_id': 21,
     'name': 'Colorado Avalanche',
     'secondary_name': 'Colorado Avalanche',
     'slug': 'colorado-avalanche',
     'nhl_abbreviation': 'COL',
     'nst_abbreviation': 'COL',
    },
    'EDM': {
     'dk_abbreviation': 'EDM',
     'dk_team_id': 4959,
     'nhl_id': 22,
     'name': 'Edmonton Oilers',
     'secondary_name': 'Edmonton Oilers',
     'slug': 'edmonton-oilers',
     'nhl_abbreviation': 'EDM',
     'nst_abbreviation': 'EDM',
    },
    'VAN': {
     'dk_abbreviation': 'VAN',
     'dk_team_id': 4975,
     'nhl_id': 23,
     'name': 'Vancouver Canucks',
     'secondary_name': 'Vancouver Canucks',
     'slug': 'vancouver-canucks',
     'nhl_abbreviation': 'VAN',
     'nst_abbreviation': 'VAN',
    },
    'ANA': {
     'dk_abbreviation': 'ANH',
     'dk_team_id': 4978,
     'nhl_id': 24,
     'name': 'Anaheim Ducks',
     'secondary_name': 'Anaheim Ducks',
     'slug': 'anaheim-ducks',
     'nhl_abbreviation': 'ANA',
     'nst_abbreviation': 'ANA',
    },
    'DAL': {
     'dk_abbreviation': 'DAL',
     'dk_team_id': 4962,
     'nhl_id': 25,
     'name': 'Dallas Stars',
     'secondary_name': 'Dallas Stars',
     'slug': 'dallas-stars',
     'nhl_abbreviation': 'DAL',
     'nst_abbreviation': 'DAL',
    },
    'LAK': {
     'dk_abbreviation': 'LA',
     'dk_team_id': 4961,
     'nhl_id': 26,
     'name': 'Los Angeles Kings',
     'secondary_name': 'Los Angeles Kings',
     'slug': 'los-angeles-kings',
     'nhl_abbreviation': 'LAK',
     'nst_abbreviation': 'L.A',
    },
    'SJS': {
     'dk_abbreviation': 'SJ',
     'dk_team_id': 4971,
     'nhl_id': 28,
     'name': 'San Jose Sharks',
     'secondary_name': 'San Jose Sharks',
     'slug': 'san-jose-sharks',
     'nhl_abbreviation': 'SJS',
     'nst_abbreviation': 'S.J',
    },
    'CBJ': {
     'dk_abbreviation': 'CLS',
     'dk_team_id': 4982,
     'nhl_id': 29,
     'name': 'Columbus Blue Jackets',
     'secondary_name': 'Columbus Blue Jackets',
     'slug': 'columbus-blue-jackets',
     'nhl_abbreviation': 'CBJ',
     'nst_abbreviation': 'CBJ',
    },
    'MIN': {
     'dk_abbreviation': 'MIN',
     'dk_team_id': 4983,
     'nhl_id': 30,
     'name': 'Minnesota Wild',
     'secondary_name': 'Minnesota Wild',
     'slug': 'minnesota-wild',
     'nhl_abbreviation': 'MIN',
     'nst_abbreviation': 'MIN',
    },
    'WPG': {
     'dk_abbreviation': 'WPG',
     'dk_team_id': 4981,
     'nhl_id': 52,
     'name': 'Winnipeg Jets',
     'secondary_name': 'Winnipeg Jets',
     'slug': 'winnipeg-jets',
     'nhl_abbreviation': 'WPG',
     'nst_abbreviation': 'WPG',
    },
    'ARI': {
     'dk_abbreviation': 'ARI',
     'dk_team_id': 4977,
     'nhl_id': 53,
     'name': 'Arizona Coyotes',
     'secondary_name': 'Arizona Coyotes',
     'slug': 'arizona-coyotes',
     'nhl_abbreviation': 'ARI',
     'nst_abbreviation': 'ARI',
    },
    'VGK': {
     'dk_abbreviation': 'VGK',
     'dk_team_id': 58462,
     'nhl_id': 54,
     'name': 'Vegas Golden Knights',
     'secondary_name': 'Vegas Golden Knights',
     'slug': 'vegas-golden-knights',
     'nhl_abbreviation': 'VGK',
     'nst_abbreviation': 'VGK',
    }
}

# ------------------------------- #
# ------------------------------- #

# --------- #
#    NBA    #
# --------- #
NBA_TEAMS = {
  'ATL': {
    'tricode': 'ATL',
    'urlName': 'hawks',
    'teamShortName': 'Atlanta',
    'abbreviation': 'ATL',
    'dk_abbreviation': 'ATL',
    'name': 'Atlanta Hawks',
    'secondary_name': 'Atlanta Hawks',
    'nba_id': '1610612737',
    'dk_team_id': 0
  },
  'BOS': {
    'tricode': 'BOS',
    'urlName': 'celtics',
    'teamShortName': 'Boston',
    'abbreviation': 'BOS',
    'dk_abbreviation': 'BOS',
    'name': 'Boston Celtics',
    'secondary_name': 'Boston Celtics',
    'nba_id': '1610612738',
    'dk_team_id': 0
  },
  'BKN': {
    'tricode': 'BKN',
    'urlName': 'nets',
    'teamShortName': 'Brooklyn',
    'abbreviation': 'BKN',
    'dk_abbreviation': 'BKN',
    'name': 'Brooklyn Nets',
    'secondary_name': 'Brooklyn Nets',
    'nba_id': '1610612751',
    'dk_team_id': 0
  },
  'CHA': {
    'tricode': 'CHA',
    'urlName': 'hornets',
    'teamShortName': 'Charlotte',
    'abbreviation': 'CHA',
    'dk_abbreviation': 'CHA',
    'name': 'Charlotte Hornets',
    'secondary_name': 'Charlotte Hornets',
    'nba_id': '1610612766',
    'dk_team_id': 0
  },
  'CHI': {
    'tricode': 'CHI',
    'urlName': 'bulls',
    'teamShortName': 'Chicago',
    'abbreviation': 'CHI',
    'dk_abbreviation': 'CHI',
    'name': 'Chicago Bulls',
    'secondary_name': 'Chicago Bulls',
    'nba_id': '1610612741',
    'dk_team_id': 0
  },
  'CLE': {
    'tricode': 'CLE',
    'urlName': 'cavaliers',
    'teamShortName': 'Cleveland',
    'abbreviation': 'CLE',
    'dk_abbreviation': 'CLE',
    'name': 'Cleveland Cavaliers',
    'secondary_name': 'Cleveland Cavaliers',
    'nba_id': '1610612739',
    'dk_team_id': 0
  },
  'DAL': {
    'tricode': 'DAL',
    'urlName': 'mavericks',
    'teamShortName': 'Dallas',
    'abbreviation': 'DAL',
    'dk_abbreviation': 'DAL',
    'name': 'Dallas Mavericks',
    'secondary_name': 'Dallas Mavericks',
    'nba_id': '1610612742',
    'dk_team_id': 0
  },
  'DEN': {
    'tricode': 'DEN',
    'urlName': 'nuggets',
    'teamShortName': 'Denver',
    'abbreviation': 'DEN',
    'dk_abbreviation': 'DEN',
    'name': 'Denver Nuggets',
    'secondary_name': 'Denver Nuggets',
    'nba_id': '1610612743',
    'dk_team_id': 0
  },
  'DET': {
    'tricode': 'DET',
    'urlName': 'pistons',
    'teamShortName': 'Detroit',
    'abbreviation': 'DET',
    'dk_abbreviation': 'DET',
    'name': 'Detroit Pistons',
    'secondary_name': 'Detroit Pistons',
    'nba_id': '1610612765',
    'dk_team_id': 0
  },
  'GSW': {
    'tricode': 'GSW',
    'urlName': 'warriors',
    'teamShortName': 'Golden State',
    'abbreviation': 'GSW',
    'dk_abbreviation': 'GS',
    'name': 'Golden State Warriors',
    'secondary_name': 'Golden State Warriors',
    'nba_id': '1610612744',
    'dk_team_id': 0
  },
  'HOU': {
    'tricode': 'HOU',
    'urlName': 'rockets',
    'teamShortName': 'Houston',
    'abbreviation': 'HOU',
    'dk_abbreviation': 'HOU',
    'name': 'Houston Rockets',
    'secondary_name': 'Houston Rockets',
    'nba_id': '1610612745',
    'dk_team_id': 0
  },
  'IND': {
    'tricode': 'IND',
    'urlName': 'pacers',
    'teamShortName': 'Indiana',
    'abbreviation': 'IND',
    'dk_abbreviation': 'IND',
    'name': 'Indiana Pacers',
    'secondary_name': 'Indiana Pacers',
    'nba_id': '1610612754',
    'dk_team_id': 0
  },
  'LAC': {
    'tricode': 'LAC',
    'urlName': 'clippers',
    'teamShortName': 'LA Clippers',
    'abbreviation': 'LAC',
    'dk_abbreviation': 'LAC',
    'name': 'LA Clippers',
    'secondary_name': 'Los Angeles Clippers',
    'nba_id': '1610612746',
    'dk_team_id': 0
  },
  'LAL': {
    'tricode': 'LAL',
    'urlName': 'lakers',
    'teamShortName': 'L.A. Lakers',
    'abbreviation': 'LAL',
    'dk_abbreviation': 'LAL',
    'name': 'Los Angeles Lakers',
    'secondary_name': 'Los Angeles Lakers',
    'nba_id': '1610612747',
    'dk_team_id': 0
  },
  'MEM': {
    'tricode': 'MEM',
    'urlName': 'grizzlies',
    'teamShortName': 'Memphis',
    'abbreviation': 'MEM',
    'dk_abbreviation': 'MEM',
    'name': 'Memphis Grizzlies',
    'secondary_name': 'Memphis Grizzlies',
    'nba_id': '1610612763',
    'dk_team_id': 0
  },
  'MIA': {
    'tricode': 'MIA',
    'urlName': 'heat',
    'teamShortName': 'Miami',
    'abbreviation': 'MIA',
    'dk_abbreviation': 'MIA',
    'name': 'Miami Heat',
    'secondary_name': 'Miami Heat',
    'nba_id': '1610612748',
    'dk_team_id': 0
  },
  'MIL': {
    'tricode': 'MIL',
    'urlName': 'bucks',
    'teamShortName': 'Milwaukee',
    'abbreviation': 'MIL',
    'dk_abbreviation': 'MIL',
    'name': 'Milwaukee Bucks',
    'secondary_name': 'Milwaukee Bucks',
    'nba_id': '1610612749',
    'dk_team_id': 0
  },
  'MIN': {
    'tricode': 'MIN',
    'urlName': 'timberwolves',
    'teamShortName': 'Minnesota',
    'abbreviation': 'MIN',
    'dk_abbreviation': 'MIN',
    'name': 'Minnesota Timberwolves',
    'secondary_name': 'Minnesota Timberwolves',
    'nba_id': '1610612750',
    'dk_team_id': 0
  },
  'NOP': {
    'tricode': 'NOP',
    'urlName': 'pelicans',
    'teamShortName': 'New Orleans',
    'abbreviation': 'NOP',
    'dk_abbreviation': 'NOP',
    'name': 'New Orleans Pelicans',
    'secondary_name': 'New Orleans Pelicans',
    'nba_id': '1610612740',
    'dk_team_id': 0
  },
  'NYK': {
    'tricode': 'NYK',
    'urlName': 'knicks',
    'teamShortName': 'New York',
    'abbreviation': 'NYK',
    'dk_abbreviation': 'NYK',
    'name': 'New York Knicks',
    'secondary_name': 'New York Knicks',
    'nba_id': '1610612752',
    'dk_team_id': 0
  },
  'OKC': {
    'tricode': 'OKC',
    'urlName': 'thunder',
    'teamShortName': 'Oklahoma City',
    'abbreviation': 'OKC',
    'dk_abbreviation': 'OKC',
    'name': 'Oklahoma City Thunder',
    'secondary_name': 'Oklahoma City Thunder',
    'nba_id': '1610612760',
    'dk_team_id': 0
  },
  'ORL': {
    'tricode': 'ORL',
    'urlName': 'magic',
    'teamShortName': 'Orlando',
    'abbreviation': 'ORL',
    'dk_abbreviation': 'ORL',
    'name': 'Orlando Magic',
    'secondary_name': 'Orlando Magic',
    'nba_id': '1610612753',
    'dk_team_id': 0
  },
  'PHI': {
    'tricode': 'PHI',
    'urlName': 'sixers',
    'teamShortName': 'Philadelphia',
    'abbreviation': 'PHI',
    'dk_abbreviation': 'PHI',
    'name': 'Philadelphia 76ers',
    'secondary_name': 'Philadelphia 76ers',
    'nba_id': '1610612755',
    'dk_team_id': 0
  },
  'PHX': {
    'tricode': 'PHX',
    'urlName': 'suns',
    'teamShortName': 'Phoenix',
    'abbreviation': 'PHX',
    'dk_abbreviation': 'PHO',
    'name': 'Phoenix Suns',
    'secondary_name': 'Phoenix Suns',
    'nba_id': '1610612756',
    'dk_team_id': 0
  },
  'POR': {
    'tricode': 'POR',
    'urlName': 'blazers',
    'teamShortName': 'Portland',
    'abbreviation': 'POR',
    'dk_abbreviation': 'POR',
    'name': 'Portland Trail Blazers',
    'secondary_name': 'Portland Trail Blazers',
    'nba_id': '1610612757',
    'dk_team_id': 0
  },
  'SAC': {
    'tricode': 'SAC',
    'urlName': 'kings',
    'teamShortName': 'Sacramento',
    'abbreviation': 'SAC',
    'dk_abbreviation': 'SAC',
    'name': 'Sacramento Kings',
    'secondary_name': 'Sacramento Kings',
    'nba_id': '1610612758',
    'dk_team_id': 0
  },
  'SAS': {
    'tricode': 'SAS',
    'urlName': 'spurs',
    'teamShortName': 'San Antonio',
    'abbreviation': 'SAS',
    'dk_abbreviation': 'SA',
    'name': 'San Antonio Spurs',
    'secondary_name': 'San Antonio Spurs',
    'nba_id': '1610612759',
    'dk_team_id': 0
  },
  'TOR': {
    'tricode': 'TOR',
    'urlName': 'raptors',
    'teamShortName': 'Toronto',
    'abbreviation': 'TOR',
    'dk_abbreviation': 'TOR',
    'name': 'Toronto Raptors',
    'secondary_name': 'Toronto Raptors',
    'nba_id': '1610612761',
    'dk_team_id': 0
  },
  'UTA': {
    'tricode': 'UTA',
    'urlName': 'jazz',
    'teamShortName': 'Utah',
    'abbreviation': 'UTA',
    'dk_abbreviation': 'UTA',
    'name': 'Utah Jazz',
    'secondary_name': 'Utah Jazz',
    'nba_id': '1610612762',
    'dk_team_id': 0
  },
  'WAS': {
    'tricode': 'WAS',
    'urlName': 'wizards',
    'teamShortName': 'Washington',
    'abbreviation': 'WAS',
    'dk_abbreviation': 'WAS',
    'name': 'Washington Wizards',
    'secondary_name': 'Washington Wizards',
    'nba_id': '1610612764',
    'dk_team_id': 0
  }
}


# --------- #
#    MLB    #
# --------- #
MLB_TEAMS = {

}



# --------- #
#    NFL    #
# --------- #
NFL_TEAMS = {
  'TEN': {
        'nfl': 'TEN',
        'dk': 'TEN',
        'dk_id': 336,
        'nfl_team_id': 2100,
        'pfr': 'OTI',
        'pff': 31,
        'pfflabel': 'TEN',
        'fo': 'TEN',
        'full': 'Tennessee Titans',
        'location': 'Tennessee',
        'short_location': 'Tennessee',
        'nickname': 'Titans',
        'slug': 'tennessee-titans'
  },
  'IND': {
          'nfl': 'IND',
          'dk': 'IND',
          'dk_id': 338,
          'nfl_team_id': 2200,
          'pfr': 'CLT',
          'pff': 14,
          'pfflabel': 'IND',
          'fo': 'IND',
          'full': 'Indianapolis Colts',
          'location': 'Indianapolis',
          'short_location': 'Indianapolis',
          'nickname': 'Colts',
          'slug': 'indianapolis-colts'
  },
  'ARI': {
          'nfl': 'ARI',
          'dk': 'ARI',
          'dk_id': 355,
          'nfl_team_id': 3800,
          'pfr': 'CRD',
          'pff': 1,
          'pfflabel': 'ARZ',
          'fo': 'ARI',
          'full': 'Arizona Cardinals',
          'location': 'Arizona',
          'short_location': 'Arizona',
          'nickname': 'Cardinals',
          'slug': 'arizona-cardinals'
  },
  'NE': {
          'nfl': 'NE',
          'dk': 'NE',
          'dk_id': 348,
          'nfl_team_id': 3200,
          'pfr': 'NWE',
          'pff': 19,
          'pfflabel': 'NE',
          'fo': 'NE',
          'full': 'New England Patriots',
          'location': 'New England',
          'short_location': 'New England',
          'nickname': 'Patriots',
          'slug': 'new-england-patriots'
  },
  'CLE': {
          'nfl': 'CLE',
          'dk': 'CLE',
          'dk_id': 329,
          'nfl_team_id': 1050,
          'pfr': 'CLE',
          'pff': 8,
          'pfflabel': 'CLV',
          'fo': 'CLE',
          'full': 'Cleveland Browns',
          'location': 'Cleveland',
          'short_location': 'Cleveland',
          'nickname': 'Browns',
          'slug': 'cleveland-browns'
  },
  'JAX': {
          'nfl': 'JAC',
          'dk': 'JAX',
          'dk_id': 365,
          'nfl_team_id': 2250,
          'pfr': 'JAX',
          'pff': 15,
          'pfflabel': 'JAX',
          'fo': 'JAX',
          'full': 'Jacksonville Jaguars',
          'location': 'Jacksonville',
          'short_location': 'Jacksonville',
          'nickname': 'Jaguars',
          'slug': 'jacksonville-jaguars'
  },
  'MIA': {
          'nfl': 'MIA',
          'dk': 'MIA',
          'dk_id': 345,
          'nfl_team_id': 2700,
          'pfr': 'MIA',
          'pff': 17,
          'pfflabel': 'MIA',
          'fo': 'MIA',
          'full': 'Miami Dolphins',
          'location': 'Miami',
          'short_location': 'Miami',
          'nickname': 'Dolphins',
          'slug': 'miami-dolphins'
  },
  'NYJ': {
          'nfl': 'NYJ',
          'dk': 'NYJ',
          'dk_id': 352,
          'nfl_team_id': 3430,
          'pfr': 'NYJ',
          'pff': 22,
          'pfflabel': 'NYJ',
          'fo': 'NYJ',
          'full': 'New York Jets',
          'location': 'New York Jets',
          'short_location': 'NY Jets',
          'nickname': 'Jets',
          'slug': 'new-york-jets'
  },
  'LV': {
          'nfl': 'LV',
          'dk': 'LV',
          'dk_id': 341,
          'nfl_team_id': 2520,
          'pfr': 'VEG',
          'pff': 23,
          'pfflabel': 'LV',
          'fo': 'LV',
          'full': 'Las Vegas Raiders',
          'location': 'Las Vegas',
          'short_location': 'Las Vegas',
          'nickname': 'Raiders',
          'slug': 'las-vegas-raiders'
  },
  'ATL': {
          'nfl': 'ATL',
          'dk': 'ATL',
          'dk_id': 323,
          'nfl_team_id': 200,
          'pfr': 'ATL',
          'pff': 2,
          'pfflabel': 'ATL',
          'fo': 'ATL',
          'full': 'Atlanta Falcons',
          'location': 'Atlanta',
          'short_location': 'Atlanta',
          'nickname': 'Falcons',
          'slug': 'atlanta-falcons'
  },
  'NYG': {
          'nfl': 'NYG',
          'dk': 'NYG',
          'dk_id': 351,
          'nfl_team_id': 3410,
          'pfr': 'NYG',
          'pff': 21,
          'pfflabel': 'NYG',
          'fo': 'NYG',
          'full': 'New York Giants',
          'location': 'New York Giants',
          'short_location': 'NY Giants',
          'nickname': 'Giants',
          'slug': 'new-york-giants'
  },
  'CIN': {
          'nfl': 'CIN',
          'dk': 'CIN',
          'dk_id': 327,
          'nfl_team_id': 920,
          'pfr': 'CIN',
          'pff': 7,
          'pfflabel': 'CIN',
          'fo': 'CIN',
          'full': 'Cincinnati Bengals',
          'location': 'Cincinnati',
          'short_location': 'Cincinnati',
          'nickname': 'Bengals',
          'slug': 'cincinnati-bengals'
  },
  'LAC': {
          'nfl': 'LAC',
          'dk': 'LAC',
          'dk_id': 357,
          'nfl_team_id': 4400,
          'pfr': 'SDG',
          'pff': 27,
          'pfflabel': 'LAC',
          'fo': 'LAC',
          'full': 'Los Angeles Chargers',
          'location': 'Los Angeles Chargers',
          'short_location': 'LA Chargers',
          'nickname': 'Chargers',
          'slug': 'los-angeles-chargers'
  },
  'BUF': {
          'nfl': 'BUF',
          'dk': 'BUF',
          'dk_id': 324,
          'nfl_team_id': 610,
          'pfr': 'BUF',
          'pff': 4,
          'pfflabel': 'BUF',
          'fo': 'BUF',
          'full': 'Buffalo Bills',
          'location': 'Buffalo',
          'short_location': 'Buffalo',
          'nickname': 'Bills',
          'slug': 'buffalo-bills'
  },
  'CAR': {
          'nfl': 'CAR',
          'dk': 'CAR',
          'dk_id': 364,
          'nfl_team_id': 750,
          'pfr': 'CAR',
          'pff': 5,
          'pfflabel': 'CAR',
          'fo': 'CAR',
          'full': 'Carolina Panthers',
          'location': 'Carolina',
          'short_location': 'Carolina',
          'nickname': 'Panthers',
          'slug': 'carolina-panthers'
  },
  'MIN': {
          'nfl': 'MIN',
          'dk': 'MIN',
          'dk_id': 347,
          'nfl_team_id': 3000,
          'pfr': 'MIN',
          'pff': 18,
          'pfflabel': 'MIN',
          'fo': 'MIN',
          'full': 'Minnesota Vikings',
          'location': 'Minnesota',
          'short_location': 'Minnesota',
          'nickname': 'Vikings',
          'slug': 'minnesota-vikings'
  },
  'NO': {
          'nfl': 'NO',
          'dk': 'NO',
          'dk_id': 350,
          'nfl_team_id': 3300,
          'pfr': 'NOR',
          'pff': 20,
          'pfflabel': 'NO',
          'fo': 'NO',
          'full': 'New Orleans Saints',
          'location': 'New Orleans',
          'short_location': 'New Orleans',
          'nickname': 'Saints',
          'slug': 'new-orleans-saints'
  },
  'DEN': {
          'nfl': 'DEN',
          'dk': 'DEN',
          'dk_id': 332,
          'nfl_team_id': 1400,
          'pfr': 'DEN',
          'pff': 10,
          'pfflabel': 'DEN',
          'fo': 'DEN',
          'full': 'Denver Broncos',
          'location': 'Denver',
          'short_location': 'Denver',
          'nickname': 'Broncos',
          'slug': 'denver-broncos'
  },
  'SF': {
          'nfl': 'SF',
          'dk': 'SF',
          'dk_id': 359,
          'nfl_team_id': 4500,
          'pfr': 'SFO',
          'pff': 28,
          'pfflabel': 'SF',
          'fo': 'SF',
          'full': 'San Francisco 49ers',
          'location': 'San Francisco',
          'short_location': 'San Francisco',
          'nickname': '49ers',
          'slug': 'san-francisco-49ers'
  },
  'KC': {
          'nfl': 'KC',
          'dk': 'KC',
          'dk_id': 339,
          'nfl_team_id': 2310,
          'pfr': 'KAN',
          'pff': 16,
          'pfflabel': 'KC',
          'fo': 'KC',
          'full': 'Kansas City Chiefs',
          'location': 'Kansas City',
          'short_location': 'Kansas City',
          'nickname': 'Chiefs',
          'slug': 'kansas-city-chiefs'
  },
  'TB': {
          'nfl': 'TB',
          'dk': 'TB',
          'dk_id': 362,
          'nfl_team_id': 4900,
          'pfr': 'TAM',
          'pff': 30,
          'pfflabel': 'TB',
          'fo': 'TB',
          'full': 'Tampa Bay Buccaneers',
          'location': 'Tampa Bay',
          'short_location': 'Tampa Bay',
          'nickname': 'Buccaneers',
          'slug': 'tampa-bay-buccaneers'
  },
  'BAL': {
          'nfl': 'BAL',
          'dk': 'BAL',
          'dk_id': 366,
          'nfl_team_id': 325,
          'pfr': 'RAV',
          'pff': 3,
          'pfflabel': 'BLT',
          'fo': 'BAL',
          'full': 'Baltimore Ravens',
          'location': 'Baltimore',
          'short_location': 'Baltimore',
          'nickname': 'Ravens',
          'slug': 'baltimore-ravens'
  },
  'PIT': {
          'nfl': 'PIT',
          'dk': 'PIT',
          'dk_id': 356,
          'nfl_team_id': 3900,
          'pfr': 'PIT',
          'pff': 25,
          'pfflabel': 'PIT',
          'fo': 'PIT',
          'full': 'Pittsburgh Steelers',
          'location': 'Pittsburgh',
          'short_location': 'Pittsburgh',
          'nickname': 'Steelers',
          'slug': 'pittsburgh-steelers'
  },
  'WAS': {
          'nfl': 'WAS',
          'dk': 'WAS',
          'dk_id': 363,
          'nfl_team_id': 5110,
          'pfr': 'WAS',
          'pff': 32,
          'pfflabel': 'WAS',
          'fo': 'WAS',
          'full': 'Washington Football Team',
          'location': 'Washington',
          'short_location': 'Washington',
          'nickname': 'Football Team',
          'slug': 'washington-football-team'
  },
  'CHI': {
          'nfl': 'CHI',
          'dk': 'CHI',
          'dk_id': 326,
          'nfl_team_id': 810,
          'pfr': 'CHI',
          'pff': 6,
          'pfflabel': 'CHI',
          'fo': 'CHI',
          'full': 'Chicago Bears',
          'location': 'Chicago',
          'short_location': 'Chicago',
          'nickname': 'Bears',
          'slug': 'chicago-bears'
  },
  'GB': {
          'nfl': 'GB',
          'dk': 'GB',
          'dk_id': 335,
          'nfl_team_id': 1800,
          'pfr': 'GNB',
          'pff': 12,
          'pfflabel': 'GB',
          'fo': 'GB',
          'full': 'Green Bay Packers',
          'location': 'Green Bay',
          'short_location': 'Green Bay',
          'nickname': 'Packers',
          'slug': 'green-bay-packers'
  },
  'PHI': {
          'nfl': 'PHI',
          'dk': 'PHI',
          'dk_id': 354,
          'nfl_team_id': 3700,
          'pfr': 'PHI',
          'pff': 24,
          'pfflabel': 'PHI',
          'fo': 'PHI',
          'full': 'Philadelphia Eagles',
          'location': 'Philadelphia',
          'short_location': 'Philadelphia',
          'nickname': 'Eagles',
          'slug': 'philadelphia-eagles'
  },
  'HOU': {
          'nfl': 'HOU',
          'dk': 'HOU',
          'dk_id': 325,
          'nfl_team_id': 2120,
          'pfr': 'HTX',
          'pff': 13,
          'pfflabel': 'HST',
          'fo': 'HOU',
          'full': 'Houston Texans',
          'location': 'Houston',
          'short_location': 'Houston',
          'nickname': 'Texans',
          'slug': 'houston-texans'
  },
  'DET': {
          'nfl': 'DET',
          'dk': 'DET',
          'dk_id': 334,
          'nfl_team_id': 1540,
          'pfr': 'DET',
          'pff': 11,
          'pfflabel': 'DET',
          'fo': 'DET',
          'full': 'Detroit Lions',
          'location': 'Detroit',
          'short_location': 'Detroit',
          'nickname': 'Lions',
          'slug': 'detroit-lions'
  },
  'DAL': {
          'nfl': 'DAL',
          'dk': 'DAL',
          'dk_id': 331,
          'nfl_team_id': 1200,
          'pfr': 'DAL',
          'pff': 9,
          'pfflabel': 'DAL',
          'fo': 'DAL',
          'full': 'Dallas Cowboys',
          'location': 'Dallas',
          'short_location': 'Dallas',
          'nickname': 'Cowboys',
          'slug': 'dallas-cowboys'
  },
  'SEA': {
          'nfl': 'SEA',
          'dk': 'SEA',
          'dk_id': 361,
          'nfl_team_id': 4600,
          'pfr': 'SEA',
          'pff': 29,
          'pfflabel': 'SEA',
          'fo': 'SEA',
          'full': 'Seattle Seahawks',
          'location': 'Seattle',
          'short_location': 'Seattle',
          'nickname': 'Seahawks',
          'slug': 'seattle-seahawks'
  },
  'LAR': {
          'nfl': 'LA',
          'dk': 'LAR',
          'dk_id': 343,
          'nfl_team_id': 2510,
          'pfr': 'RAM',
          'pff': 26,
          'pfflabel': 'LA',
          'fo': 'LAR',
          'full': 'Los Angeles Rams',
          'location': 'Los Angeles Rams',
          'short_location': 'LA Rams',
          'nickname': 'Rams',
          'slug': 'los-angeles-rams'
  }
}



# ----------------------------------------- #
#          Sports IDs, keys, names          #
#  Keys are named by 'title' from odds API  #
# ----------------------------------------- #
SPORTS = {
    'NFL':{
        'dk_id': 1,
        'dk_name': 'NFL',
        'odds_key': 'americanfootball_nfl',
        'sport_data': NFL_TEAMS
    },
    'NHL':{
        'dk_id': 3,
        'dk_name': 'NHL',
        'odds_key': 'icehockey_nhl',
        'sport_data': NHL_TEAMS
    },
    'NBA':{
        'dk_id': 4,
        'dk_name': 'NBA',
        'odds_key': 'basketball_nba',
        'sport_data': NBA_TEAMS
    },
    'MLB':{
        'dk_id': 2,
        'dk_name': 'MLB',
        'odds_key': 'baseball_mlb',
        'sport_data': MLB_TEAMS
    },
    'GOLF':{
        'dk_id': 13,
        'dk_name': 'GOLF'
    },
    'EPL':{
        'dk_id': 12,
        'dk_name': 'SOC',
        'odds_key': 'soccer_epl'
    },
    'NCAAF':{
        'dk_id': 5,
        'dk_name': 'CFB',
        'odds_key': 'americanfootball_ncaaf'
    },
    'NCAAB':{
        'dk_id': 6,
        'dk_name': 'CBB',
        'odds_key': 'basketball_ncaab'
    },
    'MMA':{
        'dk_id': 9,
        'dk_name': 'MMA',
        'odds_key': 'mma_mixed_martial_arts'
    }
}







#
