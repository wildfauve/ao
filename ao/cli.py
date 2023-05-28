import click

from ao import command, presenter
from .majors import tournaments
from .fantasy import teams


def tournament_names():
    return tournaments.tournament_names()


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
    presenter.event_team_scores_table(command.leaderboard_df(tournament, command.BoardType(board_type), round_number))
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--fantasy-team-name", "-f",
              type=click.Choice(teams.symbolised_names()),
              help="team name to explain points")
@click.option("--round_number", "-r", type=int, default=None, help="Leaderboard for specific round")
def show_draw(tournament, fantasy_team_name, round_number):

    command.show_draw(tournament_name=tournament, round=round_number, team_name=fantasy_team_name)
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
@click.option("--round_number", "-r", type=int, default=1, help="The round number to show.")
@click.option("--draw", "-d",
              type=click.Choice(['MensSingles', 'WomensSingles']),
              default='MensSingles',
              help="Show the state of a round for an event.")
@click.option("--template_name", "-n",
              type=click.Choice(['mens_singles', 'womens_singles']),
              default='mens_singles',
              help="A result template to cut and paste")
@click.option("--format", "-f",
              type=click.Choice(['py', 'csv']),
              default='py',
              help="PY or CSV")
def fantasy_score_template(tournament, round_number, draw, template_name, format):
    """
    Get a result DSL template
    """
    command.fantasy_score_template(tournament, draw, round_number, template_name, format)
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


@click.command()
@click.option("--ttl-file", "-f", type=str, default=None, help="location of TTL Graph output")
def generate_graph(ttl_file):
    """
    Generates TTL Graph
    """
    command.generate_graph(ttl_file)
    pass


@click.command()
@click.option("--file", "-f", type=str, default=None, help="Player class file")
def player_scrap(file):
    """
    Generates a player class file from the top 200 from the ATP and WTA
    """
    command.player_scrap(file)
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--entries_file", "-e", type=str, default=None, help="Entries class file")
@click.option("--draws_file", "-d", type=str, default=None, help="draws class file")
@click.option("--results_file", "-s", type=str, default=None, help="results file")
@click.option("--round_number", "-r", type=int, default=None, help="The round number to show.")
@click.option('--scores-only/--full-draw', "-o/-f", default=False)
def draw_scrap(tournament, entries_file, draws_file, results_file, round_number, scores_only):
    """
    """
    command.draw_scrap(tournament=tournament,
                       entries_file=entries_file,
                       draws_file=draws_file,
                       results_file=results_file,
                       round_number=round_number,
                       scores_only=scores_only)
    pass


@click.option('--file', '-f', required=True)
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--position/--accum", "-p/-a", required=True, help="Plot Position, or plot total scores")
@click.command()
def ranking_plot(file, tournament, position):
    """
    Generate a Ranking Graph
    """
    command.rank_plot(file=file, tournament_name=tournament, position=position)
    pass


cli.add_command(leaderboard)
cli.add_command(show_round)
cli.add_command(show_draw)
cli.add_command(explain_team_score)
cli.add_command(result_template)
cli.add_command(generate_graph)
cli.add_command(player_scrap)
cli.add_command(draw_scrap)
cli.add_command(ranking_plot)
cli.add_command(fantasy_score_template)
