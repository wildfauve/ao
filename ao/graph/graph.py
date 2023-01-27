from rdflib import Graph, URIRef
from pathlib import Path

from . import binding

BASE_PATH = Path(__file__).parent.parent

ONTO_PATH = (BASE_PATH / "ontology" / "tennis_majors.ttl")


def graph():
    g = initgraph()
    g.parse(ONTO_PATH)
    return g


def initgraph() -> Graph:
    return binding.bind(rdf_graph())


def rdf_graph():
    return Graph()


def gics_ontology_and_ind(base_path):
    return ((base_path / GICS_CLASSIFICATION_PATH).resolve(),
            (base_path / GICS_CLASSIFICATION_IND_PATH).resolve())


def gics_pickle_path(base_path, ontology_version):
    return (base_path / f"{GICS_PICKLE_NAME}v{ontology_version}.p").resolve()
