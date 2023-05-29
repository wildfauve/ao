from typing import Callable, List, Tuple
from functools import reduce
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


class PointsStrategyCalculator:

    def __init__(self, points_strategy: PointsStrategy, per_round_accum_strategy: Callable):
        self.points_strategy = points_strategy
        self.per_round_accum_strategy = per_round_accum_strategy

    def calc(self, selection, explain: bool = False):
        result = [points_strategy(selection, explain) for points_strategy in self.points_strategy_fns()]
        if explain:
            return result
        return sum(result)

    def points_strategy_fns(self):
        return [self.selected_correct_winner, self.selected_correct_sets, self.lost_but_in_max_sets]

    def selected_correct_winner(self, selection, explain: bool = False):
        if selection.match.match_winner == selection.selected_winner:
            return self._calc(self.points_strategy.WINNER, selection.round_id, explain)
        return self._calc(self.points_strategy.NO_POINTS, selection.round_id, explain, self.points_strategy.WINNER)

    def selected_correct_sets(self, selection, explain: bool = False):
        if selection.match.match_winner != selection.selected_winner:
            return self._calc(self.points_strategy.NO_POINTS, selection.round_id, explain,
                              self.points_strategy.NUMBER_OF_SETS)
        if selection.in_number_sets == selection.match.number_of_sets_played():
            return self._calc(self.points_strategy.NUMBER_OF_SETS, selection.round_id, explain)
        return self._calc(self.points_strategy.NO_POINTS, selection.round_id, explain,
                          self.points_strategy.NUMBER_OF_SETS)

    def lost_but_in_max_sets(self, selection, explain: bool = False):
        if (selection.match.match_winner != selection.selected_winner) and selection.match.max_sets_played():
            return self._calc(self.points_strategy.LOST_WITH_MAX_SETS, selection.round_id, explain)
        return self._calc(self.points_strategy.NO_POINTS, selection.round_id, explain,
                          self.points_strategy.LOST_WITH_MAX_SETS)

    def _calc(self, points_type, rd, explain: bool = False, when_no_points: PointsStrategy = None):
        points_name, value = points_type.value
        if points_type == self.points_strategy.NO_POINTS:
            return value if not explain else {when_no_points.value[0]: value}
        return self._points_with_factor(value, rd) if not explain else {points_name: self._points_with_factor(value, rd)}

    def _points_with_factor(self, points, rd):
        return points * self.per_round_accum_strategy(rd)

    def calc_points_schedule(self, number_of_matches):
        round_of = self._max_number_rds(number_of_matches)
        return reduce(self._points_schedule_for_rd, zip(round_of, range(1, len(round_of) + 1)), [])

    def _points_schedule_for_rd(self, acc: List, rd_match_numbers: Tuple):
        num_matches, rd = rd_match_numbers
        pts = self.per_round_accum_strategy(rd) * (sum([pts for _name, pts in self._points_of_type()]) * num_matches)
        acc.append(pts)
        return acc

    def _points_of_type(self):
        return [self.points_strategy.WINNER.value,
                self.points_strategy.NUMBER_OF_SETS.value]

    def _max_number_rds(self, number_of_matches):
        return self._rd_range([], number_of_matches)

    def _rd_range(self, acc, curr):
        if curr < 1:
            return acc
        acc.append(curr)
        return self._rd_range(acc, int(curr / 2))


def doubling_per_round_strategy(rd: int):
    if rd == 1:
        return 1
    return 2 ** (rd - 1)
