from typing import Tuple, Dict
from functools import reduce

from ao.players import atp_players as players
from .event_web_parser import fo_draw_parser


def build_draw(tournament: str,
               entries_file=None,
               draws_file=None,
               results_file=None,
               for_round=None,
               scores_only=False):
    (_format_results(
        _format_brackets(
            _format_entries(
                    _parser_for_event(tournament).build_draw(for_round, scores_only),
                entries_file),
            draws_file),
        results_file))


def _parser_for_event(_tournament):
    return fo_draw_parser


# def _match_number(matches):
#     for _, draw_matches in matches.items():
#         for num in range(0, len(draw_matches)):
#             draw_matches[num].set_match_number(num + 1)
#     return matches


def _format_entries(draws: Dict, entries_file):
    if not entries_file:
        return draws
    py = reduce(_entry_def, draws.items(), _entry_imports_hdr())
    _write_file(entries_file, py)
    return draws


def _format_brackets(draws, draws_file):
    if not draws_file:
        return draws
    py = reduce(_bracket_def, draws.items(), _first_round_draw_def())
    _write_file(draws_file, py)
    return draws


def _format_results(draws, results_file):
    if not results_file:
        return draws
    py = reduce(_results_def, draws.items(), _results_mod_def())
    _write_file(results_file, py)
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


def _results_mod_def():
    return """from typing import List
from ao.players import wta_players, atp_players
from ao.model import draw

    
def add_results(draws: List[draw.Draw]):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, draws)
    womens_singles = draw.find_draw_by_cls(draw.WomensSingles, draws)
    mens_singles_results(mens_singles)
    womens_singles_results(womens_singles)
    return mens_singles, womens_singles
    
"""


def _entry_def(py, draw_tuple):
    draw_name, matches = draw_tuple
    return reduce(_player_entry, matches, _entry_function(py, draw_name)) + f"\n{']':>4}"


def _bracket_def(py, draw_tuple):
    draw_name, matches = draw_tuple
    return reduce(_players_bracket, matches, _match_function(py, draw_name)) + f"\n{']':>4}"


def _results_def(py, draw_tuple):
    draw_name, matches = draw_tuple
    return reduce(_match_result, matches, _result_function(py, draw_name)) + f"\n{']':>4}"


def _players_bracket(acc, match):
    return acc + match.match_format()


def _match_result(acc, match):
    return acc + match.results_format(f"{'':>8}")


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


def _result_function(py, name):
    return py + f"""
def {'mens_singles_results(draw)' if name == "FO2023MensSingles" else "womens_singles_results(draw)"}:
        return [
    """


def _write_file(file_name, klasses):
    with open(f"{file_name}", 'w') as f:
        f.write(klasses)
