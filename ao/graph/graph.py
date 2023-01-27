from rdflib import Graph, URIRef
from pathlib import Path

from . import binding

BASE_PATH = (Path(__file__).parent.parent / "ontology")
EVENT_BASE_PATH = (Path(__file__).parent.parent / "majors")

TENNIS_ONTO = (BASE_PATH / "ontology.ttl")
PLAYERS_IND = (BASE_PATH / "players.ttl")
AO2023 = (EVENT_BASE_PATH / "year_2023" / "australian_open" / "triple_store" / "ao2023.ttl")


def graph():
    g = initgraph()
    g.parse(TENNIS_ONTO)
    g.parse(PLAYERS_IND)
    g.parse(AO2023)
    return g


def initgraph() -> Graph:
    return binding.bind(rdf_graph())


def rdf_graph():
    return Graph()
