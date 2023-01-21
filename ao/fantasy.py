from functools import partial
from . import match, error

from .util import fn, identity


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

    def _find_fantasy_event(self, event):
        return fn.find(partial(self._event_predicate, event), self.fantasy_events)

    def _event_predicate(self, test_ev: match.Event, fantasy_event):
        return test_ev == fantasy_event.event


class FantasyEvent:
    def __init__(self, event: match.Event, team: Team):
        self.event = event
        self.team = team
        self.match_selections = {}

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

    def _find_match(self, event, round_id, match_id):
        return event.for_round(round_id).for_match(match_id)

    def winner(self, player_name):
        self.selected_winner = self.match.player_from_player_name(player_name)
        return self

    def in_sets(self, number_of_sets):
        self.in_number_sets = number_of_sets
        return self
