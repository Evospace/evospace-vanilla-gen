from Common import *

global_family = []
families = []
families = []
biomes = []
generators = []
complexbiomes = []


mega_boime_size = 0.003
biome_family_size = 0.016

# Legacy mega families (WorldGeneratorBiome / Rivers / Plains): unchanged pre-hills set.
legacy_mega_family_childs = [
	"SeaBiomeFamily",
	"SnowBiomeFamily",
	"PrairieBiomeFamily",
	"PineForestBiomeFamily",
	"PlainBiomeFamily",
	"SandBiomeFamily",
	"ForestBiomeFamily",
	"SwampBiomeFamily",
	"VolcanicBiomeFamily",
	"FertileForestBiomeFamily",
]

# UWorldGeneratorConfigurable only: legacy cellular set plus dedicated hills/mountains families.
# Snow and MountainsBiomeFamily are excluded from cellular picking in C++ (height / regional mask).
configurable_mega_family_childs = legacy_mega_family_childs + [
	"HillsBiomeFamily",
	"MountainsBiomeFamily",
]

global_family.append({
		"Name":"GlobalBiomeMegaFamily",
		"Class":"GlobalBiomeFamily",
		"Childs": legacy_mega_family_childs,
        "ChildFrequency": mega_boime_size,
	})
global_family.append({
		"Name":"GlobalBiomeMegaFamily2",
		"Class":"GlobalBiomeFamily2",
		"Childs": legacy_mega_family_childs,
        "ChildFrequency": mega_boime_size,
	})
global_family.append({
		"Name":"GlobalBiomeMegaFamily3",
		"Class":"GlobalBiomeFamily3",
		"Childs": legacy_mega_family_childs,
        "ChildFrequency": mega_boime_size,
	})
# Dedicated family for UWorldGeneratorConfigurable (deep copy of MegaFamily2).
global_family.append({
		"Name":"GlobalBiomeMegaFamilyConfigurable",
		"Class":"GlobalBiomeFamilyConfigurable",
		"Childs": configurable_mega_family_childs,
        "ChildFrequency": mega_boime_size,
	})
global_family.append({
		"Name":"GlobalBiomeMegaFamilyMoon",
		"Class":"GlobalBiomeFamilyMoon",
		"Childs": ["MoonBiomeFamily"],
        "ChildFrequency": mega_boime_size,
	})
	
	# ENaturalBiome ordinals match legacy_mega_family_childs indices 0..9, then configurable adds:
	#Sea = 0,
	#Taiga = 1,
	#Steppe = 2,
	#Pineforest = 3,
	#Grassland = 4,
	#Desert = 5,
	#Forest = 6,
	#Swamp = 7,
	#Volcano = 8,
	#FertileForest = 9,
	#Hills = 10,
	#Mountains = 11,
	#Wasteland = 12,  # flat/concrete worlds only (not in mega family childs)

