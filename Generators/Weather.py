from Common import *

# Weather presets in Evospace content-generation style
# Fields map to UStaticWeather DeserializeJson:
#   Cloudiness01, Precipitation01, Fog01, Storminess01, WindSpeed

weathers = [
	{
		"Name": "Clear",
		"Cloudiness01": 0.05,
		"Precipitation01": 0.0,
		"Fog01": 0.0,
		"Storminess01": 0.0,
		"WindSpeed": 0.5,
		"MinDurationSeconds": 90,
		"MaxDurationSeconds": 240,
	},
	{
		"Name": "SlightlyCloudy",
		"Cloudiness01": 0.15,
		"Precipitation01": 0.0,
		"Fog01": 0.05,
		"Storminess01": 0.0,
		"WindSpeed": 0.7,
		"MinDurationSeconds": 90,
		"MaxDurationSeconds": 240,
	},
	{
		"Name": "PartlyCloudy",
		"Cloudiness01": 0.35,
		"Precipitation01": 0.0,
		"Fog01": 0.05,
		"Storminess01": 0.0,
		"WindSpeed": 1.0,
		"MinDurationSeconds": 90,
		"MaxDurationSeconds": 240,
	},
	{
		"Name": "Overcast",
		"Cloudiness01": 0.9,
		"Precipitation01": 0.0,
		"Fog01": 0.1,
		"Storminess01": 0.0,
		"WindSpeed": 1.5,
		"MinDurationSeconds": 1,
		"MaxDurationSeconds": 30,
	},
	{
		"Name": "LightRain",
		"Cloudiness01": 0.85,
		"Precipitation01": 0.25,
		"Fog01": 0.15,
		"Storminess01": 0.1,
		"WindSpeed": 2.0,
		"MinDurationSeconds": 1,
		"MaxDurationSeconds": 30,
	},
	{
		"Name": "Rain",
		"Cloudiness01": 0.95,
		"Precipitation01": 0.5,
		"Fog01": 0.25,
		"Storminess01": 0.3,
		"WindSpeed": 3.0,
		"MinDurationSeconds": 1,
		"MaxDurationSeconds": 30,
	},
	{
		"Name": "Storm",
		"Cloudiness01": 1.0,
		"Precipitation01": 0.85,
		"Fog01": 0.35,
		"Storminess01": 1.0,
		"WindSpeed": 6.0,
		"MinDurationSeconds": 1,
		"MaxDurationSeconds": 30,
	},
	{
		"Name": "Foggy",
		"Cloudiness01": 0.6,
		"Precipitation01": 0.0,
		"Fog01": 0.8,
		"Storminess01": 0.0,
		"WindSpeed": 0.2,
		"MinDurationSeconds": 1,
		"MaxDurationSeconds": 30,
	},
	{
		"Name": "ExtremeFoggy",
		"Cloudiness01": 0.8,
		"Precipitation01": 0.0,
		"Fog01": 1.0,
		"Storminess01": 0.05,
		"WindSpeed": 0.01,
		"MinDurationSeconds": 1,
		"MaxDurationSeconds": 30,
	}
]

# Build objects in standard "Objects" array layout
objects_array = []
loc_entries = []

selection_weights = {
	"Clear": 40,
	"SlightlyCloudy": 30,
	"PartlyCloudy": 30,
	"Overcast": 20,
	"LightRain": 5,
	"Rain": 5,
	"Storm": 3,
	"Foggy": 15,
	"ExtremeFoggy": 3,
}

for w in weathers:
	name = w["Name"]
	weight = selection_weights.get(name, 10)
	objects_array.append({
		"Class": "StaticWeather",
		"Name": name,
		"Label": [name, "weather"],
		"Cloudiness01": clamp(w["Cloudiness01"], 0.0, 1.0),
		"Precipitation01": clamp(w["Precipitation01"], 0.0, 1.0),
		"Fog01": clamp(w["Fog01"], 0.0, 1.0),
		"Storminess01": clamp(w["Storminess01"], 0.0, 1.0),
		"WindSpeed": max(0.0, w["WindSpeed"]),
		"SelectionWeight": max(0.0, weight),
		"MinDurationSeconds": w["MinDurationSeconds"],
		"MaxDurationSeconds": w["MaxDurationSeconds"],
	})

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/weather.json", data)


