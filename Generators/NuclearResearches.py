from Common import *
from Materials import *

def append_nuclear(xy, append_levels, researches):
	append_levels({
		"Class": "StaticResearch",
		"Name": "ControlCell" + static_research,
		"LabelParts": [["ControlCell", "parts"]],
		"RequiredResearch": ["FissionReactor"+static_research],
		"Unlocks": [["Assembler" + base_recipe, "ControlCell"], ["Hand" + base_recipe, "ControlCell"],["FissionReactor" + base_recipe, "ControlCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ReflectorCell" + static_research,
		"LabelParts": [["ReflectorCell", "parts"]],
		"RequiredResearch": ["ControlCell"+static_research],
		"Unlocks": [["Assembler" + base_recipe, "ReflectorCell"], ["Hand" + base_recipe, "ReflectorCell"],["FissionReactor" + base_recipe, "UraniumCell2"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ReactionThrottling" + static_research,
		"LabelParts": [["ReactionThrottling", "researches"]],
		"RequiredResearch": ["ControlCell" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "ControlCell3"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedReflection" + static_research,
		"LabelParts": [["AdvancedReflection", "researches"]],
		"RequiredResearch": ["ReflectorCell" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "UraniumCell3"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedReflection2" + static_research,
		"LabelParts": [["AdvancedReflection", "researches"], ["II", "common"]],
		"RequiredResearch": ["AdvancedReflection" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "UraniumCell4"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ThoriumReaction" + static_research,
		"LabelParts": [["ThoriumReaction", "researches"]],
		"RequiredResearch": ["AdvancedReflection" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "ThoriumCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "PlutoniumReaction" + static_research,
		"LabelParts": [["PlutoniumReaction", "researches"]],
		"RequiredResearch": ["ThoriumReaction" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "PlutoniumCell"]],
		
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "PlutoniumReaction2" + static_research,
		"LabelParts": [["PlutoniumReaction", "researches"], ["II", "common"]],
		"RequiredResearch": ["PlutoniumReaction" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "PlutoniumCell2"]],
		
		
		"Levels": [5,5],
	})