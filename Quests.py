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
        "Reward": {"items": [{"name": "SteelIngot", "count": 5}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronOre",
        "QuestTextKeys": ["collect", "IronOre"],
        "Item": "IronOre",
        "chapter": "RoadToSteel",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronImpureOreGravel2",
        "QuestTextKeys": ["collect"],
        "Item": "IronImpureOreGravel",
        "chapter": "RoadToSteel",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronOreGravel2",
        "QuestTextKeys": ["collect"],
        "Item": "IronOreGravel",
        "chapter": "RoadToSteel",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronImpureOreDust2",
        "QuestTextKeys": ["collect"],
        "Item": "IronImpureOreDust",
        "chapter": "RoadToSteel",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CokeOven",
        "QuestTextKeys": ["collect", "CokeOven"],
        "Item": "CopperCokeOven",
        "chapter": "RoadToSteel",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "BlastFurnace",
        "QuestTextKeys": ["collect", "BlastFurnace"],
        "Item": "CopperBlastFurnace",
        "chapter": "RoadToSteel",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CoalPiece",
        "QuestTextKeys": ["collect", "achievement", "CoalPiece"],
        "Item": "CoalPiece",
        "chapter": "RoadToSteel",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CokePiece",
        "QuestTextKeys": ["collect", "CokePiece"],
        "Item": "CokePiece",
        "chapter": "RoadToSteel",
        "Sorter": 3.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CoalDust",
        "QuestTextKeys": ["collect", "CoalDust"],
        "Item": "CoalDust",
        "chapter": "RoadToSteel",
        "Sorter": 4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CokeDust",
        "QuestTextKeys": ["collect", "CokeDust"],
        "Item": "CokeDust",
        "chapter": "RoadToSteel",
        "Sorter": 4.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelAge",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "SteelIngot",
        "achievement": "SteelAge",
        "chapter": "RoadToSteel",
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
        "Reward": {"items": []},
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumAge",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "AluminiumIngot",
        "achievement": "AluminiumAge",
        "chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumOre",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "TitaniumOre",
        "achievement": "TitaniumOre",
        "chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumAge",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "TitaniumIngot",
        "achievement": "TitaniumAge",
        "chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelAge",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "StainlessSteelIngot",
        "achievement": "StainlessSteelAge",
        "chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronOreAchievement",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "IronOre",
        "achievement": "IronOre",
        "chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumOreAchievement",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "AluminiumOre",
        "achievement": "AluminiumOre",
        "chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "GoldOreAchievement",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "GoldOre",
        "achievement": "GoldOre",
        "chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "UraniumOreAchievement",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "UraniumOre",
        "achievement": "UraniumOre",
        "chapter": "Other",
    }
)

quests.append(
    {
        "class": quest,
        "name": "CoalOreAchievement",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "CoalPiece",
        "achievement": "CoalOre",
        "chapter": "Other",
    }
)

# FirstSteps

