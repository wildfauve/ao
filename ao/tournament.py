from . import match
from .players import *
from .teams import *

# Mens Singles

mens_singles = (match.Event("MensSingles", 5)
                .draw_size(number_of_matches=8)
                .init_draw((1, Nishioka, Khachanov),
                           (2, Hurkacz, Korda),
                           (3, Tsitsipas, Sinner),
                           (4, Lehecka, Auger_Aliassime),
                           (5, Rublev, Rune),
                           (6, deMinaur, Djokovic),
                           (7, Shelton, Wolf),
                           (8, BautistaAgut, Paul)))

womens_singles = (match.Event("WomensSingles", 3)
                  .draw_size(number_of_matches=8)
                  .init_draw((1, Swiatek, Rybakina),
                             (2, Ostapenko, Gauff),
                             (3, Pegula, Krejcikova),
                             (4, Azarenka, Zhu),
                             (5, Pliskova, Zhang),
                             (6, Linette, Garcia),
                             (7, Sabalenka, Bencic),
                             (8, Vekic, Fruhvirtova)))


# TeamGelatoGiants
TeamGelatoGiants.event(mens_singles).match("1.1").winner(Nishioka).in_sets(4)
TeamGelatoGiants.event(mens_singles).match("1.2").winner(Korda).in_sets(3)
TeamGelatoGiants.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(3)
TeamGelatoGiants.event(mens_singles).match("1.4").winner("Auger-Aliassime").in_set(3)
TeamGelatoGiants.event(mens_singles).match("1.5").winner("Rublev").in_sets(3)
TeamGelatoGiants.event(mens_singles).match("1.6").winner("Djokovic").in_sets(4)
TeamGelatoGiants.event(mens_singles).match("1.7").winner("Wolf").in_sets(3)
TeamGelatoGiants.event(mens_singles).match("1.8").winner("Bautista-Agut").in_sets(4)

TeamGelatoGiants.event(womens_singles).match("1.1").winner(Swiatek).in_sets(2)
TeamGelatoGiants.event(womens_singles).match("1.2").winner(Gauff).in_sets(2)
TeamGelatoGiants.event(womens_singles).match("1.3").winner(Pegula).in_sets(2)
TeamGelatoGiants.event(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
TeamGelatoGiants.event(womens_singles).match("1.5").winner(Pliskova).in_sets(3)
TeamGelatoGiants.event(womens_singles).match("1.6").winner(Linette).in_sets(3)
TeamGelatoGiants.event(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
TeamGelatoGiants.event(womens_singles).match("1.8").winner(Vekic).in_sets(2)
                                                         

 # TeamPolarPrecision
TeamPolarPrecision.event(mens_singles).match("1.1").winner(Nishioka).in_sets(5)
TeamPolarPrecision.event(mens_singles).match("1.2").winner(Korda).in_sets(4)
TeamPolarPrecision.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
TeamPolarPrecision.event(mens_singles).match("1.4").winner("Auger-Aliassime").in_set(4)
TeamPolarPrecision.event(mens_singles).match("1.5").winner("Rublev").in_sets(4)
TeamPolarPrecision.event(mens_singles).match("1.6").winner("deMinaur").in_sets(5)
TeamPolarPrecision.event(mens_singles).match("1.7").winner("Shelton").in_sets(5)
TeamPolarPrecision.event(mens_singles).match("1.8").winner("Bautista-Agut").in_sets(5)

TeamPolarPrecision.event(womens_singles).match("1.1").winner(Rybakina).in_sets(3)
TeamPolarPrecision.event(womens_singles).match("1.2").winner(Gauff).in_sets(3)
TeamPolarPrecision.event(womens_singles).match("1.3").winner(Pegula).in_sets(3)
TeamPolarPrecision.event(womens_singles).match("1.4").winner(Zhu).in_sets(3)
TeamPolarPrecision.event(womens_singles).match("1.5").winner(Zhang).in_sets(3)
TeamPolarPrecision.event(womens_singles).match("1.6").winner(Garcia).in_sets(3)
TeamPolarPrecision.event(womens_singles).match("1.7").winner(Benecic).in_sets(3)
TeamPolarPrecision.event(womens_singles).match("1.8").winner(Vekic).in_sets(3)
                                                           
 
# TeamHeroHangouts
TeamHeroHangouts.event(mens_singles).match("1.1").winner(Khachanov).in_sets(4)
TeamHeroHangouts.event(mens_singles).match("1.2").winner(Hurkacz).in_sets(4)
TeamHeroHangouts.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
TeamHeroHangouts.event(mens_singles).match("1.4").winner("Auger-Aliassime").in_set(5)
TeamHeroHangouts.event(mens_singles).match("1.5").winner("Rune").in_sets(5)
TeamHeroHangouts.event(mens_singles).match("1.6").winner("Djokovic").in_sets(5)
TeamHeroHangouts.event(mens_singles).match("1.7").winner("Wolf").in_sets(4)
TeamHeroHangouts.event(mens_singles).match("1.8").winner("Bautista-Agut").in_sets(5)

TeamHeroHangouts.event(womens_singles).match("1.1").winner(Swiatek).in_sets(3)
TeamHeroHangouts.event(womens_singles).match("1.2").winner(Gauff).in_sets(3)
TeamHeroHangouts.event(womens_singles).match("1.3").winner(Krejcikova).in_sets(3)
TeamHeroHangouts.event(womens_singles).match("1.4").winner(Zhu).in_sets(3)
TeamHeroHangouts.event(womens_singles).match("1.5").winner(Zhang).in_sets(3)
TeamHeroHangouts.event(womens_singles).match("1.6").winner(Linette).in_sets(3)
TeamHeroHangouts.event(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
TeamHeroHangouts.event(womens_singles).match("1.8").winner(Fruhvirtova).in_sets(3)   
                                                         

# TeamBearNecessities
TeamBearNecessities.event(mens_singles).match("1.1").winner(Khachanov).in_sets(5)
TeamBearNecessities.event(mens_singles).match("1.2").winner(Korda).in_sets(5)
TeamBearNecessities.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
TeamBearNecessities.event(mens_singles).match("1.4").winner("Auger-Aliassime").in_set(4)
TeamBearNecessities.event(mens_singles).match("1.5").winner("Rublev").in_sets(4)
TeamBearNecessities.event(mens_singles).match("1.6").winner("deMinaur").in_sets(5)
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
                                                            
                                                         
# TeamMusicalBears
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


# TeamFauve
TeamFauve.event(mens_singles).match("1.1").winner("Khachanov").in_sets(3)
TeamFauve.event(mens_singles).match("1.2").winner("Hurkacz").in_sets(3)
TeamFauve.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
TeamFauve.event(mens_singles).match("1.4").winner("Auger-Aliassime").in_sets(4)
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


# TeamClojo
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


# TeamLightHouse
TeamLightHouse.event(mens_singles).match("1.1").winner("Khachanov").in_sets(5)
TeamLightHouse.event(mens_singles).match("1.2").winner("Korda").in_sets(4)
TeamLightHouse.event(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
TeamLightHouse.event(mens_singles).match("1.4").winner("Auger-Aliassime").in_sets(3)
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
