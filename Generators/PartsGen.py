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
	
def append_gas_burning(recipe):
	gas2 = copy.deepcopy(recipe);
	gas2["Input"]["Items"].append({ "Name": "Oxygen", "Count": gas2["Input"]["Items"][0]["Count"]})
	gas2["Output"]["Items"][0]["Count"] = gas2["Output"]["Items"][0]["Count"] * 2
	gas2["Output"]["Items"] = [gas2["Output"]["Items"][0]]
	recipes_gasturb.append(gas2) 
	
	recipes_gasturb.append(recipe)

def append_recipe(crafter, recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]

	con_recipe = copy.deepcopy(recipe)
	crafter.append(con_recipe)

	recipe["Ticks"] = 20
	recipe.pop("ResourceInput", None)
	recipes_hand.append(recipe)

def append_recipe_diss(crafter, recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]

	diss_recipe = copy.deepcopy(recipe)
	temp = diss_recipe["Input"]
	diss_recipe["Input"] = diss_recipe["Output"] 
	diss_recipe["Output"] = temp
	diss_recipe["Ticks"] *= 2
	recipes_disassembler.append(diss_recipe)

	con_recipe = copy.deepcopy(recipe)
	crafter.append(con_recipe)

	recipe["Ticks"] = 20
	recipe.pop("ResourceInput", None)
	recipes_hand.append(recipe)

# tiered parts
for part in parts:
	for tier in tiers_numlist:
		material = tier_material[tier]
		material_tier = tier
		if part["StartTier"] <= tier and part["EndTier"] >= tier:
			cvs.append([material + part["Name"], CamelToSpaces(material) + " " + part["Label"]])
			level = tier - part["StartTier"]
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
						dict[i] = dict[i].replace("%Material%", tier_material[tier])		
				item["Materials"] = dict
			
			objects_array.append(item)

			item["DescriptionParts"] = [["Part","common"]]
			
			images.append({ "NewName": "T_" + material + part["Name"],
				"Base": "T_" + part["Name"],
				"MulMask": "T_Material" + material,
				"AddMask": "T_" + part["Name"] + additive_ico,
			})
			
			if part["Name"] == "Casing":
				recipes_hand.append({
					"Name": material + "Casing",
					"Input":{
						"Items":[
							{
								"Name": material + "Plate",
								"Count": 3
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": material + "Casing",
								"Count": 1
							}
						]
					},
					"Ticks" : 40
				})
				objects_array.append({ "Class": tesselator_cube,
					"Name": material + "Casing" + tesselator,
					"Material" : "/Game/Materials/" + material + "Casing"
				})
				objects_array.append({ "Class": "StaticBlock",
					"Name": material + "Casing" + static_block,
					"Item" : material + "Casing",
					"Tesselator": material + "Casing" + tesselator,
				})
			
			if part["Name"] == "Gearbox":
				items = []
				
				if tier < 7:
					plate_count = 1 if tier < 3 else 4
					items.append({
						"Name": material + "Plate",
						"Count": plate_count
					})
				else:
					items.append({
						"Name": "UltimateFrame",
						"Count": 1
					})
				
				if tier <= 2:
					parts_count = 2 + (4 if tier == 2 else 0)
					items.append({
						"Name": material + "Parts",
						"Count": parts_count
					})
				
				if tier >= 2:
					index = tier - 1 if tier < 3 else 2
					gearbox_count = 1 if tier < 3 else (1 + (tier - 2))
					items.append({
						"Name": tier_material[index] + "Gearbox",
						"Count": gearbox_count
					})
				
				recipe = {
					"Name": material + "Gearbox",
					"Input": { "Items": items },
					"Output": {
						"Items": [{
							"Name": material + "Gearbox",
							"Count": 1
						}]
					},
					"Ticks": 200 * 2 ** material_tier
				}
				
				append_recipe_diss(recipes_assembler, recipe)

			if part["Name"] == "SolarCell":
				inp = [{
					"Name": wires[tier],
					"Count": 2
				}]
				if tier > 3:
					inp.append({
						"Name": tier_material[tier - 1] + "SolarCell",
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
				append_recipe(recipes_assembler, {
					"Name": material + "SolarCell",
					"Input":{
						"Items": inp
					},
					"Output":{
						"Items":[
							{
								"Name": material + "SolarCell",
								"Count": 1
							}
						]
					},
					"Ticks" : 80,
					"Tier": level
				})

			if part["Name"] == "Plate":
				append_recipe(recipes_hammer, {
					"Name": material + "Plate",
					"Input":{
						"Items":[
							{
								"Name": material + ("Ingot" if material != "Stone" else "Surface"),
								"Count": 1
							},
						]
					},
					"Output":{
						"Items":[
							{
								"Name": material + "Plate",
								"Count": 1
							}
						]
					},
					"Ticks" : 80,
					"Tier": material_tier
				})
				
			if part["Name"] == "Parts":
				append_recipe(recipes_cutter, {
					"Name": material + "Parts",
					"Input":{
						"Items":[
							{
								"Name": material + "Plate",
								"Count": 1
							},
						]
					},
					"Output":{
						"Items":[
							{
								"Name": material + "Parts",
								"Count": 1
							}
						]
					},
					"Ticks" : 80,
					"Productivity": 50,
				})

# ingots, dusts, fluids, gems, blocks
for material in materials:
	material_tier = 0 if "Tier" not in material else material["Tier"]
	# abstract
	if "IsAbstract" in material:
		cvs.append([material["Name"], material["Label"]])
		item = { "Class": "StaticItem",
			"Name": material["Name"],
			"Image": "T_" + material["Name"],
			
			"StackSize": 1,
			"LabelParts": [[material["Name"], "parts"]],
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
	if "IsExact" in material:
		cvs.append([material["Name"], material["Label"]])
		item = { "Class": "StaticItem",
			"Name": material["Name"],
			"Image": "T_" + material["Name"],
			
			"StackSize": 64 if material["Name"] != "Signal" else 214748364,
			
			"LabelParts": [[material["Name"], "parts"]],
		}
			
		if "Craftable" in material:
			item["Craftable"] = False
			
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

	# ingot
	if "IsIngot" in material:
		cvs.append([material["Name"] + "Ingot", material["Label"] + " Ingot"])
		item = { "Class": "StaticItem",
			"Name": material["Name"] + "Ingot",
			"Image": "T_" + material["Name"] + "Ingot",
			"StackSize": 128,
			"Mesh": "/Game/Models/Ingot",
			"Materials" : [
				"/Game/Materials/" + material["Name"]
			],			
			"LabelParts": [[material["Name"] + "Ingot", "parts"]],
			"Category": "Ingot",
		}
		
		if "Category" in material:
			item["Category"] = material["Category"]
			
		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "Ingot",
			"Base": "T_" + "Ingot",
			"MulMask": "T_Material" + material["Name"],
			"AddMask": "T_" + "Ingot" + additive_ico,
		})
		
		if "SmeltLevel" in material and material["SmeltLevel"] <= 0:
			recipes_smelt.append({
				"Name": material["Name"] + "Ingot",
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
							"Name": material["Name"] + "Ingot",
							"Count": 1
						}
					]
				},
				"Ticks" : 100,
			})
			
		recipes_macerator.append({
			"Name": material["Name"] + "Ingot",
			"Input":{
				"Items":[
					{
						"Name": material["Name"] + "Ingot",
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
			
	if "IsBlock" in material:
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
	if "IsFluid" in material:
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
	if "IsGas" in material:
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
				"Name": material["Name"],
			})
	
	# dust
	if "IsDust" in material:
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