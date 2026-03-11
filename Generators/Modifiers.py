from Common import *

objects_array = []

objects_array.append({
    "Class": "StaticModifier",
    "Name": "DrillingRigProductivityStaticModifier",
    "Image": "T_Multitool",
    "Label": ["DrillingRigProductivity", "modifiers"],
    "Description": ["DrillingRigProductivityDescription", "modifiers"]
})
objects_array.append({
    "Class": "StaticModifier",
    "Name": "PumpjackProductivityStaticModifier",
    "Image": "T_Multitool",
    "Label": ["PumpjackProductivity", "modifiers"],
    "Description": ["PumpjackProductivityDescription", "modifiers"]
})

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/modifiers.json", data)