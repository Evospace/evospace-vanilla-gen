from Common import *

objects_array = []

objects_array.append({
    "Class": "StaticModifier",
    "Name": "DrillingRigProductivity",
    "Image": "T_DrillingRigProductivity",
    "Label": ["DrillingRigProductivity", "modifiers"]
})
objects_array.append({
    "Class": "StaticModifier",
    "Name": "PumpjackProductivity",
    "Image": "T_PumpjackProductivity",
    "Label": ["PumpjackProductivity", "modifiers"]
})

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/modifiers.json", data)