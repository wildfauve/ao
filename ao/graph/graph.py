from rdflib import Graph, URIRef
from pathlib import Path

from . import binding

BASE_PATH = (Path(__file__).parent.parent / "ontology")

TENNIS_ONTO = (BASE_PATH / "ontology.ttl")
PLAYERS_IND = (BASE_PATH / "players.ttl")
TOURNAMENT_IND = (BASE_PATH / "tournaments.ttl")


def graph():
    g = initgraph()
    g.parse(TENNIS_ONTO)
    g.parse(PLAYERS_IND)
    g.parse(TOURNAMENT_IND)
    return g


def initgraph() -> Graph:
    return binding.bind(rdf_graph())


def rdf_graph():
    return Graph()
