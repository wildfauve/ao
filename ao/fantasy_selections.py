import sys
import re
from ao.fantasy.teams import *
from ao.ontology.players import *

def apply(mens_singles, womens_singles):
    return [getattr(sys.modules[__name__], team_fn)(mens_singles, womens_singles) for team_fn in apply_functions_for_teams()]

def apply_functions_for_teams():
    return [f for f in dir(sys.modules[__name__]) if re.match("^team_", f)]

def team_gelato_giants(mens_singles, womens_singles):
    TeamGelatoGiants.draw(mens_singles).match("1.1").winner(Nishioka).in_sets(4)
    TeamGelatoGiants.draw(mens_singles).match("1.2").winner(Korda).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("1.5").winner(Rublev).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("1.6").winner(Djokovic).in_sets(4)
    TeamGelatoGiants.draw(mens_singles).match("1.7").winner(Wolf).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("1.8").winner(BautistaAgut).in_sets(4)

    TeamGelatoGiants.draw(womens_singles).match("1.1").winner(Swiatek).in_sets(2)
    TeamGelatoGiants.draw(womens_singles).match("1.2").winner(Gauff).in_sets(2)
    TeamGelatoGiants.draw(womens_singles).match("1.3").winner(Pegula).in_sets(2)
    TeamGelatoGiants.draw(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("1.5").winner(Pliskova).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("1.6").winner(Linette).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("1.8").winner(Vekic).in_sets(2)
    
    # Quarters
    TeamGelatoGiants.draw(mens_singles).match("2.1").winner(Khachanov).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(4)
    TeamGelatoGiants.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("2.4").winner(Shelton).in_sets(4)

    TeamGelatoGiants.draw(womens_singles).match("2.1").winner(Rybakina).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("2.2").winner(Pegula).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("2.3").winner(Pliskova).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("2.4").winner(Sabalenka).in_sets(2)
    
    # Semis
    TeamGelatoGiants.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(5)
    TeamGelatoGiants.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(3)
    
    TeamGelatoGiants.draw(womens_singles).match("3.1").winner(Azarenka).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(2)

    # Finals
    TeamGelatoGiants.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(3)

    TeamGelatoGiants.draw(womens_singles).match("4.1").winner(Sabalenka).in_sets(2)

    return TeamGelatoGiants


def team_polar_precision(mens_singles, womens_singles):
    TeamPolarPrecision.draw(mens_singles).match("1.1").winner(Nishioka).in_sets(5)
    TeamPolarPrecision.draw(mens_singles).match("1.2").winner(Korda).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("1.6").winner(DeMinaur).in_sets(5)
    TeamPolarPrecision.draw(mens_singles).match("1.7").winner("Shelton").in_sets(5)
    TeamPolarPrecision.draw(mens_singles).match("1.8").winner(BautistaAgut).in_sets(5)

    TeamPolarPrecision.draw(womens_singles).match("1.1").winner(Rybakina).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.2").winner(Gauff).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.3").winner(Pegula).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.4").winner(Zhu).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.5").winner(Zhang).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.7").winner(Bencic).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.8").winner(Vekic).in_sets(3)
    
    # Quarters
    TeamPolarPrecision.draw(mens_singles).match("2.1").winner(Khachanov).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(5)
    TeamPolarPrecision.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("2.4").winner(Shelton).in_sets(5)

    TeamPolarPrecision.draw(womens_singles).match("2.1").winner(Ostapenko).in_sets(2)
    TeamPolarPrecision.draw(womens_singles).match("2.2").winner(Azarenka).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("2.3").winner(Linette).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("2.4").winner(Sabalenka).in_sets(3)

    # Semis
    TeamPolarPrecision.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(4)

    TeamPolarPrecision.draw(womens_singles).match("3.1").winner(Azarenka).in_sets(2)
    TeamPolarPrecision.draw(womens_singles).match("3.2").winner(Linette).in_sets(3)

    # Finals
    TeamPolarPrecision.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(5)

    TeamPolarPrecision.draw(womens_singles).match("4.1").winner(Sabalenka).in_sets(3)

    return TeamPolarPrecision


