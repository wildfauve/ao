from tests.shared import *

def test_create_match(event, players):
    pl1, pl2, pl3, pl4 = players
    assert len(event.rounds) == 2

    r1_m1, r1_m2 = event.for_round(1).matches

    assert r1_m1.number == 1
    assert r1_m1.match_id == "1.1"
    assert r1_m1.player1 == pl1
    assert r1_m1.player2 == pl2
    assert r1_m2.number == 2
    assert r1_m2.match_id == "1.2"
    assert r1_m2.player1 == pl3
    assert r1_m2.player2 == pl4

    r2_m1, = event.rounds[1].matches

    assert r2_m1.number == 1
    assert r2_m1.match_id == "2.1"
    assert not r2_m1.player1


def test_results(event, players):
    pl1, pl2, pl3, pl4 = players

    event.for_round(1).for_match(1).score(pl1, (6, 4, 6, 4, 6)).score(pl2, (4, 6, 4, 6, 4))

    mt = event.for_round(1).for_match(1)

    assert mt.is_finished()
    assert mt.winner() == pl1

    next_rd_mt = event.for_round(2).for_match(1)
    assert next_rd_mt.player1 == pl1
    assert not next_rd_mt.player2

    # When game not finished
    event.for_round(1).for_match(2).score(pl3, (6, 3, 6)).score(pl4, (4, 6, 4))

    assert next_rd_mt.player1 == pl1
    assert next_rd_mt.player2 == pl3
    assert not next_rd_mt.is_finished()


def test_results_when_not_max_sets(event, players):
    pl1, pl2, pl3, pl4 = players

    event.for_round(1).for_match(1).score(pl1, (6, 6, 6)).score(pl2, (4, 4, 4))

    mt = event.for_round(1).for_match(1)

    assert mt.is_finished()
    assert mt.winner() == pl1


def test_show_round_matches(capsys, event):
    rd = event.for_round(1)

    rd.show()

    captured = capsys.readouterr()

    expected_output = """Round: 1
Matches:
1.1  -- (  1) Player1 
        (   ) Player2 
1.2  -- ( 10) Player3 
        (   ) Player4 
"""

    assert captured.out == expected_output



def test_show_round_matches_with_scores(capsys, event, players):
    pl1, pl2, pl3, pl4 = players

    event.for_round(1).for_match(1).score(pl1, (6, 6, 6)).score(pl2, (4, 4, 4))

    rd = event.for_round(1)

    rd.show()

    captured = capsys.readouterr()

    expected_output = """Round: 1
Matches:
1.1  -- (  1) Player1 6 6 6  <
        (   ) Player2 4 4 4  
1.2  -- ( 10) Player3 
        (   ) Player4 
"""
    assert expected_output in captured.out


def test_result_template(capsys, event, players):
    results = event.for_round(1).result_template("mens_singles")
    breakpoint()