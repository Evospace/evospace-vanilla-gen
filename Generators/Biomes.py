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
climate_niches = [
	{"Temperature": 0.06, "Humidity": 0.28, "Weight": -0.006, "Leaves": ["SnowBiome"]},
	{"Temperature": 0.06, "Humidity": 0.72, "Weight": -0.006, "Leaves": ["SnowForestBiome", "SnowGroveBiome"]},
	{"Temperature": 0.28, "Humidity": 0.18, "Leaves": ["TundraBiome"]},
	{"Temperature": 0.28, "Humidity": 0.5, "Leaves": ["ForestTundraBiome"]},
	{"Temperature": 0.28, "Humidity": 0.8, "Leaves": ["PineForestBiome"]},
	{"Temperature": 0.5, "Humidity": 0.1, "Leaves": ["PrairieDryPlainsBiome", "PrairiePlainsBiome"]},
	{"Temperature": 0.5, "Humidity": 0.3, "Leaves": ["ForestSteppeBiome"]},
	{"Temperature": 0.5, "Humidity": 0.5, "Weight": 0.006, "Leaves": ["PlainsBiome"]},
	{"Temperature": 0.5, "Humidity": 0.7, "Leaves": ["ForestBiome"]},
	{"Temperature": 0.5, "Humidity": 0.9, "Leaves": ["BogBiome", "BogForestBiome"]},
	{"Temperature": 0.72, "Humidity": 0.1, "Leaves": ["SemiDesertBiome"]},
	{"Temperature": 0.72, "Humidity": 0.3, "Leaves": ["SavannaBiome"]},
	{"Temperature": 0.72, "Humidity": 0.5, "Leaves": ["RedPlainsBiome", "WhitePlainsBiome", "YellowPlainsBiome"]},
	{"Temperature": 0.72, "Humidity": 0.7, "Leaves": ["BushlandBiome"]},
	{"Temperature": 0.72, "Humidity": 0.9, "Leaves": ["PeatBiome", "ClayBiome"]},
	{"Temperature": 0.92, "Humidity": 0.15, "Leaves": ["DesertBiome"]},
	{"Temperature": 0.92, "Humidity": 0.48, "Leaves": ["WoodlandBiome"]},
	{"Temperature": 0.92, "Humidity": 0.7, "Leaves": ["FertileForestBiome"]},
	{"Temperature": 0.92, "Humidity": 0.9, "Leaves": ["DipteroBiome"]},
]
climate_sea = {
	"Cold": "GravelSeaBiome", "ColdBelow": 0.18,
	"Shallow": "SeaGrassBiome", "ShallowAbove": -6,
	"Deep": "EmptySeaBiome", "DeepBelow": -16,
	"Open": "SeaBiome",
}
climate_mountains = {
	"Snow": "MountainsSnowBiome", "SnowBelow": 0.22,
	"Dry": "MountainsLayeredBiome", "DryBelow": 0.35,
	"Wet": "MountainsDarkStoneBiome", "WetAbove": 0.7,
	"Rock": "MountainsStoneBiome",
	"Height": "ClimateMountainHeight",
	"Erosion": {"Strength": 26.0, "CellBlocks": 128, "Octaves": 3, "Gain": 0.5, "Lacunarity": 2.0, "SlopeStart": 0.02, "SlopeFull": 0.25,
	            "ShoreHeight": 1.0, "ShoreBlend": 3.0, "Branching": 1.0, "Relief": 60.0, "SharpRidges": True},
}
climate_volcanic = {
	"Core": "VolcanoBiome", "Rim": "BrokenLandBiome",
	"Frequency": 0.0011, "Share": 0.07, "CoreShare": 0.35, "MinHeight": 3,
}
climate_childs = []
climate_shelves = [
	{"Name": "Lowland",    "Uplift": 0.40, "Blocks": 0,  "Height": "ShelfLowlandHeight"},
	{"Name": "LowTerrace", "Uplift": 0.54, "Blocks": 12, "Height": "ShelfTerraceHeight"},
	{"Name": "Terrace",    "Uplift": 0.62, "Blocks": 16, "Height": "ShelfTerraceHeight"},
	{"Name": "Upland",     "Uplift": 0.74, "Blocks": 34, "Height": "ShelfUplandHeight"},
	{"Name": "Highland",   "Uplift": 0.83, "Blocks": 48, "Height": "ShelfHighlandHeight"},
]
climate_leaf_relief = {
	"DesertBiome": "SandHeight",
	"SemiDesertBiome": "SandHeight",
	"BogBiome": "SwampHeight",
	"BogForestBiome": "SwampHeight",
	"PeatBiome": "SwampHeight",
	"ClayBiome": "SwampHeight",
	"SnowBiome": "SnowHeight",
	"SnowForestBiome": "SnowForestHeight",
	"SnowGroveBiome": "SnowForestHeight",
	"VolcanoBiome": "VolcanicHeight",
	"BrokenLandBiome": "VolcanicHeight",
}
for leaf in [l for n in climate_niches for l in n["Leaves"]] + [v for g in (climate_sea, climate_mountains, climate_volcanic) for k, v in g.items() if isinstance(v, str) and k != "Height"]:
	if leaf not in climate_childs:
		climate_childs.append(leaf)

