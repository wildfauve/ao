from .players import *


def add_results(events):
    mens_singles, womens_singles = get_events(events)
    results(mens_singles, womens_singles)
    return mens_singles, womens_singles


def get_events(events):
    return events['MensSingles'], events['WomensSingles']


def results(mens_singles, womens_singles):
    # 4th Round Results
    mens_singles.for_round(1).for_match(1).score(Khachanov, (6, 6, 7)).score(Nishioka, (0, 0, 6))
    mens_singles.for_round(1).for_match(2).score(Korda, (3, 6, 6, 1, 7)).score(Hurkacz, (6, 2, 3, 6, 6))
    mens_singles.for_round(1).for_match(3).score(Tsitsipas, (6, 6, 3, 4, 6)).score(Sinner, (4, 4, 6, 6, 3))
    mens_singles.for_round(1).for_match(4).score(Lehecka, (4, 6, 7, 7)).score(Auger_Aliassime, (6, 3, 6, 6))
    mens_singles.for_round(1).for_match(5).score(Rublev, ()).score(Rune, ())
    mens_singles.for_round(1).for_match(6).score(DeMinaur, ()).score(Djokovic, ())
    mens_singles.for_round(1).for_match(7).score(Shelton, ()).score(Wolf, ())
    mens_singles.for_round(1).for_match(8).score(BautistaAgut, ()).score(Paul, ())

    womens_singles.for_round(1).for_match(1).score(Rybakina, (6, 6)).score(Swiatek, (4, 4))
    womens_singles.for_round(1).for_match(2).score(Ostapenko, (7, 6)).score(Gauff, (6, 4))
    womens_singles.for_round(1).for_match(3).score(Pegula, (7, 6)).score(Krejcikova, (5, 2))
    womens_singles.for_round(1).for_match(4).score(Azarenka, (4, 6, 6)).score(Zhu, (6, 1, 4))
    womens_singles.for_round(1).for_match(5).score(Pliskova, ()).score(Zhang, ())
    womens_singles.for_round(1).for_match(6).score(Linette, ()).score(Garcia, ())
    womens_singles.for_round(1).for_match(7).score(Sabalenka, (7, 6)).score(Bencic, (5, 2))
    womens_singles.for_round(1).for_match(8).score(Vekic, ()).score(Fruhvirtova, ())

    # Quarter Final Results

