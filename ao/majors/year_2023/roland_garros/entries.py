from typing import Tuple, List, Optional
from ao import model
from ao.players import atp_players, wta_players


def mens_singles_entries():
    return [
        (atp_players.Alcaraz, '1'),
        (atp_players.Cobolli, 'Q'),
        (atp_players.OConnell, None),
        (atp_players.Daniel, None),
        (atp_players.Arnaldi, None),
        (atp_players.Galan, None),
        (atp_players.Nakashima, None),
        (atp_players.Shapovalov, '26'),
        (atp_players.Musetti, '17'),
        (atp_players.Ymer_Mikael, None),
        (atp_players.Shevchenko, None),
        (atp_players.Otte, None),
        (atp_players.Pouille, 'Q'),
        (atp_players.Rodionov, 'L'),
        (atp_players.Paire, 'W'),
        (atp_players.Norrie, '14'),
        (atp_players.Auger_Aliassime, '10'),
        (atp_players.Fognini, None),
        (atp_players.Kubler, None),
        (atp_players.Diaz_Acosta, 'L'),
        (atp_players.Ofner, 'Q'),
        (atp_players.Cressy, None),
        (atp_players.Mcdonald, None),
        (atp_players.Korda, '24'),
        (atp_players.Zapata_Miralles, '32'),
        (atp_players.Schwartzman, None),
        (atp_players.Isner, None),
        (atp_players.Borges, None),
        (atp_players.Carballes_Baena, None),
        (atp_players.Nava, 'Q'),
        (atp_players.Vesely, None),
        (atp_players.Tsitsipas, '5'),
        (atp_players.Djokovic, '3'),
        (atp_players.Kovacevic, None),
        (atp_players.Fucsovics, None),
        (atp_players.Grenier, 'W'),
        (atp_players.Van_Assche, None),
        (atp_players.Cecchinato, None),
        (atp_players.Fils, 'W'),
        (atp_players.Davidovich_Fokina, '29'),
        (atp_players.Bautista_Agut, '19'),
        (atp_players.Wu, None),
        (atp_players.Shang, 'Q'),
        (atp_players.Varillas, None),
        (atp_players.Martinez, 'Q'),
        (atp_players.Griekspoor, None),
        (atp_players.Goffin, None),
        (atp_players.Hurkacz, '13'),
        (atp_players.Khachanov, '11'),
        (atp_players.Lestienne, None),
        (atp_players.Kypson, 'W'),
        (atp_players.Albot, 'Q'),
        (atp_players.Wawrinka, None),
        (atp_players.Ramos_Vinolas, None),
        (atp_players.Kokkinakis, 'W'),
        (atp_players.Evans, '20'),
        (atp_players.Shelton, '30'),
        (atp_players.Sonego, None),
        (atp_players.Mannarino, None),
        (atp_players.Humbert, None),
        (atp_players.Cazaux, 'W'),
        (atp_players.Moutet, None),
        (atp_players.Djere, None),
        (atp_players.Rublev, '7'),
        (atp_players.Rune, '6'),
        (atp_players.Eubanks, None),
        (atp_players.Monfils, None),
        (atp_players.Baez, None),
        (atp_players.Mpetshi_Perricard, 'W'),
        (atp_players.Olivieri, 'Q'),
        (atp_players.Vavassori, 'Q'),
        (atp_players.Kecmanovic, '31'),
        (atp_players.Cerundolo_Francisco, '23'),
        (atp_players.Munar, None),
        (atp_players.Monteiro, None),
        (atp_players.Hanfmann, "L"),
        (atp_players.Gasquet, None),
        (atp_players.Rinderknech, None),
        (atp_players.Mmoh, None),
        (atp_players.Fritz, '9'),
        (atp_players.Paul, '16'),
        (atp_players.Stricker, 'L'),
        (atp_players.Jarry, None),
        (atp_players.Dellien, None),
        (atp_players.Medjedovic, 'Q'),
        (atp_players.Giron, None),
        (atp_players.Lehecka, None),
        (atp_players.Struff, '21'),
        (atp_players.Van_De_Zandschulp, '25'),
        (atp_players.Tirante, 'Q'),
        (atp_players.Zhang_Zhizhen, None),
        (atp_players.Lajovic, None),
        (atp_players.Bublik, None),
        (atp_players.Zeppieri, 'Q'),
        (atp_players.Ymer_Elias, 'Q'),
        (atp_players.Ruud, '4'),
        (atp_players.Sinner, '8'),
        (atp_players.Muller, None),
        (atp_players.Altmaier, None),
        (atp_players.Huesler, None),
        (atp_players.Ruusuvuori, None),
        (atp_players.Barrere, None),
        (atp_players.Skatov, 'Q'),
        (atp_players.Dimitrov, '28'),
        (atp_players.Zverev, '22'),
        (atp_players.Harris, None),
        (atp_players.Gaston, 'W'),
        (atp_players.Molcan, None),
        (atp_players.Popyrin, None),
        (atp_players.Karatsev, 'Q'),
        (atp_players.Krajinovic, None),
        (atp_players.Tiafoe, '12'),
        (atp_players.Coric, '15'),
        (atp_players.Coria, None),
        (atp_players.Thiem, None),
        (atp_players.Cachin, None),
        (atp_players.Draper, None),
        (atp_players.Etcheverry, None),
        (atp_players.Ivashka, None),
        (atp_players.De_Minaur, '18'),
        (atp_players.Nishioka, '27'),
        (atp_players.Wolf, None),
        (atp_players.Purcell, None),
        (atp_players.Thompson, None),
        (atp_players.Halys, None),
        (atp_players.Pella, None),
        (atp_players.Seyboth_Wild, 'Q'),
        (atp_players.Medvedev, '2'),

    ]


