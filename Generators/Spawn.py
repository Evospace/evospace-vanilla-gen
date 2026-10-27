#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common import *

data = {
	"Objects": [
		{
			"Class": "StaticPlayer",
			"Name": "Player",
			"HandRecipes": "HandRecipeDictionary",
			"Hotbar": ["Multitool", "BasicPlatform"],
			"Tools": ["Multitool", "Screwdriver", "GroundLevelingTool"],
			"Light": "BuiltinFlashlight",
			"BlueprintItem": "ConstructionBlueprint",
			"StartInventory": {
				"Items": [
					{
						"Name": "BuildingMaterial",
						"Count": 1000
					},
					{
						"Name": "Portal",
						"Count": 1
					}
				]
			},
			"StartResearches": ["MineralsScan", "BasicPlatform", "Chest", "Electricity", "PowerGeneration", "Smelting", "Metalwork", "DistributedComputing", "CopperWire"]
		}
	]
}

write_file("Generated/Mixed/player.json", data)
