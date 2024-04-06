from Common import *
from Materials import *

def append_equipment(xy, append_levels, researches):
	append_levels({
		"Class": "StaticResearchToolUnlock",
		"Name": "Torch" + static_research,
		"LabelParts": [["Torch", "misc"]],
		"Chapter": "Production"+static_chapter,
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Torch"],["Assembler" + base_recipe, "Torch"]],
		"Levels": [1,1],
		"Position": [xy[0] - 0, xy[1] - 1],
		"CostMul":0.25,
	})
	append_levels({
		"Class": "StaticResearchToolUnlock",
		"Name": "Multitool" + static_research,
		"LabelParts": [["Multitool", "parts"]],
		"Chapter": "Production"+static_chapter,
		"RequiredResearches": ["Smelting" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Multitool"]],
		"Levels": [1,1],
		"Position": [xy[0] - 0, xy[1] + 0],
	})
	append_levels({
		"Class": "StaticResearchToolUnlock",
		"Name": "Scanner" + static_research,
		"LabelParts": [["Scanner", "misc"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Scanner"]],
		"Position": [xy[0] - 1, xy[1] + 0],
		"Chapter": "Production" + static_chapter,
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "Steampack" + static_research,
		"LabelParts": [["Steampack", "misc"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Steampack"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 1, xy[1] + 1],
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "HighPressureSteampack" + static_research,
		"LabelParts": [["HighPressureSteampack", "misc"]],
		"RequiredResearches": ["Steampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "HighPressureSteampack"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 2, xy[1] + 1],
		"Levels": [2,2],
	})
	append_levels({
		"Class": static_research,
		"Name": "HighCapacitySteampack" + static_research,
		"LabelParts": [["HighCapacitySteampack", "misc"]],
		"RequiredResearches": ["Steampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "HighCapacitySteampack"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 2, xy[1] + 2],
		"Levels": [2,2],
	})
	append_levels({
		"Class": static_research,
		"Name": "AdvancedSteampack" + static_research,
		"LabelParts": [["AdvancedSteampack", "misc"]],
		"RequiredResearches": ["HighCapacitySteampack" + static_research, "HighPressureSteampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "AdvancedSteampack"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 3, xy[1] + 2],
		"Levels": [3,3],
	})
	append_levels({
		"Class": static_research,
		"Name": "Flashlight" + static_research,
		"LabelParts": [["Flashlight", "misc"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Flashlight"]],
		"Position": [xy[0] - 0, xy[1] + 2],
		"Chapter": "Production" + static_chapter,
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "Jetpack" + static_research,
		"LabelParts": [["Jetpack", "misc"]],
		"RequiredResearches": ["Steampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Jetpack"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 1, xy[1] + 2],
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "AdvancedJetpack" + static_research,
		"LabelParts": [["AdvancedJetpack", "misc"]],
		"RequiredResearches": ["Jetpack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "AdvancedJetpack"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 1, xy[1] + 3],
		"Levels": [3,3],
	})
	append_levels({
		"Class": static_research,
		"Name": "AntigravityUnit" + static_research,
		"LabelParts": [["AntigravityUnit", "misc"]],
		"RequiredResearches": ["AdvancedJetpack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "AntigravityUnit"]],
		"Chapter": "Production" + static_chapter,
		"Position": [xy[0] - 1, xy[1] + 4],
		"Levels": [5,5],
	})