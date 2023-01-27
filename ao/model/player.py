from functools import partial
from ao.util import fn, error


def find_player(player, players):
    pl = fn.find(partial(_player_predicate, player), players)
    if not pl:
        raise error.ConfigException(f"{player.name} is either not found or is not in the game")
    return pl


def find_player_by_name(player_name, players):
    pl = fn.find(partial(_player_name_predicate, player_name), players)
    if not pl:
        raise error.ConfigException(f"Player with name {player_name} not found")
    return pl



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
