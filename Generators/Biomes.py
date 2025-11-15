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
		"Name":"PrairieBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"PrairieDryPlainsBiome",
			"PrairieDryHillsBiome",
			"PrairiePlainsBiome",
		],
		"ChildFrequency": biome_family_size,
		"Weather": ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain"]
	},	{
		"Name":"SandBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"DesertBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather": ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain"]
	},	{
		"Name":"ForestBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"ForestBiome",
			"PlainsBiome",
			"BushlandBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather": ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "Foggy"]
	},	{
		"Name":"PineForestBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"PineForestBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather": ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "Foggy"]
	},	{
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
		"Weather": ["Clear", "SlightlyCloudy", "PartlyCloudy", "LightRain", "Foggy"]
	},	{
		"Name":"VolcanicBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"VolcanoBiome",
			"BrokenLandBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather": ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "Storm"]
	},	{
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
		"Weather": ["Overcast", "LightRain", "Rain", "Foggy", "ExtremeFoggy"]
	},	{
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
		"Weather": ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "LightRain"]
	},	{
		"Name":"SnowBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"SnowBiome",
			"SnowGrassBiome",
			"SnowForestBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather": ["Clear", "SlightlyCloudy", "PartlyCloudy", "Foggy", "ExtremeFoggy"]
	},
	{
		"Name":"FertileForestBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"FertileForestBiome"
		],
		"ChildFrequency": biome_family_size,
		"Weather": ["Clear", "SlightlyCloudy", "PartlyCloudy", "Overcast", "Foggy"]
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