# biome families
families.extend([
	{
		# Dry steppe / prairie: continental climate, many fair days,
		# occasional convective showers in summer, thin radiation fog
		# on cool calm mornings. No heavy storms, no deep fog banks.
		"Name":"PrairieBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"PrairieDryPlainsBiome",
			"PrairieDryHillsBiome",
			"PrairiePlainsBiome",
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain", "Rain", "LightLowFog"],
		"WeatherWeights": [     32,               24,             16,         10,          8,      3,             7],
	},	{
		# Hot desert: overwhelming clear sky, some haze, essentially no rain.
		# Rare sandstorm mapped to "Storm" for wind/visibility spike.
		# Ground fog and drizzle are omitted on purpose.
		"Name":"SandBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"DesertBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["Clear", "SlightlyCloudy", "PartlyCloudy", "Storm"],
		"WeatherWeights": [     62,               28,              6,       4],
	},	{
		# Temperate mixed forest: balanced sky states, regular but
		# moderate rain, morning/valley fog fairly common.
		"Name":"ForestBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"ForestBiome",
			"PlainsBiome",
			"BushlandBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain", "Rain", "Foggy", "LightLowFog"],
		"WeatherWeights": [     16,               16,             16,         14,         10,      6,      10,            12],
	},	{
		# Taiga / cool conifer belt: fewer truly clear days, dominant
		# overcast/low cloud, frequent drizzle, persistent valley fog.
		# No big thunderstorms (cold air is stable).
		"Name":"PineForestBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"PineForestBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain", "Rain", "Foggy", "LightLowFog"],
		"WeatherWeights": [     10,               14,             16,         20,         12,      6,      12,            10],
	},	{
		# Coast / open sea: strong maritime character - persistent sea fog,
		# drizzle, and proper storms with wind. Blue skies exist but are
		# less durable than inland.
		"Name":"SeaBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"SeaBiome",
			"SeaGrassBiome",
			"EmptySeaBiome",
            "GravelSeaBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain", "Rain", "Storm", "Foggy"],
		"WeatherWeights": [     10,               12,             14,         14,         12,     10,       6,      22],
	},	{
		# Volcanic zone: ash-loaded atmosphere, dominant overcast/haze,
		# frequent violent thunderstorms triggered by heat, occasional
		# ashfall episodes mapped to fog layers. Almost no serene skies.
		"Name":"VolcanicBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"VolcanoBiome",
			"BrokenLandBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain", "Storm", "Foggy", "ExtremeFoggy"],
		"WeatherWeights": [      6,               14,             12,         24,          8,      22,      10,              4],
	},	{
		# Wetland / swamp: saturated air, dominant overcast with steady
		# rain and multiple fog layers at ground level. Fair weather is
		# essentially absent. Occasional summer thunderstorm.
		"Name":"SwampBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"PeatBiome",
			"BogBiome",
			"BogForestBiome",
			"ClayBiome",
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["PartlyCloudy", "Overcast", "LightRain", "Rain", "Storm", "Foggy", "ExtremeFoggy", "DenseLowFog", "LightLowFog"],
		"WeatherWeights": [             5,         12,          18,     15,       3,      18,              8,            10,            11],
	},	{
		# Open plains / grassland: similar to prairie but more humid -
		# more showers, occasional thunderstorm, brief morning ground fog.
		"Name":"PlainBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"PlainsBiome",
			"RedPlainsBiome",
			"WhitePlainsBiome",
			"YellowPlainsBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain", "Rain", "Storm", "LightLowFog"],
		"WeatherWeights": [     26,               20,             18,         12,         10,      5,       2,             7],
	},	{
		# Cold / snow regions: crisp clear days alternate with low overcast.
		# No rain (would look wrong on snow); instead frequent ice fog
		# and ground-hugging dense fog in valleys.
		"Name":"SnowBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"SnowBiome",
			"SnowGrassBiome",
			"SnowForestBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "Foggy", "ExtremeFoggy", "DenseLowFog", "LightLowFog"],
		"WeatherWeights": [     18,               16,             14,         14,      12,              8,             8,            10],
	},
	{
		# Humid productive / subtropical forest: very wet, frequent
		# showers and thunderstorms, dense canopy fog after rain.
		# Long dry spells are rare.
		"Name":"FertileForestBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"FertileForestBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain", "Rain", "Storm", "Foggy", "LightLowFog"],
		"WeatherWeights": [               5,             10,         15,         20,     20,      10,      12,             8],
	},
	{
		# Flat concrete wasteland world: keep weather variants strictly clear-only
		"Name":"WastelandBiomeFamily",
		"Class":"BiomeFamily",
		"Childs": [],
		"ChildFrequency": biome_family_size,
		"Weather": ["Clear"],
		"WeatherWeights": [1],
	},
	{
		# Rolling hills: moderate relief, grass-covered slopes, occasional showers.
		"Name":"HillsBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"HillsBiome",
			"HillsForestBiome",
		],
		"ChildFrequency": biome_family_size * 0.85,
		"Weather":        ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain", "Rain", "LightLowFog"],
		"WeatherWeights": [     22,               18,             16,         12,         10,      5,             7],
	},
	{
		# Airless gray regolith: clear sky only, no weather drama.
		"Name":"MoonBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"MoonRegolithBiome",
		],
		"ChildFrequency": biome_family_size,
		"Weather":        ["Clear"],
		"WeatherWeights": [1],
	},
	{
		# High mountains: cold, crisp air, sparse vegetation, snow caps at altitude.
		"Name":"MountainsBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"MountainsStoneBiome",
			"MountainsDarkStoneBiome",
			"MountainsLayeredBiome",
			"MountainsSnowBiome",
		],
		"ChildFrequency": biome_family_size * 0.70,
		"Weather":        ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "Foggy", "ExtremeFoggy", "LightLowFog"],
		"WeatherWeights": [     20,               14,             12,         16,      14,              8,            16],
	},
])

