from Common import *
from Materials import *

def append_nuclear(xy, append_levels, researches):
	append_levels({
		"Class": static_research,
		"Name": "ControlCell" + static_research,
		"LabelParts": [["ControlCell", "parts"]],
		"RequiredResearches": ["FissionReactor"+static_research],
		"Unlocks": [["Assembler" + base_recipe, "ControlCell"], ["Hand" + base_recipe, "ControlCell"],["FissionReactor" + base_recipe, "ControlCell"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] + 1, xy[1] + 0],
		"Levels": [5,5],
	})
	append_levels({
		"Class": static_research,
		"Name": "ReflectorCell" + static_research,
		"LabelParts": [["ReflectorCell", "parts"]],
		"RequiredResearches": ["ControlCell"+static_research],
		"Unlocks": [["Assembler" + base_recipe, "ReflectorCell"], ["Hand" + base_recipe, "ReflectorCell"],["FissionReactor" + base_recipe, "UraniumCell2"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] + 2, xy[1] + 0],
		"Levels": [5,5],
	})
	append_levels({
		"Class": static_research,
		"Name": "ReactionThrottling" + static_research,
		"LabelParts": [["ReactionThrottling", "researches"]],
		"RequiredResearches": ["ControlCell" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "ControlCell3"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] + 1, xy[1] + 1],
		"Levels": [5,5],
	})
	append_levels({
		"Class": static_research,
		"Name": "AdvancedReflection" + static_research,
		"LabelParts": [["AdvancedReflection", "researches"]],
		"RequiredResearches": ["ReflectorCell" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "UraniumCell3"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] + 2, xy[1] + 1],
		"Levels": [5,5],
	})
	append_levels({
		"Class": static_research,
		"Name": "AdvancedReflection2" + static_research,
		"LabelParts": [["AdvancedReflection", "researches"], ["II", "common"]],
		"RequiredResearches": ["AdvancedReflection" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "UraniumCell4"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] + 2, xy[1] + 2],
		"Levels": [5,5],
	})
	append_levels({
		"Class": static_research,
		"Name": "ThoriumReaction" + static_research,
		"LabelParts": [["ThoriumReaction", "researches"]],
		"RequiredResearches": ["AdvancedReflection" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "ThoriumCell"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] + 3, xy[1] + 0],
		"Levels": [5,5],
	})
	append_levels({
		"Class": static_research,
		"Name": "PlutoniumReaction" + static_research,
		"LabelParts": [["PlutoniumReaction", "researches"]],
		"RequiredResearches": ["ThoriumReaction" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "PlutoniumCell"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] + 4, xy[1] + 0],
		"Levels": [5,5],
	})
	append_levels({
		"Class": static_research,
		"Name": "PlutoniumReaction2" + static_research,
		"LabelParts": [["PlutoniumReaction", "researches"], ["II", "common"]],
		"RequiredResearches": ["PlutoniumReaction" + static_research],
		"Unlocks": [["FissionReactor" + base_recipe, "PlutoniumCell2"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] + 4, xy[1] + 1],
		"Levels": [5,5],
	})