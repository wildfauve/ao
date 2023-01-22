from typing import Tuple, Callable
from functools import partial
import math

from . import error
from .util import fn, echo, identity


def find_event(event_name, events):
    return fn.find(partial(_event_name_predicate, event_name), events)


def find_player(player, players):
    pl = fn.find(partial(_player_predicate, player), players)
    if not pl:
        raise error.ConfigException
    return pl


def find_player_by_name(player_name, players):
    pl = fn.find(partial(_player_name_predicate, player_name), players)
    if not pl:
        raise error.ConfigException(f"Player with name {player_name} not found")
    return pl


def _event_name_predicate(event_name, event):
    return event_name == event.name


def _player_predicate(player_to_find, player):
    return player_to_find == player


def _player_name_predicate(player_name_to_find, player):
    if not player:
        return None
    return player_name_to_find in player.name


class Player:

    def __init__(self, name, seed=None):
        self.name = name
        self.seed = seed

    def seeding(self):
        if not self.seed:
            return "   "
        return str(self.seed).rjust(3)

    def __hash__(self):
        return hash((self.name,))

    def __eq__(self, other):
        return self.name == other.name


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

    def advance_winner(self, match):
        rd_id, mt_id = identity.split_match_id(match.match_id)
        if len(self.rounds) < rd_id + 1:
            # we are finished
            breakpoint()
        next_rd_match_number = self._next_rd_match_number(rd_id, mt_id)
        # This is the next round
        # rd_id is indexed from 1, so next rd in rounds list is the same number
        return self.rounds[rd_id].add_winner_to_match(next_rd_match_number, match.winner())

    def _next_rd_match_number(self, rd_id, this_rd_match_number):
        if len(self.rounds[rd_id].matches) == 1:
            return 1
        return math.ceil(this_rd_match_number / 2)

    def _build_draw(self, round_id, number_of_slots):
        self.rounds.append(Round(round_id,
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

    def add_winner_to_match(self, match_number, player):
        if len(self.matches) < match_number:
            raise error.ConfigException(f"Match number {match_number} over total matches {len(self.matches)}")

        mt = self._find_match(match_number)
        return mt.add_player(player)

    def build_match(self, match_number, player1, player2):
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
        return Match(self.round_id,
                     match_number,
                     self.games_best_of,
                     self.advance_winner_fn)

    def _match_number_predicate(self, number, match):
        return match.number == number


class Match:
    def __init__(self, round_id, match_number, best_of, advance_winner_fn: Callable):
        self.number = match_number
        self.match_id = f"{round_id}.{match_number}"
        self.advance_winner_fn = advance_winner_fn
        self.best_of = best_of
        self.player1 = None
        self.player2 = None
        self.scores = None
        self.sets = None
        self.match_winner = None

    def show(self):
        sp = len(self.match_id)
        echo.echo(f"{self.match_id}  -- {self.show_player(self.player1)}")
        echo.echo(f"{' ' * (sp + 4)} {self.show_player(self.player2)}")

    def show_player(self, player):
        if not player:
            return "?"
        return f"({player.seeding()}) {player.name} {self.show_set_and_winner(player)}"

    def show_set_and_winner(self, player):
        if not self.is_finished():
            return ""
        chevon = "<" if player == self.match_winner else ""
        return f"{' '.join([str(s) for s in self.scores[player]])}  {chevon}"

    def find_player_by_player(self, player):
        return find_player(player, [self.player1, self.player2])

    def player_from_player_name(self, player_name):
        if not self.has_draw():
            raise error.ConfigException("No draw has been set for match")
        return find_player_by_name(player_name, [self.player1, self.player2])

    def add_player(self, player):
        if self.player1 and self.player2:
            raise error.PlayerAdvanceError(
                f"Can't advance player, match {self.match_id} full with {self.player1.name} and {self.player2.name}")

        echo.echo(f"Add {player.name} to match {self.match_id}")

        if not self.player1:
            self.player1 = player
        else:
            self.player2 = player
        return self

    def add_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.scores = {self.player1: tuple(), self.player2: tuple()}
        self.sets = [Set(set_num, player1, player2) for set_num in range(1, self.best_of + 1)]
        return self

    def score(self, player, set_games: Tuple[int, int, int]):
        pl = find_player(player, [self.player1, self.player2])
        self.scores[pl] = set_games
        [self.sets[set_number].result_for_player(pl, set_games[set_number]) for set_number in range(len(set_games))]
        self.winner()
        return self

    def number_of_sets_played(self):
        return len(fn.remove_none([s.winner for s in self.sets]))

    def max_sets_played(self):
        return self.best_of == self.number_of_sets_played()

    def is_finished(self):
        if not self.scores:
            return False
        return all([len(sc) >= math.ceil(self.best_of / 2) for sc in self.scores.values()])

    def has_draw(self):
        return self.player1 and self.player2

    def winner(self):
        if not self.is_finished():
            return None
        if self.match_winner:
            return self.match_winner
        self.match_winner = self._determine_winner()

        echo.echo(f"""Match {self.match_id} Winner {self.match_winner.name} 
        {self.match_winner.name}: {self.show_set_and_winner(self.match_winner)}
        {self._losing_player().name}: {self.show_set_and_winner(self._losing_player())}""")

        self.advance_winner_fn(self)
        return self.match_winner

    def _losing_player(self):
        if not self.is_finished():
            return None
        if self.player1 == self.match_winner:
            return self.player2
        return self.player1

    def _determine_winner(self):
        winners_by_sets = fn.remove_none([s.winner for s in self.sets])
        if winners_by_sets.count(self.player1) > winners_by_sets.count(self.player2):
            return self.player1
        return self.player2


class Set:
    def __init__(self, number, player1, player2):
        self.number = number
        self.player1 = player1
        self.player2 = player2
        self.games = []
        self.winner = None

    def result_for_player(self, player, score):
        pl = find_player(player, [self.player1, self.player2])
        self.games.append((pl, score))
        if self._set_completed():
            self.winner = self._determine_winner()
        return self

    def _set_completed(self):
        return len([g for pl, g in self.games]) == 2

    def _determine_winner(self):
        pl1, pl1_games = self.games[0]
        pl2, pl2_games = self.games[1]
        if pl1_games == pl2_games:
            raise error.ConfigException
        return pl1 if pl1_games > pl2_games else pl2
