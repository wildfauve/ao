from ao.ontology.players import *
from ao.model import event


def events():
    return {"MensSingles": (event.Event("MensSingles", 5)
                            .draw_size(number_of_matches=8)
                            .init_draw((1, Nishioka, Khachanov),
                                       (2, Hurkacz, Korda),
                                       (3, Tsitsipas, Sinner),
                                       (4, Lehecka, Auger_Aliassime),
                                       (5, Rublev, Rune),
                                       (6, DeMinaur, Djokovic),
                                       (7, Shelton, Wolf),
                                       (8, BautistaAgut, Paul))),
            "WomensSingles": (event.Event("WomensSingles", 3)
                              .draw_size(number_of_matches=8)
                              .init_draw((1, Swiatek, Rybakina),
                                         (2, Ostapenko, Gauff),
                                         (3, Pegula, Krejcikova),
                                         (4, Azarenka, Zhu),
                                         (5, Pliskova, Zhang),
                                         (6, Linette, Garcia),
                                         (7, Sabalenka, Bencic),
                                         (8, Vekic, Fruhvirtova)))
            }
