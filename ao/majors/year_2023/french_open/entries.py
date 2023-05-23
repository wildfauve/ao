from typing import Tuple, List, Optional
from ao import model
from ao.players import players


def mens_singles_entries() -> List[Tuple[model.player, Optional[int]]]:
    """
    A list of player entries into the Mens Single Draw

    (players.<PlayerName>, seed)

    """
    return [
        (players.Nishioka, None),
        (players.Khachanov, None)
    ]


def womens_singles_entries() -> List[Tuple[model.player, Optional[int]]]:
    """
    A list of player entries into the Womens Single Draw

    (players.<PlayerName>, seed)

    """

    return [
        (players.Swiatek, None),
        (players.Rybakina, None)
    ]
