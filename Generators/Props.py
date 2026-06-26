from Common import *
from OresGen import ore_types

variation_helper = [
	"", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"
]

props = [
	{
		"Name": "Cactus",
		"ScaleMin": .5,
		"ScaleMax": 2,
		"Variations": 2,
		"ProjectToTerrainPower": 1,
		"IsBig": False,
		"Drops": "Organics",
		"Count": 30,
		"AdditiveElevation": 0
	},
	{
		"Name":"Dandaleon",
		"ScaleMin": 2,
		"ScaleMax": 4,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"Count": 1,
		"IsBig": False,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0
	},
	{
		"Name": "Fern",
		"ScaleMin": 4,
		"ScaleMax": 6,
		"Variations": 3,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"Count": 2,
		"IsBig": False,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"SurfaceHeightMin": 0
	},
	{
		"Name": "LongGrass",
		"ScaleMin": 3.5,
		"ScaleMax": 4,
		"Variations": 4,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"Count": 1,
		"IsBig": False,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 15,
		"SurfaceHeightMin": 0,
		"HighDetailShadow": True,
		"Image": "T_TerrainGrass",
	},
	{
		"Name": "YellowGrass",
		"ScaleMin": 3.5,
		"ScaleMax": 4,
		"Variations": 2,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"Count": 1,
		"IsBig": False,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 15,
		"SurfaceHeightMin": 0,
		"HighDetailShadow": True,
		"Image": "T_TerrainGrass",
	},
	{
		"Name": "SeaPlant",
		"ScaleMin": 2,
		"ScaleMax": 4,
		"Variations": 22,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"Count": 10,
		"IsBig": False,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"SurfaceHeightMax": 0,
		"TopHeightMax": 0,
		"HighDetailShadow": True
	},
	{
		"Name": "SeaGrass",
		"ScaleMin": 2,
		"ScaleMax": 4,
		"Variations": 5,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"Count": 1,
		"IsBig": False,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"SurfaceHeightMax": 0,
		"TopHeightMax": 0,
		"HighDetailShadow": True,
		"Image": "T_TerrainGrass",
	},
	{
		"Name": "TallGrass",
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"Count": 1,
		"IsBig": False,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"SurfaceHeightMin": 0,
		"HighDetailShadow": True,
		"Image": "T_TerrainGrass",
	},
	{
		"Name": "Broadleaf",
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 3,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"Count": 25,
		"HitsToBreak": 10,
		"DamageEffect": "/Game/EffectActors/TreeDamageEffect.TreeDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/TreeBreakEffect.TreeBreakEffect_C"
	},
	{
		"Name": "Shrub",
		"ScaleMin": 1.5,
		"ScaleMax": 2.5,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"IsBig": True,
		"Drops": "Log",
		"Count": 1,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"TimeMul": 1
	},
	{
		"Name": "Rock",
		"ScaleMin": .6,
		"ScaleMax": 3,
		"Variations": 2,
		"ProjectToTerrainPower": 1,
		"IsBig": True,
		"Drops": "StoneSurface",
		"Count": 20,
		"AdditiveElevation": 0,
		"HitsToBreak": 8,
		"HighDetailShadow": True,
		"DamageEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/RockBreakEffect.RockBreakEffect_C",
		"Image": "T_TerrainRock",
	},
	{
		"Name": "Pine",
		"ScaleMin": .6,
		"ScaleMax": 1.4,
		"Variations": 3,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"Count": 20,
		"HitsToBreak": 8,
		"DamageEffect": "/Game/EffectActors/TreeDamageEffect.TreeDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/TreeBreakEffect.TreeBreakEffect_C"
	},
	{
		"Name": "SnowyPine",
		"ScaleMin": .6,
		"ScaleMax": 1.2,
		"Variations": 3,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"Count": 20,
		"HitsToBreak": 8,
		"DamageEffect": "/Game/EffectActors/TreeDamageEffect.TreeDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/TreeBreakEffect.TreeBreakEffect_C"
	},
	{
		"Name": "Conifer",
		"ScaleMin": .6,
		"ScaleMax": 1.4,
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"Count": 20,
		"HitsToBreak": 8,
		"DamageEffect": "/Game/EffectActors/TreeDamageEffect.TreeDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/TreeBreakEffect.TreeBreakEffect_C"
	},
	{
		"Name": "Palm",
		"ScaleMin": .6,
		"ScaleMax": 1.3,
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"Count": 10,
		"HitsToBreak": 4,
		"DamageEffect": "/Game/EffectActors/TreeDamageEffect.TreeDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/TreeBreakEffect.TreeBreakEffect_C"
	},
	{
		"Name": "Rogoz",
		"ScaleMin": 2,
		"ScaleMax": 3,
		"Variations": 5,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"IsBig": False,
		"Count": 1,
		"CullBegin": 7000,
		"CullEnd": 8000,
		"AdditiveElevation": 24,
		"SurfaceHeightMin": -1,
		"SurfaceHeightMax": 0,
		"HighDetailShadow": True
	},{
		"Name": "Lily", 
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 1,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"Count": 1,
		"CullBegin": 7000,
		"CullEnd": 8000,
		"AdditiveElevation": -40,
		"Floating": True,
		"IsBig": False,
		"HighDetailShadow": True
	},{
		"Name": "LilyFlower",
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"Count": 1,
		"CullBegin": 7000,
		"CullEnd": 8000,
		"AdditiveElevation": -40,
		"Floating": True,
		"IsBig": False,
	},{
		"Name": "Shroom",
		"ScaleMin": 1,
		"ScaleMax": 2,
		"Variations": 4,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"Count": 10,
		"AdditiveElevation": 20,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"IsBig": False,
		"HighDetailShadow": True
	},{
		"Name": "YellowFlower",
		"ScaleMin": 1,
		"ScaleMax": 2,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"Count": 1,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"IsBig": False,
		"HighDetailShadow": True
	},{
		"Name": "RedFlower",
		"ScaleMin": 1,
		"ScaleMax": 2,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"Count": 1,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"IsBig": False,
		"HighDetailShadow": True
	},{
		"Name": "WhiteFlower",
		"ScaleMin": 1,
		"ScaleMax": 2,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"Count": 1,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"IsBig": False,
		"HighDetailShadow": True
	},{
		"Name": "BigBush",
		"ScaleMin": 1.5,
		"ScaleMax": 3,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"IsBig": False,
		"Drops": "Log",
		"Count": 1,
		"AdditiveElevation": 0,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"HitsToBreak": 2,
	},{
		"Name": "SmallRock",
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "StoneSurface",
		"Count": 2,
		"HitsToBreak": 1,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"IsBig": False,
		"DamageEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
		"Image": "T_TerrainRock",
	},{
		"Name": "SmallVolcanicRock",
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "StoneSurface",
		"Count": 2,
		"HitsToBreak": 1,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"IsBig": False,
		"DamageEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
		"Image": "T_TerrainRock",
	},{
		"Name": "DryGrass",
		"ScaleMin": 1,
		"ScaleMax": 2,
		"Variations": 2,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"Count": 1,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"IsBig": False,
		"HighDetailShadow": True,
		"Image": "T_TerrainGrass",
	},{
		"Name": "VolcanicRock",
		"ScaleMin": .5,
		"ScaleMax": 1,
		"Variations": 4,
		"ProjectToTerrainPower": 1,
		"Drops": "BasaltSurface",
		"IsBig": True,
		"AdditiveElevation": 0,
		"Count": 20,
		"HitsToBreak": 15,
		"DamageEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/RockBreakEffect.RockBreakEffect_C",
		"Image": "T_TerrainRock",
	},{
		"Name": "SnowyRock",
		"ScaleMin": .5,
		"ScaleMax": 1,
		"Variations": 4,
		"ProjectToTerrainPower": 1,
		"Drops": "BasaltSurface",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"IsBig": True,
		"AdditiveElevation": 0,
		"Count": 20,
		"HitsToBreak": 8,
		"DamageEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/RockBreakEffect.RockBreakEffect_C",
		"Image": "T_TerrainRock",
	},{
		"Name": "SnowyGrass",
		"ScaleMin": 2,
		"ScaleMax": 4,
		"Variations": 3,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"Count": 1,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"IsBig": False,
		"HighDetailShadow": True,
		"Image": "T_TerrainGrass",
	},{
		"Name": "SteamStream",
		"ScaleMin": 2,
		"ScaleMax": 4,
		"Variations": 1,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"Count": 1,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"IsBig": False,
	},{
		"Name": "FloatingIce", 
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"Count": 1,
		"CullBegin": 7000,
		"CullEnd": 8000,
		"AdditiveElevation": 0,
		"Floating": True,
		"IsBig": False,
		"HighDetailShadow": True
	},{
		"Name": "CanyonRock",
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "StoneSurface",
		"Count": 2,
		"HitsToBreak": 1,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"IsBig": False,
		"DamageEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
		"Image": "T_TerrainRock",
	}
]

