from Common import *

objects_array = [{
	"Class": "StaticItem",
	"Name": "Floppy",
	"Label": ["Floppy", "parts"],
	"Image": "T_Floppy",
	"StackSize": 1,
	"Category": "Network",
}]

floppies = [
	{"Name": "FloppyWireMonitor", "Label": "WIRE MONITOR", "Source": "Floppies/monitor.asm"},
	{"Name": "FloppySnake", "Label": "SNAKE", "Source": "Floppies/snake.asm"},
	{"Name": "FloppyFieldLog", "Label": "FIELD LOG", "Source": "Floppies/log.asm", "Sealed": True},
]

for floppy in floppies:
	objects_array.append({
		"Class": "StaticFloppy",
		"Name": floppy["Name"],
		"Label": floppy["Label"],
		"Source": floppy["Source"],
		"Locked": True,
		"Sealed": floppy.get("Sealed", False),
	})

write_file("Generated/Mixed/floppies.json", {"Objects": objects_array})
