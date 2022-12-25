from Common import *

global_family = []
families = []
families = []
biomes = []
generators = []
complexbiomes = []


mega_boime_size = 0.007
biome_family_size = 0.016

global_family.append(
    {
        "name": "GlobalBiomeMegaFamily",
        "class": "GlobalBiomeFamily",
        "Childs": [
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
        ],
    }
)
global_family.append(
    {
        "name": "GlobalBiomeMegaFamily2",
        "class": "GlobalBiomeFamily2",
        "Childs": [
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
        ],
    }
)
global_family.append(
    {
        "name": "GlobalBiomeMegaFamily3",
        "class": "GlobalBiomeFamily3",
        "Childs": [
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
        ],
    }
)

# Tundra = 0, // (84, 234, 247)
# Taiga = 1, // (5, 102, 33)
# Steppe = 2, // (249, 218, 7)
# Rainforest = 3, // (7, 249, 162)
# Grassland = 4, // (155, 224, 35)
# Desert = 5, // (250, 147, 23)
# Forest = 6, // (46, 177, 83)
# TropicalForest = 7, // (8, 250, 54)
# Sea = 8, // (35, 48, 224)
# Volcano = 9, // (255, 0, 0)

# biome families
families.extend(
    [
        {
            "name": "PrairieBiomeFamily",
            "class": "BiomeFamily",
            "Childs": [
                "PrairieDryPlainsBiome",
                "PrairieDryHillsBiome",
                "PrairiePlainsBiome",
            ],
            "ChildFrequency": biome_family_size,
        },
        {
            "name": "SandBiomeFamily",
            "class": "BiomeFamily",
            "Childs": [
                "DesertBiome",
                "MensaeBiome",
            ],
            "ChildFrequency": biome_family_size,
        },
        {
            "name": "ForestBiomeFamily",
            "class": "BiomeFamily",
            "Childs": [
                "DenseForestBiome",
                "PlainsBiome",
                "BushlandBiome",
            ],
            "ChildFrequency": biome_family_size,
        },
        {
            "name": "PineForestBiomeFamily",
            "class": "BiomeFamily",
            "Childs": [
                "PineForestBiome",
                "DensePineForestBiome",
            ],
            "ChildFrequency": biome_family_size,
        },
        {
            "name": "SeaBiomeFamily",
            "class": "BiomeFamily",
            "Childs": [
                "SeaBiome",
                "IslesBiome",
                "SeaGrassBiome",
                "EmptySeaBiome",
            ],
            "ChildFrequency": biome_family_size,
        },
        {
            "name": "VolcanicBiomeFamily",
            "class": "BiomeFamily",
            "Childs": ["VolcanoBiome", "BrokenLandBiome"],
            "ChildFrequency": biome_family_size,
        },
        {
            "name": "SwampBiomeFamily",
            "class": "BiomeFamily",
            "Childs": [
                "PeatBiome",
                "BogBiome",
                "BogForestBiome",
                "ClayBiome",
            ],
            "ChildFrequency": biome_family_size,
        },
        {
            "name": "PlainBiomeFamily",
            "class": "BiomeFamily",
            "Childs": [
                "PlainsBiome",
                "RedPlainsBiome",
                "WhitePlainsBiome",
                "YellowPlainsBiome",
            ],
            "ChildFrequency": biome_family_size,
        },
        {
            "name": "SnowBiomeFamily",
            "class": "BiomeFamily",
            "Childs": ["SnowBiome", "SnowGrassBiome", "SnowForestBiome"],
            "ChildFrequency": biome_family_size,
        },
    ]
)