for ore in ore_types:
	props.append({
		"Name": ore["Name"] + "Cluster",
		"ScaleMin": 2,
		"ScaleMax": 2,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": ore["Drops"],
		"Count": 1,
		"CullBegin": 90000,
		"CullEnd": 100000,
		"AdditiveElevation": 0,
		"IsBig": True,
		"Image": "T_Error",
		"HitsToBreak": -1,
		"DamageEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
		"BreakEffect": "/Game/EffectActors/RockBreakEffect.RockBreakEffect_C",
		"Image": "T_TerrainCluster",
	})

# Oil deposit spawns like ore, yields RawOil for pumpjacks
props.append({
	"Name": "OilCluster",
	"ScaleMin": 2,
	"ScaleMax": 2,
	"Variations": 1,
	"ProjectToTerrainPower": 1,
	"Drops": "RawOil",
	"Count": 1,
	"Minable": False,
	"CullBegin": 90000,
	"CullEnd": 100000,
	"AdditiveElevation": 0,
	"IsBig": True,
	"Image": "T_Error",
	"HitsToBreak": -1,
	"DamageEffect": "/Game/EffectActors/RockDamageEffect.RockDamageEffect_C",
	"BreakEffect": "/Game/EffectActors/RockBreakEffect.RockBreakEffect_C",
	"Image": "T_TerrainCluster",
})

