from . import player
from ao.util import error


class Set:
    def __init__(self, number, player1, player2):
        self.number = number
        self.player1 = player1
        self.player2 = player2
        self.games = []
        self.winner = None

    def result_for_player(self, for_player, score):
        pl = player.find_player(for_player, [self.player1, self.player2])
        self.games.append((pl, score))
        if self._set_completed():
            self.winner = self.determine_winner()
        return self

    def _set_completed(self):
        return len([g for pl, g in self.games]) == 2

    def determine_winner(self) -> bool:
        if not self.games or len(self.games) != 2:
            return None
        pl1, pl1_games = self.games[0]
        pl2, pl2_games = self.games[1]
        if pl1_games == pl2_games:
            raise error.ConfigException(f"{pl1.name} games {pl1_games} same as {pl2.name} games {pl2_games}")
        return pl1 if pl1_games > pl2_games else pl2
