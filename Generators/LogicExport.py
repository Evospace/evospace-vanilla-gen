from Common import *

logic_exports = [
    {
        "Name": "ChestExportInventory",
        "Enabled": True,
        "Label": ["ExportInventory", "ui"],
        "Tooltip": ["ExportInventoryTooltip", "ui"]
    },
    {
        "Name": "CrafterWorking",
        "UseSignal": True,
        "Signal": "W",
        "Enabled": False,
        "Label": ["ExportWorking", "ui"],
        "Tooltip": ["ExportWorkingTooltip", "ui"]
    },
    {
        "Name": "CrafterProgress",
        "UseSignal": True,
        "Signal": "P",
        "Enabled": False,
        "Label": ["ExportProgress", "ui"],
        "Tooltip": ["ExportProgressTooltip", "ui"]
    },
    {
        "Name": "CrafterInputInventory",
        "Enabled": False,
        "Label": ["ExportInputInventory", "ui"],
        "Tooltip": ["ExportInputInventoryTooltip", "ui"]
    },
    {
        "Name": "CrafterOutputInventory",
        "Enabled": False,
        "Label": ["ExportOutputInventory", "ui"],
        "Tooltip": ["ExportOutputInventoryTooltip", "ui"]
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