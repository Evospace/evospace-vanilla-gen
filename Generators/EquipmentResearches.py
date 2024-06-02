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
		
		"CostMul":0.25,
	})
	append_levels({
		"Class": "StaticResearchModifier",
		"Name": "Multitool" + static_research,
		"LabelParts": [["Multitool", "parts"]],
		"Chapter": "Production"+static_chapter,
		"RequiredResearches": ["Smelting" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Multitool"]],
		"Levels": [1,10],
		
		"Image": "T_Multitool",
		"Modifier": "ToolLevelStaticModifier",
		"BonusValue": 1.0
	})
	append_levels({
		"Class": "StaticResearchToolUnlock",
		"Name": "Scanner" + static_research,
		"LabelParts": [["Scanner", "misc"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Scanner"]],
		
		"Chapter": "Production" + static_chapter,
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Steampack" + static_research,
		"LabelParts": [["Steampack", "misc"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Steampack"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "HighPressureSteampack" + static_research,
		"LabelParts": [["HighPressureSteampack", "misc"]],
		"RequiredResearches": ["Steampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "HighPressureSteampack"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "HighCapacitySteampack" + static_research,
		"LabelParts": [["HighCapacitySteampack", "misc"]],
		"RequiredResearches": ["Steampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "HighCapacitySteampack"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedSteampack" + static_research,
		"LabelParts": [["AdvancedSteampack", "misc"]],
		"RequiredResearches": ["HighCapacitySteampack" + static_research, "HighPressureSteampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "AdvancedSteampack"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Flashlight" + static_research,
		"LabelParts": [["Flashlight", "misc"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Flashlight"]],
		
		"Chapter": "Production" + static_chapter,
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Jetpack" + static_research,
		"LabelParts": [["Jetpack", "misc"]],
		"RequiredResearches": ["Steampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Jetpack"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedJetpack" + static_research,
		"LabelParts": [["AdvancedJetpack", "misc"]],
		"RequiredResearches": ["Jetpack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "AdvancedJetpack"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AntigravityUnit" + static_research,
		"LabelParts": [["AntigravityUnit", "misc"]],
		"RequiredResearches": ["AdvancedJetpack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "AntigravityUnit"]],
		"Chapter": "Production" + static_chapter,
		
		"Levels": [5,5],
	})