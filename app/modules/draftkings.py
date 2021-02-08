#!/usr/bin/env python3
import requests, json, os, sys, csv, pickle
sys.path.append('..')
import utils.helpers as utils, utils.urls as urls, pandas as pd, utils.data as data, datetime as dt 



# ---------- #
#  *BROKEN*  #
# ---------- #
# due to change in draftkings API endpoints.
# will need to access contests, and get draftgroup IDs from list of contests


def get_slate(sportId, *args):
    
    check_list = data.CLASSIC_IDS # Only using classic DFS game type for now
    counter, game_count, id_counter = 1, 1, 1
    draft_group_ids, dg_ids, slate, dg_times = [], {}, {}, []
    newDict = requests.get(urls.upcoming_draft_groups_url()).json()


    for x in newDict['draftGroups']:
        if x['sportId'] == sportId and x['gameTypeId'] in check_list:
            dg_ids[id_counter] = {
                'id': x['draftGroupId'],
                'start': dt.datetime.timestamp(utils.strip_datetime(x['minStartTime']))
            }
            dg_times.append(dg_ids[id_counter]['start'])
            id_counter += 1

    next_slate = utils.return_dgid_from_ts(dg_ids, min(dg_times))
    print(urls.draftables_url(next_slate))
    # r = requests.get(urls.draftables_url(next_slate)).json()
    # print(r)
    # with open(output_file, "w+") as f:
        # json.dump(r, f)
    # for game in r['competitions']:
    #     if sportId == 3:
    #         for x in data.NHL_TEAMS:
    #             if game['homeTeam']['abbreviation'] in data.NHL_TEAMS[x]['dk_abbreviation']:
    #                 team1 = data.NHL_TEAMS[x]['secondary_name']
    #             elif game['awayTeam']['abbreviation'] in data.NHL_TEAMS[x]['dk_abbreviation']:
    #                 team2 = data.NHL_TEAMS[x]['secondary_name']
    #     elif sportId == 4:
    #         for x in data.NBA_TEAMS:
    #             if game['homeTeam']['abbreviation'] in data.NBA_TEAMS[x]['dk_abbreviation']:
    #                 team1 = data.NBA_TEAMS[x]['secondary_name']
    #             elif game['awayTeam']['abbreviation'] in data.NBA_TEAMS[x]['dk_abbreviation']:
    #                 team2 = data.NBA_TEAMS[x]['secondary_name']
    #     else:
    #         team1 = game['homeTeam']['abbreviation']
    #         team2 = game['awayTeam']['abbreviation']
    #     slate[counter] = {
    #         'team': team1,
    #         'opp': team2
    #     }
    #     counter += 1
    #     slate[counter] = {
    #         'team': team2,
    #         'opp': team1
    #     }
    #     counter += 1
    #     game_count += 1

    # df_slate = pd.DataFrame.from_dict(slate, orient='index')


    # df_slate = df_slate.set_index(['game', 'team'])

    # return df_slate

get_slate(1)