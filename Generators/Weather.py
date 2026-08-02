from Common import *

# Look presets in Evospace content-generation style. A look is how a biome shows one severity band
# of the global weather cycle; wind and severity come from the simulation, not from here.
# Fields map to UStaticWeather DeserializeJson:
#   Cloudiness01, Precipitation01, Fog01, SecondFog01, Storminess01

weathers = [
	{
		"Name": "Clear",
		"Cloudiness01": 0.05,
		"Precipitation01": 0.0,
		"Fog01": 0.0,
		"SecondFog01": 0.0,
		"Storminess01": 0.0,
	},
	{
		"Name": "SlightlyCloudy",
		"Cloudiness01": 0.15,
		"Precipitation01": 0.0,
		"Fog01": 0.05,
		"SecondFog01": 0.0,
		"Storminess01": 0.0,
	},
	{
		"Name": "PartlyCloudy",
		"Cloudiness01": 0.35,
		"Precipitation01": 0.0,
		"Fog01": 0.05,
		"SecondFog01": 0.0,
		"Storminess01": 0.0,
	},
	{
		"Name": "Overcast",
		"Cloudiness01": 0.95,
		"Precipitation01": 0.0,
		"Fog01": 0.02,
		"SecondFog01": 0.0,
		"Storminess01": 0.15,
	},
	{
		"Name": "LightRain",
		"Cloudiness01": 0.85,
		"Precipitation01": 0.25,
		"Fog01": 0.15,
		"SecondFog01": 0.0,
		"Storminess01": 0.1,
		"Effect": "Rain",
	},
	{
		"Name": "Rain",
		"Cloudiness01": 0.95,
		"Precipitation01": 0.5,
		"Fog01": 0.25,
		"SecondFog01": 0.0,
		"Storminess01": 0.3,
		"Effect": "Rain",
	},
	{
		"Name": "Storm",
		"Cloudiness01": 1.0,
		"Precipitation01": 0.85,
		"Fog01": 0.35,
		"SecondFog01": 0.0,
		"Storminess01": 1.0,
		"Effect": "Rain",
	},
	{
		"Name": "Foggy",
		"Cloudiness01": 0.6,
		"Precipitation01": 0.0,
		"Fog01": 0.8,
		"SecondFog01": 0.6,
		"Storminess01": 0.0,
	},
	{
		"Name": "ExtremeFoggy",
		"Cloudiness01": 0.8,
		"Precipitation01": 0.0,
		"Fog01": 1.0,
		"SecondFog01": 0.85,
		"Storminess01": 0.05,
	},
	{
		"Name": "DenseLowFog",
		"Cloudiness01": 0.35,
		"Precipitation01": 0.0,
		"Fog01": 0.15,
		"SecondFog01": 1.0,
		"Storminess01": 0.0,
	},
	{
		"Name": "LightLowFog",
		"Cloudiness01": 0.25,
		"Precipitation01": 0.0,
		"Fog01": 0.15,
		"SecondFog01": 0.35,
		"Storminess01": 0.0,
	},
	{
		"Name": "Snowfall",
		"Cloudiness01": 0.9,
		"Precipitation01": 0.0,
		"EffectIntensity01": 0.35,
		"Fog01": 0.2,
		"SecondFog01": 0.1,
		"Storminess01": 0.1,
		"Effect": "Snow",
	},
	{
		"Name": "Blizzard",
		"Cloudiness01": 1.0,
		"Precipitation01": 0.0,
		"EffectIntensity01": 0.85,
		"Fog01": 0.6,
		"SecondFog01": 0.4,
		"Storminess01": 0.9,
		"Effect": "Snow",
	},
	{
		"Name": "DustHaze",
		"Cloudiness01": 0.3,
		"Precipitation01": 0.0,
		"EffectIntensity01": 0.3,
		"Fog01": 0.5,
		"SecondFog01": 0.2,
		"Storminess01": 0.3,
		"Effect": "Dust",
	},
	{
		"Name": "SandStorm",
		"Cloudiness01": 0.5,
		"Precipitation01": 0.0,
		"EffectIntensity01": 0.9,
		"Fog01": 0.9,
		"SecondFog01": 0.5,
		"Storminess01": 0.9,
		"Effect": "Dust",
	}
]

# Build objects in standard "Objects" array layout
# Which look a biome shows in each severity band is defined per biome family in Biomes.py.

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
		"SecondFog01": clamp(w.get("SecondFog01", 0.0), 0.0, 1.0),
		"Storminess01": clamp(w["Storminess01"], 0.0, 1.0),
		"Effect": w.get("Effect", "None"),
		"EffectIntensity01": clamp(w.get("EffectIntensity01", w["Precipitation01"]), 0.0, 1.0),
	})

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/weather.json", data)


