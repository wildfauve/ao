import pytest

from ao.model import player, tournament_event, tournament, draw
from ao.players import players


@pytest.fixture
def test_tournament():
    return build_tournament()


def build_tournament():
    TestMajor2023 = tournament_event.TournamentEvent(
        event_of=tournament.GrandSlam(name="Test Open", subject_name="TestOpen", perma_id="to"),
        year=2023)

    T2023MensSingles = (draw.MensSingles(name="MensSingles", best_of=5, tournament=TestMajor2023)
                        .draw_size(number_of_matches=2))

    T2023WomensSingles = (draw.WomensSingles(name="WomensSingles", best_of=3, tournament=TestMajor2023)
                          .draw_size(number_of_matches=2))

    TestMajor2023.has_draw(T2023MensSingles)

    T2023MensSingles.has_entry(players.Khachanov, seed=18)
    T2023MensSingles.has_entry(players.Hurkacz, seed=10)
    T2023MensSingles.has_entry(players.Korda, seed=29)
    T2023MensSingles.has_entry(players.Tsitsipas, seed=3)

    T2023MensSingles.init_draw((1, players.Hurkacz, players.Khachanov),
                               (2, players.Korda, players.Tsitsipas))

    return TestMajor2023
