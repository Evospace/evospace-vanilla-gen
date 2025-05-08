from Common import *
from Materials import *

def append_nuclear(xy, append_levels, researches):
	append_levels({
		"Class": research_recipe,
		"Name": "ControlCell",
		"LabelParts": [["ControlCell", "parts"]],
		"RequiredResearch": ["FissionReactor"],
		"Unlocks": [[assembler_r_dict, "ControlCell"], ["Hand" + r_dict, "ControlCell"],["FissionReactor" + r_dict, "ControlCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "ReflectorCell",
		"LabelParts": [["ReflectorCell", "parts"]],
		"RequiredResearch": ["ControlCell"],
		"Unlocks": [[assembler_r_dict, "ReflectorCell"], ["Hand" + r_dict, "ReflectorCell"],["FissionReactor" + r_dict, "UraniumCell2"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "ReactionThrottling",
		"LabelParts": [["ReactionThrottling", "researches"]],
		"RequiredResearch": ["ControlCell"],
		"Unlocks": [["FissionReactor" + r_dict, "ControlCell3"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "AdvancedReflection",
		"LabelParts": [["AdvancedReflection", "researches"]],
		"RequiredResearch": ["ReflectorCell"],
		"Unlocks": [["FissionReactor" + r_dict, "UraniumCell3"]],
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "AdvancedReflection2",
		"LabelParts": [["AdvancedReflection", "researches"], ["II", "common"]],
		"RequiredResearch": ["AdvancedReflection"],
		"Unlocks": [["FissionReactor" + r_dict, "UraniumCell4"]],
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "ThoriumReaction",
		"LabelParts": [["ThoriumReaction", "researches"]],
		"RequiredResearch": ["AdvancedReflection"],
		"Unlocks": [["FissionReactor" + r_dict, "ThoriumCell"]],
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "PlutoniumReaction",
		"LabelParts": [["PlutoniumReaction", "researches"]],
		"RequiredResearch": ["ThoriumReaction"],
		"Unlocks": [["FissionReactor" + r_dict, "PlutoniumCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": research_recipe,
		"Name": "PlutoniumReaction2",
		"LabelParts": [["PlutoniumReaction", "researches"], ["II", "common"]],
		"RequiredResearch": ["PlutoniumReaction"],
		"Unlocks": [["FissionReactor" + r_dict, "PlutoniumCell2"]],
		
		
		"Levels": [5,5],
	})