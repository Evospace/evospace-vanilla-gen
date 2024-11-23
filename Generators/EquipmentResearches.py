from Common import *
from Materials import *

def append_equipment(xy, append_levels, researches):
	append_levels({
		"Class": "StaticResearchModifier",
		"Name": "Multitool" + static_research,
		"LabelParts": [["Multitool", "parts"]],
		
		"Unlocks": [],
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
		
		
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Steampack" + static_research,
		"LabelParts": [["Steampack", "misc"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Steampack"]],
		
		
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "HighPressureSteampack" + static_research,
		"LabelParts": [["HighPressureSteampack", "misc"]],
		"RequiredResearches": ["Steampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "HighPressureSteampack"]],
		
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "HighCapacitySteampack" + static_research,
		"LabelParts": [["HighCapacitySteampack", "misc"]],
		"RequiredResearches": ["Steampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "HighCapacitySteampack"]],
		
		
		"Levels": [2,2],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedSteampack" + static_research,
		"LabelParts": [["AdvancedSteampack", "misc"]],
		"RequiredResearches": ["HighCapacitySteampack" + static_research, "HighPressureSteampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "AdvancedSteampack"]],
		
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Flashlight" + static_research,
		"LabelParts": [["Flashlight", "misc"]],
		"RequiredResearches": ["Multitool" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Flashlight"]],
		
		
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "Jetpack" + static_research,
		"LabelParts": [["Jetpack", "misc"]],
		"RequiredResearches": ["Steampack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "Jetpack"]],
		
		
		"Levels": [1,1],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AdvancedJetpack" + static_research,
		"LabelParts": [["AdvancedJetpack", "misc"]],
		"RequiredResearches": ["Jetpack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "AdvancedJetpack"]],
		
		
		"Levels": [3,3],
	})
	append_levels({
		"Class": "StaticResearch",
		"Name": "AntigravityUnit" + static_research,
		"LabelParts": [["AntigravityUnit", "misc"]],
		"RequiredResearches": ["AdvancedJetpack" + static_research],
		"Unlocks": [["Hand" + base_recipe, "AntigravityUnit"]],
		
		
		"Levels": [5,5],
	})