from Common import *

logic_exports = [
    {
        "Name": "ChestExportInventory",
        "Enabled": True,
        "Label": ["ExportInventory", "ui"],
        "Tooltip": ["ExportInventoryTooltip", "ui"]
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