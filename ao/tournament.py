from .model import match
from . import fantasy_selections, leaderboard
from .fantasy import teams
from .majors.year_2023.australian_open import results, events
from .util import echo


def show_leaderboard(board_type, round_number=None):
    leaderboard_for_teams(apply_fantasy(start()), board_type, round_number)
    pass


def show_round(event_name, round_number):
    events = start()
    ev = match.find_event(event_name, events)
    if not ev:
        echo.echo(f"Event with name {event_name} not found")
    ev.for_round(round_number).show()


def result_template(event_name, round_number, template_name):
    events = start()
    ev = match.find_event(event_name, events)
    if not ev:
        echo.echo(f"Event with name {event_name} not found")
    results = ev.for_round(round_number).result_template(template_name)
    for result in results:
        echo.echo(result)


def explain_team_points(team_name):
    teams.explain_points_for_team(team_name, apply_fantasy(start()))
    pass


def start():
    return results.add_results(events.events())


def apply_fantasy(event_tuple):
    mens_singles, womens_singles = event_tuple
    return fantasy_selections.apply(mens_singles, womens_singles)


def leaderboard_for_teams(teams, board_type, round_number):
    leaderboard.current_leaderboard(teams, board_type, round_number)
