from typing import Tuple
from functools import reduce, partial
from bs4 import BeautifulSoup

from ao.players import atp_players as players
from ao.util import fn

rankings = [('ao/util/data_scrapping/data/fo_2023_mens_singles_draw.html', 'FO2023MensSingles')]


def build_draw(entries_file, draws_file):
    _format_brackets(_format_entries(_brackets(_get_pages(rankings)), entries_file), draws_file)


def _get_pages(urls):
    return [(BeautifulSoup(open(f, encoding='UTF-8'), "html.parser"), draw) for f, draw in urls]


def _brackets(pages):
    return reduce(_singles_brackets, pages, {})


def _singles_brackets(acc, draw_tuple):
    draw, draw_name = draw_tuple
    entries = reduce(_entries, draw.find_all('div', class_='scores-draw-entry-box'), [])
    return {**acc, **{draw_name: entries}}


def _entries(acc, entry):
    return reduce(_table, entry.find_all('table'), acc)


def _table(acc, table):
    return reduce(_tr, table.find_all('tr'), acc)


def _tr(acc, row):
    td = row.find_all('td')
    pl_match_position = td[0].text
    seed = td[1].text.lstrip().rstrip().replace("(", "").replace(")", "")
    player = td[2].find('a').text.lstrip().rstrip()
    acc.append((pl_match_position, player, seed))
    return acc


def _format_klass_name(name):
    return name.rstrip().split(' ')[-1].replace("-", "_").replace("'", "")


def _format_entries(draws, entries_file):
    py = reduce(_entry_def, draws.items(), _imports_hdr())
    _write_file(entries_file, py)
    return draws


def _format_brackets(draws, draws_file):
    py = reduce(_bracket_def, draws.items(), _first_round_draw_def())
    _write_file(draws_file, py)
    return draws


def _imports_hdr():
    return "from typing import Tuple, List, Optional\nfrom ao import model\nfrom ao.players import players\n\n"


def _first_round_draw_def():
    return """from typing import Tuple, List
from ao.players import players
from ao import model"""


def _entry_def(py, draw_tuple):
    draw_name, entries = draw_tuple
    return reduce(_player_entry, entries, _entry_function(py, draw_name)) + f"\n{']':>4}"


def _bracket_def(py, draw_tuple):
    draw_name, entries = draw_tuple
    return reduce(partial(_players_bracket, entries), zip(range(1, 128, 2), range(2, 129, 2)),
                  _match_function(py, draw_name))


def _players_bracket(entries, acc, bracket):
    pl1, pl2 = bracket
    pl1_entry = fn.find(partial(_entry_predicate, pl1), entries)
    pl2_entry = fn.find(partial(_entry_predicate, pl2), entries)
    return acc + f"{'':>12}({int(pl2 / 2)}, {_player_definition(pl1_entry)}, {_player_definition(pl2_entry)}),\n"


def _entry_predicate(bracket_number, entry):
    return int(entry[0]) == bracket_number


def _player_entry(py, entry):
    entry_number, player, seed = entry
    return py + f"{'':>12}(players.{_player_definition(entry)}, {seed if seed else 'None'}),\n"


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
def {'mens_singles_entries()' if name == "FO2023MensSingles" else "womens_singles_entries"} -> List[Tuple[model.player, Optional[int]]]:
    return [
"""


def _match_function(py, name):
    return py + f"""
def {'mens_draw_round_1()' if name == "FO2023MensSingles" else "mens_draw_round_1()"} -> List[Tuple[model.player, Optional[int]]]:
    return [
"""


def _write_file(file_name, klasses):
    with open(f"{file_name}", 'w') as f:
        f.write(klasses)
