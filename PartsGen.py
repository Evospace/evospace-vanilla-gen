from MachinesList import *
from PartsList import *
from Common import *
import copy

objects_array = []

researches = []

images = []
recipes_cutter = []
recipes_hammer = []
recipes_macerator = []
recipes_hand = []
recipes_assembler = []
recipes_furnace = []
recipes_press = []
recipes_wrench = []
recipes_smelt = []
recipes_liq_dump = []
recipes_gas_dump = []
recipes_gasfurn = []

recipes_gasturb = []

cvs = []
	
def append_gas_burning(recipe):
	gas2 = copy.deepcopy(recipe);
	gas2["Input"]["Items"].append({ "Name": "Oxygen", "Count": gas2["Input"]["Items"][0]["Count"]})
	gas2["Output"]["Items"][0]["Count"] = gas2["Output"]["Items"][0]["Count"] * 2
	gas2["Output"]["Items"] = [gas2["Output"]["Items"][0]]
	recipes_gasturb.append(gas2) 
	
	recipes_gasturb.append(recipe)

# tiered parts
for part in parts:
	for tier in tiers_numlist:
		material = tier_material[tier]
		if part["StartTier"] <= tier and part["EndTier"] >= tier:
			cvs.append([material + part["Name"], CamelToSpaces(material) + " " + part["Label"]])
			level = tier - part["StartTier"]
			item = { "Class": static_item,
				"Name": material + part["Name"],
				"LabelParts": [[material + part["Name"], "parts"]],
				"Image": "T_" + material + part["Name"],
				"MaxCount": part["Stack"],
				"LogicJson":
				{
					"StaticBlock": material + part["Name"]
				},
				"Tag": "Misc",
				"Materials" : [
					"Materials/" + material
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
					if dict[i].find("%Material%") is not -1:
						dict[i] = dict[i].replace("%Material%", tier_material[tier])		
				item["Materials"] = dict
			
			if "Tag" in part:
				item["Tag"] = part["Tag"]
			
			objects_array.append(item)
			
			images.append({ "NewName": "T_" + material + part["Name"],
				"Base": "T_" + part["Name"],
				"MulMask": "T_" + material,
				"AddMask": "T_" + part["Name"] + additive_ico,
			})
			
			
			if "Volume" in part:
				recipes_macerator.append({
					"Name": material + part["Name"],
					"Input":{
						"Items":[
							{
								"Name": material + part["Name"],
								"Count": 1
							},
						]
					},
					"ResourceInput":{
						"Name": "Kinetic",
						"Count": 10  * 1.5**level
					},
					"Output":{
						"Items":[
							{
								"Name": material + "Dust",
								"Count": part["Volume"]
							}
						]
					},
					"Ticks" : 80 * part["Volume"]  * 1.5**level,
				})
			recipes_wrench.append(simple_in_out_recipe(material + part["Name"]))
			
			if part["Name"] == "Casing" and part["StartTier"] <= tier and part["EndTier"] >= tier:
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
					"Material" : "Materials/" + material + "Casing"
				})
				objects_array.append({ "Class": static_block,
					"Name": material + "Casing",
					"Item" : material + "Casing",
					"Tesselator": material + "Casing" + tesselator,
				})
			
			if part["Name"] == "Plate":
				recipes_hammer.append({
					"Name": material + "Plate",
					"Input":{
						"Items":[
							{
								"Name": material + ("Ingot" if material is not "Stone" else "Surface"),
								"Count": 1
							},
						]
					},
					"ResourceInput":{
						"Name": "Kinetic",
						"Count": 10 * 1.5**level
					},
					"Output":{
						"Items":[
							{
								"Name": material + "Plate",
								"Count": 1
							}
						]
					},
					"Ticks" : 80 * 1.5**level,
				})
				recipes_hand.append({
					"Name": material + "Plate",
					"Input":{
						"Items":[
							{
								"Name": material + ("Ingot" if material is not "Stone" else "Surface"),
								"Count": 1
							}
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
					"Ticks" : 20,
				})
				
			if part["Name"] == "Parts":
				recipes_hand.append({ # parts recipe
					"Name": material + "Parts",
					"Input":{
						"Items":[
							{
								"Name": material + "Plate",
								"Count": 1
							}
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
					"Ticks" : 20,
				})
				recipes_cutter.append({
					"Name": material + "Parts",
					"Input":{
						"Items":[
							{
								"Name": material + "Plate",
								"Count": 1
							},
						]
					},
					"ResourceInput":{
						"Name": "Kinetic",
						"Count": 10 * 1.5**level
					},
					"Output":{
						"Items":[
							{
								"Name": material + "Parts",
								"Count": 1
							}
						]
					},
					"Ticks" : 80 * 1.5**level,
				})

# ingots, dusts, fluids, gems, blocks
for material in materials:

	# abstract
	if "IsAbstract" in material:
		cvs.append([material["Name"], material["Label"]])
		item = { "Class": static_item,
			"Name": material["Name"],
			"Image": "T_" + material["Name"],
			
			"MaxCount": 1,
			"Tag": "Misc",
			"LabelParts": [[material["Name"], "parts"]],
		}
		
		if "Unit" in material:
			item["Unit"] = material["Unit"]
			
		if "UnitMul" in material:
			item["UnitMul"] = material["UnitMul"]
			
		if "Category" in material:
			item["Category"] = material["Category"]
			
		if "Tag" in material:
			item["Tag"] = material["Tag"]
			
		if "Description" in material:
			item["DescriptionParts"] = material["Description"]
			
		objects_array.append(item)
	
	# exact
	if "IsExact" in material:
		cvs.append([material["Name"], material["Label"]])
		item = { "Class": static_item,
			"Name": material["Name"],
			"Image": "T_" + material["Name"],
			
			"MaxCount": 32 if material["Name"] != "Signal" else 214748364,
			
			"LabelParts": [[material["Name"], "parts"]],
			"Tag": "Misc",
		}
			
		if "Craftable" in material:
			item["Craftable"] = False
			
		if "Category" in material:
			item["Category"] = material["Category"]
			
		if "Description" in material:
			item["DescriptionParts"] = material["Description"]
			
		if "Tag" in material:
			item["Tag"] = material["Tag"]
			
		if "Unit" in material:
			item["Unit"] = material["Unit"]
			
		if "Stack" in material:
			item["MaxCount"] = material["Stack"]
			
		if "Mesh" in material:
			item["Mesh"] = material["Mesh"]
			item["Materials"] =	[
				"Materials/" + material["Name"]
			]
			
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
						#{
						#	"Name": "AshDust",
						#	"Count": material["Burnable"]["TotalAsh"],
						#}
					],
					
				},
				"ResourceOutput":{
						"Name": "Heat",
						"Count": material["Burnable"]["HeatPerTick"],
					},
				"Ticks" : material["Burnable"]["BurnTime"],
			})
			item["DescriptionParts"] = [["burnable", "common", material["Burnable"]["BurnTime"]*material["Burnable"]["HeatPerTick"]],
										["power_output", "common", material["Burnable"]["HeatPerTick"]*20]]
			
		objects_array.append(item)

	# ingot
	if "IsIngot" in material:
		cvs.append([material["Name"] + "Ingot", material["Label"] + " Ingot"])
		item = { "Class": static_item,
			"Name": material["Name"] + "Ingot",
			"Image": "T_" + material["Name"] + "Ingot",
			"MaxCount": 32,
			"Mesh": "Models/Ingot",
			"Materials" : [
				"Materials/" + material["Name"]
			],			
			"LabelParts": [[material["Name"] + "Ingot", "parts"]],
			"Tag": "Misc",
			"Category": "Ingot",
		}
		
		if "Category" in material:
			item["Category"] = material["Category"]
			
		if "Tag" in material:
			item["Tag"] = material["Tag"]
			
		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "Ingot",
			"Base": "T_" + "Ingot",
			"MulMask": "T_" + material["Name"],
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
				"Ticks" : 200,
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
			"Ticks" : 120,
		})
			
	if "IsBlock" in material:
		cvs.append([material["Name"] + "Block", material["Label"] + " Block"])
		item = { "Class": static_item,
			"Name": material["Name"] + "Block",
			"Image": "T_" + material["Name"] + "Block",
			"MaxCount": 999,
			#"Mesh": "Models/Ingot",
			"Materials" : [
				"Materials/" + material["Name"]
			],			
			"LabelParts": [[material["Name"] + "Block", "parts"]],
			"Tag": "Decoration",
			"Category": "Block",
			"ItemLogic": building_cube_logic,
			"LogicJson":
			{
				"StaticBlock": material["Name"] + "Block"
			},
		}
		
		if "Category" in material:
			item["Category"] = material["Category"]
			
		if "Tag" in material:
			item["Tag"] = material["Tag"]
			
		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "Block",
				"Base": "T_" + "Block",
				"MulMask": "T_" + material["Name"],
				"AddMask": "T_" + "Block" + additive_ico,
			})
		objects_array.append({ "Class": tesselator_cube,
			"Name": material["Name"] + "Block" + tesselator,
			"Material" : "Materials/" + material["Name"]
		})
		objects_array.append({ "Class": static_block,
			"Name": material["Name"] + "Block",
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
		
		recipes_wrench.append({
			"Name": material["Name"] + "Block" + "Wrenching",
			"Ticks" : 20,
			"Input":{
				"Items":[
					{
						"Name": material["Name"] + "Block",
						"Count": 1
					}
				]
			},
			"Output":{
				"Items":[
					{
						"Name": material["Name"] + "Block",
						"Count": 1
					}
				]
			}
		})
	
	# fluid
	if "IsFluid" in material:
		cvs.append([material["Name"], material["Label"]])
		item = { "Class": static_item,
			"Name": material["Name"] + "",
			"Image": "T_" + material["Name"] + "",
			
			"MaxCount": 1,
			"Category": "",
			"Tag": "Misc",
			"LabelParts": [[material["Name"], "parts"]],
			
			"UnitMul": 1.0 / 1000.0,
			
			"Category": "Fluid",
			"DescriptionParts":[["Fluid","common"],["ByPipes","common"]],
			"Solid": False,
		}
		
		if "Category" in material:
			item["Category"] = material["Category"]
			
		if "Tag" in material:
			item["Tag"] = material["Tag"]
		
		#if item["MaterialKey"] + " " + item["Key"] in explicites:
		#	item["ExplicitKey"] = ex_cvs[explicites.index(item["MaterialKey"] + " " + item["Key"])][0]
		
		if "Burnable" in material:
			item["DescriptionParts"].append(["burnable", "common", material["Burnable"]["BurnTime"]*material["Burnable"]["HeatPerTick"]])
			item["DescriptionParts"].append(["power_output", "common", material["Burnable"]["HeatPerTick"]*20])
		
		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "",
			"Base": "T_" + "",
			"MulMask": "T_" + material["Name"],
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
				"ResourceOutput":{
						"Name": "Heat",
						"Count": material["Burnable"]["HeatPerTick"],
					},
				"Ticks" : material["Burnable"]["BurnTime"],
				"Name": material["Name"] + "",
			})
		
		recipes_liq_dump.append({
			"Name": material["Name"] + "Dumping",
			"Input":{
				"Items":[
					{
						"Name": material["Name"] + "",
						"Count": 1000 if material["Name"] != "Steam" else 10000
					}
				]
			},
			"Output":{
				"Items":
				[
				]
			},
			"Ticks" : 200,
		})
	
	# gas
	if "IsGas" in material:
		cvs.append([material["Name"], material["Label"]])
		item = { "Class": static_item,
			"Name": material["Name"] + "",
			"Image": "T_" + material["Name"] + "",
			
			"MaxCount": 1,
			"Category": "",
			"Tag": "Misc",
			"LabelParts": [[material["Name"], "parts"]],
			
			"UnitMul": 1.0 / 1000.0,
			
			"Category": "Fluid",
			"DescriptionParts":[["Gas","common"],["ByPipes","common"]],
			"Solid": False,
		}
		
		if "Category" in material:
			item["Category"] = material["Category"]
			
		if "Tag" in material:
			item["Tag"] = material["Tag"]
		
		#if item["MaterialKey"] + " " + item["Key"] in explicites:
		#	item["ExplicitKey"] = ex_cvs[explicites.index(item["MaterialKey"] + " " + item["Key"])][0]
		
		if "Burnable" in material:
			item["DescriptionParts"].append(["burnable", "common", material["Burnable"]["BurnTime"]*material["Burnable"]["HeatPerTick"]])
			item["DescriptionParts"].append(["power_output", "common", material["Burnable"]["HeatPerTick"]*20])
		
		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "",
			"Base": "T_" + "",
			"MulMask": "T_" + material["Name"],
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
				"ResourceOutput":{
						"Name": "Heat",
						"Count": material["Burnable"]["HeatPerTick"],
					},
				"Ticks" : material["Burnable"]["BurnTime"],
				"Name": material["Name"],
			})
		
		recipes_gas_dump.append({
			"Name": material["Name"],
			"Input":{
				"Items":[
					{
						"Name": material["Name"] + "",
						"Count": 1000 if material["Name"] != "Steam" else 10000
					}
				]
			},
			"Output":{
				"Items":
				[
				]
			},
			"Ticks" : 1,
		})
	
	# dust
	if "IsDust" in material:
		cvs.append([material["Name"] + "Dust", material["Label"] + " Dust"])
		item = { "Class": static_item,
			"Name": material["Name"] + "Dust",
			"Image": "T_" + material["Name"] + "Dust",
			
			"MaxCount": 32,
			
			"LabelParts": [[material["Name"] + "Dust", "parts"]],
			"Tag": "Misc",
			"Mesh": "Models/Dust",
			"Materials": [
				"Materials/" + material["Name"] + "Dust"
			],
			"UnitMul": 1,
			"Category": "Dust",
		}
		
		if "Category" in material:
			item["Category"] = material["Category"]
			
		if "Tag" in material:
			item["Tag"] = material["Tag"]
			
		objects_array.append(item)
		
		images.append({ "NewName": "T_" + material["Name"] + "Dust",
			"Base": "T_" + "Dust",
			"MulMask": "T_" + material["Name"],
			"AddMask": "T_" + "Dust" + additive_ico,
		})
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
						#{
						#	"Name": "AshDust",
						#	"Count": material["Burnable"]["TotalAsh"]
						#},
					],
				},
				"ResourceOutput":{
						"Name": "Heat",
						"Count": material["Burnable"]["HeatPerTick"],
					},
				"Ticks" : material["Burnable"]["BurnTime"],
				"Name": material["Name"] + "Dust",
			})
			
