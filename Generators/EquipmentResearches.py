from Common import *
from Materials import *

def append_equipment(xy, append_levels, researches):
	append_levels({
		"Class": research_recipe,
		"Name": "Steampack",
		"Label": ["Steampack", "misc"],
		"RequiredResearch": ["Circuit"],
		"Unlocks": [["Hand" + r_dict, "Steampack"]],
		"Levels": [1,1],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "HighPressureSteampack",
		"Label": ["HighPressureSteampack", "misc"],
		"RequiredResearch": ["Steampack"],
		"Unlocks": [["Hand" + r_dict, "HighPressureSteampack"]],
		"Levels": [2,2],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "HighCapacitySteampack",
		"Label": ["HighCapacitySteampack", "misc"],
		"RequiredResearch": ["Steampack"],
		"Unlocks": [["Hand" + r_dict, "HighCapacitySteampack"]],
		
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "AdvancedSteampack",
		"Label": ["AdvancedSteampack", "misc"],
		"RequiredResearch": ["HighCapacitySteampack", "HighPressureSteampack"],
		"Unlocks": [["Hand" + r_dict, "AdvancedSteampack"]],
		
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "Jetpack",
		"Label": ["Jetpack", "misc"],
		"RequiredResearch": ["AdvancedCircuit", "Steampack", "ElectricEngine1"],
		"Unlocks": [["Hand" + r_dict, "Jetpack"]],
		
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "AdvancedJetpack",
		"Label": ["AdvancedJetpack", "misc"],
		"RequiredResearch": ["Jetpack", "Processor", "ElectricEngine2"],
		"Unlocks": [["Hand" + r_dict, "AdvancedJetpack"]],
		
		
		"Levels": [4,4],
		"CostMul": 2.5,
	})
	append_levels({
		"Class": research_recipe,
		"Name": "AntigravityUnit",
		"Label": ["AntigravityUnit", "misc"],
		"RequiredResearch": ["AdvancedJetpack", "QuantumProcessor", "Catalyst"],
		"Unlocks": [["Hand" + r_dict, "AntigravityUnit"]],
		
		
		"Levels": [5,5],
	})