from Common import *
from Materials import *

def append_equipment(xy, append_levels, researches):
	append_levels({
		"Class": static_research,
		"Name": "Torch",
		"LabelParts": [["Torch", "misc"]],
		"Chapter": "Production",
		"RequiredResearches": ["Multitool"],
		"Unlocks": [["Hand", "Torch"],["Assembler", "Torch"]],
		"Levels": [1,1],
		"Position": [xy[0] - 0, xy[1] - 1],
		"CostMul":0.25,
	})
	append_levels({
		"Class": static_research,
		"Name": "Multitool",
		"LabelParts": [["Multitool", "parts"]],
		"Chapter": "Production",
		"RequiredResearches": ["Smelting"],
		"Unlocks": [["Hand", "%Material%Multitool"]],
		"Levels": [1,7],
		"Position": [xy[0] - 0, xy[1] + 0],
	})
	append_levels({
		"Class": static_research,
		"Name": "Scanner",
		"LabelParts": [["Scanner", "misc"]],
		"RequiredResearches": ["Multitool"],
		"Unlocks": [["Hand", "Scanner"]],
		"Position": [xy[0] - 1, xy[1] + 0],
		"Chapter": "Production",
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "Steampack",
		"LabelParts": [["Steampack", "misc"]],
		"RequiredResearches": ["Multitool"],
		"Unlocks": [["Hand", "Steampack"]],
		"Chapter": "Production",
		"Position": [xy[0] - 1, xy[1] + 1],
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "Screwdriver",
		"LabelParts": [["Screwdriver", "parts"]],
		"RequiredResearches": ["Multitool"],
		"Unlocks": [["Hand", tier_material[1] + "Screwdriver"]],
		"Position": [xy[0] - 0, xy[1] + 1],
		"Chapter": "Production",
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "Flashlight",
		"LabelParts": [["Flashlight", "misc"]],
		"RequiredResearches": ["Screwdriver"],
		"Unlocks": [["Hand", "Flashlight"]],
		"Position": [xy[0] - 0, xy[1] + 2],
		"Chapter": "Production",
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "Jetpack",
		"LabelParts": [["Jetpack", "misc"]],
		"RequiredResearches": ["Steampack"],
		"Unlocks": [["Hand", "Jetpack"]],
		"Chapter": "Production",
		"Position": [xy[0] - 1, xy[1] + 2],
		"Levels": [1,1],
	})
	append_levels({
		"Class": static_research,
		"Name": "AdvancedJetpack",
		"LabelParts": [["AdvancedJetpack", "misc"]],
		"RequiredResearches": ["Jetpack"],
		"Unlocks": [["Hand", "AdvancedJetpack"]],
		"Chapter": "Production",
		"Position": [xy[0] - 1, xy[1] + 3],
		"Levels": [3,3],
	})
	append_levels({
		"Class": static_research,
		"Name": "AntigravityUnit",
		"LabelParts": [["AntigravityUnit", "misc"]],
		"RequiredResearches": ["AdvancedJetpack"],
		"Unlocks": [["Hand", "AntigravityUnit"]],
		"Chapter": "Production",
		"Position": [xy[0] - 1, xy[1] + 4],
		"Levels": [5,5],
	})