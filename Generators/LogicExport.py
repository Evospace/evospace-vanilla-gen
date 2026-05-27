from Common import *

logic_exports = [
    {
        "Name": "Storage",
        "Enabled": True,
        "Label": ["Storage", "logic_export"],
        "Tooltip": ["StorageTooltip", "logic_export"]
    },
    {
        "Name": "Working",
        "UseSignal": True,
        "Signal": "W",
        "Enabled": False,
        "Label": ["Working", "logic_export"],
        "Tooltip": ["WorkingTooltip", "logic_export"]
    },
    {
        "Name": "Progress",
        "UseSignal": True,
        "Signal": "P",
        "Enabled": False,
        "Label": ["Progress", "logic_export"],
        "Tooltip": ["ProgressTooltip", "logic_export"]
    },
    {
        "Name": "TimePassed",
        "UseSignal": True,
        "Signal": "P",
        "Enabled": True,
        "Label": ["TimePassed", "logic_export"],
        "Tooltip": ["TimePassedTooltip", "logic_export"]
    },
    {
        "Name": "InputInventory",
        "Enabled": False,
        "Label": ["InputInventory", "logic_export"],
        "Tooltip": ["InputInventoryTooltip", "logic_export"]
    },
    {
        "Name": "OutputInventory",
        "Enabled": False,
        "Label": ["OutputInventory", "logic_export"],
        "Tooltip": ["OutputInventoryTooltip", "logic_export"]
    },
    {
        "Name": "SpotlightAimX",
        "UseSignal": True,
        "Signal": "X",
        "Enabled": False,
        "Label": ["SpotlightAimX", "logic_export"],
        "Tooltip": ["SpotlightAimXTooltip", "logic_export"]
    },
    {
        "Name": "SpotlightAimY",
        "UseSignal": True,
        "Signal": "Y",
        "Enabled": False,
        "Label": ["SpotlightAimY", "logic_export"],
        "Tooltip": ["SpotlightAimYTooltip", "logic_export"]
    },
    {
        "Name": "SpotlightColorR",
        "UseSignal": True,
        "Signal": "R",
        "Enabled": False,
        "Label": ["SpotlightColorR", "logic_export"],
        "Tooltip": ["SpotlightColorRTooltip", "logic_export"]
    },
    {
        "Name": "SpotlightColorG",
        "UseSignal": True,
        "Signal": "G",
        "Enabled": False,
        "Label": ["SpotlightColorG", "logic_export"],
        "Tooltip": ["SpotlightColorGTooltip", "logic_export"]
    },
    {
        "Name": "SpotlightColorB",
        "UseSignal": True,
        "Signal": "B",
        "Enabled": False,
        "Label": ["SpotlightColorB", "logic_export"],
        "Tooltip": ["SpotlightColorBTooltip", "logic_export"]
    }
]

objects_array = []
	
for logic_export in logic_exports:
    logic_export["Class"] = "LogicExportOption"

    objects_array.append(logic_export)


data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/logic_export.json", data)