def named_prop(name):
	return [x for x in props if x["Name"] == name][0]

proplists = [
	{ 
		"Name": "PrairieDryPropList",
		"Array": [
			{
				"Props": ["SmallRock"],
				"Chance": 0.01
			},{
				"Props": ["DryGrass"],
				"Chance": 0.5
			},{
				"Props": ["Broadleaf", "Broadleaf", "Conifer", "BigBush"],
				"Chance": 0.0001
			}
		]
	},{ 
		"Name": "PrairiePropList",
		"Array": [
			{
				"Props": ["SmallRock"],
				"Chance": 0.01
			},{
				"Props": ["DryGrass"],
				"Chance": 0.35
			},{
				"Props": ["YellowGrass"],
				"Chance": 0.35
			},{
				"Props": ["Broadleaf", "Broadleaf", "Conifer", "BigBush"],
				"Chance": 0.0004
			}
		]
	},
	{ 
		"Name": "DipteroPropList",
		"Array": [
			{
				"Props": ["Broadleaf", "Broadleaf", "Conifer", "Shrub", "BigBush"],
				"Chance": 0.01
			},{
				"Props": ["SmallRock"],
				"Chance": 0.01
			},{
				"Props": ["Fern"],
				"Chance": 0.05
			},{
				"Props": ["LongGrass"],
				"Chance": 0.9
			}
		]
	},{ 
		"Name": "VolcanicProps",
		"Array": [
			{
				"Props": ["SmallVolcanicRock"],
				"Chance": 0.02
			},
			{
				"Props": ["VolcanicRock"],
				"Chance": 0.01
			}
		]
	},{
		"Name": "SnowProps",
		"Array": [
			{
				"Props": ["SnowyRock"],
				"Chance": 0.01
			}
		]
	},{ 
		"Name": "BushlandProps",
		"Array": [
			{
				"Props": ["Shrub", "BigBush"],
				"Chance": 0.05
			},{
				"Props": ["LongGrass"],
				"Chance": 0.75
			},{
				"Props": ["TallGrass"],
				"Chance": 0.05
			}
		]
	},{ 	
		"Name": "GrasslandProps",
		"Array": [
			{
				"Props": ["Rock"],
				"Chance": 0.005
			},{
				"Props": ["Dandaleon"],
				"Chance": 0.05
			},{
				"Props": ["LongGrass"],
				"Chance": 0.9
			},{
				"Props": ["TallGrass"],
				"Chance": 0.15
			}
		]
	},{ 
		"Name": "RedFlowersProps",
		"Array": [
			{
				"Props": ["RedFlower"],
				"Chance": 0.5
			},{
				"Props": ["LongGrass"],
				"Chance": 0.9
			}
		]
	},{ 
		"Name": "YellowFlowersProps",
		"Array": [
			{
				"Props": ["YellowFlower"],
				"Chance": 0.5
			},{
				"Props": ["LongGrass"],
				"Chance": 0.9
			}
		]
	},{ 
		"Name": "WhiteFlowersProps",
		"Array": [
			{
				"Props": ["WhiteFlower"],
				"Chance": 0.5
			},{
				"Props": ["LongGrass"],
				"Chance": 0.9
			},{
				"Attaches": ["Butterfly"],
				"Chance": 0.001
			}
		]
	},{ 
		"Name": "ForestProps",
		"Array": [
			{
				"Props": ["Broadleaf", "Broadleaf", "Conifer", "Shrub", "BigBush"],
				"Chance": 0.01
			},{
				"Props": ["SmallRock"],
				"Chance": 0.01
			},{
				"Props": ["Fern"],
				"Chance": 0.05
			},{
				"Props": ["Dandaleon"],
				"Chance": 0.5
			},{
				"Props": ["LongGrass"],
				"Chance": 0.9
			},{
				"Props": ["Shroom"],
				"Chance": 0.01
			}

		]
	},	{ 
		"Name": "FertileForestProps",
		"Array": [
			{
				"Props": ["Broadleaf", "Broadleaf", "Conifer", "Shrub", "BigBush"],
				"Chance": 0.02
			},{
				"Props": ["SmallRock"],
				"Chance": 0.005
			},{
				"Props": ["Fern"],
				"Chance": 0.02
			},{
				"Props": ["Dandaleon"],
				"Chance": 0.45
			},{
				"Props": ["YellowFlower"],
				"Chance": 0.1
			},{
				"Props": ["WhiteFlower"],
				"Chance": 0.1
			},{
				"Props": ["LongGrass"],
				"Chance": 0.8
			},{
				"Props": ["TallGrass"],
				"Chance": 0.1
			},{
				"Props": ["Shroom"],
				"Chance": 0.02
			}
		]
	},{ 
		"Name": "PineForestProps",
		"Array": [
			{
				"Props": ["Rock"],
				"Chance": 0.002
			},{
				"Props": ["SmallRock"],
				"Chance": 0.01
			},{
				"Props": ["Pine"],
				"Chance": 0.01
			},{
				"Props": ["DryGrass"],
				"Chance": 0.1
			},{
				"Props": ["Shroom"],
				"Chance": 0.01
			}
		]
	},{	
		"Name": "UnimplementedProps",
		"Array": [
			{
				"Props": ["Rock"],
				"Chance": 0.01
			}
		]
	},{	
		"Name": "DesertProps",
		"Array": [
			{
				"Props": ["Cactus"],
				"Chance": 0.01
			},{
				"Props": ["Palm"],
				"Chance": 0.002
			}
		]
	},{	
		"Name": "SeaPlantProps",
		"Array": [
			{
				"Props": ["SmallRock"],
				"Chance": 0.01
			},{
				"Props": ["SeaPlant"],
				"Chance": 0.07
			}
		]
	},{	
		"Name": "SeaGrassProps",
		"Array": [
			{
				"Props": ["SmallRock"],
				"Chance": 0.01
			},{
				"Props": ["SeaGrass"],
				"Chance": 0.15
			}
		]
	},{	
		"Name": "EmptySeaProps",
		"Array": [
			{
				"Props": ["SmallRock"],
				"Chance": 0.05
			}
		]
	},{	
		"Name": "SwampProps",
		"Array": [
			{
				"Props": ["SmallRock"],
				"Chance": 0.01
			},{
				"Props": ["LongGrass"],
				"Chance": 0.75
			},{
				"Props": ["Fern"],
				"Chance": 0.05
			},{
				"Props": ["Rogoz"],
				"Chance": 0.5
			},{
				"Props": ["Lily"],
				"Chance": 0.5
			},{
				"Props": ["LilyFlower"],
				"Chance": 0.05
			}
		]
	},{	
		"Name": "SwampForestProps",
		"Array": [
			{
				"Props": ["LongGrass"],
				"Chance": 0.7
			},{
				"Props": ["Fern"],
				"Chance": 0.05
			},{
				"Props": ["Rogoz"],
				"Chance": 0.5
			},{
				"Props": ["Broadleaf", "BigBush"],
				"Chance": 0.01
			},{
				"Props": ["Shroom"],
				"Chance": 0.01
			}
		]
	},{	
		"Name": "ClayBeachProps",
		"Array": [
			{
				"Props": ["YellowGrass"],
				"Chance": 0.07
			},{
				"Props": ["Rogoz"],
				"Chance": 0.5
			},{
				"Props": ["Broadleaf", "BigBush"],
				"Chance": 0.01
			},{
				"Props": ["Shroom"],
				"Chance": 0.01
			}
		]
	},
	{	
		"Name": "SnowGrassProps",
		"Array": [
			{
				"Props": ["SnowyGrass"],
				"Chance": 0.2
			},
			{
				"Props": ["SnowyRock"],
				"Chance": 0.01
			},{
				"Props": ["FloatingIce"],
				"Chance": 0.3
			}
		]
	},
	{	
		"Name": "SnowForestProps",
		"Array": [
			{
				"Props": ["SnowyGrass"],
				"Chance": 0.2
			},{
				"Props": ["SnowyPine"],
				"Chance": 0.005
			},{
				"Props": ["FloatingIce"],
				"Chance": 0.3
			}
		]
	}
]

