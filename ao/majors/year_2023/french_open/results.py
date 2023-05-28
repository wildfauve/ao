from typing import List
from ao.players import wta_players, atp_players
from ao import model


def add_results(draws: List[model.Draw]):
    mens_singles = model.find_draw_by_cls(model.MensSingles, draws)
    womens_singles = model.find_draw_by_cls(model.WomensSingles, draws)
    mens_singles_results(mens_singles)
    womens_singles_results(womens_singles)
    return mens_singles, womens_singles


def mens_singles_results(draw):
    return [
        draw.for_round(1).for_match(3).score(atp_players.Arnaldi, (2, 6, 6, 6)).score(atp_players.Galan, (6, 3, 0, 2)),
        draw.for_round(1).for_match(5).score(atp_players.Musetti, (7, 6, 6)).score(atp_players.Ymer_Mikael, (5, 2, 4)),
        draw.for_round(1).for_match(6).score(atp_players.Shevchenko, (7, 4, 6, 7)).score(atp_players.Otte,
                                                                                         (5, 6, 1, 6)),
        draw.for_round(1).for_match(7).score(atp_players.Pouille, (6, 6, 6)).score(atp_players.Rodionov, (2, 4, 3)),
        draw.for_round(1).for_match(10).score(atp_players.Kubler, (1, 6, 6, 3, 6)).score(atp_players.Diaz_Acosta,
                                                                                         (6, 3, 4, 6, 1)),
        draw.for_round(1).for_match(11).score(atp_players.Ofner, (6, 7, 6)).score(atp_players.Cressy, (4, 6, 2)),
        draw.for_round(1).for_match(12).score(atp_players.Mcdonald, (4, 5, 4)).score(atp_players.Korda, (6, 7, 6)),
        draw.for_round(1).for_match(14).score(atp_players.Isner, (4, 7, 6, 6, 6)).score(atp_players.Borges,
                                                                                        (6, 5, 7, 4, 7)),
        draw.for_round(1).for_match(15).score(atp_players.Carballes_Baena, (7, 6, 6)).score(atp_players.Nava,
                                                                                            (6, 3, 2)),
        draw.for_round(1).for_match(16).score(atp_players.Vesely, (5, 3, 6, 6)).score(atp_players.Tsitsipas,
                                                                                      (7, 6, 4, 7)),
        draw.for_round(1).for_match(18).score(atp_players.Fucsovics, (6, 5, 6, 6)).score(atp_players.Grenier,
                                                                                         (3, 7, 1, 3)),
        draw.for_round(1).for_match(23).score(atp_players.Martinez, (4, 6, 6, 5, 3)).score(atp_players.Griekspoor,
                                                                                           (6, 2, 0, 7, 6)),
        draw.for_round(1).for_match(24).score(atp_players.Goffin, (3, 7, 4, 6, 4)).score(atp_players.Hurkacz,
                                                                                         (6, 5, 6, 2, 6)),
        draw.for_round(1).for_match(25).score(atp_players.Khachanov, (3, 1, 6, 6, 6)).score(atp_players.Lestienne,
                                                                                            (6, 6, 2, 1, 3)),
        draw.for_round(1).for_match(26).score(atp_players.Kypson, (3, 2, 6, 1)).score(atp_players.Albot, (6, 6, 4, 6)),
        draw.for_round(1).for_match(28).score(atp_players.Kokkinakis, (6, 6, 6)).score(atp_players.Evans, (4, 4, 4)),
        draw.for_round(1).for_match(29).score(atp_players.Shelton, (4, 6, 3, 3)).score(atp_players.Sonego,
                                                                                       (6, 3, 6, 6)),
        draw.for_round(1).for_match(30).score(atp_players.Mannarino, (3, 3, 1)).score(atp_players.Humbert, (6, 6, 6)),
        draw.for_round(1).for_match(31).score(atp_players.Cazaux, (1, 3, 6, 4)).score(atp_players.Moutet, (6, 6, 4, 6)),
        draw.for_round(1).for_match(32).score(atp_players.Djere, (1, 6, 3, 4)).score(atp_players.Rublev, (6, 3, 6, 6)),

    ]


def womens_singles_results(draw):
    return [
        draw.for_round(1).for_match(33).score(wta_players.Sakkari, (6, 5)).score(wta_players.Muchova, (7, 7)),
        draw.for_round(1).for_match(34).score(wta_players.Podoroska, (6, 6)).score(wta_players.Ponchet, (0, 2)),
        draw.for_round(1).for_match(35).score(wta_players.Errani, (3, 6, 6)).score(wta_players.Teichmann, (6, 4, 2)),
        draw.for_round(1).for_match(36).score(wta_players.Bondar, (4, 2)).score(wta_players.Begu, (6, 6)),
        draw.for_round(1).for_match(37).score(wta_players.Linette, (3, 6, 3)).score(wta_players.Fernandez, (6, 1, 6)),
        draw.for_round(1).for_match(38).score(wta_players.Tauson, (6, 6)).score(wta_players.Sasnovich, (2, 0)),
        draw.for_round(1).for_match(39).score(wta_players.Jeanjean, (6, 6, 6)).score(wta_players.Birrell, (4, 7, 3)),
        draw.for_round(1).for_match(41).score(wta_players.Samsonova, (6, 6)).score(wta_players.Volynets, (0, 1)),
        draw.for_round(1).for_match(43).score(wta_players.Sherif, (6, 6)).score(wta_players.Brengle, (3, 1)),
        draw.for_round(1).for_match(44).score(wta_players.Townsend, (1, 2)).score(wta_players.Potapova, (6, 6)),
        draw.for_round(1).for_match(45).score(wta_players.Mertens, (6, 6)).score(wta_players.Hruncakova, (1, 4)),
        draw.for_round(1).for_match(47).score(wta_players.Cornet, (3, 4)).score(wta_players.Giorgi, (6, 6)),
        draw.for_round(1).for_match(48).score(wta_players.Collins, (4, 2)).score(wta_players.Pegula, (6, 6)),
        draw.for_round(1).for_match(51).score(wta_players.Parrizas_Diaz, (6, 2, 4)).score(wta_players.Hunter,
                                                                                          (4, 6, 6)),
        draw.for_round(1).for_match(56).score(wta_players.Niemeier, (3, 2)).score(wta_players.Kasatkina, (6, 3)),
        draw.for_round(1).for_match(60).score(wta_players.Zidansek, (3, 1)).score(wta_players.Zheng, (6, 6)),
        draw.for_round(1).for_match(61).score(wta_players.Zhang_Shuai, (1, 1)).score(wta_players.Frech, (6, 6)),
        draw.for_round(1).for_match(62).score(wta_players.Bejlek, (0, 3)).score(wta_players.Rakhimova, (6, 6)),
        draw.for_round(1).for_match(63).score(wta_players.Udvardy, (7, 3, 1)).score(wta_players.Shymanovich, (6, 6, 6)),
        draw.for_round(1).for_match(64).score(wta_players.Kostyuk, (3, 2)).score(wta_players.Sabalenka, (6, 6)),

    ]
