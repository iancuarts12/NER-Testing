train_data = [
    # TRAIN_DATA for NER training
    ("Mark Lester Cabaluna performed toilet maintenance in Makati yesterday.",
     {'entities': [(0, 20, 'PERSON'), (31, 49, 'SERVICE'), (53, 59, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Maria Clara Santos offers Drain unclogging services for homes in Pasig.",
     {'entities': [(0, 18, 'PERSON'), (26, 42, 'SERVICE'), (65, 70, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Luis Miguel Reyes specializes in Plumbing and pipe repair for clients in Mandaluyong.",
     {'entities': [(0, 17, 'PERSON'), (33, 41, 'SPECIALIZATION'), (46, 57, 'SERVICE'), (73, 84, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Adrian D. Cuarteros provided washing machine maintenance for a household in Malabon.",
     {'entities': [(0, 19, 'PERSON'), (29, 56, 'SERVICE'), (76, 83, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("The electrician Kevin John Bautista handled electrical wiring and rewiring in Taguig.",
     {'entities': [(4, 15, 'SPECIALIZATION'), (16, 35, 'PERSON'), (44, 74, 'SERVICE'), (78, 84, 'GPE')]}),
    # CHANGED: reordered entity list to match sentence word order so offsets are correct

    ("We scheduled a refrigerator maintenance with Juan Dela Cruz at a Pasay residence.",
     {'entities': [(15, 39, 'SERVICE'), (45, 59, 'PERSON'), (65, 70, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Housekeeping team led by Maria Teresa Lopez did deep cleaning at the office in Quezon.",
     {'entities': [(0, 12, 'SPECIALIZATION'), (25, 43, 'PERSON'), (48, 61, 'SERVICE'), (79, 85, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("I want sofa maintenance for the old couch — contacted Antonio Ramos in Marikina.",
     {'entities': [(7, 23, 'SERVICE'), (54, 67, 'PERSON'), (71, 79, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Pablo Reyes is a plumber who offers toilet maintenance and drain unclogging in Navotas.",
     {'entities': [(0, 11, 'PERSON'), (17, 24, 'SPECIALIZATION'), (36, 54, 'SERVICE'), (59, 75, 'SERVICE'), (79, 86, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Engineers called by Kevin Lee performed water heater maintenance in Muntinlupa.",
     {'entities': [(20, 29, 'PERSON'), (40, 64, 'SERVICE'), (68, 78, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Sofia Garcia did cabinet maintenance after the flood in Parañaque.",
     {'entities': [(0, 12, 'PERSON'), (17, 36, 'SERVICE'), (56, 65, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Office requested general cleaning and laundry; contact person is Mark Anthony Delacruz in San Juan.",
     {'entities': [(17, 33, 'SERVICE'), (38, 45, 'SERVICE'), (65, 86, 'PERSON'), (90, 98, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Repaired the electric fan; technician Juan Pablo Santos listed electric fan maintenance as the service in Valenzuela.",
     {'entities': [(38, 55, 'PERSON'), (63, 87, 'SERVICE'), (106, 116, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Angela Reyes scheduled refrigerator maintenance for a client in Muntinlupa.",
     {'entities': [(0, 12, 'PERSON'), (23, 47, 'SERVICE'), (64, 74, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Cleaning crew from Parañaque performed deep cleaning and general cleaning; supervisor is Roberto Cruz.",
     {'entities': [(19, 28, 'GPE'), (39, 52, 'SERVICE'), (57, 73, 'SERVICE'), (89, 101, 'PERSON')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Mr. Benjamin Santos performed sink and faucet maintenance at a house in Pateros.",
     {'entities': [(4, 19, 'PERSON'), (30, 57, 'SERVICE'), (72, 79, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("The team led by Electrician Jose Miguel Duran did socket maintenance and lighting maintenance in Manila.",
     {'entities': [(16, 27, 'SPECIALIZATION'), (28, 45, 'PERSON'), (50, 68, 'SERVICE'), (73, 93, 'SERVICE'), (97, 103, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("We called Ana Lucia Rivera for water line maintenance after the burst in Quezon.",
     {'entities': [(10, 26, 'PERSON'), (31, 53, 'SERVICE'), (73, 79, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Alfredo Gonzales does bathtub maintenance and pipe repair around Makati.",
     {'entities': [(0, 16, 'PERSON'), (22, 41, 'SERVICE'), (46, 57, 'SERVICE'), (65, 71, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists

    ("Household appliances: Television maintenance, air conditioner maintenance, and refrigerator maintenance offered by Appliance Maintenance expert Maria Elena Cruz in Taguig.",
     {'entities': [(22, 44, 'SERVICE'), (46, 73, 'SERVICE'), (79, 103, 'SERVICE'), (115, 136, 'SPECIALIZATION'), (144, 160, 'PERSON'), (164, 170, 'GPE')]}),
    # Verified indices and ensured labels belong to the allowed SERVICE/SPECIALIZATION lists
]