## -*- coding: utf-8 -*-

from Common import *
from Materials import *

parts = []

parts.append(
    {
        "Label": "Plate",
        "name": "Plate",
        "Volume": 1,  # from 1 ingot
        "StartTier": 1,
        "EndTier": 100,
        "Stack": 64,
    }
)
parts.append(
    {
        "Label": "Parts",
        "name": "Parts",
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
        "name": "Casing",
        "StartTier": 1,
        "EndTier": 100,
        "item_logic": building_cube_logic,
        "Stack": 32,
        "RequiredResearches": ["MetalConstructions"],
        "tag": "Decoration",
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
        "name": "Multitool",
        "Label": "Multitool",
        "item_logic": "Equipped/MultitoolBP.MultitoolBP_C",
        "StartTier": 1,
        "EndTier": 7,
        "CommonTextKeys": ["Multitool"],
    },
    {
        "name": "Screwdriver",
        "Label": "Screwdriver",
        "item_logic": "Equipped/ScrewdriverBP.ScrewdriverBP_C",
        "StartTier": 1,
        "EndTier": 1,
        "CommonTextKeys": ["Screwdriver"],
    },
    {
        "name": "PaintTool",
        "Label": "Paint Tool",
        "item_logic": "Equipped/PaintToolBP.PaintToolBP_C",
        "StartTier": 1,
        "EndTier": 1,
        "CommonTextKeys": ["Multitool"],
        "CustomData": {"PaintMaterial": "Amethyst"},
    }
    # {
    # 	"name": "BuildTool",
    # 	"Label": "Build Tool",
    # 	"item_logic": "Equipped/BuildToolBP.BuildToolBP_C",
    # 	"StartTier": 7,
    # 	"EndTier": 7,
    # }
    # ,{
    # 	"name": "AdminTool",
    # 	"Label": "Admin Tool",
    # 	"item_logic": "Equipped/AdminToolBP.AdminToolBP_C",
    # 	"StartTier": 7,
    # 	"EndTier": 7,
    # },
    # {
    # 	"name": "StorageUpgrade",
    # 	"Label": "Storage Upgrade",
    # 	"item_logic": "Equipped/StorageUpgradeBP.StorageUpgradeBP_C",
    # 	"StartTier": 0,
    # 	"EndTier": 7,
    # }
]
