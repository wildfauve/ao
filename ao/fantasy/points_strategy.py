from enum import Enum


class PointsStrategy(Enum):
    pass


class Points521(PointsStrategy):
    NO_POINTS = ('', 0)
    WINNER = ('correct-winner', 5)
    NUMBER_OF_SETS = ('correct-sets', 2)
    LOST_WITH_MAX_SETS = ('bonus-for-loss-in-max-sets', 1)


class Points1HalfHalf(PointsStrategy):
    NO_POINTS = ('', 0)
    WINNER = ('correct-winner', 1)
    NUMBER_OF_SETS = ('correct-sets', 0.5)
    LOST_WITH_MAX_SETS = ('bonus-for-loss-in-max-sets', 0.5)


def doubling_per_round_strategy(round: int):
    if round == 1:
        return 1
    return 2 ** (round - 1)
