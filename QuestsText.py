from Common import *

cvs = []

cvs.append(["ChapterCompleted", "Chapter complete."])
cvs.append(["Completed", "Quest complete."])
cvs.append(["Collect", "Collect this item."])
cvs.append(["Achievement", "Achievement!"])
cvs.append(["RefiningMachine", "RefiningMachineDescription"])

cvs.append(["FirstSteps", "First Steps"])
cvs.append(["RoadToSteel", "Road to Steel"])
cvs.append(["Farming", "Farming"])
cvs.append(["Refining", "Ore Refining"])
cvs.append(["Steam", "Steam"])
cvs.append(["RoadToAluminium", "Road to Aluminium"])
cvs.append(["RoadToSS", "Road to Stainless Steel"])
cvs.append(["RoadToTitanium", "Road to Titanium"])
cvs.append(["RoadToHardMetal", "Road to Hard Metal"])
cvs.append(["RoadToNeutronium", "Road to Neutronium"])
cvs.append(["Other", "Other"])
cvs.append(["Decorative", "Decorative"])
cvs.append(["Woodwork", "Woodwork"])
cvs.append(["FasterRefining", "Faster Refining"])
cvs.append(["Logistics", "Logistics"])
cvs.append(["FastTravel", "Fast Travel"])
cvs.append(["FasterSteel", "Faster Steel"])
cvs.append(["AdvancedLogistics", "Advanced Logistics"])
cvs.append(["HeatTransferring", "Heat Transferring"])

cvs.append(["CoalPiece", "CoalPieceDescription"])
cvs.append(["CoalDust", "CoalDustDescription"])

cvs.append(["CokePiece", "CokePieceDescription"])
cvs.append(["CokeDust", "Faster way of producing a coke. Put a <item>Coal Dust</> into a <machine>Coke Oven</>."])

cvs.append(["HigherLevel", "This is just improved version of machine. It can make complexer recipes without penalty and can use modules."])
cvs.append(["Jumppack", "This is a really fast way to travel. You need to select it on the hotbar to use. Press jump to use."])
cvs.append(["Plate", "While it is possible to create all machines directly from ingots - this is not the best way.\n"
"In a much more efficient way, it will create plates with the help of <machine>Automatic Hammer</>\n"
"It creates 1 plate of 1 ingot, while hands creates 1 plate of 2 ingots."])

cvs.append(["Refined", "You will receive 1.5 times more metal from ore by making this item."])

cvs.append(["Furnace", "Uses fuel to produce a <item>Heat</>. The Heat is fransferring into block on top of a furnace. Heat output is marked by flame icon."])
cvs.append(["Dryer", "Uses heat to make recipes. Usable to increase fuel efficiency by producing Coal Dust from a <item>Log</>/<item>Stick</>/<item>Sawdust</>."])
cvs.append(["Smelter", "Uses heat to make ingots. Ingots are smelted from ore very slowly. It is much more efficient to refine an ore before smelting."])
cvs.append(["AlloySmelter", "AlloySmelterDescription"])
cvs.append(["CastIron", "Used for advanced steel making process. Uses less coke in the process, and also has a much higher production rate.\n"
"The resulting cast iron must be melted in an <machine>Arc Furnace.</>"])

cvs.append(["CopperOre", "Common ore. Occurs in all biomes. Plenty of <item>Copper Ore</> can be found at a coast. You can see a water from some hill."])

cvs.append(["IronOre", "Common ore. Occurs in all biomes. Plenty of <item>Iron Ore</> can be found in the swamp."])

cvs.append(["Boiler", "BoilerDescription"])
cvs.append(["Pump", "Infinitely generates water."])
cvs.append(["Pipe", "PipeDescription"])
cvs.append(["Bed", "Right click on a Bed to update your Spawnpoint. You can travel to a Spawnpoint from the Pause Menu (Esc)."])

cvs.append(["Organics", "Can be gathered from most of small plants in the world."])
cvs.append(["BambooFarm", "Growing bamboo sprout. Break with a <item>Multitool</> to harvest."])
cvs.append(["PumpkinFarm", "Growing pumpkin. Break with a <item>Multitool</> to harvest."])

cvs.append(["AutomaticHammer", "AutomaticHammerDescription"])
cvs.append(["Macerator", "MaceratorDescription"])
cvs.append(["OreWasher", "OreWasherDescription"])

cvs.append(["BlastFurnace", "It has 2 inputs: one for <item>Iron Ingots</>, the other for a coke. To output a production use a <machine>Robot Arm</>."])
cvs.append(["CokeOven", "Has input for a coal and output for a coke. Has fluid output for an <item>Ore Water</> marked with drop icon."])

cvs.append(["RobotArm", "Robot Arm"])
cvs.append(["FilteringRobotArm", "FilteringRobotArm"])
cvs.append(["Conveyor", "Conveyor"])
cvs.append(["ConveyorSplitter", "Conveyor Splitter"])

write_file("Loc/source/quests.json", cvs)