import sys
from ao.fantasy.teams import *
from ao.fantasy import helpers
from ao.players import atp_players as men, wta_players as women

this = sys.modules[__name__]

TEAM = TeamGelatoGiants
def team_gelato_giants(mens_singles, womens_singles):
    helpers.selection_fn_caller(this, [mens_singles, womens_singles])
    return TEAM


def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles).match('1.1').winner(men).in_sets()  # (  1) Carlos Alcaraz  OR  (  Q) Cobolli
    TEAM.draw(mens_singles).match('1.2').winner(men).in_sets()  # (   ) Christopher O'Connell  OR  (   ) Taro Daniel
    TEAM.draw(mens_singles).match('1.3').winner(men).in_sets()  # (   ) Matteo Arnaldi  OR  (   ) Daniel Elahi Galan
    TEAM.draw(mens_singles).match('1.4').winner(men).in_sets()  # (   ) Brandon Nakashima  OR  ( 26) Denis Shapovalov
    TEAM.draw(mens_singles).match('1.5').winner(men).in_sets()  # ( 17) Lorenzo Musetti  OR  (   ) Mikael Ymer
    TEAM.draw(mens_singles).match('1.6').winner(men).in_sets()  # (   ) Alexander Shevchenko  OR  (   ) Oscar Otte
    TEAM.draw(mens_singles).match('1.7').winner(men).in_sets()  # (  Q) Pouille  OR  (  L) Jurij Rodionov
    TEAM.draw(mens_singles).match('1.8').winner(men).in_sets()  # (  W) Benoit Paire  OR  ( 14) Cameron Norrie
    TEAM.draw(mens_singles).match('1.9').winner(men).in_sets()  # ( 10) Felix Auger-Aliassime  OR  (   ) Fabio Fognini
    TEAM.draw(mens_singles).match('1.10').winner(men).in_sets()  # (   ) Jason Kubler  OR  (  L) Diaz Acosta
    TEAM.draw(mens_singles).match('1.11').winner(men).in_sets()  # (  Q) Sebastian Ofner  OR  (   ) Maxime Cressy
    TEAM.draw(mens_singles).match('1.12').winner(men).in_sets()  # (   ) Mackenzie McDonald  OR  ( 24) Sebastian Korda
    TEAM.draw(mens_singles).match(
        '1.13').winner(men).in_sets()  # ( 32) Bernabe Zapata Miralles  OR  (   ) Diego Schwartzman
    TEAM.draw(mens_singles).match('1.14').winner(men).in_sets()  # (   ) John Isner  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles).match('1.15').winner(men).in_sets()  # (   ) Roberto Carballes Baena  OR  (  Q) Emilio Nava
    TEAM.draw(mens_singles).match('1.16').winner(men).in_sets()  # (   ) Jiri Vesely  OR  (  5) Stefanos Tsitsipas
    TEAM.draw(mens_singles).match('1.17').winner(men).in_sets()  # (  3) Novak Djokovic  OR  (   ) Aleksandar Kovacevic
    TEAM.draw(mens_singles).match('1.18').winner(men).in_sets()  # (   ) Marton Fucsovics  OR  (  W) Hugo Grenier
    TEAM.draw(mens_singles).match('1.19').winner(men).in_sets()  # (   ) Luca Van Assche  OR  (   ) Marco Cecchinato
    TEAM.draw(mens_singles).match('1.20').winner(men).in_sets()  # (  W) Arthur Fils  OR  ( 29) Alejandro Davidovich Fokina
    TEAM.draw(mens_singles).match('1.21').winner(men).in_sets()  # ( 19) Roberto Bautista Agut  OR  (   ) Yibing Wu
    TEAM.draw(mens_singles).match('1.22').winner(men).in_sets()  # (  Q) Juncheng Shang  OR  (   ) Juan Pablo Varillas
    TEAM.draw(mens_singles).match('1.23').winner(men).in_sets()  # (  Q) Pedro Martinez  OR  (   ) Tallon Griekspoor
    TEAM.draw(mens_singles).match('1.24').winner(men).in_sets()  # (   ) David Goffin  OR  ( 13) Hubert Hurkacz
    TEAM.draw(mens_singles).match('1.25').winner(men).in_sets()  # ( 11) Karen Khachanov  OR  (   ) Constant Lestienne
    TEAM.draw(mens_singles).match('1.26').winner(men).in_sets()  # (  W) Patrick Kypson  OR  (  Q) Radu Albot
    TEAM.draw(mens_singles).match('1.27').winner(men).in_sets()  # (   ) Stan Wawrinka  OR  (   ) Albert Ramos-Vinolas
    TEAM.draw(mens_singles).match('1.28').winner(men).in_sets()  # (  W) Thanasi Kokkinakis  OR  ( 20) Daniel Evans
    TEAM.draw(mens_singles).match('1.29').winner(men).in_sets()  # ( 30) Ben Shelton  OR  (   ) Lorenzo Sonego
    TEAM.draw(mens_singles).match('1.30').winner(men).in_sets()  # (   ) Adrian Mannarino  OR  (   ) Ugo Humbert
    TEAM.draw(mens_singles).match('1.31').winner(men).in_sets()  # (  W) Arthur Cazaux  OR  (   ) Corentin Moutet
    TEAM.draw(mens_singles).match('1.32').winner(men).in_sets()  # (   ) Laslo Djere  OR  (  7) Andrey Rublev
    TEAM.draw(mens_singles).match('1.33').winner(men).in_sets()  # (  6) Holger Rune  OR  (   ) Christopher Eubanks
    TEAM.draw(mens_singles).match('1.34').winner(men).in_sets()  # (   ) Gael Monfils  OR  (   ) Sebastian Baez
    TEAM.draw(mens_singles).match('1.35').winner(men).in_sets()  # (  W) G.Mpetshi Perricard  OR  (  Q) GA.Olivieri
    TEAM.draw(mens_singles).match('1.36').winner(men).in_sets()  # (  Q) Andrea Vavassori  OR  ( 31) Miomir Kecmanovic
    TEAM.draw(mens_singles).match('1.37').winner(men).in_sets()  # ( 23) Francisco Cerundolo  OR  (   ) Jaume Munar
    TEAM.draw(mens_singles).match('1.38').winner(men).in_sets()  # (   ) Thiago Monteiro  OR  (   ) Benjamin Bonzi
    TEAM.draw(mens_singles).match('1.39').winner(men).in_sets()  # (   ) Richard Gasquet  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles).match('1.40').winner(men).in_sets()  # (   ) Michael Mmoh  OR  (  9) Taylor Fritz
    TEAM.draw(mens_singles).match('1.41').winner(men).in_sets()  # ( 16) Tommy Paul  OR  (  L) D.Stricker
    TEAM.draw(mens_singles).match('1.42').winner(men).in_sets()  # (   ) Nicolas Jarry  OR  (   ) Hugo Dellien
    TEAM.draw(mens_singles).match('1.43').winner(men).in_sets()  # (  Q) H.Medjedovic  OR  (   ) Marcos Giron
    TEAM.draw(mens_singles).match('1.44').winner(men).in_sets()  # (   ) Jiri Lehecka  OR  ( 21) Jan-Lennard Struff
    TEAM.draw(mens_singles).match('1.45').winner(men).in_sets()  # ( 25) B.Van De Zandschulp  OR  (  Q) TA.Tirante
    TEAM.draw(mens_singles).match('1.46').winner(men).in_sets()  # (   ) Zhizhen Zhang  OR  (   ) Dusan Lajovic
    TEAM.draw(mens_singles).match('1.47').winner(men).in_sets()  # (   ) Alexander Bublik  OR  (  Q) Giulio Zeppieri
    TEAM.draw(mens_singles).match('1.48').winner(men).in_sets()  # (  Q) Elias Ymer  OR  (  4) Casper Ruud
    TEAM.draw(mens_singles).match('1.49').winner(men).in_sets()  # (  8) Jannik Sinner  OR  (   ) Alexandre Muller
    TEAM.draw(mens_singles).match('1.50').winner(men).in_sets()  # (   ) Daniel Altmaier  OR  (   ) Marc-Andrea Huesler
    TEAM.draw(mens_singles).match('1.51').winner(men).in_sets()  # (   ) Emil Ruusuvuori  OR  (   ) Gregoire Barrere
    TEAM.draw(mens_singles).match('1.52').winner(men).in_sets()  # (  Q) Timofey Skatov  OR  ( 28) Grigor Dimitrov
    TEAM.draw(mens_singles).match('1.53').winner(men).in_sets()  # ( 22) Alexander Zverev  OR  (   ) Lloyd Harris
    TEAM.draw(mens_singles).match('1.54').winner(men).in_sets()  # (  W) Hugo Gaston  OR  (   ) Alex Molcan
    TEAM.draw(mens_singles).match('1.55').winner(men).in_sets()  # (   ) Alexei Popyrin  OR  (  Q) Aslan Karatsev
    TEAM.draw(mens_singles).match('1.56').winner(men).in_sets()  # (   ) Filip Krajinovic  OR  ( 12) Frances Tiafoe
    TEAM.draw(mens_singles).match('1.57').winner(men).in_sets()  # ( 15) Borna Coric  OR  (   ) Federico Coria
    TEAM.draw(mens_singles).match('1.58').winner(men).in_sets()  # (   ) Dominic Thiem  OR  (   ) Pedro Cachin
    TEAM.draw(mens_singles).match('1.59').winner(men).in_sets()  # (   ) Jack Draper  OR  (   ) Tomas Martin Etcheverry
    TEAM.draw(mens_singles).match('1.60').winner(men).in_sets()  # (   ) Ilya Ivashka  OR  ( 18) Alex De Minaur
    TEAM.draw(mens_singles).match('1.61').winner(men).in_sets()  # ( 27) Yoshihito Nishioka  OR  (   ) J.J. Wolf
    TEAM.draw(mens_singles).match('1.62').winner(men).in_sets()  # (   ) Max Purcell  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles).match('1.63').winner(men).in_sets()  # (   ) Quentin Halys  OR  (   ) Guido Pella
    TEAM.draw(mens_singles).match('1.64').winner(men).in_sets()  # (  Q) T.Seyboth Wild  OR  (  2) Daniil Medvedev