# tools	
for tool in tools:
	cvs.append([tool["Name"], tool["Label"]])
	for tier in tiers_numlist:
		if tool["StartTier"] <= tier and tool["EndTier"] >= tier:
			item_name = tier_material[tier] + tool["Name"]
			item = { "Class": static_item,
				"Name": item_name,
				"Image": "T_" + item_name,
				"ItemLogic": tool["ItemLogic"],
				"LogicJson": {
					"RecipeDictionary": tool["Name"] + recipe_dictionary,
					"Tier": tier,
				},
				"MaxCount": 1,
				"LabelParts": [[tier_material[tier], "common"], [tool["Name"], "parts"]],
				"Tag": "Misc",
				"LabelFormat": ["machines_label_format","common"],
			}
				
			objects_array.append(item)
			
			images.append({ "NewName": "T_" + item_name,
				"Base": "T_" + tool["Name"],
				"MulMask": "T_" + tier_material[tier],
				"AddMask": "T_" + tool["Name"] + additive_ico
			})
			
			if tool["Name"] == "Screwdriver" and "IsIngot" in named_material(tier_material[tier]):
				recipes_hand.append({
					"Name": tier_material[tier] + "Screwdriver",
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Parts",
								"Count": 1
							},{
								"Name": "Plank",
								"Count": 1
							},
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Screwdriver",
								"Count": 1
							}
						]
					},
					"Ticks" : 40
				})
				
			if tool["Name"] == "Multitool" and "IsIngot" in named_material(tier_material[tier]):
				recipes_hand.append({
					"Name": tier_material[tier] + "Multitool",
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Pipe",
								"Count": 2
							},
							{
								"Name": tier_material[tier] + "Plate",
								"Count": 2
							},
							{
								"Name": tier_material[tier] + "Parts",
								"Count": tier * 5 + 10
							},
							{
								"Name": circuits[tier],
								"Count": 10
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Multitool",
								"Count": 1
							}
						]
					},
					"Ticks" : 40
				})
				
			if tool["Name"] == "PaintTool" and "IsIngot" in named_material(tier_material[tier]):
				recipes_hand.append({
					"Name": tier_material[tier] + "PaintTool",
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Pipe",
								"Count": 2
							},
							{
								"Name": tier_material[tier] + "Plate",
								"Count": 2
							},
							{
								"Name": tier_material[tier] + "Parts",
								"Count": tier * 5 + 10
							},
							{
								"Name": circuits[tier],
								"Count": 10
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "PaintTool",
								"Count": 1
							}
						]
					},
					"Ticks" : 40
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