ore_props = []
for ore in ore_types:
	ore_props.append(ore["Name"]+"Cluster")
ore_props.append("OilCluster")

objects_array = []

# Small, dense, decorative foliage is streamed around the player (UGrassStreamingSubsystem)
# instead of being instanced per-column. Tag by name; everything else stays column-instanced.
streamed_prop_names = {
	"Dandaleon", "Fern", "LongGrass", "YellowGrass", "DryGrass",
	"TallGrass", "SeaGrass", "SeaPlant",
}
for prop in props:
	if prop["Name"] in streamed_prop_names:
		prop["Streamed"] = True

for prop in props:
	image = "T_" + prop["Name"] if "Image" not in prop else prop["Image"]

	for variation in range(0, prop["Variations"]):
		objects_array.append({ "Class": "StaticItem",
			"Name": prop["Name"] + variation_helper[variation],
			"StackSize": 32,
			"Image": image,
			"Category": "Terrain",
			"Label": [prop["Name"], "props"],
			"DescriptionParts":[["WorldObject","common"]],
		})

	for variation in range(0, prop["Variations"]):
		# Non-minable props (e.g. OilCluster) still need Result for map icons and USourceData::Item in OreGenerator
		minable = (
			{"Minable": False, "Result": prop["Drops"], "Count": prop["Count"]}
			if prop.get("Minable") is False
			else {"Result": prop["Drops"], "Count": prop["Count"]}
		)
		temp_prop = { "Class": "StaticProp",
			"Name": prop["Name"] + variation_helper[variation],
			"Mesh": "/Game/Props/" + prop["Name"] + "/" + prop["Name"] + variation_helper[variation],
			"ScaleMin": prop["ScaleMin"],
			"ScaleMax": prop["ScaleMax"],
			"ProjectToTerrainPower": prop["ProjectToTerrainPower"],
			"AdditiveElevation": prop.get("AdditiveElevation", 0),
			"Item": prop["Name"],
			"Minable": minable,
			"IsBig": prop["IsBig"]
		}
		if "DamageEffect" in prop:
			temp_prop["DamageEffect"] = prop["DamageEffect"]
		if "BreakEffect" in prop:
			temp_prop["BreakEffect"] = prop["BreakEffect"]
		if "HitsToBreak" in prop:
			temp_prop["HitsToBreak"] = prop["HitsToBreak"]
		if "CullBegin" in prop:
			temp_prop["CullBegin"] = prop["CullBegin"]
		if "Floating" in prop:
			temp_prop["Floating"] = prop["Floating"]
		if "CullEnd" in prop:
			temp_prop["CullEnd"] = prop["CullEnd"]
		if "SurfaceHeightMax" in prop:
			temp_prop["SurfaceHeightMax"] = prop["SurfaceHeightMax"]
		if "SurfaceHeightMin" in prop:
			temp_prop["SurfaceHeightMin"] = prop["SurfaceHeightMin"]
		if "TopHeightMax" in prop:
			temp_prop["TopHeightMax"] = prop["TopHeightMax"]
		if "HighDetailShadow" in prop:
			temp_prop["HighDetailShadow"] = prop["HighDetailShadow"]
		if "Streamed" in prop:
			temp_prop["Streamed"] = prop["Streamed"]
		objects_array.append(temp_prop)

