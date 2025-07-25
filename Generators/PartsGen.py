from MachinesList import *
from PartsList import *
from Common import *
import copy

objects_array = []

images = []
recipes_cutter = []
recipes_hammer = []
recipes_macerator = []
recipes_hand = []
recipes_assembler = []
recipes_furnace = []
recipes_press = []
recipes_smelt = []
recipes_gasfurn = []
recipes_disassembler = []

cvs = []

def generate_part(name, material_dict):
	part = named_part(name)
	material = material_dict["Name"]
	tier = material_dict["Tier"] if "Tier" in material_dict else 0
	cvs.append([material + part["Name"], CamelToSpaces(material) + " " + part["Label"]])
	item = { "Class": "StaticItem",
		"Name": material + part["Name"],
		"Label": [material + part["Name"], "parts"],
		"Image": "T_" + material + part["Name"],
		"StackSize": part["StackSize"],
		"Materials" : [
			"/Game/Materials/" + material
		],
		"Mesh": "/Game/Models/"+name+"Crate",
		"Tier": tier,
		"Category": "Parts",
	}
	if "Mesh" in part:
		item["Mesh"] = part["Mesh"]

	if "ItemLogic" in part:
		item["ItemLogic"] = part["ItemLogic"]
		
	if "Materials" in part:
		dict = copy.deepcopy(part["Materials"])
		for i in range(0, len(dict)):
			if dict[i].find("%Material%") != -1:
				dict[i] = dict[i].replace("%Material%", material)		
		item["Materials"] = dict
	
	objects_array.append(item)

	item["DescriptionParts"] = [["Part","common"]]
	
	images.append({ "NewName": "T_" + material + part["Name"],
		"Base": "T_" + part["Name"],
		"MulMask": "T_Material" + material,
		"AddMask": "T_" + part["Name"] + additive_ico,
	})

