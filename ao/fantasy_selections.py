import sys
from .teams import *
from .players import *

def apply(mens_singles, womens_singles):
    return [getattr(sys.modules[__name__], team_fn)(mens_singles, womens_singles) for team_fn in apply_functions_for_teams()]

def apply_functions_for_teams():
    return [f for f in dir(sys.modules[__name__]) if "team_" in f]

def team_gelato_giants(mens_singles, womens_singles):
    TeamGelatoGiants.event(mens_singles).match("1.1").winner(Nishioka).in_sets(4)
    TeamGelatoGiants.event(mens_singles).match("1.2").winner(Korda).in_sets(3)
    TeamGelatoGiants.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(3)
    TeamGelatoGiants.event(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(3)
    TeamGelatoGiants.event(mens_singles).match("1.5").winner(Rublev).in_sets(3)
    TeamGelatoGiants.event(mens_singles).match("1.6").winner(Djokovic).in_sets(4)
    TeamGelatoGiants.event(mens_singles).match("1.7").winner(Wolf).in_sets(3)
    TeamGelatoGiants.event(mens_singles).match("1.8").winner(BautistaAgut).in_sets(4)

    TeamGelatoGiants.event(womens_singles).match("1.1").winner(Swiatek).in_sets(2)
    TeamGelatoGiants.event(womens_singles).match("1.2").winner(Gauff).in_sets(2)
    TeamGelatoGiants.event(womens_singles).match("1.3").winner(Pegula).in_sets(2)
    TeamGelatoGiants.event(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamGelatoGiants.event(womens_singles).match("1.5").winner(Pliskova).in_sets(3)
    TeamGelatoGiants.event(womens_singles).match("1.6").winner(Linette).in_sets(3)
    TeamGelatoGiants.event(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamGelatoGiants.event(womens_singles).match("1.8").winner(Vekic).in_sets(2)

    return TeamGelatoGiants


def team_polar_precision(mens_singles, womens_singles):
    TeamPolarPrecision.event(mens_singles).match("1.1").winner(Nishioka).in_sets(5)
    TeamPolarPrecision.event(mens_singles).match("1.2").winner(Korda).in_sets(4)
    TeamPolarPrecision.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamPolarPrecision.event(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(4)
    TeamPolarPrecision.event(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamPolarPrecision.event(mens_singles).match("1.6").winner(DeMinaur).in_sets(5)
    TeamPolarPrecision.event(mens_singles).match("1.7").winner("Shelton").in_sets(5)
    TeamPolarPrecision.event(mens_singles).match("1.8").winner(BautistaAgut).in_sets(5)

    TeamPolarPrecision.event(womens_singles).match("1.1").winner(Rybakina).in_sets(3)
    TeamPolarPrecision.event(womens_singles).match("1.2").winner(Gauff).in_sets(3)
    TeamPolarPrecision.event(womens_singles).match("1.3").winner(Pegula).in_sets(3)
    TeamPolarPrecision.event(womens_singles).match("1.4").winner(Zhu).in_sets(3)
    TeamPolarPrecision.event(womens_singles).match("1.5").winner(Zhang).in_sets(3)
    TeamPolarPrecision.event(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamPolarPrecision.event(womens_singles).match("1.7").winner(Bencic).in_sets(3)
    TeamPolarPrecision.event(womens_singles).match("1.8").winner(Vekic).in_sets(3)

    return TeamPolarPrecision


def team_hero_hangouts(mens_singles, womens_singles):
    TeamHeroHangouts.event(mens_singles).match("1.1").winner(Khachanov).in_sets(4)
    TeamHeroHangouts.event(mens_singles).match("1.2").winner(Hurkacz).in_sets(4)
    TeamHeroHangouts.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
    TeamHeroHangouts.event(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(5)
    TeamHeroHangouts.event(mens_singles).match("1.5").winner("Rune").in_sets(5)
    TeamHeroHangouts.event(mens_singles).match("1.6").winner("Djokovic").in_sets(5)
    TeamHeroHangouts.event(mens_singles).match("1.7").winner("Wolf").in_sets(4)
    TeamHeroHangouts.event(mens_singles).match("1.8").winner(BautistaAgut).in_sets(5)

    TeamHeroHangouts.event(womens_singles).match("1.1").winner(Swiatek).in_sets(3)
    TeamHeroHangouts.event(womens_singles).match("1.2").winner(Gauff).in_sets(3)
    TeamHeroHangouts.event(womens_singles).match("1.3").winner(Krejcikova).in_sets(3)
    TeamHeroHangouts.event(womens_singles).match("1.4").winner(Zhu).in_sets(3)
    TeamHeroHangouts.event(womens_singles).match("1.5").winner(Zhang).in_sets(3)
    TeamHeroHangouts.event(womens_singles).match("1.6").winner(Linette).in_sets(3)
    TeamHeroHangouts.event(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamHeroHangouts.event(womens_singles).match("1.8").winner(Fruhvirtova).in_sets(3)

    return TeamHeroHangouts


def team_bear_necessities(mens_singles, womens_singles):
    TeamBearNecessities.event(mens_singles).match("1.1").winner(Khachanov).in_sets(5)
    TeamBearNecessities.event(mens_singles).match("1.2").winner(Korda).in_sets(5)
    TeamBearNecessities.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamBearNecessities.event(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(4)
    TeamBearNecessities.event(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamBearNecessities.event(mens_singles).match("1.6").winner(DeMinaur).in_sets(5)
    TeamBearNecessities.event(mens_singles).match("1.7").winner("Wolf").in_sets(5)
    TeamBearNecessities.event(mens_singles).match("1.8").winner("Paul").in_sets(5)

    TeamBearNecessities.event(womens_singles).match("1.1").winner(Rybakina).in_sets(3)
    TeamBearNecessities.event(womens_singles).match("1.2").winner(Ostapenko).in_sets(3)
    TeamBearNecessities.event(womens_singles).match("1.3").winner(Krejcikova).in_sets(3)
    TeamBearNecessities.event(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamBearNecessities.event(womens_singles).match("1.5").winner(Pliskova).in_sets(3)
    TeamBearNecessities.event(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamBearNecessities.event(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamBearNecessities.event(womens_singles).match("1.8").winner(Vekic).in_sets(3)

    return TeamBearNecessities


def team_musical_bears(mens_singles, womens_singles):
    TeamMusicalBears.event(mens_singles).match("1.1").winner(Khachanov).in_sets(4)
    TeamMusicalBears.event(mens_singles).match("1.2").winner(Korda).in_sets(4)
    TeamMusicalBears.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamMusicalBears.event(mens_singles).match("1.4").winner("Lehecka").in_sets(4)
    TeamMusicalBears.event(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamMusicalBears.event(mens_singles).match("1.6").winner("Djokovic").in_sets(3)
    TeamMusicalBears.event(mens_singles).match("1.7").winner("Wolf").in_sets(4)
    TeamMusicalBears.event(mens_singles).match("1.8").winner("Paul").in_sets(4)

    TeamMusicalBears.event(womens_singles).match("1.1").winner(Swiatek).in_sets(3)
    TeamMusicalBears.event(womens_singles).match("1.2").winner(Ostapenko).in_sets(2)
    TeamMusicalBears.event(womens_singles).match("1.3").winner(Pegula).in_sets(3)
    TeamMusicalBears.event(womens_singles).match("1.4").winner(Azarenka).in_sets(2)
    TeamMusicalBears.event(womens_singles).match("1.5").winner(Zhang).in_sets(2)
    TeamMusicalBears.event(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamMusicalBears.event(womens_singles).match("1.7").winner(Bencic).in_sets(2)
    TeamMusicalBears.event(womens_singles).match("1.8").winner(Fruhvirtova).in_sets(2)

    return TeamMusicalBears


def team_fauve(mens_singles, womens_singles):
    TeamFauve.event(mens_singles).match("1.1").winner("Khachanov").in_sets(3)
    TeamFauve.event(mens_singles).match("1.2").winner("Hurkacz").in_sets(3)
    TeamFauve.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
    TeamFauve.event(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(4)
    TeamFauve.event(mens_singles).match("1.5").winner("Rublev").in_sets(5)
    TeamFauve.event(mens_singles).match("1.6").winner("Djokovic").in_sets(3)
    TeamFauve.event(mens_singles).match("1.7").winner("Shelton").in_sets(4)
    TeamFauve.event(mens_singles).match("1.8").winner("Bautista Agut").in_sets(5)

    TeamFauve.event(womens_singles).match("1.1").winner(Swiatek).in_sets(2)
    TeamFauve.event(womens_singles).match("1.2").winner(Ostapenko).in_sets(3)
    TeamFauve.event(womens_singles).match("1.3").winner(Pegula).in_sets(2)
    TeamFauve.event(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamFauve.event(womens_singles).match("1.5").winner(Zhang).in_sets(3)
    TeamFauve.event(womens_singles).match("1.6").winner(Garcia).in_sets(2)
    TeamFauve.event(womens_singles).match("1.7").winner(Bencic).in_sets(3)
    TeamFauve.event(womens_singles).match("1.8").winner(Fruhvirtova).in_sets(3)

    return TeamFauve


def team_clojo(mens_singles, womens_singles):
    TeamClojo.event(mens_singles).match("1.1").winner("Khachanov").in_sets(5)
    TeamClojo.event(mens_singles).match("1.2").winner("Korda").in_sets(4)
    TeamClojo.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamClojo.event(mens_singles).match("1.4").winner("Lehecka").in_sets(4)
    TeamClojo.event(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamClojo.event(mens_singles).match("1.6").winner("Djokovic").in_sets(4)
    TeamClojo.event(mens_singles).match("1.7").winner("Wolf").in_sets(3)
    TeamClojo.event(mens_singles).match("1.8").winner("Paul").in_sets(3)

    TeamClojo.event(womens_singles).match("1.1").winner(Swiatek).in_sets(3)
    TeamClojo.event(womens_singles).match("1.2").winner(Gauff).in_sets(3)
    TeamClojo.event(womens_singles).match("1.3").winner(Pegula).in_sets(3)
    TeamClojo.event(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamClojo.event(womens_singles).match("1.5").winner(Pliskova).in_sets(3)
    TeamClojo.event(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamClojo.event(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamClojo.event(womens_singles).match("1.8").winner(Vekic).in_sets(2)

    return TeamClojo


def team_light_house(mens_singles, womens_singles):
    TeamLightHouse.event(mens_singles).match("1.1").winner("Khachanov").in_sets(5)
    TeamLightHouse.event(mens_singles).match("1.2").winner("Korda").in_sets(4)
    TeamLightHouse.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
    TeamLightHouse.event(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(3)
    TeamLightHouse.event(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamLightHouse.event(mens_singles).match("1.6").winner("Djokovic").in_sets(3)
    TeamLightHouse.event(mens_singles).match("1.7").winner("Wolf").in_sets(5)
    TeamLightHouse.event(mens_singles).match("1.8").winner("Paul").in_sets(4)

    TeamLightHouse.event(womens_singles).match("1.1").winner(Swiatek).in_sets(2)
    TeamLightHouse.event(womens_singles).match("1.2").winner(Gauff).in_sets(2)
    TeamLightHouse.event(womens_singles).match("1.3").winner(Pegula).in_sets(2)
    TeamLightHouse.event(womens_singles).match("1.4").winner(Azarenka).in_sets(2)
    TeamLightHouse.event(womens_singles).match("1.5").winner(Pliskova).in_sets(2)
    TeamLightHouse.event(womens_singles).match("1.6").winner(Garcia).in_sets(2)
    TeamLightHouse.event(womens_singles).match("1.7").winner(Sabalenka).in_sets(2)
    TeamLightHouse.event(womens_singles).match("1.8").winner(Vekic).in_sets(3)

    return TeamLightHouse
