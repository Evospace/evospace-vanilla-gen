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

music = [
	("CelestialSerenity", 3.255),
	("DowntempoNeon", 4.875),
	("FactoryMustGrow", 5.975),
	("Classic", 6.07),
	("CosmicEchoes", 7.39),
]

objects_array = [{
	"Class": "StaticRadioEther",
	"Name": ether,
	"Band": [3.0, 8.0],
	"Noise": 0.3,
}]

for signal in signals:
	objects_array.append({
		"Class": "StaticRadioSignal",
		"Ether": ether,
		**signal,
	})

for key, frequency in music:
	objects_array.append({
		"Class": "StaticRadioSignal",
		"Name": "Music" + key,
		"Ether": ether,
		"Frequency": frequency,
		"Bandwidth": 5.0,
		"Power": 0.8,
		"Carrier": 0.6,
		"Fading": 0.35,
		"Sound": "Radio/Music/" + key + ".ogg",
	})

write_file("Generated/Mixed/radio.json", {"Objects": objects_array})
