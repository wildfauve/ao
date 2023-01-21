from functools import partial
from . import match, error

from .util import fn, identity, echo


class Team:
    def __init__(self, name, members):
        self.name = name
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
        self.match = self._find_match(event, round_id, match_id)
        self.selected_winner = None
        self.in_number_sets = None

    def points(self):
        if not self.match.is_finished():
            return 0
        return sum([points_strategy() for points_strategy in self.points_strategy_fns()])

    def show(self):
        self.match.show()
        echo.echo(f"     |_ Selected Winner        : {self.selected_winner.name}")
        echo.echo(f"     |_ Selected Number of Sets: {self.in_number_sets}")

    def _find_match(self, event, round_id, match_id):
        return event.for_round(round_id).for_match(match_id)

    def winner(self, player_name):
        if isinstance(player_name, match.Player):
            self.selected_winner = self.match.find_player_by_player(player_name)
        else:
            self.selected_winner = self.match.player_from_player_name(player_name)
        return self

    def in_sets(self, number_of_sets):
        self.in_number_sets = number_of_sets
        return self

    def points_strategy_fns(self):
        return [self.selected_correct_winner, self.selected_correct_sets, self.lost_but_in_max_sets]

    def selected_correct_winner(self):
        if self.match.match_winner == self.selected_winner:
            return 5
        return 0

    def selected_correct_sets(self):
        if self.in_number_sets == self.match.number_of_sets_played():
            return 2
        return 0

    def lost_but_in_max_sets(self):
        if (self.match.match_winner != self.selected_winner) and self.match.max_sets_played():
            return 1
        return 0
