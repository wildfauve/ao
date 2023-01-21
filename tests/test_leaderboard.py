from ao import leaderboard
from tests.shared import *

def test_allocate_points(capsys, event, event2, players, fantasy_team, fantasy_team_2):
    pl1, pl2, pl3, pl4 = players

    fantasy_team.event(event).match("1.1").winner(pl1).in_sets(3)
    fantasy_team.event(event).match("1.2").winner(pl3).in_sets(3)
    fantasy_team.event(event2).match("1.1").winner(pl1).in_sets(3)
    fantasy_team.event(event2).match("1.2").winner(pl3).in_sets(3)

    fantasy_team_2.event(event).match("1.1").winner(pl2).in_sets(3)
    fantasy_team_2.event(event).match("1.2").winner(pl4).in_sets(3)
    fantasy_team_2.event(event2).match("1.1").winner(pl2).in_sets(3)
    fantasy_team_2.event(event2).match("1.2").winner(pl4).in_sets(3)


    event.for_round(1).for_match(1).score(pl1, (6, 6, 6)).score(pl2, (4, 4, 4))
    event2.for_round(1).for_match(1).score(pl1, (6, 4, 6)).score(pl2, (4, 6, 4))

    leaderboard.show([fantasy_team, fantasy_team_2])

    captured = capsys.readouterr()

    expected = """14  FantasyTeam1
5   FantasyTeam2
"""

    assert captured.out == expected

