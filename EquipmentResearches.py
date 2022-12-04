from Common import *
from Materials import *

def append_equipment(xy, append_levels, researches):
	append_levels({
		"Class": static_research,
		"Name": "Torch" + static_research,
		"LabelParts": [["Torch", "misc"]],
		"Chapter": "Production"+static_chapter,
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + recipe_dictionary, "Torch"],["Assembler" + recipe_dictionary, "Torch"]],
		"Levels": [1,1],
		"Position": [xy[0] - 0, xy[1] - 1],
		"CostMul":0.25,
	})
	append_levels({
		"Class": static_research,
		"Name": "Multitool" + static_research,
		"LabelParts": [["Multitool", "parts"]],
		"Chapter": "Production"+static_chapter,
		"RequiredResearches": ["Smelting" + static_research],
		"Unlocks": [["Hand" + recipe_dictionary, "%Material%Multitool"]],
		"Levels": [1,7],
		"Position": [xy[0] - 0, xy[1] + 0],
	})
	append_levels({
		"Class": static_research,
		"Name": "Scanner" + static_research,
		"LabelParts": [["Scanner", "misc"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + recipe_dictionary, "Scanner"]],
		"Position": [xy[0] - 1, xy[1] + 0],
		"Chapter": "Production" + static_chapter,
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "Steampack" + static_research,
		"LabelParts": [["Steampack", "misc"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + recipe_dictionary, "Steampack"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 1, xy[1] + 1],
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "Screwdriver" + static_research,
		"LabelParts": [["Screwdriver", "parts"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + recipe_dictionary, tier_material[1] + "Screwdriver"]],
		"Position": [xy[0] - 0, xy[1] + 1],
		"Chapter": "Production" + static_chapter,
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "Flashlight" + static_research,
		"LabelParts": [["Flashlight", "misc"]],
		"RequiredResearches": ["Screwdriver" + static_research],
		"Unlocks": [["Hand" + recipe_dictionary, "Flashlight"]],
		"Position": [xy[0] - 0, xy[1] + 2],
		"Chapter": "Production" + static_chapter,
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "Jetpack" + static_research,
		"LabelParts": [["Jetpack", "misc"]],
		"RequiredResearches": ["Steampack" + static_research],
		"Unlocks": [["Hand" + recipe_dictionary, "Jetpack"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 1, xy[1] + 2],
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "AdvancedJetpack" + static_research,
		"LabelParts": [["AdvancedJetpack", "misc"]],
		"RequiredResearches": ["Jetpack" + static_research],
		"Unlocks": [["Hand" + recipe_dictionary, "AdvancedJetpack"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 1, xy[1] + 3],
		"Levels": [3,3],
	})
	append_levels({
		"Class": static_research,
		"Name": "AntigravityUnit" + static_research,
		"LabelParts": [["AntigravityUnit", "misc"]],
		"RequiredResearches": ["AdvancedJetpack" + static_research],
		"Unlocks": [["Hand" + recipe_dictionary, "AntigravityUnit"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 1, xy[1] + 4],
		"Levels": [5,5],
	})