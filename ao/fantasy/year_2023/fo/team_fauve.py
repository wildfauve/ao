from ao.fantasy.teams import *
from ao.players import atp_players as men, wta_players as women

TEAM = TeamFauve
def team_fauve(mens_singles, womens_singles):
    # Round 1
    TEAM.draw(mens_singles).match('1.1').winner(men.Alcaraz).in_sets(3)  # (  1) Carlos Alcaraz  OR  (  Q) Cobolli
    TEAM.draw(mens_singles).match('1.2').winner(men.OConnell).in_sets(4)  # (   ) Christopher O'Connell  OR  (   ) Taro Daniel
    TEAM.draw(mens_singles).match('1.3').winner(men.Galan).in_sets(4)  # (   ) Matteo Arnaldi  OR  (   ) Daniel Elahi Galan
    TEAM.draw(mens_singles).match('1.4').winner(men.Shapovalov).in_sets(3)  # (   ) Brandon Nakashima  OR  ( 26) Denis Shapovalov
    TEAM.draw(mens_singles).match('1.5').winner(men.Musetti).in_sets(3)  # ( 17) Lorenzo Musetti  OR  (   ) Mikael Ymer
    TEAM.draw(mens_singles).match('1.6').winner(men.Otte).in_sets(5)  # (   ) Alexander Shevchenko  OR  (   ) Oscar Otte
    TEAM.draw(mens_singles).match('1.7').winner(men.Pouille).in_sets(5)  # (  Q) Pouille  OR  (  L) Jurij Rodionov
    TEAM.draw(mens_singles).match('1.8').winner(men.Norrie).in_sets(3)  # (  W) Benoit Paire  OR  ( 14) Cameron Norrie
    TEAM.draw(mens_singles).match('1.9').winner(men.Auger_Aliassime).in_sets(3)  # ( 10) Felix Auger-Aliassime  OR  (   ) Fabio Fognini
    TEAM.draw(mens_singles).match('1.10').winner(men.Kubler).in_sets(3)  # (   ) Jason Kubler  OR  (  L) Diaz Acosta
    TEAM.draw(mens_singles).match('1.11').winner(men.Cressy).in_sets(4)  # (  Q) Sebastian Ofner  OR  (   ) Maxime Cressy
    TEAM.draw(mens_singles).match('1.12').winner(men.Korda).in_sets(3)  # (   ) Mackenzie McDonald  OR  ( 24) Sebastian Korda
    TEAM.draw(mens_singles).match('1.13').winner(
        men.Zapata_Miralles).in_sets(3)  # ( 32) Bernabe Zapata Miralles  OR  (   ) Diego Schwartzman
    TEAM.draw(mens_singles).match('1.14').winner(men.Borges).in_sets(4)  # (   ) John Isner  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles).match('1.15').winner(men.Carballes_Baena).in_sets(4)  # (   ) Roberto Carballes Baena  OR  (  Q) Emilio Nava
    TEAM.draw(mens_singles).match('1.16').winner(men.Tsitsipas).in_sets(3)  # (   ) Jiri Vesely  OR  (  5) Stefanos Tsitsipas
    TEAM.draw(mens_singles).match('1.17').winner(men.Djokovic).in_sets(3)  # (  3) Novak Djokovic  OR  (   ) Aleksandar Kovacevic
    TEAM.draw(mens_singles).match('1.18').winner(men.Fucsovics).in_sets(4)  # (   ) Marton Fucsovics  OR  (  W) Hugo Grenier
    TEAM.draw(mens_singles).match('1.19').winner(men.Cecchinato).in_sets(4)  # (   ) Luca Van Assche  OR  (   ) Marco Cecchinato
    TEAM.draw(mens_singles).match('1.20').winner(
        men.Fognini).in_sets(4)  # (  W) Arthur Fils  OR  ( 29) Alejandro Davidovich Fokina
    TEAM.draw(mens_singles).match('1.21').winner(men.Bautista_Agut).in_sets(3)  # ( 19) Roberto Bautista Agut  OR  (   ) Yibing Wu
    TEAM.draw(mens_singles).match('1.22').winner(men.Varillas).in_sets(4)  # (  Q) Juncheng Shang  OR  (   ) Juan Pablo Varillas
    TEAM.draw(mens_singles).match('1.23').winner(men.Griekspoor).in_sets(4)  # (  Q) Pedro Martinez  OR  (   ) Tallon Griekspoor
    TEAM.draw(mens_singles).match('1.24').winner(men.Hurkacz).in_sets(3)  # (   ) David Goffin  OR  ( 13) Hubert Hurkacz
    TEAM.draw(mens_singles).match('1.25').winner(men.Khachanov).in_sets(3)  # ( 11) Karen Khachanov  OR  (   ) Constant Lestienne
    TEAM.draw(mens_singles).match('1.26').winner(men.Albot).in_sets(5)  # (  W) Patrick Kypson  OR  (  Q) Radu Albot
    TEAM.draw(mens_singles).match('1.27').winner(men.Wawrinka).in_sets(4)  # (   ) Stan Wawrinka  OR  (   ) Albert Ramos-Vinolas
    TEAM.draw(mens_singles).match('1.28').winner(men.Evans).in_sets(4)  # (  W) Thanasi Kokkinakis  OR  ( 20) Daniel Evans
    TEAM.draw(mens_singles).match('1.29').winner(men.Shelton).in_sets(4)  # ( 30) Ben Shelton  OR  (   ) Lorenzo Sonego
    TEAM.draw(mens_singles).match('1.30').winner(men.Humbert).in_sets(4)  # (   ) Adrian Mannarino  OR  (   ) Ugo Humbert
    TEAM.draw(mens_singles).match('1.31').winner(men.Moutet).in_sets(4)  # (  W) Arthur Cazaux  OR  (   ) Corentin Moutet
    TEAM.draw(mens_singles).match('1.32').winner(men.Rublev).in_sets(3)  # (   ) Laslo Djere  OR  (  7) Andrey Rublev
    TEAM.draw(mens_singles).match('1.33').winner(men.Rune).in_sets(3)  # (  6) Holger Rune  OR  (   ) Christopher Eubanks
    TEAM.draw(mens_singles).match('1.34').winner(men.Baez).in_sets(5)  # (   ) Gael Monfils  OR  (   ) Sebastian Baez
    TEAM.draw(mens_singles).match('1.35').winner(men.Olivieri).in_sets(4)  # (  W) G.Mpetshi Perricard  OR  (  Q) GA.Olivieri
    TEAM.draw(mens_singles).match('1.36').winner(men.Kecmanovic).in_sets(3)  # (  Q) Andrea Vavassori  OR  ( 31) Miomir Kecmanovic
    TEAM.draw(mens_singles).match('1.37').winner(men.Cerundolo_Francisco).in_sets(3)  # ( 23) Francisco Cerundolo  OR  (   ) Jaume Munar
    TEAM.draw(mens_singles).match('1.38').winner(men.Bonzi).in_sets(4)  # (   ) Thiago Monteiro  OR  (   ) Benjamin Bonzi
    TEAM.draw(mens_singles).match('1.39').winner(men.Gasquet).in_sets(4)  # (   ) Richard Gasquet  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles).match('1.40').winner(men.Fritz).in_sets(3)  # (   ) Michael Mmoh  OR  (  9) Taylor Fritz
    TEAM.draw(mens_singles).match('1.41').winner(men.Paul).in_sets(3)  # ( 16) Tommy Paul  OR  (  L) D.Stricker
    TEAM.draw(mens_singles).match('1.42').winner(men.Dellien).in_sets(5)  # (   ) Nicolas Jarry  OR  (   ) Hugo Dellien
    TEAM.draw(mens_singles).match('1.43').winner(men.Giron).in_sets(4)  # (  Q) H.Medjedovic  OR  (   ) Marcos Giron
    TEAM.draw(mens_singles).match('1.44').winner(men.Struff).in_sets(4)  # (   ) Jiri Lehecka  OR  ( 21) Jan-Lennard Struff
    TEAM.draw(mens_singles).match('1.45').winner(men.Van_De_Zandschulp).in_sets(3)  # ( 25) B.Van De Zandschulp  OR  (  Q) TA.Tirante
    TEAM.draw(mens_singles).match('1.46').winner(men.Lajovic).in_sets(4)  # (   ) Zhizhen Zhang  OR  (   ) Dusan Lajovic
    TEAM.draw(mens_singles).match('1.47').winner(men.Bublik).in_sets(4)  # (   ) Alexander Bublik  OR  (  Q) Giulio Zeppieri
    TEAM.draw(mens_singles).match('1.48').winner(men.Ruud).in_sets(3)  # (  Q) Elias Ymer  OR  (  4) Casper Ruud
    TEAM.draw(mens_singles).match('1.49').winner(men.Sinner).in_sets(3)  # (  8) Jannik Sinner  OR  (   ) Alexandre Muller
    TEAM.draw(mens_singles).match('1.50').winner(men.Altmaier).in_sets(4)  # (   ) Daniel Altmaier  OR  (   ) Marc-Andrea Huesler
    TEAM.draw(mens_singles).match('1.51').winner(men.Ruusuvuori).in_sets(4)  # (   ) Emil Ruusuvuori  OR  (   ) Gregoire Barrere
    TEAM.draw(mens_singles).match('1.52').winner(men.Dimitrov).in_sets(4)  # (  Q) Timofey Skatov  OR  ( 28) Grigor Dimitrov
    TEAM.draw(mens_singles).match('1.53').winner(men.Zverev).in_sets(3)  # ( 22) Alexander Zverev  OR  (   ) Lloyd Harris
    TEAM.draw(mens_singles).match('1.54').winner(men.Molcan).in_sets(4)  # (  W) Hugo Gaston  OR  (   ) Alex Molcan
    TEAM.draw(mens_singles).match('1.55').winner(men.Popyrin).in_sets(3)  # (   ) Alexei Popyrin  OR  (  Q) Aslan Karatsev
    TEAM.draw(mens_singles).match('1.56').winner(men.Tiafoe).in_sets(4)  # (   ) Filip Krajinovic  OR  ( 12) Frances Tiafoe
    TEAM.draw(mens_singles).match('1.57').winner(men.Coric).in_sets(3)  # ( 15) Borna Coric  OR  (   ) Federico Coria
    TEAM.draw(mens_singles).match('1.58').winner(men.Thiem).in_sets(4)  # (   ) Dominic Thiem  OR  (   ) Pedro Cachin
    TEAM.draw(mens_singles).match('1.59').winner(men.Etcheverry).in_sets(4)  # (   ) Jack Draper  OR  (   ) Tomas Martin Etcheverry
    TEAM.draw(mens_singles).match('1.60').winner(men.De_Minaur).in_sets(4)  # (   ) Ilya Ivashka  OR  ( 18) Alex De Minaur
    TEAM.draw(mens_singles).match('1.61').winner(men.Nishioka).in_sets(3)  # ( 27) Yoshihito Nishioka  OR  (   ) J.J. Wolf
    TEAM.draw(mens_singles).match('1.62').winner(men.Purcell).in_sets(5)  # (   ) Max Purcell  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles).match('1.63').winner(men.Pella).in_sets(4)  # (   ) Quentin Halys  OR  (   ) Guido Pella
    TEAM.draw(mens_singles).match('1.64').winner(men.Medvedev).in_sets(3)  # (  Q) T.Seyboth Wild  OR  (  2) Daniil Medvedev

    TEAM.draw(womens_singles).match('1.1').winner(women.Swiatek).in_sets(2)  # (  1) Iga Swiatek  OR  (   ) Cristina Bucsa
    TEAM.draw(womens_singles).match('1.2').winner(women.Liu).in_sets(2)  # (  Q) Y.In-Albon  OR  (   ) Claire Liu
    TEAM.draw(womens_singles).match('1.3').winner(women.Peterson).in_sets(3)  # (   ) Rebecca Peterson  OR  (  Q) F.Ferro
    TEAM.draw(womens_singles).match('1.4').winner(women.Bouzkova).in_sets(2)  # (   ) Xinyu Wang  OR  ( 31) Marie Bouzkova
    TEAM.draw(womens_singles).match('1.5').winner(
        women.Azarenka).in_sets(3)  # ( 18) Victoria Azarenka  OR  (   ) Bianca Andreescu
    TEAM.draw(womens_singles).match('1.6').winner(women.Kalinskaya).in_sets(2)  # (   ) Anna Kalinskaya  OR  (  W) Emma Navarro
    TEAM.draw(womens_singles).match('1.7').winner(women.Davis).in_sets(3)  # (   ) Lin Zhu  OR  (   ) Lauren Davis
    TEAM.draw(womens_singles).match('1.8').winner(women.Krejcikova).in_sets(2)  # (   ) Lesia Tsurenko  OR  ( 13) Barbora Krejcikova
    TEAM.draw(womens_singles).match('1.9').winner(
        women.Kudermetova_Veronika).in_sets(2)  # ( 11) Veronika Kudermetova  OR  (   ) Anna Karolina Schmiedlova
    TEAM.draw(womens_singles).match('1.10').winner(women.Kucova).in_sets(3)  # (  L) Aliona Bolsova  OR  (   ) Kristina Kucova
    TEAM.draw(womens_singles).match('1.11').winner(women.Day).in_sets(3)  # (  Q) K.Day  OR  (  W) Kristina Mladenovic
    TEAM.draw(womens_singles).match('1.12').winner(women.Keys).in_sets(2)  # (   ) Kaia Kanepi  OR  ( 20) Madison Keys
    TEAM.draw(womens_singles).match('1.13').winner(women.Kalinina).in_sets(2)  # ( 25) Anhelina Kalinina  OR  (  W) Diane Parry
    TEAM.draw(womens_singles).match('1.14').winner(
        women.Riske_Amritraj).in_sets(3)  # (  Q) Mirra Andreeva  OR  (   ) Alison Riske-Amritraj
    TEAM.draw(womens_singles).match('1.15').winner(women.Grabher).in_sets(2)  # (  Q) Arantxa Rus  OR  (   ) Julia Grabher
    TEAM.draw(womens_singles).match('1.16').winner(women.Gauff).in_sets(2)  # (   ) Rebeka Masarova  OR  (  6) Coco Gauff
    TEAM.draw(womens_singles).match('1.17').winner(
        women.Rybakina).in_sets(2)  # (  4) Elena Rybakina  OR  (  Q) Brenda Fruhvirtova
    TEAM.draw(womens_singles).match('1.18').winner(women.Kovinic).in_sets(3)  # (   ) Linda Noskova  OR  (   ) Danka Kovinic
    TEAM.draw(womens_singles).match('1.19').winner(women.Sorribes_Tormo).in_sets(2)  # (  W) Clara Burel  OR  (   ) Sorribes Tormo
    TEAM.draw(womens_singles).match('1.20').winner(women.Rogers).in_sets(2)  # (   ) Petra Martic  OR  ( 32) Shelby Rogers
    TEAM.draw(womens_singles).match('1.21').winner(
        women.Alexandrova).in_sets(2)  # ( 23) Ekaterina Alexandrova  OR  (   ) Viktoriya Tomova
    TEAM.draw(womens_singles).match('1.22').winner(women.Friedsam).in_sets(2)  # (  L) Nao Hibino  OR  (   ) Anna-Lena Friedsam
    TEAM.draw(womens_singles).match('1.23').winner(women.Marino).in_sets(3)  # (   ) Rebecca Marino  OR  (   ) Diana Shnaider
    TEAM.draw(womens_singles).match('1.24').winner(
        women.Haddad_Maia).in_sets(2)  # (   ) Tatjana Maria  OR  ( 14) Beatriz Haddad Maia
    TEAM.draw(womens_singles).match('1.25').winner(
        women.Kvitova).in_sets(2)  # ( 10) Petra Kvitova  OR  (   ) Elisabetta Cocciaretto
    TEAM.draw(womens_singles).match('1.26').winner(women.Mandlik).in_sets(3)  # (  Q) Simona Waltert  OR  (  Q) Elizabeth Mandlik
    TEAM.draw(womens_singles).match('1.27').winner(women.Kontaveit).in_sets(3)  # (   ) Anett Kontaveit  OR  (   ) Bernarda Pera
    TEAM.draw(womens_singles).match('1.28').winner(women.Vekic).in_sets(2)  # (  Q) Dayana Yastremska  OR  ( 22) Donna Vekic
    TEAM.draw(womens_singles).match('1.29').winner(women.Cirstea).in_sets(3)  # ( 30) Sorana Cirstea  OR  (   ) Jasmine Paolini
    TEAM.draw(womens_singles).match('1.30').winner(women.Baindl).in_sets(3)  # (  Q) Olga Danilovic  OR  (   ) Kateryna Baindl
    TEAM.draw(womens_singles).match('1.31').winner(women.Dodin).in_sets(2)  # (  W) Selena Janicijevic  OR  (   ) Dodin
    TEAM.draw(womens_singles).match('1.32').winner(women.Jabeur).in_sets(2)  # (   ) Lucia Bronzetti  OR  (  7) Ons Jabeur
    TEAM.draw(womens_singles).match('1.33').winner(women.Sakkari).in_sets(2)  # (  8) Maria Sakkari  OR  (   ) Karolina Muchova
    TEAM.draw(womens_singles).match('1.34').winner(women.Podoroska).in_sets(3)  # (   ) Nadia Podoroska  OR  (  W) Ponchet
    TEAM.draw(womens_singles).match('1.35').winner(women.Teichmann).in_sets(3)  # (   ) Sara Errani  OR  (   ) Jil Teichmann
    TEAM.draw(womens_singles).match('1.36').winner(women.Begu).in_sets(2)  # (   ) Anna Bondar  OR  ( 27) Irina-Camelia Begu
    TEAM.draw(womens_singles).match('1.37').winner(women.Linette).in_sets(2)  # ( 21) Magda Linette  OR  (   ) Leylah Fernandez
    TEAM.draw(womens_singles).match('1.38').winner(women.Sasnovich).in_sets(2)  # (  Q) C.Tauson  OR  (   ) Aliaksandra Sasnovich
    TEAM.draw(womens_singles).match('1.39').winner(women.Jeanjean).in_sets(3)  # (  W) Leolia Jeanjean  OR  (  W) Kimberly Birrell
    TEAM.draw(womens_singles).match('1.40').winner(women.Bencic).in_sets(2)  # (  L) Elina Avanesyan  OR  ( 12) Belinda Bencic
    TEAM.draw(womens_singles).match('1.41').winner(
        women.Samsonova).in_sets(2)  # ( 15) Liudmila Samsonova  OR  (   ) Katie Volynets
    TEAM.draw(womens_singles).match('1.42').winner(
        women.Fruhvirtova_Linda).in_sets(3)  # (   ) Anastasia Pavlyuchenkova  OR  (   ) Linda Fruhvirtova
    TEAM.draw(womens_singles).match('1.43').winner(women.Sherif).in_sets(3)  # (   ) Mayar Sherif  OR  (   ) Madison Brengle
    TEAM.draw(womens_singles).match('1.44').winner(
        women.Potapova).in_sets(2)  # (  Q) Taylor Townsend  OR  ( 24) Anastasia Potapova
    TEAM.draw(womens_singles).match('1.45').winner(women.Mertens).in_sets(2)  # ( 28) Elise Mertens  OR  (  L) V.Hruncakova
    TEAM.draw(womens_singles).match('1.46').winner(women.Bogdan).in_sets(3)  # (   ) Catherine McNally  OR  (   ) Ana Bogdan
    TEAM.draw(womens_singles).match('1.47').winner(women.Giorgi).in_sets(3)  # (   ) Alize Cornet  OR  (   ) Camila Giorgi
    TEAM.draw(womens_singles).match('1.48').winner(women.Pegula).in_sets(2)  # (   ) Danielle Collins  OR  (  3) Jessica Pegula
    TEAM.draw(womens_singles).match('1.49').winner(women.Garcia).in_sets(2)  # (  5) Caroline Garcia  OR  (   ) Xinyu Wang
    TEAM.draw(womens_singles).match('1.50').winner(
        women.Bonaventure).in_sets(3)  # (   ) Anna Blinkova  OR  (   ) Ysaline Bonaventure
    TEAM.draw(womens_singles).match('1.51').winner(women.Parrizas_Diaz).in_sets(2)  # (   ) Nuria Parrizas Diaz  OR  (  Q) Storm Hunter
    TEAM.draw(womens_singles).match('1.52').winner(women.Trevisan).in_sets(2)  # (   ) Svitolina  OR  ( 26) Martina Trevisan
    TEAM.draw(womens_singles).match('1.53').winner(
        women.Ostapenko).in_sets(2)  # ( 17) Jelena Ostapenko  OR  (   ) Tereza Martincova
    TEAM.draw(womens_singles).match('1.54').winner(
        women.Siniakova).in_sets(3)  # (   ) Peyton Stearns  OR  (   ) Katerina Siniakova
    TEAM.draw(womens_singles).match('1.55').winner(women.Vondrousova).in_sets(3)  # (   ) Marketa Vondrousova  OR  (   ) Alycia Parks
    TEAM.draw(womens_singles).match('1.56').winner(women.Kasatkina).in_sets(2)  # (   ) Jule Niemeier  OR  (  9) Daria Kasatkina
    TEAM.draw(womens_singles).match('1.57').winner(
        women.Pliskova).in_sets(2)  # ( 16) Karolina Pliskova  OR  (   ) Sloane Stephens
    TEAM.draw(womens_singles).match('1.58').winner(women.Gracheva).in_sets(3)  # (   ) Varvara Gracheva  OR  (   ) Dalma Galfi
    TEAM.draw(womens_singles).match('1.59').winner(women.Putintseva).in_sets(3)  # (   ) Yulia Putintseva  OR  (   ) Maryna Zanevska
    TEAM.draw(womens_singles).match('1.60').winner(women.Zheng).in_sets(2)  # (  Q) Tamara Zidansek  OR  ( 19) Qinwen Zheng
    TEAM.draw(womens_singles).match('1.61').winner(women.Zhang_Shuai).in_sets(2)  # ( 29) Shuai Zhang  OR  (   ) Magdalena Frech
    TEAM.draw(womens_singles).match('1.62').winner(women.Rakhimova).in_sets(2)  # (  Q) Sara Bejlek  OR  (   ) Kamilla Rakhimova
    TEAM.draw(womens_singles).match('1.63').winner(women.Udvardy).in_sets(3)  # (   ) Panna Udvardy  OR  (  Q) I.Shymanovich
    TEAM.draw(womens_singles).match('1.64').winner(women.Sabalenka).in_sets(2)  # (   ) Marta Kostyuk  OR  (  2) Aryna Sabalenka


    return TeamFauve

