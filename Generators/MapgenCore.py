from Common import *

objects_array = []

csv = []

mapgen_objects = [
	{
		"Name": "Sand",
		"Color": [142 / 255., 119 / 255.,  71 / 255.],
		"Side": [158 / 255., 123 / 255.,  100 / 255.],
		"Item": [200 / 255., 200 / 255.,  50 / 255.],
		"Drops": "Sand",
		"Hardness": 1
	},{
		"Name": "Sandstone",
		"Color": [223 / 255., 221 / 255.,  192 / 255.],
		"Side": [158 / 255., 123 / 255.,  100 / 255.],
		"Item": [200 / 255., 200 / 255.,  50 / 255.],
		"Drops": "Sand",
		"Hardness": 1
	},{
		"Name": "Stone",
		"Color": [111 / 255., 106 / 255., 85 / 255.],
		"Side": [111 / 255., 106 / 255., 85 / 255.],
		"Item": [128 / 255., 128 / 255.,  128 / 255.],
		"Drops": "Stone",
		"Hardness": 2
	},{
		"Name": "DesertSand",
		"Color": [175 / 255., 148 / 255.,  87 / 255.],
		"Side": [180 / 255., 133 / 255.,  109 / 255.],
		"Item": [200 / 255., 200 / 255.,  50 / 255.],
		"Drops": "Sand",
		"Hardness": 1
	},{
		"Name": "Grass",
		"Color": [85 / 255. / 5, 100 / 255. / 5, 29 / 255. / 5],
		"Side": [134 / 255. / 5, 102 / 255. / 5,  64 / 255. / 5],
		"Item": [102 / 255., 51 / 255.,  0 / 255.],
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "BogFog",
		"Color": [255 / 255., 0 / 255.,  0 / 255.],
		"Side": [255 / 255., 0 / 255.,  0 / 255.],
		"Item": [102 / 255., 51 / 255.,  0 / 255.],
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "Lava",
		"Color": [104 / 255., 104 / 255., 104 / 255.],
		"Side": [104 / 255., 104 / 255., 104 / 255.],
		"Item": [127 / 255., 127 / 255.,  127 / 255.],
		"Drops": "Basalt",
		"Hardness": 5
	},{
		"Name": "Basalt",
		"Color": [105 / 255., 105 / 255., 105 / 255.],
		"Side": [105 / 255., 105 / 255., 105 / 255.],
		"Item": [128 / 255., 128 / 255.,  128 / 255.],
		"Drops": "Basalt",
		"Hardness": 2
	},{
		"Name": "Bog",
		"Color": [109 / 255. / 5, 108 / 255. / 5,  20 / 255. / 5],
		"Side": [134 / 255. / 5, 102 / 255. / 5,  64 / 255. / 5],
		"Item": [102 / 255., 51 / 255.,  0 / 255.],
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "PineForest",
		"Color": [87 / 255., 66 / 255., 38 / 255.],
		"Side": [87 / 255., 66 / 255.,  38 / 255.],
		"Item": [102 / 255., 51 / 255.,  0 / 255.],
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "Dirt",
		"Color": [134 / 255., 102 / 255.,  64 / 255.],
		"Side": [134 / 255., 102 / 255.,  64 / 255.],
		"Item": [102 / 255., 51 / 255.,  0 / 255.],
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "Gravel",
		"Color": [141 / 255., 118 / 255.,  70 / 255.],
		"Side": [141 / 255., 118 / 255.,  70 / 255.],
		"Item": [200 / 255., 200 / 255.,  50 / 255.],
		"Drops": "Gravel",
		"Hardness": 1
	},{
		"Name": "DryGrass",
		"Color": [85 / 255., 50 / 255., 29 / 255.],
		"Side": [134 / 255., 102 / 255.,  65 / 255.],
		"Item": [102 / 255., 51 / 255.,  0 / 255.],
		"Drops": "Dirt",
		"Hardness": 1
	},{
		"Name": "Limestone",
		"Color": [161 / 255., 156 / 255., 135 / 255.],
		"Side": [161 / 255., 156 / 255., 135 / 255.],
		"Item": [161 / 255., 156 / 255., 135 / 255.],
		"Drops": "Gravel",
		"Hardness": 1.5
	},{
		"Name": "RedStone",
		"Color": [91 / 255., 56 / 255., 35 / 255.],
		"Side": [91 / 255., 56 / 255., 35 / 255.],
		"Item": [91 / 255., 56 / 255., 35 / 255.],
		"Drops": "RedStone",
		"Hardness": 2
	},{
		"Name": "DarkStone",
		"Color": [12 / 255., 8 / 255., 12 / 255.],
		"Side": [12 / 255., 8 / 255., 12 / 255.],
		"Item": [12 / 255., 8 / 255., 12 / 255.],
		"Drops": "DarkStone",
		"Hardness": 2
	},{
		"Name": "Snow",
		"Color": [253 / 255., 252 / 255., 254 / 255.],
		"Side": [133 / 255., 101 / 255.,  64 / 255.],
		"Item": [255 / 255., 255 / 255., 255 / 255.],
		"Drops": "Snow",
		"Hardness": 1
	},{
		"Name": "Granite",
		"Color": [111 / 255., 106 / 255., 85 / 255.],
		"Side": [111 / 255., 106 / 255., 85 / 255.],
		"Item": [128 / 255., 128 / 255.,  128 / 255.],
		"Drops": "Granite",
		"Hardness": 4,
		"Unbreakable": True
	},{
		"Name": "Peat",
		"Color": [109 / 255. / 7, 108 / 255. / 7,  20 / 255. / 7],
		"Side": [134 / 255. / 7, 102 / 255. / 7,  64 / 255. / 7],
		"Item": [102 / 255., 51 / 255.,  0 / 255.],
		"Drops": "Peat",
		"Hardness": 1
	}
]

pickaxe_recipes = []

for object in mapgen_objects:
	csv.append([object["Name"] + "Surface", CamelToSpaces(object["Name"])])

	objects_array.append({ "Class": "StaticItem",
		"Name": object["Name"] + "Surface" + static_item,
		"Image": "T_" + object["Name"],
		
		"ItemLogic": building_brush_slot_logic,
		"Mesh": "/Game/Models/piece",
		"Materials" : ["/Game/Materials/" + object["Drops"]],
		"Color": object["Item"],
		"LogicJson":
		{
			"StaticBlock": object["Name"] + "Surface" + static_surface
		},
		"StackSize": 999,
		"LabelParts": [[object["Name"]+ "Surface", "mapgen_core"]],
	})
	objects_array.append({ "Class": "TesselatorMarching",
		"Name": object["Name"] + "Surface" + tesselator,
		"Material": "/Game/Materials/Triplanar/" + object["Name"] + "Material"
	})
	objects_array.append({
		"Class": "StaticBlock",
		"Name": object["Name"] + "Surface" + static_surface,
		"Tesselator": object["Name"] + "Surface" + tesselator,
		"Item" : object["Name"] + "Surface" + static_item,
		"ColorSide": object["Side"],
		"ColorTop": object["Color"],
		"Minable": {"Minable": False} if "Unbreakable" in object else {"Result": object["Drops"] + "Surface" + static_item},
		"Surface": True
	})
	
data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/mapgen_core.json", data);
write_file("Loc/source/mapgen_core.json", csv)