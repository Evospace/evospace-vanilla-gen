from Common import *
from Materials import *

def append_nuclear(xy, append_levels, researches):
	append_levels({
		"Class": research_recipe,
		"Name": "ControlCell",
		"Label": ["ControlCell", "parts"],
		"RequiredResearch": ["FissionReactor"],
		"Unlocks": [[assembler_r_dict, "ControlCell"], ["Hand" + r_dict, "ControlCell"],["FissionReactor" + r_dict, "ControlCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "ReflectorCell",
		"Label": ["ReflectorCell", "parts"],
		"RequiredResearch": ["ControlCell"],
		"Unlocks": [[assembler_r_dict, "ReflectorCell"], ["Hand" + r_dict, "ReflectorCell"],["FissionReactor" + r_dict, "UraniumCell2"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "AdvancedReflection",
		"Label": ["AdvancedReflection", "researches"],
		"RequiredResearch": ["ReflectorCell"],
		"Unlocks": [["FissionReactor" + r_dict, "UraniumCell3"]],
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "ThoriumReaction",
		"Label": ["ThoriumReaction", "researches"],
		"RequiredResearch": ["AdvancedReflection"],
		"Unlocks": [
			["FissionReactor" + r_dict, "ThoriumCell"],
			["Hand" + r_dict, "ThoriumCell"],
			["Hand" + r_dict, "Uranium233Cell"],
		],
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "PlutoniumReaction",
		"Label": ["PlutoniumReaction", "researches"],
		"RequiredResearch": ["ThoriumReaction"],
		"Unlocks": [
			["FissionReactor" + r_dict, "PlutoniumCell"],
			["Hand" + r_dict, "PlutoniumCell"],
		],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "PlutoniumReaction2",
		"Label": ["TwoWorldsFormat", "common", ["PlutoniumReaction", "researches"], ["II", "common"]],
		"RequiredResearch": ["PlutoniumReaction"],
		"Unlocks": [["FissionReactor" + r_dict, "PlutoniumCell2"]],
		
		
		"Levels": [5,5],
	})