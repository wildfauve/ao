from typing import Callable
from functools import partial

from ao.model import match, entry
from ao.util import fn, error, echo


class Round:
    def __init__(self, round_id, number_match_slots, games_best_of, advance_winner_fn: Callable):
        self.number_match_slots = number_match_slots
        self.name = f"Round of {number_match_slots}"
        self.round_id = round_id
        self.matches = []
        self.games_best_of = games_best_of
        self.advance_winner_fn = advance_winner_fn
        self._build_match_slots()

    def show(self):
        echo.echo(f"Round: {self.round_id}")
        echo.echo(f"Matches:")
        for match in self.matches:
            match.show()

    def result_template(self, event_name):
        return [match.result_template(event_name, self.round_id) for match in self.matches]

    def add_winner_to_match(self, match_number, player):
        if len(self.matches) < match_number:
            raise error.ConfigException(f"Match number {match_number} over total matches {len(self.matches)}")

        mt = self._find_match(match_number)
        return mt.add_player(player)

    def build_match(self, match_number, player1: entry.Entry, player2: entry.Entry):
        mt = self._find_match(match_number)
        mt.add_players(player1, player2)
        return self

    def for_match(self, match_number):
        return self._find_match(match_number)

    def _find_match(self, match_number):
        mt = fn.find(partial(self._match_number_predicate, match_number), self.matches)
        if not mt:
            raise error.ConfigException
        return mt

    def _build_match_slots(self):
        [self.matches.append(self._match_constructor(match_number)) for match_number in
         range(1, self.number_match_slots + 1)]
        return self

    def _match_constructor(self, match_number):
        return match.Match(self.round_id,
                           match_number,
                           self.games_best_of,
                           self.advance_winner_fn)

    def _match_number_predicate(self, number, match):
        return match.number == number
