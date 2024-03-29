from ao.graph import graph
from ao.majors import tournaments
from ao.fantasy import teams

def generate(ttl_file):
    g = graph.empty_graph()

    [t.build_graph(g) for t in tournaments.TournamentsInFantasy]

    teams.build_graph(g)

    graph.write_to_ttl(g, file=ttl_file)
