from ao.model import tournament
import importlib

AustralianOpen = tournament.GrandSlam(name="Australian Open", subject_name="AustralianOpen", perma_id="ao")
FrenchOpen = tournament.GrandSlam(name="French Open", subject_name="FrenchOpen", perma_id="fo")

TournamentLoaderConfig = {
    'AustralianOpen2023': (2023, "australian_open"),
    'FrenchOpen2023': (2023, "french_open")
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
