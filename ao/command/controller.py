from functools import partial

from ao.model import tournament_event, draw
from . import leaderboard, graph_generator
from ao.fantasy import teams, selections
from ao.majors import tournaments
from ao import fantasy
from ao.util import echo, fn


def show_leaderboard(tournament_name, board_type, round_number=None):
    tournie = find_tournament_by_name(tournament_name)
    if not tournie:
        return
    leaderboard_for_teams(apply_fantasy(start(tournie)), board_type, round_number)
    pass


def show_round(tournament_name, draw_name, round_number):
    tournie = find_tournament_by_name(tournament_name)
    if not tournie:
        return
    start(tournie)
    for_draw = draw.find_draw(draw_name, tournie.draws)
    if not for_draw:
        echo.echo(f"Draw with name {draw_name} not found in {tournie.label}")
    for_draw.for_round(round_number).show()


def result_template(tournament_name, draw_name, round_number, template_name):
    tournie = find_tournament_by_name(tournament_name)
    if not tournie:
        return
    start(tournie)
    for_draw = draw.find_draw(draw_name, tournie.draws)
    if not for_draw:
        echo.echo(f"Draw with name {draw_name} not found in {tournie.label}")
        return
    results = for_draw.for_round(round_number).result_template(template_name)
    for result in results:
        echo.echo(result)


def explain_team_points(tournament_name, team_name):
    tournie = find_tournament_by_name(tournament_name)
    if not tournie:
        return
    teams.explain_points_for_team(team_name, apply_fantasy(start(tournie)))
    pass

def generate_graph(ttl_file):
    graph_generator.generate(ttl_file)

# Helpers

def start(tournie):
    return tournie


def apply_fantasy(tournie):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, tournie.draws)
    womens_singles = draw.find_draw_by_cls(draw.WomensSingles, tournie.draws)

    fantasy_module = fantasy.fantasy_tournaments.get(tournie.name, None)

    if not fantasy_module:
        echo.echo(f"No fantasy selections for {tournie.name}")
        return

    return selections.apply(fantasy_module, mens_singles, womens_singles)


def leaderboard_for_teams(teams, board_type, round_number):
    leaderboard.current_leaderboard(teams, board_type, round_number)


def find_tournament_by_name(for_name: str):
    """
    imports tournament modules only when being used on the CLI.
    """
    tournie = tournaments.tournament_in_fantasy(for_name)
    if not tournie:
        echo.echo(f"{for_name} does not exist as a tournament")
    return tournie

