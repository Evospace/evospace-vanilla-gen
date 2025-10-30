from Common import *

objects_array = []

csv = []

mapgen_objects = [
	{
		"Name": "Sand",
		"Color": "#fbeebf",
		"Side": "#928c76",
		"Drops": "Sand",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/SandBreakEffect.SandBreakEffect_C"
	},{
		"Name": "Sandstone",
		"Color": "#fbeebf",
		"Side": "#928c76",
		"Drops": "Sand",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/SandBreakEffect.SandBreakEffect_C"
	},{
		"Name": "Stone",
		"Color": "#928c76",
		"Side": "#928c76",
		"Drops": "Stone",
		"Hardness": 2
	},{
		"Name": "DesertSand",
		"Color": "#fde489",
		"Side": "#fde489",
		"Drops": "Sand",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/SandBreakEffect.SandBreakEffect_C"
	},{
		"Name": "Grass",
		"Color": "#525c27",
		"Side": "#55321d",
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "Lava",
		"Color": "#686868",
		"Side": "#414141",
		"Drops": "Basalt",
		"Hardness": 5
	},{
		"Name": "Basalt",
		"Color": "#696969",
		"Side": "#414141",
		"Drops": "Basalt",
		"Hardness": 2
	},{
		"Name": "Bog",
		"Color": "#24120a",
		"Side": "#2c2215",
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "PineForest",
		"Color": "#574226",
		"Side": "#574226",
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "Dirt",
		"Color": "#866640",
		"Side": "#866640",
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "Gravel",
		"Color": "#e9ddb1",
		"Side": "#e9ddb1",
		"Drops": "Gravel",
		"Hardness": 1
	},{
		"Name": "DryGrass",
		"Color": "#55321d",
		"Side": "#866641",
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "Clay",
		"Color": "#6f452e",
		"Side": "#6f452e",
		"Drops": "Sand",
		"Hardness": 1.0,
		"BreakEffect": "/Game/EffectActors/ClayBreakEffect.ClayBreakEffect_C"
	},{
		"Name": "Limestone",
		"Color": "#a19c87",
		"Side": "#a19c87",
		"Drops": "Gravel",
		"Hardness": 1.5
	},{
		"Name": "RedStone",
		"Color": "#5b3823",
		"Side": "#5b3823",
		"Drops": "RedStone",
		"Hardness": 2
	},{
		"Name": "DarkStone",
		"Color": "#0c080c",
		"Side": "#0c080c",
		"Drops": "DarkStone",
		"Hardness": 2
	},{
		"Name": "Snow",
		"Color": "#fdfcfe",
		"Side": "#856540",
		"Drops": "Snow",
		"Hardness": 1
	},{
		"Name": "Granite",
		"Color": "#6f6a55",
		"Side": "#6f6a55",
		"Drops": "Granite",
		"Hardness": 4,
		"Unbreakable": True
	},{
		"Name": "Peat",
		"Color": "#0f0f05",
		"Side": "#12120e",
		"Drops": "Peat",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/PeatBreakEffect.PeatBreakEffect_C"
	},
]

pickaxe_recipes = []

for object in mapgen_objects:
	csv.append([object["Name"] + "Surface", CamelToSpaces(object["Name"])])

	objects_array.append({ "Class": "StaticItem",
		"Name": object["Name"] + "Surface",
		"Image": "T_" + object["Name"],
		
		"ItemLogic": building_brush_slot_logic,
		"Mesh": "/Game/Models/piece",
		"Materials" : ["/Game/Materials/" + object["Drops"]],
		"Block": object["Name"] + "Surface",
		"StackSize": 999,
		"Label": [object["Name"]+ "Surface", "mapgen_core"],
	})
	objects_array.append({ "Class": "TesselatorMarching",
		"Name": object["Name"] + "Surface" + tesselator,
		"Material": "/Game/Materials/Triplanar/" + object["Name"] + "Material"
	})
	staticBlock = {
		"Class": "StaticBlock",
		"Name": object["Name"] + "Surface" + static_surface,
		"Tesselator": object["Name"] + "Surface" + tesselator,
		"Item" : object["Name"] + "Surface",
		"ColorSide": object["Side"],
		"ColorTop": object["Color"],
		"Minable": {"Minable": False} if "Unbreakable" in object else {"Result": object["Drops"] + "Surface"},
		"Surface": True
	}
	if "BreakEffect" in object:
		staticBlock["BreakEffect"] = object["BreakEffect"]
	objects_array.append(staticBlock)
	
data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/mapgen_core.json", data);
write_file("Loc/source/mapgen_core.json", csv)