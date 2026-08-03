from Common import *

# Look presets in Evospace content-generation style. A look is how a biome shows one severity band
# of the global weather cycle; wind and severity come from the simulation, not from here.
#
# The fog fields are the exponential height fog's own settings, applied as written:
#   FogDensity              density at sea level; visibility in metres is about 62 / density
#   FogHeightFalloff        density halves every 10 / falloff metres of altitude
#   FogMaxOpacity           0..1 cap on how opaque the fog may get
#   FogStartDistance        centimetres in front of the camera before fog starts
#   FogTint                 linear RGB multiplied into the fog and ambient colour
#   SecondFogDensity        second layer density at its own height
#   SecondFogHeightFalloff  second layer falloff, same units as FogHeightFalloff
#   SecondFogHeightOffset   second layer height above sea level, in centimetres
# The second layer is the ground fog bank: it thickens downwards from its height, so a bank set at
# 1200 with falloff 1.4 fills the valleys and is gone from the ridges. The world's sea level is 0.
#
# The climate is damp: even the clear bands carry haze, and every band above Overcast puts fog in
# the low ground.

weathers = [
	{
		"Name": "Clear",
		"Cloudiness01": 0.05,
		"Precipitation01": 0.0,
		"Storminess01": 0.0,
		"FogDensity": 0.003,
		"FogHeightFalloff": 0.04,
		"FogTint": [0.50, 0.60, 0.72],
	},
	{
		# Fair-weather cumulus for the Light severity band. Kept high enough that
		# CloudCoverage = Lerp(0, 0.8, Cloudiness) still reads as real scattered clouds,
		# not the sparse wisps left by the old 0.15 value.
		"Name": "SlightlyCloudy",
		"Cloudiness01": 0.48,
		"Precipitation01": 0.0,
		"Storminess01": 0.0,
		"FogDensity": 0.0038,
		"FogHeightFalloff": 0.05,
		"FogTint": [0.52, 0.60, 0.70],
	},
	{
		"Name": "PartlyCloudy",
		"Cloudiness01": 0.68,
		"Precipitation01": 0.0,
		"Storminess01": 0.0,
		"FogDensity": 0.005,
		"FogHeightFalloff": 0.05,
		"FogTint": [0.55, 0.61, 0.70],
	},
	{
		"Name": "Overcast",
		"Cloudiness01": 0.95,
		"Precipitation01": 0.0,
		"Storminess01": 0.15,
		"FogDensity": 0.008,
		"FogHeightFalloff": 0.07,
		"FogTint": [0.62, 0.65, 0.70],
	},
	{
		"Name": "LightRain",
		"Cloudiness01": 0.85,
		"Precipitation01": 0.25,
		"Storminess01": 0.1,
		"FogDensity": 0.016,
		"FogHeightFalloff": 0.10,
		"SecondFogDensity": 0.008,
		"SecondFogHeightFalloff": 0.8,
		"SecondFogHeightOffset": 1000.0,
		"FogTint": [0.55, 0.59, 0.64],
		"Effect": "Rain",
	},
	{
		"Name": "Rain",
		"Cloudiness01": 0.95,
		"Precipitation01": 0.5,
		"Storminess01": 0.3,
		"FogDensity": 0.03,
		"FogHeightFalloff": 0.12,
		"SecondFogDensity": 0.017,
		"SecondFogHeightFalloff": 0.8,
		"SecondFogHeightOffset": 1200.0,
		"FogTint": [0.50, 0.54, 0.60],
		"Effect": "Rain",
	},
	{
		"Name": "Storm",
		"Cloudiness01": 1.0,
		"Precipitation01": 0.85,
		"Storminess01": 1.0,
		"FogDensity": 0.055,
		"FogHeightFalloff": 0.15,
		"SecondFogDensity": 0.028,
		"SecondFogHeightFalloff": 0.8,
		"SecondFogHeightOffset": 1200.0,
		"FogTint": [0.42, 0.45, 0.52],
		"Effect": "Rain",
	},
	{
		"Name": "Foggy",
		"Cloudiness01": 0.6,
		"Precipitation01": 0.0,
		"Storminess01": 0.0,
		"FogDensity": 0.025,
		"FogHeightFalloff": 0.15,
		"SecondFogDensity": 0.14,
		"SecondFogHeightFalloff": 0.8,
		"SecondFogHeightOffset": 2000.0,
		"FogTint": [0.72, 0.75, 0.78],
	},
	{
		"Name": "ExtremeFoggy",
		"Cloudiness01": 0.8,
		"Precipitation01": 0.0,
		"Storminess01": 0.05,
		"FogDensity": 0.06,
		"FogHeightFalloff": 0.20,
		"SecondFogDensity": 0.22,
		"SecondFogHeightFalloff": 0.55,
		"SecondFogHeightOffset": 2600.0,
		"FogTint": [0.78, 0.80, 0.82],
	},
	{
		"Name": "DenseLowFog",
		"Cloudiness01": 0.48,
		"Precipitation01": 0.0,
		"Storminess01": 0.0,
		"FogDensity": 0.004,
		"FogHeightFalloff": 0.06,
		"SecondFogDensity": 0.20,
		"SecondFogHeightFalloff": 1.4,
		"SecondFogHeightOffset": 1200.0,
		"FogTint": [0.70, 0.73, 0.77],
	},
	{
		# Pine Light band: valley fog plus a readable broken cloud deck above it.
		"Name": "LightLowFog",
		"Cloudiness01": 0.42,
		"Precipitation01": 0.0,
		"Storminess01": 0.0,
		"FogDensity": 0.003,
		"FogHeightFalloff": 0.05,
		"SecondFogDensity": 0.042,
		"SecondFogHeightFalloff": 1.2,
		"SecondFogHeightOffset": 1000.0,
		"FogTint": [0.62, 0.67, 0.73],
	},
	{
		# Snow biome Precipitation band: UDW Snow particles, not Rain.
		"Name": "Snowfall",
		"Cloudiness01": 0.9,
		"Precipitation01": 0.35,
		"EffectIntensity01": 0.35,
		"Storminess01": 0.1,
		"FogDensity": 0.025,
		"FogHeightFalloff": 0.12,
		"SecondFogDensity": 0.014,
		"SecondFogHeightFalloff": 0.9,
		"SecondFogHeightOffset": 1200.0,
		"FogTint": [0.78, 0.82, 0.88],
		"Effect": "Snow",
	},
	{
		# Snow biome Extreme band.
		"Name": "Blizzard",
		"Cloudiness01": 1.0,
		"Precipitation01": 0.85,
		"EffectIntensity01": 0.85,
		"Storminess01": 0.9,
		"FogDensity": 0.085,
		"FogHeightFalloff": 0.15,
		"SecondFogDensity": 0.056,
		"SecondFogHeightFalloff": 0.7,
		"SecondFogHeightOffset": 1500.0,
		"FogTint": [0.82, 0.86, 0.90],
		"Effect": "Snow",
	},
	{
		# Desert Precipitation band: UDW Dust particles instead of rain.
		"Name": "DustHaze",
		"Cloudiness01": 0.3,
		"Precipitation01": 0.3,
		"EffectIntensity01": 0.3,
		"Storminess01": 0.3,
		"FogDensity": 0.028,
		"FogHeightFalloff": 0.05,
		"FogTint": [0.72, 0.58, 0.40],
		"Effect": "Dust",
	},
	{
		# Desert Extreme band.
		"Name": "SandStorm",
		"Cloudiness01": 0.5,
		"Precipitation01": 0.9,
		"EffectIntensity01": 0.9,
		"Storminess01": 0.9,
		"FogDensity": 0.12,
		"FogHeightFalloff": 0.06,
		"SecondFogDensity": 0.07,
		"SecondFogHeightFalloff": 0.5,
		"SecondFogHeightOffset": 2000.0,
		"FogTint": [0.78, 0.60, 0.38],
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
		"Storminess01": clamp(w["Storminess01"], 0.0, 1.0),
		"FogDensity": max(w["FogDensity"], 0.0),
		"FogHeightFalloff": max(w["FogHeightFalloff"], 0.0),
		"FogMaxOpacity": clamp(w.get("FogMaxOpacity", 1.0), 0.0, 1.0),
		"FogStartDistance": max(w.get("FogStartDistance", 0.0), 0.0),
		"FogTint": w["FogTint"],
		"SecondFogDensity": max(w.get("SecondFogDensity", 0.0), 0.0),
		"SecondFogHeightFalloff": max(w.get("SecondFogHeightFalloff", 1.0), 0.0),
		"SecondFogHeightOffset": w.get("SecondFogHeightOffset", 0.0),
		"Effect": w.get("Effect", "None"),
		"EffectIntensity01": clamp(w.get("EffectIntensity01", w["Precipitation01"]), 0.0, 1.0),
	})

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/weather.json", data)
