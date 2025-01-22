from Common import *
from Materials import *

def append_nuclear(xy, append_levels, researches):
	append_levels({
		"Class": "StaticResearch",
		"Name": "ControlCell",
		"LabelParts": [["ControlCell", "parts"]],
		"RequiredResearch": ["FissionReactor"+static_research],
		"Unlocks": [["Assembler" + base_recipe, "ControlCell"], ["Hand" + base_recipe, "ControlCell"],["FissionReactor" + base_recipe, "ControlCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ReflectorCell",
		"LabelParts": [["ReflectorCell", "parts"]],
		"RequiredResearch": ["ControlCell"+static_research],
		"Unlocks": [["Assembler" + base_recipe, "ReflectorCell"], ["Hand" + base_recipe, "ReflectorCell"],["FissionReactor" + base_recipe, "UraniumCell2"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ReactionThrottling",
		"LabelParts": [["ReactionThrottling", "researches"]],
		"RequiredResearch": ["ControlCell"],
		"Unlocks": [["FissionReactor" + base_recipe, "ControlCell3"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedReflection",
		"LabelParts": [["AdvancedReflection", "researches"]],
		"RequiredResearch": ["ReflectorCell"],
		"Unlocks": [["FissionReactor" + base_recipe, "UraniumCell3"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedReflection2",
		"LabelParts": [["AdvancedReflection", "researches"], ["II", "common"]],
		"RequiredResearch": ["AdvancedReflection"],
		"Unlocks": [["FissionReactor" + base_recipe, "UraniumCell4"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ThoriumReaction",
		"LabelParts": [["ThoriumReaction", "researches"]],
		"RequiredResearch": ["AdvancedReflection"],
		"Unlocks": [["FissionReactor" + base_recipe, "ThoriumCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "PlutoniumReaction",
		"LabelParts": [["PlutoniumReaction", "researches"]],
		"RequiredResearch": ["ThoriumReaction"],
		"Unlocks": [["FissionReactor" + base_recipe, "PlutoniumCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "PlutoniumReaction2",
		"LabelParts": [["PlutoniumReaction", "researches"], ["II", "common"]],
		"RequiredResearch": ["PlutoniumReaction"],
		"Unlocks": [["FissionReactor" + base_recipe, "PlutoniumCell2"]],
		
		
		"Levels": [5,5],
	})