from Common import *

sounds = ["Siren", "Alarm", "Buzzer", "Beep", "Chime", "Horn"]

write_file("Generated/Mixed/speaker.json", {"Objects": [{
	"Class": "StaticSpeakerSound",
	"Name": name,
	"Label": [name, "ui"],
	"Sound": "Speaker/" + name.lower() + ".ogg",
} for name in sounds]})
