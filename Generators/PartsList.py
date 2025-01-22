## -*- coding: utf-8 -*-

from Common import *
from Materials import *

parts = [
    {
		"Label" : "Plate",
		"Name" : "Plate",
		"Volume": 1, # from 1 ingot
		"StartTier": 1,
		"EndTier": 100,
		"StackSize": 64,
	},
	{
		"Label" : "Parts",
		"Name" : "Parts",
		"Volume": 1,
		"StartTier": 1,
		"EndTier": 100,
		"StackSize": 64,
		"Mesh":"/Game/Models/PartsCrate",
		"Materials":["/Game/Materials/Pine","/Game/Materials/%Material%"],
	},
	{
		"Label" : "Casing",
		"Name" : "Casing",
		"StartTier": 1,
		"EndTier": 100,
		"ItemLogic": building_cube_logic,
		"StackSize": 32,
		"RequiredResearch":["MetalConstructions"+static_research],
	},
	{
		"Label" : "Gearbox",
		"Name" : "Gearbox",
		"StartTier": 1,
		"EndTier": 100,
		"StackSize": 32
	},
	{
		"Label" : "Solar Cell",
		"Name" : "SolarCell",
		"StartTier": 3,
		"EndTier": 100,
		"StackSize": 32
	},
	{
		"Label" : "Locomotive",
		"Name" : "Locomotive",
		"StartTier": 2,
		"EndTier": 2,
		"StackSize": 1
	},
	{
		"Label" : "Wagon",
		"Name" : "Wagon",
		"StartTier": 2,
		"EndTier": 2,
		"StackSize": 1
	}
]

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

catalyzers = [
	"CopperDust",      # 0 stone
	"CopperDust",      # 1 copper
	"GoldDust",        # 2 steel
	"GoldDust",        # 3 alum
	"Processor",        # 4 ss
	"QuantumCircuit",   # 5 tita
	"QuantumProcessor", # 6 hard
	"QuantumBrain",     # 7 neu
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
		"CommonTextKeys": [
			"Multitool"
		]
	},{
		"Name": "Screwdriver",
		"Label": "Screwdriver",
		"ItemLogic": "Equipped/ScrewdriverBP.ScrewdriverBP_C",
		"CommonTextKeys": [
			"Screwdriver"
		]
	},{
		"Name": "PaintTool",
		"Label": "Paint Tool",
		"ItemLogic": "Equipped/PaintToolBP.PaintToolBP_C",
		"CommonTextKeys": [
			"Multitool"
		],
		"CustomData":{
			"PaintMaterial":"Amethyst"
		}
	},{
		"Name": "ConstructionTool",
		"Label": "Construction Tool",
		"ItemLogic": "Equipped/ConstructionToolBP.ConstructionToolBP_C",
	},{
		"Name": "DeconstructionTool",
		"Label": "Deconstruction Tool",
		"ItemLogic": "Equipped/DeconstructionToolBP.DeconstructionToolBP_C",
	},{
		"Name": "ConstructionBlueprint",
		"Label": "Construction Blueprint",
        "ItemLogic": "Equipped/BlueprintToolBP.BlueprintToolBP_C",
	},{
		"Name": "DeconstructionBlueprint",
		"Label": "Deconstruction Blueprint",
        "ItemLogic": "Equipped/BlueprintToolBP.BlueprintToolBP_C",
	},{
		"Name": "UpgradeBlueprint",
		"Label": "Upgrade Blueprint",
        "ItemLogic": "Equipped/BlueprintToolBP.BlueprintToolBP_C",
	}
	#{
	#	"Name": "BuildTool",
	#	"Label": "Build Tool",
	#	"ItemLogic": "Equipped/BuildToolBP.BuildToolBP_C",
	#	"StartTier": 7,
	#	"EndTier": 7,
	#}
	#,{
	#	"Name": "AdminTool",
	#	"Label": "Admin Tool",
	#	"ItemLogic": "Equipped/AdminToolBP.AdminToolBP_C",
	#	"StartTier": 7,
	#	"EndTier": 7,
	#},
	#{
	#	"Name": "StorageUpgrade",
	#	"Label": "Storage Upgrade",
	#	"ItemLogic": "Equipped/StorageUpgradeBP.StorageUpgradeBP_C",
	#	"StartTier": 0,
	#	"EndTier": 7,
	#}
]