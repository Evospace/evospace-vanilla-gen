## -*- coding: utf-8 -*-

from Common import *
from Materials import *

parts = []
	
parts.append({
	"Label" : "Plate",
	"Name" : "Plate",
	"Volume": 1, # from 1 ingot
	"StartTier": 1,
	"EndTier": 100,
	"Stack": 64,
})	
parts.append({
	"Label" : "Parts",
	"Name" : "Parts",
	"Volume": 1,
	"StartTier": 1,
	"EndTier": 100,
	"Stack": 64,
	"Mesh":"Models/PartsCrate",
	"Materials":["Materials/Pine","Materials/%Material%"],
})
parts.append({
	"Label" : "Casing",
	"Name" : "Casing",
	"StartTier": 1,
	"EndTier": 100,
	"ItemLogic": building_cube_logic,
	"Stack": 32,
	"RequiredResearches":["MetalConstructions"+static_research],
	"Tag": "Decoration"
})

circuits = [
	"CopperParts" + static_item,
	"CopperParts" + static_item,
	"Circuit" + static_item,
	"AdvancedCircuit" + static_item,
	"Processor" + static_item,
	"QuantumCircuit" + static_item,
	"QuantumProcessor" + static_item,
	"QuantumBrain" + static_item,
]

wires = [
	"CopperWire" + static_item,
	"CopperWire" + static_item,
	"CopperWire" + static_item,
	"CopperWire" + static_item,
	"CopperWire" + static_item,
	"GoldWire" + static_item,
	"GoldWire" + static_item,
	"SuperconductorWire" + static_item,
]

cables = [
	"CopperConnector" + static_item,
	"CopperConnector" + static_item,
	"CopperConnector" + static_item,
	"CopperConnector" + static_item,
	"CopperConnector" + static_item,
	"CopperConnector" + static_item,
	"CopperConnector" + static_item,
	"CopperConnector" + static_item,
]

electric_isolators = [
	"Glass" + static_item,
	"Glass" + static_item,
	"Glass" + static_item,
	"Glass" + static_item,
	"Glass" + static_item,
	"Glass" + static_item,
	"Glass" + static_item,
	"Glass" + static_item,
]

heat_isolators = [
	"StoneSurface" + static_item,
	"StoneSurface" + static_item,
	"StoneSurface" + static_item,
	"Concrete" + static_item,
	"Concrete" + static_item,
	"ReinforcedConcrete" + static_item,
	"ReinforcedConcrete" + static_item,
	"ReinforcedConcrete" + static_item,
]

tools = [
	{
		"Name": "Multitool",
		"Label": "Multitool",
		"ItemLogic": "Equipped/MultitoolBP.MultitoolBP_C",
		"StartTier": 1,
		"EndTier": 7,
		"CommonTextKeys": [
			"Multitool"
		]
	},{
		"Name": "Screwdriver",
		"Label": "Screwdriver",
		"ItemLogic": "Equipped/ScrewdriverBP.ScrewdriverBP_C",
		"StartTier": 1,
		"EndTier": 1,
		"CommonTextKeys": [
			"Screwdriver"
		]
	},{
		"Name": "PaintTool",
		"Label": "Paint Tool",
		"ItemLogic": "Equipped/PaintToolBP.PaintToolBP_C",
		"StartTier": 1,
		"EndTier": 1,
		"CommonTextKeys": [
			"Multitool"
		],
		"CustomData":{
			"PaintMaterial":"Amethyst"
		}
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