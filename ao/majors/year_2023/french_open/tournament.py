from . import results
from ao.majors import tournaments
from ao.players import players
from ao.model import tournament_event, draw
from ao.fantasy import points_strategy

FrenchOpen2023 = tournament_event.TournamentEvent(event_of=tournaments.FrenchOpen, year=2023)

FO2023MensSingles = (draw.MensSingles(name="MensSingles", best_of=5, tournament=FrenchOpen2023)
                     .draw_size(number_of_matches=8)
                     .fantasy_points_strategy(points_strategy.Points521))

FO2023WomensSingles = (draw.WomensSingles("WomensSingles", best_of=3, tournament=FrenchOpen2023)
                       .draw_size(number_of_matches=8)
                       .fantasy_points_strategy(points_strategy.Points521))

FO2023MensSingles.has_entry(players.Nishioka, seed=31)
FO2023MensSingles.has_entry(players.Khachanov, seed=18)
FO2023MensSingles.has_entry(players.Hurkacz, seed=10)
FO2023MensSingles.has_entry(players.Korda, seed=29)
FO2023MensSingles.has_entry(players.Tsitsipas, seed=3)
FO2023MensSingles.has_entry(players.Sinner, seed=15)
FO2023MensSingles.has_entry(players.Lehecka, seed=None)
FO2023MensSingles.has_entry(players.Auger_Aliassime, seed=6)
FO2023MensSingles.has_entry(players.Rublev, seed=5)
FO2023MensSingles.has_entry(players.Rune, seed=9)
FO2023MensSingles.has_entry(players.DeMinaur, seed=22)
FO2023MensSingles.has_entry(players.Djokovic, seed=4)
FO2023MensSingles.has_entry(players.Shelton, seed=None)
FO2023MensSingles.has_entry(players.Wolf, seed=None)
FO2023MensSingles.has_entry(players.BautistaAgut, seed=24)
FO2023MensSingles.has_entry(players.Paul, seed=None)

FO2023WomensSingles.has_entry(players.Swiatek, seed=1)
FO2023WomensSingles.has_entry(players.Rybakina, seed=22)
FO2023WomensSingles.has_entry(players.Ostapenko, seed=17)
FO2023WomensSingles.has_entry(players.Gauff, seed=7)
FO2023WomensSingles.has_entry(players.Pegula, seed=3)
FO2023WomensSingles.has_entry(players.Krejcikova, seed=20)
FO2023WomensSingles.has_entry(players.Azarenka, seed=24)
FO2023WomensSingles.has_entry(players.Zhu, seed=None)
FO2023WomensSingles.has_entry(players.Pliskova, seed=30)
FO2023WomensSingles.has_entry(players.Zhang, seed=23)
FO2023WomensSingles.has_entry(players.Linette, seed=None)
FO2023WomensSingles.has_entry(players.Garcia, seed=4)
FO2023WomensSingles.has_entry(players.Sabalenka, seed=5)
FO2023WomensSingles.has_entry(players.Bencic, seed=12)
FO2023WomensSingles.has_entry(players.Vekic, seed=None)
FO2023WomensSingles.has_entry(players.Fruhvirtova, seed=None)

FrenchOpen2023.has_draw(FO2023WomensSingles).has_draw(FO2023MensSingles)

FO2023MensSingles.init_draw((1, players.Nishioka, players.Khachanov),
                            (2, players.Hurkacz, players.Korda),
                            (3, players.Tsitsipas, players.Sinner),
                            (4, players.Lehecka, players.Auger_Aliassime),
                            (5, players.Rublev, players.Rune),
                            (6, players.DeMinaur, players.Djokovic),
                            (7, players.Shelton, players.Wolf),
                            (8, players.BautistaAgut, players.Paul))

FO2023WomensSingles.init_draw((1, players.Swiatek, players.Rybakina),
                              (2, players.Ostapenko, players.Gauff),
                              (3, players.Pegula, players.Krejcikova),
                              (4, players.Azarenka, players.Zhu),
                              (5, players.Pliskova, players.Zhang),
                              (6, players.Linette, players.Garcia),
                              (7, players.Sabalenka, players.Bencic),
                              (8, players.Vekic, players.Fruhvirtova))

results.add_results([FO2023MensSingles, FO2023WomensSingles])
