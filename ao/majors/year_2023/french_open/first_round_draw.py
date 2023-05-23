from typing import Tuple, List
from ao.players import players
from ao import model



def mens_draw_round_1() -> List[Tuple[int, model.Player, model.Player]]:
    return [
        (1, players.Nishioka, players.Khachanov)
    ]


def womens_draw_round_1() -> List[Tuple[int, model.Player, model.Player]]:
    return [
        (1, players.Swiatek, players.Rybakina)
    ]