def womens_singles_round_1(womens_singles):
    TEAM.draw(womens_singles).match('1.1').winner(women).in_sets()  # (  1) Iga Swiatek  OR  (   ) Cristina Bucsa
    TEAM.draw(womens_singles).match('1.2').winner(women).in_sets()  # (  Q) Y.In-Albon  OR  (   ) Claire Liu
    TEAM.draw(womens_singles).match('1.3').winner(women).in_sets()  # (   ) Rebecca Peterson  OR  (  Q) F.Ferro
    TEAM.draw(womens_singles).match('1.4').winner(women).in_sets()  # (   ) Xinyu Wang  OR  ( 31) Marie Bouzkova
    TEAM.draw(womens_singles).match('1.5').winner(women).in_sets()  # ( 18) Victoria Azarenka  OR  (   ) Bianca Andreescu
    TEAM.draw(womens_singles).match('1.6').winner(women).in_sets()  # (   ) Anna Kalinskaya  OR  (  W) Emma Navarro
    TEAM.draw(womens_singles).match('1.7').winner(women).in_sets()  # (   ) Lin Zhu  OR  (   ) Lauren Davis
    TEAM.draw(womens_singles).match('1.8').winner(women).in_sets()  # (   ) Lesia Tsurenko  OR  ( 13) Barbora Krejcikova
    TEAM.draw(womens_singles).match(
        '1.9').winner(women).in_sets()  # ( 11) Veronika Kudermetova  OR  (   ) Anna Karolina Schmiedlova
    TEAM.draw(womens_singles).match('1.10').winner(women).in_sets()  # (  L) Aliona Bolsova  OR  (   ) Kristina Kucova
    TEAM.draw(womens_singles).match('1.11').winner(women).in_sets()  # (  Q) K.Day  OR  (  W) Kristina Mladenovic
    TEAM.draw(womens_singles).match('1.12').winner(women).in_sets()  # (   ) Kaia Kanepi  OR  ( 20) Madison Keys
    TEAM.draw(womens_singles).match('1.13').winner(women).in_sets()  # ( 25) Anhelina Kalinina  OR  (  W) Diane Parry
    TEAM.draw(womens_singles).match('1.14').winner(women).in_sets()  # (  Q) Mirra Andreeva  OR  (   ) Alison Riske-Amritraj
    TEAM.draw(womens_singles).match('1.15').winner(women).in_sets()  # (  Q) Arantxa Rus  OR  (   ) Julia Grabher
    TEAM.draw(womens_singles).match('1.16').winner(women).in_sets()  # (   ) Rebeka Masarova  OR  (  6) Coco Gauff
    TEAM.draw(womens_singles).match('1.17').winner(women).in_sets()  # (  4) Elena Rybakina  OR  (  Q) Brenda Fruhvirtova
    TEAM.draw(womens_singles).match('1.18').winner(women).in_sets()  # (   ) Linda Noskova  OR  (   ) Danka Kovinic
    TEAM.draw(womens_singles).match('1.19').winner(women).in_sets()  # (  W) Clara Burel  OR  (   ) Sorribes Tormo
    TEAM.draw(womens_singles).match('1.20').winner(women).in_sets()  # (   ) Petra Martic  OR  ( 32) Shelby Rogers
    TEAM.draw(womens_singles).match(
        '1.21').winner(women).in_sets()  # ( 23) Ekaterina Alexandrova  OR  (   ) Viktoriya Tomova
    TEAM.draw(womens_singles).match('1.22').winner(women).in_sets()  # (  L) Nao Hibino  OR  (   ) Anna-Lena Friedsam
    TEAM.draw(womens_singles).match('1.23').winner(women).in_sets()  # (   ) Rebecca Marino  OR  (   ) Diana Shnaider
    TEAM.draw(womens_singles).match('1.24').winner(women).in_sets()  # (   ) Tatjana Maria  OR  ( 14) Beatriz Haddad Maia
    TEAM.draw(womens_singles).match('1.25').winner(women).in_sets()  # ( 10) Petra Kvitova  OR  (   ) Elisabetta Cocciaretto
    TEAM.draw(womens_singles).match('1.26').winner(women).in_sets()  # (  Q) Simona Waltert  OR  (  Q) Elizabeth Mandlik
    TEAM.draw(womens_singles).match('1.27').winner(women).in_sets()  # (   ) Anett Kontaveit  OR  (   ) Bernarda Pera
    TEAM.draw(womens_singles).match('1.28').winner(women).in_sets()  # (  Q) Dayana Yastremska  OR  ( 22) Donna Vekic
    TEAM.draw(womens_singles).match('1.29').winner(women).in_sets()  # ( 30) Sorana Cirstea  OR  (   ) Jasmine Paolini
    TEAM.draw(womens_singles).match('1.30').winner(women).in_sets()  # (  Q) Olga Danilovic  OR  (   ) Kateryna Baindl
    TEAM.draw(womens_singles).match('1.31').winner(women).in_sets()  # (  W) Selena Janicijevic  OR  (   ) Dodin
    TEAM.draw(womens_singles).match('1.32').winner(women).in_sets()  # (   ) Lucia Bronzetti  OR  (  7) Ons Jabeur
    TEAM.draw(womens_singles).match('1.33').winner(women).in_sets()  # (  8) Maria Sakkari  OR  (   ) Karolina Muchova
    TEAM.draw(womens_singles).match('1.34').winner(women).in_sets()  # (   ) Nadia Podoroska  OR  (  W) Ponchet
    TEAM.draw(womens_singles).match('1.35').winner(women).in_sets()  # (   ) Sara Errani  OR  (   ) Jil Teichmann
    TEAM.draw(womens_singles).match('1.36').winner(women).in_sets()  # (   ) Anna Bondar  OR  ( 27) Irina-Camelia Begu
    TEAM.draw(womens_singles).match('1.37').winner(women).in_sets()  # ( 21) Magda Linette  OR  (   ) Leylah Fernandez
    TEAM.draw(womens_singles).match('1.38').winner(women).in_sets()  # (  Q) C.Tauson  OR  (   ) Aliaksandra Sasnovich
    TEAM.draw(womens_singles).match('1.39').winner(women).in_sets()  # (  W) Leolia Jeanjean  OR  (  W) Kimberly Birrell
    TEAM.draw(womens_singles).match('1.40').winner(women).in_sets()  # (  L) Elina Avanesyan  OR  ( 12) Belinda Bencic
    TEAM.draw(womens_singles).match('1.41').winner(women).in_sets()  # ( 15) Liudmila Samsonova  OR  (   ) Katie Volynets
    TEAM.draw(womens_singles).match(
        '1.42').winner(women).in_sets()  # (   ) Anastasia Pavlyuchenkova  OR  (   ) Linda Fruhvirtova
    TEAM.draw(womens_singles).match('1.43').winner(women).in_sets()  # (   ) Mayar Sherif  OR  (   ) Madison Brengle
    TEAM.draw(womens_singles).match('1.44').winner(women).in_sets()  # (  Q) Taylor Townsend  OR  ( 24) Anastasia Potapova
    TEAM.draw(womens_singles).match('1.45').winner(women).in_sets()  # ( 28) Elise Mertens  OR  (  L) V.Hruncakova
    TEAM.draw(womens_singles).match('1.46').winner(women).in_sets()  # (   ) Catherine McNally  OR  (   ) Ana Bogdan
    TEAM.draw(womens_singles).match('1.47').winner(women).in_sets()  # (   ) Alize Cornet  OR  (   ) Camila Giorgi
    TEAM.draw(womens_singles).match('1.48').winner(women).in_sets()  # (   ) Danielle Collins  OR  (  3) Jessica Pegula
    TEAM.draw(womens_singles).match('1.49').winner(women).in_sets()  # (  5) Caroline Garcia  OR  (   ) Xinyu Wang
    TEAM.draw(womens_singles).match('1.50').winner(women).in_sets()  # (   ) Anna Blinkova  OR  (   ) Ysaline Bonaventure
    TEAM.draw(womens_singles).match('1.51').winner(women).in_sets()  # (   ) Nuria Parrizas Diaz  OR  (  Q) Storm Hunter
    TEAM.draw(womens_singles).match('1.52').winner(women).in_sets()  # (   ) Svitolina  OR  ( 26) Martina Trevisan
    TEAM.draw(womens_singles).match('1.53').winner(women).in_sets()  # ( 17) Jelena Ostapenko  OR  (   ) Tereza Martincova
    TEAM.draw(womens_singles).match('1.54').winner(women).in_sets()  # (   ) Peyton Stearns  OR  (   ) Katerina Siniakova
    TEAM.draw(womens_singles).match('1.55').winner(women).in_sets()  # (   ) Marketa Vondrousova  OR  (   ) Alycia Parks
    TEAM.draw(womens_singles).match('1.56').winner(women).in_sets()  # (   ) Jule Niemeier  OR  (  9) Daria Kasatkina
    TEAM.draw(womens_singles).match('1.57').winner(women).in_sets()  # ( 16) Karolina Pliskova  OR  (   ) Sloane Stephens
    TEAM.draw(womens_singles).match('1.58').winner(women).in_sets()  # (   ) Varvara Gracheva  OR  (   ) Dalma Galfi
    TEAM.draw(womens_singles).match('1.59').winner(women).in_sets()  # (   ) Yulia Putintseva  OR  (   ) Maryna Zanevska
    TEAM.draw(womens_singles).match('1.60').winner(women).in_sets()  # (  Q) Tamara Zidansek  OR  ( 19) Qinwen Zheng
    TEAM.draw(womens_singles).match('1.61').winner(women).in_sets()  # ( 29) Shuai Zhang  OR  (   ) Magdalena Frech
    TEAM.draw(womens_singles).match('1.62').winner(women).in_sets()  # (  Q) Sara Bejlek  OR  (   ) Kamilla Rakhimova
    TEAM.draw(womens_singles).match('1.63').winner(women).in_sets()  # (   ) Panna Udvardy  OR  (  Q) I.Shymanovich
    TEAM.draw(womens_singles).match('1.64').winner(women).in_sets()  # (   ) Marta Kostyuk  OR  (  2) Aryna Sabalenka

    return TeamGelatoGiants
