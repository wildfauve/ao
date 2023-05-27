from ao.fantasy.teams import *
from ao.players import atp_players as men, wta_players as women

TEAM = TeamMusicalBears


def team_musical_bears(mens_singles, womens_singles):
    TEAM.draw(mens_singles).match('1.1').winner(men.Alcaraz).in_sets(3)  # (  1) Carlos Alcaraz  OR  (  Q) Cobolli
    TEAM.draw(mens_singles).match('1.2').winner(men.OConnell).in_sets(
        4)  # (   ) Christopher O'Connell  OR  (   ) Taro Daniel
    TEAM.draw(mens_singles).match('1.3').winner(men.Galan).in_sets(
        4)  # (   ) Matteo Arnaldi  OR  (   ) Daniel Elahi Galan
    TEAM.draw(mens_singles).match('1.4').winner(men.Shapovalov).in_sets(
        3)  # (   ) Brandon Nakashima  OR  ( 26) Denis Shapovalov
    TEAM.draw(mens_singles).match('1.5').winner(men.Musetti).in_sets(3)  # ( 17) Lorenzo Musetti  OR  (   ) Mikael Ymer
    TEAM.draw(mens_singles).match('1.6').winner(men.Otte).in_sets(5)  # (   ) Alexander Shevchenko  OR  (   ) Oscar Otte
    TEAM.draw(mens_singles).match('1.7').winner(men.Pouille).in_sets(5)  # (  Q) Pouille  OR  (  L) Jurij Rodionov
    TEAM.draw(mens_singles).match('1.8').winner(men.Norrie).in_sets(3)  # (  W) Benoit Paire  OR  ( 14) Cameron Norrie
    TEAM.draw(mens_singles).match('1.9').winner(men.Auger_Aliassime).in_sets(
        3)  # ( 10) Felix Auger-Aliassime  OR  (   ) Fabio Fognini
    TEAM.draw(mens_singles).match('1.10').winner(men.Kubler).in_sets(3)  # (   ) Jason Kubler  OR  (  L) Diaz Acosta
    TEAM.draw(mens_singles).match('1.11').winner(men.Cressy).in_sets(
        4)  # (  Q) Sebastian Ofner  OR  (   ) Maxime Cressy
    TEAM.draw(mens_singles).match('1.12').winner(men.Korda).in_sets(
        3)  # (   ) Mackenzie McDonald  OR  ( 24) Sebastian Korda
    TEAM.draw(mens_singles).match('1.13').winner(
        men.Zapata_Miralles).in_sets(3)  # ( 32) Bernabe Zapata Miralles  OR  (   ) Diego Schwartzman
    TEAM.draw(mens_singles).match('1.14').winner(men.Borges).in_sets(4)  # (   ) John Isner  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles).match('1.15').winner(men.Carballes_Baena).in_sets(
        4)  # (   ) Roberto Carballes Baena  OR  (  Q) Emilio Nava
    TEAM.draw(mens_singles).match('1.16').winner(men.Tsitsipas).in_sets(
        3)  # (   ) Jiri Vesely  OR  (  5) Stefanos Tsitsipas
    TEAM.draw(mens_singles).match('1.17').winner(men.Djokovic).in_sets(
        3)  # (  3) Novak Djokovic  OR  (   ) Aleksandar Kovacevic
    TEAM.draw(mens_singles).match('1.18').winner(men.Fucsovics).in_sets(
        4)  # (   ) Marton Fucsovics  OR  (  W) Hugo Grenier
    TEAM.draw(mens_singles).match('1.19').winner(men.Cecchinato).in_sets(
        4)  # (   ) Luca Van Assche  OR  (   ) Marco Cecchinato
    TEAM.draw(mens_singles).match('1.20').winner(
        men.Fognini).in_sets(4)  # (  W) Arthur Fils  OR  ( 29) Alejandro Davidovich Fokina
    TEAM.draw(mens_singles).match('1.21').winner(men.Bautista_Agut).in_sets(
        3)  # ( 19) Roberto Bautista Agut  OR  (   ) Yibing Wu
    TEAM.draw(mens_singles).match('1.22').winner(men.Varillas).in_sets(
        4)  # (  Q) Juncheng Shang  OR  (   ) Juan Pablo Varillas
    TEAM.draw(mens_singles).match('1.23').winner(men.Griekspoor).in_sets(
        4)  # (  Q) Pedro Martinez  OR  (   ) Tallon Griekspoor
    TEAM.draw(mens_singles).match('1.24').winner(men.Hurkacz).in_sets(3)  # (   ) David Goffin  OR  ( 13) Hubert Hurkacz
    TEAM.draw(mens_singles).match('1.25').winner(men.Khachanov).in_sets(
        3)  # ( 11) Karen Khachanov  OR  (   ) Constant Lestienne
    TEAM.draw(mens_singles).match('1.26').winner(men.Albot).in_sets(5)  # (  W) Patrick Kypson  OR  (  Q) Radu Albot
    TEAM.draw(mens_singles).match('1.27').winner(men.Wawrinka).in_sets(
        4)  # (   ) Stan Wawrinka  OR  (   ) Albert Ramos-Vinolas
    TEAM.draw(mens_singles).match('1.28').winner(men.Evans).in_sets(
        4)  # (  W) Thanasi Kokkinakis  OR  ( 20) Daniel Evans
    TEAM.draw(mens_singles).match('1.29').winner(men.Shelton).in_sets(4)  # ( 30) Ben Shelton  OR  (   ) Lorenzo Sonego
    TEAM.draw(mens_singles).match('1.30').winner(men.Humbert).in_sets(
        4)  # (   ) Adrian Mannarino  OR  (   ) Ugo Humbert
    TEAM.draw(mens_singles).match('1.31').winner(men.Moutet).in_sets(
        4)  # (  W) Arthur Cazaux  OR  (   ) Corentin Moutet
    TEAM.draw(mens_singles).match('1.32').winner(men.Rublev).in_sets(3)  # (   ) Laslo Djere  OR  (  7) Andrey Rublev
    TEAM.draw(mens_singles).match('1.33').winner(men.Rune).in_sets(
        3)  # (  6) Holger Rune  OR  (   ) Christopher Eubanks
    TEAM.draw(mens_singles).match('1.34').winner(men.Monfils).in_sets(4)  # (   ) Gael Monfils  OR  (   ) Sebastian Baez
    TEAM.draw(mens_singles).match('1.35').winner(men.Mpetshi_Perricard).in_sets(
        4)  # (  W) G.Mpetshi Perricard  OR  (  Q) GA.Olivieri
    TEAM.draw(mens_singles).match('1.36').winner(men.Kecmanovic).in_sets(
        3)  # (  Q) Andrea Vavassori  OR  ( 31) Miomir Kecmanovic
    TEAM.draw(mens_singles).match('1.37').winner(men.Cerundolo_Francisco).in_sets(
        3)  # ( 23) Francisco Cerundolo  OR  (   ) Jaume Munar
    TEAM.draw(mens_singles).match('1.38').winner(men.Monteiro).in_sets(
        4)  # (   ) Thiago Monteiro  OR  (   ) Benjamin Bonzi
    TEAM.draw(mens_singles).match('1.39').winner(men.Rinderknech).in_sets(
        4)  # (   ) Richard Gasquet  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles).match('1.40').winner(men.Fritz).in_sets(3)  # (   ) Michael Mmoh  OR  (  9) Taylor Fritz
    TEAM.draw(mens_singles).match('1.41').winner(men.Paul).in_sets(3)  # ( 16) Tommy Paul  OR  (  L) D.Stricker
    TEAM.draw(mens_singles).match('1.42').winner(men.Jarry).in_sets(5)  # (   ) Nicolas Jarry  OR  (   ) Hugo Dellien
    TEAM.draw(mens_singles).match('1.43').winner(men.Medjedovic).in_sets(
        4)  # (  Q) H.Medjedovic  OR  (   ) Marcos Giron
    TEAM.draw(mens_singles).match('1.44').winner(men.Struff).in_sets(
        4)  # (   ) Jiri Lehecka  OR  ( 21) Jan-Lennard Struff
    TEAM.draw(mens_singles).match('1.45').winner(men.Van_De_Zandschulp).in_sets(
        4)  # ( 25) B.Van De Zandschulp  OR  (  Q) TA.Tirante
    TEAM.draw(mens_singles).match('1.46').winner(men.Zhang_Zhizhen).in_sets(
        4)  # (   ) Zhizhen Zhang  OR  (   ) Dusan Lajovic
    TEAM.draw(mens_singles).match('1.47').winner(men.Bublik).in_sets(
        4)  # (   ) Alexander Bublik  OR  (  Q) Giulio Zeppieri
    TEAM.draw(mens_singles).match('1.48').winner(men.Ruud).in_sets(3)  # (  Q) Elias Ymer  OR  (  4) Casper Ruud
    TEAM.draw(mens_singles).match('1.49').winner(men.Sinner).in_sets(
        3)  # (  8) Jannik Sinner  OR  (   ) Alexandre Muller
    TEAM.draw(mens_singles).match('1.50').winner(men.Huesler).in_sets(
        4)  # (   ) Daniel Altmaier  OR  (   ) Marc-Andrea Huesler
    TEAM.draw(mens_singles).match('1.51').winner(men.Barrere).in_sets(
        4)  # (   ) Emil Ruusuvuori  OR  (   ) Gregoire Barrere
    TEAM.draw(mens_singles).match('1.52').winner(men.Dimitrov).in_sets(
        4)  # (  Q) Timofey Skatov  OR  ( 28) Grigor Dimitrov
    TEAM.draw(mens_singles).match('1.53').winner(men.Zverev).in_sets(
        3)  # ( 22) Alexander Zverev  OR  (   ) Lloyd Harris
    TEAM.draw(mens_singles).match('1.54').winner(men.Gaston).in_sets(4)  # (  W) Hugo Gaston  OR  (   ) Alex Molcan
    TEAM.draw(mens_singles).match('1.55').winner(men.Karatsev).in_sets(
        4)  # (   ) Alexei Popyrin  OR  (  Q) Aslan Karatsev
    TEAM.draw(mens_singles).match('1.56').winner(men.Tiafoe).in_sets(
        4)  # (   ) Filip Krajinovic  OR  ( 12) Frances Tiafoe
    TEAM.draw(mens_singles).match('1.57').winner(men.Coric).in_sets(3)  # ( 15) Borna Coric  OR  (   ) Federico Coria
    TEAM.draw(mens_singles).match('1.58').winner(men.Cachin).in_sets(4)  # (   ) Dominic Thiem  OR  (   ) Pedro Cachin
    TEAM.draw(mens_singles).match('1.59').winner(men.Draper).in_sets(
        4)  # (   ) Jack Draper  OR  (   ) Tomas Martin Etcheverry
    TEAM.draw(mens_singles).match('1.60').winner(men.De_Minaur).in_sets(
        4)  # (   ) Ilya Ivashka  OR  ( 18) Alex De Minaur
    TEAM.draw(mens_singles).match('1.61').winner(men.Nishioka).in_sets(
        3)  # ( 27) Yoshihito Nishioka  OR  (   ) J.J. Wolf
    TEAM.draw(mens_singles).match('1.62').winner(men.Thompson).in_sets(
        4)  # (   ) Max Purcell  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles).match('1.63').winner(men.Halys).in_sets(4)  # (   ) Quentin Halys  OR  (   ) Guido Pella
    TEAM.draw(mens_singles).match('1.64').winner(men.Medvedev).in_sets(
        3)  # (  Q) T.Seyboth Wild  OR  (  2) Daniil Medvedev

    return TeamMusicalBears