def womens_singles_entries():
    return [
        (wta_players.Swiatek, '1'),
        (wta_players.Bucsa, None),
        (wta_players.In_Albon, 'Q'),
        (wta_players.Liu, None),
        (wta_players.Peterson, None),
        (wta_players.Ferro, 'Q'),
        (wta_players.Wang_Xinyu, None),
        (wta_players.Bouzkova, '31'),
        (wta_players.Azarenka, '18'),
        (wta_players.Andreescu, None),
        (wta_players.Andreeva_Erika, None),
        (wta_players.Navarro, 'W'),
        (wta_players.Zhu, None),
        (wta_players.Davis, None),
        (wta_players.Tsurenko, None),
        (wta_players.Krejcikova, '13'),
        (wta_players.Kudermetova_Veronika, '11'),
        (wta_players.Schmiedlova, None),
        (wta_players.Bolsova, 'L'),
        (wta_players.Kucova, None),
        (wta_players.Day, 'Q'),
        (wta_players.Mladenovic, 'W'),
        (wta_players.Kanepi, None),
        (wta_players.Keys, '20'),
        (wta_players.Kalinina, '25'),
        (wta_players.Parry, 'W'),
        (wta_players.Andreeva_Mirra, 'Q'),
        (wta_players.Riske_Amritraj, None),
        (wta_players.Rus, 'Q'),
        (wta_players.Grabher, None),
        (wta_players.Masarova, None),
        (wta_players.Gauff, '6'),
        (wta_players.Rybakina, '4'),
        (wta_players.Fruhvirtova_Brenda, 'Q'),
        (wta_players.Noskova, None),
        (wta_players.Kovinic, None),
        (wta_players.Burel, 'W'),
        (wta_players.Sorribes_Tormo, None),
        (wta_players.Martic, None),
        (wta_players.Rogers, '32'),
        (wta_players.Alexandrova, '23'),
        (wta_players.Tomova, None),
        (wta_players.Hibino, 'L'),
        (wta_players.Friedsam, None),
        (wta_players.Marino, None),
        (wta_players.Shnaider, None),
        (wta_players.Maria, None),
        (wta_players.Haddad_Maia, '14'),
        (wta_players.Kvitova, '10'),
        (wta_players.Cocciaretto, None),
        (wta_players.Waltert, 'Q'),
        (wta_players.Mandlik, 'Q'),
        (wta_players.Kontaveit, None),
        (wta_players.Pera, None),
        (wta_players.Yastremska, 'Q'),
        (wta_players.Vekic, '22'),
        (wta_players.Cirstea, '30'),
        (wta_players.Paolini, None),
        (wta_players.Danilovic, 'Q'),
        (wta_players.Baindl, None),
        (wta_players.Janicijevic, 'W'),
        (wta_players.Dodin, None),
        (wta_players.Bronzetti, None),
        (wta_players.Jabeur, '7'),
        (wta_players.Sakkari, '8'),
        (wta_players.Muchova, None),
        (wta_players.Podoroska, None),
        (wta_players.Ponchet, 'W'),
        (wta_players.Errani, None),
        (wta_players.Teichmann, None),
        (wta_players.Bondar, None),
        (wta_players.Begu, '27'),
        (wta_players.Linette, '21'),
        (wta_players.Fernandez, None),
        (wta_players.Tauson, 'Q'),
        (wta_players.Sasnovich, None),
        (wta_players.Jeanjean, 'W'),
        (wta_players.Birrell, 'W'),
        (wta_players.Avanesyan, 'L'),
        (wta_players.Bencic, '12'),
        (wta_players.Samsonova, '15'),
        (wta_players.Volynets, None),
        (wta_players.Pavlyuchenkova, None),
        (wta_players.Fruhvirtova_Linda, None),
        (wta_players.Sherif, None),
        (wta_players.Brengle, None),
        (wta_players.Townsend, 'Q'),
        (wta_players.Potapova, '24'),
        (wta_players.Mertens, '28'),
        (wta_players.Hruncakova, 'L'),
        (wta_players.Osorio, "L"),
        (wta_players.Bogdan, None),
        (wta_players.Cornet, None),
        (wta_players.Giorgi, None),
        (wta_players.Collins, None),
        (wta_players.Pegula, '3'),
        (wta_players.Garcia, '5'),
        (wta_players.Wang_Xinyu, None),
        (wta_players.Blinkova, None),
        (wta_players.Bonaventure, None),
        (wta_players.Parrizas_Diaz, None),
        (wta_players.Hunter, 'Q'),
        (wta_players.Svitolina, None),
        (wta_players.Trevisan, '26'),
        (wta_players.Ostapenko, '17'),
        (wta_players.Martincova, None),
        (wta_players.Stearns, None),
        (wta_players.Siniakova, None),
        (wta_players.Vondrousova, None),
        (wta_players.Parks, None),
        (wta_players.Niemeier, None),
        (wta_players.Kasatkina, '9'),
        (wta_players.Pliskova, '16'),
        (wta_players.Stephens, None),
        (wta_players.Gracheva, None),
        (wta_players.Galfi, None),
        (wta_players.Putintseva, None),
        (wta_players.Zanevska, None),
        (wta_players.Zidansek, 'Q'),
        (wta_players.Zheng, '19'),
        (wta_players.Zhang_Shuai, '29'),
        (wta_players.Frech, None),
        (wta_players.Bejlek, 'Q'),
        (wta_players.Rakhimova, None),
        (wta_players.Udvardy, None),
        (wta_players.Shymanovich, 'Q'),
        (wta_players.Kostyuk, None),
        (wta_players.Sabalenka, '2'),

    ]
