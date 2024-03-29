from typing import Tuple, Dict
from functools import reduce, partial

from ao.players import atp_players as players
from .event_web_parser import wm_parser


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
        results_file,
        for_round))


def _parser_for_event(_tournament):
    return wm_parser


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


def _format_results(draws, results_file, for_round):
    if not results_file:
        return draws
    py = reduce(partial(_results_def, for_round), draws.items(), _results_mod_def())
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
    return ""


def _entry_def(py, draw_tuple):
    draw_name, matches = draw_tuple
    return reduce(_player_entry, matches, _entry_function(py, draw_name)) + f"\n{']':>4}"


def _bracket_def(py, draw_tuple):
    draw_name, matches = draw_tuple
    return reduce(_players_bracket, matches, _match_function(py, draw_name)) + f"\n{']':>4}"


def _results_def(for_round, py, draw_tuple):
    draw_name, matches = draw_tuple
    return reduce(_match_result, matches, _result_function(py, draw_name, for_round)) + f"\n{']':>4}"


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
    return f"players.{entry[1].klass_name}"


def _entry_function(py, name):
    return py + f"""
def {'womens_singles_entries()' if "WomensSingles" in name else "mens_singles_entries()"}:
    return [
"""


def _match_function(py, name):
    return py + f"""
def {'womens_draw_round_1()' if "WomensSingles" in name else "mens_draw_round_1()"}:
    return [
"""


def _result_function(py, name, for_round):
    defn = f"mens_singles_results_r{for_round}(draw)" if name == "FO2023MensSingles" else f"womens_singles_results_r{for_round}(draw)"
    return py + f"""
def {defn}:
        return [
    """


def _write_file(file_name, klasses):
    with open(f"{file_name}", 'w') as f:
        f.write(klasses)
