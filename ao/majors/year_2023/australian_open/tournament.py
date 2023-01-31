from . import results
from ao.majors import tournaments
from ao.players import players
from ao.model import tournament_event, draw

AustralianOpen2023 = tournament_event.TournamentEvent(event_of=tournaments.AustralianOpen, year=2023)

AO2023MensSingles = (draw.MensSingles(name="MensSingles", best_of=5, tournament=AustralianOpen2023)
                     .draw_size(number_of_matches=8))

AO2023WomensSingles = (draw.WomensSingles("WomensSingles", best_of=3, tournament=AustralianOpen2023)
                       .draw_size(number_of_matches=8))

AO2023MensSingles.has_entry(players.Nishioka, seed=31)
AO2023MensSingles.has_entry(players.Khachanov, seed=18)
AO2023MensSingles.has_entry(players.Hurkacz, seed=10)
AO2023MensSingles.has_entry(players.Korda, seed=29)
AO2023MensSingles.has_entry(players.Tsitsipas, seed=3)
AO2023MensSingles.has_entry(players.Sinner, seed=15)
AO2023MensSingles.has_entry(players.Lehecka, seed=None)
AO2023MensSingles.has_entry(players.Auger_Aliassime, seed=6)
AO2023MensSingles.has_entry(players.Rublev, seed=5)
AO2023MensSingles.has_entry(players.Rune, seed=9)
AO2023MensSingles.has_entry(players.DeMinaur, seed=22)
AO2023MensSingles.has_entry(players.Djokovic, seed=4)
AO2023MensSingles.has_entry(players.Shelton, seed=None)
AO2023MensSingles.has_entry(players.Wolf, seed=None)
AO2023MensSingles.has_entry(players.BautistaAgut, seed=24)
AO2023MensSingles.has_entry(players.Paul, seed=None)

AO2023WomensSingles.has_entry(players.Swiatek, seed=1)
AO2023WomensSingles.has_entry(players.Rybakina, seed=22)
AO2023WomensSingles.has_entry(players.Ostapenko, seed=17)
AO2023WomensSingles.has_entry(players.Gauff, seed=7)
AO2023WomensSingles.has_entry(players.Pegula, seed=3)
AO2023WomensSingles.has_entry(players.Krejcikova, seed=20)
AO2023WomensSingles.has_entry(players.Azarenka, seed=24)
AO2023WomensSingles.has_entry(players.Zhu, seed=None)
AO2023WomensSingles.has_entry(players.Pliskova, seed=30)
AO2023WomensSingles.has_entry(players.Zhang, seed=23)
AO2023WomensSingles.has_entry(players.Linette, seed=None)
AO2023WomensSingles.has_entry(players.Garcia, seed=4)
AO2023WomensSingles.has_entry(players.Sabalenka, seed=5)
AO2023WomensSingles.has_entry(players.Bencic, seed=12)
AO2023WomensSingles.has_entry(players.Vekic, seed=None)
AO2023WomensSingles.has_entry(players.Fruhvirtova, seed=None)

AustralianOpen2023.has_draw(AO2023WomensSingles).has_draw(AO2023MensSingles)

AO2023MensSingles.init_draw((1, players.Nishioka, players.Khachanov),
                            (2, players.Hurkacz, players.Korda),
                            (3, players.Tsitsipas, players.Sinner),
                            (4, players.Lehecka, players.Auger_Aliassime),
                            (5, players.Rublev, players.Rune),
                            (6, players.DeMinaur, players.Djokovic),
                            (7, players.Shelton, players.Wolf),
                            (8, players.BautistaAgut, players.Paul))

AO2023WomensSingles.init_draw((1, players.Swiatek, players.Rybakina),
                              (2, players.Ostapenko, players.Gauff),
                              (3, players.Pegula, players.Krejcikova),
                              (4, players.Azarenka, players.Zhu),
                              (5, players.Pliskova, players.Zhang),
                              (6, players.Linette, players.Garcia),
                              (7, players.Sabalenka, players.Bencic),
                              (8, players.Vekic, players.Fruhvirtova))

results.add_results([AO2023MensSingles, AO2023WomensSingles])