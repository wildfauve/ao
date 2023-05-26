from typing import List
from functools import partial
from rdflib import Graph, URIRef, Literal, RDF
from ao.graph import rdf_prefix



class Player:

    def __init__(self, name, tour_symbol=None):
        self.name = name
        self.subject = rdf_prefix.fau_ten_ind[self.uri_name()]
        self.tour_symbol = tour_symbol

    def uri_name(self):
        return self.name.split(" ")[-1]

    def __hash__(self):
        return hash((self.name,))

    def __eq__(self, other):
        if not self or not other:
            breakpoint()
        return self.name == other.name

    def to_ttl_player(self):
        return f"""
        fau-ten-ind:{self.uri_name()}
        a         fau-ten:Player, owl:NamedIndividual ;
        foaf:name \"{self.name}\" .
        """

    def to_ttl_entry(self):
        return f"""
        fau-ten-ind:{self.uri_name()}AO2023Entry
        a                        fau-ten:QualifiedPlayer ;
        fau-ten:isEntryForPlayer fau-ten-ind:{self.uri_name()} .
        """
