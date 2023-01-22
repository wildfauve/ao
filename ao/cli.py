import click

from . import tournament


@click.group()
def cli():
    pass


@click.command()
def leaderboard():
    """
    Starts the tournament,  applies the results, applies the fantasy selection and prints the leaderboard
    """
    tournament.runner()
    pass


@click.command()
@click.option("--round_number", "-r", type=int, default=1, help="The round number to show.")
@click.option("--event", "-e",
              type=click.Choice(['MensSingles', 'WomensSingles']),
              default='MensSingles',
              help="Show the state of a round for an event.")
def show_round(round_number, event):
    """
    Shows the round of an event
    """
    tournament.show_round(event, round_number)
    pass


cli.add_command(leaderboard)
cli.add_command(show_round)