def team_hero_hangouts(mens_singles, womens_singles):
    TeamHeroHangouts.draw(mens_singles).match("1.1").winner(Khachanov).in_sets(4)
    TeamHeroHangouts.draw(mens_singles).match("1.2").winner(Hurkacz).in_sets(4)
    TeamHeroHangouts.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("1.5").winner("Rune").in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("1.6").winner("Djokovic").in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("1.7").winner("Wolf").in_sets(4)
    TeamHeroHangouts.draw(mens_singles).match("1.8").winner(BautistaAgut).in_sets(5)

    TeamHeroHangouts.draw(womens_singles).match("1.1").winner(Swiatek).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.2").winner(Gauff).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.3").winner(Krejcikova).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.4").winner(Zhu).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.5").winner(Zhang).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.6").winner(Linette).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.8").winner(Fruhvirtova).in_sets(3)
    
    # Quarters
    TeamHeroHangouts.draw(mens_singles).match("2.1").winner(Korda).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("2.2").winner(Lehecka).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("2.4").winner(Paul).in_sets(5)

    TeamHeroHangouts.draw(womens_singles).match("2.1").winner(Ostapenko).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("2.2").winner(Azarenka).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("2.3").winner(Linette).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("2.4").winner(Vekic).in_sets(3)

    # Semis
    TeamHeroHangouts.draw(mens_singles).match("3.1").winner(Khachanov).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(3)

    TeamHeroHangouts.draw(womens_singles).match("3.1").winner(Rybakina).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(3)

    # Finals
    TeamHeroHangouts.draw(mens_singles).match("4.1").winner(Tsitsipas).in_sets(4)

    TeamHeroHangouts.draw(womens_singles).match("4.1").winner(Rybakina).in_sets(2)

    return TeamHeroHangouts


def team_bear_necessities(mens_singles, womens_singles):
    TeamBearNecessities.draw(mens_singles).match("1.1").winner(Khachanov).in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("1.2").winner(Korda).in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamBearNecessities.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(4)
    TeamBearNecessities.draw(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamBearNecessities.draw(mens_singles).match("1.6").winner(DeMinaur).in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("1.7").winner("Wolf").in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("1.8").winner("Paul").in_sets(5)

    TeamBearNecessities.draw(womens_singles).match("1.1").winner(Rybakina).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.2").winner(Ostapenko).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.3").winner(Krejcikova).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.5").winner(Pliskova).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.8").winner(Vekic).in_sets(3)
    
    # Quarters
    TeamBearNecessities.draw(mens_singles).match("2.1").winner(Khachanov).in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(3)
    TeamBearNecessities.draw(mens_singles).match("2.4").winner(Shelton).in_sets(5)

    TeamBearNecessities.draw(womens_singles).match("2.1").winner(Rybakina).in_sets(2)
    TeamBearNecessities.draw(womens_singles).match("2.2").winner(Pegula).in_sets(2)
    TeamBearNecessities.draw(womens_singles).match("2.3").winner(Pliskova).in_sets(2)
    TeamBearNecessities.draw(womens_singles).match("2.4").winner(Sabalenka).in_sets(3)

    # Semis
    TeamBearNecessities.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(4)
    TeamBearNecessities.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(3)

    TeamBearNecessities.draw(womens_singles).match("3.1").winner(Azarenka).in_sets(2)
    TeamBearNecessities.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(2)

    # Finals
    TeamBearNecessities.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(4)

    TeamBearNecessities.draw(womens_singles).match("4.1").winner(Sabalenka).in_sets(2)

    return TeamBearNecessities


