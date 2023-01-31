import click

from . import command
from .majors import tournaments
from .leaderboard import BoardType
from .fantasy import teams


def tournament_names():
    return [t.name for t in tournaments.TournamentsInFantasy]

@click.group()
def cli():
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--round_number", "-r", type=int, default=None, help="Leaderboard for specific round")
@click.option("--board_type", "-b",
              type=click.Choice(['f1', 'fantasy']),
              default='fantasy',
              help="Either the Fantasy Leaderboard or the F1 leaderboard")
def leaderboard(tournament, round_number, board_type):
    """
    Starts the tournament,  applies the results, applies the fantasy selection and prints the leaderboard
    """
    command.show_leaderboard(tournament, BoardType(board_type), round_number)
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--draw", "-d",
              type=click.Choice(['MensSingles', 'WomensSingles']),
              default='MensSingles',
              help="Show the state of a round for an event.")
@click.option("--round_number", "-r", type=int, default=1, help="The round number to show.")
def show_round(tournament, round_number, draw):
    """
    Shows the round of an event
    """
    command.show_round(tournament, draw, round_number)
    pass

@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--round_number", "-r", type=int, default=1, help="The round number to show.")
@click.option("--draw", "-d",
              type=click.Choice(['MensSingles', 'WomensSingles']),
              default='MensSingles',
              help="Show the state of a round for an event.")
@click.option("--template_name", "-n",
              type=click.Choice(['mens_singles', 'womens_singles']),
              default='mens_singles',
              help="A result template to cut and paste")
def result_template(tournament, round_number, draw, template_name):
    """
    Get a result DSL template
    """
    command.result_template(tournament, draw, round_number, template_name)
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--fantasy-team-name", "-f",
              type=click.Choice(teams.symbolised_names()),
              help="team name to explain points")
def explain_team_score(tournament, fantasy_team_name):
    """
    Shows the round of an event
    """
    command.explain_team_points(tournament, fantasy_team_name)
    pass



cli.add_command(leaderboard)
cli.add_command(show_round)
cli.add_command(explain_team_score)
cli.add_command(result_template)
