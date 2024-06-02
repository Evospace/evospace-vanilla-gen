from Common import *
from Materials import *

def append_nuclear(xy, append_levels, researches):
	append_levels({
		"Class": "StaticResearch",
		"Name": "ControlCell" + static_research,
		"LabelParts": [["ControlCell", "parts"]],
		"RequiredResearches": ["FissionReactor"+static_research],
		"Unlocks": [["Assembler" + base_recipe, "ControlCell"], ["Hand" + base_recipe, "ControlCell"],["FissionReactor" + base_recipe, "ControlCell"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ReflectorCell" + static_research,
		"LabelParts": [["ReflectorCell", "parts"]],
		"RequiredResearches": ["ControlCell"+static_research],
		"Unlocks": [["Assembler" + base_recipe, "ReflectorCell"], ["Hand" + base_recipe, "ReflectorCell"],["FissionReactor" + base_recipe, "UraniumCell2"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ReactionThrottling" + static_research,
		"LabelParts": [["ReactionThrottling", "researches"]],
		"RequiredResearches": ["ControlCell" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "ControlCell3"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedReflection" + static_research,
		"LabelParts": [["AdvancedReflection", "researches"]],
		"RequiredResearches": ["ReflectorCell" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "UraniumCell3"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedReflection2" + static_research,
		"LabelParts": [["AdvancedReflection", "researches"], ["II", "common"]],
		"RequiredResearches": ["AdvancedReflection" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "UraniumCell4"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "ThoriumReaction" + static_research,
		"LabelParts": [["ThoriumReaction", "researches"]],
		"RequiredResearches": ["AdvancedReflection" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "ThoriumCell"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "PlutoniumReaction" + static_research,
		"LabelParts": [["PlutoniumReaction", "researches"]],
		"RequiredResearches": ["ThoriumReaction" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "PlutoniumCell"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [5,5],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "PlutoniumReaction2" + static_research,
		"LabelParts": [["PlutoniumReaction", "researches"], ["II", "common"]],
		"RequiredResearches": ["PlutoniumReaction" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "PlutoniumCell2"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [5,5],
	})