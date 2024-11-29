from MachinesList import *
from Common import *

objects_array = []

cvs = []

ore_types = [
	{
		# https://en.wikipedia.org/wiki/List_of_copper_ores
		"Name": "Copper",
		"Byproducts":[
			"GoldDust", # wash
			["CopperOreDust", "MalachiteCrystal", "MalachiteCluster"], #sifter
		],
		"Color": [0.8/2.0,.3/2.0,.3/2.0],
		"Hardness": 1.5,
		"Drops": "CopperOre",
		"Remain": 1000,
	},{
		# https://www.tf.uni-kiel.de/matwis/amat/iss/kap_a/advanced/aa_2_1.html
		# https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D0%BA%D0%B5%D0%BB%D1%8C#%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5
		"Name": "Iron",
		"Byproducts":[
			"ChromiumOxideDust", # wash
			["IronOreDust", "CinnabarCrystal", "CinnabarCluster"], #sifter
		],
		"Color": [111 / 255./2.0, 106 / 255./2.0, 81 / 255./2.0],
		"Hardness": 2,
		"Drops": "IronOre",
		"Remain": 1000,
	},{
		"Name": "Uranium",
		"Byproducts":[
			"Uranium235Dust", # wash
			["ThoriumDust", "UraniniteCrystal", "UraniniteCluster"], #sifter
		],
		"ByproductChanse":[
		0.05
		],
		"Color": [0.3/2.0, 0.7/2.0, 0.3/2.0],
		"Hardness": 2,
		"Tier": 5,
		"Drops": "UraniumOre",
		"Remain": 1000,
	},{
		# https://en.wikipedia.org/wiki/Cassiterite
		"Name": "Aluminium",
		"Byproducts":[
			"TitaniumOxideDust", # wash
			["AluminiumOreDust", "RutileCrystal", "Emerald"], #sifter
		],
		"Color": [.5/2.0, .5/2.0, 1/2.0],
		"Hardness": 2,
		"Drops": "AluminiumOre",
		"Oxide": True,
		"Remain": 1000,
	},{
		"Name": "Coal",
		"Color": [.06, .06, .06],
		"Side": [.06, .06, .06],
		"Item": [.06, .06, .06],
		"Drops": "Coal",
		"Tier": 0,
		"Hardness": 1,
		"NotOre": True,
		"Remain": 1000,
	},{
		"Name": "Clay",
		"Color": [202 / 255., 115 / 512., 43 / 512.],
		"Side": [202 / 255., 115 / 512., 43 / 512.],
		"Item": [202 / 255., 115 / 512.,  43 / 512.],
		"Drops": "Clay",
		"Tier": 0,
		"Hardness": 1,
		"NotOre": True,
		"Byproducts":[
			"RareEarthElement"
		],
	}
]

images = []

