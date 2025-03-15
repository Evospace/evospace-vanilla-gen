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

recipes_gasturb = []

cvs = []

def generate_part(name, material_dict):
	part = named_part(name)
	material = material_dict["Name"]
	tier = material_dict["Tier"] if "Tier" in material_dict else 0
	cvs.append([material + part["Name"], CamelToSpaces(material) + " " + part["Label"]])
	item = { "Class": "StaticItem",
		"Name": material + part["Name"],
		"LabelParts": [[material + part["Name"], "parts"]],
		"Image": "T_" + material + part["Name"],
		"StackSize": part["StackSize"],
		"LogicJson":
		{
			"StaticBlock": material + part["Name"] + static_block
		},
		"Materials" : [
			"/Game/Materials/" + material
		],
		
		"Category": "Parts",
	}
	if "ItemLogic" in part:
		item["ItemLogic"] = part["ItemLogic"]
		
	if "Mesh" in part:
		item["Mesh"] = part["Mesh"]
		
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
	
def append_gas_burning(recipe):
	gas2 = copy.deepcopy(recipe)
	gas2["Input"]["Items"].append({ "Name": "Oxygen", "Count": gas2["Input"]["Items"][0]["Count"]})
	gas2["Output"]["Items"][0]["Count"] = gas2["Output"]["Items"][0]["Count"] * 2
	gas2["Output"]["Items"] = [gas2["Output"]["Items"][0]]
	recipes_gasturb.append(gas2) 
	
	recipes_gasturb.append(recipe)

