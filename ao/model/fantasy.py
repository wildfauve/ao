from enum import Enum
from functools import partial
from ao.model.draw import Draw
from ao.model.player import Player

from ao.util import fn, identity, echo, error


class Points(Enum):
    NO_POINTS = ('', 0)
    WINNER = ('correct-winner', 5)
    NUMBER_OF_SETS = ('correct-sets', 2)
    LOST_WITH_MAX_SETS = ('bonus-for-loss-in-max-sets', 1)


class Team:
    def __init__(self, name, members):
        self.name = name
        self.symbolic_name = name.replace(" ", "")
        self.members = members
        self.fantasy_draws = []

    def draw(self, for_draw: Draw):
        fantasy = self._find_fantasy_draw(for_draw)
        if not fantasy:
            fantasy = FantasyDraw(for_draw, self)
            self.fantasy_draws.append(fantasy)
        return fantasy

    def show_draw(self, for_draw: Draw):
        ev = self._find_fantasy_draw(for_draw)
        ev.show()

    def total_points(self, for_round=None):
        return sum([fantasy_draw.total_points(for_round) for fantasy_draw in self.fantasy_draws])

    def explain_points(self):
        return [fantasy_draw.explain_points() for fantasy_draw in self.fantasy_draws]

    def _find_fantasy_draw(self, for_draw):
        return fn.find(partial(self._draw_predicate, for_draw), self.fantasy_draws)

    def _draw_predicate(self, for_draw: Draw, fantasy_draw: Draw):
        return for_draw == fantasy_draw.draw

    def __hash__(self):
        return hash((self.symbolic_name,))

    def __eq__(self, other):
        return self.symbolic_name == other.symbolic_name


class FantasyDraw:
    def __init__(self, draw: Draw, team: Team):
        self.draw = draw
        self.team = team
        self.match_selections = {}

    def show(self):
        echo.echo(f"Event: {self.draw.name}")
        for rd_id, matches in self.match_selections.items():
            for mt_id, selection in matches.items():
                selection.show()

    def total_points(self, for_round=None):
        if for_round:
            if for_round not in self.match_selections.keys():
                return 0
            return sum([sel.points() for sel in self.match_selections[for_round].values()])
        return sum([sel.points() for selections in self.match_selections.values() for sel in selections.values()])

    def explain_points(self):
        return {
            "event": self.draw.name,
            "matches": [sel.explain_points() for selections in self.match_selections.values() for sel in
                        selections.values()]
        }

    def match(self, match_id):
        rd_id, mt_id = identity.split_match_id(match_id)
        selection = self._find_match_selection(rd_id, mt_id)
        if not selection:
            selection = Selection(self.draw, rd_id, mt_id)
            self._add_selection(selection, rd_id, mt_id)
        return selection

    def selection_for(self, round_id, match_id):
        return self._find_match_selection(round_id, match_id)

    def _add_selection(self, selection, round_id, match_id):
        if not self.match_selections.get(round_id):
            self.match_selections[round_id] = {}
        self.match_selections[round_id][match_id] = selection
        return self

    def _find_match_selection(self, round_id, match_id):
        return fn.deep_get(self.match_selections, [round_id, match_id])


class Selection:
    def __init__(self, draw, round_id, match_id):
        self.round_id = round_id
        self.match = self._find_match(draw, round_id, match_id)
        self.selected_winner = None
        self.in_number_sets = None

    def points(self):
        if not self.match.is_finished():
            return 0
        return sum([points_strategy() for points_strategy in self.points_strategy_fns()])

    def explain_points(self):
        if not self.match.is_finished():
            return {
                "match": self.match.match_id,
                "between": f"{self.match.player1.player().name}, {self.match.player2.player().name}" if self.match.has_draw() else None,
                "result-winner": "Not Finished",
                "selected-winner": self.selected_winner.player().name if self.selected_winner else None,
                "selected-in-sets": self.in_number_sets if self.in_number_sets else None,
                "points": []
            }

        return {
            "match": self.match.match_id,
            "between": f"{self.match.player1.player().name}, {self.match.player2.player().name}",
            "result-winner": self.match.match_winner.player().name,
            "result-in-sets": self.match.number_of_sets_played(),
            "selected-winner": self.selected_winner.player().name if self.selected_winner else None,
            "selected-in-sets": self.in_number_sets if self.in_number_sets else None,
            "points": [points_strategy(explain=True) for points_strategy in self.points_strategy_fns()]
        }

    def show(self):
        self.match.show()
        echo.echo(f"     |_ Selected Winner        : {self.selected_winner.player().name}")
        echo.echo(f"     |_ Selected Number of Sets: {self.in_number_sets}")

    def _find_match(self, draw, round_id, match_id):
        return draw.for_round(round_id).for_match(match_id)

    def winner(self, player_name=None):
        if not player_name:
            return self
        if isinstance(player_name, Player):
            self.selected_winner = self.match.find_player_by_player(player_name)
        else:
            self.selected_winner = self.match.player_from_player_name(player_name)
        return self

    def in_sets(self, number_of_sets=None):
        if not number_of_sets:
            return self
        self.in_number_sets = number_of_sets
        return self

    def points_strategy_fns(self):
        return [self.selected_correct_winner, self.selected_correct_sets, self.lost_but_in_max_sets]

    def selected_correct_winner(self, explain: bool = False):
        if self.match.match_winner == self.selected_winner:
            return self.calc(Points.WINNER, explain)
        return self.calc(Points.NO_POINTS, explain, Points.WINNER)

    def selected_correct_sets(self, explain: bool = False):
        if self.match.match_winner != self.selected_winner:
            return self.calc(Points.NO_POINTS, explain, Points.NUMBER_OF_SETS)
        if self.in_number_sets == self.match.number_of_sets_played():
            return self.calc(Points.NUMBER_OF_SETS, explain)
        return self.calc(Points.NO_POINTS, explain, Points.NUMBER_OF_SETS)

    def lost_but_in_max_sets(self, explain: bool = False):
        if (self.match.match_winner != self.selected_winner) and self.match.max_sets_played():
            return self.calc(Points.LOST_WITH_MAX_SETS, explain)
        return self.calc(Points.NO_POINTS, explain, Points.LOST_WITH_MAX_SETS)

    def calc(self, points_type, explain: bool = False, when_no_points: Points = None):
        points_name, value = points_type.value
        if points_type == Points.NO_POINTS:
            return value if not explain else {when_no_points.value[0]: value}
        return self.points_with_factor(value) if not explain else {points_name: self.points_with_factor(value)}

    def points_with_factor(self, points):
        return points * self.round_factor()

    def round_factor(self):
        if self.round_id == 1:
            return 1
        return 2 ** (self.round_id - 1)