qchapters.append(
    {
        "name": "FirstSteps",
        "class": qchapter,
        "Key": "FirstSteps",
        "Sorter": 0,
        "Reward": {"items": [{"name": "CopperMultitool", "count": 1}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "Log",
        "QuestTextKeys": ["collect"],
        "Item": "Log",
        "achievement": "Log",
        "chapter": "FirstSteps",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Furnace",
        "QuestTextKeys": ["collect", "Furnace"],
        "Item": "StoneFurnace",
        "chapter": "FirstSteps",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Dryer",
        "QuestTextKeys": ["collect", "Dryer"],
        "Item": "StoneDryer",
        "chapter": "FirstSteps",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Smelter",
        "QuestTextKeys": ["collect", "Smelter"],
        "Item": "StoneSmelter",
        "chapter": "FirstSteps",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Bed",
        "QuestTextKeys": ["collect", "Bed"],
        "Item": "Bed",
        "chapter": "FirstSteps",
        "Sorter": 2.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperOre",
        "QuestTextKeys": ["collect", "achievement", "CopperOre"],
        "Item": "CopperOre",
        "achievement": "CopperOre",
        "chapter": "FirstSteps",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperAge",
        "QuestTextKeys": ["collect", "achievement"],
        "Item": "CopperIngot",
        "achievement": "CopperAge",
        "chapter": "FirstSteps",
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
        "Reward": {"items": [{"name": "CopperMultitool", "count": 1}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "Organics",
        "QuestTextKeys": ["collect", "Organics"],
        "Item": "OrganicsPiece",
        "chapter": "Farming",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Farm",
        "QuestTextKeys": ["collect", "BambooFarm"],
        "Item": "CopperFarm",
        "chapter": "Farming",
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
            "items": [
                {"name": "CopperVent", "count": 1},
                {"name": "CopperPipe", "count": 10},
            ]
        },
    }
)

quests.append(
    {
        "class": quest,
        "name": "Boiler",
        "QuestTextKeys": ["collect", "Boiler"],
        "Item": "SteelBoiler",
        "chapter": "Steam",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Pump",
        "QuestTextKeys": ["collect", "Pump"],
        "Item": "SteelPump",
        "chapter": "Steam",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Pipe",
        "QuestTextKeys": ["collect", "Pipe"],
        "Item": "SteelPipe",
        "chapter": "Steam",
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
            "items": [
                {"name": "CopperFluidDump", "count": 1},
                {"name": "CopperVent", "count": 2},
            ]
        },
    }
)

quests.append(
    {
        "class": quest,
        "name": "AutomaticHammer",
        "QuestTextKeys": [
            "collect",
            "AutomaticHammer",
            "RefiningMachine",
        ],
        "Item": "CopperAutomaticHammer",
        "chapter": "Refining",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperPlate",
        "QuestTextKeys": ["collect", "Plate"],
        "Item": "CopperPlate",
        "chapter": "Refining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperImpureOreGravel",
        "QuestTextKeys": ["collect", "Refined"],
        "Item": "CopperImpureOreGravel",
        "chapter": "Refining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Washer",
        "QuestTextKeys": [
            "collect",
            "OreWasher",
            "RefiningMachine",
        ],
        "Item": "SteelOreWasher",
        "chapter": "Refining",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperOreGravel",
        "QuestTextKeys": ["collect", "Refined"],
        "Item": "CopperOreGravel",
        "chapter": "Refining",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Macerator",
        "QuestTextKeys": [
            "collect",
            "Macerator",
            "RefiningMachine",
        ],
        "Item": "CopperMacerator",
        "chapter": "Refining",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperImpureOreDust",
        "QuestTextKeys": ["collect", "Refined"],
        "Item": "CopperImpureOreDust",
        "chapter": "Refining",
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
        "Reward": {"items": [{"name": "CopperIngot", "count": 20}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "Steampack",
        "QuestTextKeys": [
            "collect",
            "Jumppack",
        ],
        "Item": "Steampack",
        "chapter": "FastTravel",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Jetpack",
        "QuestTextKeys": [
            "collect",
            "Jumppack",
        ],
        "Item": "Jetpack",
        "chapter": "FastTravel",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AdvancedJetpack",
        "QuestTextKeys": [
            "collect",
            "Jumppack",
        ],
        "Item": "AdvancedJetpack",
        "chapter": "FastTravel",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AntigravityUnit",
        "QuestTextKeys": [
            "collect",
            "Jumppack",
        ],
        "Item": "AntigravityUnit",
        "chapter": "FastTravel",
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
        "Reward": {"items": [{"name": "SteelFilteringRobotArm", "count": 3}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperRobotArm",
        "QuestTextKeys": ["collect", "RobotArm"],
        "Item": "CopperRobotArm",
        "chapter": "Logistics",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelRobotArm",
        "QuestTextKeys": ["collect", "RobotArm"],
        "Item": "SteelRobotArm",
        "chapter": "Logistics",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelFilteringRobotArm",
        "QuestTextKeys": ["collect", "FilteringRobotArm"],
        "Item": "SteelFilteringRobotArm",
        "chapter": "Logistics",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperConveyor",
        "QuestTextKeys": ["collect", "Conveyor"],
        "Item": "CopperConveyor",
        "chapter": "Logistics",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperConveyorSplitter",
        "QuestTextKeys": ["collect", "ConveyorSplitter"],
        "Item": "CopperConveyorSplitter",
        "chapter": "Logistics",
        "Sorter": 4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelConveyor",
        "QuestTextKeys": ["collect", "Conveyor"],
        "Item": "SteelConveyor",
        "chapter": "Logistics",
        "Sorter": 5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelConveyorSplitter",
        "QuestTextKeys": ["collect", "ConveyorSplitter"],
        "Item": "SteelConveyorSplitter",
        "chapter": "Logistics",
        "Sorter": 6,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperDeployer",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "CopperDeployer",
        "chapter": "Logistics",
        "Sorter": 7,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelDeployer",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "SteelDeployer",
        "chapter": "Logistics",
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
        "Reward": {"items": [{"name": "SteelIngot", "count": 10}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelCokeOven",
        "QuestTextKeys": ["collect", "CokeOven"],
        "Item": "SteelCokeOven",
        "chapter": "FasterSteel",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CokeDustFasterS",
        "QuestTextKeys": ["collect"],
        "Item": "CokeDust",
        "chapter": "FasterSteel",
        "Sorter": 1.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronDustFasterS",
        "QuestTextKeys": ["collect"],
        "Item": "IronDust",
        "chapter": "FasterSteel",
        "Sorter": 1.2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelAlloySmelter",
        "QuestTextKeys": ["collect", "AlloySmelter"],
        "Item": "SteelAlloySmelter",
        "chapter": "FasterSteel",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CastIronIngot",
        "QuestTextKeys": ["collect", "CastIron"],
        "Item": "CastIronIngot",
        "chapter": "FasterSteel",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CastIronDust",
        "QuestTextKeys": ["collect", "CastIron"],
        "Item": "CastIronDust",
        "chapter": "FasterSteel",
        "Sorter": 3.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelArcFurnace",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "SteelArcFurnace",
        "chapter": "FasterSteel",
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
            "items": [
                {"name": "SteelPipe", "count": 5},
                {"name": "CopperVent", "count": 2},
            ]
        },
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelAutomaticHammer",
        "QuestTextKeys": ["collect", "HigherLevel"],
        "Item": "SteelAutomaticHammer",
        "chapter": "FasterRefining",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelPlate",
        "QuestTextKeys": ["collect", "Plate"],
        "Item": "SteelPlate",
        "chapter": "FasterRefining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronImpureOreGravel",
        "QuestTextKeys": ["collect", "Refined"],
        "Item": "IronImpureOreGravel",
        "chapter": "FasterRefining",
        "Sorter": 0.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelWasher",
        "QuestTextKeys": ["collect", "HigherLevel"],
        "Item": "SteelOreWasher",
        "chapter": "FasterRefining",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronOreGravel",
        "QuestTextKeys": ["collect", "Refined"],
        "Item": "IronOreGravel",
        "chapter": "FasterRefining",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelMacerator",
        "QuestTextKeys": ["collect", "HigherLevel"],
        "Item": "SteelMacerator",
        "chapter": "FasterRefining",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronImpureOreDust",
        "QuestTextKeys": ["collect", "Refined"],
        "Item": "IronImpureOreDust",
        "chapter": "FasterRefining",
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
        "Reward": {"items": [{"name": "AluminiumIngot", "count": 5}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumOre",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumOre",
        "chapter": "RoadToAluminium",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumImpureOreGravel",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumImpureOreGravel",
        "chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumOreGravel",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumOreGravel",
        "chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumImpureOreDust",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumImpureOreDust",
        "chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumOxideDust",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumOxideDust",
        "chapter": "RoadToAluminium",
        "Sorter": 0.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelAlloySmelterAlum",
        "QuestTextKeys": ["collect"],
        "Item": "SteelAlloySmelter",
        "chapter": "RoadToAluminium",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumCarbideIngot",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumCarbideIngot",
        "chapter": "RoadToAluminium",
        "Sorter": 1.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumCarbideDust",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumCarbideDust",
        "chapter": "RoadToAluminium",
        "Sorter": 2.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelArcFurnaceAlum",
        "QuestTextKeys": ["collect"],
        "Item": "SteelArcFurnace",
        "chapter": "RoadToAluminium",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumIngot",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumIngot",
        "chapter": "RoadToAluminium",
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
        "Reward": {"items": [{"name": "AluminiumPneumaticPipe", "count": 15}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "CopperBufferChest",
        "QuestTextKeys": ["collect"],
        "Item": "CopperBufferChest",
        "chapter": "AdvancedLogistics",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SteelBufferChest",
        "QuestTextKeys": ["collect"],
        "Item": "SteelBufferChest",
        "chapter": "AdvancedLogistics",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumBufferChest",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumBufferChest",
        "chapter": "AdvancedLogistics",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumDeployer",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumDeployer",
        "chapter": "AdvancedLogistics",
        "Sorter": 4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumRobotArm",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumRobotArm",
        "chapter": "AdvancedLogistics",
        "Sorter": 5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumFilteringRobotArm",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumFilteringRobotArm",
        "chapter": "AdvancedLogistics",
        "Sorter": 6,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumPneumaticPipe",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumPneumaticPipe",
        "chapter": "AdvancedLogistics",
        "Sorter": 7,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumPneumaticInput",
        "QuestTextKeys": ["collect"],
        "Item": "AluminiumPneumaticInput",
        "chapter": "AdvancedLogistics",
        "Sorter": 8,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumConveyor",
        "QuestTextKeys": ["collect", "Conveyor"],
        "Item": "AluminiumConveyor",
        "chapter": "AdvancedLogistics",
        "Sorter": 9,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumConveyorSplitter",
        "QuestTextKeys": ["collect", "ConveyorSplitter"],
        "Item": "AluminiumConveyorSplitter",
        "chapter": "AdvancedLogistics",
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
        "Reward": {"items": [{"name": "StainlessSteelIngot", "count": 5}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "ChromeOxideDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "ChromeOxideDust",
        "chapter": "RoadToSS",
        "Sorter": 9.6,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminothermicChromeDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "AluminothermicChromeDust",
        "chapter": "RoadToSS",
        "Sorter": 9.7,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumSolidFurnace",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "AluminiumSolidFurnace",
        "chapter": "RoadToSS",
        "Sorter": 9.8,
    }
)

quests.append(
    {
        "class": quest,
        "name": "ChromeDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "ChromeDust",
        "chapter": "RoadToSS",
        "Sorter": 9.85,
    }
)

quests.append(
    {
        "class": quest,
        "name": "IronDustSS",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "IronDust",
        "chapter": "RoadToSS",
        "Sorter": 9.9,
    }
)

quests.append(
    {
        "class": quest,
        "name": "NickelDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "NickelDust",
        "chapter": "RoadToSS",
        "Sorter": 9.9,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumMixer",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "AluminiumMixer",
        "chapter": "RoadToSS",
        "Sorter": 9.95,
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "StainlessSteelDust",
        "chapter": "RoadToSS",
        "Sorter": 10,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminiumArcFurnace",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "AluminiumArcFurnace",
        "chapter": "RoadToSS",
        "Sorter": 11,
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelIngot",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "StainlessSteelIngot",
        "chapter": "RoadToSS",
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
        "Reward": {"items": [{"name": "NakCoolantDust", "count": 10}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelHeatExchanger",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "StainlessSteelHeatExchanger",
        "chapter": "HeatTransferring",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelInverseHeatExchanger",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "StainlessSteelInverseHeatExchanger",
        "chapter": "HeatTransferring",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelRadiator",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "StainlessSteelRadiator",
        "chapter": "HeatTransferring",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "NakCoolantDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "NakCoolantDust",
        "chapter": "HeatTransferring",
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
        "Reward": {"items": [{"name": "TitaniumIngot", "count": 5}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "CokeDustTit",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "CokeDust",
        "chapter": "RoadToTitanium",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumOxideDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TitaniumOxideDust",
        "chapter": "RoadToTitanium",
        "Sorter": 1.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelAlloySmelter",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "StainlessSteelAlloySmelter",
        "chapter": "RoadToTitanium",
        "Sorter": 1.2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "PreparedTitaniumOxideDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "PreparedTitaniumOxideDust",
        "chapter": "RoadToTitanium",
        "Sorter": 1.3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "ManganeseOxideDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "ManganeseOxideDust",
        "chapter": "RoadToTitanium",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "AluminothermicManganeseDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "AluminothermicManganeseDust",
        "chapter": "RoadToTitanium",
        "Sorter": 3.1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelSolidFurnace",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "StainlessSteelSolidFurnace",
        "chapter": "RoadToTitanium",
        "Sorter": 3.2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "ManganeseDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "ManganeseDust",
        "chapter": "RoadToTitanium",
        "Sorter": 3.3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "SaltDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "SaltDust",
        "chapter": "RoadToTitanium",
        "Sorter": 7,
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelChemReactor",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "StainlessSteelChemReactor",
        "chapter": "RoadToTitanium",
        "Sorter": 8,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumSponge",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TitaniumSponge",
        "chapter": "RoadToTitanium",
        "Sorter": 9.4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "StainlessSteelInductionFurnace",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "StainlessSteelInductionFurnace",
        "chapter": "RoadToTitanium",
        "Sorter": 9.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumIngot",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TitaniumIngot",
        "chapter": "RoadToTitanium",
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
        "Reward": {"items": [{"name": "HardMetalIngot", "count": 5}]},
    }
)

quests.append(
    {
        "class": quest,
        "name": "TungstenOxideDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TungstenOxideDust",
        "chapter": "RoadToHardMetal",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumInductionFurnace2",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TitaniumInductionFurnace",
        "chapter": "RoadToHardMetal",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "HotTungstenIngot",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "HotTungstenIngot",
        "chapter": "RoadToHardMetal",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumChemReactor",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TitaniumChemReactor",
        "chapter": "RoadToHardMetal",
        "Sorter": 4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TungstenCarbideIngot",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TungstenCarbideIngot",
        "chapter": "RoadToHardMetal",
        "Sorter": 5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TungstenCarbideDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TungstenCarbideDust",
        "chapter": "RoadToHardMetal",
        "Sorter": 6.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CobaltOxideDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "CobaltOxideDust",
        "chapter": "RoadToHardMetal",
        "Sorter": 6.55,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumChemReactor2",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TitaniumChemReactor",
        "chapter": "RoadToHardMetal",
        "Sorter": 6.555,
    }
)

quests.append(
    {
        "class": quest,
        "name": "CobaltDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "CobaltDust",
        "chapter": "RoadToHardMetal",
        "Sorter": 6.6,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumMixer",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TitaniumMixer",
        "chapter": "RoadToHardMetal",
        "Sorter": 6.9,
    }
)

quests.append(
    {
        "class": quest,
        "name": "HardMetalDust",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "HardMetalDust",
        "chapter": "RoadToHardMetal",
        "Sorter": 7,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumInductionFurnace",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TitaniumInductionFurnace",
        "chapter": "RoadToHardMetal",
        "Sorter": 7.5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "HotHardMetalIngot",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "HotHardMetalIngot",
        "chapter": "RoadToHardMetal",
        "Sorter": 8,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TitaniumFreezer",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "TitaniumFreezer",
        "chapter": "RoadToHardMetal",
        "Sorter": 9,
    }
)

quests.append(
    {
        "class": quest,
        "name": "HardMetalIngot",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "HardMetalIngot",
        "chapter": "RoadToHardMetal",
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
        "Reward": {"items": [{"name": "WoodenPlanks", "count": 64}]},
        "achievement": "Woodwork",
    }
)

quests.append(
    {
        "class": quest,
        "name": "Door",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "Door",
        "chapter": "Woodwork",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Chair",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "Chair",
        "chapter": "Woodwork",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Fence",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "Fence",
        "chapter": "Woodwork",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Ladder",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "Ladder",
        "chapter": "Woodwork",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Rack",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "Rack",
        "chapter": "Woodwork",
        "Sorter": 4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Table",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "Table",
        "chapter": "Woodwork",
        "Sorter": 5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Torch",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "Torch",
        "chapter": "Woodwork",
        "Sorter": 6,
    }
)

quests.append(
    {
        "class": quest,
        "name": "WoodenChest",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "WoodenChest",
        "chapter": "Woodwork",
        "Sorter": 7,
    }
)

quests.append(
    {
        "class": quest,
        "name": "WoodenStairs",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "WoodenStairs",
        "chapter": "Woodwork",
        "Sorter": 7,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Window",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "Window",
        "chapter": "Woodwork",
        "Sorter": 8,
    }
)

quests.append(
    {
        "class": quest,
        "name": "WoodenPlanks",
        "QuestTextKeys": [
            "collect",
        ],
        "Item": "WoodenPlanks",
        "chapter": "Woodwork",
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
            "items": [
                {"name": "DarkStoneSurface", "count": 50},
                {"name": "StoneSurface", "count": 50},
                {"name": "RedStoneSurface", "count": 50},
            ]
        },
    }
)

quests.append(
    {
        "class": quest,
        "name": "DarkBricks",
        "QuestTextKeys": ["collect"],
        "Item": "DarkBricks",
        "chapter": "Decorative",
        "Sorter": 0,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Bricks",
        "QuestTextKeys": ["collect"],
        "Item": "Bricks",
        "chapter": "Decorative",
        "Sorter": 1,
    }
)

quests.append(
    {
        "class": quest,
        "name": "RedBricks",
        "QuestTextKeys": ["collect"],
        "Item": "RedBricks",
        "chapter": "Decorative",
        "Sorter": 2,
    }
)

quests.append(
    {
        "class": quest,
        "name": "RedStoneTiles",
        "QuestTextKeys": ["collect"],
        "Item": "RedStoneTiles",
        "chapter": "Decorative",
        "Sorter": 3,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Terracotta",
        "QuestTextKeys": ["collect"],
        "Item": "Terracotta",
        "chapter": "Decorative",
        "Sorter": 4,
    }
)

quests.append(
    {
        "class": quest,
        "name": "TerracottaTiles",
        "QuestTextKeys": ["collect"],
        "Item": "TerracottaTiles",
        "chapter": "Decorative",
        "Sorter": 5,
    }
)

quests.append(
    {
        "class": quest,
        "name": "DarkStoneTiles",
        "QuestTextKeys": ["collect"],
        "Item": "DarkStoneTiles",
        "chapter": "Decorative",
        "Sorter": 6,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Column",
        "QuestTextKeys": ["collect"],
        "Item": "Column",
        "chapter": "Decorative",
        "Sorter": 7,
    }
)

quests.append(
    {
        "class": quest,
        "name": "FluetedColumn",
        "QuestTextKeys": ["collect"],
        "Item": "FluetedColumn",
        "chapter": "Decorative",
        "Sorter": 8,
    }
)

quests.append(
    {
        "class": quest,
        "name": "Stairs",
        "QuestTextKeys": ["collect"],
        "Item": "Stairs",
        "chapter": "Decorative",
        "Sorter": 9,
    }
)

quests.append(
    {
        "class": quest,
        "name": "StoneTiles",
        "QuestTextKeys": ["collect"],
        "Item": "StoneTiles",
        "chapter": "Decorative",
        "Sorter": 10,
    }
)

data = {"Objects": quests}

write_file("Generated/Quests/quests.generated.json", data)

data = {"Objects": qchapters}

write_file("Generated/Chapters/qchapters.generated.json", data)
