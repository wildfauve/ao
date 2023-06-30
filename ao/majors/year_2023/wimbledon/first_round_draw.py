from ao.players import atp_players, wta_players
from ao import model


def womens_draw_round_1():
    return [
            (1, wta_players.Swiatek, wta_players.Zhu),
            (2, wta_players.Trevisan, wta_players.Sorribes_Tormo),
            (3, wta_players.Parry, wta_players.Dart),
            (4, wta_players.Fruhvirtova_Linda, wta_players.Martic),
            (5, wta_players.Linette, wta_players.Teichmann),
            (6, wta_players.Strycova, wta_players.Zanevska),
            (7, wta_players.Collins, wta_players.Grabher),
            (8, wta_players.Swan, wta_players.Bencic),
            (9, wta_players.Kasatkina, wta_players.Dolehide),
            (10, wta_players.Burrage, wta_players.Mcnally),
            (11, wta_players.Podoroska, wta_players.Martincova),
            (12, wta_players.Yuan, wta_players.Azarenka),
            (13, wta_players.Mertens, wta_players.Hruncakova),
            (14, wta_players.Williams, wta_players.Svitolina),
            (15, wta_players.Hunter, wta_players.Wang_Xinyu),
            (16, wta_players.Kenin, wta_players.Gauff),
            (17, wta_players.Pegula, wta_players.Davis),
            (18, wta_players.Bucsa, wta_players.Rakhimova),
            (19, wta_players.Osorio, wta_players.Cocciaretto),
            (20, wta_players.Masarova, wta_players.Sherif),
            (21, wta_players.Zheng, wta_players.Siniakova),
            (22, wta_players.Tsurenko, wta_players.Liu),
            (23, wta_players.Parks, wta_players.Friedsam),
            (24, wta_players.Bogdan, wta_players.Samsonova),
            (25, wta_players.Kudermetova_Veronika, wta_players.Kanepi),
            (26, wta_players.Vondrousova, wta_players.Stearns),
            (27, wta_players.Stephens, wta_players.Peterson),
            (28, wta_players.Zhang_Shuai, wta_players.Vekic),
            (29, wta_players.Bouzkova, wta_players.Waltert),
            (30, wta_players.Kontaveit, wta_players.Stefanini),
            (31, wta_players.Baindl, wta_players.Fernandez),
            (32, wta_players.Volynets, wta_players.Garcia),
            (33, wta_players.Jabeur, wta_players.Frech),
            (34, wta_players.Bonaventure, wta_players.Bai),
            (35, wta_players.Bondar, wta_players.Andreescu),
            (36, wta_players.Maneiro, wta_players.Kalinina),
            (37, wta_players.Pliskova, wta_players.Stevanovic),
            (38, wta_players.Zhao, wta_players.Korpatsch),
            (39, wta_players.Sasnovich, wta_players.Parrizas_Diaz),
            (40, wta_players.Paolini, wta_players.Kvitova),
            (41, wta_players.Haddad_Maia, wta_players.Putintseva),
            (42, wta_players.Cristian, wta_players.Bronzetti),
            (43, wta_players.Cirstea, wta_players.Maria),
            (44, wta_players.Minnen, wta_players.Ostapenko),
            (45, wta_players.Pera, wta_players.Tomova),
            (46, wta_players.Boulter, wta_players.Saville),
            (47, wta_players.Hibino, wta_players.Cornet),
            (48, wta_players.Rogers, wta_players.Rybakina),
            (49, wta_players.Sakkari, wta_players.Kostyuk),
            (50, wta_players.Riske_Amritraj, wta_players.Badosa),
            (51, wta_players.Golubic, wta_players.Schmiedlova),
            (52, wta_players.Kartal, wta_players.Keys),
            (53, wta_players.Potapova, wta_players.Naef),
            (54, wta_players.Juvan, wta_players.Betova),
            (55, wta_players.Andreeva_Mirra, wta_players.Wang_Xiyu),
            (56, wta_players.Watson, wta_players.Krejcikova),
            (57, wta_players.Muchova, wta_players.Niemeier),
            (58, wta_players.Noskova, wta_players.Galfi),
            (59, wta_players.Brengle, wta_players.Errani),
            (60, wta_players.Navarro, wta_players.Alexandrova),
            (61, wta_players.Begu, wta_players.Marino),
            (62, wta_players.Wickmayer, wta_players.Blinkova),
            (63, wta_players.Gracheva, wta_players.Giorgi),
            (64, wta_players.Udvardy, wta_players.Sabalenka),

   ]
