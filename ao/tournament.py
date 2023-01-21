from . import match
from .players import *

# Mens Singles

mens_singles = (match.Event("MensSingles", 5)
                .draw_size(number_of_matches=8)
                .init_draw((1, Nishioka, Khachanov),
                           (2, Hurkacz, Korda),
                           (3, Tsitsipas, Sinner),
                           (4, Lehecka, Auger_Aliassime),
                           (5, Rublev, Rune),
                           (6, deMinaur, Djokovic),
                           (7, Shelton, Wolf),
                           (8, BautistaAgut, Paul)))

womens_singles = (match.Event("WomensSingles", 3)
                  .draw_size(number_of_matches=8)
                  .init_draw((1, Swiatek, Rybakina),
                             (2, Ostapenko, Gauff),
                             (3, Pegula, Krejcikova),
                             (4, Azarenka, Zhu),
                             (5, Pliskova, Zhang),
                             (6, Linette, Garcia),
                             (7, Sabalenka, Bencic),
                             (8, Vekic, Fruhvirtova)))
