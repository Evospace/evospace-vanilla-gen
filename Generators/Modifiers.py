from Common import *

objects_array = []
cvs = []

objects_array.append({
    "Class": "StaticModifier",
    "Name": "ToolLevelStaticModifier",
    "Image": "T_Multitool",
    "Label": ["Multitool", "parts"],
    "Description": ["MultitoolSpeedDescription", "modifiers"]
})
cvs.append(["MultitoolDescription", ""])

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/modifiers.json", data)
write_file("Loc/source/modifiers.json", cvs)