# commands.py

COMMANDS = {
    "bloodlegacy": {
        "Bloodlegacy Commands": [
            {
                "template": ".bl cst [BloodOrStat] [BloodStat]",
                "label": "Choose Stat",
                "description": "Choose a bonus stat to enhance for your blood legacy.",
                "params": ["BloodOrStat", "BloodStat"],
                "options": {
                    "BloodOrStat": [
                        "Brute", "Corruption", "Creature", "Draculin", "Immortal", "Mutant", "Rogue", "Scholar", "Warrior", "Worker",
                    ],
                    "BloodStat": [
                        "HealingReceived","DamageReduction","PhysicalResistance",
                        "SpellResistance","ResourceYield","ReducedBloodDrain",
                        "SpellCooldownRecoveryRate","WeaponCooldownRecoveryRate",
                        "UltimateCooldownRecoveryRate","MinionDamage",
                        "AbilityAttackSpeed","CorruptionDamageReduction"
                    ]
                }
            },
            {
                "template": ".bl get [BloodType]",
                "label": "Get Blood Type",
                "description": "Display current blood legacy details.",
                "params": ["BloodType"],
                "options": {
                    "BloodType": [
                        "Brute", "Corruption", "Creature", "Draculin", "Immortal", "Mutant", "Rogue", "Scholar", "Warrior", "Worker",
                    ],
                }
            },
            {
                "template": ".bl list",
                "label": "List Bloodlegacies",
                "description": "Lists blood legacies available.",
                "params": []
            },
            {
                "template": ".bl liststats",
                "label": "List Blood Stats",
                "description": "Lists blood stats available.",
                "params": []
            },
            {
                "template": ".bl log",
                "label": "Toggle Blood Log",
                "description": "Toggles Legacy progress logging.",
                "params": []
            },
            {
                "template": ".bl resetstats",
                "label": "Reset Blood Stats",
                "description": "Reset stats for current blood legacy.",
                "params": []
            },
            {
                "template": ".bl set [Player] [Blood] [Level]",
                "label": "*Set Blood Level",
                "description": "Sets another player’s blood legacy level.",
                "params": ["Player", "Blood", "Level"],
                "options": {
                    "Blood": [
                        "Brute", "Corruption", "Creature", "Draculin", "Immortal", "Mutant", "Rogue", "Scholar", "Warrior", "Worker",
                    ],
                }
            }
        ]
    },

    "classes": {
        "Class Commands": [
            {
                "template": ".class c [Class]",
                "label":    "Change Class",
                "description": "Change classes.",
                "params":   ["Class"],
                "options":  {
                    "Class": [
                        "BloodKnight","DemonHunter","VampireLord",
                        "ShadowBlade","ArcaneSorcerer","DeathMage"
                    ]
                }
            },
            {
                "template": ".class csp [#]",
                "label":    "Choose Spell",
                "description": "Sets shift spell for class if prestige level is high enough.",
                "params":   ["#"],
            },
            {
                "template": ".class l",
                "label":    "List Classes",
                "description": "List available classes.",
                "params":   [],
            },
            {
                "template": ".class lsp [Class]",
                "label":    "List Spells",
                "description": "Shows spells that can be gained from class.",
                "params":   ["Class"],
                "options":  {
                    "Class": [
                        "BloodKnight","DemonHunter","VampireLord",
                        "ShadowBlade","ArcaneSorcerer","DeathMage"
                    ]
                }
            },
            {
                "template": ".class lst [Class]",
                "label":    "List Synergies",
                "description": "List weapon and blood stat synergies for a class.",
                "params":   ["Class"],
                "options":  {
                    "Class": [
                        "BloodKnight","DemonHunter","VampireLord",
                        "ShadowBlade","ArcaneSorcerer","DeathMage"
                    ]
                }
            },
            {
                "template": ".class shift",
                "label":    "Toggle Shift",
                "description": "Toggle shift spell.",
                "params":   [],
            },
            {
                "template": ".class s [Class]",
                "label":    "Select Class",
                "description": "Select class.",
                "params":   ["Class"],
                "options":  {
                    "Class": [
                        "BloodKnight","DemonHunter","VampireLord",
                        "ShadowBlade","ArcaneSorcerer","DeathMage"
                    ]
                }
            },
        ]
    },

    "familiars": {
        "Familiar Commands": [
            {"template": ".fam a [Player] [Guid]",     "label":"*Add Familiar",         "description":"Unit testing.","params":["Player","Guid"]},
            {"template": ".fam abg [BattleGroup]",     "label":"Add BattleGroup",      "description":"Creates new battle group.","params":["BattleGroup"]},
            {"template": ".fam ab [BoxName]",          "label":"Add Box",              "description":"Adds empty box with name.","params":["BoxName"]},
            {"template": ".fam b [#]",                 "label":"Bind Familiar",        "description":"Activates specified familiar.","params":["#"]},
            {"template": ".fam challenge [Player]",    "label":"Challenge Player",     "description":"Challenge or queue battle.","params":["Player"]},
            {"template": ".fam cbg [BattleGroup]",     "label":"Choose BattleGroup",   "description":"Sets active battle group.","params":["BattleGroup"]},
            {"template": ".fam cb [Name]",             "label":"Choose Box",           "description":"Choose active box of familiars.","params":["Name"]},
            {"template": ".fam dbg [BattleGroup]",     "label":"Del BattleGroup",      "description":"Deletes a battle group.","params":["BattleGroup"]},
            {"template": ".fam db [BoxName]",          "label":"Del Box",              "description":"Deletes specified box if empty.","params":["BoxName"]},
            {"template": ".fam echoes [VBloodName]",   "label":"Echoes Purchase",      "description":"VBlood purchasing for exo reward.","params":["VBloodName"]},
            {"template": ".fam actions",               "label":"Emote Actions",        "description":"Shows available emote actions.","params":[]},
            {"template": ".fam e",                     "label":"Toggle Emotes",        "description":"Toggle emote actions.","params":[]},
            {"template": ".fam gl",                    "label":"Get Level",            "description":"Display current familiar leveling.","params":[]},
            {"template": ".fam l",                     "label":"List Familiars",       "description":"Lists unlocked familiars.","params":[]},
            {"template": ".fam bg [BattleGroup]",      "label":"List BattleGroup",     "description":"Displays details of a battle group.","params":["BattleGroup"]},
            {"template": ".fam bgs",                   "label":"List BattleGroups",    "description":"Lists available battle groups.","params":[]},
            {"template": ".fam boxes",                 "label":"List Boxes",           "description":"Shows the available familiar boxes.","params":[]},
            {"template": ".fam mb [BoxName]",          "label":"Move Box",             "description":"Moves active familiar to specified box.","params":["BoxName"]},
            {"template": ".fam pr",                    "label":"Prestige Familiar",    "description":"Prestiges familiar.","params":[]},
            {"template": ".fam r [#]",                 "label":"Remove Familiar",      "description":"Removes familiar permanently.","params":["#"]},
            {"template": ".fam rb [Old] [New]",        "label":"Rename Box",           "description":"Renames a box.","params":["Old","New"]},
            {"template": ".fam reset",                 "label":"Reset Familiars",      "description":"Resets familiar data.","params":[]},
            {"template": ".fam s [Name]",              "label":"Search Familiars",     "description":"Searches boxes for familiar(s).","params":["Name"]},
            {"template": ".fam sba",                   "label":"*Set BattlArena",       "description":"Set battle arena location.","params":[]},
            {"template": ".fam sl [Player] [Level]",   "label":"*Set Level",            "description":"Set current familiar level.","params":["Player","Level"]},
            {"template": ".fam shiny [SpellSchool]",   "label":"Shiny Buff",           "description":"Chooses shiny buff for familiar.","params":["SpellSchool"], "options": {"SpellSchool":["blood", "chaos", "frost", "illusion", "storm", "unholy"]}},
            {"template": ".fam sbg [Group] [Slot]",    "label":"Slot BattlGroup",      "description":"Assigns to a battle group slot.","params":["Group","Slot"]},
            {"template": ".fam sb [Name]",             "label":"Smart Bind",           "description":"Searches and binds a familiar.","params":["Name"]},
            {"template": ".fam t",                     "label":"Toggle Familiar",      "description":"Calls or dismisses familiar.","params":[]},
            {"template": ".fam c",                     "label":"Toggle Combat",        "description":"Enable/disable combat for familiar.","params":[]},
            {"template": ".fam option [Setting]",      "label":"Toggle Option",        "description":"Toggles various familiar settings.","params":["Setting"]},
            {"template": ".fam ub",                    "label":"Unbind Familiar",      "description":"Destroys active familiar.","params":[]},
        ]
    },

    "leveling": {
        "Level Commands": [
            {"template": ".lvl get",                  "label":"Get Level",      "description":"Display current leveling progress.","params":[]},
            {"template": ".lvl ignore [Player]",      "label":"*Ignore XP",      "description":"Ignore shared experience for player.","params":["Player"]},
            {"template": ".lvl log",                  "label":"Toggle Log",     "description":"Toggles leveling progress logging.","params":[]},
            {"template": ".lvl set [Player] [Level]", "label":"*Set Level",      "description":"Sets player level.","params":["Player","Level"]},
        ]
    },

    "miscellaneous": {
        "Miscellaneous": [
            {"template": ".misc prepare",             "label":"Prepare Hunt",   "description":"Completes GettingReadyForTheHunt.","params":[]},
            {"template": ".misc remindme",            "label":"Toggle Remind",  "description":"Toggles general reminders.","params":[]},
            {"template": ".misc sct [Type]",          "label":"Toggle SCT",     "description":"Toggles scrolling text elements.","params":["Type"], "options": {"Type":["info","warning","error"]}},
            {"template": ".misc silence",             "label":"Silence Music",  "description":"Resets stuck combat music.","params":[]},
            {"template": ".misc kitme",               "label":"Starter Kit",    "description":"Provides starting kit.","params":[]},
            {"template": ".misc userstats",           "label":"User Stats",     "description":"Shows neat information about the player.","params":[]},
        ]
    },

    "prestige": {
        "Prestige Commands": [
            {"template": ".prestige exoform",                      "label":"Toggle Exoform",       "description":"Toggles taunting to enter exoform.","params":[]},
            {"template": ".prestige get [PrestigeType]",           "label":"Get Prestige",         "description":"Shows player's prestige status.","params":["PrestigeType"], "options":{"PrestigeType":["AxeExpertise", "BruteLegacy", "ClawsExpertise", "CreatureLegacy", "CrossbowExpertise",
                                                                                                                                                                                                        "DaggersExpertise", "DraculinLegacy", "Experience", "Exo", "FishingPoleExpertise", "GreatSwordExpertise",
                                                                                                                                                                                                        "ImmortalLegacy", "MaceExpertise", "MutantLegacy", "LongbowExpertise", "PistolsExpertise",
                                                                                                                                                                                                        "ReaperExpertise", "RogueLegacy", "ScholarLegacy", "SlashersExpertise", "SpearExpertise", "SwordExpertise",
                                                                                                                                                                                                        "TwinBladesExpertise", "UnarmedExpertise", "WhipExpertise", "WorkerLegacy" ]}},
            {"template": ".prestige iacknowledgethiswillremoveallprestigebuffsfromplayersandwantthattohappen",          "label":"*Ack Remove Buffs",     "description":"Globally removes prestige buffs.","params":[]},
            {"template": ".prestige ignore [Player]",              "label":"*Ignore Leaderboard",   "description":"Toggle player on prestige leaderboard.","params":["Player"]},
            {"template": ".prestige lb [PrestigeType]",            "label":"Leaderboard",          "description":"Lists prestige leaderboard.","params":["PrestigeType"], "options":{"PrestigeType":["AxeExpertise", "BruteLegacy", "ClawsExpertise", "CreatureLegacy", "CrossbowExpertise",
                                                                                                                                                                                                        "DaggersExpertise", "DraculinLegacy", "Experience", "Exo", "FishingPoleExpertise", "GreatSwordExpertise",
                                                                                                                                                                                                        "ImmortalLegacy", "MaceExpertise", "MutantLegacy", "LongbowExpertise", "PistolsExpertise",
                                                                                                                                                                                                        "ReaperExpertise", "RogueLegacy", "ScholarLegacy", "SlashersExpertise", "SpearExpertise", "SwordExpertise",
                                                                                                                                                                                                        "TwinBladesExpertise", "UnarmedExpertise", "WhipExpertise", "WorkerLegacy" ]}},
            {"template": ".prestige l",                            "label":"List Prestiges",       "description":"Lists prestiges available.","params":[]},
            {"template": ".prestige shroud",                       "label":"Toggle Shroud",        "description":"Toggles permashroud.","params":[]},
            {"template": ".prestige r [Player] [PrestigeType]",    "label":"*Reset Prestige",       "description":"Handles resetting prestige.","params":["Player","PrestigeType"], "options":{"PrestigeType":["AxeExpertise", "BruteLegacy", "ClawsExpertise", "CreatureLegacy", "CrossbowExpertise",
                                                                                                                                                                                                        "DaggersExpertise", "DraculinLegacy", "Experience", "Exo", "FishingPoleExpertise", "GreatSwordExpertise",
                                                                                                                                                                                                        "ImmortalLegacy", "MaceExpertise", "MutantLegacy", "LongbowExpertise", "PistolsExpertise",
                                                                                                                                                                                                        "ReaperExpertise", "RogueLegacy", "ScholarLegacy", "SlashersExpertise", "SpearExpertise", "SwordExpertise",
                                                                                                                                                                                                        "TwinBladesExpertise", "UnarmedExpertise", "WhipExpertise", "WorkerLegacy" ]}},
            {"template": ".prestige sf [Form]",                    "label":"Select Form",          "description":"Select active exoform shapeshift.","params":["Form"], "options":{"Form":["EvolvedVampire","CorruptedSerpent"]}},
            {"template": ".prestige me [PrestigeType]",            "label":"Prestige Self",        "description":"Handles player prestiging.","params":["PrestigeType"], "options":{"PrestigeType":["AxeExpertise", "BruteLegacy", "ClawsExpertise", "CreatureLegacy", "CrossbowExpertise",
                                                                                                                                                                                                        "DaggersExpertise", "DraculinLegacy", "Experience", "Exo", "FishingPoleExpertise", "GreatSwordExpertise",
                                                                                                                                                                                                        "ImmortalLegacy", "MaceExpertise", "MutantLegacy", "LongbowExpertise", "PistolsExpertise",
                                                                                                                                                                                                        "ReaperExpertise", "RogueLegacy", "ScholarLegacy", "SlashersExpertise", "SpearExpertise", "SwordExpertise",
                                                                                                                                                                                                        "TwinBladesExpertise", "UnarmedExpertise", "WhipExpertise", "WorkerLegacy" ]}},
            {"template": ".prestige set [Player] [PrestigeType] [Level]", "label":"*Set Prestige Level","description":"Sets a player's prestige level.","params":["Player","PrestigeType","Level"],"options":{"PrestigeType":["AxeExpertise", "BruteLegacy", "ClawsExpertise", "CreatureLegacy", "CrossbowExpertise",
                                                                                                                                                                                                        "DaggersExpertise", "DraculinLegacy", "Experience", "Exo", "FishingPoleExpertise", "GreatSwordExpertise",
                                                                                                                                                                                                        "ImmortalLegacy", "MaceExpertise", "MutantLegacy", "LongbowExpertise", "PistolsExpertise",
                                                                                                                                                                                                        "ReaperExpertise", "RogueLegacy", "ScholarLegacy", "SlashersExpertise", "SpearExpertise", "SwordExpertise",
                                                                                                                                                                                                        "TwinBladesExpertise", "UnarmedExpertise", "WhipExpertise", "WorkerLegacy" ]}},
            {"template": ".prestige sb",                           "label":"Sync Buffs",           "description":"Applies prestige buffs appropriately.","params":[]},
        ]
    },

    "professions": {
        "Profession Commands": [
            {"template": ".prof l",                             "label":"List Professions",   "description":"Lists professions available.","params":[]},
            {"template": ".prof get [Profession]",             "label":"Get Profession",     "description":"Display your current profession progress.","params":["Profession"], "options":{"Profession":["Mining","Woodcutting","Harvesting","Fishing","Alchemy","Blacksmithing","Enchanting","Tailoring"]}},
            {"template": ".prof log",                          "label":"Toggle Log",         "description":"Toggles profession progress logging.","params":[]},
            {"template": ".prof set [Player] [Profession] [Level]", "label":"*Set Profession Level","description":"Sets player profession level.","params":["Player","Profession","Level"], "options":{"Profession":["Mining","Woodcutting","Harvesting","Fishing","Alchemy","Blacksmithing","Enchanting","Tailoring"]}},
        ]
    },

    "quests": {
        "Quest Commands": [
            {"template": ".quest c [Name] [QuestType]", "label":"*Force Complete",  "description":"Forcibly completes a specified quest.","params":["Name","QuestType"], "options":{"QuestType":["daily","weekly"]}},
            {"template": ".quest log",                 "label":"Toggle Log",      "description":"Toggles quest progress logging.","params":[]},
            {"template": ".quest p [QuestType]",       "label":"Progress",        "description":"Display your current quest progress.","params":["QuestType"], "options":{"QuestType":["daily","weekly"]}},
            {"template": ".quest rf [Name]",           "label":"*Refresh Quests",  "description":"Refreshes daily and weekly quests.","params":["Name"]},
            {"template": ".quest r [QuestType]",       "label":"Reroll Quest",    "description":"Reroll quest for cost.","params":["QuestType"], "options":{"QuestType":["daily","weekly"]}},
            {"template": ".quest t [QuestType]",       "label":"Track Quest",     "description":"Locate and track quest target.","params":["QuestType"], "options":{"QuestType":["daily","weekly"]}},
        ]
    },

    "weapon": {
        "Weapon Commands": [
            {
                "template": ".wep cst [WeaponOrStat] [WeaponStat]",
                "label": "Choose Stat",
                "description": "Choose a weapon stat to enhance based on expertise.",
                "params": ["WeaponOrStat","WeaponStat"],
                "options": {
                    "WeaponOrStat": ["Axe", "Claws", "Crossbow", "Daggers", "FishingPole", "Greatsword", 
                                     "Longbow", "Mace", "Pistol", "Reaper",
                                     "Slashers", "Spear", "Sword", "Twinblades", "Unarmed", "Whip"],
                    "WeaponStat": [
                        "MaxHealth","MovementSpeed","PrimaryAttackSpeed","PhysicalLifeLeech",
                        "SpellLifeLeech","PrimaryLifeLeech","PhysicalPower","SpellPower",
                        "PhysicalCritChance","PhysicalCritDamage","SpellCritChance","SpellCritDamage"
                    ]
                }
            },
            {
                "template": ".wep get",
                "label": "Get Expertise",
                "description": "Display current weapon expertise details.",
                "params": []
            },
            {
                "template": ".wep list",
                "label": "List Expertises",
                "description": "List weapon expertise categories.",
                "params": []
            },
            {
                "template": ".wep liststats",
                "label": "List Weapon Stats",
                "description": "List available weapon stats.",
                "params": []
            },
            {
                "template": ".wep lockspells",
                "label": "Lock Spells",
                "description": "Lock in your next spells to unarmed slots.",
                "params": []
            },
            {
                "template": ".wep log",
                "label": "Toggle Expertise Log",
                "description": "Toggle logging of weapon expertise gains.",
                "params": []
            },
            {
                "template": ".wep resetstats",
                "label": "Reset Weapon Stats",
                "description": "Reset current weapon stat selections.",
                "params": []
            },
            {
                "template": ".wep set [Name] [Weapon] [Level]",
                "label": "*Set Expertise",
                "description": "Set a player’s weapon expertise level.",
                "params": ["Name","Weapon","Level"]
            },
            {
                "template": ".wep setspells [Name] [Slot] [PrefabGuid] [Radius]",
                "label": "*Set Spells",
                "description": "Manually assign spells for testing with optional radius.",
                "params": ["Name","Slot","PrefabGuid","Radius"]
            }
        ]
    }
}
