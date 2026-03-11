from Common import *

objects_array = []

objects_array.append({
    "Class": "StaticModifier",
    "Name": "DrillingRigProductivity",
    "Image": "T_Multitool",
    "Label": ["DrillingRigProductivity", "modifiers"]
})
objects_array.append({
    "Class": "StaticModifier",
    "Name": "PumpjackProductivity",
    "Image": "T_Multitool",
    "Label": ["PumpjackProductivity", "modifiers"]
})

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/modifiers.json", data)