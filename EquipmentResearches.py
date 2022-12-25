from Common import *
from Materials import *


def append_equipment(xy, append_levels, researches):
    append_levels(
        {
            "class": static_research,
            "name": "Torch",
            "label_parts": [["Torch", "misc"]],
            "Chapter": "Production",
            "RequiredResearches": ["Multitool"],
            "Unlocks": [["Hand", "Torch"], ["Assembler", "Torch"]],
            "Levels": [1, 1],
            "Position": [xy[0] - 0, xy[1] - 1],
            "CostMul": 0.25,
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Multitool",
            "label_parts": [["Multitool", "parts"]],
            "Chapter": "Production",
            "RequiredResearches": ["Smelting"],
            "Unlocks": [["Hand", "%Material%Multitool"]],
            "Levels": [1, 7],
            "Position": [xy[0] - 0, xy[1] + 0],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Scanner",
            "label_parts": [["Scanner", "misc"]],
            "RequiredResearches": ["Multitool"],
            "Unlocks": [["Hand", "Scanner"]],
            "Position": [xy[0] - 1, xy[1] + 0],
            "Chapter": "Production",
            "Levels": [1, 1],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Steampack",
            "label_parts": [["Steampack", "misc"]],
            "RequiredResearches": ["Multitool"],
            "Unlocks": [["Hand", "Steampack"]],
            "Chapter": "Production",
            "Position": [xy[0] - 1, xy[1] + 1],
            "Levels": [1, 1],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Screwdriver",
            "label_parts": [["Screwdriver", "parts"]],
            "RequiredResearches": ["Multitool"],
            "Unlocks": [["Hand", tier_material[1] + "Screwdriver"]],
            "Position": [xy[0] - 0, xy[1] + 1],
            "Chapter": "Production",
            "Levels": [1, 1],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Flashlight",
            "label_parts": [["Flashlight", "misc"]],
            "RequiredResearches": ["Screwdriver"],
            "Unlocks": [["Hand", "Flashlight"]],
            "Position": [xy[0] - 0, xy[1] + 2],
            "Chapter": "Production",
            "Levels": [1, 1],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Jetpack",
            "label_parts": [["Jetpack", "misc"]],
            "RequiredResearches": ["Steampack"],
            "Unlocks": [["Hand", "Jetpack"]],
            "Chapter": "Production",
            "Position": [xy[0] - 1, xy[1] + 2],
            "Levels": [1, 1],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "AdvancedJetpack",
            "label_parts": [["AdvancedJetpack", "misc"]],
            "RequiredResearches": ["Jetpack"],
            "Unlocks": [["Hand", "AdvancedJetpack"]],
            "Chapter": "Production",
            "Position": [xy[0] - 1, xy[1] + 3],
            "Levels": [3, 3],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "AntigravityUnit",
            "label_parts": [["AntigravityUnit", "misc"]],
            "RequiredResearches": ["AdvancedJetpack"],
            "Unlocks": [["Hand", "AntigravityUnit"]],
            "Chapter": "Production",
            "Position": [xy[0] - 1, xy[1] + 4],
            "Levels": [5, 5],
        }
    )
