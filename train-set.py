train_data = [

    # --- Toilet Maintenance ---
    ("My father John is a plumber and he frequently performs toilet maintenance.",
     {"entities": [(10, 14, "PERSON"), (19, 26, "SPECIALIZATION"), (54, 72, "SERVICE")]}),

    ("Yesterday Mike handled a toilet repair task after a client complaint.",
     {"entities": [(10, 14, "PERSON"), (24, 38, "SKILL")]}), 

    ("The plumber David is skilled at toilet unclogging and flushing system repair.",
     {"entities": [(4, 11, "SPECIALIZATION"), (12, 17, "PERSON"), (35, 51, "SKILL"), (56, 77, "SKILL")]}),  

    ("Sarah Johnson specializes in toilet installation and toilet replacement for households.",
     {"entities": [(0, 13, "PERSON"), (27, 45, "SKILL"), (50, 68, "SKILL")]}), 

    # --- Sink and Faucet Maintenance ---
    ("A plumber Sarah usually manages sink and faucet maintenance in apartments.",
     {"entities": [(2, 9, "SPECIALIZATION"), (10, 15, "PERSON"), (32, 57, "SERVICE")]}), 

    ("Robert Chen installed a faucet yesterday — that was a proper faucet installation job.",
     {"entities": [(0, 11, "PERSON"), (61, 79, "SKILL")]}), 

    ("Our team did faucet repair and sink replacement last week.",
     {"entities": [(16, 28, "SKILL"), (33, 49, "SKILL")]}),  

    ("The leak fixing task was completed under sink repair services.",
     {"entities": [(4, 15, "SKILL"), (47, 58, "SKILL")]}),

    # --- Drain Unclogging ---
    ("They called us for drain unclogging and hydro jetting service.",
     {"entities": [(19, 34, "SERVICE"), (39, 53, "SKILL")]}),  

    ("The technician performed drain snaking yesterday.",
     {"entities": [(26, 38, "SKILL")]}),  

    ("Pipe inspection was part of the drain cleaning procedure.",
     {"entities": [(0, 14, "SKILL"), (34, 48, "SKILL")]}),

    # --- Shower Maintenance ---
    ("We often handle shower maintenance like showerhead installation and repair.",
     {"entities": [(0, 2, "PERSON"), (17, 34, "SERVICE"), (40, 62, "SKILL"), (67, 73, "SKILL")]}), 

    ("Maria Garcia completed leak fixing and valve replacement for shower maintenance.",
     {"entities": [(0, 12, "PERSON"), (21, 32, "SKILL"), (37, 54, "SKILL"), (60, 77, "SERVICE")]}),  

    # --- Bathtub Maintenance ---
    ("The plumber completed bathtub installation yesterday.",
     {"entities": [(4, 11, "SPECIALIZATION"), (21, 41, "SKILL")]}),

    ("James Wilson handled caulking and sealing after bathtub repair jobs.",
     {"entities": [(0, 12, "PERSON"), (21, 41, "SKILL"), (47, 60, "SKILL")]}),  

    ("Leak fixing and drain repair are common for bathtub maintenance.",
     {"entities": [(0, 11, "SKILL"), (16, 28, "SKILL"), (42, 60, "SERVICE")]}),  

    # --- Pipe Repair ---
    ("Pipe repair involves pipe welding, pipe cutting, and joint sealing.",
     {"entities": [(0, 10, "SERVICE"), (20, 31, "SKILL"), (34, 45, "SKILL"), (51, 63, "SKILL")]}),

    ("Leak detection and pipe replacement are critical for plumbers.",
     {"entities": [(0, 14, "SKILL"), (19, 35, "SKILL"), (52, 60, "SPECIALIZATION")]}), 

    # --- Water Line Maintenance ---
    ("Water line maintenance requires pressure testing and pipe fitting.",
     {"entities": [(0, 21, "SERVICE"), (32, 47, "SKILL"), (52, 63, "SKILL")]}),  

    ("Pipe connection is essential for water line repair services.",
     {"entities": [(0, 15, "SKILL"), (33, 48, "SKILL")]}), 

    # --- Water Heater Maintenance ---
    ("The team carried out water heater maintenance with sediment flushing.",
     {"entities": [(20, 43, "SERVICE"), (50, 66, "SKILL")]}), 

    ("Thermostat adjustment is a key part of water heater maintenance.",
     {"entities": [(0, 21, "SKILL"), (32, 55, "SERVICE")]}),  

    # --- Lighting Maintenance ---
    ("The electrician Maria was hired for lighting maintenance at the office.",
     {"entities": [(4, 15, "SPECIALIZATION"), (16, 21, "PERSON"), (40, 59, "SERVICE")]}),  

    ("He completed an LED light installation yesterday.",
     {"entities": [(0, 2, "PERSON"), (16, 39, "SKILL")]}),  

    ("Incandescent light installation and bulb replacement were requested.",
     {"entities": [(0, 30, "SKILL"), (36, 52, "SKILL")]}), 

    ("Fluorescent light installation was done by the electrician.",
     {"entities": [(0, 32, "SKILL"), (44, 55, "SPECIALIZATION")]}), 

    ("Emily Davis specializes in light fixture installment and LED light installation.",
     {"entities": [(0, 11, "PERSON"), (25, 49, "SKILL"), (55, 78, "SKILL")]}),  

    # --- Electrical Wiring and Rewiring ---
    ("Electrical wiring and rewiring often requires conduit installation and wire installation.",
     {"entities": [(0, 30, "SERVICE"), (48, 67, "SKILL"), (73, 89, "SKILL")]}),  

    ("The electrician handled circuit connection and electrical insulation jobs.",
     {"entities": [(4, 15, "SPECIALIZATION"), (24, 41, "SKILL"), (47, 69, "SKILL")]}), 

    # --- Socket Maintenance ---
    ("Socket maintenance includes socket replacement and socket installation.",
     {"entities": [(0, 17, "SERVICE"), (28, 45, "SKILL"), (51, 68, "SKILL")]}),  

    ("The technician completed childproof outlet installation for safety.",
     {"entities": [(25, 54, "SKILL")]}),  

    ("Copper sweating and socket tester use are common tasks.",
     {"entities": [(0, 14, "SKILL"), (20, 33, "SKILL")]}), 

    # --- Washing Machine Maintenance ---
    ("The technician did washing machine maintenance yesterday.",
     {"entities": [(20, 46, "SERVICE")]}),  

    ("I handled washing machine repair and hose replacement tasks.",
     {"entities": [(0, 1, "PERSON"), (10, 33, "SKILL"), (39, 55, "SKILL")]}),  

    ("Belt replacement and drum cleaning are common for washing machines.",
     {"entities": [(0, 15, "SKILL"), (21, 33, "SKILL")]}),  

    ("Michael Brown specializes in leak tracking and washing machine repair.",
     {"entities": [(0, 13, "PERSON"), (26, 38, "SKILL"), (43, 66, "SKILL")]}),  

    # --- Television Maintenance ---
    ("Television maintenance includes screen repair and remote sensor repair.",
     {"entities": [(0, 22, "SERVICE"), (33, 45, "SKILL"), (51, 71, "SKILL")]}),  

    ("The electrician completed backlight replacement and power supply board repair.",
     {"entities": [(4, 15, "SPECIALIZATION"), (27, 48, "SKILL"), (54, 78, "SKILL")]}),

    ("Screen replacement and backlight repair are common TV jobs.",
     {"entities": [(0, 18, "SKILL"), (24, 40, "SKILL")]}), 

    # --- Electric Fan Maintenance ---
    ("The team managed electric fan maintenance with motor cleaning and lubrication.",
     {"entities": [(17, 40, "SERVICE"), (47, 60, "SKILL"), (66, 77, "SKILL")]}),  

    ("Blade replacement and bearing replacement are standard fan tasks.",
     {"entities": [(0, 16, "SKILL"), (22, 40, "SKILL")]}),  

    ("Oscillation mechanism repair is often needed in fan servicing.",
     {"entities": [(0, 28, "SKILL")]}),  

    ("Jennifer Lee fixed the speed control repair issue quickly.",
     {"entities": [(0, 12, "PERSON"), (22, 41, "SKILL")]}),  

    # --- Refrigerator Maintenance ---
    ("Refrigerator maintenance tasks include ice maker repair and thermostat control check.",
     {"entities": [(0, 24, "SERVICE"), (42, 57, "SKILL"), (63, 86, "SKILL")]}),

    ("The technician did condenser coil cleaning and defrost system maintenance.",
     {"entities": [(21, 44, "SKILL"), (50, 76, "SKILL")]}),

    # --- Air Conditioner Maintenance ---
    ("Air conditioner maintenance involves coil cleaning and filter cleaning.",
     {"entities": [(0, 28, "SERVICE"), (40, 51, "SKILL"), (57, 71, "SKILL")]}),  

    ("He handled an air conditioner repair and later an installation job.",
     {"entities": [(0, 2, "PERSON"), (13, 36, "SKILL"), (47, 62, "SKILL")]}),  

    ("System tune-up is included in air conditioner servicing.",
     {"entities": [(0, 13, "SKILL")]}),

    # --- Sofa Maintenance ---
    ("The carpenter performed sofa maintenance last weekend.",
     {"entities": [(4, 13, "SPECIALIZATION"), (22, 37, "SERVICE")]}),  

    ("Cushion repair and spring replacement were done on the sofa.",
     {"entities": [(0, 13, "SKILL"), (19, 35, "SKILL")]}),

    ("He did upholstery cleaning and cushion replacement after sofa damage.",
     {"entities": [(0, 2, "PERSON"), (7, 25, "SKILL"), (31, 49, "SKILL")]}),

    ("Frame reinforcement was carried out during sofa maintenance.",
     {"entities": [(0, 18, "SKILL"), (41, 56, "SERVICE")]}),  

    # --- Bed Maintenance ---
    ("Bed maintenance often requires headboard repair and slat replacement.",
     {"entities": [(0, 13, "SERVICE"), (33, 48, "SKILL"), (54, 68, "SKILL")]}),  

    ("Frame tightening and mattress rotation are bed upkeep tasks.",
     {"entities": [(0, 15, "SKILL"), (21, 38, "SKILL")]}),  

    # --- Cabinet Maintenance ---
    ("Cabinet maintenance usually means cabinet repair or lock replacement.",
     {"entities": [(0, 18, "SERVICE"), (34, 47, "SKILL"), (52, 67, "SKILL")]}),  

    ("Handle replacement and cabinet refacing were completed last month.",
     {"entities": [(0, 17, "SKILL"), (23, 39, "SKILL")]}),  

    # --- Door Maintenance --- #
    ("Door maintenance involves hinge replacement and door alignment.",
     {"entities": [(0, 15, "SERVICE"), (26, 42, "SKILL"), (48, 60, "SKILL")]}),  

    ("Weather stripping installation and roller repair are door fixes.",
     {"entities": [(0, 28, "SKILL"), (34, 46, "SKILL")]}),  

    ("The technician did scratch repair, dent repair, and sliding track repair.",
     {"entities": [(20, 33, "SKILL"), (36, 46, "SKILL"), (53, 72, "SKILL")]}),  

    ("Automatic door mechanism was installed for security.",
     {"entities": [(0, 24, "SKILL")]}), 

    # --- General Cleaning ---
    ("Housekeeping tasks include general cleaning such as sweeping floors and mopping floors.",
     {"entities": [(27, 42, "SERVICE"), (53, 67, "SKILL"), (73, 86, "SKILL")]}),

    ("The maid spent the afternoon vacuuming carpet and surface wiping.",
     {"entities": [(26, 41, "SKILL"), (47, 60, "SKILL")]}),

    ("Organizing and decluttering are part of general cleaning routines.",
     {"entities": [(0, 10, "SKILL"), (15, 27, "SKILL"), (37, 52, "SERVICE")]}),  

    # --- Deep Cleaning ---
    ("Deep cleaning involves upholstery deep cleaning and mattress sanitizing.",
     {"entities": [(0, 12, "SERVICE"), (22, 46, "SKILL"), (52, 70, "SKILL")]}),  

    ("He worked on tile scrubbing and steam cleaning for the client.",
     {"entities": [(0, 2, "PERSON"), (12, 25, "SKILL"), (31, 44, "SKILL")]}),  

    ("Stain removal is necessary during deep cleaning jobs.",
     {"entities": [(0, 12, "SKILL"), (32, 44, "SERVICE")]}),  

    # --- Laundry ---
    ("Laundry service often includes clothes sorting and hand washing delicates.",
     {"entities": [(0, 7, "SERVICE"), (29, 43, "SKILL"), (49, 69, "SKILL")]}),  

    ("Ironing and hand washing are daily household tasks.",
     {"entities": [(0, 7, "SKILL"), (12, 24, "SKILL")]}),

    ("She managed laundry yesterday, focusing on ironing clothes.",
     {"entities": [(0, 3, "PERSON"), (14, 21, "SERVICE"), (39, 45, "SKILL")]}),
]