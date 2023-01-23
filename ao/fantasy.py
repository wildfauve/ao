from enum import Enum
from functools import partial
from . import match, error

from .util import fn, identity, echo


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
        self.fantasy_events = []

    def event(self, event: match.Event):
        fantasy = self._find_fantasy_event(event)
        if not fantasy:
            fantasy = FantasyEvent(event, self)
            self.fantasy_events.append(fantasy)
        return fantasy

    def show_event(self, event: match.Event):
        ev = self._find_fantasy_event(event)
        ev.show()

    def total_points(self):
        return sum([fantasy_event.total_points() for fantasy_event in self.fantasy_events])

    def explain_points(self):
        return [fantasy_event.explain_points() for fantasy_event in self.fantasy_events]

    def _find_fantasy_event(self, event):
        return fn.find(partial(self._event_predicate, event), self.fantasy_events)

    def _event_predicate(self, test_ev: match.Event, fantasy_event):
        return test_ev == fantasy_event.event


class FantasyEvent:
    def __init__(self, event: match.Event, team: Team):
        self.event = event
        self.team = team
        self.match_selections = {}

    def show(self):
        echo.echo(f"Event: {self.event.name}")
        for rd_id, matches in self.match_selections.items():
            for mt_id, selection in matches.items():
                selection.show()

    def total_points(self):
        return sum([sel.points() for selections in self.match_selections.values() for sel in selections.values()])

    def explain_points(self):
        return {
            "event": self.event.name,
            "matches": [sel.explain_points() for selections in self.match_selections.values() for sel in
                        selections.values()]
        }

    def match(self, match_id):
        rd_id, mt_id = identity.split_match_id(match_id)
        selection = self._find_match_selection(rd_id, mt_id)
        if not selection:
            selection = Selection(self.event, rd_id, mt_id)
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
    def __init__(self, event, round_id, match_id):
        self.round_id = round_id
        self.match = self._find_match(event, round_id, match_id)
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
                "between": f"{self.match.player1.name}, {self.match.player2.name}" if self.match.has_draw() else None,
                "result-winner": "Not Finished",
                "selected-winner": self.selected_winner.name if self.selected_winner else None,
                "selected-in-sets": self.in_number_sets if self.in_number_sets else None,
                "points": []
            }

        return {
            "match": self.match.match_id,
            "between": f"{self.match.player1.name}, {self.match.player2.name}",
            "result-winner": self.match.match_winner.name,
            "result-in-sets": self.match.number_of_sets_played(),
            "selected-winner": self.selected_winner.name if self.selected_winner else None,
            "selected-in-sets": self.in_number_sets if self.in_number_sets else None,
            "points": [points_strategy(explain=True) for points_strategy in self.points_strategy_fns()]
        }

    def show(self):
        self.match.show()
        echo.echo(f"     |_ Selected Winner        : {self.selected_winner.name}")
        echo.echo(f"     |_ Selected Number of Sets: {self.in_number_sets}")

    def _find_match(self, event, round_id, match_id):
        return event.for_round(round_id).for_match(match_id)

    def winner(self, player_name = None):
        if not player_name:
            return self
        if isinstance(player_name, match.Player):
            self.selected_winner = self.match.find_player_by_player(player_name)
        else:
            self.selected_winner = self.match.player_from_player_name(player_name)
        return self

    def in_sets(self, number_of_sets = None):
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
        return (self.round_id - 1) * 2