# generators
generators.extend([
	# general
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "DryGrassLayering",
		"Blocks": ["DryGrassSurface" + static_surface, "DirtSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "GrassLayering",
		"Blocks": ["GrassSurface" + static_surface, "DirtSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},
	
	# jungle
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "DipteroLayering",
		"Blocks": ["GrassSurface" + static_surface, "DirtSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},
	
	# snow
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "SnowLayering",
		"Blocks": ["SnowSurface", "DirtSurface", "StoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "DarkStoneSurface"],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},
	
	# swamp
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "BogGrassLayeringGrass",
		"Blocks": ["BogSurface", "DirtSurface", "StoneSurface", "StoneSurface", "DarkStoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "RedStoneSurface"],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},{
		"Class": "SimpleLayeringGenerator",
		"Name": "PeatLayering",
		"Blocks": ["PeatSurface", "PeatSurface", "StoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "DarkStoneSurface"],
		"Starts": [0, 2, 4, 9, 12, 16, 19, 23, 30]
	},{
		"Class": "SimpleLayeringGenerator",
		"Name": "ClayLayering",
		"Blocks": ["ClaySurface", "ClaySurface", "DarkStoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "DarkStoneSurface"],
		"Starts": [0, 2, 6, 9, 12, 16, 19, 23, 30]
	},{
		# Clay only fills the carved basins (the lowlands): where ClayBasinHeight
		# drops below -2 the "Low" clay stack is used, otherwise the boggy grass
		# swells. Threshold matches SwampHeight's basin carve so clay reads as wet
		# bottoms instead of blanketing the whole clay sub-biome.
		"Class": "LowlandLayeringGenerator",
		"Name": "ClayLowlandLayering",
		"Blocks": ["BogSurface", "DirtSurface", "StoneSurface", "StoneSurface", "DarkStoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "RedStoneSurface"],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
		"LowBlocks": ["ClaySurface", "ClaySurface", "DarkStoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "DarkStoneSurface"],
		"LowStarts": [0, 2, 6, 9, 12, 16, 19, 23, 30],
		"Height": "ClayBasinHeight",
		"Below": -2.0,
	},
	
	# grass
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "JustGrassLayeringPine",
		"Blocks": ["PineForestSurface" + static_surface, "DirtSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},
	
	# sea
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "SeaBottomLayeringSand",
		"Blocks": ["SandSurface" + static_surface, "LimestoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 9, 12, 16, 19, 23, 30]
	},{
		"Class": "SimpleLayeringGenerator",
		"Name": "SeaBottomLayeringGravel",
		"Blocks": ["GravelSurface" + static_surface, "LimestoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 9, 12, 16, 19, 23, 30]
	},{
		"Class": "SimpleLayeringGenerator",
		"Name": "SeaBottomLayeringCopper",
		"Blocks": ["ClaySurface" + static_surface, "LimestoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 9, 12, 16, 19, 23, 30]
	},{
		"Class": "SimpleLayeringGenerator",
		"Name": "SeaBottomLayeringClay",
		"Blocks": ["ClaySurface" + static_surface, "LimestoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 9, 12, 16, 19, 23, 30]
	},
	
	# volcanic
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "VolcanicLayeringBasalt",
		"Blocks": ["BasaltSurface" + static_surface, "LavaSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface],
		"Starts": [0, 4, 9, 12, ]
	},
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "BrokenLandLayeringBasalt",
		"Blocks": ["BasaltSurface" + static_surface, "LavaSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface],
		"Starts": [0, 4, 9, 12, ]
	},
	
	# river
	{
		"Class":"SimpleLayeringGenerator",
		"Name":"RiverLayeringSand",
		"Blocks":["SandSurface" + static_surface, "SandstoneSurface" + static_surface, "LimestoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},
	
	# desert
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "SandLayeringSand",
		"Blocks": ["DesertSandSurface" + static_surface, "SandstoneSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "SandDesertLayeringSand",
		"Blocks": ["DesertSandSurface" + static_surface, "SandstoneSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},
	
	# hills / mountains
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "HillsLayering",
		"Blocks": ["GrassSurface" + static_surface, "DirtSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 5, 9, 12, 16, 19, 23, 30]
	},
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "MountainStoneLayering",
		"Blocks": ["StoneSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 5, 9, 12, 16, 19, 23]
	},
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "MountainDarkStoneLayering",
		"Blocks": ["DarkStoneSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 5, 9, 12, 16, 19, 23]
	},
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "MountainLayeredLayering",
		"Blocks": ["StoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "DarkStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "DarkStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 4, 6, 8, 10, 12, 16, 20, 24, 30]
	},
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "MountainSnowLayering",
		"Blocks": ["SnowSurface", "StoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "RedStoneSurface", "StoneSurface", "DarkStoneSurface"],
		"Starts": [0, 2, 5, 9, 12, 16, 19, 23]
	},
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "RegolithLayering",
		"Blocks": ["GravelSurface" + static_surface, "StoneSurface" + static_surface,
		           "DarkStoneSurface" + static_surface, "StoneSurface" + static_surface],
		"Starts": [0, 2, 8, 20]
	}
])

# ---- Per-biome terrain height (biome_plan.md) ----
# Each leaf biome adds detail on top of the shared reference base elevation.
# A NoiseGenerator maps raw noise [-1,1] into [Min,Max]; a HeightGenerator
# sums its noises. Layer dict keys match JSON (CamelCase). SeedOffset
# decorrelates layers within a stack. Loaded from the "Generators" content
height_noises = []
height_gens = []

def add_height(name, layers):
	noise_names = []
	for i, l in enumerate(layers):
		nn = name + "Noise" + str(i)
		noise_type = l.get("NoiseType", "SimplexFractal")
		entry = {
			"Class": "NoiseGenerator",
			"Name": nn,
			"NoiseType": noise_type,
			"Frequency": l["Frequency"],
			"FractalOctaves": l.get("FractalOctaves", 4),
			"Min": l["Min"],
			"Max": l["Max"],
			"SeedOffset": l.get("SeedOffset", i * 911 + 17),
		}
		if noise_type == "Cellular" or "CellularReturnType" in l:
			entry["CellularReturnType"] = l.get("CellularReturnType", "Distance")
		if "CellularDistanceFunction" in l:
			entry["CellularDistanceFunction"] = l["CellularDistanceFunction"]
		if "CellularJitter" in l:
			entry["CellularJitter"] = l["CellularJitter"]
		if "FractalType" in l:
			entry["FractalType"] = l["FractalType"]
		if "Power" in l:
			entry["Power"] = l["Power"]
		height_noises.append(entry)
		noise_names.append(nn)
	height_gens.append({
		"Class": "HeightGenerator",
		"Name": name,
		"Noises": noise_names,
	})

# climate-scale relief; amplitudes are detail added on top of the global backbone
add_height("PlainHeight",        [{"Frequency": 0.012, "FractalOctaves": 2, "Min": 0,  "Max": 4}])
add_height("PrairieHeight",      [{"Frequency": 0.010, "FractalOctaves": 2, "Min": 0,  "Max": 4}])
add_height("PrairieHillsHeight", [{"Frequency": 0.013, "FractalOctaves": 2, "Min": 2,  "Max": 4}])
add_height("ForestHeight",       [{"Frequency": 0.009, "FractalOctaves": 2, "Min": 0,  "Max": 4},
                                  {"Frequency": 0.030, "FractalOctaves": 2, "Min": 0,  "Max": 4}])
# Gently rolling, morainic relief: a broad swell plus low hummocks under the canopy
add_height("PineForestHeight",   [{"Frequency": 0.006, "FractalOctaves": 3, "Min": -3, "Max": 6},
                                  {"Frequency": 0.022, "FractalOctaves": 2, "Min": 0,  "Max": 3}])
add_height("SnowHeight",         [{"Frequency": 0.004, "FractalOctaves": 2, "Min": 0,  "Max": 4},
                                  {"Frequency": 0.020, "FractalOctaves": 2, "Min": 0,  "Max": 7}])
add_height("SandHeight",         [{"NoiseType": "Cellular", "FractalOctaves": 2, "Frequency": 0.040, "CellularReturnType": "Distance",
                                  "CellularDistanceFunction": "Natural", "CellularJitter": 0.75, "Min": -2, "Max": 2}])
# Flat wetland base plus rare circular lake basins carved by a sparse cellular field.
add_height("SwampHeight",        [{"Frequency": 0.020, "FractalOctaves": 2, "Min": -2, "Max": 3},
                                  {"NoiseType": "Cellular", "Frequency": 0.0035, "FractalOctaves": 1,
                                   "CellularReturnType": "Distance2Cave", "CellularDistanceFunction": "Natural",
                                   "CellularJitter": 0.55, "Min": 0, "Max": -7, "Power": 5, "SeedOffset": 4201}])
add_height("VolcanicHeight",     [{"Frequency": 0.01, "FractalOctaves": 5, "Min": -4,  "Max": 4},
                                  {"Frequency": 0.05, "FractalOctaves": 2, "Min": 1,  "Max": 10, "Power": 10}])
add_height("FertileForestHeight",[{"Frequency": 0.009, "FractalOctaves": 2, "Min": 0,  "Max": 4}])

# Moderate rolling hills (gameplay_mountains_plan: foothill relief, rounded silhouettes).
add_height("HillsHeight",        [{"Frequency": 0.010, "FractalOctaves": 4, "Min": -8,  "Max": 12},
                                  {"Frequency": 0.025, "FractalOctaves": 2, "Min": -4,  "Max": 8}])
# Ridged foothill / mountain detail for MountainsBiomeFamily (configurable generator).
add_height("MountainsHeight",    [{"Frequency": 0.006, "FractalOctaves": 5, "FractalType": "Ridged", "Min": -2, "Max": 24, "Power": 2},
                                  {"Frequency": 0.015, "FractalOctaves": 3, "Min": -3,  "Max": 12, "Power": 1}])
add_height("MoonCraterHeight",   [{"NoiseType": "Cellular", "FractalOctaves": 2, "Frequency": 0.035,
                                  "CellularReturnType": "Distance2Sub", "Min": -6, "Max": 2},
                                 {"Frequency": 0.01, "FractalOctaves": 3, "Min": -1, "Max": 1}])
# Basin-only field for the clay biome's lowland layering. MUST mirror SwampHeight's
# second (basin) layer exactly — same noise params AND SeedOffset — so the clay
# patches line up with the actual carved basins of the clay terrain (ClayBiome
# uses SwampHeight). The flat fbm layer of SwampHeight is intentionally omitted
# here so only the real depressions read as "lowland" (not random fbm dips).
add_height("ClayBasinHeight",    [{"NoiseType": "Cellular", "Frequency": 0.0035, "FractalOctaves": 1,
                                   "CellularReturnType": "Distance2Cave", "CellularDistanceFunction": "Natural",
                                   "CellularJitter": 0.55, "Min": 0, "Max": -7, "Power": 5, "SeedOffset": 4201}])

# noises + height generators load first (single-pass-safe ordering)
generators = height_noises + height_gens + generators

#biomes
biomes.extend([
	# prairie
	{
		"Class":"Biome",
		"Name":"PrairieDryPlainsBiome",
		"Layering":"DryGrassLayering",
		"Props":"PrairieDryProps"
	},
	{
		"Class":"Biome",
		"Name":"PrairiePlainsBiome",
		"Layering":"DryGrassLayering",
		"Props":"PrairieProps"
	},
	{
		"Class":"Biome",
		"Name":"PrairieDryHillsBiome",
		"Layering":"DryGrassLayering",
		"Props":"PrairieDryProps"
	},
	
	# forest
	{
		"Class":"Biome",
		"Name":"PineForestBiome",
		"Layering":"JustGrassLayeringPine",
		"Props":"PineForestProps",
		"Color":[184/255.0, 255/255.0, 133/255.0]
	},{
		"Class":"Biome",
		"Name":"ForestBiome",
		"Layering":"GrassLayering",
		"Props":"ForestProps",
		"Color":[184/255.0, 255/255.0, 133/255.0]
	},
	
	# snow
	{
		"Class":"Biome",
		"Name":"SnowBiome",
		"Layering":"SnowLayering",
		"Props": "SnowProps"
	},
	{
		"Class":"Biome",
		"Name":"SnowGrassBiome",
		"Layering":"SnowLayering",
		"Props": "SnowGrassGenerator"
	},
	{
		"Class":"Biome",
		"Name":"SnowForestBiome",
		"Layering":"SnowLayering",
		"Props": "SnowForestGenerator"
	},
	
	# jungle
	{
		"Class":"Biome",
		"Name":"DipteroBiome",
		"Layering":"DipteroLayering",
		"Props":"DipteroProps",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"BrokenLandBiome",
		"Layering":"BrokenLandLayeringBasalt",
		"Props":"VolcanicProps"
	}
	
	# volcano
	,{
		"Class":"Biome",
		"Name":"VolcanoBiome",
		"Layering":"VolcanicLayeringBasalt"
	}
	
	# sea
	,{
		"Class":"Biome",
		"Name":"SeaBiome",
		"Layering":"SeaBottomLayeringSand",
		"Props":"SeaPlantProps"
	},{
		"Class":"Biome",
		"Name":"SeaGrassBiome",
		"Layering":"SeaBottomLayeringSand",
		"Props":"SeaGrassProps"
	},{
		"Class":"Biome",
		"Name":"EmptySeaBiome",
		"Layering":"SeaBottomLayeringSand",
		"Props":"EmptySeaProps"
	},{
		"Class":"Biome",
		"Name":"GravelSeaBiome",
		"Layering":"SeaBottomLayeringGravel"
	},{
		"Class":"Biome",
		"Name":"SeaPlantBiome",
		"Layering":"SeaBottomLayeringSand",
		"Props":"SeaPlantProps"
	}
	
	# grass
	,{
		"Class":"Biome",
		"Name":"HillsBiome",
		"Layering":"HillsLayering",
		"Props":"HillsProps",
		"Color":[184/255.0, 255/255.0, 133/255.0]
	},{
		"Class":"Biome",
		"Name":"HillsForestBiome",
		"Layering":"HillsLayering",
		"Props":"HillsForestProps",
		"Color":[184/255.0, 255/255.0, 133/255.0]
	},{
		"Class":"Biome",
		"Name":"MountainsStoneBiome",
		"Layering":"MountainStoneLayering",
		"Props":"MountainProps",
		"SurfaceRockDetail": 2.5
	},{
		"Class":"Biome",
		"Name":"MountainsDarkStoneBiome",
		"Layering":"MountainDarkStoneLayering",
		"Props":"MountainDarkProps",
		"SurfaceRockDetail": 2.5
	},{
		"Class":"Biome",
		"Name":"MountainsLayeredBiome",
		"Layering":"MountainLayeredLayering",
		"Props":"MountainProps",
		"SurfaceRockDetail": 2.5
	},{
		"Class":"Biome",
		"Name":"MountainsSnowBiome",
		"Layering":"MountainSnowLayering",
		"Props":"MountainSnowProps",
		# snow cover softens the crags a bit
		"SurfaceRockDetail": 1.5
	},	{
		"Class":"Biome",
		"Name":"BogBiome",
		"Layering":"BogGrassLayeringGrass",
		"Props":"BogProps",
		"WaterMurkiness": 1.0,
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"PeatBiome",
		"Layering":"PeatLayering",
		"Props":"OreProps"
	},{
		"Class":"Biome",
		"Name":"ClayBiome",
		"Layering":"ClayLowlandLayering",
		"Props":"ClayProps"
	},{
		"Class":"Biome",
		"Name":"BogForestBiome",
		"Layering":"BogGrassLayeringGrass",
		"Props":"BogForestProps",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"PineForestBiome",
		"Layering":"JustGrassLayeringPine",
		"Props":"PineForestProps"
	},{
		"Class":"Biome",
		"Name":"ForestBiome",
		"Layering":"GrassLayering",
		"Props":"ForestProps",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"BushlandBiome",
		"Layering":"GrassLayering",
		"Props":"BushlandProps",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"FertileForestBiome",
		"Layering":"GrassLayering",
		"Props":"FertileForestProps",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},
	
	# plains
	{
		"Class":"Biome",
		"Name":"PlainsBiome",
		"Layering":"GrassLayering",
		"Props":"GrasslandProps"
	},{
		"Class":"Biome",
		"Name":"RedPlainsBiome",
		"Layering":"GrassLayering",
		"Props":"GrasslandPropsRed"
	},{
		"Class":"Biome",
		"Name":"WhitePlainsBiome",
		"Layering":"GrassLayering",
		"Props":"GrasslandPropsWhite"
	},{
		"Class":"Biome",
		"Name":"YellowPlainsBiome",
		"Layering":"GrassLayering",
		"Props":"GrasslandPropsYellow"
	},
	
	# desert
	{
		"Class":"Biome",
		"Name":"DesertBiome",
		"Layering":"SandDesertLayeringSand",
		"Props":"SandlandProps"
	},

	# moon
	{
		"Class":"Biome",
		"Name":"MoonRegolithBiome",
		"Layering":"RegolithLayering",
		"Color":[0.62, 0.62, 0.64]
	},
	
	# river
	{
		"Class":"Biome",
		"Name":"RiverBiome",
		"Layering":"RiverLayeringSand"
	}
])

# Assign a height generator to each leaf biome (sea biomes stay flat: omitted,
# so they contribute zero detail and remain at the reference sea floor).
biome_height = {
	"PrairieDryPlainsBiome": "PrairieHeight",
	"PrairiePlainsBiome":    "PrairieHeight",
	"PrairieDryHillsBiome":  "PrairieHillsHeight",
	"PineForestBiome":       "PineForestHeight",
	"ForestBiome":           "ForestHeight",
	"SnowBiome":             "SnowHeight",
	"SnowGrassBiome":        "SnowHeight",
	"SnowForestBiome":       "SnowHeight",
	"DipteroBiome":          "ForestHeight",
	"BrokenLandBiome":       "VolcanicHeight",
	"VolcanoBiome":          "VolcanicHeight",
	"HillsBiome":            "HillsHeight",
	"HillsForestBiome":      "HillsHeight",
	"MountainsStoneBiome":     "MountainsHeight",
	"MountainsDarkStoneBiome": "MountainsHeight",
	"MountainsLayeredBiome":   "MountainsHeight",
	"MountainsSnowBiome":      "MountainsHeight",
	"BogBiome":              "SwampHeight",
	"PeatBiome":             "SwampHeight",
	"ClayBiome":             "SwampHeight",
	"BogForestBiome":        "SwampHeight",
	"BushlandBiome":         "ForestHeight",
	"FertileForestBiome":    "FertileForestHeight",
	"PlainsBiome":           "PlainHeight",
	"RedPlainsBiome":        "PlainHeight",
	"WhitePlainsBiome":      "PlainHeight",
	"YellowPlainsBiome":     "PlainHeight",
	"DesertBiome":           "SandHeight",
	"RiverBiome":            "PlainHeight",
	"MoonRegolithBiome":     "MoonCraterHeight",
}
for b in biomes:
	h = biome_height.get(b["Name"])
	if h:
		b["Height"] = h

data = {
	"Objects": generators
}

write_file("Generated/Generators/vanilla.json", data)

data = {
	"Objects": biomes
}

write_file("Generated/Biomes/vanilla.json", data)

data = {
	"Objects": families
}

write_file("Generated/BiomeFamilies/vanilla.json", data)

data = {
	"Objects": global_family
}

write_file("Generated/GlobalBiomFamily/vanilla.json", data)