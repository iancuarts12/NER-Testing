train_data = [
   # Toilet Repair
   ("Toilet installation is part of the renovation process in Quezon City.",
        {"entities": [(0, 19, "SKILL"), (57, 69, "GPE")]}),
    ("John Santos regularly handles toilet installations for clients in Makati.",
        {"entities": [(0, 11, "PERSON"), (30, 50, "SKILL"), (66, 73, "GPE")]}),
    ("The team focuses on installing toilets efficiently in Pasig.",
        {"entities": [(20, 39, "SKILL"), (54, 60, "GPE")]}),
    ("Installation of toilet was completed yesterday by Mario Reyes in Mandaluyong.",
        {"entities": [(0, 23, "SKILL"), (50,62, "PERSON"), (65, 77, "GPE")]}),
    ("Installation of toilets requires careful alignment in Pasay City.",
        {"entities": [(0, 24, "SKILL"), (54, 64, "GPE")]}),
    ("Installing of toilet is scheduled for tomorrow in Taguig.",
        {"entities": [(0, 21, "SKILL"), (50, 57, "GPE")]}),
    ("Maria Cruz is installing toilets in Marikina this week.",
        {"entities": [(0, 10, "PERSON"), (14, 33, "SKILL"), (36, 45, "GPE")]}),
    ("They are installing toilet in the guest bathroom in Parañaque.",
        {"entities": [(9, 26, "SKILL"), (52, 62, "GPE")]}),
    ("Technicians are installing toilets across multiple homes in Valenzuela.",
        {"entities": [(0,11, "SPECIALIZATION"),(16, 34, "SKILL"), (60, 71, "GPE")]}),
    ("Anya from Manila installed a toilet in her new apartment.", 
        {"entities": [(0, 4, "PERSON"), (10, 16, "GPE"), (17, 36, "SKILL")]}),
    ("Pablo Reyes from Mandaluyong installed a toilet for a client yesterday.", 
        {"entities": [(0, 11, "PERSON"), (17, 28, "GPE"), (29, 48, "SKILL")]}),
    ("The plumber performs toilet repair in all bathrooms in San Juan.", 
     {"entities": [(4, 11, "SPECIALIZATION"), (21, 35, "SKILLS"), (55, 64, "GPE")]}),
    ("The plumber performs toilet repair in all bathrooms in San Juan.", 
     {"entities": [(4, 11, "SPECIALIZATION"), (20, 34, "SKILLS"), (55, 64, "GPE")]}), 
    
    ("Toilet repairs are essential to maintain hygiene in Muntinlupa.", 
     {"entities": [(0, 14, "SKILLS"), (52, 63, "GPE")]}),  
    
    ("Carlos Garcia handles toilet repairs every week in Navotas.", 
     {"entities": [(0, 13, "PERSON"), (22, 36, "SKILLS"), (51, 60, "GPE")]}),  
    
    ("Repairing toilet is part of regular maintenance tasks in Malabon.", 
     {"entities": [(0, 16, "SKILLS"), (57, 65, "GPE")]}),  
    
    ("Repairing toilets requires skill and precision in Las Piñas.", 
     {"entities": [(0, 17, "SKILLS"), (50, 60, "GPE")]}),  
    
    ("They are repairing toilet in the master bathroom in Pateros.", 
     {"entities": [(9, 25, "SKILLS"), (52, 60, "GPE")]}),  
    
    ("Repairing of toilets takes time when plumbing is old in Pasig.", 
     {"entities": [(0, 19, "SKILLS"), (56, 62, "GPE")]}),  
    
    ("The plumber repaired toilet last Tuesday in Quezon City.", 
     {"entities": [(4, 11, "SPECIALIZATION"), (12, 28, "SKILLS"), (44, 56, "GPE")]}),  
    
    ("Ana Reyes repaired toilets in the guest restroom yesterday in Makati.", 
     {"entities": [(0, 9, "PERSON"), (10, 26, "SKILLS"), (62, 69, "GPE")]}),  
    
    # Leak Fixing
    ("Leak fixing is crucial to prevent water damage in bathrooms in Mandaluyong.", 
     {"entities": [(0, 12, "SKILLS"), (62, 75, "GPE")]}),  
    
    ("Fixing leak requires proper tools and expertise in Taguig.", 
     {"entities": [(0, 12, "SKILLS"), (51, 58, "GPE")]}),  
    
    ("They are fixing leaks in the old building plumbing in Marikina.", 
     {"entities": [(9, 21, "SKILLS"), (54, 63, "GPE")]}),  

    ("Fixing of leak is part of the maintenance checklist in Parañaque.", 
     {"entities": [(0, 15, "SKILLS"), (56, 65, "GPE")]}),  
    
    ("Fixing of leaks takes priority after heavy rain in Valenzuela.", 
     {"entities": [(0, 16, "SKILLS"), (51, 62, "GPE")]}),  
    
    ("The plumber fixed a leak under the kitchen sink in San Juan.", 
     {"entities": [(4, 11, "SPECIALIZATION"), (12, 25, "SKILLS"), (51, 60, "GPE")]}), 
    
    ("He fixed leaks in the restroom yesterday in Muntinlupa.", 
     {"entities": [(3, 14, "SKILLS"), (44, 54, "GPE")]}),  
    
    ("Fixed leak was repaired by the maintenance team quickly in Navotas.", 
     {"entities": [(0, 10, "SKILLS"), (59, 67, "GPE")]}),  
    
    # Toilet Unclogging - Only SKILLS and GPE, no SERVICE
    ("Toilet unclogging is an important maintenance task in Malabon.", 
     {"entities": [(0, 18, "SKILLS"), (54, 62, "GPE")]}),  
    
    ("Toilet uncloggings occur frequently in busy restrooms in Las Piñas.", 
     {"entities": [(0, 19, "SKILLS"), (57, 67, "GPE")]}),  
    
    ("Unclogging toilet requires special tools and care in Pasig.", 
     {"entities": [(0, 17, "SKILLS"), (53, 59, "GPE")]}),  
    
    ("Unclogging toilets is often performed by professional plumbers in Quezon City.", 
     {"entities": [(0, 18, "SKILLS"), (66, 79, "GPE")]}),  

    ("Unclogging of toilet was scheduled for the morning in Makati.", 
     {"entities": [(0, 20, "SKILLS"), (53, 61, "GPE")]}),  
    
    ("Unclogging of toilets takes precedence in commercial buildings in Mandaluyong.", 
     {"entities": [(0, 21, "SKILLS"), (66, 77, "GPE")]}),  
    
    ("The plumber unclogged toilet in the master bathroom yesterday in Taguig.", 
     {"entities": [(4, 11, "SPECIALIZATION"), (12, 28, "SKILLS"), (65, 73, "GPE")]}),  
    
    # Flushing Repair System - Only SKILLS and GPE, no SERVICE
    ("Flushing system repair is critical to proper toilet function in Marikina.", 
     {"entities": [(0, 22, "SKILLS"), (64, 74, "GPE")]}),  
    
    ("Flushing systems repair occurs regularly in public restrooms in Parañaque.", 
     {"entities": [(0, 23, "SKILLS"), (64, 74, "GPE")]}),  
    
    ("Repairing flushing system requires precision and care in Valenzuela.", 
     {"entities": [(0, 25, "SKILLS"), (57, 67, "GPE")]}), 
    
    ("Repairing flushing systems is often handled by professional plumbers in San Juan.", 
     {"entities": [(0, 25, "SKILLS"), (60,68, "SPECIALIZATION"),(72, 81, "GPE")]}),  
    
    # Toilet Replacement
    ("Toilet replacement is necessary when toilets are old in Muntinlupa.", 
     {"entities": [(0, 18, "SKILLS"), (56, 67, "GPE")]}),
    
    ("Toilet replacements occur frequently in hotels in Navotas.", 
     {"entities": [(0, 19, "SKILLS"), (50, 58, "GPE")]}), 

    ("Replacing toilet is part of the regular maintenance routine in Malabon.", 
     {"entities": [(0, 16, "SKILLS"), (63, 71, "GPE")]}), 
    
    ("Replacing toilets requires careful handling by the team in Pasig.", 
     {"entities": [(0, 17, "SKILLS"), (59, 65, "GPE")]}), 
    
    ("Replacing of toilet was scheduled for this morning in Quezon City.", 
     {"entities": [(0, 19, "SKILLS"), (54, 65, "GPE")]}), 
    
    ("The plumber replaced toilet in the guest bathroom yesterday in Makati.", 
     {"entities": [(4, 11, "SPECIALIZATION"), (12, 28, "SKILLS"), (62,70,"GPE")]}), 
    
    ("He replaced toilets across multiple units quickly in Mandaluyong.", 
     {"entities": [(3, 20, "SKILLS"), (53, 65, "GPE")]}), 
    
    ("They replaced a toilet in the office restroom in Taguig.", 
     {"entities": [(5, 22, "SKILLS"), (49, 56, "GPE")]}),  
    
    ("The maintenance team replaced a toilet yesterday in Marikina.", 
     {"entities": [(21, 39, "SKILLS"), (52, 61, "GPE")]}),  
]