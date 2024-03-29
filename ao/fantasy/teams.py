from typing import Union
from functools import partial, reduce
import json

from rich.console import Console
from rich.table import Table
from rich import box

from ao.model import fantasy
from ao.util import fn, echo

console = Console()

TeamGelatoGiants = fantasy.Team("Team Gelato Giants", "Bronzie, Juki & Lemmie")
TeamPolarPrecision = fantasy.Team("Team Polar Precision", "IceT, Pepsi, Rollie & Gertie")
TeamHeroHangouts = fantasy.Team("Team Hero Hangouts", "Marmalade, Richmond, Greenwich")
TeamBearNecessities = fantasy.Team("Team Bear Necessities", "Fraser, Tom, Frank, Spencer & Duck")
TeamMusicalBears = fantasy.Team("Team Musical Bears", "Rinksy, Beetie, Motzie")
TeamFauve = fantasy.Team("Team Fauve", "Perky")
TeamClojo = fantasy.Team("Team Clojo", "Claudie, Fyodoro")
TeamLightHouse = fantasy.Team("Team LightHouse", "Edouard, Piri")

teams = [TeamGelatoGiants,
         TeamPolarPrecision,
         TeamHeroHangouts,
         TeamBearNecessities,
         TeamMusicalBears,
         TeamClojo,
         TeamLightHouse,
         TeamFauve]


def build_graph(g):
    [team.build_graph(g) for team in teams]


def symbolised_names():
    return [t.symbolic_name for t in teams]


def points_details_all_teams(teams):
    return reduce(_team_points_aggregate, teams, {})


def _team_points_aggregate(accum, team):
    for_team = explain_points_for_team(team)
    return {**accum, **{team: for_team}}


def explain_points_for_team(team: Union[str, fantasy.Team], teams=None):
    tm = find_team_by_name(team, teams) if isinstance(team, str) else team
    if not tm:
        echo.echo("Team Not Found")
        return None
    return tm.explain_points()


def show_draw_for_team(team_name, teams, round):
    team = find_team_by_name(team_name, teams)
    if not team:
        echo.echo("Team Not Found")
        return None

    table = Table(title=f"Leaderboard For Round {round}", box=box.ROUNDED)

    table.add_column("Draw", justify="center", style="cyan", no_wrap=True)
    table.add_column("Match Number", justify="center", style="cyan", no_wrap=True)
    table.add_column("Match", justify="center", style="cyan", no_wrap=True)
    table.add_column("Selected Winner", justify="left", style="magenta")
    table.add_column("Selected Sets", justify="left", style="magenta")

    team.show_draws(table=table, for_round=round)

    console.print(table)


def find_team_by_name(team_name, teams):
    return fn.find(partial(_team_name_predicate, team_name), teams)


def find_team(team, teams):
    return fn.find(partial(_team_predicate, team), teams)


def _team_name_predicate(team_name, team):
    return team_name == team.symbolic_name


def _team_predicate(team_to_find, team):
    return team_to_find == team
