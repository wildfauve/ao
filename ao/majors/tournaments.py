from typing import List
import importlib
import re

from ao import model

AustralianOpen = model.GrandSlam(name="Australian Open", subject_name="AustralianOpen", perma_id="ao")
FrenchOpen = model.GrandSlam(name="French Open", subject_name="FrenchOpen", perma_id="fo")
Wimbledon = model.GrandSlam(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")
USOpen = model.GrandSlam(name="US Open", subject_name="UsOpen", perma_id="uo")

TournamentLoaderConfig = {
    'AustralianOpen2023': (2023, "australian_open"),
    'FrenchOpen2023': (2023, "french_open"),
    'Wimbledon2023': (2023, "wimbledon")
}


def tournament_names():
    return TournamentLoaderConfig.keys()


def tournament_in_fantasy(name):
    """
    Takes a tournament name and dynamically loads the tournament module associated with that tournament.
    For example, if the name is AustralianOpen2023, the module loaded is ao.majors.year_2023.australian_open.tournament


    :param name:
    :return:
    """
    if name not in tournament_names():
        return None
    year, tournament_module_name = TournamentLoaderConfig.get(name)
    tournament_module = importlib.import_module(f"ao.majors.year_{year}.{tournament_module_name}.tournament")
    return getattr(tournament_module, name)


def add_results(draws: List[model.Draw], results_module):
    mens, womens = _for_round(model.find_draw_by_cls(model.MensSingles, draws),
                              model.find_draw_by_cls(model.WomensSingles, draws),
                              results_module)
    return mens, womens


def _for_round(mens_singles, womens_singles, results_module):
    return _for_rd_fn_caller(results_module, [mens_singles, womens_singles])


def _for_rd_fn_caller(results_module, draws: List):
    for draw in draws:
        [getattr(results_module, f)(draw) for f in dir(results_module) if re.match(f"^{draw.fn_symbol}_", f)]
    return draws
