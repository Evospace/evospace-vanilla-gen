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
        "max_count": 64,
    }
)
parts.append(
    {
        "Label": "Parts",
        "name": "Parts",
        "Volume": 1,
        "StartTier": 1,
        "EndTier": 100,
        "max_count": 64,
        "mesh": "Models/PartsCrate",
        "Materials": ["Materials/Pine", "Materials/%Material%"],
    }
)
parts.append(
    {
        "Label": "Casing",
        "name": "Casing",
        "StartTier": 1,
        "EndTier": 100,
        "logic": building_cube_logic,
        "max_count": 32,
        "required": ["MetalConstructions"],
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
        "logic": "Equipped/MultitoolBP.MultitoolBP_C",
        "StartTier": 1,
        "EndTier": 7,
        "CommonTextKeys": ["Multitool"],
    },
    {
        "name": "Screwdriver",
        "Label": "Screwdriver",
        "logic": "Equipped/ScrewdriverBP.ScrewdriverBP_C",
        "StartTier": 1,
        "EndTier": 1,
        "CommonTextKeys": ["Screwdriver"],
    },
    {
        "name": "PaintTool",
        "Label": "Paint Tool",
        "logic": "Equipped/PaintToolBP.PaintToolBP_C",
        "StartTier": 1,
        "EndTier": 1,
        "CommonTextKeys": ["Multitool"],
        "CustomData": {"PaintMaterial": "Amethyst"},
    }
    # {
    # 	"name": "BuildTool",
    # 	"Label": "Build Tool",
    # 	"logic": "Equipped/BuildToolBP.BuildToolBP_C",
    # 	"StartTier": 7,
    # 	"EndTier": 7,
    # }
    # ,{
    # 	"name": "AdminTool",
    # 	"Label": "Admin Tool",
    # 	"logic": "Equipped/AdminToolBP.AdminToolBP_C",
    # 	"StartTier": 7,
    # 	"EndTier": 7,
    # },
    # {
    # 	"name": "StorageUpgrade",
    # 	"Label": "Storage Upgrade",
    # 	"logic": "Equipped/StorageUpgradeBP.StorageUpgradeBP_C",
    # 	"StartTier": 0,
    # 	"EndTier": 7,
    # }
]
