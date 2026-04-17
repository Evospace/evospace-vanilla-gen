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