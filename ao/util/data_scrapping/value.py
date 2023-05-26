from typing import Callable
from dataclasses import dataclass
import bs4

name_split_char = "."


@dataclass
class Player:
    name: str
    player_module: Callable
    seed: str = None

    def player_entry_klass_name(self):
        formatted_name = self._format_klass_name()
        if formatted_name not in dir(self.player_module):
            return f"{formatted_name}--FIXME"
        return formatted_name

    def _format_klass_name(self):
        return self.name.rstrip().split(name_split_char)[-1].replace("-", "_").replace("'", "")

    def entry_definition(self):
        return f"{'':>12}({self.player_definition()}, {self.seed if self.seed else 'None'}),\n"

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
