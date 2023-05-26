from typing import Tuple, Dict
from functools import reduce, partial
from bs4 import BeautifulSoup

from ao.players import atp_players as players
from ao.util import fn
from . import fo_draw_parser

# rankings = [('ao/util/data_scrapping/data/fo_2023_mens_singles_draw.html', 'FO2023MensSingles')]
rankings = [('ao/util/data_scrapping/data/fo_2023_womens_singles_draw.html', 'FO2023WomensSingles')]


def build_draw(entries_file, draws_file):
    _format_brackets(_format_entries(fo_draw_parser.build_draw(), entries_file), draws_file)


def _get_pages(urls):
    return [(BeautifulSoup(open(f, encoding='UTF-8'), "html.parser"), draw) for f, draw in urls]


def _format_entries(matches: Dict, entries_file):
    py = reduce(_entry_def, matches.items(), _entry_imports_hdr())
    _write_file(entries_file, py)
    return matches


def _format_brackets(draws, draws_file):
    py = reduce(_bracket_def, draws.items(), _first_round_draw_def())
    _write_file(draws_file, py)
    return draws


def _entry_imports_hdr():
    return """from typing import Tuple, List, Optional
from ao import model
from ao.players import wta_players, atp_players
"""


def _first_round_draw_def():
    return """from typing import Tuple, List
from ao.players import wta_players, atp_players
from ao import model"""


def _entry_def(py, draw_tuple):
    draw_name, matches = draw_tuple
    return reduce(_player_entry, matches, _entry_function(py, draw_name)) + f"\n{']':>4}"


def _bracket_def(py, draw_tuple):
    draw_name, matches = draw_tuple
    return reduce(partial(_players_bracket, matches), range(0, len(matches)),
                  _match_function(py, draw_name)) + f"\n{']':>4}"


def _players_bracket(matches, acc, match_number):
    return acc + matches[match_number].match_format(match_number)


def _entry_predicate(bracket_number, entry):
    return int(entry[0]) == bracket_number


def _player_entry(py, match):
    return py + match.entry_format()


def _player_definition(entry: Tuple[str, str, str]):
    if not entry:
        return f"players.NOT-FOUND"
    return f"players.{_player_entry_klass_name(entry[1])}"


def _player_entry_klass_name(name):
    formatted_name = _format_klass_name(name)
    if formatted_name not in dir(players):
        return f"{formatted_name}--FIXME"
    return formatted_name


def _entry_function(py, name):
    return py + f"""
def {'mens_singles_entries()' if name == "FO2023MensSingles" else "womens_singles_entries()"}:
    return [
"""


def _match_function(py, name):
    return py + f"""
def {'mens_draw_round_1()' if name == "FO2023MensSingles" else "womens_draw_round_1()"}:
    return [
"""


def _write_file(file_name, klasses):
    with open(f"{file_name}", 'w') as f:
        f.write(klasses)