objects_array.append({ "Class": recipe_dictionary,
	"Name": "CuttingMachine" + recipe_dictionary,
	"Recipes": recipes_cutter
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "AutomaticHammer" + recipe_dictionary,
	"Recipes": recipes_hammer
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Macerator" + recipe_dictionary,
	"Recipes": recipes_macerator
})

for r in recipes_hand:
	r["Locked"] = True

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Hand" + recipe_dictionary,
	"Recipes": recipes_hand,
	"UsedIn": [{
		"Item": "Hand",
	}]
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Press" + recipe_dictionary,
	"Recipes": recipes_press
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Furnace" + recipe_dictionary,
	"Recipes": recipes_furnace
})


used_in = []
for tier in range(tools[0]["StartTier"], tools[0]["EndTier"]):
	used_in.append({
		"Item": tier_material[tier] + "Multitool",
	})
	
objects_array.append({ "Class": recipe_dictionary,
	"Name": "Multitool" + recipe_dictionary,
	"Recipes": recipes_wrench,
	"UsedIn": used_in
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Smelter" + recipe_dictionary,
	"Recipes": recipes_smelt
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Assembler" + recipe_dictionary,
	"Recipes": recipes_assembler
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "FluidDump" + recipe_dictionary,
	"Recipes": recipes_liq_dump
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "GasDump" + recipe_dictionary,
	"Recipes": recipes_gas_dump
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "FluidFurnace" + recipe_dictionary,
	"Recipes": recipes_gasfurn
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/parts.json", data);

data = {
	"Objects": researches
}

write_file("Generated/Researches/parts.json", data);

write_file("Loc/source/parts.json", cvs)