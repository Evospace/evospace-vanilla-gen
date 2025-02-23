from Common import *

global_family = []
families = []
families = []
biomes = []
generators = []
complexbiomes = []


mega_boime_size = 0.007
biome_family_size = 0.016

global_family.append({
		"Name":"GlobalBiomeMegaFamily",
		"Class":"GlobalBiomeFamily",
		"Childs":
		[
			"SnowBiomeFamily",
			"SnowBiomeFamily",
			"PrairieBiomeFamily",
			"PineForestBiomeFamily",
			"PlainBiomeFamily", 
			"SandBiomeFamily",
			"ForestBiomeFamily",
			"SwampBiomeFamily", 
			"SeaBiomeFamily",
			"VolcanicBiomeFamily",
		]
	})
global_family.append({
		"Name":"GlobalBiomeMegaFamily2",
		"Class":"GlobalBiomeFamily2",
		"Childs":
		[
			"SnowBiomeFamily",
			"SnowBiomeFamily",
			"PrairieBiomeFamily",
			"PineForestBiomeFamily",
			"PlainBiomeFamily", 
			"SandBiomeFamily",
			"ForestBiomeFamily",
			"SwampBiomeFamily", 
			"SeaBiomeFamily",
			"VolcanicBiomeFamily",
		]
	})
