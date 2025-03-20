## -*- coding: utf-8 -*-

from Common import *
from Materials import *

parts = [
	{
		"Label": "Parts",
		"Name": "Parts",
		"StackSize": 64,
		"Mesh":"/Game/Models/PartsCrate",
		"Materials":["/Game/Materials/Pine","/Game/Materials/%Material%"],
	},{
		"Label": "Gearbox",
		"Name": "Gearbox",
		"StackSize": 32
	},{
		"Label": "Solar Cell",
		"Name": "SolarCell",
		"StackSize": 32
	},{
		"Label": "Sheet",
		"Name": "Sheet",
		"StackSize": 128
	},{
		"Label": "Wire",
		"Name": "Wire",
		"StackSize": 128
	},{
		"Label": "Foil",
		"Name": "Foil",
		"StackSize": 128
	}
]

def named_part(name):
	list = [x for x in parts if x["Name"] == name]
	if len(list) > 0:
		return list[0]
	raise Exception(f"Part {name} not found!")

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

a_wires = [
	"CopperWire", # 0 stone
	"CopperWire", # 1 copper
	"CopperWire", # 2 steel
	"CopperrWire", # 3 alum
	"SilverWire",   # 4 ss
	"GoldWire", # 5 tita
	"PlatinumWire",  # 6 hard
	"YttriumWire",  # 7 neu
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
	"StoneSurface",
	"StoneSurface",
	"StoneSurface",
	"StoneSurface",
	"StoneSurface",
]

tools = [
	{
		"Name": "Multitool",
		"Label": "Multitool",
		"ItemLogic": "/Game/Equipped/MultitoolBP.MultitoolBP_C",
		"CommonTextKeys": [
			"Multitool"
		]
	},{
		"Name": "Screwdriver",
		"Label": "Screwdriver",
		"ItemLogic": "/Game/Equipped/ScrewdriverBP.ScrewdriverBP_C",
		"CommonTextKeys": [
			"Screwdriver"
		]
	},{
		"Name": "PaintTool",
		"Label": "Paint Tool",
		"ItemLogic": "/Game/Equipped/PaintToolBP.PaintToolBP_C",
		"CommonTextKeys": [
			"Multitool"
		],
		"CustomData":{
			"PaintMaterial":"Amethyst"
		}
	},{
		"Name": "ConstructionTool",
		"Label": "Construction Tool",
		"ItemLogic": "/Game/Equipped/ConstructionToolBP.ConstructionToolBP_C",
	},{
		"Name": "DeconstructionTool",
		"Label": "Deconstruction Tool",
		"ItemLogic": "/Game/Equipped/DeconstructionToolBP.DeconstructionToolBP_C",
	},{
		"Name": "ConstructionBlueprint",
		"Label": "Construction Blueprint",
        "ItemLogic": "/Game/Equipped/BlueprintToolBP.BlueprintToolBP_C",
	},{
		"Name": "DeconstructionBlueprint",
		"Label": "Deconstruction Blueprint",
        "ItemLogic": "/Game/Equipped/BlueprintToolBP.BlueprintToolBP_C",
	},{
		"Name": "UpgradeBlueprint",
		"Label": "Upgrade Blueprint",
        "ItemLogic": "/Game/Equipped/BlueprintToolBP.BlueprintToolBP_C",
	},{
		"Name": "DecorationTool",
		"Label": "Decoration Tool",
		"ItemLogic": "/Game/Equipped/DecorationToolBP.DecorationToolBP_C",
	}
	#{
	#	"Name": "BuildTool",
	#	"Label": "Build Tool",
	#	"ItemLogic": "/Game/Equipped/BuildToolBP.BuildToolBP_C",
	#	"StartTier": 7,
	#	"EndTier": 7,
	#}
	#,{
	#	"Name": "AdminTool",
	#	"Label": "Admin Tool",
	#	"ItemLogic": "/Game/Equipped/AdminToolBP.AdminToolBP_C",
	#	"StartTier": 7,
	#	"EndTier": 7,
	#},
	#{
	#	"Name": "StorageUpgrade",
	#	"Label": "Storage Upgrade",
	#	"ItemLogic": "/Game/Equipped/StorageUpgradeBP.StorageUpgradeBP_C",
	#	"StartTier": 0,
	#	"EndTier": 7,
	#}
]