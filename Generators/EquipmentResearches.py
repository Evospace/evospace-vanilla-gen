from Common import *
from Materials import *

def append_equipment(xy, append_levels, researches):
	append_levels({
		"Class": "StaticResearch",
		"Name": "Steampack" + static_research,
		"LabelParts": [["Steampack", "misc"]],
		"RequiredResearch": ["Circuit"],
		"Unlocks": [["Hand" + base_recipe, "Steampack"]],
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "HighPressureSteampack" + static_research,
		"LabelParts": [["HighPressureSteampack", "misc"]],
		"RequiredResearch": ["Steampack"],
		"Unlocks": [["Hand" + base_recipe, "HighPressureSteampack"]],
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "HighCapacitySteampack" + static_research,
		"LabelParts": [["HighCapacitySteampack", "misc"]],
		"RequiredResearch": ["Steampack"],
		"Unlocks": [["Hand" + base_recipe, "HighCapacitySteampack"]],
		
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedSteampack" + static_research,
		"LabelParts": [["AdvancedSteampack", "misc"]],
		"RequiredResearch": ["HighCapacitySteampack", "HighPressureSteampack"],
		"Unlocks": [["Hand" + base_recipe, "AdvancedSteampack"]],
		
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Flashlight" + static_research,
		"LabelParts": [["Flashlight", "misc"]],
		"RequiredResearch": ["Multitool"],
		"Unlocks": [["Hand" + base_recipe, "Flashlight"]],
		
		
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Jetpack" + static_research,
		"LabelParts": [["Jetpack", "misc"]],
		"RequiredResearch": ["AdvancedCircuit", "Steampack", "ElectricEngine1"],
		"Unlocks": [["Hand" + base_recipe, "Jetpack"]],
		
		
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedJetpack" + static_research,
		"LabelParts": [["AdvancedJetpack", "misc"]],
		"RequiredResearch": ["Jetpack", "Processor", "ElectricEngine2"],
		"Unlocks": [["Hand" + base_recipe, "AdvancedJetpack"]],
		
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AntigravityUnit" + static_research,
		"LabelParts": [["AntigravityUnit", "misc"]],
		"RequiredResearch": ["AdvancedJetpack", "QuantumProcessor", "Calalyst"],
		"Unlocks": [["Hand" + base_recipe, "AntigravityUnit"]],
		
		
		"Levels": [5,5],
	})