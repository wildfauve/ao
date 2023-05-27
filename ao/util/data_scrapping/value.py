from typing import Callable
from dataclasses import dataclass
import bs4

from ao.players import players
from ao import model
from ao.util import fn


@dataclass
class Player:
    name: str
    player_module: Callable
    seed: str = None
    player_klass: model.Player = None

    def __post_init__(self):
        self.player_klass = players.match_player_by_name(self.name, self.player_module)

    def player_entry_klass_name(self):
        if self.player_klass:
            return self.player_klass.klass_name
        breakpoint()

    def entry_definition(self):
        return f"{'':>12}({self.player_definition()}, {self._seed()}),\n"

    def _seed(self):
        return f"'{self.seed}'" if self.seed else None

    def player_definition(self):
        return f"{self._player_mod_name()}.{self.player_entry_klass_name()}"

    def _player_mod_name(self):
        return self.player_module.__name__.split(".")[-1]


@dataclass
class MatchBlock:
    href: str
    html: bs4.element.Tag
    round: str
    player1: Player
    player2: Player

    def __hash__(self):
        return hash((self.href,))

    def __eq__(self, other):
        return self.href == other.href

    def entry_format(self):
        return self.player1.entry_definition() + self.player2.entry_definition()

    def _match_id(self, match_number):
        return int(match_number) + 1

    def match_format(self, match_number):
        return f"{'':>12}({self._match_id(match_number)}, {self.player1.player_definition()}, {self.player2.player_definition()}),  \n"
