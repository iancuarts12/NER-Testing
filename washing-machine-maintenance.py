train_data = [ 
    # ----------- Washing Machine Maintenance ----------- 

    # Washing Machine Repair
    ("Washing machine repair is essential to maintain appliance performance.", 
     {"entities": [(0, 23, "SKILL")]}),

    ("Washing machine repairs are performed regularly to prevent breakdowns.", 
     {"entities": [(0, 24, "SKILL")]}),

    ("Repairing washing machine helps restore proper function to the appliance.", 
     {"entities": [(0, 24, "SKILL")]}),

    ("Repairing washing machines is part of routine appliance maintenance.", 
     {"entities": [(0, 25, "SKILL")]}),

    ("Repairing of washing machine requires careful diagnosis of faults.", 
     {"entities": [(0, 27, "SKILL")]}),

    ("Repairing of washing machines ensures proper operation of all components.", 
     {"entities": [(0, 28, "SKILL")]}),

    ("Repaired washing machines restored proper washing cycles in the unit.", 
     {"entities": [(0, 25, "SKILL")]}),

    ("Repaired a washing machine resolved the persistent leakage issue.", 
     {"entities": [(0, 26, "SKILL")]}),

    ("Repaired a washing machines improved appliance efficiency.", 
     {"entities": [(0, 27, "SKILL")]}),


    # Belt Replacement
    ("Belt replacement ensures proper operation of washing machines.", 
     {"entities": [(0, 18, "SKILL")]}),

    ("Belt replacements are conducted to maintain appliance efficiency.", 
     {"entities": [(0, 19, "SKILL")]}),

    ("Replacement of belt restores correct functioning of the washing machine.", 
     {"entities": [(0, 22, "SKILL")]}),

    ("Replacement of belts prevents slippage and mechanical failure.", 
     {"entities": [(0, 23, "SKILL")]}),

    ("Replacement of washing machine belt ensures smooth washing cycles.", 
     {"entities": [(0, 33, "SKILL")]}),

    ("Replacement of washing machine belts improves overall appliance performance.", 
     {"entities": [(0, 34, "SKILL")]}),

    ("Replacing washing machine belt is part of routine maintenance.", 
     {"entities": [(0, 28, "SKILL")]}),

    ("Replacing washing machine belts helps maintain appliance efficiency.", 
     {"entities": [(0, 29, "SKILL")]}),

    ("Replacing of washing machine belt requires proper alignment and tension.", 
     {"entities": [(0, 32, "SKILL")]}),

    ("Replacing of washing machine belts ensures smooth operation.", 
     {"entities": [(0, 33, "SKILL")]}),

    ("Replacing belt is necessary when it shows signs of wear.", 
     {"entities": [(0, 16, "SKILL")]}),

    ("Replacing belts prevents machine malfunction and downtime.", 
     {"entities": [(0, 17, "SKILL")]}),

    ("Replacing of belt requires careful removal and fitting.", 
     {"entities": [(0, 21, "SKILL")]}),

    ("Replacing of belts ensures all washing machine components function properly.", 
     {"entities": [(0, 22, "SKILL")]}),

    ("Replaced a washing machine belt restored proper operation.", 
     {"entities": [(0, 29, "SKILL")]}),

    ("Replaced a washing machine belts improved appliance efficiency.", 
     {"entities": [(0, 30, "SKILL")]}),

    ("Replaced washing machine belt prevented slippage during operation.", 
     {"entities": [(0, 28, "SKILL")]}),

    ("Replaced washing machine belts ensured smooth and reliable cycles.", 
     {"entities": [(0, 29, "SKILL")]}),


    # Drum Cleaning
    ("Drum cleaning is essential to maintain washing machine hygiene.", 
     {"entities": [(0, 13, "SKILL")]}),

    ("Cleaning drum prevents buildup of detergent residues in appliances.", 
     {"entities": [(0, 14, "SKILL")]}),

    ("Cleaning drums ensures proper washing performance and longevity.", 
     {"entities": [(0, 15, "SKILL")]}),

    ("Cleaned drum restored proper hygiene and functionality.", 
     {"entities": [(0, 12, "SKILL")]}),

    ("Cleaned drums improved washing machine efficiency and performance.", 
     {"entities": [(0, 13, "SKILL")]}),

    ("Cleaned washing machine drum removed buildup and odor effectively.", 
     {"entities": [(0, 25, "SKILL")]}),

    ("Cleaned washing machine drums ensured all components functioned properly.", 
     {"entities": [(0, 26, "SKILL")]}),

    ("Cleaned a washing machine drum restored full washing capacity.", 
     {"entities": [(0, 27, "SKILL")]}),

    ("Cleaned a washing machine drums prevented mold and mildew buildup.", 
     {"entities": [(0, 28, "SKILL")]}),

    ("Washing machine drum cleaning is part of routine maintenance.", 
     {"entities": [(0, 31, "SKILL")]}),

    ("Cleaning of washing machine drum ensures proper hygiene.", 
     {"entities": [(0, 28, "SKILL")]}),

    ("Cleaning of washing machine drums prevents odor and residue buildup.", 
     {"entities": [(0, 29, "SKILL")]}),

    ("Cleaning of drum maintains appliance performance and longevity.", 
     {"entities": [(0, 17, "SKILL")]}),

    ("Cleaning of drums is performed regularly to avoid buildup.", 
     {"entities": [(0, 18, "SKILL")]}),

    ("Cleaned a drum removed all residues and maintained proper hygiene.", 
     {"entities": [(0, 15, "SKILL")]}),

    ("Cleaned a drums improved washing efficiency and hygiene.", 
     {"entities": [(0, 16, "SKILL")]}),


    # Hose Replacement
    ("Hose replacement ensures proper water flow in the washing machine.", 
     {"entities": [(0, 16, "SKILL")]}),

    ("Hose replacements prevent leaks and maintain appliance efficiency.", 
     {"entities": [(0, 17, "SKILL")]}),

    ("Replacing hose restores proper water circulation in the system.", 
     {"entities": [(0, 15, "SKILL")]}),

    ("Replacing hoses prevents water leakage and ensures smooth operation.", 
     {"entities": [(0, 16, "SKILL")]}),

    ("Replacing of hose is necessary when wear and tear is observed.", 
     {"entities": [(0, 20, "SKILL")]}),

    ("Replacing of hoses ensures all washing machine components function properly.", 
     {"entities": [(0, 21, "SKILL")]}),

    ("Replacing of washing machine hose prevents leaks and flooding.", 
     {"entities": [(0, 32, "SKILL")]}),

    ("Replacing of washing machine hoses improves water flow and washing efficiency.", 
     {"entities": [(0, 33, "SKILL")]}),

    ("Replacement of washing machine hose is part of routine maintenance.", 
     {"entities": [(0, 33, "SKILL")]}),

    ("Replacement of washing machine hoses prevents leaks and damages.", 
     {"entities": [(0, 34, "SKILL")]}),

    ("Replacement of hose ensures proper water flow and machine safety.", 
     {"entities": [(0, 23, "SKILL")]}),

    ("Replacement of hoses improves washing machine longevity.", 
     {"entities": [(0, 24, "SKILL")]}),


    # Washing Machine Hose Installation
    ("Washing machine hose installation is essential for proper water flow.", 
     {"entities": [(0, 33, "SKILL")]}),

    ("Washing machine hose installations prevent leaks and ensure smooth operation.", 
     {"entities": [(0, 34, "SKILL")]}),

    ("Installation of washing machine hose ensures proper connection and function.", 
     {"entities": [(0, 31, "SKILL")]}),

    ("Installation of washing machine hoses prevents leakage and flooding.", 
     {"entities": [(0, 32, "SKILL")]}),

    ("Installment of washing machine hose is part of routine maintenance.", 
     {"entities": [(0, 30, "SKILL")]}),

    ("Installment of washing machine hoses ensures proper appliance function.", 
     {"entities": [(0, 31, "SKILL")]}),

    ("Installing washing machine hose requires careful handling to avoid leaks.", 
     {"entities": [(0, 28, "SKILL")]}),

    ("Installing washing machine hoses improves water flow and appliance efficiency.", 
     {"entities": [(0, 29, "SKILL")]}),

    ("Installed washing machine hose restored proper water circulation in the unit.", 
     {"entities": [(0, 28, "SKILL")]}),

    ("Installed washing machine hoses prevented leakage during washing cycles.", 
     {"entities": [(0, 29, "SKILL")]}),

    ("Installed a washing machine hose ensured correct water connection.", 
     {"entities": [(0, 31, "SKILL")]}),

    ("Installed a washing machine hoses improved machine performance and safety.", 
     {"entities": [(0, 32, "SKILL")]}),
]
