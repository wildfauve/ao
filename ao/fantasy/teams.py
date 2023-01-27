from functools import partial
import json

from ao.model import fantasy
from ao.util import fn, echo

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

def symbolised_names():
    return [t.symbolic_name for t in teams]

def explain_points_for_team(team_name, teams):
    team = find_team_by_name(team_name, teams)
    if not team:
        echo.echo("Team Not Found")
        return None
    echo.echo(json.dumps(team.explain_points(), indent=4))
    pass


def find_team_by_name(team_name, teams):
    breakpoint()
    return fn.find(partial(_team_name_predicate, team_name), teams)

def find_team(team, teams):
    return fn.find(partial(_team_predicate, team), teams)



def _team_name_predicate(team_name, team):
    return team_name == team.symbolic_name


def _team_predicate(team_to_find, team):
    return team_to_find == team
