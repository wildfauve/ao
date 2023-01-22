from . import teams
from ao.util import echo

def current_leaderboard():
    show(teams.teams)

def show(teams):
    echo.echo("Leaderboard:")
    echo.echo("------------")
    rankings = sorted_teams(teams)
    ljust_len = int(len(str(max([r[1] for r in rankings]))))
    for team, score in sorted_teams(teams):
        echo.echo(f"{str(score).ljust(ljust_len)}  {team.name}")
    pass


def sorted_teams(teams):
    return sorted([(team, team.total_points()) for team in teams], key=lambda t: t[1], reverse=True)