global_family.append({
		"Name":"GlobalBiomeMegaFamilyClimate",
		"Class":"GlobalBiomeFamilyClimate",
		"Childs": climate_childs,
        "ChildFrequency": mega_boime_size,
		"Climate": {
			"TemperatureFrequency": 0.0005,
			"HumidityFrequency": 0.0007,
			"TemperatureSpread": 1.15,
			"HumiditySpread": 1.1,
			"WarpFrequency": 0.0025,
			"WarpAmp": 90,
			"JitterFrequency": 0.05,
			"JitterAmp": 0.03,
			"VariantFrequency": 0.005,
			"LapseRate": 0.0045,
			"LapseStart": 18,
			"CoastWet": 0.22,
			"CoastBand": 0.12,
			"InlandDry": 0.12,
			"InlandStart": 0.15,
			"InlandBand": 0.3,
		},
		"Shelves": climate_shelves,
		"LeafRelief": climate_leaf_relief,
		"Niches": climate_niches,
		"Sea": climate_sea,
		"Mountains": climate_mountains,
		"Volcanic": climate_volcanic,
	})
global_family.append({
		"Name":"GlobalBiomeMegaFamilyMoon",
		"Class":"GlobalBiomeFamilyMoon",
		"Childs": ["MoonHighlandBiome", "MoonMareBiome"],
        "ChildFrequency": mega_boime_size,
		"WeatherLooks": ["Clear", "Clear", "Clear", "Clear", "Clear"],
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
		"WeatherLooks": ["Clear", "SlightlyCloudy", "Overcast", "LightRain", "Rain"],
	},	{
		# Hot desert: mostly clear, then fair-weather clouds on Light, thicker
		# broken cover on Overcast, dust for the wet bands. No rain/fog looks —
		# precipitation maps to DustHaze / SandStorm instead.
		"Name":"SandBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"DesertBiome"
		],
		"ChildFrequency": biome_family_size,
		"WeatherLooks": ["Clear", "SlightlyCloudy", "PartlyCloudy", "DustHaze", "SandStorm"],
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
		"WeatherLooks": ["Clear", "SlightlyCloudy", "Overcast", "LightRain", "Rain"],
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
		"WeatherLooks": ["SlightlyCloudy", "LightLowFog", "Overcast", "LightRain", "Rain"],
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
		"WeatherLooks": ["Clear", "SlightlyCloudy", "Overcast", "Rain", "Storm"],
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
		"WeatherLooks": ["SlightlyCloudy", "PartlyCloudy", "Overcast", "Foggy", "Storm"],
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
		"WeatherLooks": ["PartlyCloudy", "Overcast", "LightRain", "Rain", "Storm"],
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
		"WeatherLooks": ["Clear", "SlightlyCloudy", "Overcast", "LightRain", "Storm"],
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
		"WeatherLooks": ["Clear", "SlightlyCloudy", "Overcast", "Snowfall", "Blizzard"],
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
		"WeatherLooks": ["SlightlyCloudy", "PartlyCloudy", "Overcast", "Rain", "Storm"],
	},
	{
		# Flat concrete wasteland world: keep weather variants strictly clear-only
		"Name":"WastelandBiomeFamily",
		"Class":"BiomeFamily",
		"Childs": [],
		"ChildFrequency": biome_family_size,
		"WeatherLooks": ["Clear", "Clear", "Clear", "Clear", "Clear"],
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
		"WeatherLooks": ["Clear", "SlightlyCloudy", "Overcast", "LightRain", "Rain"],
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
		"WeatherLooks": ["Clear", "SlightlyCloudy", "Overcast", "Foggy", "ExtremeFoggy"],
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
	{
		"Class": "LowlandLayeringGenerator",
		"Name": "SemiDesertLayering",
		"Blocks": ["SandyDryGrassSurface" + static_surface, "DirtSurface" + static_surface, "SandstoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 5, 9, 12, 16, 19, 23, 30],
		"LowBlocks": ["DesertSandSurface" + static_surface, "SandstoneSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"LowStarts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
		"Height": "SemiDesertPatchHeight",
		"Below": 0.0,
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
		"Name": "MoonHighlandLayering",
		"Blocks": ["LimestoneSurface" + static_surface, "StoneSurface" + static_surface,
		           "DarkStoneSurface" + static_surface, "StoneSurface" + static_surface],
		"Starts": [0, 3, 10, 22]
	},
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "MoonMareLayering",
		"Blocks": ["BasaltSurface" + static_surface, "DarkStoneSurface" + static_surface,
		           "StoneSurface" + static_surface],
		"Starts": [0, 6, 18]
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
		if "FractalGain" in l:
			entry["FractalGain"] = l["FractalGain"]
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
add_height("PlainHeight",        [{"Frequency": 0.012, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0,  "Max": 4}])
add_height("PrairieHeight",      [{"Frequency": 0.010, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0,  "Max": 4}])
add_height("PrairieHillsHeight", [{"Frequency": 0.013, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 2,  "Max": 4}])
add_height("ForestHeight",       [{"Frequency": 0.009, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0,  "Max": 4},
                                  {"Frequency": 0.030, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0,  "Max": 1.5}])
# Gently rolling, morainic relief: a broad swell plus low hummocks under the canopy
add_height("PineForestHeight",   [{"Frequency": 0.006, "FractalOctaves": 3, "FractalGain": 0.35, "Min": -3, "Max": 6},
                                  {"Frequency": 0.022, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0,  "Max": 1.5}])
add_height("SnowHeight",         [{"Frequency": 0.0035, "FractalOctaves": 3, "FractalGain": 0.4, "Min": -3, "Max": 7},
                                  {"Frequency": 0.011, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0, "Max": 2},
                                  {"Frequency": 0.008, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0, "Max": 10, "Power": 8, "SeedOffset": 6113}])
add_height("SnowForestHeight",   [{"Frequency": 0.005, "FractalOctaves": 3, "FractalGain": 0.4, "Min": -3, "Max": 6},
                                  {"Frequency": 0.02, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0, "Max": 1.2}])
add_height("SandHeight",         [{"NoiseType": "Cellular", "FractalOctaves": 2, "Frequency": 0.040, "CellularReturnType": "Distance",
                                  "CellularDistanceFunction": "Natural", "CellularJitter": 0.75, "Min": -2, "Max": 2}])
# Flat wetland base plus rare circular lake basins carved by a sparse cellular field.
add_height("SwampHeight",        [{"Frequency": 0.020, "FractalOctaves": 2, "Min": -2, "Max": 3},
                                  {"NoiseType": "Cellular", "Frequency": 0.0035, "FractalOctaves": 1,
                                   "CellularReturnType": "Distance2Cave", "CellularDistanceFunction": "Natural",
                                   "CellularJitter": 0.55, "Min": 0, "Max": -7, "Power": 5, "SeedOffset": 4201}])
add_height("VolcanicHeight",     [{"Frequency": 0.01, "FractalOctaves": 5, "Min": -4,  "Max": 4},
                                  {"Frequency": 0.05, "FractalOctaves": 2, "Min": 1,  "Max": 10, "Power": 10}])
add_height("FertileForestHeight",[{"Frequency": 0.009, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0,  "Max": 4}])

# Moderate rolling hills (gameplay_mountains_plan: foothill relief, rounded silhouettes).
add_height("HillsHeight",        [{"Frequency": 0.010, "FractalOctaves": 4, "Min": -8,  "Max": 12},
                                  {"Frequency": 0.025, "FractalOctaves": 2, "Min": -4,  "Max": 8}])
# Ridged foothill / mountain detail for MountainsBiomeFamily (configurable generator).
add_height("MountainsHeight",    [{"Frequency": 0.006, "FractalOctaves": 5, "FractalType": "Ridged", "Min": -2, "Max": 24, "Power": 2},
                                  {"Frequency": 0.015, "FractalOctaves": 3, "Min": -3,  "Max": 12, "Power": 1}])
# Basin-only field for the clay biome's lowland layering. MUST mirror SwampHeight's
# second (basin) layer exactly — same noise params AND SeedOffset — so the clay
# patches line up with the actual carved basins of the clay terrain (ClayBiome
# uses SwampHeight). The flat fbm layer of SwampHeight is intentionally omitted
# here so only the real depressions read as "lowland" (not random fbm dips).
add_height("ClayBasinHeight",    [{"NoiseType": "Cellular", "Frequency": 0.0035, "FractalOctaves": 1,
                                   "CellularReturnType": "Distance2Cave", "CellularDistanceFunction": "Natural",
                                   "CellularJitter": 0.55, "Min": 0, "Max": -7, "Power": 5, "SeedOffset": 4201}])
add_height("ShelfLowlandHeight",  [{"Frequency": 0.005, "FractalOctaves": 2, "FractalGain": 0.4, "Min": -1, "Max": 2, "SeedOffset": 7401}])
add_height("ShelfTerraceHeight",  [{"Frequency": 0.009, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0, "Max": 4, "SeedOffset": 7411},
                                   {"Frequency": 0.030, "FractalOctaves": 2, "FractalGain": 0.35, "Min": 0, "Max": 1.5, "SeedOffset": 7412}])
add_height("ShelfUplandHeight",   [{"Frequency": 0.008, "FractalOctaves": 3, "Min": -3, "Max": 8, "SeedOffset": 7421},
                                   {"Frequency": 0.022, "FractalOctaves": 2, "Min": 0, "Max": 3, "SeedOffset": 7422}])
add_height("ShelfHighlandHeight", [{"Frequency": 0.007, "FractalOctaves": 4, "Min": -4, "Max": 10, "SeedOffset": 7431},
                                   {"Frequency": 0.020, "FractalOctaves": 3, "FractalType": "Ridged", "Min": 0, "Max": 4, "SeedOffset": 7432}])
add_height("ClimateMountainHeight", [{"Frequency": 0.011, "FractalOctaves": 3, "FractalType": "Ridged", "Min": 0, "Max": 4, "Power": 2, "SeedOffset": 7301}])
add_height("SemiDesertPatchHeight", [{"Frequency": 0.03, "FractalOctaves": 2, "Min": -1, "Max": 1, "SeedOffset": 5303}])

# noises + height generators load first (single-pass-safe ordering)
generators = height_noises + height_gens + generators

dry_sources = {"OreList": "OreProps", "StoneSource": "StoneSurface"}
world_sources = {**dry_sources, "WaterSource": "Water"}
generators.extend([
	{"Class": "WorldGeneratorRivers", "Name": "WorldGeneratorRivers", "GlobalBiome": "GlobalBiomeMegaFamily2", "UnderworldBlock": "GraniteSurface", **world_sources},
	{"Class": "WorldGeneratorLegacy", "Name": "WorldGeneratorBiome", "GlobalBiome": "GlobalBiomeMegaFamily", "UnderworldBlock": "GraniteSurface", **world_sources},
	{"Class": "WorldGeneratorPlains", "Name": "WorldGeneratorPlains", "GlobalBiome": "GlobalBiomeMegaFamily3", "UnderworldBlock": "GraniteSurface", **world_sources},
	{"Class": "WorldGeneratorMoon", "Name": "WorldGeneratorMoon", "GlobalBiome": "GlobalBiomeMegaFamilyMoon", "UnderworldBlock": "GraniteSurface", **dry_sources},
	{"Class": "WorldGeneratorConfigurable", "Name": "WorldGeneratorConfigurable", "GlobalBiome": "GlobalBiomeMegaFamilyConfigurable", "UnderworldBlock": "GraniteSurface", **world_sources},
	{"Class": "WorldGeneratorClimate", "Name": "WorldGeneratorClimate", "GlobalBiome": "GlobalBiomeMegaFamilyClimate", "UnderworldBlock": "GraniteSurface", **world_sources,
	 "Erosion": {"Strength": 2.0, "CellBlocks": 40, "Octaves": 2, "Gain": 0.5, "Lacunarity": 2.0, "SlopeStart": 0.08, "SlopeFull": 0.3,
	             "ShoreHeight": 1.0, "ShoreBlend": 3.0, "Branching": 1.0}},
	{"Class": "FlatWorldGenerator", "Name": "FlatWorldGenerator", "Layers": [{"Block": "ReinforcedConcrete", "Height": 3}], "Biome": "WastelandBiomeFamily", **world_sources},
	{"Class": "WorldGeneratorOrbit", "Name": "WorldGeneratorOrbit", "PlatformBlock": "Concrete", "Biome": "WastelandBiomeFamily", **dry_sources},
])

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
		"Props":"PineForestProps"	},{
		"Class":"Biome",
		"Name":"ForestBiome",
		"Layering":"GrassLayering",
		"Props":"ForestProps"	},
	
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
	{
		"Class":"Biome",
		"Name":"SnowGroveBiome",
		"Layering":"SnowLayering",
		"Props": "SnowGroveGenerator"
	},
	
	# jungle
	{
		"Class":"Biome",
		"Name":"DipteroBiome",
		"Layering":"DipteroLayering",
		"Props":"DipteroProps"	},{
		"Class":"Biome",
		"Name":"BrokenLandBiome",
		"DrillSource":"BasaltSurface",
		"Layering":"BrokenLandLayeringBasalt",
		"Props":"VolcanicProps"
	}
	
	# volcano
	,{
		"Class":"Biome",
		"Name":"VolcanoBiome",
		"DrillSource":"BasaltSurface",
		"Layering":"VolcanicLayeringBasalt"
	}
	
	# sea
	,{
		"Class":"Biome",
		"Name":"SeaBiome",
		"DrillSource":"SandSurface",
		"Layering":"SeaBottomLayeringSand",
		"Props":"SeaPlantProps"
	},{
		"Class":"Biome",
		"Name":"SeaGrassBiome",
		"DrillSource":"SandSurface",
		"Layering":"SeaBottomLayeringSand",
		"Props":"SeaGrassProps"
	},{
		"Class":"Biome",
		"Name":"EmptySeaBiome",
		"DrillSource":"SandSurface",
		"Layering":"SeaBottomLayeringSand",
		"Props":"EmptySeaProps"
	},{
		"Class":"Biome",
		"Name":"GravelSeaBiome",
		"Layering":"SeaBottomLayeringGravel"
	},{
		"Class":"Biome",
		"Name":"SeaPlantBiome",
		"DrillSource":"SandSurface",
		"Layering":"SeaBottomLayeringSand",
		"Props":"SeaPlantProps"
	}
	
	# grass
	,{
		"Class":"Biome",
		"Name":"HillsBiome",
		"Layering":"HillsLayering",
		"Props":"HillsProps"	},{
		"Class":"Biome",
		"Name":"HillsForestBiome",
		"Layering":"HillsLayering",
		"Props":"HillsForestProps"	},{
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
		"WaterMurkiness": 1.0	},{
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
		"Props":"BogForestProps"	},{
		"Class":"Biome",
		"Name":"PineForestBiome",
		"Layering":"JustGrassLayeringPine",
		"Props":"PineForestProps"
	},{
		"Class":"Biome",
		"Name":"ForestBiome",
		"Layering":"GrassLayering",
		"Props":"ForestProps"	},{
		"Class":"Biome",
		"Name":"BushlandBiome",
		"Layering":"GrassLayering",
		"Props":"BushlandProps"	},{
		"Class":"Biome",
		"Name":"FertileForestBiome",
		"Layering":"GrassLayering",
		"Props":"FertileForestProps"	},
	
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
		"DrillSource":"SandSurface",
		"Layering":"SandDesertLayeringSand",
		"Props":"SandlandProps"
	},

	# climate transitions
	{
		"Class":"Biome",
		"Name":"TundraBiome",
		"Layering":"DryGrassLayering",
		"Props":"TundraProps"
	},{
		"Class":"Biome",
		"Name":"ForestTundraBiome",
		"Layering":"JustGrassLayeringPine",
		"Props":"ForestTundraProps"
	},{
		"Class":"Biome",
		"Name":"ForestSteppeBiome",
		"Layering":"GrassLayering",
		"Props":"ForestSteppeProps"
	},{
		"Class":"Biome",
		"Name":"SemiDesertBiome",
		"DrillSource":"SandSurface",
		"Layering":"SemiDesertLayering",
		"Props":"SemiDesertProps"
	},{
		"Class":"Biome",
		"Name":"SavannaBiome",
		"Layering":"DryGrassLayering",
		"Props":"SavannaProps"
	},{
		"Class":"Biome",
		"Name":"WoodlandBiome",
		"Layering":"GrassLayering",
		"Props":"WoodlandProps"
	},

	# moon
	{
		"Class":"Biome",
		"Name":"MoonHighlandBiome",
		"Layering":"MoonHighlandLayering"
	},
	{
		"Class":"Biome",
		"Name":"MoonMareBiome",
		"DrillSource":"BasaltSurface",
		"Layering":"MoonMareLayering"
	},

	
	# river
	{
		"Class":"Biome",
		"Name":"RiverBiome",
		"DrillSource":"SandSurface",
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
	"SnowGrassBiome":        "SnowForestHeight",
	"SnowForestBiome":       "SnowForestHeight",
	"SnowGroveBiome":        "SnowForestHeight",
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
	"TundraBiome":           "PrairieHeight",
	"ForestTundraBiome":     "PineForestHeight",
	"ForestSteppeBiome":     "ForestHeight",
	"SemiDesertBiome":       "SandHeight",
	"SavannaBiome":          "PrairieHeight",
	"WoodlandBiome":         "ForestHeight",
}
for b in biomes:
	h = biome_height.get(b["Name"])
	if h:
		b["Height"] = h

# Looks are authored per family, but the weather controller asks the leaf biome under the camera.
looks_by_biome = {}
for f in families + [g for g in global_family if "WeatherLooks" in g]:
	for child in f.get("Childs", []):
		looks_by_biome.setdefault(child, f["WeatherLooks"])

# Snow-capped mountains share the mountain family height/props, but their
# precipitation bands are snow (same as SnowBiomeFamily), not plain fog.
looks_by_biome["MountainsSnowBiome"] = ["Clear", "SlightlyCloudy", "Overcast", "Snowfall", "Blizzard"]
looks_by_biome["TundraBiome"] = ["Clear", "SlightlyCloudy", "Overcast", "Snowfall", "Blizzard"]
looks_by_biome["SnowGroveBiome"] = ["Clear", "SlightlyCloudy", "Overcast", "Snowfall", "Blizzard"]
looks_by_biome["ForestTundraBiome"] = ["SlightlyCloudy", "LightLowFog", "Overcast", "Snowfall", "Blizzard"]
looks_by_biome["ForestSteppeBiome"] = ["Clear", "SlightlyCloudy", "Overcast", "LightRain", "Rain"]
looks_by_biome["SemiDesertBiome"] = ["Clear", "SlightlyCloudy", "PartlyCloudy", "DustHaze", "SandStorm"]
looks_by_biome["SavannaBiome"] = ["Clear", "SlightlyCloudy", "PartlyCloudy", "Rain", "Storm"]
looks_by_biome["WoodlandBiome"] = ["Clear", "SlightlyCloudy", "PartlyCloudy", "LightRain", "Rain"]
looks_by_biome["DipteroBiome"] = ["SlightlyCloudy", "PartlyCloudy", "Overcast", "Rain", "Storm"]

default_looks = ["Clear", "SlightlyCloudy", "Overcast", "LightRain", "Rain"]
for b in biomes:
	b["WeatherLooks"] = looks_by_biome.get(b["Name"], default_looks)

def map_mix(a, b, t):
	return [round(a[i] + (b[i] - a[i]) * t, 3) for i in range(3)]

def map_scale(a, k):
	return [round(v * k, 3) for v in a]

map_sea = [0.329, 0.918, 0.969]
map_snow = [1.843, 1.958, 2.0]
map_prairie = [0.219, 0.091, 0.026]
map_pine = [0.433, 0.5, 0.154]
map_plain = [0.272, 0.672, 0.469]
map_desert = [2.0, 0.576, 0.0]
map_forest = [0.212, 0.536, 0.126]
map_swamp = [0.029, 0.099, 0.045]
map_volcano = [0.281, 0.125, 0.235]
map_fertile = [0.649, 1.0, 0.052]
map_hills = [1.057, 1.104, 0.772]
map_mountains = [2.723, 2.942, 3.0]

map_colors = {
	"SeaBiomeFamily": map_sea,
	"SnowBiomeFamily": map_snow,
	"PrairieBiomeFamily": map_prairie,
	"PineForestBiomeFamily": map_pine,
	"PlainBiomeFamily": map_plain,
	"SandBiomeFamily": map_desert,
	"ForestBiomeFamily": map_forest,
	"SwampBiomeFamily": map_swamp,
	"VolcanicBiomeFamily": map_volcano,
	"FertileForestBiomeFamily": map_fertile,
	"HillsBiomeFamily": map_hills,
	"MountainsBiomeFamily": map_mountains,
	"WastelandBiomeFamily": [1.0, 0.0, 1.0],

	"SeaBiome": map_sea,
	"SeaGrassBiome": map_mix(map_sea, map_plain, 0.25),
	"EmptySeaBiome": map_scale(map_sea, 0.75),
	"GravelSeaBiome": map_mix(map_sea, [0.5, 0.5, 0.5], 0.4),
	"SeaPlantBiome": map_mix(map_sea, map_plain, 0.15),
	"SnowBiome": map_snow,
	"SnowGrassBiome": map_mix(map_snow, map_pine, 0.3),
	"SnowForestBiome": map_mix(map_snow, map_pine, 0.5),
	"SnowGroveBiome": map_mix(map_snow, map_pine, 0.4),
	"TundraBiome": map_mix(map_snow, map_prairie, 0.6),
	"ForestTundraBiome": map_mix(map_snow, map_pine, 0.7),
	"PineForestBiome": map_pine,
	"PrairieDryPlainsBiome": map_prairie,
	"PrairieDryHillsBiome": map_scale(map_prairie, 1.2),
	"PrairiePlainsBiome": map_mix(map_prairie, map_plain, 0.25),
	"ForestSteppeBiome": map_mix(map_prairie, map_forest, 0.5),
	"PlainsBiome": map_plain,
	"RedPlainsBiome": map_mix(map_plain, [0.8, 0.25, 0.2], 0.5),
	"WhitePlainsBiome": map_mix(map_plain, [1.0, 1.0, 1.0], 0.5),
	"YellowPlainsBiome": map_mix(map_plain, [1.0, 0.9, 0.1], 0.5),
	"ForestBiome": map_forest,
	"BushlandBiome": map_mix(map_forest, map_plain, 0.5),
	"BogBiome": map_swamp,
	"BogForestBiome": map_scale(map_swamp, 1.5),
	"PeatBiome": [0.06, 0.05, 0.03],
	"ClayBiome": [0.14, 0.08, 0.05],
	"DesertBiome": map_desert,
	"SemiDesertBiome": map_mix(map_desert, map_prairie, 0.4),
	"SavannaBiome": map_mix(map_desert, map_plain, 0.45),
	"WoodlandBiome": map_mix(map_fertile, map_prairie, 0.5),
	"FertileForestBiome": map_fertile,
	"DipteroBiome": map_scale(map_fertile, 0.65),
	"VolcanoBiome": map_volcano,
	"BrokenLandBiome": map_scale(map_volcano, 1.5),
	"HillsBiome": map_hills,
	"HillsForestBiome": map_mix(map_hills, map_forest, 0.5),
	"MountainsStoneBiome": map_mountains,
	"MountainsDarkStoneBiome": map_scale(map_mountains, 0.45),
	"MountainsLayeredBiome": [2.4, 1.8, 1.5],
	"MountainsSnowBiome": map_scale(map_mountains, 1.1),
	"MoonHighlandBiome": [0.62, 0.62, 0.64],
	"MoonMareBiome": [0.32, 0.32, 0.34],
	"RiverBiome": map_plain,
}
for entry in biomes + families:
	entry["Color"] = map_colors[entry["Name"]]

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