from Common import *
from Materials import *


def append_nuclear(xy, append_levels, researches):
    append_levels(
        {
            "class": static_research,
            "name": "ControlCell",
            "label_parts": [["ControlCell", "parts"]],
            "RequiredResearches": ["FissionReactor"],
            "Unlocks": [
                ["Assembler", "ControlCell"],
                ["Hand", "ControlCell"],
                ["FissionReactor", "ControlCell"],
            ],
            "Chapter": "Production",
            "Position": [xy[0] + 1, xy[1] + 0],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "ReflectorCell",
            "label_parts": [["ReflectorCell", "parts"]],
            "RequiredResearches": ["ControlCell"],
            "Unlocks": [
                ["Assembler", "ReflectorCell"],
                ["Hand", "ReflectorCell"],
                ["FissionReactor", "UraniumCell2"],
            ],
            "Chapter": "Production",
            "Position": [xy[0] + 2, xy[1] + 0],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "ReactionThrottling",
            "label_parts": [["ReactionThrottling", "researches"]],
            "RequiredResearches": ["ControlCell"],
            "Unlocks": [["FissionReactor", "ControlCell3"]],
            "Chapter": "Production",
            "Position": [xy[0] + 1, xy[1] + 1],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "AdvancedReflection",
            "label_parts": [["AdvancedReflection", "researches"]],
            "RequiredResearches": ["ReflectorCell"],
            "Unlocks": [["FissionReactor", "UraniumCell3"]],
            "Chapter": "Production",
            "Position": [xy[0] + 2, xy[1] + 1],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "AdvancedReflection2",
            "label_parts": [["AdvancedReflection", "researches"], ["II", "common"]],
            "RequiredResearches": ["AdvancedReflection"],
            "Unlocks": [["FissionReactor", "UraniumCell4"]],
            "Chapter": "Production",
            "Position": [xy[0] + 2, xy[1] + 2],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "ThoriumReaction",
            "label_parts": [["ThoriumReaction", "researches"]],
            "RequiredResearches": ["AdvancedReflection"],
            "Unlocks": [["FissionReactor", "ThoriumCell"]],
            "Chapter": "Production",
            "Position": [xy[0] + 3, xy[1] + 0],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "PlutoniumReaction",
            "label_parts": [["PlutoniumReaction", "researches"]],
            "RequiredResearches": ["ThoriumReaction"],
            "Unlocks": [["FissionReactor", "PlutoniumCell"]],
            "Chapter": "Production",
            "Position": [xy[0] + 4, xy[1] + 0],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "class": static_research,
            "name": "PlutoniumReaction2",
            "label_parts": [["PlutoniumReaction", "researches"], ["II", "common"]],
            "RequiredResearches": ["PlutoniumReaction"],
            "Unlocks": [["FissionReactor", "PlutoniumCell2"]],
            "Chapter": "Production",
            "Position": [xy[0] + 4, xy[1] + 1],
            "Levels": [5, 5],
        }
    )
