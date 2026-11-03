from Common import *

ether = "Shortwave"

signals = [
	{"Name": "MorseBeacon", "Frequency": 3.512, "Bandwidth": 0.4, "Power": 0.6, "Carrier": 0.0, "Fading": 0.5, "Sound": "Radio/morse_beacon.wav"},
	{"Name": "Teletype", "Frequency": 3.945, "Bandwidth": 0.5, "Power": 0.5, "Carrier": 0.0, "Fading": 0.3, "Sound": "Radio/rtty.wav"},
	{"Name": "Buzzer", "Frequency": 4.625, "Bandwidth": 1.0, "Power": 0.9, "Carrier": 0.3, "Fading": 0.2, "Sound": "Radio/buzzer.wav"},
	{"Name": "TimeSignal", "Frequency": 5.0, "Bandwidth": 2.0, "Power": 0.8, "Carrier": 0.6, "Fading": 0.4, "Sound": "Radio/time_signal.wav"},
	{"Name": "NumbersStation", "Frequency": 6.84, "Bandwidth": 3.0, "Power": 0.7, "Carrier": 0.5, "Fading": 0.35, "Sound": "Radio/numbers_station.wav"},
	{"Name": "IntervalSignal", "Frequency": 7.33, "Bandwidth": 4.0, "Power": 0.6, "Carrier": 0.5, "Fading": 0.3, "Sound": "Radio/interval_signal.wav"},
	{"Name": "Pulsar", "Frequency": 7.905, "Bandwidth": 6.0, "Power": 0.35, "Carrier": 0.0, "Fading": 0.1, "Sound": "Radio/pulsar.wav"},
]

def cosmos(track):
	return "/Game/Music/Cosmos/" + track + "." + track

cosmos_call = "Radio/cosmos_call.wav"

cosmos_program = [
	cosmos("Cosmos_03"), 1,
	cosmos("Cosmos_05"), 3,
	cosmos("Cosmos_02"), 2,
	cosmos("Cosmos_01"), 1,
	cosmos_call, 2,
	cosmos("Cosmos_06"), 2,
	cosmos("Cosmos_07"), 2,
	cosmos("Cosmos_04"), 3,
	cosmos_call, 2,
]

def noise(track):
	return "Radio/Noise/" + track + ".wav"

interference = {
	"Static": {"Sound": noise("crackle"), "Level": 0.7},
	"Hum": {"Sound": noise("hum"), "Level": 0.6},
	"Woodpecker": {"Sound": noise("woodpecker"), "Level": 0.7},
	"Jammer": {"Sound": noise("jammer"), "Level": 0.6},
	"Whistlers": {"Sound": noise("whistler"), "Level": 0.4, "Fading": 0.7},
	"Storm": {"Sound": noise("storm"), "Level": 0.9, "Absorb": 0.3},
	"Blackout": {"Absorb": 0.95},
	"Aurora": {"Flutter": 0.8},
	"Drift": {"Drift": 1.5},
}

def place(name, band=None, every=None, lasts=None, **overrides):
	entry = {**interference[name], **overrides}
	if band:
		entry["Band"] = band
	if every:
		entry["Every"], entry["Lasts"] = every, lasts
	return entry

shortwave_interference = [
	place("Static", Level=0.25),
	place("Hum", [3.0, 3.4]),
	place("Storm", [4.15, 4.45], Level=0.6, Fading=0.4),
	place("Jammer", [5.3, 5.55]),
	place("Woodpecker", [6.2, 6.45], 600, 480),
	place("Whistlers", [7.55, 7.8]),
	place("Jammer", [6.836, 6.844], 1500, 60, Level=0.5),
	place("Storm", None, 2400, 40),
	place("Blackout", None, 3600, 90),
	place("Aurora", [5.5, 8.0], 2700, 90),
	place("Drift", [3.4, 5.3], 2100, 60),
]

objects_array = [{
	"Class": "StaticRadioEther",
	"Name": ether,
	"Band": [3.0, 8.0],
	"Noise": 0.3,
	"Interference": shortwave_interference,
}]

for signal in signals:
	objects_array.append({
		"Class": "StaticRadioSignal",
		"Ether": ether,
		**signal,
	})

objects_array.append({
	"Class": "StaticRadioSignal",
	"Name": "Cosmos",
	"Ether": ether,
	"Frequency": 5.975,
	"Bandwidth": 5.0,
	"Power": 0.8,
	"Carrier": 0.6,
	"Fading": 0.35,
	"Detune": -44.6144,
	"Program": cosmos_program,
})

write_file("Generated/Mixed/radio.json", {"Objects": objects_array})