def mens_draw_round_1():
    return [
            (1, atp_players.Alcaraz, atp_players.Chardy),
            (2, atp_players.Muller, atp_players.Rinderknech),
            (3, atp_players.Kubler, atp_players.Humbert),
            (4, atp_players.Cecchinato, atp_players.Jarry),
            (5, atp_players.Zverev, atp_players.Brouwer),
            (6, atp_players.Huesler, atp_players.Watanuki),
            (7, atp_players.Berrettini, atp_players.Sonego),
            (8, atp_players.Coppejans, atp_players.De_Minaur),
            (9, atp_players.Tiafoe, atp_players.Wu),
            (10, atp_players.Stricker, atp_players.Popyrin),
            (11, atp_players.Ivashka, atp_players.Coria),
            (12, atp_players.Shimabukuro, atp_players.Dimitrov),
            (13, atp_players.Davidovich_Fokina, atp_players.Fils),
            (14, atp_players.Zhang_Zhizhen, atp_players.Van_De_Zandschulp),
            (15, atp_players.Arnaldi, atp_players.Carballes_Baena),
            (16, atp_players.Loffhagen, atp_players.Rune),
            (17, atp_players.Medvedev, atp_players.Fery),
            (18, atp_players.Mannarino, atp_players.Shevchenko),
            (19, atp_players.Giron, atp_players.Dellien),
            (20, atp_players.Fucsovics, atp_players.Griekspoor),
            (21, atp_players.Cerundolo_Francisco, atp_players.Borges),
            (22, atp_players.Lehecka, atp_players.Ofner),
            (23, atp_players.Raonic, atp_players.Novak),
            (24, atp_players.Mochizuki, atp_players.Paul),
            (25, atp_players.Norrie, atp_players.Machac),
            (26, atp_players.Eubanks, atp_players.Monteiro),
            (27, atp_players.OConnell, atp_players.Medjedovic),
            (28, atp_players.Vesely, atp_players.Korda),
            (29, atp_players.Shelton, atp_players.Daniel),
            (30, atp_players.Cressy, atp_players.Djere),
            (31, atp_players.Peniston, atp_players.Murray_Andy),
            (32, atp_players.Thiem, atp_players.Tsitsipas),
            (33, atp_players.Sinner, atp_players.Cerundolo_Juan),
            (34, atp_players.Kecmanovic, atp_players.Schwartzman),
            (35, atp_players.Vukic, atp_players.Altmaier),
            (36, atp_players.Halys, atp_players.Evans),
            (37, atp_players.Nishioka, atp_players.Galan),
            (38, atp_players.Koepfer, atp_players.Otte),
            (39, atp_players.Ymer_Mikael, atp_players.Molcan),
            (40, atp_players.Hanfmann, atp_players.Fritz),
            (41, atp_players.Coric, atp_players.Pella),
            (42, atp_players.Bonzi, atp_players.Mayot),
            (43, atp_players.Moutet, atp_players.Gasquet),
            (44, atp_players.Safiullin, atp_players.Bautista_Agut),
            (45, atp_players.Shapovalov, atp_players.Albot),
            (46, atp_players.Harris, atp_players.Barrere),
            (47, atp_players.Broady, atp_players.Lestienne),
            (48, atp_players.Lokoli, atp_players.Ruud),
            (49, atp_players.Rublev, atp_players.Purcell),
            (50, atp_players.Van_Assche, atp_players.Karatsev),
            (51, atp_players.Baez, atp_players.Vera),
            (52, atp_players.Goffin, atp_players.Kyrgios),
            (53, atp_players.Bublik, atp_players.Mcdonald),
            (54, atp_players.Wolf, atp_players.Couacaud),
            (55, atp_players.Marterer, atp_players.Gojo),
            (56, atp_players.Krajinovic, atp_players.Auger_Aliassime),
            (57, atp_players.Musetti, atp_players.Varillas),
            (58, atp_players.Isner, atp_players.Munar),
            (59, atp_players.Choinski, atp_players.Lajovic),
            (60, atp_players.Ramos_Vinolas, atp_players.Hurkacz),
            (61, atp_players.Etcheverry, atp_players.Zapata_Miralles),
            (62, atp_players.Ruusuvuori, atp_players.Wawrinka),
            (63, atp_players.Thompson, atp_players.Nakashima),
            (64, atp_players.Cachin, atp_players.Djokovic),
   ]