DENSITY_MUL = 0.6

TREE_PROPS = {"Broadleaf", "Conifer", "Pine", "SnowyPine", "Palm"}

CLUSTER_PROPS = {
	"Shrub", "BigBush", "Fern", "Cactus",
	"Rock", "SmallRock", "VolcanicRock", "SmallVolcanicRock", "SnowyRock", "CanyonRock",
}

DEFAULT_CLUSTER = {
	"MinRadius": 2,
	"MaxRadius": 7,
	"MinCount": 3,
	"MaxCount": 10,
	"CenterSpacing": 14,
	"Jitter": 1.5,
	"DensityThreshold": 0.5,
}

SPARSE_CLUSTER = {
	**DEFAULT_CLUSTER,
	"MinCount": 2,
	"MaxCount": 5,
	"CenterSpacing": 20,
	"DensityThreshold": 0.45,
}

DESERT_CLUSTER = {
	**DEFAULT_CLUSTER,
	"MinCount": 2,
	"MaxCount": 4,
	"CenterSpacing": 18,
	"DensityThreshold": 0.48,
}

PROP_CLUSTER_SETTINGS = {
	"Cactus": DESERT_CLUSTER,
	"Rock": SPARSE_CLUSTER,
	"SmallRock": SPARSE_CLUSTER,
	"VolcanicRock": SPARSE_CLUSTER,
	"SmallVolcanicRock": SPARSE_CLUSTER,
	"SnowyRock": SPARSE_CLUSTER,
	"CanyonRock": SPARSE_CLUSTER,
}

