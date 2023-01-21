import pytest

from ao import fantasy

@pytest.fixture
def fantasy_team():
    return fantasy.Team("FantasyTeam1", "Member1")

@pytest.fixture
def fantasy_team_2():
    return fantasy.Team("FantasyTeam2", "Member2")