for ore_type in ore_types:
	item_name = ore_type["Name"] + "Ore" + static_item
	named_mat = named_material(ore_type["Name"])
	
	cvs.append([ore_type["Name"]+"Ore", ore_type["Name"]+" Ore"])
	
	item = { "Class": "StaticItem",
		"Name": item_name,
		"Mesh": "/Game/Models/Ore",
		"Image": "T_" + ore_type["Name"] + "Ore",
		"StackSize": 64, 
		"Category": "Ore",
		"LabelParts": [[ore_type["Name"]+"Ore", "ores"]],
		"CommonTextKeys":[
		],
		"Materials" : [
			"/Game/Materials/" + ore_type["Name"] + "ImpureOreGravel"
		],
	}
	if "SmeltLevel" in named_mat:
		item["CommonTextKeys"].append("SmeltLevel" + str(named_mat["SmeltLevel"]))
	
	objects_array.append(item)
	objects_array.append({ "Class": "TesselatorMarching",
		"Name": ore_type["Name"] + "Ore" + tesselator,
		"Material": "/Game/Materials/Triplanar/" + ore_type["Name"] + "OreMaterial"
	})
	objects_array.append({ "Class": "StaticBlock",
		"Name": ore_type["Name"] + "Ore" + static_surface,
		"Tesselator": ore_type["Name"] + "Ore" + tesselator,
		"Item": item_name,
		"ColorSide": ore_type["Color"],
		"ColorTop": ore_type["Color"],
		"Minable": {"Result": ore_type["Drops"] + static_item},
		"Surface": True
	})
	images.append({
		"Base": "T_" + "Ore",
		"NewName": "T_" + ore_type["Name"] + "Ore",
		"MulMask": "T_" + ore_type["Name"]
	})

	if "NotOre" not in ore_type:		
		# impur gravel		
		cvs.append([ore_type["Name"]+"ImpureOreGravel", ore_type["Name"]+" Impure Ore Gravel"])
		item = { "Class": "StaticItem",
			"Name": ore_type["Name"] + "ImpureOreGravel" + static_item,
			"Label": ore_type["Name"] + " Impure Ore Gravel",
			"Mesh": "/Game/Models/Gravel",
			
			"Image": "T_" + ore_type["Name"] + "ImpureOreGravel",
			"StackSize": 64, 

			"Materials" : [
				"/Game/Materials/" + ore_type["Name"] + "ImpureOreGravel"
			],
			"Category": "Ore",
			
			"LabelParts": [[ore_type["Name"]+"ImpureOreGravel","ores"]],
			
			"CommonTextKeys":[
			],
		}
		if "SmeltLevel" in named_mat:
			item["CommonTextKeys"].append("SmeltLevel" + str(named_mat["SmeltLevel"]))
		if "Mesh" in named_mat:
			item["Mesh"] = named_mat["Mesh"]
		objects_array.append(item)
		# gravel
		cvs.append([ore_type["Name"]+"OreGravel", ore_type["Name"]+" Ore Gravel"])
		item = { "Class": "StaticItem",
			"Name": ore_type["Name"] + "OreGravel" + static_item,
			"Label": ore_type["Name"] + " Ore Gravel",
			"Mesh": "/Game/Models/Gravel",
			
			"Image": "T_" + ore_type["Name"] + "OreGravel",
			"StackSize": 64,

			"Materials" : [
				"/Game/Materials/" + ore_type["Name"] + "OreGravel"
			],
			"Category": "Ore",
			
			"LabelParts": [[ore_type["Name"]+"OreGravel","ores"]],
			
			"CommonTextKeys":[
			],
		}
			
		if "SmeltLevel" in named_mat:
			item["CommonTextKeys"].append("SmeltLevel" + str(named_mat["SmeltLevel"]))
		objects_array.append(item)
			
		# impure dust
		cvs.append([ore_type["Name"] + "OreDust", ore_type["Name"]+" Impure Ore Dust"])
		item = { "Class": "StaticItem",
			"Name": ore_type["Name"] + "OreDust" + static_item,
			"Label": ore_type["Name"] + " Impure Ore Dust",
			"Mesh": "/Game/Models/Dust",
			
			"Image": "T_" + ore_type["Name"] + "OreDust",
			"StackSize": 64,

			"Materials" : [
				"/Game/Materials/ImpureOreDust"
			],
			"Category": "Ore",
			
			"LabelParts": [[ore_type["Name"]+"OreDust","ores"]],
			
			"CommonTextKeys":[
			],
			"Materials" : [
				"/Game/Materials/" + ore_type["Name"] + "OreGravel"
			],
		}
			
		if "SmeltLevel" in named_mat:
			item["CommonTextKeys"].append("SmeltLevel" + str(named_mat["SmeltLevel"]))
		objects_array.append(item)
		images.append({
			"Base": "T_" + "Gravel",
			"NewName": "T_" + ore_type["Name"] + "OreGravel",
			"MulMask": "T_" + ore_type["Name"],
			"AddMask": "T_" + "Gravel" + additive_ico
		})
		images.append({
			"Base": "T_" + "Gravel",
			"NewName": "T_" + ore_type["Name"] + "ImpureOreGravel",
			"MulMask": "T_" + ore_type["Name"],
			"AddMask": ["T_" + "impure_gravel_add", "T_"+"Gravel" + additive_ico]
		})
		images.append({
			"Base": "T_" + "Dust",
			"NewName": "T_" + ore_type["Name"] + "OreDust",
			"MulMask": "T_" + ore_type["Name"],
			"AddMask": "T_" + "impure_dust_add"
		})
data = {
	"Objects": objects_array
}
filename = "Generated/Mixed/ores.json"

write_file(filename, data)
 
objects_array = []

objects_array.append({	
		"Class": ico_generator,
		"Name": "Ores" + ico_generator,
		"Images": images
	})
	
data = {
	"Objects": objects_array
}

write_file("Generated/Resources/ores.json", data);

write_file("Loc/source/ores.json", cvs)