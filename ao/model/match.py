from typing import Callable, Tuple
import math

from . import player, set
from ao.util import fn, error, echo


def split_match_id(match_id):
    return [int(ident) for ident in match_id.split(".")]


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

    def result_template(self, event_name, round_number):
        match_part = f"{event_name}.for_round({round_number}).for_match({self.number})"
        if self.has_draw():
            score_part = f"score({self.player1.name}, ()).score({self.player2.name}, ())"
        else:
            score_part = f"score(?, ()).score(?, ())"
        return f"{match_part}.{score_part}"

    def find_player_by_player(self, for_player):
        return player.find_player(for_player, [self.player1, self.player2])

    def player_from_player_name(self, player_name):
        if not self.has_draw():
            raise error.ConfigException("No draw has been set for match")
        return player.find_player_by_name(player_name, [self.player1, self.player2])

    def add_player(self, player):
        if self.player1 and self.player2:
            raise error.PlayerAdvanceError(
                f"Can't advance player, match {self.match_id} full with {self.player1.name} and {self.player2.name}")

        echo.echo(f"Add {player.name} to match {self.match_id}")

        if not self.player1:
            self.player1 = player
            self._init_scores(player)
        else:
            self.player2 = player
            self._init_scores(player)
        return self

    def add_players(self, player1, player2):
        self.player1 = player1
        self._init_scores(player1)
        self.player2 = player2
        self._init_scores(player2)
        return self

    def score(self, for_player, set_games: Tuple[int, int, int]):
        pl = player.find_player(for_player, [self.player1, self.player2])
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

    def _init_scores(self, for_player):
        if not self.scores:
            self.scores = {for_player: tuple()}
        else:
            self.scores[for_player] = tuple()
        if self.has_draw():
            self.sets = [set.Set(set_num, self.player1, self.player2) for set_num in range(1, self.best_of + 1)]
        return self

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
