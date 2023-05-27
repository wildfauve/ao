from typing import Tuple
from functools import reduce, partial

import requests
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
    'FO2023QualMensSingles': {'name': "qual_mens_singles",
                              'player_module': atp_players,
                              'url_pattern': '/en-us/matches/2023/QM'}
}

round_map = {'first round': 1,
             'second round': 2,
             'third round': 3}

draws = [('https://www.rolandgarros.com/en-us/results/SM?round=1', 'FO2023MensSingles'),
         ('https://www.rolandgarros.com/en-us/results/SD?round=1', 'FO2023WomensSingles')]

# draws = [('ao/util/data_scrapping/data/fo_q_mens_with_results.html', 'FO2023QualMensSingles')]

match_ids = []


def build_draw(for_rd):
    return _brackets(_get_pages(draws), for_rd)


def _get_pages(urls):
    return [(_get_page(url), draw) for url, draw in
            urls]


def _get_page(url_or_file):
    if 'http' in url_or_file:
        return BeautifulSoup(requests.get(url_or_file).text, "html.parser")
    return BeautifulSoup(open(url_or_file, encoding='UTF-8'), "html.parser")


def _brackets(pages, for_rd):
    return reduce(partial(_singles_brackets, for_rd), pages, {})


def _singles_brackets(for_rd, acc, draw_tuple):
    draw, draw_name = draw_tuple
    links = draw.find_all('a')
    matches = [x for x in links if x.get('href') and draw_map[draw_name]['url_pattern'] in x.get('href')]

    matches = sorted(fn.remove_none(map(partial(_match, draw_map[draw_name], for_rd), matches)), key=lambda m: m.href)

    return {**acc, **{draw_name: matches}}


def _match(draw_mapping, for_rd, match_html):
    match_id = match_html.get('href')
    rd = _round(match_html)
    if for_rd and rd != for_rd:
        return None
    if match_id in match_ids:
        return None
    match_ids.append(match_id)

    bloc = match_html.find('div', class_='player-bloc')
    return value.MatchBlock(href=match_id,
                            html=bloc,
                            round=rd,
                            draw_attr_name=draw_mapping['name'],
                            player1=_player_and_scoring_bloc(draw_mapping, bloc, 'team-a-content'),
                            player2=_player_and_scoring_bloc(draw_mapping, bloc, 'team-b-content'))


def _player_and_scoring_bloc(draw_mapping, player_bloc, klass):
    bloc = player_bloc.find('div', class_=klass)
    return _player(draw_mapping, bloc)


def _round(match_html):
    rd = match_html.find('div', class_='roundLabel')
    if not rd:
        return None
    return round_map[rd.text.lstrip().rstrip()]


def _player(draw_mapping, content):
    seed_content = content.find('span', class_='num')
    if seed_content:
        seed = seed_content.text.replace(")", "").replace("(", "")
    else:
        seed = None

    name = content.find('div', class_='name').text.lstrip().rstrip()
    scores = [s.contents[0] for s in content.find_all('div', class_='set')]
    return value.Player(name=name, seed=seed, player_module=draw_mapping['player_module'], scores=scores)
