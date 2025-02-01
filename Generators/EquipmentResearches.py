from Common import *
from Materials import *

def append_equipment(xy, append_levels, researches):
	append_levels({
		"Class": "StaticResearch",
		"Name": "Steampack",
		"LabelParts": [["Steampack", "misc"]],
		"RequiredResearch": ["Circuit"],
		"Unlocks": [["Hand" + r_dict, "Steampack"]],
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "HighPressureSteampack",
		"LabelParts": [["HighPressureSteampack", "misc"]],
		"RequiredResearch": ["Steampack"],
		"Unlocks": [["Hand" + r_dict, "HighPressureSteampack"]],
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "HighCapacitySteampack",
		"LabelParts": [["HighCapacitySteampack", "misc"]],
		"RequiredResearch": ["Steampack"],
		"Unlocks": [["Hand" + r_dict, "HighCapacitySteampack"]],
		
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedSteampack",
		"LabelParts": [["AdvancedSteampack", "misc"]],
		"RequiredResearch": ["HighCapacitySteampack", "HighPressureSteampack"],
		"Unlocks": [["Hand" + r_dict, "AdvancedSteampack"]],
		
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Flashlight",
		"LabelParts": [["Flashlight", "misc"]],
		"RequiredResearch": ["Multitool"],
		"Unlocks": [["Hand" + r_dict, "Flashlight"]],
		
		
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Jetpack",
		"LabelParts": [["Jetpack", "misc"]],
		"RequiredResearch": ["AdvancedCircuit", "Steampack", "ElectricEngine1"],
		"Unlocks": [["Hand" + r_dict, "Jetpack"]],
		
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedJetpack",
		"LabelParts": [["AdvancedJetpack", "misc"]],
		"RequiredResearch": ["Jetpack", "Processor", "ElectricEngine2"],
		"Unlocks": [["Hand" + r_dict, "AdvancedJetpack"]],
		
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AntigravityUnit",
		"LabelParts": [["AntigravityUnit", "misc"]],
		"RequiredResearch": ["AdvancedJetpack", "QuantumProcessor", "Calalyst"],
		"Unlocks": [["Hand" + r_dict, "AntigravityUnit"]],
		
		
		"Levels": [5,5],
	})