for material in materials:
	material_tier = 0 if "Tier" not in material else material["Tier"]
	m_name = material["Name"]

	if "Items" not in material:
		print("Material "+ m_name +" has no Items")
		continue

	if "SolarCell" in material["Items"]:
		generate_part("SolarCell", material)
		inp = [{
			"Name": a_wires[material_tier],
			"Count": 2
		}]
		if material_tier > 3:
			inp.append({
				"Name": tier_material[material_tier - 1] + "SolarCell",
				"Count": 2
			})
		else:
			inp.append({
			"Name": "SiliconWafer",
			"Count": 2
			})
			inp.append({
				"Name": "AluminiumPlate",
				"Count": 1
			})
		recipes_assembler.append({
			"Name": m_name + "SolarCell",
			"Input":{
				"Items": inp
			},
			"Output":{
				"Items":[
					{
						"Name": m_name + "SolarCell",
						"Count": 1
					}
				]
			},
			"Ticks" : 80,
			"Tier": material_tier
		})

	if "Parts" in material["Items"]:
		generate_part("Parts", material)
		recipes_hand.append({
			"Name": m_name + "Parts",
			"Input":{
				"Items":[
					{
						"Name": m_name + "Plate",
						"Count": 1
					},
				]
			},
			"Output":{
				"Items":[
					{
						"Name": m_name + "Parts",
						"Count": 1
					}
				]
			},
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

	if "Gearbox" in material["Items"]:
		generate_part("Gearbox", material)
		if material_tier == 1:
			recipes_hand.append({
				"Name": m_name + "Gearbox",
				"Input": items([
					[m_name + "Plate"],
					[m_name + "Parts", 3],
				], material_tier),
				"Output": one_item(m_name + "Gearbox", 1),
				"Tier": material_tier,
				"Ticks": 200
			})
		else:
			recipes_hand.append({
				"Name": m_name + "Gearbox",
				"Input": items([
					[m_name + "Plate", 3],
					[m_name + "Parts", 6],
				], material_tier),
				"Output": one_item(m_name + "Gearbox", 1),
				"Tier": material_tier,
				"Ticks": 200
			})

	# abstract
	if "Abstract" in material["Items"]:
		cvs.append([m_name, material["Label"]])
		item = { "Class": "StaticItem",
			"Name": m_name,
			"Image": "T_" + m_name,
			
			"StackSize": 1,
			"LabelParts": [[m_name, "parts"]],
			"Type": "Abstract"
		}
		
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
			
			"LabelParts": [[material["Name"], "parts"]],
		}
			
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
				"Ticks" : material["Burnable"]["BurnTime"],
			})
			item["DescriptionParts"] = [["burnable", "common"]]
										#["power_output", "common", material["Burnable"]["HeatPerTick"]*20]]
			
		objects_array.append(item)

	# plate
	if "Plate" in material["Items"]:
		cvs.append([material["Name"] + "Plate", material["Label"] + " Plate"])
		item = { "Class": "StaticItem",
			"Name": material["Name"] + "Plate",
			"Image": "T_" + material["Name"] + "Plate",
			"StackSize": 128,
			"Mesh": "/Game/Models/Ingot",
			"Materials" : [
				"/Game/Materials/" + material["Name"]
			],			
			"LabelParts": [[material["Name"] + "Plate", "parts"]],
			"Category": "Plate",
		}
		
		if "Category" in material:
			item["Category"] = material["Category"]
			
		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "Plate",
			"Base": "T_" + "Plate",
			"MulMask": "T_Material" + material["Name"],
			"AddMask": "T_" + "Plate" + additive_ico,
		})
		
		if "SmeltLevel" in material and material["SmeltLevel"] <= 0:
			recipes_smelt.append({
				"Name": material["Name"] + "Plate",
				"Input":{
					"Items":[
						{
							"Name": material["Name"] + "Dust",
							"Count": 1
						}
					],
					
				},
				"ResourceInput":{
						"Name": "Heat",
						"Count": 10,
					},
				"Output":{
					"Items":[
						{
							"Name": material["Name"] + "Plate",
							"Count": 1
						}
					]
				},
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
			"LabelParts": [[material["Name"] + "Block", "parts"]],
			"Category": "Block",
			"ItemLogic": building_cube_logic,
			"LogicJson":
			{
				"StaticBlock": material["Name"] + "Block" + static_block
			},
		}
		
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
		
		recipes_press.append({
			"Name": material["Name"] + "Block",
			"Input":{
				"Items":[
					{
						"Name": material["Name"] + "Dust",
						"Count": 4
					}
				],
				
			},
			"ResourceInput":{
					"Name": "Kinetic",
					"Count": 10,
				},
			"Output":{
				"Items":[
					{
						"Name": material["Name"] + "Block",
						"Count": 1
					}
				]
			},
			"Ticks" : 200,
		})
	
	# fluid
	if "Fluid" in material["Items"]:
		cvs.append([material["Name"], material["Label"]])
		item = { "Class": "StaticItem",
			"Name": material["Name"] + "",
			"Image": "T_" + material["Name"] + "",
			
			"StackSize": 1000,
			"Category": "",
			"LabelParts": [[material["Name"], "parts"]],
			
			"UnitMul": 1.0 / 1000.0,
			
			"Category": "Fluid",
			"DescriptionParts":[["Fluid","common"],["ByPipes","common"]],
			"Type": "Fluid"
		}
		
		if "Category" in material:
			item["Category"] = material["Category"]
		
		#if item["MaterialKey"] + " " + item["Key"] in explicites:
		#	item["ExplicitKey"] = ex_cvs[explicites.index(item["MaterialKey"] + " " + item["Key"])][0]
		
		#if "Burnable" in material:
		#	item["DescriptionParts"].append(["burnable", "common", material["Burnable"]["BurnTime"]*material["Burnable"]["HeatPerTick"]])
		#	item["DescriptionParts"].append(["power_output", "common", material["Burnable"]["HeatPerTick"]*20])

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
			recipes_gasfurn.append({
				"Input":{
					"Items":[
						{
							"Name": material["Name"] + "",
							"Count": 1000
						}
					]
				},
				"Output":{
					"Items":[
					],
					
				},
				"Ticks" : material["Burnable"]["BurnTime"],
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
			"LabelParts": [[material["Name"], "parts"]],
			
			"UnitMul": 1.0 / 1000.0,
			
			"Category": "Fluid",
			"DescriptionParts":[["Gas","common"],["ByPipes","common"]],
			"Type": "Fluid"
		}
		
		if "Category" in material:
			item["Category"] = material["Category"]
		
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
			recipes_gasfurn.append({
				"Input":{
					"Items":[
						{
							"Name": material["Name"] + "",
							"Count": 1000
						}
					]
				},
				"Output":{
					"Items":[
					],
					
				},
				"Ticks" : material["Burnable"]["BurnTime"],
				"Name": material["Name"],
			})
	
	# dust
	if "Dust" in material["Items"]:
		cvs.append([material["Name"] + "Dust", material["Label"] + " Dust"])
		item = { "Class": "StaticItem",
			"Name": material["Name"] + "Dust",
			"Image": "T_" + material["Name"] + "Dust",
			
			"StackSize": 64,
			
			"LabelParts": [[material["Name"] + "Dust", "parts"]],
			"Mesh": "/Game/Models/Dust",
			"Materials": [
				"/Game/Materials/" + material["Name"] + "Dust"
			],
			"UnitMul": 1,
			"Category": "Dust",
		}
		
		if "Category" in material:
			item["Category"] = material["Category"]
			
		objects_array.append(item)
		
		dustItem = { "NewName": "T_" + material["Name"] + "Dust",
			"Base": "T_" + "Dust",
			"MulMask": "T_Material" + material["Name"],
			"AddMask": ["T_" + "Dust" + additive_ico],
		}
		if material["Name"] == "Rhodium" or material["Name"] == "Platinum":
			dustItem["AddMask"].append("T_" + "Shiny" + additive_ico)
		images.append(dustItem)

		if "Burnable" in material:
			recipes_furnace.append({
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
				"Ticks" : material["Burnable"]["BurnTime"],
				"Name": material["Name"] + "Dust",
			})
			
# tools	
for tool in tools:
	cvs.append([tool["Name"], tool["Label"]])
	item_name = tool["Name"]
	item = { "Class": "StaticItem",
		"Name": item_name,
		"Image": "T_" + item_name,
		"ItemLogic": tool["ItemLogic"],
		"LogicJson": {
			"RecipeDictionary": tool["Name"] + r_dict,
		},
		"StackSize": 1,
		"LabelParts": [[tool["Name"], "parts"]],
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
	"Name": "Press" + r_dict,
	"Recipes": recipes_press
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
	"Recipes": recipes_gasfurn
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/parts.json", data);

write_file("Loc/source/parts.json", cvs)