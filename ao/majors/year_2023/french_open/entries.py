from typing import Tuple, List, Optional
from ao import model
from ao.players import atp_players, wta_players

WC = None

def mens_singles_entries() -> List[Tuple[model.player, Optional[int]]]:
    """
    A list of player entries into the Mens Single Draw

    (players.<PlayerName>, seed)

    """
    return [
        (atp_players.Alcaraz, 1),
        (atp_players.OConnell, None),
        (atp_players.Daniel, None),
        (atp_players.Arnaldi, None),
        (atp_players.Galan, None),
        (atp_players.Nakashima, None),
        (atp_players.Shapovalov, 26),
        (atp_players.Musetti, 17),
        (atp_players.Ymer_Mikael, None),
        (atp_players.Shevchenko, None),
        (atp_players.Otte, None),
        (atp_players.Paire, WC),
        (atp_players.Norrie, 14),
        (atp_players.Auger_Aliassime, 10),
        (atp_players.Fognini, None),
        (atp_players.Kubler, None),
        (atp_players.Cressy, None),
        (atp_players.McDonald, None),
        (atp_players.Korda, 24),
        (atp_players.Miralles, 32),
        (atp_players.Schwartzman, None),
        (atp_players.Isner, None),
        (atp_players.Borges, None),
        (atp_players.Baena, None),
        (atp_players.Vesely, None),
        (atp_players.Tsitsipas, 5),
        (atp_players.Djokovic, 3),
        (atp_players.Kovacevic, None),
        (atp_players.Fucsovics, None),
        (atp_players.Grenier, WC),
        (atp_players.Assche, None),
        (atp_players.Cecchinato, None),
        (atp_players.Fils, WC),
        (atp_players.Fokina, 29),
        (atp_players.Agut, 19),
        (atp_players.Wu, None),
        (atp_players.Varillas, None),
        (atp_players.Griekspoor, None),
        (atp_players.Goffin, None),
        (atp_players.Hurkacz, 13),
        (atp_players.Khachanov, 11),
        (atp_players.Lestienne, None),
        (atp_players.Kypson, WC),
        (atp_players.Wawrinka, None),
        (atp_players.Ramos_Vinolas, None),
        (atp_players.Kokkinakis, WC),
        (atp_players.Evans, 20),
        (atp_players.Shelton, 30),
        (atp_players.Sonego, None),
        (atp_players.Mannarino, None),
        (atp_players.Humbert, None),
        (atp_players.Cazaux, WC),
        (atp_players.Moutet, None),
        (atp_players.Djere, None),
        (atp_players.Rublev, 7),
        (atp_players.Rune, 6),
        (atp_players.Eubanks, None),
        (atp_players.Monfils, WC),
        (atp_players.Baez, None),
        (atp_players.Perricard, WC),
        (atp_players.Kecmanovic, 31),
        (atp_players.Cerundolo_Francisco, 23),
        (atp_players.Munar, None),
        (atp_players.Monteiro, None),
        (atp_players.Bonzi, None),
        (atp_players.Gasquet, None),
        (atp_players.Rinderknech, None),
        (atp_players.Mmoh, None),
        (atp_players.Fritz, 9),
        (atp_players.Paul, 16),
        (atp_players.Jarry, None),
        (atp_players.Dellien, None),
        (atp_players.Giron, None),
        (atp_players.Lehecka, None),
        (atp_players.Struff, 21),
        (atp_players.Zandschulp, 25),
        (atp_players.Zhang_Zhizhen, None),
        (atp_players.Lajovic, None),
        (atp_players.Bublik, None),
        (atp_players.Ruud, 4),
        (atp_players.Sinner, 8),
        (atp_players.Muller, None),
        (atp_players.Altmaier, None),
        (atp_players.Huesler, None),
        (atp_players.Ruusuvuori, None),
        (atp_players.Barrere, None),
        (atp_players.Dimitrov, 28),
        (atp_players.Zverev, 22),
        (atp_players.Harris, None),
        (atp_players.Gaston, WC),
        (atp_players.Molcan, None),
        (atp_players.Popyrin, None),
        (atp_players.Krajinovic, None),
        (atp_players.Tiafoe, 12),
        (atp_players.Coric, 15),
        (atp_players.Coria, None),
        (atp_players.Thiem, None),
        (atp_players.Cachin, None),
        (atp_players.Draper, None),
        (atp_players.Etcheverry, None),
        (atp_players.Ivashka, None),
        (atp_players.Minaur, 18),
        (atp_players.Nishioka, 27),
        (atp_players.Wolf, None),
        (atp_players.Purcell, None),
        (atp_players.Thompson, None),
        (atp_players.Halys, None),
        (atp_players.Pella, None),
        (atp_players.Medvedev, 2),
    ]


def womens_singles_entries() -> List[Tuple[model.player, Optional[int]]]:
    """
    A list of player entries into the Womens Single Draw

    (players.<PlayerName>, seed)

    """

    return [
    ]