# generators
generators.extend(
    [
        # general
        {
            "class": "SimpleLayeringGenerator",
            "name": "DryGrassLayering",
            "Blocks": [
                "DryGrassSurface",
                "DirtSurface",
                "StoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "GrassLayering",
            "Blocks": [
                "GrassSurface",
                "DirtSurface",
                "StoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        # prairie
        {
            "name": "PrairieDryProps",
            "class": "PropsGenerator",
            "PropList": "PrairieDryPropList",
        },
        {
            "name": "PrairieProps",
            "class": "PropsGenerator",
            "PropList": "PrairiePropList",
        },
        # jungle
        {
            "class": "SimpleLayeringGenerator",
            "name": "DipteroLayering",
            "Blocks": [
                "GrassSurface",
                "DirtSurface",
                "StoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "name": "DipteroProps",
            "class": "PropsGenerator",
            "PropList": "DipteroPropList",
        },
        # snow
        {
            "class": "SimpleLayeringGenerator",
            "name": "SnowLayering",
            "Blocks": [
                "SnowSurface",
                "DirtSurface",
                "StoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        # swamp
        {
            "class": "SimpleLayeringGenerator",
            "name": "BogGrassLayeringGrass",
            "Blocks": [
                "BogSurface",
                "DirtSurface",
                "StoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
            ],
            "Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "PeatLayering",
            "Blocks": [
                "PeatSurface",
                "StoneSurface",
                "StoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 2, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "ClayLayering",
            "Blocks": [
                "ClayOre",
                "ClayOre",
                "DarkStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 2, 6, 9, 12, 16, 19, 23, 30],
        },
        {"name": "BogPropsBase", "class": "PropsGenerator", "PropList": "SwampProps"},
        {
            "name": "BogForestPropsBase",
            "class": "PropsGenerator",
            "PropList": "SwampForestProps",
        },
        {"name": "OrePropsBase", "class": "PropsGenerator", "PropList": "OreProps"},
        {"name": "BogHeightMapBase", "class": "BogHeightMap"},
        {"name": "BogForestHeightMapBase", "class": "BogForestHeightMap"},
        # grass
        {
            "class": "SimpleLayeringGenerator",
            "name": "JustGrassLayeringPine",
            "Blocks": [
                "PineForestSurface",
                "DirtSurface",
                "StoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "name": "GrasslandPropsBase",
            "class": "PropsGenerator",
            "PropList": "GrasslandProps",
        },
        {
            "name": "GrasslandPropsRed",
            "class": "PropsGenerator",
            "PropList": "RedFlowersProps",
        },
        {
            "name": "GrasslandPropsWhite",
            "class": "PropsGenerator",
            "PropList": "WhiteFlowersProps",
        },
        {
            "name": "GrasslandPropsYellow",
            "class": "PropsGenerator",
            "PropList": "YellowFlowersProps",
        },
        {
            "name": "BushlandPropsBase",
            "class": "PropsGenerator",
            "PropList": "BushlandProps",
        },
        {
            "name": "ForestPropsBase",
            "class": "PropsGenerator",
            "PropList": "ForestProps",
        },
        {
            "name": "PineForestPropsBase",
            "class": "PropsGenerator",
            "PropList": "PineForestProps",
        },
        {"name": "FieldsHeightMapBase", "class": "FieldsHeightMap"},
        {"name": "HillsHeightMapBase", "class": "HillsHeightMap"},
        {"name": "HillsSIMDHeightMapBase", "class": "HillsSIMDHeightMap"},
        {"name": "MountainsHeightMapBase", "class": "MountainsHeightMap"},
        {"name": "MountainDensityBase", "class": "MountainDensity"},
        # forest
        {
            "name": "DenseForestPropsBase",
            "class": "PropsGenerator",
            "PropList": "DenseForestProps",
        },
        {
            "name": "DensePineForestPropsBase",
            "class": "PropsGenerator",
            "PropList": "DensePineForestProps",
        },
        # sea
        {
            "class": "SimpleLayeringGenerator",
            "name": "SeaBottomLayeringSand",
            "Blocks": [
                "SandSurface",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "IslesLayeringSand",
            "Blocks": [
                "SandSurface",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "SeaBottomLayeringGravel",
            "Blocks": [
                "GravelSurface",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "SeaBottomLayeringCopper",
            "Blocks": [
                "CopperOre",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 2, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "SeaBottomLayeringClay",
            "Blocks": [
                "ClayOre",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 2, 9, 12, 16, 19, 23, 30],
        },
        {
            "name": "IslesPropsBase",
            "class": "PropsGenerator",
            "PropList": "IslandProps",
        },
        {
            "name": "SeaGrassPropsBase",
            "class": "PropsGenerator",
            "PropList": "SeagrassProps",
        },
        {
            "name": "EmptySeaPropsBase",
            "class": "PropsGenerator",
            "PropList": "EmptySeaProps",
        },
        {"class": "SeaBottomHeightMap", "name": "SeaBottomHeightMapBase"},
        {"class": "IslesHeightMap", "name": "IslesHeightMapBase"},
        # volcanic
        {
            "class": "SimpleLayeringGenerator",
            "name": "VolcanicLayeringBasalt",
            "Blocks": [
                "BasaltSurface",
                "LavaSurface",
                "RedStoneSurface",
                "StoneSurface",
            ],
            "Starts": [
                0,
                4,
                9,
                12,
            ],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "BrokenLandLayeringBasalt",
            "Blocks": [
                "BasaltSurface",
                "LavaSurface",
                "RedStoneSurface",
                "StoneSurface",
            ],
            "Starts": [
                0,
                4,
                9,
                12,
            ],
        },
        {"class": "VolcanoHeightMap", "name": "VolcanoHeightMapBase"},
        {"class": "BrokenLandHeightMap", "name": "BrokenLandHeightMapBase"},
        {
            "name": "SmallRocksPropsBase",
            "class": "PropsGenerator",
            "PropList": "SmallRocksProps",
        },
        # river
        {
            "class": "SimpleLayeringGenerator",
            "name": "RiverLayeringSand",
            "Blocks": [
                "SandSurface",
                "SandstoneSurface",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {"class": "RiverHeightMap", "name": "RiverHeightMapBase"},
        # desert
        {
            "class": "SimpleLayeringGenerator",
            "name": "SandLayeringSand",
            "Blocks": [
                "DesertSandSurface",
                "SandstoneSurface",
                "StoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "SandDesertLayeringSand",
            "Blocks": [
                "DesertSandSurface",
                "SandstoneSurface",
                "StoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "MensaeMountainDesertLayeringSand",
            "Blocks": [
                "DesertSandSurface",
                "SandstoneSurface",
                "StoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "Starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "name": "SandlandPropsBase",
            "class": "PropsGenerator",
            "PropList": "DesertProps",
        },
        {"class": "SandDesertHeightMap", "name": "SandDesertHeightMapBase"},
        {
            "class": "MensaeMountainDesertLayering",
            "name": "MensaeMountainDesertLayeringBase",
        },
        {
            "class": "MensaeMountainDesertHeightMap",
            "name": "MensaeMountainDesertHeightMapBase",
        },
        {"class": "MensaeUMountainDensity", "name": "MensaeUMountainDensityBase"},
        # snow
        {"name": "SnowPropsBase", "class": "PropsGenerator", "PropList": "SnowProps"},
        {
            "name": "SnowGrassGenerator",
            "class": "PropsGenerator",
            "PropList": "SnowGrassProps",
        },
        {
            "name": "SnowForestGenerator",
            "class": "PropsGenerator",
            "PropList": "SnowForestProps",
        },
    ]
)

# biomes
biomes.extend(
    [
        # prairie
        {
            "class": "Biome",
            "name": "PrairieDryPlainsBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "DryGrassLayering",
            "Props": "PrairieDryProps",
        },
        {
            "class": "Biome",
            "name": "PrairiePlainsBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "DryGrassLayering",
            "Props": "PrairieProps",
        },
        {
            "class": "Biome",
            "name": "PrairieDryHillsBiome",
            "Height": "HillsSIMDHeightMapBase",
            "Layering": "DryGrassLayering",
            "Props": "PrairieDryProps",
        },
        # forest
        {
            "class": "Biome",
            "name": "DensePineForestBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "JustGrassLayeringPine",
            "Props": "DensePineForestPropsBase",
            "Color": [184 / 255.0, 255 / 255.0, 133 / 255.0],
        },
        {
            "class": "Biome",
            "name": "DenseForestBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "GrassLayering",
            "Props": "DenseForestPropsBase",
            "Color": [184 / 255.0, 255 / 255.0, 133 / 255.0],
        },
        # snow
        {
            "class": "Biome",
            "name": "SnowBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "SnowLayering",
            "Props": "SnowPropsBase",
        },
        {
            "class": "Biome",
            "name": "SnowGrassBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "SnowLayering",
            "Props": "SnowGrassGenerator",
        },
        {
            "class": "Biome",
            "name": "SnowForestBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "SnowLayering",
            "Props": "SnowForestGenerator",
        },
        # jungle
        {
            "class": "Biome",
            "name": "DipteroBiome",
            "Height": "HillsSIMDHeightMapBase",
            "Layering": "DipteroLayering",
            "Props": "DipteroProps",
            "Color": [204 / 255.0, 255 / 255.0, 153 / 255.0],
        },
        {
            "class": "Biome",
            "name": "BrokenLandBiome",
            "Height": "BrokenLandHeightMapBase",
            "Layering": "BrokenLandLayeringBasalt",
            "Props": "SmallRocksPropsBase",
        }
        # volcano
        ,
        {
            "class": "Biome",
            "name": "VolcanoBiome",
            "Height": "VolcanoHeightMapBase",
            "Layering": "VolcanicLayeringBasalt",
        }
        # sea
        ,
        {
            "class": "Biome",
            "name": "SeaBiome",
            "Height": "SeaBottomHeightMapBase",
            "Layering": "SeaBottomLayeringSand",
            "Props": "IslesPropsBase",
        },
        {
            "class": "Biome",
            "name": "SeaGrassBiome",
            "Height": "SeaBottomHeightMapBase",
            "Layering": "SeaBottomLayeringSand",
            "Props": "SeaGrassPropsBase",
        },
        {
            "class": "Biome",
            "name": "EmptySeaBiome",
            "Height": "SeaBottomHeightMapBase",
            "Layering": "SeaBottomLayeringSand",
            "Props": "EmptySeaPropsBase",
        },
        {
            "class": "Biome",
            "name": "GravelSeaBiome",
            "Height": "IslesHeightMapBase",
            "Layering": "SeaBottomLayeringGravel",
        },
        {
            "class": "Biome",
            "name": "CopperSeaBiome",
            "Height": "IslesHeightMapBase",
            "Layering": "SeaBottomLayeringCopper",
        },
        {
            "class": "Biome",
            "name": "ClaySeaBiome",
            "Height": "IslesHeightMapBase",
            "Layering": "SeaBottomLayeringClay",
        },
        {
            "class": "Biome",
            "name": "IslesBiome",
            "Height": "IslesHeightMapBase",
            "Layering": "IslesLayeringSand",
            "Props": "IslesPropsBase",
        },
        {
            "class": "Biome",
            "name": "SeaGrassBiome",
            "Height": "IslesHeightMapBase",
            "Layering": "IslesLayeringSand",
            "Props": "SeaGrassPropsBase",
        }
        # grass
        ,
        {
            "class": "Biome",
            "name": "HillsBiome",
            "Height": "HillsSIMDHeightMapBase",
            "Layering": "GrassLayering",
            "Props": "GrasslandPropsBase",
        },
        {
            "class": "Biome",
            "name": "MountainsBiome",
            "Height": "MountainsHeightMapBase",
            "Layering": "GrassLayering",
        },
        {
            "class": "Biome",
            "name": "BogBiome",
            "Height": "BogForestHeightMapBase",
            "Layering": "BogGrassLayeringGrass",
            "Props": "BogPropsBase",
            "Color": [204 / 255.0, 255 / 255.0, 153 / 255.0],
        },
        {
            "class": "Biome",
            "name": "PeatBiome",
            "Height": "BogHeightMapBase",
            "Layering": "PeatLayering",
            "Props": "OrePropsBase",
        },
        {
            "class": "Biome",
            "name": "ClayBiome",
            "Height": "BogHeightMapBase",
            "Layering": "ClayLayering",
            "Props": "OrePropsBase",
        },
        {
            "class": "Biome",
            "name": "BogForestBiome",
            "Height": "BogForestHeightMapBase",
            "Layering": "BogGrassLayeringGrass",
            "Props": "BogForestPropsBase",
            "Color": [204 / 255.0, 255 / 255.0, 153 / 255.0],
        },
        {
            "class": "Biome",
            "name": "PineForestBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "JustGrassLayeringPine",
            "Props": "PineForestPropsBase",
        },
        {
            "class": "Biome",
            "name": "ForestBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "GrassLayering",
            "Props": "ForestPropsBase",
            "Color": [204 / 255.0, 255 / 255.0, 153 / 255.0],
        },
        {
            "class": "Biome",
            "name": "BushlandBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "GrassLayering",
            "Props": "BushlandPropsBase",
            "Color": [204 / 255.0, 255 / 255.0, 153 / 255.0],
        },
        # plains
        {
            "class": "Biome",
            "name": "PlainsBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "GrassLayering",
            "Props": "GrasslandPropsBase",
        },
        {
            "class": "Biome",
            "name": "RedPlainsBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "GrassLayering",
            "Props": "GrasslandPropsRed",
        },
        {
            "class": "Biome",
            "name": "WhitePlainsBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "GrassLayering",
            "Props": "GrasslandPropsWhite",
        },
        {
            "class": "Biome",
            "name": "YellowPlainsBiome",
            "Height": "FieldsHeightMapBase",
            "Layering": "GrassLayering",
            "Props": "GrasslandPropsYellow",
        },
        # desert
        {
            "class": "Biome",
            "name": "DesertBiome",
            "Height": "SandDesertHeightMapBase",
            "Layering": "SandDesertLayeringSand",
            "Props": "SandlandPropsBase",
        },
        {
            "class": "Biome",
            "name": "MensaeBiome",
            "Height": "MensaeMountainDesertHeightMapBase",
            "Layering": "MensaeMountainDesertLayeringSand",
        },
        # river
        {
            "class": "Biome",
            "name": "RiverBiome",
            "Height": "RiverHeightMapBase",
            "Layering": "RiverLayeringSand",
        },
    ]
)

data = {"Objects": generators}

write_file("Generated/Generators/vanilla.json", data)

data = {"Objects": biomes}

write_file("Generated/Biomes/vanilla.json", data)

data = {"Objects": families}

write_file("Generated/BiomeFamilies/vanilla.json", data)

data = {"Objects": global_family}

write_file("Generated/GlobalBiomFamily/vanilla.json", data)
