from ao.model import fantasy
from ao.players import atp_players as men, wta_players as women

TEAM = fantasy.Team("TEAM")
def mens_singles_round_2(mens_singles):
    TEAM.draw(mens_singles).match('2.1').winner(men).in_sets()  # (  1) Alcaraz  OR  (   ) Daniel
    TEAM.draw(mens_singles).match('2.2').winner(men).in_sets()  # (   ) Arnaldi  OR  ( 26) Shapovalov
    TEAM.draw(mens_singles).match('2.3').winner(men).in_sets()  # ( 17) Musetti  OR  (   ) Shevchenko
    TEAM.draw(mens_singles).match('2.4').winner(men).in_sets()  # (  Q) Pouille  OR  ( 14) Norrie
    TEAM.draw(mens_singles).match('2.5').winner(men).in_sets()  # (   ) Fognini  OR  (   ) Kubler
    TEAM.draw(mens_singles).match('2.6').winner(men).in_sets()  # (  Q) Ofner  OR  ( 24) Korda
    TEAM.draw(mens_singles).match('2.7').winner(men).in_sets()  # (   ) Schwartzman  OR  (   ) Borges
    TEAM.draw(mens_singles).match('2.8').winner(men).in_sets()  # (   ) Carballes_Baena  OR  (  5) Tsitsipas
    TEAM.draw(mens_singles).match('2.9').winner(men).in_sets()  # (  3) Djokovic  OR  (   ) Fucsovics
    TEAM.draw(mens_singles).match('2.10').winner(men).in_sets()  # (   ) Van_Assche  OR  ( 29) Davidovich_Fokina
    TEAM.draw(mens_singles).match('2.11').winner(men).in_sets()  # ( 19) Bautista_Agut  OR  (   ) Varillas
    TEAM.draw(mens_singles).match('2.12').winner(men).in_sets()  # (   ) Griekspoor  OR  ( 13) Hurkacz
    TEAM.draw(mens_singles).match('2.13').winner(men).in_sets()  # ( 11) Khachanov  OR  (  Q) Albot
    TEAM.draw(mens_singles).match('2.14').winner(men).in_sets()  # (   ) Wawrinka  OR  (  W) Kokkinakis
    TEAM.draw(mens_singles).match('2.15').winner(men).in_sets()  # (   ) Sonego  OR  (   ) Humbert
    TEAM.draw(mens_singles).match('2.16').winner(men).in_sets()  # (   ) Moutet  OR  (  7) Rublev
    TEAM.draw(mens_singles).match('2.17').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.18').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.19').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.20').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.21').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.22').winner(men).in_sets()  # (   ) Giron  OR  (   ) Lehecka
    TEAM.draw(mens_singles).match('2.23').winner(men).in_sets()  # (  Q) Tirante  OR  (   ) Zhang_Zhizhen
    TEAM.draw(mens_singles).match('2.24').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.25').winner(men).in_sets()  # (  8) Sinner  OR  (   ) Altmaier
    TEAM.draw(mens_singles).match('2.26').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.27').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.28').winner(men).in_sets()  # (  Q) Karatsev  OR  ( 12) Tiafoe
    TEAM.draw(mens_singles).match('2.29').winner(men).in_sets()  # ( 15) Coric  OR  (   ) Cachin
    TEAM.draw(mens_singles).match('2.30').winner(men).in_sets()  # (   ) Etcheverry  OR  ( 18) De_Minaur
    TEAM.draw(mens_singles).match('2.31').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.32').winner(men).in_sets()  # TBD  OR  TBD
    return TEAM


def womens_singles_round_2(womens_singles):
    TEAM.draw(womens_singles).match('2.1').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.2').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.3').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.4').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.5').winner(women).in_sets()  # (   ) Schmiedlova  OR  (  L) Bolsova
    TEAM.draw(womens_singles).match('2.6').winner(women).in_sets()  # (  Q) Day  OR  ( 20) Keys
    TEAM.draw(womens_singles).match('2.7').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.8').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.9').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.10').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.11').winner(women).in_sets()  # ( 23) Alexandrova  OR  (   ) Friedsam
    TEAM.draw(womens_singles).match('2.12').winner(women).in_sets()  # (   ) Shnaider  OR  ( 14) Haddad_Maia
    TEAM.draw(womens_singles).match('2.13').winner(women).in_sets()  # (   ) Cocciaretto  OR  (  Q) Waltert
    TEAM.draw(womens_singles).match('2.14').winner(women).in_sets()  # (   ) Pera  OR  ( 22) Vekic
    TEAM.draw(womens_singles).match('2.15').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.16').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.17').winner(women).in_sets()  # (   ) Muchova  OR  (   ) Podoroska
    TEAM.draw(womens_singles).match('2.18').winner(women).in_sets()  # (   ) Errani  OR  ( 27) Begu
    TEAM.draw(womens_singles).match('2.19').winner(women).in_sets()  # (   ) Fernandez  OR  (  Q) Tauson
    TEAM.draw(womens_singles).match('2.20').winner(women).in_sets()  # (  W) Jeanjean  OR  (  L) Avanesyan
    TEAM.draw(womens_singles).match('2.21').winner(women).in_sets()  # ( 15) Samsonova  OR  (   ) Pavlyuchenkova
    TEAM.draw(womens_singles).match('2.22').winner(women).in_sets()  # (   ) Sherif  OR  ( 24) Potapova
    TEAM.draw(womens_singles).match('2.23').winner(women).in_sets()  # ( 28) Mertens  OR  (  L) Osorio
    TEAM.draw(womens_singles).match('2.24').winner(women).in_sets()  # (   ) Giorgi  OR  (  3) Pegula
    TEAM.draw(womens_singles).match('2.25').winner(women).in_sets()  # (  5) Garcia  OR  (   ) Blinkova
    TEAM.draw(womens_singles).match('2.26').winner(women).in_sets()  # (  Q) Hunter  OR  (   ) Svitolina
    TEAM.draw(womens_singles).match('2.27').winner(women).in_sets()  # ( 17) Ostapenko  OR  (   ) Stearns
    TEAM.draw(womens_singles).match('2.28').winner(women).in_sets()  # (   ) Vondrousova  OR  (  9) Kasatkina
    TEAM.draw(womens_singles).match('2.29').winner(women).in_sets()  # (   ) Stephens  OR  (   ) Gracheva
    TEAM.draw(womens_singles).match('2.30').winner(women).in_sets()  # (   ) Putintseva  OR  ( 19) Zheng
    TEAM.draw(womens_singles).match('2.31').winner(women).in_sets()  # (   ) Frech  OR  (   ) Rakhimova
    TEAM.draw(womens_singles).match('2.32').winner(women).in_sets()  # (  Q) Shymanovich  OR  (  2) Sabalenka
    return TEAM
