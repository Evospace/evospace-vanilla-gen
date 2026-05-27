from Common import *

logic_imports = [
    {
        "Name": "Working",
        "UseSignal": True,
        "Signal": "W",
        "Enabled": True,
        "Label": ["Working", "logic_import"],
        "Tooltip": ["WorkingTooltip", "logic_import"]
    },
    {
        "Name": "SpotlightAimX",
        "UseSignal": True,
        "Signal": "X",
        "Enabled": False,
        "Label": ["SpotlightAimX", "logic_import"],
        "Tooltip": ["SpotlightAimXTooltip", "logic_import"]
    },
    {
        "Name": "SpotlightAimY",
        "UseSignal": True,
        "Signal": "Y",
        "Enabled": False,
        "Label": ["SpotlightAimY", "logic_import"],
        "Tooltip": ["SpotlightAimYTooltip", "logic_import"]
    },
    {
        "Name": "SpotlightColorR",
        "UseSignal": True,
        "Signal": "R",
        "Enabled": False,
        "Label": ["SpotlightColorR", "logic_import"],
        "Tooltip": ["SpotlightColorRTooltip", "logic_import"]
    },
    {
        "Name": "SpotlightColorG",
        "UseSignal": True,
        "Signal": "G",
        "Enabled": False,
        "Label": ["SpotlightColorG", "logic_import"],
        "Tooltip": ["SpotlightColorGTooltip", "logic_import"]
    },
    {
        "Name": "SpotlightColorB",
        "UseSignal": True,
        "Signal": "B",
        "Enabled": False,
        "Label": ["SpotlightColorB", "logic_import"],
        "Tooltip": ["SpotlightColorBTooltip", "logic_import"]
    }
]

objects_array = []

for logic_import in logic_imports:
    logic_import["Class"] = "LogicImportOption"
    objects_array.append(logic_import)

data = {
    "Objects": objects_array
}

write_file("Generated/Mixed/logic_import.json", data)
