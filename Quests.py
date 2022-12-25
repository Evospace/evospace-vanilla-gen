from Common import *

quests = []
qchapters = []

# RoadToSteel

qchapters.append(
    {
        "name": "RoadToSteel",
        "class": qchapter,
        "Key": "RoadToSteel",
        "Sorter": 4,
        "Reward": {"Items": [{"name": "SteelIngot", "Count": 5}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronOre",
        "QuestTextKeys": ["Collect", "IronOre"],
        "Item": "IronOre",
        "Chapter": "RoadToSteel",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronImpureOreGravel2",
        "QuestTextKeys": ["Collect"],
        "Item": "IronImpureOreGravel",
        "Chapter": "RoadToSteel",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronOreGravel2",
        "QuestTextKeys": ["Collect"],
        "Item": "IronOreGravel",
        "Chapter": "RoadToSteel",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronImpureOreDust2",
        "QuestTextKeys": ["Collect"],
        "Item": "IronImpureOreDust",
        "Chapter": "RoadToSteel",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CokeOven",
        "QuestTextKeys": ["Collect", "CokeOven"],
        "Item": "CopperCokeOven",
        "Chapter": "RoadToSteel",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "BlastFurnace",
        "QuestTextKeys": ["Collect", "BlastFurnace"],
        "Item": "CopperBlastFurnace",
        "Chapter": "RoadToSteel",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CoalPiece",
        "QuestTextKeys": ["Collect", "Achievement", "CoalPiece"],
        "Item": "CoalPiece",
        "Chapter": "RoadToSteel",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CokePiece",
        "QuestTextKeys": ["Collect", "CokePiece"],
        "Item": "CokePiece",
        "Chapter": "RoadToSteel",
        "Sorter": 3.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CoalDust",
        "QuestTextKeys": ["Collect", "CoalDust"],
        "Item": "CoalDust",
        "Chapter": "RoadToSteel",
        "Sorter": 4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CokeDust",
        "QuestTextKeys": ["Collect", "CokeDust"],
        "Item": "CokeDust",
        "Chapter": "RoadToSteel",
        "Sorter": 4.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelAge",
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
        "name": "Other",
        "class": qchapter,
        "Key": "Other",
        "Sorter": 1000,
        "Reward": {"Items": []},
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumAge",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "AluminiumIngot",
        "Achievement": "AluminiumAge",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumOre",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "TitaniumOre",
        "Achievement": "TitaniumOre",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumAge",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "TitaniumIngot",
        "Achievement": "TitaniumAge",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelAge",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "StainlessSteelIngot",
        "Achievement": "StainlessSteelAge",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronOreAchievement",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "IronOre",
        "Achievement": "IronOre",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumOreAchievement",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "AluminiumOre",
        "Achievement": "AluminiumOre",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "GoldOreAchievement",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "GoldOre",
        "Achievement": "GoldOre",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "UraniumOreAchievement",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "UraniumOre",
        "Achievement": "UraniumOre",
        "Chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "CoalOreAchievement",
        "QuestTextKeys": ["Collect", "Achievement"],
        "Item": "CoalPiece",
        "Achievement": "CoalOre",
        "Chapter": "Other",
    }
)

# FirstSteps

qchapters.append(
    {
        "name": "FirstSteps",
        "class": qchapter,
        "Key": "FirstSteps",
        "Sorter": 0,
        "Reward": {"Items": [{"name": "CopperMultitool", "Count": 1}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "Log",
        "QuestTextKeys": ["Collect"],
        "Item": "Log",
        "Achievement": "Log",
        "Chapter": "FirstSteps",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Furnace",
        "QuestTextKeys": ["Collect", "Furnace"],
        "Item": "StoneFurnace",
        "Chapter": "FirstSteps",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Dryer",
        "QuestTextKeys": ["Collect", "Dryer"],
        "Item": "StoneDryer",
        "Chapter": "FirstSteps",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Smelter",
        "QuestTextKeys": ["Collect", "Smelter"],
        "Item": "StoneSmelter",
        "Chapter": "FirstSteps",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Bed",
        "QuestTextKeys": ["Collect", "Bed"],
        "Item": "Bed",
        "Chapter": "FirstSteps",
        "Sorter": 2.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperOre",
        "QuestTextKeys": ["Collect", "Achievement", "CopperOre"],
        "Item": "CopperOre",
        "Achievement": "CopperOre",
        "Chapter": "FirstSteps",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperAge",
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
        "name": "Farming",
        "class": qchapter,
        "Key": "Farming",
        "Sorter": 1,
        "Reward": {"Items": [{"name": "CopperMultitool", "Count": 1}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "Organics",
        "QuestTextKeys": ["Collect", "Organics"],
        "Item": "OrganicsPiece",
        "Chapter": "Farming",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Farm",
        "QuestTextKeys": ["Collect", "BambooFarm"],
        "Item": "CopperFarm",
        "Chapter": "Farming",
        "Sorter": 1,
    }
)

# Steam

qchapters.append(
    {
        "name": "Steam",
        "class": qchapter,
        "Key": "Steam",
        "Sorter": 2,
        "Reward": {
            "Items": [
                {"name": "CopperVent", "Count": 1},
                {"name": "CopperPipe", "Count": 10},
            ]
        },
    }
)

quests.append(
    {
        "class": quest,
        "name": "Boiler",
        "QuestTextKeys": ["Collect", "Boiler"],
        "Item": "SteelBoiler",
        "Chapter": "Steam",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Pump",
        "QuestTextKeys": ["Collect", "Pump"],
        "Item": "SteelPump",
        "Chapter": "Steam",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Pipe",
        "QuestTextKeys": ["Collect", "Pipe"],
        "Item": "SteelPipe",
        "Chapter": "Steam",
        "Sorter": 2,
    }
)

# Refining

qchapters.append(
    {
        "name": "Refining",
        "class": qchapter,
        "Key": "Refining",
        "Sorter": 3,
        "Reward": {
            "Items": [
                {"name": "CopperFluidDump", "Count": 1},
                {"name": "CopperVent", "Count": 2},
            ]
        },
    }
)

quests.append(
    {
        "class": quest,
        "name": "AutomaticHammer",
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
        "class": quest,
        "name": "CopperPlate",
        "QuestTextKeys": ["Collect", "Plate"],
        "Item": "CopperPlate",
        "Chapter": "Refining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperImpureOreGravel",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "CopperImpureOreGravel",
        "Chapter": "Refining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Washer",
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
        "class": quest,
        "name": "CopperOreGravel",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "CopperOreGravel",
        "Chapter": "Refining",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Macerator",
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
        "class": quest,
        "name": "CopperImpureOreDust",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "CopperImpureOreDust",
        "Chapter": "Refining",
        "Sorter": 2.5,
    }
)

# Fast travel

qchapters.append(
    {
        "name": "FastTravel",
        "class": qchapter,
        "Key": "FastTravel",
        "Sorter": 3.1,
        "Reward": {"Items": [{"name": "CopperIngot", "Count": 20}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "Steampack",
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
        "class": quest,
        "name": "Jetpack",
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
        "class": quest,
        "name": "AdvancedJetpack",
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
        "class": quest,
        "name": "AntigravityUnit",
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
        "name": "Logistics",
        "class": qchapter,
        "Key": "Logistics",
        "Sorter": 4.1,
        "Reward": {"Items": [{"name": "SteelFilteringRobotArm", "Count": 3}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperRobotArm",
        "QuestTextKeys": ["Collect", "RobotArm"],
        "Item": "CopperRobotArm",
        "Chapter": "Logistics",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelRobotArm",
        "QuestTextKeys": ["Collect", "RobotArm"],
        "Item": "SteelRobotArm",
        "Chapter": "Logistics",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelFilteringRobotArm",
        "QuestTextKeys": ["Collect", "FilteringRobotArm"],
        "Item": "SteelFilteringRobotArm",
        "Chapter": "Logistics",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperConveyor",
        "QuestTextKeys": ["Collect", "Conveyor"],
        "Item": "CopperConveyor",
        "Chapter": "Logistics",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperConveyorSplitter",
        "QuestTextKeys": ["Collect", "ConveyorSplitter"],
        "Item": "CopperConveyorSplitter",
        "Chapter": "Logistics",
        "Sorter": 4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelConveyor",
        "QuestTextKeys": ["Collect", "Conveyor"],
        "Item": "SteelConveyor",
        "Chapter": "Logistics",
        "Sorter": 5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelConveyorSplitter",
        "QuestTextKeys": ["Collect", "ConveyorSplitter"],
        "Item": "SteelConveyorSplitter",
        "Chapter": "Logistics",
        "Sorter": 6,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperDeployer",
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
        "class": quest,
        "name": "SteelDeployer",
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
        "name": "FasterSteel",
        "class": qchapter,
        "Key": "FasterSteel",
        "Sorter": 4.15,
        "Reward": {"Items": [{"name": "SteelIngot", "Count": 10}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelCokeOven",
        "QuestTextKeys": ["Collect", "CokeOven"],
        "Item": "SteelCokeOven",
        "Chapter": "FasterSteel",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CokeDustFasterS",
        "QuestTextKeys": ["Collect"],
        "Item": "CokeDust",
        "Chapter": "FasterSteel",
        "Sorter": 1.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronDustFasterS",
        "QuestTextKeys": ["Collect"],
        "Item": "IronDust",
        "Chapter": "FasterSteel",
        "Sorter": 1.2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelAlloySmelter",
        "QuestTextKeys": ["Collect", "AlloySmelter"],
        "Item": "SteelAlloySmelter",
        "Chapter": "FasterSteel",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CastIronIngot",
        "QuestTextKeys": ["Collect", "CastIron"],
        "Item": "CastIronIngot",
        "Chapter": "FasterSteel",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CastIronDust",
        "QuestTextKeys": ["Collect", "CastIron"],
        "Item": "CastIronDust",
        "Chapter": "FasterSteel",
        "Sorter": 3.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelArcFurnace",
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
        "name": "FasterRefining",
        "class": qchapter,
        "Key": "FasterRefining",
        "Sorter": 4.2,
        "Reward": {
            "Items": [
                {"name": "SteelPipe", "Count": 5},
                {"name": "CopperVent", "Count": 2},
            ]
        },
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelAutomaticHammer",
        "QuestTextKeys": ["Collect", "HigherLevel"],
        "Item": "SteelAutomaticHammer",
        "Chapter": "FasterRefining",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelPlate",
        "QuestTextKeys": ["Collect", "Plate"],
        "Item": "SteelPlate",
        "Chapter": "FasterRefining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronImpureOreGravel",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "IronImpureOreGravel",
        "Chapter": "FasterRefining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelWasher",
        "QuestTextKeys": ["Collect", "HigherLevel"],
        "Item": "SteelOreWasher",
        "Chapter": "FasterRefining",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronOreGravel",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "IronOreGravel",
        "Chapter": "FasterRefining",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelMacerator",
        "QuestTextKeys": ["Collect", "HigherLevel"],
        "Item": "SteelMacerator",
        "Chapter": "FasterRefining",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronImpureOreDust",
        "QuestTextKeys": ["Collect", "Refined"],
        "Item": "IronImpureOreDust",
        "Chapter": "FasterRefining",
        "Sorter": 2.5,
    }
)

# RoadToAluminium

qchapters.append(
    {
        "name": "RoadToAluminium",
        "class": qchapter,
        "Key": "RoadToAluminium",
        "Sorter": 4.25,
        "Reward": {"Items": [{"name": "AluminiumIngot", "Count": 5}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumOre",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumOre",
        "Chapter": "RoadToAluminium",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumImpureOreGravel",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumImpureOreGravel",
        "Chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumOreGravel",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumOreGravel",
        "Chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumImpureOreDust",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumImpureOreDust",
        "Chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumOxideDust",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumOxideDust",
        "Chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelAlloySmelterAlum",
        "QuestTextKeys": ["Collect"],
        "Item": "SteelAlloySmelter",
        "Chapter": "RoadToAluminium",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumCarbideIngot",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumCarbideIngot",
        "Chapter": "RoadToAluminium",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumCarbideDust",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumCarbideDust",
        "Chapter": "RoadToAluminium",
        "Sorter": 2.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelArcFurnaceAlum",
        "QuestTextKeys": ["Collect"],
        "Item": "SteelArcFurnace",
        "Chapter": "RoadToAluminium",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumIngot",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumIngot",
        "Chapter": "RoadToAluminium",
        "Sorter": 4,
    }
)

# AdvancedLogistics

qchapters.append(
    {
        "name": "AdvancedLogistics",
        "class": qchapter,
        "Key": "AdvancedLogistics",
        "Sorter": 4.3,
        "Reward": {"Items": [{"name": "AluminiumPneumaticPipe", "Count": 15}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperBufferChest",
        "QuestTextKeys": ["Collect"],
        "Item": "CopperBufferChest",
        "Chapter": "AdvancedLogistics",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelBufferChest",
        "QuestTextKeys": ["Collect"],
        "Item": "SteelBufferChest",
        "Chapter": "AdvancedLogistics",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumBufferChest",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumBufferChest",
        "Chapter": "AdvancedLogistics",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumDeployer",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumDeployer",
        "Chapter": "AdvancedLogistics",
        "Sorter": 4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumRobotArm",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumRobotArm",
        "Chapter": "AdvancedLogistics",
        "Sorter": 5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumFilteringRobotArm",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumFilteringRobotArm",
        "Chapter": "AdvancedLogistics",
        "Sorter": 6,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumPneumaticPipe",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumPneumaticPipe",
        "Chapter": "AdvancedLogistics",
        "Sorter": 7,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumPneumaticInput",
        "QuestTextKeys": ["Collect"],
        "Item": "AluminiumPneumaticInput",
        "Chapter": "AdvancedLogistics",
        "Sorter": 8,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumConveyor",
        "QuestTextKeys": ["Collect", "Conveyor"],
        "Item": "AluminiumConveyor",
        "Chapter": "AdvancedLogistics",
        "Sorter": 9,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumConveyorSplitter",
        "QuestTextKeys": ["Collect", "ConveyorSplitter"],
        "Item": "AluminiumConveyorSplitter",
        "Chapter": "AdvancedLogistics",
        "Sorter": 10,
    }
)

# RoadToSS

qchapters.append(
    {
        "name": "RoadToSS",
        "class": qchapter,
        "Key": "RoadToSS",
        "Sorter": 5,
        "Reward": {"Items": [{"name": "StainlessSteelIngot", "Count": 5}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "ChromeOxideDust",
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
        "class": quest,
        "name": "AluminothermicChromeDust",
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
        "class": quest,
        "name": "AluminiumSolidFurnace",
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
        "class": quest,
        "name": "ChromeDust",
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
        "class": quest,
        "name": "IronDustSS",
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
        "class": quest,
        "name": "NickelDust",
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
        "class": quest,
        "name": "AluminiumMixer",
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
        "class": quest,
        "name": "StainlessSteelDust",
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
        "class": quest,
        "name": "AluminiumArcFurnace",
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
        "class": quest,
        "name": "StainlessSteelIngot",
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
        "name": "HeatTransferring",
        "class": qchapter,
        "Key": "HeatTransferring",
        "Sorter": 5.5,
        "Reward": {"Items": [{"name": "NakCoolantDust", "Count": 10}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelHeatExchanger",
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
        "class": quest,
        "name": "StainlessSteelInverseHeatExchanger",
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
        "class": quest,
        "name": "StainlessSteelRadiator",
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
        "class": quest,
        "name": "NakCoolantDust",
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
        "name": "RoadToTitanium",
        "class": qchapter,
        "Key": "RoadToTitanium",
        "Sorter": 6,
        "Reward": {"Items": [{"name": "TitaniumIngot", "Count": 5}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "CokeDustTit",
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
        "class": quest,
        "name": "TitaniumOxideDust",
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
        "class": quest,
        "name": "StainlessSteelAlloySmelter",
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
        "class": quest,
        "name": "PreparedTitaniumOxideDust",
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
        "class": quest,
        "name": "ManganeseOxideDust",
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
        "class": quest,
        "name": "AluminothermicManganeseDust",
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
        "class": quest,
        "name": "StainlessSteelSolidFurnace",
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
        "class": quest,
        "name": "ManganeseDust",
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
        "class": quest,
        "name": "SaltDust",
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
        "class": quest,
        "name": "StainlessSteelChemReactor",
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
        "class": quest,
        "name": "TitaniumSponge",
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
        "class": quest,
        "name": "StainlessSteelInductionFurnace",
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
        "class": quest,
        "name": "TitaniumIngot",
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
        "name": "RoadToHardMetal",
        "class": qchapter,
        "Key": "RoadToHardMetal",
        "Sorter": 7,
        "Reward": {"Items": [{"name": "HardMetalIngot", "Count": 5}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "TungstenOxideDust",
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
        "class": quest,
        "name": "TitaniumInductionFurnace2",
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
        "class": quest,
        "name": "HotTungstenIngot",
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
        "class": quest,
        "name": "TitaniumChemReactor",
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
        "class": quest,
        "name": "TungstenCarbideIngot",
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
        "class": quest,
        "name": "TungstenCarbideDust",
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
        "class": quest,
        "name": "CobaltOxideDust",
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
        "class": quest,
        "name": "TitaniumChemReactor2",
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
        "class": quest,
        "name": "CobaltDust",
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
        "class": quest,
        "name": "TitaniumMixer",
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
        "class": quest,
        "name": "HardMetalDust",
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
        "class": quest,
        "name": "TitaniumInductionFurnace",
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
        "class": quest,
        "name": "HotHardMetalIngot",
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
        "class": quest,
        "name": "TitaniumFreezer",
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
        "class": quest,
        "name": "HardMetalIngot",
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
        "name": "Woodwork",
        "class": qchapter,
        "Key": "Woodwork",
        "Sorter": 998,
        "Reward": {"Items": [{"name": "WoodenPlanks", "Count": 64}]},
        "Achievement": "Woodwork",
    }
)

quests.append(
    {
        "class": quest,
        "name": "Door",
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
        "class": quest,
        "name": "Chair",
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
        "class": quest,
        "name": "Fence",
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
        "class": quest,
        "name": "Ladder",
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
        "class": quest,
        "name": "Rack",
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
        "class": quest,
        "name": "Table",
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
        "class": quest,
        "name": "Torch",
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
        "class": quest,
        "name": "WoodenChest",
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
        "class": quest,
        "name": "WoodenStairs",
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
        "class": quest,
        "name": "Window",
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
        "class": quest,
        "name": "WoodenPlanks",
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
        "name": "Decorative",
        "class": qchapter,
        "Key": "Decorative",
        "Sorter": 999,
        "Reward": {
            "Items": [
                {"name": "DarkStoneSurface", "Count": 50},
                {"name": "StoneSurface", "Count": 50},
                {"name": "RedStoneSurface", "Count": 50},
            ]
        },
    }
)

quests.append(
    {
        "class": quest,
        "name": "DarkBricks",
        "QuestTextKeys": ["Collect"],
        "Item": "DarkBricks",
        "Chapter": "Decorative",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Bricks",
        "QuestTextKeys": ["Collect"],
        "Item": "Bricks",
        "Chapter": "Decorative",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "RedBricks",
        "QuestTextKeys": ["Collect"],
        "Item": "RedBricks",
        "Chapter": "Decorative",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "RedStoneTiles",
        "QuestTextKeys": ["Collect"],
        "Item": "RedStoneTiles",
        "Chapter": "Decorative",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Terracotta",
        "QuestTextKeys": ["Collect"],
        "Item": "Terracotta",
        "Chapter": "Decorative",
        "Sorter": 4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TerracottaTiles",
        "QuestTextKeys": ["Collect"],
        "Item": "TerracottaTiles",
        "Chapter": "Decorative",
        "Sorter": 5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "DarkStoneTiles",
        "QuestTextKeys": ["Collect"],
        "Item": "DarkStoneTiles",
        "Chapter": "Decorative",
        "Sorter": 6,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Column",
        "QuestTextKeys": ["Collect"],
        "Item": "Column",
        "Chapter": "Decorative",
        "Sorter": 7,
    }
)

quests.append(
    {
        "class": quest,
        "name": "FluetedColumn",
        "QuestTextKeys": ["Collect"],
        "Item": "FluetedColumn",
        "Chapter": "Decorative",
        "Sorter": 8,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Stairs",
        "QuestTextKeys": ["Collect"],
        "Item": "Stairs",
        "Chapter": "Decorative",
        "Sorter": 9,
    }
)

quests.append(
    {
        "class": quest,
        "name": "StoneTiles",
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
