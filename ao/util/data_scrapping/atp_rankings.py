from functools import reduce, partial
import requests
from bs4 import BeautifulSoup
# from markdownify import MarkdownConverter, markdownify as md
import argparse
import string

rankings = [('https://nytimes.stats.com/tennis/rankings.asp?tour=ATP&rank=3', '/tennis/players.asp?tour=ATP&id='),
            ('https://nytimes.stats.com/tennis/rankings.asp?tour=WTA&rank=3', '/tennis/players.asp?tour=WTA&id=')]


def players(file):
    klasses = format_klasses(display_dups(player_links(get_pages(rankings))))
    write_file(file, klasses)


def get_pages(urls):
    return [(BeautifulSoup(requests.get(url).text, "html.parser"), link_pattern) for url, link_pattern in urls]


def player_links(pages):
    return reduce(tour_links, pages, [])


def tour_links(players, page_tuple):
    pg, link_form = page_tuple
    [players.append(player_model(link)) for link in pg.find_all("a") if link_form in link.get('href')]
    return players


def display_dups(players):
    klass_names = [name for _, _, name in players]
    dups = {f"Duplicate: {dup} occurances: {klass_names.count(dup)}" for dup in klass_names if
            klass_names.count(dup) > 1}
    for dup in dups:
        print(dup)
    return players


def player_model(link):
    return (link.get('href'), link.string, format_klass_name(link.string))


def format_klass_name(name):
    return name.rstrip().split(' ')[-1].replace("-", "_").replace("'", "")


def format_klasses(players):
    """
    from ao.model.player import Player

    Nishioka = Player("Y. Nishioka")
    """
    return reduce(partial(player_def, [player[2] for player in players]), players, "from ao.model.player import Player\n\n")


def player_def(players_klass_names, klasses, player):
    link, name, klass_name = player
    if players_klass_names.count(klass_name) > 1:
        klass_name = deal_with_dup(klass_name, name)
    return klasses + f"{klass_name} = Player(\"{name}\")\n\n"


def deal_with_dup(klass_name, name):
    first_name = name.split(' ')[0].replace("-", "_").replace("'", "")
    return f"{klass_name}_{first_name}"


def write_file(file_name, klasses):
    with open(f"{file_name}", 'w') as f:
        f.write(klasses)
