import pytest

from ao.model import player
from ao.model.event import Event


@pytest.fixture
def event(players):
    pl1, pl2, pl3, pl4 = players
    ev = (Event("MensSingles", best_of=5)
          .draw_size(number_of_matches=2)
          .init_draw((1, pl1, pl2),
                     (2, pl3, pl4)))
    return ev


@pytest.fixture
def event2(players):
    pl1, pl2, pl3, pl4 = players
    ev = (Event("WomensSingles", best_of=3)
          .draw_size(number_of_matches=2)
          .init_draw((1, pl1, pl2),
                     (2, pl3, pl4)))
    return ev


@pytest.fixture
def players():
    pl1 = player.Player(name="Player1", seed=1)
    pl2 = player.Player(name="Player2")
    pl3 = player.Player(name="Player3", seed=10)
    pl4 = player.Player(name="Player4")

    return pl1, pl2, pl3, pl4
