from Common import *
from Materials import *

def append_equipment(xy, append_levels, researches):
	append_levels({
		"Class": "StaticResearch",
		"Name": "Steampack",
		"LabelParts": [["Steampack", "misc"]],
		"RequiredResearch": ["Circuit"],
		"Unlocks": [["Hand" + base_recipe, "Steampack"]],
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "HighPressureSteampack",
		"LabelParts": [["HighPressureSteampack", "misc"]],
		"RequiredResearch": ["Steampack"],
		"Unlocks": [["Hand" + base_recipe, "HighPressureSteampack"]],
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "HighCapacitySteampack",
		"LabelParts": [["HighCapacitySteampack", "misc"]],
		"RequiredResearch": ["Steampack"],
		"Unlocks": [["Hand" + base_recipe, "HighCapacitySteampack"]],
		
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedSteampack",
		"LabelParts": [["AdvancedSteampack", "misc"]],
		"RequiredResearch": ["HighCapacitySteampack", "HighPressureSteampack"],
		"Unlocks": [["Hand" + base_recipe, "AdvancedSteampack"]],
		
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Flashlight",
		"LabelParts": [["Flashlight", "misc"]],
		"RequiredResearch": ["Multitool"],
		"Unlocks": [["Hand" + base_recipe, "Flashlight"]],
		
		
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Jetpack",
		"LabelParts": [["Jetpack", "misc"]],
		"RequiredResearch": ["AdvancedCircuit", "Steampack", "ElectricEngine1"],
		"Unlocks": [["Hand" + base_recipe, "Jetpack"]],
		
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedJetpack",
		"LabelParts": [["AdvancedJetpack", "misc"]],
		"RequiredResearch": ["Jetpack", "Processor", "ElectricEngine2"],
		"Unlocks": [["Hand" + base_recipe, "AdvancedJetpack"]],
		
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AntigravityUnit",
		"LabelParts": [["AntigravityUnit", "misc"]],
		"RequiredResearch": ["AdvancedJetpack", "QuantumProcessor", "Calalyst"],
		"Unlocks": [["Hand" + base_recipe, "AntigravityUnit"]],
		
		
		"Levels": [5,5],
	})