# PropsGenerator name -> legacy StaticPropList name (Biomes.py references generator by name).
PROPS_GENERATOR_SOURCES = [
	("PrairieDryProps", "PrairieDryPropList"),
	("PrairieProps", "PrairiePropList"),
	("DipteroProps", "DipteroPropList"),
	("BogProps", "SwampProps"),
	("BogForestProps", "SwampForestProps"),
	("OreProps", "ClayBeachProps"),
	("GrasslandProps", "GrasslandProps"),
	("GrasslandPropsRed", "RedFlowersProps"),
	("GrasslandPropsWhite", "WhiteFlowersProps"),
	("GrasslandPropsYellow", "YellowFlowersProps"),
	("BushlandProps", "BushlandProps"),
	("ForestProps", "ForestProps"),
	("PineForestProps", "PineForestProps"),
	("FertileForestProps", "FertileForestProps"),
	("SeaPlantProps", "SeaPlantProps"),
	("SeaGrassProps", "SeaGrassProps"),
	("EmptySeaProps", "EmptySeaProps"),
	("VolcanicProps", "VolcanicProps"),
	("SandlandProps", "DesertProps"),
	("SnowProps", "SnowProps"),
	("SnowGrassGenerator", "SnowGrassProps"),
	("SnowForestGenerator", "SnowForestProps"),
	("HillsProps", "GrasslandProps"),
	("HillsForestProps", "BushlandProps"),
	("MountainSnowProps", "SnowProps"),
]

