from . import results, entries, first_round_draw
from ao.majors import tournaments
from ao.model import tournament_event, draw
from ao.fantasy import points_strategy

FrenchOpen2023 = tournament_event.TournamentEvent(event_of=tournaments.FrenchOpen, year=2023)

FO2023MensSingles = (draw.MensSingles(name="MensSingles", best_of=5, tournament=FrenchOpen2023)
                     .draw_size(number_of_matches=1)
                     .add_entries(entries.mens_singles_entries())
                     .init_draw(first_round_draw.mens_draw_round_1())
                     .fantasy_points_strategy(points_strategy.Points521))

FO2023WomensSingles = (draw.WomensSingles("WomensSingles", best_of=3, tournament=FrenchOpen2023)
                       .draw_size(number_of_matches=1)
                       .add_entries(entries.womens_singles_entries())
                       .init_draw(first_round_draw.womens_draw_round_1())
                       .fantasy_points_strategy(points_strategy.Points521))

FrenchOpen2023.has_draw(FO2023WomensSingles).has_draw(FO2023MensSingles)


results.add_results([FO2023MensSingles, FO2023WomensSingles])
