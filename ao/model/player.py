from typing import List
from functools import partial
from rdflib import Graph, URIRef, Literal, RDF
from ao.graph import rdf_prefix
from ao.util import fn


class Player:
    klass_name_replace_set = [("-", "_"), (" ", "_"), ("'", "")]
    dot_name_split_char = "."
    sp_name_split_char = " "


    def __init__(self, name, tour_symbol: str, klass_name: str, alt_names: List = None):
        self.name = name
        self.subject = rdf_prefix.fau_ten_ind[self.uri_name()]
        self.tour_symbol = tour_symbol
        self.klass_name = klass_name
        self.alt_names = alt_names if alt_names else []

    def _format_player_klass_name(self, name):
        nm = name.rstrip().lstrip()
        if "." in nm:
            splitter = self.dot_name_split_char
        else:
            splitter = self.sp_name_split_char
        return fn.multi_replace(nm.split(splitter)[-1], self.klass_name_replace_set)

    def uri_name(self):
        return self.name.split(" ")[-1]

    def __hash__(self):
        return hash((self.name,))

    def __eq__(self, other):
        if not self or not other:
            breakpoint()
        return self.name == other.name

    def match_by_name(self, on_name):
        if self._format_player_klass_name(on_name) == self.klass_name:
            return self
        if self.name == on_name:
            return self
        if self._format_player_klass_name(on_name) in self.klass_name:
            if any([alt_name == on_name for alt_name in self.alt_names]):
                return self
        return None

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
