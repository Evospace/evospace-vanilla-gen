from Common import *

quests = []
qchapters = []

# RoadToSteel

qchapters.append(
    {
        "Name": "RoadToSteel",
        "Class": qchapter,
        "Key": "RoadToSteel",
        "Sorter": 4,
        "Reward": {"Items": [{"Name": "SteelIngot", "Count": 5}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "IronOre",
        "QuestTextKeys": ["Collect", "IronOre"],
        "Item": "IronOre",
        "Chapter": "RoadToSteel",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "IronImpureOreGravel2",
        "QuestTextKeys": ["Collect"],
        "Item": "IronImpureOreGravel",
        "Chapter": "RoadToSteel",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "IronOreGravel2",
        "QuestTextKeys": ["Collect"],
        "Item": "IronOreGravel",
        "Chapter": "RoadToSteel",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "IronImpureOreDust2",
        "QuestTextKeys": ["Collect"],
        "Item": "IronImpureOreDust",
        "Chapter": "RoadToSteel",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CokeOven",
        "QuestTextKeys": ["Collect", "CokeOven"],
        "Item": "CopperCokeOven",
        "Chapter": "RoadToSteel",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "BlastFurnace",
        "QuestTextKeys": ["Collect", "BlastFurnace"],
        "Item": "CopperBlastFurnace",
        "Chapter": "RoadToSteel",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CoalPiece",
        "QuestTextKeys": ["Collect", "Achievement", "CoalPiece"],
        "Item": "CoalPiece",
        "Chapter": "RoadToSteel",
        "Sorter": 3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CokePiece",
        "QuestTextKeys": ["Collect", "CokePiece"],
        "Item": "CokePiece",
        "Chapter": "RoadToSteel",
        "Sorter": 3.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CoalDust",
        "QuestTextKeys": ["Collect", "CoalDust"],
        "Item": "CoalDust",
        "Chapter": "RoadToSteel",
        "Sorter": 4,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CokeDust",
        "QuestTextKeys": ["Collect", "CokeDust"],
        "Item": "CokeDust",
        "Chapter": "RoadToSteel",
        "Sorter": 4.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelAge",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "SteelIngot",
        "Achievement": "SteelAge",
        "Chapter": "RoadToSteel",
        "Sorter": 5,
    }
)

# Other

qchapters.append(
    {
        "Name": "Other",
        "Class": qchapter,
        "Key": "Other",
        "Sorter": 1000,
        "Reward": {"Items": []},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumAge",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "AluminiumIngot",
        "Achievement": "AluminiumAge",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumOre",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "TitaniumOre",
        "Achievement": "TitaniumOre",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumAge",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "TitaniumIngot",
        "Achievement": "TitaniumAge",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StainlessSteelAge",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "StainlessSteelIngot",
        "Achievement": "StainlessSteelAge",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "IronOreAchievement",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "IronOre",
        "Achievement": "IronOre",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumOreAchievement",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "AluminiumOre",
        "Achievement": "AluminiumOre",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "GoldOreAchievement",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "GoldOre",
        "Achievement": "GoldOre",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "UraniumOreAchievement",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "UraniumOre",
        "Achievement": "UraniumOre",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CoalOreAchievement",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "CoalPiece",
        "Achievement": "CoalOre",
        "Chapter": "Other",
    }
)

# FirstSteps

qchapters.append(
    {
        "Name": "FirstSteps",
        "Class": qchapter,
        "Key": "FirstSteps",
        "Sorter": 0,
        "Reward": {"Items": [{"Name": "CopperMultitool", "Count": 1}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Log",
        "QuestTextKeys": ["Collect"],
        "Item": "Log",
        "Achievement": "Log",
        "Chapter": "FirstSteps",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Furnace",
        "QuestTextKeys": ["Collect", "Furnace"],
        "Item": "StoneFurnace",
        "Chapter": "FirstSteps",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Dryer",
        "QuestTextKeys": ["Collect", "Dryer"],
        "Item": "StoneDryer",
        "Chapter": "FirstSteps",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Smelter",
        "QuestTextKeys": ["Collect", "Smelter"],
        "Item": "StoneSmelter",
        "Chapter": "FirstSteps",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Bed",
        "QuestTextKeys": ["Collect", "Bed"],
        "Item": "Bed",
        "Chapter": "FirstSteps",
        "Sorter": 2.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperOre",
        "QuestTextKeys": ["Collect", "Achievement", "CopperOre"],
        "Item": "CopperOre",
        "Achievement": "CopperOre",
        "Chapter": "FirstSteps",
        "Sorter": 3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperAge",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "CopperIngot",
        "Achievement": "CopperAge",
        "Chapter": "FirstSteps",
        "Sorter": 4,
    }
)

# Farming

qchapters.append(
    {
        "Name": "Farming",
        "Class": qchapter,
        "Key": "Farming",
        "Sorter": 1,
        "Reward": {"Items": [{"Name": "CopperMultitool", "Count": 1}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Organics",
        "QuestTextKeys": ["Collect", "Organics"],
        "Item": "OrganicsPiece",
        "Chapter": "Farming",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Farm",
        "QuestTextKeys": ["Collect", "BambooFarm"],
        "Item": "CopperFarm",
        "Chapter": "Farming",
        "Sorter": 1,
    }
)

# Steam

qchapters.append(
    {
        "Name": "Steam",
        "Class": qchapter,
        "Key": "Steam",
        "Sorter": 2,
        "Reward": {
            "Items": [
                {"Name": "CopperVent", "Count": 1},
                {"Name": "CopperPipe", "Count": 10},
            ]
        },
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Boiler",
        "QuestTextKeys": ["Collect", "Boiler"],
        "Item": "SteelBoiler",
        "Chapter": "Steam",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Pump",
        "QuestTextKeys": ["Collect", "Pump"],
        "Item": "SteelPump",
        "Chapter": "Steam",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Pipe",
        "QuestTextKeys": ["Collect", "Pipe"],
        "Item": "SteelPipe",
        "Chapter": "Steam",
        "Sorter": 2,
    }
)

# Refining

qchapters.append(
    {
        "Name": "Refining",
        "Class": qchapter,
        "Key": "Refining",
        "Sorter": 3,
        "Reward": {
            "Items": [
                {"Name": "CopperFluidDump", "Count": 1},
                {"Name": "CopperVent", "Count": 2},
            ]
        },
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AutomaticHammer",
        "QuestTextKeys": [
            "Collect",
            "AutomaticHammer",
            "RefiningMachine",
        ],
        "Item": "CopperAutomaticHammer",
        "Chapter": "Refining",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperPlate",
        "QuestTextKeys": ["Collect", "Plate"],
        "Item": "CopperPlate",
        "Chapter": "Refining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperImpureOreGravel",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "CopperImpureOreGravel",
        "Chapter": "Refining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Washer",
        "QuestTextKeys": [
            "Collect",
            "OreWasher",
            "RefiningMachine",
        ],
        "Item": "SteelOreWasher",
        "Chapter": "Refining",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperOreGravel",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "CopperOreGravel",
        "Chapter": "Refining",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Macerator",
        "QuestTextKeys": [
            "Collect",
            "Macerator",
            "RefiningMachine",
        ],
        "Item": "CopperMacerator",
        "Chapter": "Refining",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperImpureOreDust",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "CopperImpureOreDust",
        "Chapter": "Refining",
        "Sorter": 2.5,
    }
)

# Fast travel

qchapters.append(
    {
        "Name": "FastTravel",
        "Class": qchapter,
        "Key": "FastTravel",
        "Sorter": 3.1,
        "Reward": {"Items": [{"Name": "CopperIngot", "Count": 20}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Steampack",
        "QuestTextKeys": [
            "Collect",
            "Jumppack",
        ],
        "Item": "Steampack",
        "Chapter": "FastTravel",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Jetpack",
        "QuestTextKeys": [
            "Collect",
            "Jumppack",
        ],
        "Item": "Jetpack",
        "Chapter": "FastTravel",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AdvancedJetpack",
        "QuestTextKeys": [
            "Collect",
            "Jumppack",
        ],
        "Item": "AdvancedJetpack",
        "Chapter": "FastTravel",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AntigravityUnit",
        "QuestTextKeys": [
            "Collect",
            "Jumppack",
        ],
        "Item": "AntigravityUnit",
        "Chapter": "FastTravel",
        "Sorter": 3,
    }
)

# Logistics

qchapters.append(
    {
        "Name": "Logistics",
        "Class": qchapter,
        "Key": "Logistics",
        "Sorter": 4.1,
        "Reward": {"Items": [{"Name": "SteelFilteringRobotArm", "Count": 3}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperRobotArm",
        "QuestTextKeys": ["Collect", "RobotArm"],
        "Item": "CopperRobotArm",
        "Chapter": "Logistics",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelRobotArm",
        "QuestTextKeys": ["Collect", "RobotArm"],
        "Item": "SteelRobotArm",
        "Chapter": "Logistics",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelFilteringRobotArm",
        "QuestTextKeys": ["Collect", "FilteringRobotArm"],
        "Item": "SteelFilteringRobotArm",
        "Chapter": "Logistics",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperConveyor",
        "QuestTextKeys": ["Collect", "Conveyor"],
        "Item": "CopperConveyor",
        "Chapter": "Logistics",
        "Sorter": 3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperConveyorSplitter",
        "QuestTextKeys": ["Collect", "ConveyorSplitter"],
        "Item": "CopperConveyorSplitter",
        "Chapter": "Logistics",
        "Sorter": 4,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelConveyor",
        "QuestTextKeys": ["Collect", "Conveyor"],
        "Item": "SteelConveyor",
        "Chapter": "Logistics",
        "Sorter": 5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelConveyorSplitter",
        "QuestTextKeys": ["Collect", "ConveyorSplitter"],
        "Item": "SteelConveyorSplitter",
        "Chapter": "Logistics",
        "Sorter": 6,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperDeployer",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "CopperDeployer",
        "Chapter": "Logistics",
        "Sorter": 7,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelDeployer",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "SteelDeployer",
        "Chapter": "Logistics",
        "Sorter": 8,
    }
)

# FasterSteel

qchapters.append(
    {
        "Name": "FasterSteel",
        "Class": qchapter,
        "Key": "FasterSteel",
        "Sorter": 4.15,
        "Reward": {"Items": [{"Name": "SteelIngot", "Count": 10}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelCokeOven",
        "QuestTextKeys": ["Collect", "CokeOven"],
        "Item": "SteelCokeOven",
        "Chapter": "FasterSteel",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CokeDustFasterS",
        "QuestTextKeys": ["Collect"],
        "Item": "CokeDust",
        "Chapter": "FasterSteel",
        "Sorter": 1.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "IronDustFasterS",
        "QuestTextKeys": ["Collect"],
        "Item": "IronDust",
        "Chapter": "FasterSteel",
        "Sorter": 1.2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelAlloySmelter",
        "QuestTextKeys": ["Collect", "AlloySmelter"],
        "Item": "SteelAlloySmelter",
        "Chapter": "FasterSteel",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CastIronIngot",
        "QuestTextKeys": ["Collect", "CastIron"],
        "Item": "CastIronIngot",
        "Chapter": "FasterSteel",
        "Sorter": 3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CastIronDust",
        "QuestTextKeys": ["Collect", "CastIron"],
        "Item": "CastIronDust",
        "Chapter": "FasterSteel",
        "Sorter": 3.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelArcFurnace",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "SteelArcFurnace",
        "Chapter": "FasterSteel",
        "Sorter": 4,
    }
)

# Faster Refining

qchapters.append(
    {
        "Name": "FasterRefining",
        "Class": qchapter,
        "Key": "FasterRefining",
        "Sorter": 4.2,
        "Reward": {
            "Items": [
                {"Name": "SteelPipe", "Count": 5},
                {"Name": "CopperVent", "Count": 2},
            ]
        },
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelAutomaticHammer",
        "QuestTextKeys": ["Collect", "HigherLevel"],
        "Item": "SteelAutomaticHammer",
        "Chapter": "FasterRefining",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelPlate",
        "QuestTextKeys": ["Collect", "Plate"],
        "Item": "SteelPlate",
        "Chapter": "FasterRefining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "IronImpureOreGravel",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "IronImpureOreGravel",
        "Chapter": "FasterRefining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelWasher",
        "QuestTextKeys": ["Collect", "HigherLevel"],
        "Item": "SteelOreWasher",
        "Chapter": "FasterRefining",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "IronOreGravel",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "IronOreGravel",
        "Chapter": "FasterRefining",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelMacerator",
        "QuestTextKeys": ["Collect", "HigherLevel"],
        "Item": "SteelMacerator",
        "Chapter": "FasterRefining",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "IronImpureOreDust",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "IronImpureOreDust",
        "Chapter": "FasterRefining",
        "Sorter": 2.5,
    }
)

# RoadToAluminium

qchapters.append(
    {
        "Name": "RoadToAluminium",
        "Class": qchapter,
        "Key": "RoadToAluminium",
        "Sorter": 4.25,
        "Reward": {"Items": [{"Name": "AluminiumIngot", "Count": 5}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumOre",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumOre",
        "Chapter": "RoadToAluminium",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumImpureOreGravel",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumImpureOreGravel",
        "Chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumOreGravel",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumOreGravel",
        "Chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumImpureOreDust",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumImpureOreDust",
        "Chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumOxideDust",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumOxideDust",
        "Chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelAlloySmelterAlum",
        "QuestTextKeys": ["Collect"],
        "Item": "SteelAlloySmelter",
        "Chapter": "RoadToAluminium",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumCarbideIngot",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumCarbideIngot",
        "Chapter": "RoadToAluminium",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumCarbideDust",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumCarbideDust",
        "Chapter": "RoadToAluminium",
        "Sorter": 2.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelArcFurnaceAlum",
        "QuestTextKeys": ["Collect"],
        "Item": "SteelArcFurnace",
        "Chapter": "RoadToAluminium",
        "Sorter": 3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumIngot",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumIngot",
        "Chapter": "RoadToAluminium",
        "Sorter": 4,
    }
)

# AdvancedLogistics

qchapters.append(
    {
        "Name": "AdvancedLogistics",
        "Class": qchapter,
        "Key": "AdvancedLogistics",
        "Sorter": 4.3,
        "Reward": {"Items": [{"Name": "AluminiumPneumaticPipe", "Count": 15}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CopperBufferChest",
        "QuestTextKeys": ["Collect"],
        "Item": "CopperBufferChest",
        "Chapter": "AdvancedLogistics",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SteelBufferChest",
        "QuestTextKeys": ["Collect"],
        "Item": "SteelBufferChest",
        "Chapter": "AdvancedLogistics",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumBufferChest",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumBufferChest",
        "Chapter": "AdvancedLogistics",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumDeployer",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumDeployer",
        "Chapter": "AdvancedLogistics",
        "Sorter": 4,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumRobotArm",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumRobotArm",
        "Chapter": "AdvancedLogistics",
        "Sorter": 5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumFilteringRobotArm",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumFilteringRobotArm",
        "Chapter": "AdvancedLogistics",
        "Sorter": 6,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumPneumaticPipe",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumPneumaticPipe",
        "Chapter": "AdvancedLogistics",
        "Sorter": 7,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumPneumaticInput",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumPneumaticInput",
        "Chapter": "AdvancedLogistics",
        "Sorter": 8,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumConveyor",
        "QuestTextKeys": ["Collect", "Conveyor"],
        "Item": "AluminiumConveyor",
        "Chapter": "AdvancedLogistics",
        "Sorter": 9,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumConveyorSplitter",
        "QuestTextKeys": ["Collect", "ConveyorSplitter"],
        "Item": "AluminiumConveyorSplitter",
        "Chapter": "AdvancedLogistics",
        "Sorter": 10,
    }
)

# RoadToSS

qchapters.append(
    {
        "Name": "RoadToSS",
        "Class": qchapter,
        "Key": "RoadToSS",
        "Sorter": 5,
        "Reward": {"Items": [{"Name": "StainlessSteelIngot", "Count": 5}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "ChromeOxideDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "ChromeOxideDust",
        "Chapter": "RoadToSS",
        "Sorter": 9.6,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminothermicChromeDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "AluminothermicChromeDust",
        "Chapter": "RoadToSS",
        "Sorter": 9.7,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumSolidFurnace",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "AluminiumSolidFurnace",
        "Chapter": "RoadToSS",
        "Sorter": 9.8,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "ChromeDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "ChromeDust",
        "Chapter": "RoadToSS",
        "Sorter": 9.85,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "IronDustSS",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "IronDust",
        "Chapter": "RoadToSS",
        "Sorter": 9.9,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "NickelDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "NickelDust",
        "Chapter": "RoadToSS",
        "Sorter": 9.9,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumMixer",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "AluminiumMixer",
        "Chapter": "RoadToSS",
        "Sorter": 9.95,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StainlessSteelDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "StainlessSteelDust",
        "Chapter": "RoadToSS",
        "Sorter": 10,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminiumArcFurnace",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "AluminiumArcFurnace",
        "Chapter": "RoadToSS",
        "Sorter": 11,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StainlessSteelIngot",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "StainlessSteelIngot",
        "Chapter": "RoadToSS",
        "Sorter": 12,
    }
)

# HeatTransferring

qchapters.append(
    {
        "Name": "HeatTransferring",
        "Class": qchapter,
        "Key": "HeatTransferring",
        "Sorter": 5.5,
        "Reward": {"Items": [{"Name": "NakCoolantDust", "Count": 10}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StainlessSteelHeatExchanger",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "StainlessSteelHeatExchanger",
        "Chapter": "HeatTransferring",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StainlessSteelInverseHeatExchanger",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "StainlessSteelInverseHeatExchanger",
        "Chapter": "HeatTransferring",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StainlessSteelRadiator",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "StainlessSteelRadiator",
        "Chapter": "HeatTransferring",
        "Sorter": 3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "NakCoolantDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "NakCoolantDust",
        "Chapter": "HeatTransferring",
        "Sorter": 9.45,
    }
)

# RoadToTitanium

qchapters.append(
    {
        "Name": "RoadToTitanium",
        "Class": qchapter,
        "Key": "RoadToTitanium",
        "Sorter": 6,
        "Reward": {"Items": [{"Name": "TitaniumIngot", "Count": 5}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CokeDustTit",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "CokeDust",
        "Chapter": "RoadToTitanium",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumOxideDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TitaniumOxideDust",
        "Chapter": "RoadToTitanium",
        "Sorter": 1.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StainlessSteelAlloySmelter",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "StainlessSteelAlloySmelter",
        "Chapter": "RoadToTitanium",
        "Sorter": 1.2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "PreparedTitaniumOxideDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "PreparedTitaniumOxideDust",
        "Chapter": "RoadToTitanium",
        "Sorter": 1.3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "ManganeseOxideDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "ManganeseOxideDust",
        "Chapter": "RoadToTitanium",
        "Sorter": 3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "AluminothermicManganeseDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "AluminothermicManganeseDust",
        "Chapter": "RoadToTitanium",
        "Sorter": 3.1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StainlessSteelSolidFurnace",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "StainlessSteelSolidFurnace",
        "Chapter": "RoadToTitanium",
        "Sorter": 3.2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "ManganeseDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "ManganeseDust",
        "Chapter": "RoadToTitanium",
        "Sorter": 3.3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "SaltDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "SaltDust",
        "Chapter": "RoadToTitanium",
        "Sorter": 7,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StainlessSteelChemReactor",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "StainlessSteelChemReactor",
        "Chapter": "RoadToTitanium",
        "Sorter": 8,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumSponge",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TitaniumSponge",
        "Chapter": "RoadToTitanium",
        "Sorter": 9.4,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StainlessSteelInductionFurnace",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "StainlessSteelInductionFurnace",
        "Chapter": "RoadToTitanium",
        "Sorter": 9.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumIngot",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TitaniumIngot",
        "Chapter": "RoadToTitanium",
        "Sorter": 9.6,
    }
)

# RoadToHardMetal

qchapters.append(
    {
        "Name": "RoadToHardMetal",
        "Class": qchapter,
        "Key": "RoadToHardMetal",
        "Sorter": 7,
        "Reward": {"Items": [{"Name": "HardMetalIngot", "Count": 5}]},
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TungstenOxideDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TungstenOxideDust",
        "Chapter": "RoadToHardMetal",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumInductionFurnace2",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TitaniumInductionFurnace",
        "Chapter": "RoadToHardMetal",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "HotTungstenIngot",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "HotTungstenIngot",
        "Chapter": "RoadToHardMetal",
        "Sorter": 3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumChemReactor",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TitaniumChemReactor",
        "Chapter": "RoadToHardMetal",
        "Sorter": 4,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TungstenCarbideIngot",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TungstenCarbideIngot",
        "Chapter": "RoadToHardMetal",
        "Sorter": 5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TungstenCarbideDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TungstenCarbideDust",
        "Chapter": "RoadToHardMetal",
        "Sorter": 6.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CobaltOxideDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "CobaltOxideDust",
        "Chapter": "RoadToHardMetal",
        "Sorter": 6.55,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumChemReactor2",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TitaniumChemReactor",
        "Chapter": "RoadToHardMetal",
        "Sorter": 6.555,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "CobaltDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "CobaltDust",
        "Chapter": "RoadToHardMetal",
        "Sorter": 6.6,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumMixer",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TitaniumMixer",
        "Chapter": "RoadToHardMetal",
        "Sorter": 6.9,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "HardMetalDust",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "HardMetalDust",
        "Chapter": "RoadToHardMetal",
        "Sorter": 7,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumInductionFurnace",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TitaniumInductionFurnace",
        "Chapter": "RoadToHardMetal",
        "Sorter": 7.5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "HotHardMetalIngot",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "HotHardMetalIngot",
        "Chapter": "RoadToHardMetal",
        "Sorter": 8,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TitaniumFreezer",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "TitaniumFreezer",
        "Chapter": "RoadToHardMetal",
        "Sorter": 9,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "HardMetalIngot",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "HardMetalIngot",
        "Chapter": "RoadToHardMetal",
        "Sorter": 10,
    }
)

# Wood work

qchapters.append(
    {
        "Name": "Woodwork",
        "Class": qchapter,
        "Key": "Woodwork",
        "Sorter": 998,
        "Reward": {"Items": [{"Name": "WoodenPlanks", "Count": 64}]},
        "Achievement": "Woodwork",
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Door",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "Door",
        "Chapter": "Woodwork",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Chair",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "Chair",
        "Chapter": "Woodwork",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Fence",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "Fence",
        "Chapter": "Woodwork",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Ladder",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "Ladder",
        "Chapter": "Woodwork",
        "Sorter": 3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Rack",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "Rack",
        "Chapter": "Woodwork",
        "Sorter": 4,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Table",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "Table",
        "Chapter": "Woodwork",
        "Sorter": 5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Torch",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "Torch",
        "Chapter": "Woodwork",
        "Sorter": 6,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "WoodenChest",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "WoodenChest",
        "Chapter": "Woodwork",
        "Sorter": 7,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "WoodenStairs",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "WoodenStairs",
        "Chapter": "Woodwork",
        "Sorter": 7,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Window",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "Window",
        "Chapter": "Woodwork",
        "Sorter": 8,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "WoodenPlanks",
        "QuestTextKeys": [
            "Collect",
        ],
        "Item": "WoodenPlanks",
        "Chapter": "Woodwork",
        "Sorter": 9,
    }
)

# Decorative

qchapters.append(
    {
        "Name": "Decorative",
        "Class": qchapter,
        "Key": "Decorative",
        "Sorter": 999,
        "Reward": {
            "Items": [
                {"Name": "DarkStoneSurface", "Count": 50},
                {"Name": "StoneSurface", "Count": 50},
                {"Name": "RedStoneSurface", "Count": 50},
            ]
        },
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "DarkBricks",
        "QuestTextKeys": ["Collect"],
        "Item": "DarkBricks",
        "Chapter": "Decorative",
        "Sorter": 0,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Bricks",
        "QuestTextKeys": ["Collect"],
        "Item": "Bricks",
        "Chapter": "Decorative",
        "Sorter": 1,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "RedBricks",
        "QuestTextKeys": ["Collect"],
        "Item": "RedBricks",
        "Chapter": "Decorative",
        "Sorter": 2,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "RedStoneTiles",
        "QuestTextKeys": ["Collect"],
        "Item": "RedStoneTiles",
        "Chapter": "Decorative",
        "Sorter": 3,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Terracotta",
        "QuestTextKeys": ["Collect"],
        "Item": "Terracotta",
        "Chapter": "Decorative",
        "Sorter": 4,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "TerracottaTiles",
        "QuestTextKeys": ["Collect"],
        "Item": "TerracottaTiles",
        "Chapter": "Decorative",
        "Sorter": 5,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "DarkStoneTiles",
        "QuestTextKeys": ["Collect"],
        "Item": "DarkStoneTiles",
        "Chapter": "Decorative",
        "Sorter": 6,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Column",
        "QuestTextKeys": ["Collect"],
        "Item": "Column",
        "Chapter": "Decorative",
        "Sorter": 7,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "FluetedColumn",
        "QuestTextKeys": ["Collect"],
        "Item": "FluetedColumn",
        "Chapter": "Decorative",
        "Sorter": 8,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "Stairs",
        "QuestTextKeys": ["Collect"],
        "Item": "Stairs",
        "Chapter": "Decorative",
        "Sorter": 9,
    }
)

quests.append(
    {
        "Class": quest,
        "Name": "StoneTiles",
        "QuestTextKeys": ["Collect"],
        "Item": "StoneTiles",
        "Chapter": "Decorative",
        "Sorter": 10,
    }
)

data = {"Objects": quests}

write_file("Generated/Quests/quests.generated.json", data)

data = {"Objects": qchapters}

write_file("Generated/Chapters/qchapters.generated.json", data)
