from ao.ontology.players import *
from ao.model import event

MensSingles = (event.Event(name="MensSingles", best_of=5, root_resource_name="ao")
               .draw_size(number_of_matches=8))

WomensSingles = (event.Event("WomensSingles", best_of=3, root_resource_name="ao")
                 .draw_size(number_of_matches=8))


def events():
    return {"MensSingles": (event.Event(name="MensSingles", best_of=5, root_resource_name="ao")
                            .draw_size(number_of_matches=8)
                            .init_draw((1, Nishioka, Khachanov),
                                       (2, Hurkacz, Korda),
                                       (3, Tsitsipas, Sinner),
                                       (4, Lehecka, Auger_Aliassime),
                                       (5, Rublev, Rune),
                                       (6, DeMinaur, Djokovic),
                                       (7, Shelton, Wolf),
                                       (8, BautistaAgut, Paul))),
            "WomensSingles": (event.Event("WomensSingles", best_of=3, root_resource_name="ao")
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
