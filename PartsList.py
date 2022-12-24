## -*- coding: utf-8 -*-

from Common import *
from Materials import *

parts = []

parts.append(
    {
        "Label": "Plate",
        "Name": "Plate",
        "Volume": 1,  # from 1 ingot
        "StartTier": 1,
        "EndTier": 100,
        "Stack": 64,
    }
)
parts.append(
    {
        "Label": "Parts",
        "Name": "Parts",
        "Volume": 1,
        "StartTier": 1,
        "EndTier": 100,
        "Stack": 64,
        "Mesh": "Models/PartsCrate",
        "Materials": ["Materials/Pine", "Materials/%Material%"],
    }
)
parts.append(
    {
        "Label": "Casing",
        "Name": "Casing",
        "StartTier": 1,
        "EndTier": 100,
        "ItemLogic": building_cube_logic,
        "Stack": 32,
        "RequiredResearches": ["MetalConstructions"],
        "Tag": "Decoration",
    }
)

circuits = [
    "CopperParts",
    "CopperParts",
    "Circuit",
    "AdvancedCircuit",
    "Processor",
    "QuantumCircuit",
    "QuantumProcessor",
    "QuantumBrain",
]

wires = [
    "CopperWire",
    "CopperWire",
    "CopperWire",
    "CopperWire",
    "CopperWire",
    "GoldWire",
    "GoldWire",
    "SuperconductorWire",
]

cables = [
    "CopperConnector",
    "CopperConnector",
    "CopperConnector",
    "CopperConnector",
    "CopperConnector",
    "CopperConnector",
    "CopperConnector",
    "CopperConnector",
]

electric_isolators = [
    "Glass",
    "Glass",
    "Glass",
    "Glass",
    "Glass",
    "Glass",
    "Glass",
    "Glass",
]

heat_isolators = [
    "StoneSurface",
    "StoneSurface",
    "StoneSurface",
    "Concrete",
    "Concrete",
    "ReinforcedConcrete",
    "ReinforcedConcrete",
    "ReinforcedConcrete",
]

tools = [
    {
        "Name": "Multitool",
        "Label": "Multitool",
        "ItemLogic": "Equipped/MultitoolBP.MultitoolBP_C",
        "StartTier": 1,
        "EndTier": 7,
        "CommonTextKeys": ["Multitool"],
    },
    {
        "Name": "Screwdriver",
        "Label": "Screwdriver",
        "ItemLogic": "Equipped/ScrewdriverBP.ScrewdriverBP_C",
        "StartTier": 1,
        "EndTier": 1,
        "CommonTextKeys": ["Screwdriver"],
    },
    {
        "Name": "PaintTool",
        "Label": "Paint Tool",
        "ItemLogic": "Equipped/PaintToolBP.PaintToolBP_C",
        "StartTier": 1,
        "EndTier": 1,
        "CommonTextKeys": ["Multitool"],
        "CustomData": {"PaintMaterial": "Amethyst"},
    }
    # {
    # 	"Name": "BuildTool",
    # 	"Label": "Build Tool",
    # 	"ItemLogic": "Equipped/BuildToolBP.BuildToolBP_C",
    # 	"StartTier": 7,
    # 	"EndTier": 7,
    # }
    # ,{
    # 	"Name": "AdminTool",
    # 	"Label": "Admin Tool",
    # 	"ItemLogic": "Equipped/AdminToolBP.AdminToolBP_C",
    # 	"StartTier": 7,
    # 	"EndTier": 7,
    # },
    # {
    # 	"Name": "StorageUpgrade",
    # 	"Label": "Storage Upgrade",
    # 	"ItemLogic": "Equipped/StorageUpgradeBP.StorageUpgradeBP_C",
    # 	"StartTier": 0,
    # 	"EndTier": 7,
    # }
]