def team_musical_bears(mens_singles, womens_singles):
    TeamMusicalBears.draw(mens_singles).match("1.1").winner(Khachanov).in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.2").winner(Korda).in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.4").winner("Lehecka").in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.6").winner("Djokovic").in_sets(3)
    TeamMusicalBears.draw(mens_singles).match("1.7").winner("Wolf").in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.8").winner("Paul").in_sets(4)

    TeamMusicalBears.draw(womens_singles).match("1.1").winner(Swiatek).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("1.2").winner(Ostapenko).in_sets(2)
    TeamMusicalBears.draw(womens_singles).match("1.3").winner(Pegula).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("1.4").winner(Azarenka).in_sets(2)
    TeamMusicalBears.draw(womens_singles).match("1.5").winner(Zhang).in_sets(2)
    TeamMusicalBears.draw(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("1.7").winner(Bencic).in_sets(2)
    TeamMusicalBears.draw(womens_singles).match("1.8").winner(Fruhvirtova).in_sets(2)
    
    # Quarters
    TeamMusicalBears.draw(mens_singles).match("2.1").winner(Korda).in_sets(5)
    TeamMusicalBears.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(3)
    TeamMusicalBears.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(3)
    TeamMusicalBears.draw(mens_singles).match("2.4").winner(Paul).in_sets(5)

    TeamMusicalBears.draw(womens_singles).match("2.1").winner(Ostapenko).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("2.2").winner(Pegula).in_sets(2)
    TeamMusicalBears.draw(womens_singles).match("2.3").winner(Linette).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("2.4").winner(Vekic).in_sets(3)

    # Semis
    TeamMusicalBears.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(5)
    TeamMusicalBears.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(3)

    TeamMusicalBears.draw(womens_singles).match("3.1").winner(Azarenka).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(3)

    # Finals
    TeamMusicalBears.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(4)

    TeamMusicalBears.draw(womens_singles).match("4.1").winner(Sabalenka).in_sets(3)

    return TeamMusicalBears


def team_fauve(mens_singles, womens_singles):
    TeamFauve.draw(mens_singles).match("1.1").winner("Khachanov").in_sets(3)
    TeamFauve.draw(mens_singles).match("1.2").winner("Hurkacz").in_sets(3)
    TeamFauve.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
    TeamFauve.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(4)
    TeamFauve.draw(mens_singles).match("1.5").winner("Rublev").in_sets(5)
    TeamFauve.draw(mens_singles).match("1.6").winner("Djokovic").in_sets(3)
    TeamFauve.draw(mens_singles).match("1.7").winner("Shelton").in_sets(4)
    TeamFauve.draw(mens_singles).match("1.8").winner("Bautista Agut").in_sets(5)

    TeamFauve.draw(womens_singles).match("1.1").winner(Swiatek).in_sets(2)
    TeamFauve.draw(womens_singles).match("1.2").winner(Ostapenko).in_sets(3)
    TeamFauve.draw(womens_singles).match("1.3").winner(Pegula).in_sets(2)
    TeamFauve.draw(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamFauve.draw(womens_singles).match("1.5").winner(Zhang).in_sets(3)
    TeamFauve.draw(womens_singles).match("1.6").winner(Garcia).in_sets(2)
    TeamFauve.draw(womens_singles).match("1.7").winner(Bencic).in_sets(3)
    TeamFauve.draw(womens_singles).match("1.8").winner(Fruhvirtova).in_sets(3)

    # Quarters
    TeamFauve.draw(mens_singles).match("2.1").winner(Khachanov).in_sets(4)
    TeamFauve.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(4)
    TeamFauve.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(3)
    TeamFauve.draw(mens_singles).match("2.4").winner(Shelton).in_sets(5)

    TeamFauve.draw(womens_singles).match("2.1").winner(Rybakina).in_sets(3)
    TeamFauve.draw(womens_singles).match("2.2").winner(Azarenka).in_sets(3)
    TeamFauve.draw(womens_singles).match("2.3").winner(Pliskova).in_sets(3)
    TeamFauve.draw(womens_singles).match("2.4").winner(Sabalenka).in_sets(2)

    # Semis
    TeamFauve.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(4)
    TeamFauve.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(4)

    TeamFauve.draw(womens_singles).match("3.1").winner(Azarenka).in_sets(2)
    TeamFauve.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(2)

    # Finals
    TeamFauve.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(3)

    TeamFauve.draw(womens_singles).match("4.1").winner(Sabalenka).in_sets(3)

    return TeamFauve


def team_clojo(mens_singles, womens_singles):
    TeamClojo.draw(mens_singles).match("1.1").winner("Khachanov").in_sets(5)
    TeamClojo.draw(mens_singles).match("1.2").winner("Korda").in_sets(4)
    TeamClojo.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamClojo.draw(mens_singles).match("1.4").winner("Lehecka").in_sets(4)
    TeamClojo.draw(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamClojo.draw(mens_singles).match("1.6").winner("Djokovic").in_sets(4)
    TeamClojo.draw(mens_singles).match("1.7").winner("Wolf").in_sets(3)
    TeamClojo.draw(mens_singles).match("1.8").winner("Paul").in_sets(3)

    TeamClojo.draw(womens_singles).match("1.1").winner(Swiatek).in_sets(3)
    TeamClojo.draw(womens_singles).match("1.2").winner(Gauff).in_sets(3)
    TeamClojo.draw(womens_singles).match("1.3").winner(Pegula).in_sets(3)
    TeamClojo.draw(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamClojo.draw(womens_singles).match("1.5").winner(Pliskova).in_sets(3)
    TeamClojo.draw(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamClojo.draw(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamClojo.draw(womens_singles).match("1.8").winner(Vekic).in_sets(2)

    # Quarters
    TeamClojo.draw(mens_singles).match("2.1").winner(Khachanov).in_sets(5)
    TeamClojo.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(3)
    TeamClojo.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(4)
    TeamClojo.draw(mens_singles).match("2.4").winner(Shelton).in_sets(4)

    TeamClojo.draw(womens_singles).match("2.1").winner(Rybakina).in_sets(2)
    TeamClojo.draw(womens_singles).match("2.2").winner(Azarenka).in_sets(2)
    TeamClojo.draw(womens_singles).match("2.3").winner(Pliskova).in_sets(2)
    TeamClojo.draw(womens_singles).match("2.4").winner(Sabalenka).in_sets(3)

    # Semis
    TeamClojo.draw(mens_singles).match("3.1").winner(Khachanov).in_sets(4)
    TeamClojo.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(3)

    TeamClojo.draw(womens_singles).match("3.1").winner(Rybakina).in_sets(3)
    TeamClojo.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(3)

    # Finals
    TeamClojo.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(4)

    TeamClojo.draw(womens_singles).match("4.1").winner(Rybakina).in_sets(3)

    return TeamClojo


def team_light_house(mens_singles, womens_singles):
    TeamLightHouse.draw(mens_singles).match("1.1").winner("Khachanov").in_sets(5)
    TeamLightHouse.draw(mens_singles).match("1.2").winner("Korda").in_sets(4)
    TeamLightHouse.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
    TeamLightHouse.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(3)
    TeamLightHouse.draw(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamLightHouse.draw(mens_singles).match("1.6").winner("Djokovic").in_sets(3)
    TeamLightHouse.draw(mens_singles).match("1.7").winner("Wolf").in_sets(5)
    TeamLightHouse.draw(mens_singles).match("1.8").winner("Paul").in_sets(4)

    TeamLightHouse.draw(womens_singles).match("1.1").winner(Swiatek).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("1.2").winner(Gauff).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("1.3").winner(Pegula).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("1.4").winner(Azarenka).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("1.5").winner(Pliskova).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("1.6").winner(Garcia).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("1.7").winner(Sabalenka).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("1.8").winner(Vekic).in_sets(3)
    
    # Quarters
    TeamLightHouse.draw(mens_singles).match("2.1").winner(Korda).in_sets(4)
    TeamLightHouse.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(4)
    TeamLightHouse.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(3)
    TeamLightHouse.draw(mens_singles).match("2.4").winner(Paul).in_sets(4)

    TeamLightHouse.draw(womens_singles).match("2.1").winner(Ostapenko).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("2.2").winner(Pegula).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("2.3").winner(Pliskova).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("2.4").winner(Sabalenka).in_sets(2)

    # Semis
    TeamLightHouse.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(5)
    TeamLightHouse.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(4)

    TeamLightHouse.draw(womens_singles).match("3.1").winner(Rybakina).in_sets(2)
    TeamLightHouse.draw(womens_singles).match("3.2").winner(Linette).in_sets(3)

    # Finals
    TeamLightHouse.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(5)

    TeamLightHouse.draw(womens_singles).match("4.1").winner(Rybakina).in_sets(2)

    return TeamLightHouse
