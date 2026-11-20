from Common import *
from MapgenList import mapgen_objects, triplanar_material
from TransitionColors import transition_colors

objects_array = []

pickaxe_recipes = []

for object in mapgen_objects:
	objects_array.append({ "Class": "StaticItem",
		"Name": object["Name"] + "Surface",
		"Image": "T_" + object["Name"],
		"ItemLogic": building_brush_slot_logic,
		"Meshes": ["/Game/Models/piece"],
		"ConveyorStack": 1,
		"Materials" : ["/Game/Materials/" + object["Drops"]],
		"Block": object["Name"] + "Surface",
		"StackSize": 999,
		"Label": [object["Name"]+ "Surface", "mapgen_core"],
		"Category": "Terrain",
	})

for object in mapgen_objects:
	objects_array.append({ "Class": "TesselatorMarching",
		"Name": object["Name"] + "Surface" + tesselator,
		"Material": triplanar_material(object["Name"])
	})

for object in mapgen_objects:
	mine_drop = object["MineResult"] if "MineResult" in object else object["Drops"] + "Surface"
	staticBlock = {
		"Class": "StaticBlock",
		"Name": object["Name"] + "Surface" + static_surface,
		"Tesselator": object["Name"] + "Surface" + tesselator,
		"Item" : object["Name"] + "Surface",
		"ColorTop": transition_colors[object["Name"]][0],
		"ColorSide": transition_colors[object["Name"]][1],
		"Minable": {"Minable": False} if "Unbreakable" in object else {"Result": mine_drop},
		"Surface": True
	}
	if "BreakEffect" in object:
		staticBlock["BreakEffect"] = object["BreakEffect"]
	objects_array.append(staticBlock)

objects_array.append({ "Class": "ItemGroup",
	"Name": "RockOrSoil",
	"Label": ["RockOrSoil", "mapgen_core"],
	"Members": ["StoneSurface", "BasaltSurface", "RedStoneSurface", "DarkStoneSurface", "GravelSurface", "SandSurface", "DirtSurface"],
	"StackSize": 999,
})

objects_array.append({ "Class": "ItemGroup",
	"Name": "RockOrGravel",
	"Label": ["RockOrGravel", "mapgen_core"],
	"Members": ["StoneSurface", "BasaltSurface", "RedStoneSurface", "DarkStoneSurface", "GravelSurface"],
	"StackSize": 999,
})

objects_array.append({ "Class": "ItemGroup",
	"Name": "AnyStone",
	"Label": ["AnyStone", "mapgen_core"],
	"Members": ["StoneSurface", "BasaltSurface", "RedStoneSurface", "DarkStoneSurface"],
	"StackSize": 999,
})

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/mapgen_core.json", data)