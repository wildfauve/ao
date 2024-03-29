from typing import Tuple, List
from functools import reduce, partial
import re

import requests
import json
# from bs4 import BeautifulSoup

from ao import model
from ao.players import atp_players, wta_players
from ao.util import fn

from ao.util.data_scrapping import value

match_id_pattern = re.compile('matches\\/\\d+\\/\\w{2}(\\d+)')

draw_map = {
    'WM2023WomensSingles': {'name': "womens_singles",
                            'player_module': wta_players},
    'WM2023MensSingles': {'name': "mens_singles",
                          'player_module': atp_players}}

round_code_map = {'1': 1,
                  '2': 2,
                  '3': 3,
                  '4': 4,
                  'Q': 5,
                  'S': 6,
                  'F': 7}

# draws = [("https://2023.wimbledon.com/en_GB/scores/feeds/2023/draws/LS.json", 'WM2023WomensSingles'),
#          ('https://2023.wimbledon.com/en_GB/scores/feeds/2023/draws/MS.json', 'WM2023MensSingles')]
draws = [('ao/util/data_scrapping/data/men_draw.json', 'WM2023MensSingles')]

match_ids = {'mens_singles': [], 'womens_singles': []}


def build_draw(for_rd, scores_only):
    return _assign_match_numbers(_brackets(_get_json(draws, for_rd), for_rd, scores_only))


def _get_json(urls, for_rd) -> List[Tuple]:
    return [(_get_doc(url, for_rd), draw) for url, draw in urls]


def _get_doc(url_or_file, for_rd):
    if 'http' in url_or_file:
        headers = {'Content-Type': 'application/json', 'User-Agent': 'vscode-restclient'}
        result = requests.get(url_or_file, headers=headers)
        return result.json()
    f = open(url_or_file, "r")
    return json.loads(f.read())


def _brackets(pages, for_rd, scores_only):
    return reduce(partial(_singles_brackets, for_rd, scores_only), pages, {})


def _assign_match_numbers(draws):
    for draw, matches in draws.items():
        min_number = min([_match_id_fn(m_id) for m_id in match_ids[draw_map[draw]['name']]])
        for m in matches:
            m.set_match_number_from_1(min_number)
    return draws


def _singles_brackets(for_rd, scores_only, acc, draw_tuple):
    draw, draw_name = draw_tuple
    matches = fn.remove_none([_match(draw_map[draw_name], for_rd, scores_only, match) for match in draw.get('matches')])
    return {**acc, **{draw_name: matches}}


def _match(draw_mapping, for_rd, scores_only, match):
    match_id = match.get('match_id')
    rd = round_code_map.get(match.get('roundCode'))
    if for_rd and rd != for_rd:
        return None
    if match_id in match_ids[draw_mapping['name']]:
        return None
    match_ids[draw_mapping['name']].append(match_id)

    match_bloc = value.MatchBlock(href=match_id,
                                  json=match,
                                  round=rd,
                                  draw_attr_name=draw_mapping['name'],
                                  player1=_player(draw_mapping, match.get('team1'), team=1, scores=match.get('scores')),
                                  player2=_player(draw_mapping, match.get('team2'), team=2, scores=match.get('scores')),
                                  match_id_fn=_match_id_fn)
    if scores_only and not match_bloc.has_result():
        return None
    return match_bloc

def _player(draw_mapping, player_content, team, scores):
    seed = player_content.get('seed', None) if player_content.get('seed', None) else player_content.get('entryStatus',
                                                                                                        None)
    return value.Player(name=f"{player_content.get('firstNameA')} {player_content.get('lastNameA')}",
                        seed=seed,
                        match_state=_determine_match_state_exceptions(player_content),
                        player_module=draw_mapping['player_module'],
                        scores=_scores(scores, team))


def _scores(content, team_number):
    sets = content.get('sets', None)
    if not sets:
        return None
    return [set_team_scores[team_number -1].get('score', None) for set_team_scores in sets]


def _determine_match_state_exceptions(content):
    # if content('span', class_='abandon'):
    #     return model.MatchState.RET
    # if content('span', class_='forfait'):
    #     return model.MatchState.WITHDRAWN
    return None


def _match_id_fn(match_id):
    return int(match_id[2:4])
