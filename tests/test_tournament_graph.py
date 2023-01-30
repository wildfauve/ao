from ao.majors import tournaments
from ao.majors.year_2023.australian_open import tournament
from ao.graph import graph

ttl_file = "tests/fixtures/tournaments.ttl"
def test_tournament_graph():
    g = graph.empty_graph()

    tournaments.AustralianOpen.build_graph(g)

    tournament.AustralianOpen2023.build_graph(g)

    graph.write_to_ttl(g, file=ttl_file)

    breakpoint()


def test_build_tournament_draw():
    tournament.AO2023WomensSingles.for_round(1).show()

