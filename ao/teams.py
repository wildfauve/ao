from functools import partial
import json

from .fantasy import Team
from .util import fn, echo

TeamGelatoGiants = Team("Team Gelato Giants", "Bronzie, Juki & Lemmie")
TeamPolarPrecision = Team("Team Polar Precision", "IceT, Pepsi, Rollie & Gertie")
TeamHeroHangouts = Team("Team Hero Hangouts", "Marmalade, Richmond, Greenwich")
TeamBearNecessities = Team("Team Bear Necessities", "Fraser, Tom, Frank, Spencer & Duck")
TeamMusicalBears = Team("Team Musical Bears", "Rinksy, Beetie, Motzie")
TeamFauve = Team("Team Fauve", "Perky")
TeamClojo = Team("Team Clojo", "Claudie, Fyodoro")
TeamLightHouse = Team("Team LightHouse", "Edouard, Piri")

teams = [TeamGelatoGiants,
         TeamPolarPrecision,
         TeamHeroHangouts,
         TeamBearNecessities,
         TeamMusicalBears,
         TeamClojo,
         TeamLightHouse,
         TeamFauve]

def symbolised_names():
    return [t.symbolic_name for t in teams]

def explain_points_for_team(team_name, teams):
    team = find_team(team_name, teams)
    if not team:
        echo.echo("Team Not Found")
        return None
    echo.echo(json.dumps(team.explain_points(), indent=4))
    pass


def find_team(team_name, teams):
    return fn.find(partial(_team_name_predicate, team_name), teams)


def _team_name_predicate(team_name, team):
    return team_name == team.symbolic_name
