from Common import *

# Look presets in Evospace content-generation style. A look is how a biome shows one severity band
# of the global weather cycle; wind and severity come from the simulation, not from here.
#
# A look is written in the renderer's own knobs, 0..10, and every one of them reaches Ultra Dynamic
# Sky as it stands: CloudCoverage, Thunder, Fog, and EffectIntensity for whichever Effect the look
# names (Rain / Snow / Dust). For fog, 5.5 is a hazy clear day, 8 is heavy weather, 10 is milk.
#
# The climate is damp: even the clear bands carry haze, and every band above Overcast is thick.
#
# The far map ends 4096 blocks out, and past that the world is sky. A look below min_fog shows that
# edge and every far map tile up to it, so no preset goes under it - UStaticWeather::DeserializeJson
# holds the same floor for looks that come from mods.

min_fog = 5.5
max_knob = 10.0

weathers = [
	{
		"Name": "Clear",
		"CloudCoverage": 0.4,
		"Thunder": 0,
		"Fog": 5.5,
	},
	{
		# Fair-weather cumulus for the Light severity band. Kept high enough to read as real
		# scattered clouds, not the sparse wisps it started out with.
		"Name": "SlightlyCloudy",
		"CloudCoverage": 3.8,
		"Thunder": 0,
		"Fog": 5.7,
	},
	{
		"Name": "PartlyCloudy",
		"CloudCoverage": 5.4,
		"Thunder": 0,
		"Fog": 6.0,
	},
	{
		"Name": "Overcast",
		"CloudCoverage": 8,
		"Thunder": 1.5,
		"Fog": 6.5,
	},
	{
		"Name": "LightRain",
		"CloudCoverage": 7.1,
		"Thunder": 1,
		"Fog": 7.0,
		"EffectIntensity": 2.5,
		"Effect": "Rain",
	},
	{
		"Name": "Rain",
		"CloudCoverage": 8.3,
		"Thunder": 3,
		"Fog": 7.8,
		"EffectIntensity": 5,
		"Effect": "Rain",
	},
	{
		"Name": "Storm",
		"CloudCoverage": 10,
		"Thunder": 10,
		"Fog": 8.5,
		"EffectIntensity": 8.5,
		"Effect": "Rain",
	},
	{
		"Name": "Foggy",
		"CloudCoverage": 4.8,
		"Thunder": 0,
		"Fog": 9.3,
	},
	{
		"Name": "ExtremeFoggy",
		"CloudCoverage": 6.6,
		"Thunder": 0.5,
		"Fog": 10.0,
	},
	{
		"Name": "DenseLowFog",
		"CloudCoverage": 3.8,
		"Thunder": 0,
		"Fog": 8.8,
	},
	{
		# Pine Light band: valley fog plus a readable broken cloud deck above it.
		"Name": "LightLowFog",
		"CloudCoverage": 3.4,
		"Thunder": 0,
		"Fog": 6.8,
	},
	{
		# Snow biome Precipitation band: UDW Snow particles, not Rain.
		"Name": "Snowfall",
		"CloudCoverage": 7.5,
		"Thunder": 1,
		"EffectIntensity": 3.5,
		"Fog": 7.3,
		"Effect": "Snow",
	},
	{
		# Snow biome Extreme band.
		"Name": "Blizzard",
		"CloudCoverage": 9.8,
		"Thunder": 9,
		"EffectIntensity": 8.5,
		"Fog": 9.0,
		"Effect": "Snow",
	},
	{
		# Desert Precipitation band: UDW Dust particles instead of rain.
		"Name": "DustHaze",
		"CloudCoverage": 4.7,
		"Thunder": 3,
		"EffectIntensity": 3,
		"Fog": 7.5,
		"Effect": "Dust",
	},
	{
		# Desert Extreme band.
		"Name": "SandStorm",
		"CloudCoverage": 9.4,
		"Thunder": 9,
		"EffectIntensity": 9,
		"Fog": 9.5,
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
		"CloudCoverage": clamp(w["CloudCoverage"], 0.0, max_knob),
		"Thunder": clamp(w["Thunder"], 0.0, max_knob),
		"Fog": clamp(w["Fog"], min_fog, max_knob),
		"Effect": w.get("Effect", "None"),
		"EffectIntensity": clamp(w.get("EffectIntensity", 0.0), 0.0, max_knob),
	})

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/weather.json", data)
