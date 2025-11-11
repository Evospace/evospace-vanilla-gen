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
		"WindSpeed": 0.5
	},
	{
		"Name": "PartlyCloudy",
		"Cloudiness01": 0.35,
		"Precipitation01": 0.0,
		"Fog01": 0.05,
		"Storminess01": 0.0,
		"WindSpeed": 1.0
	},
	{
		"Name": "Overcast",
		"Cloudiness01": 0.9,
		"Precipitation01": 0.0,
		"Fog01": 0.1,
		"Storminess01": 0.0,
		"WindSpeed": 1.5
	},
	{
		"Name": "LightRain",
		"Cloudiness01": 0.85,
		"Precipitation01": 0.25,
		"Fog01": 0.15,
		"Storminess01": 0.1,
		"WindSpeed": 2.0
	},
	{
		"Name": "Rain",
		"Cloudiness01": 0.95,
		"Precipitation01": 0.5,
		"Fog01": 0.25,
		"Storminess01": 0.3,
		"WindSpeed": 3.0
	},
	{
		"Name": "Storm",
		"Cloudiness01": 1.0,
		"Precipitation01": 0.85,
		"Fog01": 0.35,
		"Storminess01": 1.0,
		"WindSpeed": 6.0
	},
	{
		"Name": "Foggy",
		"Cloudiness01": 0.6,
		"Precipitation01": 0.0,
		"Fog01": 0.8,
		"Storminess01": 0.0,
		"WindSpeed": 0.2
	},
	{
		"Name": "LightSnow",
		"Cloudiness01": 0.9,
		"Precipitation01": 0.3,
		"Fog01": 0.2,
		"Storminess01": 0.1,
		"WindSpeed": 1.5
	},
	{
		"Name": "Snow",
		"Cloudiness01": 0.95,
		"Precipitation01": 0.55,
		"Fog01": 0.3,
		"Storminess01": 0.2,
		"WindSpeed": 2.0
	},
	{
		"Name": "Blizzard",
		"Cloudiness01": 1.0,
		"Precipitation01": 0.9,
		"Fog01": 0.6,
		"Storminess01": 1.0,
		"WindSpeed": 7.5
	}
]

# Build objects in standard "Objects" array layout
objects_array = []
loc_entries = []

for w in weathers:
	name = w["Name"]
	objects_array.append({
		"Class": "StaticWeather",
		"Name": name,
		"Label": [name, "weather"],
		"Cloudiness01": clamp(w["Cloudiness01"], 0.0, 1.0),
		"Precipitation01": clamp(w["Precipitation01"], 0.0, 1.0),
		"Fog01": clamp(w["Fog01"], 0.0, 1.0),
		"Storminess01": clamp(w["Storminess01"], 0.0, 1.0),
		"WindSpeed": max(0.0, w["WindSpeed"])
	})

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/weather.json", data)


