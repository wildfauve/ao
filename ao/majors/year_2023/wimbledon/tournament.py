from . import results, entries, first_round_draw
from ao.majors import tournaments
from ao.model import tournament_event, draw
from ao.fantasy import points_strategy

Wimbledon2023 = tournament_event.TournamentEvent(event_of=tournaments.Wimbledon, year=2023)


WM2023MensSingles = (draw.MensSingles(name="MensSingles",
                                      fn_symbol="mens_singles",
                                      best_of=5,
                                      tournament=Wimbledon2023)
                     .draw_size(number_of_matches=64)
                     .add_entries(entries.mens_singles_entries())
                     .init_draw(first_round_draw.mens_draw_round_1())
                     .fantasy_points_strategy(points_strategy.strategy_2_1_point5_double()))

WM2023WomensSingles = (draw.WomensSingles("WomensSingles",
                                          fn_symbol="womens_singles",
                                          best_of=3,
                                          tournament=Wimbledon2023)
                       .draw_size(number_of_matches=64)
                       .add_entries(entries.womens_singles_entries())
                       .init_draw(first_round_draw.womens_draw_round_1())
                       .fantasy_points_strategy(points_strategy.strategy_2_1_point5_double()))

Wimbledon2023.has_draw(WM2023WomensSingles).has_draw(WM2023MensSingles)

tournaments.add_results(draws=[WM2023MensSingles, WM2023WomensSingles], results_module=results)
