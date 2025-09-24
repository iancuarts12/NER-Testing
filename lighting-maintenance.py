train_data = [
    # ----------- Lighting Maintenance -----------

    # Incandescent Light Installation
    ("Incandescent light installation is performed by licensed electricians.", 
     {"entities": [(0, 31, "SKILL"), (57, 70, "SPECIALIZATION")]}),

    ("Incandescent light installations require proper handling for lighting maintenance.", 
     {"entities": [(0, 32, "SKILL"), (61, 82, "SERVICE")]}),

    ("Installation of incandescent light must follow safety standards.", 
     {"entities": [(0, 34, "SKILL")]}),

    ("Installation of incandescent lights is part of lighting maintenance.", 
     {"entities": [(0, 35, "SKILL"), (47, 68, "SERVICE")]}),

    ("Installing incandescent light ensures proper illumination in Chicago.", 
     {"entities": [(0, 30, "SKILL"), (61, 68, "GPE")]}),

    ("Installing incandescent lights is included in all lighting projects by electricians.", 
     {"entities": [(0, 31, "SKILL"), (71, 84, "SPECIALIZATION")]}),

    ("Installing of incandescent light follows strict electrical codes.", 
     {"entities": [(0, 32, "SKILL")]}),

    ("Installing of incandescent lights requires careful handling by technicians.", 
     {"entities": [(0, 32, "SKILL"), (63, 75, "SPECIALIZATION")]}),

    ("John installed incandescent light in the living room yesterday.", 
     {"entities": [(0, 4, "PERSON"), (5, 33, "SKILL")]}),

    ("We installed incandescent lights to replace old fixtures.", 
     {"entities": [(3, 32, "SKILL")]}),

    ("Installed incandescent light was inspected for proper wiring.", 
     {"entities": [(0, 28, "SKILL")]}),

    ("Installed incandescent lights provided better illumination for electrical maintenance.", 
     {"entities": [(0, 29, "SKILL"), (63, 85, "SERVICE")]}),


    # Fluorescent Light Installation
    ("Fluorescent light installation is done by qualified electricians.", 
     {"entities": [(0, 30, "SKILL"), (52, 65, "SPECIALIZATION")]}),

    ("Fluorescent light installations require careful handling of tubes.", 
     {"entities": [(0, 31, "SKILL")]}),

    ("Installation of fluorescent light must follow electrical safety codes.", 
     {"entities": [(0, 34, "SKILL")]}),

    ("Installation of fluorescent lights ensures proper office illumination.", 
     {"entities": [(0, 35, "SKILL")]}),

    ("Installing fluorescent light is part of lighting maintenance.", 
     {"entities": [(0, 29, "SKILL"), (40, 61, "SERVICE")]}),

    ("Installing fluorescent lights helps improve workspace lighting in New York.", 
     {"entities": [(0, 30, "SKILL"), (66, 75, "GPE")]}),

    ("Installing of fluorescent light requires proper protective gear.", 
     {"entities": [(0, 32, "SKILL")]}),

    ("Installing of fluorescent lights is included in all lighting projects.", 
     {"entities": [(0, 33, "SKILL")]}),

    ("Mike installed a fluorescent light in the conference room yesterday.", 
     {"entities": [(0, 4, "PERSON"), (5, 28, "SKILL")]}),

    ("Installed fluorescent lights to replace old fixtures in Los Angeles.", 
     {"entities": [(0, 29, "SKILL"), (56, 68, "GPE")]}),

    ("Installed fluorescent light was inspected by electricians for proper wiring.", 
     {"entities": [(0, 27, "SKILL"), (45, 58, "SPECIALIZATION")]}),

    ("Installed fluorescent lights improved overall lighting for appliance maintenance.", 
     {"entities": [(0, 29, "SKILL"), (59, 81, "SERVICE")]}),


    # LED Light Installation
    ("LED light installation is performed to improve energy efficiency.", 
     {"entities": [(0, 22, "SKILL")]}),

    ("LED light installations require careful handling during setup in Houston.", 
     {"entities": [(0, 23, "SKILL"), (65, 73, "GPE")]}),

    ("Installation of LED light follows strict electrical safety codes.", 
     {"entities": [(0, 25, "SKILL")]}),

    ("Installation of LED lights ensures consistent workspace illumination.", 
     {"entities": [(0, 26, "SKILL")]}),

    ("Installing of LED light is included in lighting maintenance.", 
     {"entities": [(0, 23, "SKILL"), (39, 60, "SERVICE")]}),

    ("Installing of LED lights improves energy efficiency and brightness.", 
     {"entities": [(0, 24, "SKILL")]}),

    ("Installing LED light ensures proper wiring and fixture placement.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("Installing LED lights helps maintain consistent office illumination.", 
     {"entities": [(0, 21, "SKILL")]}),

    ("Sarah installed LED light replaced the old fluorescent fixture.", 
     {"entities": [(0, 5, "PERSON"), (6, 25, "SKILL")]}),

    ("Installed LED lights improved overall lighting in Phoenix.", 
     {"entities": [(0, 21, "SKILL"), (50, 57, "GPE")]}),

    ("Installed LED light was inspected for proper electrical connection.", 
     {"entities": [(0, 19, "SKILL")]}),

    ("Installed LED lights ensured all workspaces had proper lighting maintenance.", 
     {"entities": [(0, 20, "SKILL"), (54, 76, "SERVICE")]}),


    # Bulb Replacement
    ("Bulb replacement is necessary to maintain proper lighting maintenance.", 
     {"entities": [(0, 16, "SKILL"), (49, 70, "SERVICE")]}),

    ("Bulb replacements are performed regularly in office spaces by electricians.", 
     {"entities": [(0, 17, "SKILL"), (60, 74, "SPECIALIZATION")]}),

    ("Replacing bulb helps improve lighting efficiency in rooms.", 
     {"entities": [(0, 14, "SKILL")]}),

    ("Replacing bulbs is part of lighting maintenance.", 
     {"entities": [(0, 15, "SKILL"), (27, 48, "SERVICE")]}),

    ("Replacing of bulb requires caution to avoid electrical hazards.", 
     {"entities": [(0, 17, "SKILL")]}),

    ("Replacing of bulbs is included in routine maintenance tasks.", 
     {"entities": [(0, 18, "SKILL")]}),

    ("Replacement of bulb ensures proper illumination in the office.", 
     {"entities": [(0, 19, "SKILL")]}),

    ("Replacement of bulbs is carried out during routine lighting checks.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("David replaced a bulb in the conference room yesterday.", 
     {"entities": [(0, 5, "PERSON"), (6, 21, "SKILL")]}),

    ("Replaced bulbs improved lighting in the main office in Miami.", 
     {"entities": [(0, 14, "SKILL"), (55, 61, "GPE")]}),

    ("Replaced bulb was inspected for proper functionality.", 
     {"entities": [(0, 13, "SKILL")]}),

    ("Replaced bulbs ensured consistent lighting for furniture maintenance.", 
     {"entities": [(0, 14, "SKILL"), (47, 69, "SERVICE")]}),


    # Light Fixture Installation
    ("Light fixture installation improves lighting in commercial spaces.", 
     {"entities": [(0, 26, "SKILL")]}),

    ("Light fixture installations are performed to enhance interior lighting.", 
     {"entities": [(0, 27, "SKILL")]}),

    ("Installation of light fixture must follow electrical safety standards.", 
     {"entities": [(0, 29, "SKILL")]}),

    ("Installation of light fixtures ensures proper illumination in offices.", 
     {"entities": [(0, 30, "SKILL")]}),

    ("Installing of light fixture is included in lighting maintenance.", 
     {"entities": [(0, 27, "SKILL"), (43, 63, "SERVICE")]}),

    ("Installing of light fixtures helps improve overall workspace lighting.", 
     {"entities": [(0, 28, "SKILL")]}),

    ("Installing light fixture requires careful alignment and wiring.", 
     {"entities": [(0, 24, "SKILL")]}),

    ("Installing light fixtures ensures consistent lighting throughout Chicago.", 
     {"entities": [(0, 25, "SKILL"), (65, 72, "GPE")]}),

    ("Installed light fixture replaced the old unit in the conference room.", 
     {"entities": [(0, 23, "SKILL")]}),

    ("Installed light fixtures improved lighting across all work areas.", 
     {"entities": [(0, 24, "SKILL")]}),

    ("Installed light fixture was inspected by electricians for correct connection.", 
     {"entities": [(0, 23, "SKILL"), (41, 53, "SPECIALIZATION")]}),
]