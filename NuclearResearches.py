from Common import *
from Materials import *


def append_nuclear(xy, append_levels, researches):
    append_levels(
        {
            "Class": static_research,
            "Name": "ControlCell",
            "LabelParts": [["ControlCell", "parts"]],
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
            "Class": static_research,
            "Name": "ReflectorCell",
            "LabelParts": [["ReflectorCell", "parts"]],
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
            "Class": static_research,
            "Name": "ReactionThrottling",
            "LabelParts": [["ReactionThrottling", "researches"]],
            "RequiredResearches": ["ControlCell"],
            "Unlocks": [["FissionReactor", "ControlCell3"]],
            "Chapter": "Production",
            "Position": [xy[0] + 1, xy[1] + 1],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "Class": static_research,
            "Name": "AdvancedReflection",
            "LabelParts": [["AdvancedReflection", "researches"]],
            "RequiredResearches": ["ReflectorCell"],
            "Unlocks": [["FissionReactor", "UraniumCell3"]],
            "Chapter": "Production",
            "Position": [xy[0] + 2, xy[1] + 1],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "Class": static_research,
            "Name": "AdvancedReflection2",
            "LabelParts": [["AdvancedReflection", "researches"], ["II", "common"]],
            "RequiredResearches": ["AdvancedReflection"],
            "Unlocks": [["FissionReactor", "UraniumCell4"]],
            "Chapter": "Production",
            "Position": [xy[0] + 2, xy[1] + 2],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "Class": static_research,
            "Name": "ThoriumReaction",
            "LabelParts": [["ThoriumReaction", "researches"]],
            "RequiredResearches": ["AdvancedReflection"],
            "Unlocks": [["FissionReactor", "ThoriumCell"]],
            "Chapter": "Production",
            "Position": [xy[0] + 3, xy[1] + 0],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "Class": static_research,
            "Name": "PlutoniumReaction",
            "LabelParts": [["PlutoniumReaction", "researches"]],
            "RequiredResearches": ["ThoriumReaction"],
            "Unlocks": [["FissionReactor", "PlutoniumCell"]],
            "Chapter": "Production",
            "Position": [xy[0] + 4, xy[1] + 0],
            "Levels": [5, 5],
        }
    )
    append_levels(
        {
            "Class": static_research,
            "Name": "PlutoniumReaction2",
            "LabelParts": [["PlutoniumReaction", "researches"], ["II", "common"]],
            "RequiredResearches": ["PlutoniumReaction"],
            "Unlocks": [["FissionReactor", "PlutoniumCell2"]],
            "Chapter": "Production",
            "Position": [xy[0] + 4, xy[1] + 1],
            "Levels": [5, 5],
        }
    )
