from functools import partial
import math

from . import round, match
from ao.util import fn, error, echo


def find_event(event_name, events):
    return fn.find(partial(_event_name_predicate, event_name), events)


def _event_name_predicate(event_name, event):
    return event_name == event.name


class Event:

    def __init__(self, name, best_of):
        self.name = name
        self.number_of_matches = None
        self.best_of = best_of
        self.rounds = []

    def __hash__(self):
        return hash((self.name,))

    def __eq__(self, other):
        return self.name == other.name

    def draw_size(self, number_of_matches):
        self.number_of_matches = number_of_matches
        self._build_draw(1, number_of_matches)
        return self

    def init_draw(self, *match_ups):
        if len(match_ups) != self.number_of_matches:
            raise error.ConfigException
        [self._place_in_first_round(match_up) for match_up in match_ups]
        return self

    def for_round(self, round_id):
        rd = fn.find(partial(self._round_number_predicate, round_id), self.rounds)
        if not rd:
            raise error.ConfigException(f"Round id: {round_id} does not exist")
        return rd

    def advance_winner(self, for_match):
        rd_id, mt_id = match.split_match_id(for_match.match_id)
        if len(self.rounds) < rd_id + 1:
            # we are finished
            echo.echo(f"Event Finished: Winner {for_match.winner().name}")
            return self
        next_rd_match_number = self._next_rd_match_number(rd_id, mt_id)
        # This is the next round
        # rd_id is indexed from 1, so next rd in rounds list is the same number
        return self.rounds[rd_id].add_winner_to_match(next_rd_match_number, for_match.winner())

    def _next_rd_match_number(self, rd_id, this_rd_match_number):
        if len(self.rounds[rd_id].matches) == 1:
            return 1
        return math.ceil(this_rd_match_number / 2)

    def _build_draw(self, round_id, number_of_slots):
        self.rounds.append(round.Round(round_id,
                                       number_of_slots,
                                       self.best_of,
                                       self.advance_winner))
        if number_of_slots == 1:
            return self
        self._build_draw(round_id + 1, int(number_of_slots / 2))

    def _place_in_first_round(self, match_up):
        match_number, player1, player2 = match_up
        self.rounds[0].build_match(match_number, player1, player2)
        return self

    def _round_number_predicate(self, number, round):
        return round.round_id == number
