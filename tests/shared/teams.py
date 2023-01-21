import pytest

from ao import fantasy

@pytest.fixture
def fantasy_team():
    return fantasy.Team("FantasyTeam", "Member1")