global_family.append({
		"Name":"GlobalBiomeMegaFamily3",
		"Class":"GlobalBiomeFamily3",
		"Childs":
		[
			"SnowBiomeFamily",
			"SnowBiomeFamily",
			"PrairieBiomeFamily",
			"PineForestBiomeFamily",
			"PlainBiomeFamily", 
			"SandBiomeFamily",
			"ForestBiomeFamily",
			"SwampBiomeFamily", 
			"SeaBiomeFamily",
			"VolcanicBiomeFamily",
		]
	})
	
	#Tundra = 0, // (84, 234, 247)
	#Taiga = 1, // (5, 102, 33)
	#Steppe = 2, // (249, 218, 7)
	#Rainforest = 3, // (7, 249, 162)
	#Grassland = 4, // (155, 224, 35)
	#Desert = 5, // (250, 147, 23)
	#Forest = 6, // (46, 177, 83)
	#TropicalForest = 7, // (8, 250, 54)
	#Sea = 8, // (35, 48, 224)
	#Volcano = 9, // (255, 0, 0)

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
	},{
		"Name":"SandBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"DesertBiome",
			"MensaeBiome",
		],
		"ChildFrequency": biome_family_size,
	},{
		"Name":"ForestBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"DenseForestBiome",
			"PlainsBiome",
			"BushlandBiome",
		],
		"ChildFrequency": biome_family_size,
	},{
		"Name":"PineForestBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"PineForestBiome",
			"DensePineForestBiome",
		],
		"ChildFrequency": biome_family_size,
	},{
		"Name":"SeaBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"SeaBiome",
			"IslesBiome",
			"SeaGrassBiome",
			"EmptySeaBiome",
		],
		"ChildFrequency": biome_family_size,
	},{
		"Name":"VolcanicBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"VolcanoBiome",
			"BrokenLandBiome"
		],
		"ChildFrequency": biome_family_size,
	},{
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
	},{
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
	},{
		"Name":"SnowBiomeFamily",
		"Class":"BiomeFamily",
		"Childs":
		[
			"SnowBiome",
			"SnowGrassBiome",
			"SnowForestBiome"
		],
		"ChildFrequency": biome_family_size,
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
		"Blocks": ["SnowSurface" + static_surface, "DirtSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},
	
	# swamp
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "BogGrassLayeringGrass",
		"Blocks": ["BogSurface" + static_surface, "DirtSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},{
		"Class": "SimpleLayeringGenerator",
		"Name": "PeatLayering",
		"Blocks": ["CoalOre" + static_surface, "CoalOre" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 4, 9, 12, 16, 19, 23, 30]
	},{
		"Class": "SimpleLayeringGenerator",
		"Name": "ClayLayering",
		"Blocks": ["ClayOre" + static_surface, "ClayOre" + static_surface, "DarkStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 6, 9, 12, 16, 19, 23, 30]
	},{
		"Name":"BogPropsBase",
		"Class": "PropsGenerator",
		"PropList": "SwampProps"
	},{
		"Name":"BogForestPropsBase",
		"Class": "PropsGenerator",
		"PropList": "SwampForestProps"
	},{
		"Name":"OrePropsBase",
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
		"Name":"GrasslandPropsBase",
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
		"Name":"BushlandPropsBase",
		"Class":"PropsGenerator",
		"PropList": "BushlandProps"
	},{
		"Name":"ForestPropsBase",
		"Class":"PropsGenerator",
		"PropList": "ForestProps"
	},{
		"Name":"PineForestPropsBase",
		"Class":"PropsGenerator",
		"PropList": "PineForestProps"
	},
	
	# forest
	{
		"Name":"DenseForestPropsBase",
		"Class":"PropsGenerator",
		"PropList": "DenseForestProps"
	},{
		"Name":"DensePineForestPropsBase",
		"Class":"PropsGenerator",
		"PropList": "DensePineForestProps"
	},
	
	# sea
	{
		"Class": "SimpleLayeringGenerator",
		"Name": "SeaBottomLayeringSand",
		"Blocks": ["SandSurface" + static_surface, "LimestoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 9, 12, 16, 19, 23, 30]
	},{
		"Class": "SimpleLayeringGenerator",
		"Name": "IslesLayeringSand",
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
		"Blocks": ["CopperOre" + static_surface, "LimestoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 9, 12, 16, 19, 23, 30]
	},{
		"Class": "SimpleLayeringGenerator",
		"Name": "SeaBottomLayeringClay",
		"Blocks": ["ClayOre" + static_surface, "LimestoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 9, 12, 16, 19, 23, 30]
	},{
		"Name": "IslesPropsBase",
		"Class": "PropsGenerator",
		"PropList": "IslandProps"
	},{
		"Name": "SeaGrassPropsBase",
		"Class": "PropsGenerator",
		"PropList": "SeagrassProps"
	},{
		"Name": "EmptySeaPropsBase",
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
		"Name":"SmallRocksPropsBase",
		"Class":"PropsGenerator",
		"PropList": "SmallRocksProps"
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
		"Class": "SimpleLayeringGenerator",
		"Name": "MensaeMountainDesertLayeringSand",
		"Blocks": ["DesertSandSurface" + static_surface, "SandstoneSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30]
	},
	{
		"Name": "SandlandPropsBase",
		"Class": "PropsGenerator",
		"PropList": "DesertProps"
	},
	{
		"Class": "MensaeMountainDesertLayering",
		"Name": "MensaeMountainDesertLayeringBase"
	},
	
	# snow 
	{
		"Name": "SnowPropsBase",
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
		"Name":"DensePineForestBiome",
		"Layering":"JustGrassLayeringPine",
		"Props":"DensePineForestPropsBase",
		"Color":[184/255.0, 255/255.0, 133/255.0]
	},{
		"Class":"Biome",
		"Name":"DenseForestBiome",
		"Layering":"GrassLayering",
		"Props":"DenseForestPropsBase",
		"Color":[184/255.0, 255/255.0, 133/255.0]
	},
	
	# snow
	{
		"Class":"Biome",
		"Name":"SnowBiome",
		"Layering":"SnowLayering",
		"Props": "SnowPropsBase"
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
		"Props":"SmallRocksPropsBase"
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
		"Props":"IslesPropsBase"
	},{
		"Class":"Biome",
		"Name":"SeaGrassBiome",
		"Layering":"SeaBottomLayeringSand",
		"Props":"SeaGrassPropsBase"
	},{
		"Class":"Biome",
		"Name":"EmptySeaBiome",
		"Layering":"SeaBottomLayeringSand",
		"Props":"EmptySeaPropsBase"
	},{
		"Class":"Biome",
		"Name":"GravelSeaBiome",
		"Layering":"SeaBottomLayeringGravel"
	},{
		"Class":"Biome",
		"Name":"CopperSeaBiome",
		"Layering":"SeaBottomLayeringCopper"
	},{
		"Class":"Biome",
		"Name":"ClaySeaBiome",
		"Layering":"SeaBottomLayeringClay"
	},{
		"Class":"Biome",
		"Name":"IslesBiome",
		"Layering":"IslesLayeringSand",
		"Props":"IslesPropsBase"
	},{
		"Class":"Biome",
		"Name":"SeaGrassBiome",
		"Layering":"IslesLayeringSand",
		"Props":"SeaGrassPropsBase"
	}
	
	# grass
	,{
		"Class":"Biome",
		"Name":"HillsBiome",
		"Layering":"GrassLayering",
		"Props":"GrasslandPropsBase"
	},{
		"Class":"Biome",
		"Name":"MountainsBiome",
		"Layering":"GrassLayering"
	},{
		"Class":"Biome",
		"Name":"BogBiome",
		"Layering":"BogGrassLayeringGrass",
		"Props":"BogPropsBase",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"PeatBiome",
		"Layering":"PeatLayering",
		"Props":"OrePropsBase"
	},{
		"Class":"Biome",
		"Name":"ClayBiome",
		"Layering":"ClayLayering",
		"Props":"OrePropsBase"
	},{
		"Class":"Biome",
		"Name":"BogForestBiome",
		"Layering":"BogGrassLayeringGrass",
		"Props":"BogForestPropsBase",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"PineForestBiome",
		"Layering":"JustGrassLayeringPine",
		"Props":"PineForestPropsBase"
	},{
		"Class":"Biome",
		"Name":"ForestBiome",
		"Layering":"GrassLayering",
		"Props":"ForestPropsBase",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"BushlandBiome",
		"Layering":"GrassLayering",
		"Props":"BushlandPropsBase",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},
	
	# plains
	{
		"Class":"Biome",
		"Name":"PlainsBiome",
		"Layering":"GrassLayering",
		"Props":"GrasslandPropsBase"
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
		"Props":"SandlandPropsBase"
	},{
		"Class":"Biome",
		"Name":"MensaeBiome",
		"Layering":"MensaeMountainDesertLayeringSand"
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

write_file("Generated/Generators/vanilla.json", data);

data = {
	"Objects": biomes
}

write_file("Generated/Biomes/vanilla.json", data);

data = {
	"Objects": families
}

write_file("Generated/BiomeFamilies/vanilla.json", data);

data = {
	"Objects": global_family
}

write_file("Generated/GlobalBiomFamily/vanilla.json", data);