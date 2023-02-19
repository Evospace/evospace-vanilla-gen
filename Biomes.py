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
        "childs": [
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
        "childs": [
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
        "childs": [
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
            "childs": [
                "PrairieDryPlainsBiome",
                "PrairieDryHillsBiome",
                "PrairiePlainsBiome",
            ],
            "child_frequency": biome_family_size,
        },
        {
            "name": "SandBiomeFamily",
            "class": "BiomeFamily",
            "childs": [
                "DesertBiome",
                "MensaeBiome",
            ],
            "child_frequency": biome_family_size,
        },
        {
            "name": "ForestBiomeFamily",
            "class": "BiomeFamily",
            "childs": [
                "DenseForestBiome",
                "PlainsBiome",
                "BushlandBiome",
            ],
            "child_frequency": biome_family_size,
        },
        {
            "name": "PineForestBiomeFamily",
            "class": "BiomeFamily",
            "childs": [
                "PineForestBiome",
                "DensePineForestBiome",
            ],
            "child_frequency": biome_family_size,
        },
        {
            "name": "SeaBiomeFamily",
            "class": "BiomeFamily",
            "childs": [
                "SeaBiome",
                "IslesBiome",
                "SeaGrassBiome",
                "EmptySeaBiome",
            ],
            "child_frequency": biome_family_size,
        },
        {
            "name": "VolcanicBiomeFamily",
            "class": "BiomeFamily",
            "childs": ["VolcanoBiome", "BrokenLandBiome"],
            "child_frequency": biome_family_size,
        },
        {
            "name": "SwampBiomeFamily",
            "class": "BiomeFamily",
            "childs": [
                "PeatBiome",
                "BogBiome",
                "BogForestBiome",
                "ClayBiome",
            ],
            "child_frequency": biome_family_size,
        },
        {
            "name": "PlainBiomeFamily",
            "class": "BiomeFamily",
            "childs": [
                "PlainsBiome",
                "RedPlainsBiome",
                "WhitePlainsBiome",
                "YellowPlainsBiome",
            ],
            "child_frequency": biome_family_size,
        },
        {
            "name": "SnowBiomeFamily",
            "class": "BiomeFamily",
            "childs": ["SnowBiome", "SnowGrassBiome", "SnowForestBiome"],
            "child_frequency": biome_family_size,
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
            "blocks": [
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
            "starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "GrassLayering",
            "blocks": [
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
            "starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        # prairie
        {
            "name": "PrairieDryProps",
            "class": "PropsGenerator",
            "prop_list": "PrairieDryPropList",
        },
        {
            "name": "PrairieProps",
            "class": "PropsGenerator",
            "prop_list": "PrairiePropList",
        },
        # jungle
        {
            "class": "SimpleLayeringGenerator",
            "name": "DipteroLayering",
            "blocks": [
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
            "starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "name": "DipteroProps",
            "class": "PropsGenerator",
            "prop_list": "DipteroPropList",
        },
        # snow
        {
            "class": "SimpleLayeringGenerator",
            "name": "SnowLayering",
            "blocks": [
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
            "starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        # swamp
        {
            "class": "SimpleLayeringGenerator",
            "name": "BogGrassLayeringGrass",
            "blocks": [
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
            "starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "PeatLayering",
            "blocks": [
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
            "starts": [0, 2, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "ClayLayering",
            "blocks": [
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
            "starts": [0, 2, 6, 9, 12, 16, 19, 23, 30],
        },
        {"name": "BogPropsBase", "class": "PropsGenerator", "prop_list": "SwampProps"},
        {
            "name": "BogForestPropsBase",
            "class": "PropsGenerator",
            "prop_list": "SwampForestProps",
        },
        {"name": "OrePropsBase", "class": "PropsGenerator", "prop_list": "OreProps"},
        {"name": "BogHeightMapBase", "class": "BogHeightMap"},
        {"name": "BogForestHeightMapBase", "class": "BogForestHeightMap"},
        # grass
        {
            "class": "SimpleLayeringGenerator",
            "name": "JustGrassLayeringPine",
            "blocks": [
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
            "starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "name": "GrasslandPropsBase",
            "class": "PropsGenerator",
            "prop_list": "GrasslandProps",
        },
        {
            "name": "GrasslandPropsRed",
            "class": "PropsGenerator",
            "prop_list": "RedFlowersProps",
        },
        {
            "name": "GrasslandPropsWhite",
            "class": "PropsGenerator",
            "prop_list": "WhiteFlowersProps",
        },
        {
            "name": "GrasslandPropsYellow",
            "class": "PropsGenerator",
            "prop_list": "YellowFlowersProps",
        },
        {
            "name": "BushlandPropsBase",
            "class": "PropsGenerator",
            "prop_list": "BushlandProps",
        },
        {
            "name": "ForestPropsBase",
            "class": "PropsGenerator",
            "prop_list": "ForestProps",
        },
        {
            "name": "PineForestPropsBase",
            "class": "PropsGenerator",
            "prop_list": "PineForestProps",
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
            "prop_list": "DenseForestProps",
        },
        {
            "name": "DensePineForestPropsBase",
            "class": "PropsGenerator",
            "prop_list": "DensePineForestProps",
        },
        # sea
        {
            "class": "SimpleLayeringGenerator",
            "name": "SeaBottomLayeringSand",
            "blocks": [
                "SandSurface",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "starts": [0, 3, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "IslesLayeringSand",
            "blocks": [
                "SandSurface",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "starts": [0, 3, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "SeaBottomLayeringGravel",
            "blocks": [
                "GravelSurface",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "starts": [0, 3, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "SeaBottomLayeringCopper",
            "blocks": [
                "CopperOre",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "starts": [0, 2, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "SeaBottomLayeringClay",
            "blocks": [
                "ClayOre",
                "LimestoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "RedStoneSurface",
                "StoneSurface",
                "DarkStoneSurface",
            ],
            "starts": [0, 2, 9, 12, 16, 19, 23, 30],
        },
        {
            "name": "IslesPropsBase",
            "class": "PropsGenerator",
            "prop_list": "IslandProps",
        },
        {
            "name": "SeaGrassPropsBase",
            "class": "PropsGenerator",
            "prop_list": "SeagrassProps",
        },
        {
            "name": "EmptySeaPropsBase",
            "class": "PropsGenerator",
            "prop_list": "EmptySeaProps",
        },
        {"class": "SeaBottomHeightMap", "name": "SeaBottomHeightMapBase"},
        {"class": "IslesHeightMap", "name": "IslesHeightMapBase"},
        # volcanic
        {
            "class": "SimpleLayeringGenerator",
            "name": "VolcanicLayeringBasalt",
            "blocks": [
                "BasaltSurface",
                "LavaSurface",
                "RedStoneSurface",
                "StoneSurface",
            ],
            "starts": [
                0,
                4,
                9,
                12,
            ],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "BrokenLandLayeringBasalt",
            "blocks": [
                "BasaltSurface",
                "LavaSurface",
                "RedStoneSurface",
                "StoneSurface",
            ],
            "starts": [
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
            "prop_list": "SmallRocksProps",
        },
        # river
        {
            "class": "SimpleLayeringGenerator",
            "name": "RiverLayeringSand",
            "blocks": [
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
            "starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {"class": "RiverHeightMap", "name": "RiverHeightMapBase"},
        # desert
        {
            "class": "SimpleLayeringGenerator",
            "name": "SandLayeringSand",
            "blocks": [
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
            "starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "SandDesertLayeringSand",
            "blocks": [
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
            "starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "class": "SimpleLayeringGenerator",
            "name": "MensaeMountainDesertLayeringSand",
            "blocks": [
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
            "starts": [0, 3, 6, 9, 12, 16, 19, 23, 30],
        },
        {
            "name": "SandlandPropsBase",
            "class": "PropsGenerator",
            "prop_list": "DesertProps",
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
        {"name": "SnowPropsBase", "class": "PropsGenerator", "prop_list": "SnowProps"},
        {
            "name": "SnowGrassGenerator",
            "class": "PropsGenerator",
            "prop_list": "SnowGrassProps",
        },
        {
            "name": "SnowForestGenerator",
            "class": "PropsGenerator",
            "prop_list": "SnowForestProps",
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
            
            "layering": "DryGrassLayering",
            "props": "PrairieDryProps",
        },
        {
            "class": "Biome",
            "name": "PrairiePlainsBiome",
            
            "layering": "DryGrassLayering",
            "props": "PrairieProps",
        },
        {
            "class": "Biome",
            "name": "PrairieDryHillsBiome",
            
            "layering": "DryGrassLayering",
            "props": "PrairieDryProps",
        },
        # forest
        {
            "class": "Biome",
            "name": "DensePineForestBiome",
            
            "layering": "JustGrassLayeringPine",
            "props": "DensePineForestPropsBase",
            "color": [184 / 255.0, 255 / 255.0, 133 / 255.0],
        },
        {
            "class": "Biome",
            "name": "DenseForestBiome",
            
            "layering": "GrassLayering",
            "props": "DenseForestPropsBase",
            "color": [184 / 255.0, 255 / 255.0, 133 / 255.0],
        },
        # snow
        {
            "class": "Biome",
            "name": "SnowBiome",
            
            "layering": "SnowLayering",
            "props": "SnowPropsBase",
        },
        {
            "class": "Biome",
            "name": "SnowGrassBiome",
            
            "layering": "SnowLayering",
            "props": "SnowGrassGenerator",
        },
        {
            "class": "Biome",
            "name": "SnowForestBiome",
            
            "layering": "SnowLayering",
            "props": "SnowForestGenerator",
        },
        # jungle
        {
            "class": "Biome",
            "name": "DipteroBiome",
            
            "layering": "DipteroLayering",
            "props": "DipteroProps",
            "color": [204 / 255.0, 255 / 255.0, 153 / 255.0],
        },
        {
            "class": "Biome",
            "name": "BrokenLandBiome",
            
            "layering": "BrokenLandLayeringBasalt",
            "props": "SmallRocksPropsBase",
        }
        # volcano
        ,
        {
            "class": "Biome",
            "name": "VolcanoBiome",
            
            "layering": "VolcanicLayeringBasalt",
        }
        # sea
        ,
        {
            "class": "Biome",
            "name": "SeaBiome",
            
            "layering": "SeaBottomLayeringSand",
            "props": "IslesPropsBase",
        },
        {
            "class": "Biome",
            "name": "SeaGrassBiome",
            
            "layering": "SeaBottomLayeringSand",
            "props": "SeaGrassPropsBase",
        },
        {
            "class": "Biome",
            "name": "EmptySeaBiome",
            
            "layering": "SeaBottomLayeringSand",
            "props": "EmptySeaPropsBase",
        },
        {
            "class": "Biome",
            "name": "GravelSeaBiome",
            
            "layering": "SeaBottomLayeringGravel",
        },
        {
            "class": "Biome",
            "name": "CopperSeaBiome",
            
            "layering": "SeaBottomLayeringCopper",
        },
        {
            "class": "Biome",
            "name": "ClaySeaBiome",
            
            "layering": "SeaBottomLayeringClay",
        },
        {
            "class": "Biome",
            "name": "IslesBiome",
            
            "layering": "IslesLayeringSand",
            "props": "IslesPropsBase",
        },
        {
            "class": "Biome",
            "name": "SeaGrassBiome",
            
            "layering": "IslesLayeringSand",
            "props": "SeaGrassPropsBase",
        }
        # grass
        ,
        {
            "class": "Biome",
            "name": "HillsBiome",
            
            "layering": "GrassLayering",
            "props": "GrasslandPropsBase",
        },
        {
            "class": "Biome",
            "name": "MountainsBiome",
            
            "layering": "GrassLayering",
        },
        {
            "class": "Biome",
            "name": "BogBiome",
            
            "layering": "BogGrassLayeringGrass",
            "props": "BogPropsBase",
            "color": [204 / 255.0, 255 / 255.0, 153 / 255.0],
        },
        {
            "class": "Biome",
            "name": "PeatBiome",
            
            "layering": "PeatLayering",
            "props": "OrePropsBase",
        },
        {
            "class": "Biome",
            "name": "ClayBiome",
            
            "layering": "ClayLayering",
            "props": "OrePropsBase",
        },
        {
            "class": "Biome",
            "name": "BogForestBiome",
            
            "layering": "BogGrassLayeringGrass",
            "props": "BogForestPropsBase",
            "color": [204 / 255.0, 255 / 255.0, 153 / 255.0],
        },
        {
            "class": "Biome",
            "name": "PineForestBiome",
            
            "layering": "JustGrassLayeringPine",
            "props": "PineForestPropsBase",
        },
        {
            "class": "Biome",
            "name": "ForestBiome",
            
            "layering": "GrassLayering",
            "props": "ForestPropsBase",
            "color": [204 / 255.0, 255 / 255.0, 153 / 255.0],
        },
        {
            "class": "Biome",
            "name": "BushlandBiome",
            
            "layering": "GrassLayering",
            "props": "BushlandPropsBase",
            "color": [204 / 255.0, 255 / 255.0, 153 / 255.0],
        },
        # plains
        {
            "class": "Biome",
            "name": "PlainsBiome",
            
            "layering": "GrassLayering",
            "props": "GrasslandPropsBase",
        },
        {
            "class": "Biome",
            "name": "RedPlainsBiome",
            
            "layering": "GrassLayering",
            "props": "GrasslandPropsRed",
        },
        {
            "class": "Biome",
            "name": "WhitePlainsBiome",
            
            "layering": "GrassLayering",
            "props": "GrasslandPropsWhite",
        },
        {
            "class": "Biome",
            "name": "YellowPlainsBiome",
            
            "layering": "GrassLayering",
            "props": "GrasslandPropsYellow",
        },
        # desert
        {
            "class": "Biome",
            "name": "DesertBiome",
            
            "layering": "SandDesertLayeringSand",
            "props": "SandlandPropsBase",
        },
        {
            "class": "Biome",
            "name": "MensaeBiome",
            "height": "MensaeMountainDesertHeightMapBase",
            "layering": "MensaeMountainDesertLayeringSand",
        },
        # river
        {
            "class": "Biome",
            "name": "RiverBiome",
            
            "layering": "RiverLayeringSand",
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
