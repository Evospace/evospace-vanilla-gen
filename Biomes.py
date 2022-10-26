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
		"Blocks": ["PeatSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "RedStoneSurface" + static_surface, "StoneSurface" + static_surface, "DarkStoneSurface" + static_surface],
		"Starts": [0, 2, 6, 9, 12, 16, 19, 23, 30]
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
		"PropList": "OreProps"
	},{
		"Name":"BogHeightMapBase",
		"Class":"BogHeightMap"
	},{
		"Name":"BogForestHeightMapBase",
		"Class":"BogForestHeightMap"
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
	},{
		"Name":"FieldsHeightMapBase",
		"Class":"FieldsHeightMap"
	},{
		"Name":"HillsHeightMapBase",
		"Class":"HillsHeightMap"
	},{
		"Name":"HillsSIMDHeightMapBase",
		"Class":"HillsSIMDHeightMap"
	},{
		"Name":"MountainsHeightMapBase",
		"Class":"MountainsHeightMap"
	},{
		"Name":"MountainDensityBase",
		"Class":"MountainDensity"
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
	},{
		"Class": "SeaBottomHeightMap",
		"Name": "SeaBottomHeightMapBase"
	},{
		"Class": "IslesHeightMap",
		"Name": "IslesHeightMapBase"
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
		"Class": "VolcanoHeightMap",
		"Name": "VolcanoHeightMapBase"
	},
	{
		"Class": "BrokenLandHeightMap",
		"Name": "BrokenLandHeightMapBase"
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
	{
		"Class":"RiverHeightMap",
		"Name":"RiverHeightMapBase"
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
		"Class": "SandDesertHeightMap",
		"Name": "SandDesertHeightMapBase"
	},
	{
		"Class": "MensaeMountainDesertLayering",
		"Name": "MensaeMountainDesertLayeringBase"
	},
	{
		"Class": "MensaeMountainDesertHeightMap",
		"Name": "MensaeMountainDesertHeightMapBase"
	},
	{
		"Class": "MensaeUMountainDensity",
		"Name": "MensaeUMountainDensityBase"
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
		
		"Height":"FieldsHeightMapBase",
		"Layering":"DryGrassLayering",
		"Props":"PrairieDryProps"
	},
	{
		"Class":"Biome",
		"Name":"PrairiePlainsBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"DryGrassLayering",
		"Props":"PrairieProps"
	},
	{
		"Class":"Biome",
		"Name":"PrairieDryHillsBiome",
		
		"Height":"HillsSIMDHeightMapBase",
		"Layering":"DryGrassLayering",
		"Props":"PrairieDryProps"
	},
	
	# forest
	{
		"Class":"Biome",
		"Name":"DensePineForestBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"JustGrassLayeringPine",
		"Props":"DensePineForestPropsBase",
		"Color":[184/255.0, 255/255.0, 133/255.0]
	},{
		"Class":"Biome",
		"Name":"DenseForestBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"GrassLayering",
		"Props":"DenseForestPropsBase",
		"Color":[184/255.0, 255/255.0, 133/255.0]
	},
	
	# snow
	{
		"Class":"Biome",
		"Name":"SnowBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"SnowLayering",
		"Props": "SnowPropsBase"
	},
	{
		"Class":"Biome",
		"Name":"SnowGrassBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"SnowLayering",
		"Props": "SnowGrassGenerator"
	},
	{
		"Class":"Biome",
		"Name":"SnowForestBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"SnowLayering",
		"Props": "SnowForestGenerator"
	},
	
	# jungle
	{
		"Class":"Biome",
		"Name":"DipteroBiome",
		
		"Height":"HillsSIMDHeightMapBase",
		"Layering":"DipteroLayering",
		"Props":"DipteroProps",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"BrokenLandBiome",
		
		"Height":"BrokenLandHeightMapBase",
		"Layering":"BrokenLandLayeringBasalt",
		"Props":"SmallRocksPropsBase"
	}
	
	# volcano
	,{
		"Class":"Biome",
		"Name":"VolcanoBiome",
		
		"Height":"VolcanoHeightMapBase",
		"Layering":"VolcanicLayeringBasalt"
	}
	
	# sea
	,{
		"Class":"Biome",
		"Name":"SeaBiome",
		
		"Height":"SeaBottomHeightMapBase",
		"Layering":"SeaBottomLayeringSand",
		"Props":"IslesPropsBase"
	},{
		"Class":"Biome",
		"Name":"SeaGrassBiome",
		
		"Height":"SeaBottomHeightMapBase",
		"Layering":"SeaBottomLayeringSand",
		"Props":"SeaGrassPropsBase"
	},{
		"Class":"Biome",
		"Name":"EmptySeaBiome",
		
		"Height":"SeaBottomHeightMapBase",
		"Layering":"SeaBottomLayeringSand",
		"Props":"EmptySeaPropsBase"
	},{
		"Class":"Biome",
		"Name":"GravelSeaBiome",
		
		"Height":"IslesHeightMapBase",
		"Layering":"SeaBottomLayeringGravel"
	},{
		"Class":"Biome",
		"Name":"CopperSeaBiome",
		
		"Height":"IslesHeightMapBase",
		"Layering":"SeaBottomLayeringCopper"
	},{
		"Class":"Biome",
		"Name":"ClaySeaBiome",
		
		"Height":"IslesHeightMapBase",
		"Layering":"SeaBottomLayeringClay"
	},{
		"Class":"Biome",
		"Name":"IslesBiome",
		
		"Height":"IslesHeightMapBase",
		"Layering":"IslesLayeringSand",
		"Props":"IslesPropsBase"
	},{
		"Class":"Biome",
		"Name":"SeaGrassBiome",
		
		"Height":"IslesHeightMapBase",
		"Layering":"IslesLayeringSand",
		"Props":"SeaGrassPropsBase"
	}
	
	# grass
	,{
		"Class":"Biome",
		"Name":"HillsBiome",
		
		"Height":"HillsSIMDHeightMapBase",
		"Layering":"GrassLayering",
		"Props":"GrasslandPropsBase"
	},{
		"Class":"Biome",
		"Name":"MountainsBiome",
		
		"Height":"MountainsHeightMapBase",
		"Layering":"GrassLayering"
	},{
		"Class":"Biome",
		"Name":"BogBiome",
		
		"Height":"BogForestHeightMapBase",
		"Layering":"BogGrassLayeringGrass",
		"Props":"BogPropsBase",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"PeatBiome",
		
		"Height":"BogHeightMapBase",
		"Layering":"PeatLayering",
		"Props":"OrePropsBase"
	},{
		"Class":"Biome",
		"Name":"ClayBiome",
		
		"Height":"BogHeightMapBase",
		"Layering":"ClayLayering",
		"Props":"OrePropsBase"
	},{
		"Class":"Biome",
		"Name":"BogForestBiome",
		
		"Height":"BogForestHeightMapBase",
		"Layering":"BogGrassLayeringGrass",
		"Props":"BogForestPropsBase",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"PineForestBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"JustGrassLayeringPine",
		"Props":"PineForestPropsBase"
	},{
		"Class":"Biome",
		"Name":"ForestBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"GrassLayering",
		"Props":"ForestPropsBase",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},{
		"Class":"Biome",
		"Name":"BushlandBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"GrassLayering",
		"Props":"BushlandPropsBase",
		"Color":[204/255.0, 255/255.0, 153/255.0]
	},
	
	# plains
	{
		"Class":"Biome",
		"Name":"PlainsBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"GrassLayering",
		"Props":"GrasslandPropsBase"
	},{
		"Class":"Biome",
		"Name":"RedPlainsBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"GrassLayering",
		"Props":"GrasslandPropsRed"
	},{
		"Class":"Biome",
		"Name":"WhitePlainsBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"GrassLayering",
		"Props":"GrasslandPropsWhite"
	},{
		"Class":"Biome",
		"Name":"YellowPlainsBiome",
		
		"Height":"FieldsHeightMapBase",
		"Layering":"GrassLayering",
		"Props":"GrasslandPropsYellow"
	},
	
	# desert
	{
		"Class":"Biome",
		"Name":"DesertBiome",
		
		"Height":"SandDesertHeightMapBase",
		"Layering":"SandDesertLayeringSand",
		"Props":"SandlandPropsBase"
	},{
		"Class":"Biome",
		"Name":"MensaeBiome",
		
		"Height":"MensaeMountainDesertHeightMapBase",
		"Layering":"MensaeMountainDesertLayeringSand"
	},
	
	# river
	{
		"Class":"Biome",
		"Name":"RiverBiome",
		
		"Height":"RiverHeightMapBase",
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