from typing import List
from ao.model import draw
from ao.players.atp_players import *


def add_results(draws: List[draw.Draw]):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, draws)
    womens_singles = draw.find_draw_by_cls(draw.WomensSingles, draws)
    mens_singles_results(mens_singles)
    womens_singles_results(womens_singles)
    return mens_singles, womens_singles

def mens_singles_results(draw):
    # Round 1 (round of 128)
    draw.for_round(1).for_match(1).score(Khachanov, (6, 6, 7)).score(Nishioka, (0, 0, 6))


def womens_singles_results(draw):
    # Round 1 (round of 128)
    draw.for_round(1).for_match(1).score(Rybakina, (6, 6)).score(Swiatek, (4, 4))
