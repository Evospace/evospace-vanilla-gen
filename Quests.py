from Common import *

quests = []
qchapters = []

# RoadToSteel

qchapters.append({
	"Name": "RoadToSteel" + qchapter,
	"Class": qchapter,
	"Key": "RoadToSteel",
	"Sorter": 4,
	"Reward": {
		"Items" : [
			{
				"Name": "SteelIngot" + static_item,
				"Count": 5
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "IronOre" + quest,
	"QuestTextKeys": [
		"Collect",
		"IronOre"
	],
	"Item": "IronOre" + static_item,
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "IronImpureOreGravel2" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "IronImpureOreGravel" + static_item,
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 0.1
})

quests.append({
	"Class": quest,
	"Name": "IronOreGravel2" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "IronOreGravel" + static_item,
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 0.1
})

quests.append({
	"Class": quest,
	"Name": "IronImpureOreDust2" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "IronImpureOreDust" + static_item,
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 0.1
})

quests.append({
	"Class": quest,
	"Name": "CokeOven" + quest,
	"QuestTextKeys": [
		"Collect",
		"CokeOven"
	],
	"Item": "CopperCokeOven" + static_item,
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "BlastFurnace" + quest,
	"QuestTextKeys": [
		"Collect",
		"BlastFurnace"
	],
	"Item": "CopperBlastFurnace" + static_item,
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "CoalPiece" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement",
		"CoalPiece"
	],
	"Item": "CoalPiece" + static_item,
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 3
})

quests.append({
	"Class": quest,
	"Name": "CokePiece" + quest,
	"QuestTextKeys": [
		"Collect",
		"CokePiece"
	],
	"Item": "CokePiece" + static_item,
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 3.5
})

quests.append({
	"Class": quest,
	"Name": "CoalDust" + quest,
	"QuestTextKeys": [
		"Collect",
		"CoalDust"
	],
	"Item": "CoalDust" + static_item,
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 4
})

quests.append({
	"Class": quest,
	"Name": "CokeDust" + quest,
	"QuestTextKeys": [
		"Collect",
		"CokeDust"
	],
	"Item": "CokeDust" + static_item,
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 4.5
})

quests.append({
	"Class": quest,
	"Name": "SteelAge" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "SteelIngot" + static_item,
	"Achievement": "SteelAge",
	"Chapter": "RoadToSteel" + qchapter,
	"Sorter": 5
})

# Other

qchapters.append({
	"Name": "Other" + qchapter,
	"Class": qchapter,
	"Key": "Other",
	"Sorter": 1000,
	"Reward": {
		"Items" : [
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "AluminiumAge" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "AluminiumIngot" + static_item,
	"Achievement": "AluminiumAge",
	"Chapter": "Other" + qchapter
})

quests.append({
	"Class": quest,
	"Name": "TitaniumOre" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "TitaniumOre" + static_item,
	"Achievement": "TitaniumOre",
	"Chapter": "Other" + qchapter
})

quests.append({
	"Class": quest,
	"Name": "TitaniumAge" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "TitaniumIngot" + static_item,
	"Achievement": "TitaniumAge",
	"Chapter": "Other" + qchapter
})

quests.append({
	"Class": quest,
	"Name": "StainlessSteelAge" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "StainlessSteelIngot" + static_item,
	"Achievement": "StainlessSteelAge",
	"Chapter": "Other" + qchapter
})

quests.append({
	"Class": quest,
	"Name": "IronOreAchievement" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "IronOre" + static_item,
	"Achievement": "IronOre",
	"Chapter": "Other" + qchapter,
})

quests.append({
	"Class": quest,
	"Name": "AluminiumOreAchievement" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "AluminiumOre" + static_item,
	"Achievement": "AluminiumOre",
	"Chapter": "Other" + qchapter
})

quests.append({
	"Class": quest,
	"Name": "GoldOreAchievement" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "GoldOre" + static_item,
	"Achievement": "GoldOre",
	"Chapter": "Other" + qchapter
})

quests.append({
	"Class": quest,
	"Name": "UraniumOreAchievement" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "UraniumOre" + static_item,
	"Achievement": "UraniumOre",
	"Chapter": "Other" + qchapter
})

quests.append({
	"Class": quest,
	"Name": "CoalOreAchievement" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "CoalPiece" + static_item,
	"Achievement": "CoalOre",
	"Chapter": "Other" + qchapter
})

# FirstSteps

qchapters.append({
	"Name": "FirstSteps" + qchapter,
	"Class": qchapter,
	"Key": "FirstSteps",
	"Sorter": 0,
	"Reward": {
		"Items" : [
			{
				"Name": "CopperMultitool" + static_item,
				"Count": 1
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "Log" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "Log" + static_item,
	"Achievement": "Log",
	"Chapter": "FirstSteps" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "Furnace" + quest,
	"QuestTextKeys": [
		"Collect",
		"Furnace"
	],
	"Item": "StoneFurnace" + static_item,
	"Chapter": "FirstSteps" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "Dryer" + quest,
	"QuestTextKeys": [
		"Collect",
		"Dryer"
	],
	"Item": "StoneDryer" + static_item,
	"Chapter": "FirstSteps" + qchapter,
	"Sorter": 1.5
})

quests.append({
	"Class": quest,
	"Name": "Smelter" + quest,
	"QuestTextKeys": [
		"Collect",
		"Smelter"
	],
	"Item": "StoneSmelter" + static_item,
	"Chapter": "FirstSteps" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "Bed" + quest,
	"QuestTextKeys": [
		"Collect",
		"Bed"
	],
	"Item": "Bed" + static_item,
	"Chapter": "FirstSteps" + qchapter,
	"Sorter": 2.5
})

quests.append({
	"Class": quest,
	"Name": "CopperOre" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement",
		"CopperOre"
	],
	"Item": "CopperOre" + static_item,
	"Achievement": "CopperOre",
	"Chapter": "FirstSteps" + qchapter,
	"Sorter": 3
})

quests.append({
	"Class": quest,
	"Name": "CopperAge" + quest,
	"QuestTextKeys": [
		"Collect",
		"Achievement"
	],
	"Item": "CopperIngot" + static_item,
	"Achievement": "CopperAge",
	"Chapter": "FirstSteps" + qchapter,
	"Sorter": 4
})

# Farming

qchapters.append({
	"Name": "Farming" + qchapter,
	"Class": qchapter,
	"Key": "Farming",
	"Sorter": 1,
	"Reward": {
		"Items" : [
			{
				"Name": "CopperMultitool" + static_item,
				"Count": 1
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "Organics" + quest,
	"QuestTextKeys": [
		"Collect",
		"Organics"
	],
	"Item": "OrganicsPiece" + static_item,
	"Chapter": "Farming" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "Farm" + quest,
	"QuestTextKeys": [
		"Collect",
		"BambooFarm"
	],
	"Item": "CopperFarm" + static_item,
	"Chapter": "Farming" + qchapter,
	"Sorter": 1
})

# Steam

qchapters.append({
	"Name": "Steam" + qchapter,
	"Class": qchapter,
	"Key": "Steam",
	"Sorter": 2,
	"Reward": {
		"Items" : [
			{
				"Name": "CopperVent" + static_item,
				"Count": 1
			},{
				"Name": "CopperPipe" + static_item,
				"Count": 10
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "Boiler" + quest,
	"QuestTextKeys": [
		"Collect",
		"Boiler"
	],
	"Item": "SteelBoiler" + static_item,
	"Chapter": "Steam" + qchapter,
	"Sorter": .5
})

quests.append({
	"Class": quest,
	"Name": "Pump" + quest,
	"QuestTextKeys": [
		"Collect",
		"Pump"
	],
	"Item": "SteelPump" + static_item,
	"Chapter": "Steam" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "Pipe" + quest,
	"QuestTextKeys": [
		"Collect",
		"Pipe"
	],
	"Item": "SteelPipe" + static_item,
	"Chapter": "Steam" + qchapter,
	"Sorter": 2
})

# Refining

qchapters.append({
	"Name": "Refining" + qchapter,
	"Class": qchapter,
	"Key": "Refining",
	"Sorter": 3,
	"Reward": {
		"Items" : [
			{
				"Name": "CopperFluidDump" + static_item,
				"Count": 1
			},
			{
				"Name": "CopperVent" + static_item,
				"Count": 2
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "AutomaticHammer" + quest,
	"QuestTextKeys": [
		"Collect",
		"AutomaticHammer",
		"RefiningMachine",
	],
	"Item": "CopperAutomaticHammer" + static_item,
	"Chapter": "Refining" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "CopperPlate" + quest,
	"QuestTextKeys": [
		"Collect",
		"Plate"
	],
	"Item": "CopperPlate" + static_item,
	"Chapter": "Refining" + qchapter,
	"Sorter": 0.5
})

quests.append({
	"Class": quest,
	"Name": "CopperImpureOreGravel" + quest,
	"QuestTextKeys": [
		"Collect",
		"Refined"
	],
	"Item": "CopperImpureOreGravel" + static_item,
	"Chapter": "Refining" + qchapter,
	"Sorter": 0.5
})

quests.append({
	"Class": quest,
	"Name": "Washer" + quest,
	"QuestTextKeys": [
		"Collect",
		"OreWasher",
		"RefiningMachine",
	],
	"Item": "SteelOreWasher" + static_item,
	"Chapter": "Refining" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "CopperOreGravel" + quest,
	"QuestTextKeys": [
		"Collect",
		"Refined"
	],
	"Item": "CopperOreGravel" + static_item,
	"Chapter": "Refining" + qchapter,
	"Sorter": 1.5
})

quests.append({
	"Class": quest,
	"Name": "Macerator" + quest,
	"QuestTextKeys": [
		"Collect",
		"Macerator",
		"RefiningMachine",
	],
	"Item": "CopperMacerator" + static_item,
	"Chapter": "Refining" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "CopperImpureOreDust" + quest,
	"QuestTextKeys": [
		"Collect",
		"Refined"
	],
	"Item": "CopperImpureOreDust" + static_item,
	"Chapter": "Refining" + qchapter,
	"Sorter": 2.5
})

# Fast travel

qchapters.append({
	"Name": "FastTravel" + qchapter,
	"Class": qchapter,
	"Key": "FastTravel",
	"Sorter": 3.1,
	"Reward": {
		"Items" : [
			{
				"Name": "CopperIngot" + static_item,
				"Count": 20
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "Steampack" + quest,
	"QuestTextKeys": [
		"Collect",
		"Jumppack",
	],
	"Item": "Steampack" + static_item,
	"Chapter": "FastTravel" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "Jetpack" + quest,
	"QuestTextKeys": [
		"Collect",
		"Jumppack",
	],
	"Item": "Jetpack" + static_item,
	"Chapter": "FastTravel" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "AdvancedJetpack" + quest,
	"QuestTextKeys": [
		"Collect",
		"Jumppack",
	],
	"Item": "AdvancedJetpack" + static_item,
	"Chapter": "FastTravel" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "AntigravityUnit" + quest,
	"QuestTextKeys": [
		"Collect",
		"Jumppack",
	],
	"Item": "AntigravityUnit" + static_item,
	"Chapter": "FastTravel" + qchapter,
	"Sorter": 3
})

# Logistics

qchapters.append({
	"Name": "Logistics" + qchapter,
	"Class": qchapter,
	"Key": "Logistics",
	"Sorter": 4.1,
	"Reward": {
		"Items" : [
			{
				"Name": "SteelFilteringRobotArm" + static_item,
				"Count": 3
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "CopperRobotArm" + quest,
	"QuestTextKeys": [
		"Collect",
		"RobotArm"
	],
	"Item": "CopperRobotArm" + static_item,
	"Chapter": "Logistics" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "SteelRobotArm" + quest,
	"QuestTextKeys": [
		"Collect",
		"RobotArm"
	],
	"Item": "SteelRobotArm" + static_item,
	"Chapter": "Logistics" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "SteelFilteringRobotArm" + quest,
	"QuestTextKeys": [
		"Collect",
		"FilteringRobotArm"
	],
	"Item": "SteelFilteringRobotArm" + static_item,
	"Chapter": "Logistics" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "CopperConveyor" + quest,
	"QuestTextKeys": [
		"Collect",
		"Conveyor"
	],
	"Item": "CopperConveyor" + static_item,
	"Chapter": "Logistics" + qchapter,
	"Sorter": 3
})

quests.append({
	"Class": quest,
	"Name": "CopperConveyorSplitter" + quest,
	"QuestTextKeys": [
		"Collect",
		"ConveyorSplitter"
	],
	"Item": "CopperConveyorSplitter" + static_item,
	"Chapter": "Logistics" + qchapter,
	"Sorter": 4
})

quests.append({
	"Class": quest,
	"Name": "SteelConveyor" + quest,
	"QuestTextKeys": [
		"Collect",
		"Conveyor"
	],
	"Item": "SteelConveyor" + static_item,
	"Chapter": "Logistics" + qchapter,
	"Sorter": 5
})

quests.append({
	"Class": quest,
	"Name": "SteelConveyorSplitter" + quest,
	"QuestTextKeys": [
		"Collect",
		"ConveyorSplitter"
	],
	"Item": "SteelConveyorSplitter" + static_item,
	"Chapter": "Logistics" + qchapter,
	"Sorter": 6
})

quests.append({
	"Class": quest,
	"Name": "CopperDeployer" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "CopperDeployer" + static_item,
	"Chapter": "Logistics" + qchapter,
	"Sorter": 7
})

quests.append({
	"Class": quest,
	"Name": "SteelDeployer" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "SteelDeployer" + static_item,
	"Chapter": "Logistics" + qchapter,
	"Sorter": 8
})

# FasterSteel

qchapters.append({
	"Name": "FasterSteel" + qchapter,
	"Class": qchapter,
	"Key": "FasterSteel",
	"Sorter": 4.15,
	"Reward": {
		"Items" : [
			{
				"Name": "SteelIngot" + static_item,
				"Count": 10
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "SteelCokeOven" + quest,
	"QuestTextKeys": [
		"Collect",
		"CokeOven"
	],
	"Item": "SteelCokeOven" + static_item,
	"Chapter": "FasterSteel" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "CokeDustFasterS" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "CokeDust" + static_item,
	"Chapter": "FasterSteel" + qchapter,
	"Sorter": 1.1
})

quests.append({
	"Class": quest,
	"Name": "IronDustFasterS" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "IronDust" + static_item,
	"Chapter": "FasterSteel" + qchapter,
	"Sorter": 1.2
})

quests.append({
	"Class": quest,
	"Name": "SteelAlloySmelter" + quest,
	"QuestTextKeys": [
		"Collect",
		"AlloySmelter"
	],
	"Item": "SteelAlloySmelter" + static_item,
	"Chapter": "FasterSteel" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "CastIronIngot" + quest,
	"QuestTextKeys": [
		"Collect",
		"CastIron"
	],
	"Item": "CastIronIngot" + static_item,
	"Chapter": "FasterSteel" + qchapter,
	"Sorter": 3
})

quests.append({
	"Class": quest,
	"Name": "CastIronDust" + quest,
	"QuestTextKeys": [
		"Collect",
		"CastIron"
	],
	"Item": "CastIronDust" + static_item,
	"Chapter": "FasterSteel" + qchapter,
	"Sorter": 3.1
})

quests.append({
	"Class": quest,
	"Name": "SteelArcFurnace" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "SteelArcFurnace" + static_item,
	"Chapter": "FasterSteel" + qchapter,
	"Sorter": 4
})

# Faster Refining

qchapters.append({
	"Name": "FasterRefining" + qchapter,
	"Class": qchapter,
	"Key": "FasterRefining",
	"Sorter": 4.2,
	"Reward": {
		"Items" : [
			{
				"Name": "SteelPipe" + static_item,
				"Count": 5
			},
			{
				"Name": "CopperVent" + static_item,
				"Count": 2
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "SteelAutomaticHammer" + quest,
	"QuestTextKeys": [
		"Collect",
		"HigherLevel"
	],
	"Item": "SteelAutomaticHammer" + static_item,
	"Chapter": "FasterRefining" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "SteelPlate" + quest,
	"QuestTextKeys": [
		"Collect",
		"Plate"
	],
	"Item": "SteelPlate" + static_item,
	"Chapter": "FasterRefining" + qchapter,
	"Sorter": 0.5
})

quests.append({
	"Class": quest,
	"Name": "IronImpureOreGravel" + quest,
	"QuestTextKeys": [
		"Collect",
		"Refined"
	],
	"Item": "IronImpureOreGravel" + static_item,
	"Chapter": "FasterRefining" + qchapter,
	"Sorter": 0.5
})

quests.append({
	"Class": quest,
	"Name": "SteelWasher" + quest,
	"QuestTextKeys": [
		"Collect",
		"HigherLevel"
	],
	"Item": "SteelOreWasher" + static_item,
	"Chapter": "FasterRefining" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "IronOreGravel" + quest,
	"QuestTextKeys": [
		"Collect",
		"Refined"
	],
	"Item": "IronOreGravel" + static_item,
	"Chapter": "FasterRefining" + qchapter,
	"Sorter": 1.5
})

quests.append({
	"Class": quest,
	"Name": "SteelMacerator" + quest,
	"QuestTextKeys": [
		"Collect",
		"HigherLevel"
	],
	"Item": "SteelMacerator" + static_item,
	"Chapter": "FasterRefining" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "IronImpureOreDust" + quest,
	"QuestTextKeys": [
		"Collect",
		"Refined"
	],
	"Item": "IronImpureOreDust" + static_item,
	"Chapter": "FasterRefining" + qchapter,
	"Sorter": 2.5
})

# RoadToAluminium

qchapters.append({
	"Name": "RoadToAluminium" + qchapter,
	"Class": qchapter,
	"Key": "RoadToAluminium",
	"Sorter": 4.25,
	"Reward": {
		"Items" : [
			{
				"Name": "AluminiumIngot" + static_item,
				"Count": 5
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "AluminiumOre" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumOre" + static_item,
	"Chapter": "RoadToAluminium" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "AluminiumImpureOreGravel" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumImpureOreGravel" + static_item,
	"Chapter": "RoadToAluminium" + qchapter,
	"Sorter": 0.1
})

quests.append({
	"Class": quest,
	"Name": "AluminiumOreGravel" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumOreGravel" + static_item,
	"Chapter": "RoadToAluminium" + qchapter,
	"Sorter": 0.1
})

quests.append({
	"Class": quest,
	"Name": "AluminiumImpureOreDust" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumImpureOreDust" + static_item,
	"Chapter": "RoadToAluminium" + qchapter,
	"Sorter": 0.1
})

quests.append({
	"Class": quest,
	"Name": "AluminiumOxideDust" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumOxideDust" + static_item,
	"Chapter": "RoadToAluminium" + qchapter,
	"Sorter": 0.1
})

quests.append({
	"Class": quest,
	"Name": "SteelAlloySmelterAlum" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "SteelAlloySmelter" + static_item,
	"Chapter": "RoadToAluminium" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "AluminiumCarbideIngot" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumCarbideIngot" + static_item,
	"Chapter": "RoadToAluminium" + qchapter,
	"Sorter": 1.5
})

quests.append({
	"Class": quest,
	"Name": "AluminiumCarbideDust" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumCarbideDust" + static_item,
	"Chapter": "RoadToAluminium" + qchapter,
	"Sorter": 2.5
})

quests.append({
	"Class": quest,
	"Name": "SteelArcFurnaceAlum" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "SteelArcFurnace" + static_item,
	"Chapter": "RoadToAluminium" + qchapter,
	"Sorter": 3
})

quests.append({
	"Class": quest,
	"Name": "AluminiumIngot" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumIngot" + static_item,
	"Chapter": "RoadToAluminium" + qchapter,
	"Sorter": 4
})

# AdvancedLogistics

qchapters.append({
	"Name": "AdvancedLogistics" + qchapter,
	"Class": qchapter,
	"Key": "AdvancedLogistics",
	"Sorter": 4.3,
	"Reward": {
		"Items" : [
			{
				"Name": "AluminiumPneumaticPipe" + static_item,
				"Count": 15
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "CopperBufferChest" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "CopperBufferChest" + static_item,
	"Chapter": "AdvancedLogistics" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "SteelBufferChest" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "SteelBufferChest" + static_item,
	"Chapter": "AdvancedLogistics" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "AluminiumBufferChest" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumBufferChest" + static_item,
	"Chapter": "AdvancedLogistics" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "AluminiumDeployer" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumDeployer" + static_item,
	"Chapter": "AdvancedLogistics" + qchapter,
	"Sorter": 4
})

quests.append({
	"Class": quest,
	"Name": "AluminiumRobotArm" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumRobotArm" + static_item,
	"Chapter": "AdvancedLogistics" + qchapter,
	"Sorter": 5
})

quests.append({
	"Class": quest,
	"Name": "AluminiumFilteringRobotArm" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumFilteringRobotArm" + static_item,
	"Chapter": "AdvancedLogistics" + qchapter,
	"Sorter": 6
})

quests.append({
	"Class": quest,
	"Name": "AluminiumPneumaticPipe" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumPneumaticPipe" + static_item,
	"Chapter": "AdvancedLogistics" + qchapter,
	"Sorter": 7
})

quests.append({
	"Class": quest,
	"Name": "AluminiumPneumaticInput" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "AluminiumPneumaticInput" + static_item,
	"Chapter": "AdvancedLogistics" + qchapter,
	"Sorter": 8
})

quests.append({
	"Class": quest,
	"Name": "AluminiumConveyor" + quest,
	"QuestTextKeys": [
		"Collect",
		"Conveyor"
	],
	"Item": "AluminiumConveyor" + static_item,
	"Chapter": "AdvancedLogistics" + qchapter,
	"Sorter": 9
})

quests.append({
	"Class": quest,
	"Name": "AluminiumConveyorSplitter" + quest,
	"QuestTextKeys": [
		"Collect",
		"ConveyorSplitter"
	],
	"Item": "AluminiumConveyorSplitter" + static_item,
	"Chapter": "AdvancedLogistics" + qchapter,
	"Sorter": 10
})

# RoadToSS

qchapters.append({
	"Name": "RoadToSS" + qchapter,
	"Class": qchapter,
	"Key": "RoadToSS",
	"Sorter": 5,
	"Reward": {
		"Items" : [
			{
				"Name": "StainlessSteelIngot" + static_item,
				"Count": 5
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "ChromeOxideDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "ChromeOxideDust" + static_item,
	"Chapter": "RoadToSS" + qchapter,
	"Sorter": 9.6
})

quests.append({
	"Class": quest,
	"Name": "AluminothermicChromeDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "AluminothermicChromeDust" + static_item,
	"Chapter": "RoadToSS" + qchapter,
	"Sorter": 9.7
})

quests.append({
	"Class": quest,
	"Name": "AluminiumSolidFurnace" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "AluminiumSolidFurnace" + static_item,
	"Chapter": "RoadToSS" + qchapter,
	"Sorter": 9.8
})

quests.append({
	"Class": quest,
	"Name": "ChromeDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "ChromeDust" + static_item,
	"Chapter": "RoadToSS" + qchapter,
	"Sorter": 9.85
})

quests.append({
	"Class": quest,
	"Name": "IronDustSS" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "IronDust" + static_item,
	"Chapter": "RoadToSS" + qchapter,
	"Sorter": 9.9
})

quests.append({
	"Class": quest,
	"Name": "NickelDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "NickelDust" + static_item,
	"Chapter": "RoadToSS" + qchapter,
	"Sorter": 9.9
})

quests.append({
	"Class": quest,
	"Name": "AluminiumMixer" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "AluminiumMixer" + static_item,
	"Chapter": "RoadToSS" + qchapter,
	"Sorter": 9.95
})

quests.append({
	"Class": quest,
	"Name": "StainlessSteelDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "StainlessSteelDust" + static_item,
	"Chapter": "RoadToSS" + qchapter,
	"Sorter": 10
})

quests.append({
	"Class": quest,
	"Name": "AluminiumArcFurnace" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "AluminiumArcFurnace" + static_item,
	"Chapter": "RoadToSS" + qchapter,
	"Sorter": 11
})

quests.append({
	"Class": quest,
	"Name": "StainlessSteelIngot" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "StainlessSteelIngot" + static_item,
	"Chapter": "RoadToSS" + qchapter,
	"Sorter": 12
})

# HeatTransferring

qchapters.append({
	"Name": "HeatTransferring" + qchapter,
	"Class": qchapter,
	"Key": "HeatTransferring",
	"Sorter": 5.5,
	"Reward": {
		"Items" : [
			{
				"Name": "NakCoolantDust" + static_item,
				"Count": 10
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "StainlessSteelHeatExchanger" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "StainlessSteelHeatExchanger" + static_item,
	"Chapter": "HeatTransferring" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "StainlessSteelInverseHeatExchanger" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "StainlessSteelInverseHeatExchanger" + static_item,
	"Chapter": "HeatTransferring" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "StainlessSteelRadiator" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "StainlessSteelRadiator" + static_item,
	"Chapter": "HeatTransferring" + qchapter,
	"Sorter": 3
})

quests.append({
	"Class": quest,
	"Name": "NakCoolantDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "NakCoolantDust" + static_item,
	"Chapter": "HeatTransferring" + qchapter,
	"Sorter": 9.45
})

# RoadToTitanium

qchapters.append({
	"Name": "RoadToTitanium" + qchapter,
	"Class": qchapter,
	"Key": "RoadToTitanium",
	"Sorter": 6,
	"Reward": {
		"Items" : [
			{
				"Name": "TitaniumIngot" + static_item,
				"Count": 5
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "CokeDustTit" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "CokeDust" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "TitaniumOxideDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TitaniumOxideDust" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 1.1
})

quests.append({
	"Class": quest,
	"Name": "StainlessSteelAlloySmelter" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "StainlessSteelAlloySmelter" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 1.2
})

quests.append({
	"Class": quest,
	"Name": "PreparedTitaniumOxideDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "PreparedTitaniumOxideDust" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 1.3
})

quests.append({
	"Class": quest,
	"Name": "ManganeseOxideDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "ManganeseOxideDust" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 3
})

quests.append({
	"Class": quest,
	"Name": "AluminothermicManganeseDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "AluminothermicManganeseDust" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 3.1
})

quests.append({
	"Class": quest,
	"Name": "StainlessSteelSolidFurnace" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "StainlessSteelSolidFurnace" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 3.2
})

quests.append({
	"Class": quest,
	"Name": "ManganeseDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "ManganeseDust" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 3.3
})

quests.append({
	"Class": quest,
	"Name": "SaltDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "SaltDust" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 7
})

quests.append({
	"Class": quest,
	"Name": "StainlessSteelChemReactor" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "StainlessSteelChemReactor" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 8
})

quests.append({
	"Class": quest,
	"Name": "TitaniumSponge" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TitaniumSponge" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 9.4
})

quests.append({
	"Class": quest,
	"Name": "StainlessSteelInductionFurnace" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "StainlessSteelInductionFurnace" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 9.5
})

quests.append({
	"Class": quest,
	"Name": "TitaniumIngot" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TitaniumIngot" + static_item,
	"Chapter": "RoadToTitanium" + qchapter,
	"Sorter": 9.6
})

# RoadToHardMetal

qchapters.append({
	"Name": "RoadToHardMetal" + qchapter,
	"Class": qchapter,
	"Key": "RoadToHardMetal",
	"Sorter": 7,
	"Reward": {
		"Items" : [
			{
				"Name": "HardMetalIngot" + static_item,
				"Count": 5
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "TungstenOxideDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TungstenOxideDust" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "TitaniumInductionFurnace2" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TitaniumInductionFurnace" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "HotTungstenIngot" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "HotTungstenIngot" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 3
})

quests.append({
	"Class": quest,
	"Name": "TitaniumChemReactor" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TitaniumChemReactor" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 4
})

quests.append({
	"Class": quest,
	"Name": "TungstenCarbideIngot" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TungstenCarbideIngot" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 5
})

quests.append({
	"Class": quest,
	"Name": "TungstenCarbideDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TungstenCarbideDust" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 6.5
})

quests.append({
	"Class": quest,
	"Name": "CobaltOxideDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "CobaltOxideDust" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 6.55
})

quests.append({
	"Class": quest,
	"Name": "TitaniumChemReactor2" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TitaniumChemReactor" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 6.555
})

quests.append({
	"Class": quest,
	"Name": "CobaltDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "CobaltDust" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 6.6
})

quests.append({
	"Class": quest,
	"Name": "TitaniumMixer" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TitaniumMixer" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 6.9
})

quests.append({
	"Class": quest,
	"Name": "HardMetalDust" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "HardMetalDust" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 7
})

quests.append({
	"Class": quest,
	"Name": "TitaniumInductionFurnace" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TitaniumInductionFurnace" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 7.5
})

quests.append({
	"Class": quest,
	"Name": "HotHardMetalIngot" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "HotHardMetalIngot" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 8
})

quests.append({
	"Class": quest,
	"Name": "TitaniumFreezer" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "TitaniumFreezer" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 9
})

quests.append({
	"Class": quest,
	"Name": "HardMetalIngot" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "HardMetalIngot" + static_item,
	"Chapter": "RoadToHardMetal" + qchapter,
	"Sorter": 10
})

# Wood work

qchapters.append({
	"Name": "Woodwork" + qchapter,
	"Class": qchapter,
	"Key": "Woodwork",
	"Sorter": 998,
	"Reward": {
		"Items" : [
			{
				"Name": "WoodenPlanks" + static_item,
				"Count": 64
			}
		]
	},
	"Achievement": "Woodwork",
})

quests.append({
	"Class": quest,
	"Name": "Door" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "Door" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "Chair" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "Chair" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "Fence" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "Fence" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "Ladder" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "Ladder" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 3
})

quests.append({
	"Class": quest,
	"Name": "Rack" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "Rack" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 4
})

quests.append({
	"Class": quest,
	"Name": "Table" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "Table" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 5
})

quests.append({
	"Class": quest,
	"Name": "Torch" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "Torch" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 6
})

quests.append({
	"Class": quest,
	"Name": "WoodenChest" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "WoodenChest" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 7
})

quests.append({
	"Class": quest,
	"Name": "WoodenStairs" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "WoodenStairs" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 7
})

quests.append({
	"Class": quest,
	"Name": "Window" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "Window" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 8
})

quests.append({
	"Class": quest,
	"Name": "WoodenPlanks" + quest,
	"QuestTextKeys": [
		"Collect",
	],
	"Item": "WoodenPlanks" + static_item,
	"Chapter": "Woodwork" + qchapter,
	"Sorter": 9
})

# Decorative

qchapters.append({
	"Name": "Decorative" + qchapter,
	"Class": qchapter,
	"Key": "Decorative",
	"Sorter": 999,
	"Reward": {
		"Items" : [
			{
				"Name": "DarkStoneSurface" + static_item,
				"Count": 50
			},{
				"Name": "StoneSurface" + static_item,
				"Count": 50
			},{
				"Name": "RedStoneSurface" + static_item,
				"Count": 50
			}
		]
	}
})

quests.append({
	"Class": quest,
	"Name": "DarkBricks" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "DarkBricks" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 0
})

quests.append({
	"Class": quest,
	"Name": "Bricks" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "Bricks" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 1
})

quests.append({
	"Class": quest,
	"Name": "RedBricks" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "RedBricks" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 2
})

quests.append({
	"Class": quest,
	"Name": "RedStoneTiles" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "RedStoneTiles" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 3
})

quests.append({
	"Class": quest,
	"Name": "Terracotta" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "Terracotta" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 4
})

quests.append({
	"Class": quest,
	"Name": "TerracottaTiles" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "TerracottaTiles" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 5
})

quests.append({
	"Class": quest,
	"Name": "DarkStoneTiles" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "DarkStoneTiles" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 6
})

quests.append({
	"Class": quest,
	"Name": "Column" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "Column" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 7
})

quests.append({
	"Class": quest,
	"Name": "FluetedColumn" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "FluetedColumn" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 8
})

quests.append({
	"Class": quest,
	"Name": "Stairs" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "Stairs" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 9
})

quests.append({
	"Class": quest,
	"Name": "StoneTiles" + quest,
	"QuestTextKeys": [
		"Collect"
	],
	"Item": "StoneTiles" + static_item,
	"Chapter": "Decorative" + qchapter,
	"Sorter": 10
})

data = {
	"Objects": quests
}

write_file("Generated/Quests/quests.generated.json", data);

data = {
	"Objects": qchapters
}

write_file("Generated/Chapters/qchapters.generated.json", data);