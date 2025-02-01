from Common import *
from Materials import *

def append_nuclear(xy, append_levels, researches):
	append_levels({
		"Class": "StaticResearch",
		"Name": "ControlCell",
		"LabelParts": [["ControlCell", "parts"]],
		"RequiredResearch": ["FissionReactor"+static_research],
		"Unlocks": [["Assembler" + r_dict, "ControlCell"], ["Hand" + r_dict, "ControlCell"],["FissionReactor" + r_dict, "ControlCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ReflectorCell",
		"LabelParts": [["ReflectorCell", "parts"]],
		"RequiredResearch": ["ControlCell"+static_research],
		"Unlocks": [["Assembler" + r_dict, "ReflectorCell"], ["Hand" + r_dict, "ReflectorCell"],["FissionReactor" + r_dict, "UraniumCell2"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ReactionThrottling",
		"LabelParts": [["ReactionThrottling", "researches"]],
		"RequiredResearch": ["ControlCell"],
		"Unlocks": [["FissionReactor" + r_dict, "ControlCell3"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedReflection",
		"LabelParts": [["AdvancedReflection", "researches"]],
		"RequiredResearch": ["ReflectorCell"],
		"Unlocks": [["FissionReactor" + r_dict, "UraniumCell3"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedReflection2",
		"LabelParts": [["AdvancedReflection", "researches"], ["II", "common"]],
		"RequiredResearch": ["AdvancedReflection"],
		"Unlocks": [["FissionReactor" + r_dict, "UraniumCell4"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ThoriumReaction",
		"LabelParts": [["ThoriumReaction", "researches"]],
		"RequiredResearch": ["AdvancedReflection"],
		"Unlocks": [["FissionReactor" + r_dict, "ThoriumCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "PlutoniumReaction",
		"LabelParts": [["PlutoniumReaction", "researches"]],
		"RequiredResearch": ["ThoriumReaction"],
		"Unlocks": [["FissionReactor" + r_dict, "PlutoniumCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "PlutoniumReaction2",
		"LabelParts": [["PlutoniumReaction", "researches"], ["II", "common"]],
		"RequiredResearch": ["PlutoniumReaction"],
		"Unlocks": [["FissionReactor" + r_dict, "PlutoniumCell2"]],
		
		
		"Levels": [5,5],
	})