for material in materials:
	material_tier = 0 if "Tier" not in material else material["Tier"]
	m_name = material["Name"]

	if "Items" not in material:
		print("Material "+ m_name +" has no Items")
		continue

	if "SolarCell" in material["Items"] and material_tier > 1:
		generate_part("SolarCell", material)

		if material_tier == 2:
			recipes_hand.append({
				"Name": m_name + "SolarCell",
				"Input": items([
					["Silicon", 15],
					["CopperWire", 5]
				]),
				"Output": one_item(m_name + "SolarCell"),
				"Ticks" : 80,
				"Tier": material_tier
			})
		elif material_tier == 3:
			recipes_hand.append({
				"Name": m_name + "SolarCell",
				"Input": items([
					["SiliconWafer", 5],
					["CopperWire", 5]
				]),
				"Output": one_item(m_name + "SolarCell"),
				"Ticks" : 80,
				"Tier": material_tier
			})
		else:
			recipes_hand.append({
				"Name": m_name + "SolarCell",
				"Input": items([
					[tier_material[material_tier]+"SolarCell", 4],
					["CopperWire", 2],
					["Processor" if material_tier > 3 else {}]
				]),
				"Output": one_item(m_name + "SolarCell"),
				"Ticks" : 80,
				"Tier": material_tier
			})
	
	if "Foil" in material["Items"]:
		generate_part("Foil", material)
		recipes_assembler.append({
			"Name": m_name + "Foil",
			"Input": one_item(m_name + "Plate"),
			"Output": one_item(m_name + "Foil", 3),
			"Ticks" : 80,
			"Tier": material_tier,
			"Productivity": 50,
		})
		recipes_hand.append({
			"Name":m_name+"Foil",
			"Input": one_item(m_name+"Plate", 1),
			"Output": one_item(m_name+"Foil", 1),
			"Ticks" : 20,
			"Tier": material_tier,
		})

	if "Parts" in material["Items"]:
		generate_part("Parts", material)
		recipes_hand.append({
			"Name": m_name + "Parts",
			"Input": one_item(m_name + "Plate"),
			"Output": { "Items": [
				{
					"Name": m_name + "Parts",
					"Count": 1
				},
				{
					"Name": m_name + "Parts",
					"Count": 1,
					"Bonus": True
				}
			]},
			"Ticks" : 80,
			"Tier": material_tier,
			"Productivity": 50,
		})

	if "Sheet" in material["Items"]:
		generate_part("Sheet", material)

	if "Wire" in material["Items"]:
		generate_part("Wire", material)
		recipes_assembler.append({
			"Name":m_name+"Wire2",
			"Input": one_item(m_name+"Plate", 1),
			"Output": one_item(m_name+"Wire", 2),
			"Ticks" : 40,
		})
		recipes_hand.append({
			"Name":m_name+"Wire",
			"Input": one_item(m_name+"Plate", 1),
			"Output": one_item(m_name+"Wire", 1),
			"Ticks" : 20,
		})

	# abstract
	if "Abstract" in material["Items"]:
		cvs.append([m_name, material["Label"]])
		item = { "Class": "StaticItem",
			"Name": m_name,
			"Image": "T_" + m_name,
			
			"StackSize": 1,
			"Label": [m_name, "parts"],
			"Type": "Abstract"
		}

		if "Tier" in material:
			item["Tier"] = material["Tier"]
		
		if "Unit" in material:
			item["Unit"] = material["Unit"]
			
		if "UnitMul" in material:
			item["UnitMul"] = material["UnitMul"]
			
		if "Category" in material:
			item["Category"] = material["Category"]
			
		if "Description" in material:
			item["DescriptionParts"] = material["Description"]
			
		objects_array.append(item)
	
	# exact
	if "Exact" in material["Items"]:
		cvs.append([material["Name"], material["Label"]])
		item = { "Class": "StaticItem",
			"Name": material["Name"],
			"Image": "T_" + material["Name"],
			"StackSize": 64 if material["Name"] != "Signal" else 214748364,
			"Label": [material["Name"], "parts"],
		}

		if "Tier" in material:
			item["Tier"] = material["Tier"]

		if "CustomData" in material:
			item["CustomData"] = material["CustomData"]
				
		if "Category" in material:
			item["Category"] = material["Category"]
			
		if "Description" in material:
			item["DescriptionParts"] = material["Description"]
			
		if "Unit" in material:
			item["Unit"] = material["Unit"]
			
		if "StackSize" in material:
			item["StackSize"] = material["StackSize"]
			
		if "Mesh" in material:
			item["Mesh"] = material["Mesh"]
			item["Materials"] =	[
				"/Game/Materials/" + material["Name"]
			]

		if "Circuit" in material:
			item["DescriptionParts"] = [["circuit", "common"], ["computation", "common", pow(10, material_tier - 1)*30*20]]

		if "MaxCharge" in material:
			item["MaxCharge"] = material["MaxCharge"]
			item["DescriptionParts"] = [["battery", "common", material["MaxCharge"]]]
			
		if "Materials" in material:
			item["Materials"] = material["Materials"]
		
		if "Burnable" in material:
			recipes_furnace.append({
				"Name": material["Name"],
				"Input":{
					"Items":[
						{
							"Name": material["Name"],
							"Count": 1
						}
					]
				},
				"Output":{
					"Items":[
					],
					
				},
				"Ticks" : fuel_burn_time(material, furnace_output()),
			})
			item["DescriptionParts"] = [["burnable", "common", fuel_value(material)]]
			item["Tags"] = fuel_tags()
			
		objects_array.append(item)

	# plate
	if "Plate" in material["Items"]:
		cvs.append([material["Name"] + "Plate", material["Label"] + " Plate"])
		item = { "Class": "StaticItem",
			"Name": material["Name"] + "Plate",
			"Image": "T_" + material["Name"] + "Plate",
			"StackSize": 128,
			"Mesh": "/Game/Models/Ingot",
			"Materials": [
				"",
				"/Game/Materials/" + material["Name"]
			],			
			"Label": [material["Name"] + "Plate", "parts"],
			"Category": "Plate",
		}

		if "Tier" in material:
			item["Tier"] = material["Tier"]
		
		if "Category" in material:
			item["Category"] = material["Category"]
			
		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "Plate",
			"Base": "T_" + "Plate",
			"MulMask": "T_Material" + material["Name"],
			"AddMask": "T_" + "Plate" + additive_ico,
		})
			
		if "Dust" in material["Items"]:
			if "Smelting" in material and "Smelter" in material["Smelting"]:
				recipes_smelt.append({
					"Name": material["Name"] + "Plate",
					"Input": one_item(material["Name"] + "Dust"),
					"Output": one_item(material["Name"] + "Plate"),
					"Ticks" : 100,
				})
		
			recipes_macerator.append({
				"Name": material["Name"] + "Plate",
				"Input":{
					"Items":[
						{
							"Name": material["Name"] + "Plate",
							"Count": 1
						},
					]
				},
				"ResourceInput":{
					"Name": "Kinetic",
					"Count": 15
				},
				"Output":{
					"Items":[
						{
							"Name": material["Name"] + "Dust",
							"Count": 1
						}
					]
				},
				"Ticks" : 80,
				"Tier": material_tier,
			})
			
	# block
	if "Block" in material["Items"]:
		cvs.append([material["Name"] + "Block", material["Label"] + " Block"])
		item = { "Class": "StaticItem",
			"Name": material["Name"] + "Block",
			"Image": "T_" + material["Name"] + "Block",
			"StackSize": 999,
			"Materials" : [
				"/Game/Materials/" + material["Name"]
			],			
			"Label": [material["Name"] + "Block", "parts"],
			"Category": "Block",
			"ItemLogic": building_cube_logic,
			"Block": material["Name"] + "Block",
		}
		
		if "Tier" in material:
			item["Tier"] = material["Tier"]

		if "Category" in material:
			item["Category"] = material["Category"]
			
		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "Block",
				"Base": "T_" + "Block",
				"MulMask": "T_Material" + material["Name"],
				"AddMask": "T_" + "Block" + additive_ico,
			})
		objects_array.append({ "Class": tesselator_cube,
			"Name": material["Name"] + "Block" + tesselator,
			"Material" : "/Game/Materials/" + material["Name"]
		})
		objects_array.append({ "Class": "StaticBlock",
			"Name": material["Name"] + "Block" + static_block,
			"Item" : material["Name"] + "Block",
			"Tesselator": material["Name"] + "Block" + tesselator,
		})
	
	# fluid
	if "Fluid" in material["Items"]:
		cvs.append([material["Name"], material["Label"]])
		item = { "Class": "StaticItem",
			"Name": material["Name"] + "",
			"Image": "T_" + material["Name"] + "",
			
			"StackSize": 1000,
			"Category": "",
			"Label": [material["Name"], "parts"],
			
			"UnitMul": 1.0 / 1000.0,
			
			"Category": "Fluid",
			"DescriptionParts":[["Fluid","common"],["ByPipes","common"]],
			"Type": "Fluid"
		}

		if "Tier" in material:
			item["Tier"] = material["Tier"]
		
		if "Category" in material:
			item["Category"] = material["Category"]
		
		#if item["MaterialKey"] + " " + item["Key"] in explicites:
		#	item["ExplicitKey"] = ex_cvs[explicites.index(item["MaterialKey"] + " " + item["Key"])][0]
		
		if "Burnable" in material:
			item["DescriptionParts"].append(["burnable", "common", fuel_value(material)])
			item["Tags"] = fuel_tags()

		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "",
			"Base": "T_" + "",
			"MulMask": "T_Material" + material["Name"],
			"AddMask": "T_" + "" + additive_ico,
		})
		
		if "UnitMul" in material:
			item["UnitMul"] = material["UnitMul"]
			
		if "Color" in material:
			item["Color"] = material["Color"]
		
		if "Burnable" in material:
			duration, count = fluid_furnace_pair(material)
			recipes_gasfurn.append({
				"Input":{
					"Items":[
						{
							"Name": material["Name"] + "",
							"Count": count
						}
					]
				},
				"Output":{
					"Items":[
					],
					
				},
				"Ticks" : duration,
				"Name": material["Name"] + "",
			})
	
	# gas
	if "Gas" in material["Items"]:
		cvs.append([material["Name"], material["Label"]])
		item = { "Class": "StaticItem",
			"Name": material["Name"] + "",
			"Image": "T_" + material["Name"] + "",
			
			"StackSize": 1000,
			"Category": "",
			"Label": [material["Name"], "parts"],
			
			"UnitMul": 1.0 / 1000.0,
			
			"Category": "Fluid",
			"DescriptionParts":[["Gas","common"],["ByPipes","common"]],
			"Type": "Fluid"
		}

		if "Tier" in material:
			item["Tier"] = material["Tier"]
		
		if "Category" in material:
			item["Category"] = material["Category"]

		if "UnitMul" in material:
			item["UnitMul"] = material["UnitMul"]
			
		if "Color" in material:
			item["Color"] = material["Color"]

		if "Burnable" in material:
			item["DescriptionParts"].append(["burnable", "common", fuel_value(material)])
			item["Tags"] = fuel_tags()
		
		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "",
			"Base": "T_" + "",
			"MulMask": "T_Material" + material["Name"],
			"AddMask": "T_" + "" + additive_ico,
		})
		
		if "Burnable" in material:
			duration, count = fluid_furnace_pair(material)
			recipes_gasfurn.append({
				"Input":{
					"Items":[
						{
							"Name": material["Name"] + "",
							"Count": count
						}
					]
				},
				"Output":{
					"Items":[
					],
					
				},
				"Ticks": duration,
				"Name": material["Name"],
			})
	
	# dust
	if "Dust" in material["Items"]:
		cvs.append([material["Name"] + "Dust", material["Label"] + " Dust"])
		item = { "Class": "StaticItem",
			"Name": material["Name"] + "Dust",
			"Image": "T_" + material["Name"] + "Dust",
			
			"StackSize": 64,
			
			"Label": [material["Name"] + "Dust", "parts"],
			"Mesh": "/Game/Models/DustCrate",
			"Materials": [
				"",
				"/Game/Materials/" + material["Name"] + "Dust"
			],
			"UnitMul": 1,
			"Category": "Dust",
		}

		if "Tier" in material:
			item["Tier"] = material["Tier"]
		
		if "Category" in material:
			item["Category"] = material["Category"]

		if "Burnable" in material:
			item["DescriptionParts"].append(["burnable", "common", fuel_value(material)])
			item["Tags"] = fuel_tags()
		
		dustItem = { "NewName": "T_" + material["Name"] + "Dust",
			"Base": "T_" + "Dust",
			"MulMask": "T_Material" + material["Name"],
			"AddMask": ["T_" + "Dust" + additive_ico],
		}
		if material["Name"] == "Platinum":
			dustItem["AddMask"].append("T_" + "Shiny" + additive_ico)
		images.append(dustItem)

		if "Burnable" in material:
			recipes_furnace.append({
				"Name": material["Name"] + "Dust",
				"Input":{
					"Items":[
						{
							"Name": material["Name"] + "Dust",
							"Count": 1
						}
					]
				},
				"Output":{
					"Items":[
					],
				},
				"Ticks" : fuel_burn_time(material, furnace_output()),
			})
			item["DescriptionParts"] = [["burnable", "common", fuel_value(material)]]
			item["Tags"] = fuel_tags()

		objects_array.append(item)
			
