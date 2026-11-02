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
	cosmos("Frozen_Echoes"), 1,
	cosmos("Ppmp_Aah_Echoes"), 3,
	cosmos("Echoes_of_the_Unknown"), 2,
	cosmos("Cosmic_Echoes"), 1,
	cosmos_call, 2,
	cosmos("Starlight_Voyager"), 2,
	cosmos("Tidim_Echoes"), 2,
	cosmos("Pew_Pew_Echoes"), 3,
	cosmos_call, 2,
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

objects_array.append({
	"Class": "StaticRadioSignal",
	"Name": "Cosmos",
	"Ether": ether,
	"Frequency": 5.975,
	"Bandwidth": 5.0,
	"Power": 0.8,
	"Carrier": 0.6,
	"Fading": 0.35,
	"Program": cosmos_program,
})

write_file("Generated/Mixed/radio.json", {"Objects": objects_array})
