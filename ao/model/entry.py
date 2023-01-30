from rdflib import Graph, RDF, URIRef, Literal
from ao.graph import rdf_prefix
class Entry:
    """
    <https://fauve.io/ao/2023/entries/Aliassime>
    a                        fau-ten:QualifiedPlayer ;
    fau-ten:hasSeed          6 ;
    fau-ten:isInDraw         <https://fauve.io/ao/2023/mensSingles> ;
    fau-ten:isEntryForPlayer fau-ten-ind:Aliassime .
    """

    def __init__(self, player, draw, seed):
        self.is_entry_for_player = player
        self.is_in_draw = draw
        self.has_seed = seed
        self.subject = URIRef(f"{self.is_in_draw.subject.toPython()}/{self.is_entry_for_player.uri_name()}")

    def player(self):
        return self.is_entry_for_player


    def seeding(self):
        if not self.has_seed:
            return "   "
        return str(self.has_seed).rjust(3)

    def build_graph(self, g: Graph):
        g.add((self.subject, RDF.type, rdf_prefix.fau_ten.QualifiedPlayer))
        g.add((self.subject, rdf_prefix.fau_ten.hasSeed, Literal(self.has_seed)))
        g.add((self.subject, rdf_prefix.fau_ten.isEntryForPlayer, self.player().subject))
        return g


