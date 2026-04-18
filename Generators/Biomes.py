from Common import *

global_family = []
families = []
families = []
biomes = []
generators = []
complexbiomes = []


mega_boime_size = 0.003
biome_family_size = 0.016

global_family.append({
		"Name":"GlobalBiomeMegaFamily",
		"Class":"GlobalBiomeFamily",
		"Childs":
		[
			"SeaBiomeFamily",
			"SnowBiomeFamily",
			"PrairieBiomeFamily",
			"PineForestBiomeFamily",
			"PlainBiomeFamily",
			"SandBiomeFamily",
			"ForestBiomeFamily",
			"SwampBiomeFamily",
			"VolcanicBiomeFamily",
            "FertileForestBiomeFamily"
		],
        "ChildFrequency": mega_boime_size,
	})
global_family.append({
		"Name":"GlobalBiomeMegaFamily2",
		"Class":"GlobalBiomeFamily2",
		"Childs":
		[
			"SeaBiomeFamily",
			"SnowBiomeFamily",
			"PrairieBiomeFamily",
			"PineForestBiomeFamily",
			"PlainBiomeFamily",
			"SandBiomeFamily",
			"ForestBiomeFamily",
			"SwampBiomeFamily",
			"VolcanicBiomeFamily",
            "FertileForestBiomeFamily"
		],
        "ChildFrequency": mega_boime_size,
	})
global_family.append({
		"Name":"GlobalBiomeMegaFamily3",
		"Class":"GlobalBiomeFamily3",
		"Childs":
		[
			"SeaBiomeFamily",
			"SnowBiomeFamily",
			"PrairieBiomeFamily",
			"PineForestBiomeFamily",
			"PlainBiomeFamily",
			"SandBiomeFamily",
			"ForestBiomeFamily",
			"SwampBiomeFamily",
			"VolcanicBiomeFamily",
            "FertileForestBiomeFamily"
		],
        "ChildFrequency": mega_boime_size,
	})
	
	#Sea = 0,
	#Taiga = 1,
	#Steppe = 2,
	#Pineforest = 3,
	#Grassland = 4,
	#Desert = 5,
	#Forest = 6,
	#TropicalForest = 7,
	#Volcano = 8,
    #FertileForest = 9,

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
	}
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
	
	# prairie
	{
		"Name":"PrairieDryProps",
		"Class": "PropsGenerator",
		"PropList": "PrairieDryPropList"
	},{
		"Name":"PrairieProps",
		"Class": "PropsGenerator",
		"PropList": "PrairiePropList"
	},
	
	# jungle
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "DipteroLayering",
		"Blocks": ["GrassSurface" + static_surface, "DirtSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},{
		"Name":"DipteroProps",
		"Class": "PropsGenerator",
		"PropList": "DipteroPropList"
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
		"Name":"BogProps",
		"Class": "PropsGenerator",
		"PropList": "SwampProps"
	},{
		"Name":"BogForestProps",
		"Class": "PropsGenerator",
		"PropList": "SwampForestProps"
	},{
		"Name":"OreProps",
		"Class": "PropsGenerator",
		"PropList": "ClayBeachProps"
	},
	
	# grass
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "JustGrassLayeringPine",
		"Blocks": ["PineForestSurface" + static_surface, "DirtSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},{
		"Name":"GrasslandProps",
		"Class":"PropsGenerator",
		"PropList": "GrasslandProps"
	},{
		"Name":"GrasslandPropsRed",
		"Class":"PropsGenerator",
		"PropList": "RedFlowersProps"
	},{
		"Name":"GrasslandPropsWhite",
		"Class":"PropsGenerator",
		"PropList": "WhiteFlowersProps"
	},{
		"Name":"GrasslandPropsYellow",
		"Class":"PropsGenerator",
		"PropList": "YellowFlowersProps"
	},{
		"Name":"BushlandProps",
		"Class":"PropsGenerator",
		"PropList": "BushlandProps"
	},{
		"Name":"ForestProps",
		"Class":"PropsGenerator",
		"PropList": "ForestProps"
	},{
		"Name":"PineForestProps",
		"Class":"PropsGenerator",
		"PropList": "PineForestProps"
	},{
		"Name":"FertileForestProps",
		"Class":"PropsGenerator",
		"PropList":"FertileForestProps"
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
	},{
		"Name": "SeaPlantProps",
		"Class": "PropsGenerator",
		"PropList": "SeaPlantProps"
	},{
		"Name": "SeaGrassProps",
		"Class": "PropsGenerator",
		"PropList": "SeaGrassProps"
	},{
		"Name": "EmptySeaProps",
		"Class": "PropsGenerator",
		"PropList": "EmptySeaProps"
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
	{
		"Name":"VolcanicProps",
		"Class":"PropsGenerator",
		"PropList": "VolcanicProps"
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
		"Name": "SandlandProps",
		"Class": "PropsGenerator",
		"PropList": "DesertProps"
	},
	
	# snow 
	{
		"Name": "SnowProps",
		"Class": "PropsGenerator",
		"PropList": "SnowProps"
	},
	{
		"Name": "SnowGrassGenerator",
		"Class": "PropsGenerator",
		"PropList": "SnowGrassProps"
	},
	{
		"Name": "SnowForestGenerator",
		"Class": "PropsGenerator",
		"PropList": "SnowForestProps"
	}
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
		"Layering":"GrassLayering",
		"Props":"GrasslandProps"
	},{
		"Class":"Biome",
		"Name":"MountainsBiome",
		"Layering":"GrassLayering"
	},{
		"Class":"Biome",
		"Name":"BogBiome",
		"Layering":"BogGrassLayeringGrass",
		"Props":"BogProps",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"PeatBiome",
		"Layering":"PeatLayering",
		"Props":"OreProps"
	},{
		"Class":"Biome",
		"Name":"ClayBiome",
		"Layering":"ClayLayering",
		"Props":"OreProps"
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
	
	# river
	{
		"Class":"Biome",
		"Name":"RiverBiome",
		"Layering":"RiverLayeringSand"
	}
])

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