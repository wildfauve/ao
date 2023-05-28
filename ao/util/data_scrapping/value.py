from typing import Callable, List
from dataclasses import dataclass
import re

import bs4

from ao.players import players
from ao import model
from ao.util import fn


@dataclass
class Player:
    name: str
    player_module: Callable
    scores: List = None
    seed: str = None
    player_klass: model.Player = None

    def __post_init__(self):
        self.player_klass = players.match_player_by_name(self.name, self.player_module)
        if not self.player_klass:
            breakpoint()

    def player_entry_klass_name(self):
        return self.player_klass.klass_name

    def entry_definition(self):
        return f"{'':>12}({self.player_definition()}, {self._seed()}),\n"

    def score(self):
        """
        men.Medvedev, (6, 6, 6)
        """
        return f"{self.player_definition()}, ({', '.join(self.scores)})"

    def _seed(self):
        return f"'{self.seed}'" if self.seed else None

    def player_definition(self):
        return f"{self._player_mod_name()}.{self.player_entry_klass_name()}"

    def _player_mod_name(self):
        return self.player_module.__name__.split(".")[-1]


@dataclass
class MatchBlock:
    href: str
    match_id_fn: Callable
    html: bs4.element.Tag
    round: int
    draw_attr_name: str
    player1: Player
    player2: Player
    match_number: int = None
    match_id: int = None

    def __post_init__(self):
        self.match_id = self.match_id_fn(self.href)
        return self

    def set_match_number_from_1(self, min_match):
        self.match_number = (self.match_id - min_match) + 1
        return self

    def __hash__(self):
        return hash((self.href,))

    def __eq__(self, other):
        return self.href == other.href

    def entry_format(self):
        return self.player1.entry_definition() + self.player2.entry_definition()

    def match_format(self):
        return f"{'':>12}({self.match_number}, {self.player1.player_definition()}, {self.player2.player_definition()}),  \n"

    def results_format(self, spacing):
        """
        mens_singles.for_round(1).for_match(64).score(men.Seyboth_Wild, ()).score(men.Medvedev, ())
        :return:
        """
        return f"{spacing}draw.for_round({self.round}).for_match({self.match_number}).score({self.player1.score()}).score({self.player2.score()}),\n"
        pass

    def has_result(self):
        return self.player1.scores and self.player2.scores
