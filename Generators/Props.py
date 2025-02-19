from Common import *

cvs = []

variation_helper = [
	"", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"
]

props = [
	{
		"Name": "Cactus",
		"ScaleMin": [.5, .5, .5],
		"ScaleMax": [2, 2, 2],
		"Variations": 2,
		"ProjectToTerrainPower": 1,
		"IsBig": True,
		"Drops": "Organics",
		"AdditiveElevation": 0,
		"TimeMul": 1
	},
	{
		"Name":"Dandaleon",
		"ScaleMin": [2, 2, 2],
		"ScaleMax": [4, 4, 4],
		"Variations": 3,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0
	},
	{
		"Name": "Fern",
		"ScaleMin": [4, 4, 4],
		"ScaleMax": [6, 6, 6],
		"Variations": 3,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0
	},
	{
		"Name": "LongGrass",
		"ScaleMin": [3.5, 3.5, 3.5],
		"ScaleMax": [4, 4, 4],
		"Variations": 4,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 15
	},
	{
		"Name": "SeaPlant",
		"ScaleMin": [2, 2, 2],
		"ScaleMax": [4, 4, 4],
		"Variations": 22,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"MaximumHeight": -1,
	},
	{
		"Name": "SeaGrass",
		"ScaleMin": [2, 2, 2],
		"ScaleMax": [4, 4, 4],
		"Variations": 5,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"MaximumHeight": -1,
	},
	{
		"Name": "TallGrass",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [3, 3, 3],
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0
	},
	{
		"Name": "Broadleaf",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [3, 3, 3],
		"Variations": 3,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"TimeMul": 1
	},
	{
		"Name": "Noleafes",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [3, 3, 3],
		"Variations": 1,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"TimeMul": 1
	},
	{
		"Name": "Shrub",
		"ScaleMin": [1.5, 1.5, 1.5],
		"ScaleMax": [2.5, 2.5, 2.5],
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"IsBig": True,
		"Drops": "Log",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"TimeMul": 1
	},
	{
		"Name": "Rock",
		"ScaleMin": [.6, .6, .6],
		"ScaleMax": [3, 3, 3],
		"Variations": 2,
		"ProjectToTerrainPower": 1,
		"IsBig": True,
		"Drops": "StoneSurface",
		"DropCount": 10,
		"AdditiveElevation": 0,
		"TimeMul": 1
	},
	{
		"Name": "Pine",
		"ScaleMin": [.6, .6, .6],
		"ScaleMax": [1.4, 1.4, 1.4],
		"Variations": 3,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"TimeMul": 1
	},
	{
		"Name": "SnowyPine",
		"ScaleMin": [.6, .6, .6],
		"ScaleMax": [1.2, 1.2, 1.2],
		"Variations": 3,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"TimeMul": 1
	},
	{
		"Name": "Birch",
		"ScaleMin": [.6, .6, .6],
		"ScaleMax": [1.4, 1.4, 1.4],
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"TimeMul": 1
	},
	{
		"Name": "Palm",
		"ScaleMin": [.6, .6, .6],
		"ScaleMax": [1.4, 1.4, 1.4],
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"TimeMul": 1
	},
	{
		"Name": "Rogoz",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [3, 3, 3],
		"Variations": 5,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"CullBegin": 7000,
		"CullEnd": 8000,
		"AdditiveElevation": 0
	},{
		"Name": "Lily", 
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [3, 3, 3],
		"Variations": 1,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"CullBegin": 7000,
		"CullEnd": 8000,
		"AdditiveElevation": 70,
		"Floating": True,
	},{
		"Name": "LilyFlower",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [3, 3, 3],
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"CullBegin": 7000,
		"CullEnd": 8000,
		"AdditiveElevation": 70,
		"Floating": True,
	},{
		"Name": "Shroom",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [2, 2, 2],
		"Variations": 6,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"AdditiveElevation": 20,
		"CullBegin": 10000,
		"CullEnd": 12000,
	},{
		"Name": "YellowFlower",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [2, 2, 2],
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0
	},{
		"Name": "RedFlower",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [2, 2, 2],
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0
	},{
		"Name": "WhiteFlower",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [2, 2, 2],
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0
	},{
		"Name": "BigBush",
		"ScaleMin": [1.5, 1.5, 1.5],
		"ScaleMax": [3, 3, 3],
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"HandInteraction": True,
		"Drops": "Plank",
		"AdditiveElevation": 0,
		"CullBegin": 10000,
		"CullEnd": 12000,
	},{
		"Name": "SmallRock",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [3, 3, 3],
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"HandInteraction": True,
		"Drops": "StoneSurface",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0
	},{
		"Name": "Diptero",
		"ScaleMin": [.8, .8, .8],
		"ScaleMax": [1.3, 1.3, 1.3],
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"HandInteraction": False,
		"AdditiveElevation": 0,
		"IsBig": True,
		"Drops": "Log",
		"TimeMul": 6
	},{
		"Name": "DryGrass",
		"ScaleMin": [1, 1, 1],
		"ScaleMax": [2, 2, 2],
		"Variations": 2,
		"ProjectToTerrainPower": 1,
		"HandInteraction": False,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0
	},{
		"Name": "VolcanicRock",
		"ScaleMin": [.5, .5, .5],
		"ScaleMax": [1, 1, 1],
		"Variations": 4,
		"ProjectToTerrainPower": 1,
		"HandInteraction": False,
		"Drops": "BasaltSurface",
		"DropCount": 10,
		"IsBig": True,
		"AdditiveElevation": 0,
		"TimeMul": 1
	},{
		"Name": "SnowyRock",
		"ScaleMin": [.5, .5, .5],
		"ScaleMax": [1, 1, 1],
		"Variations": 4,
		"ProjectToTerrainPower": 1,
		"HandInteraction": False,
		"Drops": "BasaltSurface",
		"DropCount": 10,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"IsBig": True,
		"AdditiveElevation": 0,
		"TimeMul": 1
	},{
		"Name": "SnowyGrass",
		"ScaleMin": [2, 2, 2],
		"ScaleMax": [4, 4, 4],
		"Variations": 3,
		"ProjectToTerrainPower": 1,
		"HandInteraction": False,
		"Drops": "Organics",
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0
	}
]

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
				"Props": ["Broadleaf", "Broadleaf", "Birch", "BigBush", "Noleafes"],
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
				"Props": ["LongGrass"],
				"Chance": 0.35
			},{
				"Props": ["Broadleaf", "Broadleaf", "Birch", "BigBush", "Noleafes"],
				"Chance": 0.0004
			}
		]
	},
	{ 
		"Name": "DipteroPropList",
		"Array": [
			{
				"Props": ["Diptero"],
				"Chance": 0.001
			},{
				"Props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
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
		"Name": "SmallRocksProps",
		"Array": [
			{
				"Props": ["SmallRock"],
				"Chance": 0.06
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
		"Name": "DenseForestProps",
		"Array": [
			{
				"Props": ["Noleafes"],
				"Chance": 0.001
			},{
				"Props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
				"Chance": 0.02
			},{
				"Props": ["SmallRock"],
				"Chance": 0.01
			},{
				"Props": ["Fern"],
				"Chance": 0.03
			},{
				"Props": ["Dandaleon"],
				"Chance": 0.3
			},{
				"Props": ["LongGrass"],
				"Chance": 0.75
			},{
				"Props": ["Shroom"],
				"Chance": 0.01
			}
		]
	},{ 
		"Name": "ForestProps",
		"Array": [
			{
				"Props": ["Noleafes"],
				"Chance": 0.001
			},{
				"Props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
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
	},{ 
		"Name": "DensePineForestProps",
		"Array": [
			{
				"Props": ["Rock"],
				"Chance": 0.001
			},{
				"Props": ["SmallRock"],
				"Chance": 0.01
			},{
				"Props": ["Pine"],
				"Chance": 0.02
			},{
				"Props": ["DryGrass"],
				"Chance": 0.03
			},{
				"Props": ["Shroom"],
				"Chance": 0.01
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
		"Name": "IslandProps",
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
		"Name": "SeagrassProps",
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
				"Props": ["Birch", "BigBush"],
				"Chance": 0.01
			},{
				"Props": ["Shroom"],
				"Chance": 0.01
			}
		]
	},{	
		"Name": "OreProps",
		"Array": [
			{
				"Props": ["LongGrass"],
				"Chance": 0.07
			},{
				"Props": ["Birch", "BigBush"],
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
			}
		]
	},
	{	
		"Name": "SnowForestProps",
		"Array": [
			{
				"Props": ["SnowyGrass"],
				"Chance": 0.2
			},
			{
				"Props": ["SnowyPine"],
				"Chance": 0.005
			}
		]
	}
]

objects_array = []
breaking_hand = []

for prop in props: 
	cvs.append([prop["Name"], CamelToSpaces(prop["Name"])])
	for variation in range(0, prop["Variations"]):
		objects_array.append({ "Class": "StaticItem",
			"Name": prop["Name"] + variation_helper[variation],
			
			"StackSize": 32,
			"Image": "T_" + prop["Name"],
			"LogicJson": {
				"StaticBlock": prop["Name"] + variation_helper[variation]
			},
			"ItemLogic": building_prop_logic,
			"Category": "Terrain",
			
			"LabelParts": [[prop["Name"], "props"]],
			"DescriptionParts":[["WorldObject","common"]],
		})
		
		temp_prop = { "Class": "BigStaticProp" if "IsBig" in prop else "SmallStaticProp",
			"Name": prop["Name"] + variation_helper[variation],
			"Mesh": "/Game/Props/" + prop["Name"] + "/" + prop["Name"] + variation_helper[variation],
			"ScaleMin": prop["ScaleMin"],
			"ScaleMax": prop["ScaleMax"],
			"ProjectToTerrainPower": prop["ProjectToTerrainPower"],
			"Item": prop["Name"],
			"Minable": {"Result": prop["Drops"]},
		}
		
		if "CullBegin" in prop:
			temp_prop["CullBegin"] = prop["CullBegin"]
			
		if "Floating" in prop:
			temp_prop["Floating"] = prop["Floating"]
			
		if "CullEnd" in prop:
			temp_prop["CullEnd"] = prop["CullEnd"]
			
		if "AdditiveElevation" in prop:
			temp_prop["AdditiveElevation"] = prop["AdditiveElevation"]	
			
		if "MaximumHeight" in prop:
			temp_prop["MaximumHeight"] = prop["MaximumHeight"]	
			
		if "MinimumHeight" in prop:
			temp_prop["MinimumHeight"] = prop["MinimumHeight"]	
			
		objects_array.append(temp_prop)


for proplist in proplists:
	proplist_datas = []
	for subitem in proplist["Array"]:
		props_array = []
		if "Props" in subitem:
			for prop_name in subitem["Props"]:
				for variation in range(0, named_prop(prop_name)["Variations"]):
					props_array.append(prop_name + variation_helper[variation])
		proplist_datas.append({
			"Props": props_array,
			"Chance": subitem["Chance"] * 0.5
		})
	objects_array.append({ "Class": prop_list,
		"Name": proplist["Name"],
		"Array": proplist_datas
	})
	
data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/props.json", data); 

objects_array = []

objects_array.append({ "Class": breaking_recipe,
	"Name": "Multitool" + breaking_recipe,
	"Recipes": breaking_hand
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/props.json", data);

write_file("Loc/source/props.json", cvs)