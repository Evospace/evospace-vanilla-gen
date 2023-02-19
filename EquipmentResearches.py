from Common import *
from Materials import *


def append_equipment(xy, append_levels, researches):
    append_levels(
        {
            "class": static_research,
            "name": "Torch",
            "label_parts": [["Torch", "misc"]],
            "chapter": "Production",
            "required": ["Multitool"],
            "unlocks": [["Hand", "Torch"], ["Assembler", "Torch"]],
            "levels": [1, 1],
            "position": [xy[0] - 0, xy[1] - 1],
            "CostMul": 0.25,
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Multitool",
            "label_parts": [["Multitool", "parts"]],
            "chapter": "Production",
            "required": ["Smelting"],
            "unlocks": [["Hand", "%Material%Multitool"]],
            "levels": [1, 7],
            "position": [xy[0] - 0, xy[1] + 0],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Scanner",
            "label_parts": [["Scanner", "misc"]],
            "required": ["Multitool"],
            "unlocks": [["Hand", "Scanner"]],
            "position": [xy[0] - 1, xy[1] + 0],
            "chapter": "Production",
            "levels": [1, 1],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Steampack",
            "label_parts": [["Steampack", "misc"]],
            "required": ["Multitool"],
            "unlocks": [["Hand", "Steampack"]],
            "chapter": "Production",
            "position": [xy[0] - 1, xy[1] + 1],
            "levels": [1, 1],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Screwdriver",
            "label_parts": [["Screwdriver", "parts"]],
            "required": ["Multitool"],
            "unlocks": [["Hand", tier_material[1] + "Screwdriver"]],
            "position": [xy[0] - 0, xy[1] + 1],
            "chapter": "Production",
            "levels": [1, 1],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Flashlight",
            "label_parts": [["Flashlight", "misc"]],
            "required": ["Screwdriver"],
            "unlocks": [["Hand", "Flashlight"]],
            "position": [xy[0] - 0, xy[1] + 2],
            "chapter": "Production",
            "levels": [1, 1],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "Jetpack",
            "label_parts": [["Jetpack", "misc"]],
            "required": ["Steampack"],
            "unlocks": [["Hand", "Jetpack"]],
            "chapter": "Production",
            "position": [xy[0] - 1, xy[1] + 2],
            "levels": [1, 1],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "AdvancedJetpack",
            "label_parts": [["AdvancedJetpack", "misc"]],
            "required": ["Jetpack"],
            "unlocks": [["Hand", "AdvancedJetpack"]],
            "chapter": "Production",
            "position": [xy[0] - 1, xy[1] + 3],
            "levels": [3, 3],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "AntigravityUnit",
            "label_parts": [["AntigravityUnit", "misc"]],
            "required": ["AdvancedJetpack"],
            "unlocks": [["Hand", "AntigravityUnit"]],
            "chapter": "Production",
            "position": [xy[0] - 1, xy[1] + 4],
            "levels": [5, 5],
        }
    )
