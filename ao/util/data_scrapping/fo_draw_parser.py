from typing import Tuple
from functools import reduce, partial

import bs4.element
from bs4 import BeautifulSoup
from dataclasses import dataclass

from ao.players import atp_players, wta_players
from ao.util import fn

from . import value

draw_map = {
    'FO2023WomensSingles': {'name': "womens_singles",
                            'player_module': wta_players,
                            'url_pattern': '/en-us/matches/2023/SD'},
    'FO2023MensSingles': {'name': "mens_singles",
                          'player_module': atp_players,
                          'url_pattern': '/en-us/matches/2023/SM'},
}

draws = [('ao/util/data_scrapping/data/fo_2023_mens_singles_draw.html', 'FO2023MensSingles'),
         ('ao/util/data_scrapping/data/fo_2023_womens_singles_draw.html', 'FO2023WomensSingles')]

match_ids = []

def build_draw():
    return _brackets(_get_pages(draws))


def _get_pages(urls):
    return [(BeautifulSoup(open(f, encoding='UTF-8'), "html.parser"), draw) for f, draw in urls]


def _brackets(pages):
    return reduce(_singles_brackets, pages, {})


def _singles_brackets(acc, draw_tuple):
    draw, draw_name = draw_tuple
    links = draw.find_all('a')
    matches = [x for x in links if x.get('href') and draw_map[draw_name]['url_pattern'] in x.get('href')]

    matches = sorted(fn.remove_none(map(partial(_match, draw_map[draw_name]), matches)), key=lambda m: m.href)

    return {**acc, **{draw_name: matches}}


def _match(draw_mapping, match_html):
    match_id = match_html.get('href')
    if match_id in match_ids:
        return None
    match_ids.append(match_id)

    bloc = match_html.find('div', class_='player-bloc')
    pl1 = _player(draw_mapping, bloc.find('div', class_='team-a-content'))
    pl2 = _player(draw_mapping, bloc.find('div', class_='team-b-content'))
    return value.MatchBlock(href=match_id,
                            html=bloc,
                            round=_round(match_html),
                            player1=pl1,
                            player2=pl2)


def _round(match_html):
    rd = match_html.find('div', class_='roundLabel')
    if not rd:
        return None
    return rd.text.lstrip().rstrip()


def _player(draw_mapping, content):
    seed_content = content.find('span', class_='num')
    if seed_content:
        seed = seed_content.text.replace(")", "").replace("(", "")
    else:
        seed = None

    name = content.find('div', class_='name').text.lstrip().rstrip()
    return value.Player(name=name, seed=seed, player_module=draw_mapping['player_module'])