# tools	
for tool in tools:
	cvs.append([tool["Name"], tool["Label"]])
	item_name = tool["Name"]
	item = { "Class": "StaticItem",
		"Name": item_name,
		"Image": "T_" + item_name,
		"ItemLogic": tool["ItemLogic"],
		"StackSize": 1,
		"Label": [tool["Name"], "parts"],
	}
		
	objects_array.append(item)
	
	images.append({ "NewName": "T_" + item_name,
		"Base": "T_" + tool["Name"],
		"MulMask": "T_Material" + "StainlessSteel",
		"AddMask": "T_" + tool["Name"] + additive_ico
	})
					
data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/parts.json", data);

objects_array = []

objects_array.append({	
		"Class": ico_generator,
		"Name": "Parts" + ico_generator,
		"Images": images
	})
	
data = {
	"Objects": objects_array
}

write_file("Generated/Resources/parts.json", data);

objects_array = []

objects_array.append({ "Class": r_dict,
	"Name": "CuttingMachine" + r_dict,
	"Recipes": recipes_cutter
})

objects_array.append({ "Class": r_dict,
	"Name": "AutomaticHammer" + r_dict,
	"Recipes": recipes_hammer
})

objects_array.append({ "Class": r_dict,
	"Name": "Macerator" + r_dict,
	"Recipes": recipes_macerator
})

for r in recipes_hand:
	r["Locked"] = True

objects_array.append({ "Class": r_dict,
	"Name": "Hand" + r_dict,
	"Recipes": recipes_hand,
	"UsedIn": [{
		"Item": "Hand",
	}]
})

objects_array.append({ "Class": r_dict,
	"Name": "Furnace" + r_dict,
	"Recipes": recipes_furnace
})

objects_array.append({ "Class": r_dict,
	"Name": "Smelter" + r_dict,
	"Recipes": recipes_smelt
})

objects_array.append({ "Class": r_dict,
	"Name": assembler_r_dict,
	"Recipes": recipes_assembler,
})

objects_array.append({ "Class": r_dict,
	"Name": "FluidFurnace" + r_dict,
	"Recipes": recipes_gasfurn,
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/parts.json", data);

write_file("Loc/source/parts.json", cvs)