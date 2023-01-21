import pytest

from tests.shared import *

from ao import fantasy, error


def test_create_pick(event, players, fantasy_team):
    pl1, pl2, pl3, pl4 = players

    selection = fantasy_team.event(event).match("1.1").winner("Player1").in_sets(3)

    assert len(fantasy_team.fantasy_events) == 1
    assert fantasy_team.fantasy_events[0].event.name == "MensSingles"

    assert selection.match.match_id == "1.1"
    assert selection.selected_winner == pl1
    assert selection.in_number_sets == 3

def test_create_pick_with_player_object(event, players, fantasy_team):
    pl1, pl2, pl3, pl4 = players

    selection = fantasy_team.event(event).match("1.1").winner(pl1).in_sets(3)

    assert selection.selected_winner == pl1


def test_sub_string_of_player_name(event, players, fantasy_team):
    pl1, pl2, pl3, pl4 = players

    selection = fantasy_team.event(event).match("1.1").winner("er1").in_sets(3)

    assert selection.selected_winner == pl1


def test_create_multiple_picks(event, players, fantasy_team):
    pl1, pl2, pl3, pl4 = players

    fantasy_team.event(event).match("1.1").winner("Player1").in_sets(3)
    fantasy_team.event(event).match("1.2").winner("Player3").in_sets(3)

    assert len(fantasy_team.fantasy_events) == 1
    assert fantasy_team.fantasy_events[0].event.name == "MensSingles"

    assert fantasy_team.fantasy_events[0].selection_for(1, 1).selected_winner == pl1
    assert fantasy_team.fantasy_events[0].selection_for(1, 2).selected_winner == pl3


def test_multiple_picks_multiple_events(event, event2, players, fantasy_team):
    pl1, pl2, pl3, pl4 = players

    fantasy_team.event(event).match("1.1").winner("Player1").in_sets(3)
    fantasy_team.event(event).match("1.2").winner("Player3").in_sets(3)
    fantasy_team.event(event2).match("1.1").winner("Player1").in_sets(3)
    fantasy_team.event(event2).match("1.2").winner("Player3").in_sets(3)


    assert len(fantasy_team.fantasy_events) == 2

    assert fantasy_team.fantasy_events[0].event.name == "MensSingles"
    assert fantasy_team.fantasy_events[0].selection_for(1, 1).selected_winner == pl1
    assert fantasy_team.fantasy_events[0].selection_for(1, 2).selected_winner == pl3

    assert fantasy_team.fantasy_events[1].event.name == "WomensSingles"
    assert fantasy_team.fantasy_events[1].selection_for(1, 1).selected_winner == pl1
    assert fantasy_team.fantasy_events[1].selection_for(1, 2).selected_winner == pl3

def test_show_event(capsys, event, event2, players, fantasy_team):
    fantasy_team.event(event).match("1.1").winner("Player1").in_sets(3)
    fantasy_team.event(event).match("1.2").winner("Player3").in_sets(3)
    fantasy_team.event(event2).match("1.1").winner("Player1").in_sets(3)
    fantasy_team.event(event2).match("1.2").winner("Player3").in_sets(3)

    fantasy_team.show_event(event)

    captured = capsys.readouterr()

    expected_output = """Event: MensSingles
1.1  -- (  1) Player1 
        (   ) Player2 
     |_ Selected Winner        : Player1
     |_ Selected Number of Sets: 3
1.2  -- ( 10) Player3 
        (   ) Player4 
     |_ Selected Winner        : Player3
     |_ Selected Number of Sets: 3
"""

    assert captured.out == expected_output


def test_match_doesnt_exist(event, players, fantasy_team):
    with pytest.raises(error.ConfigException):
        fantasy_team.event(event).match("1.3").winner("Player1").in_sets(3)


def test_round_doesnt_exist(event, players, fantasy_team):
    with pytest.raises(error.ConfigException):
        fantasy_team.event(event).match("4.1").winner("Player1").in_sets(3)


def test_match_has_no_players(event, players, fantasy_team):
    with pytest.raises(error.ConfigException):
        fantasy_team.event(event).match("2.1").winner("Player1").in_sets(3)
