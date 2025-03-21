from MachinesList import *
from Common import *
from OresGen import *

recipes_mac = [] 
recipes_smelt = []
recipes_ore_washer = [] 
recipes_sep = [] 
recipes_hammer = []
recipes_arc = []
recipes_sifter = [] 
recipes_chemical_bath = []
objects_array = []
recipes_furnace = []

for ore_type in ore_types:
	material_tier = ore_type["Tier"]
	ore_name = ore_type["Name"]
	processing = ore_type["Processing"]
	if "NotOre" not in ore_type:
	
	    # Hammer
		recipes_hammer.append({
			"Name": "Hammer" + ore_name + "Ore",
			"Input": one_item(ore_name + "Ore"),
			"Output":{
				"Items": [
					{
						"Name": ore_name + "OreImpureGravel",
						"Count": 1
					},
					{
						"Name": ore_name + "OreImpureGravel",
						"Count": 1,
						"Bonus": True
					}
				]
			},
			"Ticks": 100,
			"Tier": max(1, material_tier),
			"Productivity": 50,
		})

		# Smelter
		if "Furnace" in processing:
			recipes_smelt.append({
				"Name": "Smelter" + ore_name + "Ore",
				"Input": one_item(ore_name + "Ore"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 180,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": "Smelter" + ore_name + "Dust",
				"Input": one_item(ore_name + "Dust"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 50,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": "Smelter" + ore_name + "OreDust",
				"Input": one_item(ore_name + "OreDust"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 75,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": "Smelter" + ore_name + "OreImpureGravel",
				"Input": one_item(ore_name + "OreImpureGravel"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 120,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": "Smelter" + ore_name + "OreGravel",
				"Input": one_item(ore_name + "OreGravel"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 120,
				"Tier": material_tier,
			})

		# Macerator
		if "Macerator" in processing:
			recipes_mac.append({
				"Name": "Macerator" + ore_name + "OreImpureGravel",
				"Input": one_item(ore_name + "OreImpureGravel"),
				"Output":{
					"Items": [
						{
							"Name": processing["Macerator"],
							"Count": 1
						},
						{
							"Name": processing["Macerator"],
							"Count": 1,
							"Bonus": True
						}
					]
				},
				"Ticks" : 300,
				"Productivity": 33,
				"Tier": material_tier,
			})
			recipes_mac.append({
				"Name": "Macerator" + ore_name + "OreGravel",
				"Input":{
					"Items":[
						{
							"Name": ore_name + "OreGravel",
							"Count": 1
						},
					]
				},
				"ResourceInput":{
					"Name": "Kinetic",
					"Count": 10
				},
				"Output":{
					"Items": [
						{
							"Name": processing["Macerator"],
							"Count": 1
						},
						{
							"Name": processing["Macerator"],
							"Count": 1,
							"Bonus": True
						}
					]
				},
				"Ticks" : 200,
				"Productivity": 25,
				"Tier": material_tier,
			})

		# OreWasher
		out_items = []
		out_items.append({
			"Name": ore_type["Name"] + "OreGravel",
			"Count": 1
		})
		if "OreWasher" in ore_type["Processing"]:
			out_items.append({
				"Name": ore_type["Processing"]["OreWasher"],
				"Count": 1,
				"Probability": 10,
			})
		recipes_ore_washer.append({
			"Name": "OreWasher" + ore_name + "OreImpureGravel",
			"Input":{
				"Items":[
					{
						"Name": ore_name + "OreImpureGravel",
						"Count": 1
					},
					{
						"Name": "Water",
						"Count": 250
					}
				]
			},
			"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
			"Output":{
				"Items": out_items
			},
			"Ticks" : 200,
			"Tier": material_tier,
		})
			
		# Industrial Separator
		if "Separator" in processing:
			recipes_sep.append({
				"Name": "Separator" + ore_name + "OreDust",
				"Input": one_item(ore_name + "OreDust"),
				"Output":{
					"Items": [
						{
							"Name": processing["Separator"][0],
							"Count": 1
						}, {
							"Name": processing["Separator"][1],
							"Count": 1,
							"Probability": 14
						}
					],
				},
				"Ticks" : 60,
				"Tier": material_tier,
			})	

		# ChemicalBath
		if "ChemicalBath" in processing:
			recipes_chemical_bath.append({
				"Name": ore_type["Name"] + "ImpureOreGravel",
				"Input": {
					"Items": [
						{
							"Name": ore_type["Name"] + "OreImpureGravel",
							"Count": 1
						},{
							"Name": processing["ChemicalBath"][0],
							"Count": 100
						}
					]
				},
				"Output": {
					"Items": [
						{
							"Name": ore_type["Name"] + "OreGravel",
							"Count": 1
						},{
							"Name": processing["ChemicalBath"][1],
							"Count": 1
						},
					]
				},
				"Ticks" : 60,
				"Tier": material_tier,
			})	

		# Sifter
		if "Sifter" in processing:
			for gravel in {"OreImpureGravel"}:
				recipes_sifter.append({
					"Name": ore_type["Name"] + gravel,
					"Input": one_item(ore_type["Name"] + gravel),
					"Output":{
						"Items": [
							{
								"Name": ore_type["Processing"]["Sifter"][0],
								"Count": 1,
								"Probability": 80,
							},
							{
								"Name": ore_type["Processing"]["Sifter"][1],
								"Count": 1,
								"Probability": 20,
							},
							{
								"Name": ore_type["Processing"]["Sifter"][2],
								"Count": 1,
								"Probability": 2,
							},
						]
					},
					"Ticks" : 40,
					"Tier": material_tier,
				})	

		if "Burnable" in ore_type:
			for item, timeMul in [["Dust", 0.9], ["OreDust", 0.8], ["Ore", 0.9], ["OreGravel", 0.9], ["OreImpureGravel", 0.8]]:
				recipes_furnace.append({
					"Name": ore_type["Name"]+item,
					"Input": one_item(ore_type["Name"] + item),
					"Output":{
						"Items":[
						],
						
					},
					"Ticks" : ore_type["Burnable"]["BurnTime"] * timeMul,
				})
	
objects_array.append({ "Class": r_dict,
	"Name": "Macerator" + r_dict,
	"Recipes": recipes_mac
})
	
objects_array.append({ "Class": r_dict,
	"Name": "Smelter" + r_dict,
	"Recipes": recipes_smelt
})	

objects_array.append({ "Class": r_dict,
	"Name": "OreWasher" + r_dict,
	"Recipes": recipes_ore_washer,
})

objects_array.append({ "Class": r_dict,
	"Name": "Separator" + r_dict,
	"Recipes": recipes_sep
})

objects_array.append({ "Class": r_dict,
	"Name": "AutomaticHammer" + r_dict,
	"Recipes": recipes_hammer
})

objects_array.append({ "Class": r_dict,
	"Name": "ArcSmelter" + r_dict,
	"Recipes": recipes_arc
})

objects_array.append({ "Class": r_dict,
	"Name": "Sifter" + r_dict,
	"Recipes": recipes_sifter
})

objects_array.append({ "Class": r_dict,
	"Name": "ChemicalBath" + r_dict,
	"Recipes": recipes_chemical_bath
})

objects_array.append({ "Class": r_dict,
	"Name": "Furnace" + r_dict,
	"Recipes": recipes_furnace
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/ores.json", data)