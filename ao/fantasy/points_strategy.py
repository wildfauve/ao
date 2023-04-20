from enum import Enum


class PointsStrategy(Enum):
    pass


class Points521(PointsStrategy):
    NO_POINTS = ('', 0)
    WINNER = ('correct-winner', 5)
    NUMBER_OF_SETS = ('correct-sets', 2)
    LOST_WITH_MAX_SETS = ('bonus-for-loss-in-max-sets', 1)
