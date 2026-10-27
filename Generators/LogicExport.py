from Common import *

logic_exports = [
    {
        "Name": "Storage",
        "Enabled": True,
        "Label": ["Storage", "logic_export"],
        "Tooltip": ["StorageTooltip", "logic_export"]
    },
    {
        "Name": "Capacity",
        "UseSignal": True,
        "Signal": "C",
        "Enabled": False,
        "Label": ["Capacity", "logic_export"],
        "Tooltip": ["CapacityTooltip", "logic_export"]
    },
    {
        "Name": "Fill",
        "UseSignal": True,
        "Signal": "F",
        "Enabled": False,
        "Label": ["Fill", "logic_export"],
        "Tooltip": ["FillTooltip", "logic_export"]
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
        "Name": "Fuel",
        "UseSignal": True,
        "Signal": "F",
        "Enabled": True,
        "Label": ["Fuel", "logic_export"],
        "Tooltip": ["FuelTooltip", "logic_export"]
    },
    {
        "Name": "CargoFull",
        "UseSignal": True,
        "Signal": "L",
        "Enabled": True,
        "Label": ["CargoFull", "logic_export"],
        "Tooltip": ["CargoFullTooltip", "logic_export"]
    },
    {
        "Name": "CargoEmpty",
        "UseSignal": True,
        "Signal": "E",
        "Enabled": True,
        "Label": ["CargoEmpty", "logic_export"],
        "Tooltip": ["CargoEmptyTooltip", "logic_export"]
    },
    {
        "Name": "Inactivity",
        "UseSignal": True,
        "Signal": "I",
        "Enabled": True,
        "Label": ["Inactivity", "logic_export"],
        "Tooltip": ["InactivityTooltip", "logic_export"]
    },
    {
        "Name": "SignalStop",
        "UseSignal": True,
        "Signal": "R",
        "Enabled": True,
        "Label": ["SignalStop", "logic_export"],
        "Tooltip": ["SignalStopTooltip", "logic_export"]
    },
    {
        "Name": "SignalCaution",
        "UseSignal": True,
        "Signal": "Y",
        "Enabled": True,
        "Label": ["SignalCaution", "logic_export"],
        "Tooltip": ["SignalCautionTooltip", "logic_export"]
    },
    {
        "Name": "SignalGo",
        "UseSignal": True,
        "Signal": "G",
        "Enabled": True,
        "Label": ["SignalGo", "logic_export"],
        "Tooltip": ["SignalGoTooltip", "logic_export"]
    },
    {
        "Name": "Pressed",
        "UseSignal": True,
        "Signal": "B",
        "Enabled": True,
        "Label": ["Pressed", "logic_export"],
        "Tooltip": ["PressedTooltip", "logic_export"]
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