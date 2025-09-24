train_data = [
     # ----------- Faucet and Sink Maintenance -----------

    # Faucet Installation
    ("Faucet installation is essential for new kitchen setups.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("Faucet installation occurs frequently in commercial kitchens.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("Installing faucet requires precision and proper tools.", 
     {"entities": [(0, 18, "SKILL")]}),

    ("Installing faucets is often handled by professional plumbers.", 
     {"entities": [(0, 19, "SKILL"), (53, 61, "SPECIALIZATION")]}),

    ("Installing of faucet was scheduled for the morning.", 
     {"entities": [(0, 21, "SKILL")]}),

    ("Installing of faucets takes priority in commercial projects.", 
     {"entities": [(0, 22, "SKILL")]}),

    ("Installation of faucet is part of kitchen remodeling.", 
     {"entities": [(0, 23, "SKILL")]}),

    ("Installation of faucets requires careful handling by the team.", 
     {"entities": [(0, 22, "SKILL")]}),

    ("The plumber installed a faucet in the new kitchen.", 
     {"entities": [(12, 31, "SKILL"), (4, 12, "SPECIALIZATION")]}),

    ("He installed a faucets quickly in the guest bathroom.", 
     {"entities": [(3, 21, "SKILL")]}),

    ("Installed faucet in the office restroom by the maintenance team.", 
     {"entities": [(0, 17, "SKILL")]}),

    ("The workers installed faucets in multiple units yesterday.", 
     {"entities": [(12, 30, "SKILL")]}),

    # Faucet Repair
    ("Faucet repair is essential to prevent leaks in kitchens.", 
     {"entities": [(0, 14, "SKILL")]}),

    ("Faucet repairs are regularly performed in commercial properties.", 
     {"entities": [(0, 13, "SKILL")]}),

    ("Repairing faucet requires careful handling and proper tools.", 
     {"entities": [(0, 17, "SKILL")]}),

    ("Repairing faucets is often handled by professional plumbers.", 
     {"entities": [(0, 18, "SKILL"), (51, 60, "SPECIALIZATION")]}),

    ("Repairing of faucet was scheduled for this morning.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("Repairing of faucets takes priority in commercial projects.", 
     {"entities": [(0, 21, "SKILL")]}),

    ("The plumber repaired a faucet in the new kitchen.", 
     {"entities": [(12, 30, "SKILL"), (4, 12, "SPECIALIZATION")]}),

    ("He repaired a faucets quickly to prevent water spillage.", 
     {"entities": [(3, 21, "SKILL")]}),

    ("Repaired faucet in the office restroom by the maintenance team.", 
     {"entities": [(0, 16, "SKILL")]}),

    ("The team repaired faucets in multiple apartments yesterday.", 
     {"entities": [(9, 26, "SKILL")]}),

    # Faucet Replacement
    ("Faucet replacement is necessary when old faucets leak.", 
     {"entities": [(0, 18, "SKILL")]}),

    ("Faucet replacements occur frequently in commercial kitchens.", 
     {"entities": [(0, 19, "SKILL")]}),

    ("Replacing faucet requires proper tools and precision.", 
     {"entities": [(0, 17, "SKILL")]}),

    ("Replacing faucets is often performed by professional plumbers.", 
     {"entities": [(0, 18, "SKILL"), (40, 52, "SPECIALIZATION")]}),

    ("Replacing of faucet was scheduled for the morning.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("Replacing of faucets takes priority in commercial projects.", 
     {"entities": [(0, 21, "SKILL")]}),

    ("The plumber replaced faucet in the guest kitchen.", 
     {"entities": [(12, 28, "SKILL"), (4, 11, "SPECIALIZATION")]}),

    ("He replaced faucets quickly to prevent water spillage.", 
     {"entities": [(3, 20, "SKILL")]}),

    ("They replaced a faucet in the office restroom.", 
     {"entities": [(5, 23, "SKILL")]}),

    ("The maintenance team replaced a faucets yesterday.", 
     {"entities": [(21, 40, "SKILL")]}),

    # Sink Installation
    ("Sink installation is crucial for new kitchen setups.", 
     {"entities": [(0, 17, "SKILL")]}),

    ("Sink installations are scheduled frequently in commercial buildings.", 
     {"entities": [(0, 18, "SKILL")]}),

    ("Installing sink requires proper tools and careful handling.", 
     {"entities": [(0, 16, "SKILL")]}),

    ("Installing sinks is often performed by professional plumbers.", 
     {"entities": [(0, 17, "SKILL"), (39, 52, "SPECIALIZATION")]}),

    ("Installing of sink was scheduled for the morning.", 
     {"entities": [(0, 19, "SKILL")]}),

    ("Installing of sinks takes priority in renovation projects.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("Installation of sink is part of bathroom remodeling.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("Installation of sinks requires careful alignment and tools.", 
     {"entities": [(0, 21, "SKILL")]}),

    ("The plumber installed a sink in the new kitchen.", 
     {"entities": [(12, 28, "SKILL"), (4, 12, "SPECIALIZATION")]}),

    ("He installed a sinks quickly in the office restroom.", 
     {"entities": [(3, 20, "SKILL")]}),

    ("Installed sink in the guest bathroom by the maintenance team.", 
     {"entities": [(0, 14, "SKILL")]}),

    ("The workers installed sinks in multiple apartments yesterday.", 
     {"entities": [(12, 28, "SKILL")]}),

    # Sink Replacement
    ("Sink replacement is necessary when old sinks leak.", 
     {"entities": [(0, 16, "SKILL")]}),

    ("Sink replacements occur frequently in commercial kitchens.", 
     {"entities": [(0, 17, "SKILL")]}),

    ("Replacing sink requires proper tools and precision.", 
     {"entities": [(0, 15, "SKILL")]}),

    ("Replacing sinks is often performed by professional plumbers.", 
     {"entities": [(0, 16, "SKILL"), (51, 60, "SPECIALIZATION")]}),

    ("Replacement of sink was scheduled for the morning.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("Replacement of sinks takes priority in renovation projects.", 
     {"entities": [(0, 21, "SKILL")]}),

    ("Replacing of sink requires careful handling by the team.", 
     {"entities": [(0, 18, "SKILL")]}),

    ("Replacing of sinks is part of the maintenance checklist.", 
     {"entities": [(0, 19, "SKILL")]}),

    ("The plumber replaced a sink in the new kitchen.", 
     {"entities": [(12, 28, "SKILL"), (4, 12, "SPECIALIZATION")]}),

    ("He replaced a sinks quickly in the office restroom.", 
     {"entities": [(3, 20, "SKILL")]}),

    ("Replaced sink in the guest bathroom by the maintenance team.", 
     {"entities": [(0, 14, "SKILL")]}),

    ("The workers replaced sinks in multiple apartments yesterday.", 
     {"entities": [(12, 27, "SKILL")]}),

    # Sink Unclogging
    ("Sink unclogging is necessary to maintain proper drainage.", 
     {"entities": [(0, 15, "SKILL")]}),

    ("Unclogging sink occurs frequently in commercial kitchens.", 
     {"entities": [(0, 16, "SKILL")]}),

    ("Unclogging sinks requires proper tools and careful handling.", 
     {"entities": [(0, 17, "SKILL")]}),

    ("Unclogging of sink is often performed by maintenance professionals.", 
     {"entities": [(0, 19, "SKILL")]}),

    ("Unclogging of sinks takes priority after heavy usage.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("The plumber unclogged a sink in the restroom yesterday.", 
     {"entities": [(12, 29, "SKILL"), (4, 11, "SPECIALIZATION")]}),

    ("He unclogged a sinks quickly to restore drainage.", 
     {"entities": [(3, 21, "SKILL")]}),

    ("Unclogged sink was repaired by the maintenance team.", 
     {"entities": [(0, 15, "SKILL")]}),

    ("The team unclogged sinks in multiple apartments yesterday.", 
     {"entities": [(9, 25, "SKILL")]}),
]
