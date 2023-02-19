from Common import *
from Materials import *


def append_nuclear(xy, append_levels, researches):
    append_levels(
        {
            "class": static_research,
            "name": "ControlCell",
            "label_parts": [["ControlCell", "parts"]],
            "required": ["FissionReactor"],
            "unlocks": [
                ["Assembler", "ControlCell"],
                ["Hand", "ControlCell"],
                ["FissionReactor", "ControlCell"],
            ],
            "chapter": "Production",
            "position": [xy[0] + 1, xy[1] + 0],
            "levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "ReflectorCell",
            "label_parts": [["ReflectorCell", "parts"]],
            "required": ["ControlCell"],
            "unlocks": [
                ["Assembler", "ReflectorCell"],
                ["Hand", "ReflectorCell"],
                ["FissionReactor", "UraniumCell2"],
            ],
            "chapter": "Production",
            "position": [xy[0] + 2, xy[1] + 0],
            "levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "ReactionThrottling",
            "label_parts": [["ReactionThrottling", "researches"]],
            "required": ["ControlCell"],
            "unlocks": [["FissionReactor", "ControlCell3"]],
            "chapter": "Production",
            "position": [xy[0] + 1, xy[1] + 1],
            "levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "AdvancedReflection",
            "label_parts": [["AdvancedReflection", "researches"]],
            "required": ["ReflectorCell"],
            "unlocks": [["FissionReactor", "UraniumCell3"]],
            "chapter": "Production",
            "position": [xy[0] + 2, xy[1] + 1],
            "levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "AdvancedReflection2",
            "label_parts": [["AdvancedReflection", "researches"], ["II", "common"]],
            "required": ["AdvancedReflection"],
            "unlocks": [["FissionReactor", "UraniumCell4"]],
            "chapter": "Production",
            "position": [xy[0] + 2, xy[1] + 2],
            "levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "ThoriumReaction",
            "label_parts": [["ThoriumReaction", "researches"]],
            "required": ["AdvancedReflection"],
            "unlocks": [["FissionReactor", "ThoriumCell"]],
            "chapter": "Production",
            "position": [xy[0] + 3, xy[1] + 0],
            "levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "PlutoniumReaction",
            "label_parts": [["PlutoniumReaction", "researches"]],
            "required": ["ThoriumReaction"],
            "unlocks": [["FissionReactor", "PlutoniumCell"]],
            "chapter": "Production",
            "position": [xy[0] + 4, xy[1] + 0],
            "levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "PlutoniumReaction2",
            "label_parts": [["PlutoniumReaction", "researches"], ["II", "common"]],
            "required": ["PlutoniumReaction"],
            "unlocks": [["FissionReactor", "PlutoniumCell2"]],
            "chapter": "Production",
            "position": [xy[0] + 4, xy[1] + 1],
            "levels": [5, 5],
        }
    )
