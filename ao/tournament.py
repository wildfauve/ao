from . import match
from .players import *
from . import results, fantasy_selections, leaderboard, teams
from .util import echo

def show_leaderboard():
    leaderboard_for_teams(apply_fantasy(start()))
    pass

def show_round(event_name, round_number):
    events = start()
    ev = match.find_event(event_name, events)
    if not ev:
        echo.echo(f"Event with name {event_name} not found")
    ev.for_round(round_number).show()


def explain_team_points(team_name):
    teams.explain_points_for_team(team_name, apply_fantasy(start()))
    pass

def start():
    return results.add_results(events())


def apply_fantasy(event_tuple):
    mens_singles, womens_singles = event_tuple
    return fantasy_selections.apply(mens_singles, womens_singles)

def leaderboard_for_teams(teams):
    leaderboard.show(teams)

# Mens Singles
def events():
    return {"MensSingles": (match.Event("MensSingles", 5)
                            .draw_size(number_of_matches=8)
                            .init_draw((1, Nishioka, Khachanov),
                                       (2, Hurkacz, Korda),
                                       (3, Tsitsipas, Sinner),
                                       (4, Lehecka, Auger_Aliassime),
                                       (5, Rublev, Rune),
                                       (6, DeMinaur, Djokovic),
                                       (7, Shelton, Wolf),
                                       (8, BautistaAgut, Paul))),
            "WomensSingles": (match.Event("WomensSingles", 3)
                              .draw_size(number_of_matches=8)
                              .init_draw((1, Swiatek, Rybakina),
                                         (2, Ostapenko, Gauff),
                                         (3, Pegula, Krejcikova),
                                         (4, Azarenka, Zhu),
                                         (5, Pliskova, Zhang),
                                         (6, Linette, Garcia),
                                         (7, Sabalenka, Bencic),
                                         (8, Vekic, Fruhvirtova)))
            }
