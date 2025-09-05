from Common import *
from OresGen import ore_types

cvs = []

variation_helper = [
	"", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"
]

props = [
	{
		"Name": "Cactus",
		"ScaleMin": .5,
		"ScaleMax": 2,
		"Variations": 3,
		"ProjectToTerrainPower": 1,
		"IsBig": True,
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
		"AdditiveElevation": 0
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
		"AdditiveElevation": 15
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
		"AdditiveElevation": 15
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
		"MaximumHeight": -1,
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
		"MaximumHeight": -1,
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
		"AdditiveElevation": 0
	},
	{
		"Name": "Broadleaf",
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 3,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"Count": 3,
		"BreakChance": 15
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
		"Count": 5,
		"AdditiveElevation": 0,
		"BreakChance": 15
	},
	{
		"Name": "Pine",
		"ScaleMin": .6,
		"ScaleMax": 1.4,
		"Variations": 3,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"Count": 3,
		"BreakChance": 15
	},
	{
		"Name": "SnowyPine",
		"ScaleMin": .6,
		"ScaleMax": 1.2,
		"Variations": 3,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"Count": 3,
		"BreakChance": 15
	},
	{
		"Name": "Conifer",
		"ScaleMin": .6,
		"ScaleMax": 1.4,
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"Count": 2,
		"BreakChance": 25
	},
	{
		"Name": "Palm",
		"ScaleMin": .6,
		"ScaleMax": 1.3,
		"Variations": 2,
		"ProjectToTerrainPower": 0,
		"IsBig": True,
		"Drops": "Log",
		"Count": 2,
		"BreakChance": 25
	},
	{
		"Name": "Rogoz",
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 5,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"IsBig": False,
		"Count": 1,
		"CullBegin": 7000,
		"CullEnd": 8000,
		"AdditiveElevation": 0
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
		"AdditiveElevation": 70,
		"Floating": True,
		"IsBig": False,
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
		"AdditiveElevation": 70,
		"Floating": True,
		"IsBig": False,
	},{
		"Name": "Shroom",
		"ScaleMin": 1,
		"ScaleMax": 2,
		"Variations": 6,
		"ProjectToTerrainPower": 0,
		"Drops": "Organics",
		"Count": 10,
		"AdditiveElevation": 20,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"IsBig": False,
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
		"BreakChance": 25
	},{
		"Name": "SmallRock",
		"ScaleMin": 1,
		"ScaleMax": 3,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": "StoneSurface",
		"Count": 10,
		"CullBegin": 10000,
		"CullEnd": 12000,
		"AdditiveElevation": 0,
		"IsBig": False,
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
	},{
		"Name": "VolcanicRock",
		"ScaleMin": .5,
		"ScaleMax": 1,
		"Variations": 4,
		"ProjectToTerrainPower": 1,
		"Drops": "BasaltSurface",
		"IsBig": True,
		"AdditiveElevation": 0,
		"Count": 3,
		"BreakChance": 5
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
		"Count": 3,
		"BreakChance": 10
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
		"AdditiveElevation": 70,
		"Floating": True,
		"IsBig": False,
	}
]

for ore in ore_types:
	props.append({
		"Name": ore["Name"] + "Cluster",
		"ScaleMin": 2,
		"ScaleMax": 2,
		"Variations": 1,
		"ProjectToTerrainPower": 1,
		"Drops": ore["Name"] + "Ore",
		"Count": 1,
		"CullBegin": 90000,
		"CullEnd": 100000,
		"AdditiveElevation": 0,
		"IsBig": True,
		"Image": "T_Error",
		"BreakChance": 0
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
	},{ 
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
				"Chance": 0.06
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

objects_array = []

for prop in props: 
	cvs.append([prop["Name"], CamelToSpaces(prop["Name"])])
	for variation in range(0, prop["Variations"]):
		image = "T_" + prop["Name"] if "Image" not in prop else prop["Image"]
		objects_array.append({ "Class": "StaticItem",
			"Name": prop["Name"] + variation_helper[variation],
			"StackSize": 32,
			"Image": image,
			"Category": "Terrain",
			"Label": [prop["Name"], "props"],
			"DescriptionParts":[["WorldObject","common"]],
		})
		
		temp_prop = { "Class": "StaticProp",
			"Name": prop["Name"] + variation_helper[variation],
			"Mesh": "/Game/Props/" + prop["Name"] + "/" + prop["Name"] + variation_helper[variation],
			"ScaleMin": prop["ScaleMin"],
			"ScaleMax": prop["ScaleMax"],
			"ProjectToTerrainPower": prop["ProjectToTerrainPower"],
			"Item": prop["Name"],
			"Minable": {
				"Result": prop["Drops"],
				"Count": prop["Count"]
			},
			"IsBig": prop["IsBig"]
		}
		
		if "BreakChance" in prop:
			temp_prop["BreakChance"] = prop["BreakChance"]
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

def convert_proplists(proplists, DensityMultiplier=0.6):
    for proplist in proplists:
        proplist_datas = []
        raw_chances = [item["Chance"] * DensityMultiplier for item in proplist["Array"]]
        scale = 10000
        total_weight = 0

        for subitem, chance in zip(proplist["Array"], raw_chances):
            props_array = []
            if "Props" in subitem:
                for prop_name in subitem["Props"]:
                    for variation in range(named_prop(prop_name)["Variations"]):
                        props_array.append(prop_name + variation_helper[variation])

            weight = int(round(chance * scale))
            total_weight += weight

            proplist_datas.append({
                "Props": props_array,
                "Weight": weight
            })

        if scale - total_weight > 0.0001:
            proplist_datas.append({
                "Props": [],
                "Weight": scale - total_weight
            })

        objects_array.append({
            "Class": "StaticPropList",
            "Name": proplist["Name"],
            "Array": proplist_datas
        })

convert_proplists(proplists)

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

write_file("Generated/Mixed/props.json", data); 

objects_array = []


write_file("Loc/source/props.json", cvs)