def expand_prop_variations(prop_names):
	result = []
	for prop_name in prop_names:
		for variation in range(named_prop(prop_name)["Variations"]):
			result.append(prop_name + variation_helper[variation])
	return result

def emit_static_proplist(list_name, prop_names):
	objects_array.append({
		"Class": "StaticPropList",
		"Name": list_name,
		"Array": [{
			"Props": expand_prop_variations(prop_names),
			"Weight": 1,
		}],
	})

def cluster_settings_for(prop_names):
	for prop_name in prop_names:
		if prop_name in PROP_CLUSTER_SETTINGS:
			return PROP_CLUSTER_SETTINGS[prop_name]
	return DEFAULT_CLUSTER

def is_cluster_layer(prop_names):
	if any(p in TREE_PROPS for p in prop_names):
		return False
	return any(p in CLUSTER_PROPS for p in prop_names)

def layers_from_legacy_proplist(generator_name, legacy_plist):
	layers = []
	for index, entry in enumerate(legacy_plist["Array"]):
		if "Attaches" in entry:
			continue
		prop_names = entry.get("Props", [])
		if not prop_names:
			continue
		chance = entry["Chance"]
		list_name = f"{generator_name}_L{index}_{prop_names[0]}"
		emit_static_proplist(list_name, prop_names)
		if is_cluster_layer(prop_names):
			layers.append({
				"Mode": "Cluster",
				"PropList": list_name,
				"Cluster": cluster_settings_for(prop_names),
			})
		else:
			layers.append({
				"Mode": "Scatter",
				"PropList": list_name,
				"Density": round(chance * DENSITY_MUL, 6),
			})
	return layers

proplist_by_name = {entry["Name"]: entry for entry in proplists}

for generator_name, legacy_name in PROPS_GENERATOR_SOURCES:
	legacy_plist = proplist_by_name[legacy_name]
	layers = layers_from_legacy_proplist(generator_name, legacy_plist)
	objects_array.append({
		"Class": "PropsGenerator",
		"Name": generator_name,
		"Layers": layers,
	})

objects_array.append({
    "Class": "StaticPropList",
	"Name": "OreProps",
	"Array": [{
		"Props": ore_props,
		"Weight": 1
	}]
})
	
data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/props.json", data)