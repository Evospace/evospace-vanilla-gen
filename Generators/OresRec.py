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

for ore_type in ore_types:
	material_tier = ore_type["Tier"]
	ore_name = ore_type["Name"]
	processing = ore_type["Processing"]
	if "NotOre" not in ore_type:
		named_mat = named_material(ore_name)
	
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
			"Ticks": 100 * 2**material_tier,
			"Tier": material_tier,
			"Productivity": 50,
		})

		# Furnace
		if "Furnace" in processing:
			recipes_smelt.append({
				"Name": "Furnace" + ore_name + "Ore",
				"Input": one_item(ore_name + "Ore"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 180 * 2**material_tier,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": "Furnace" + ore_name + "OreDust",
				"Input": one_item(ore_name + "OreDust"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 100 * 2 **material_tier,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": "Furnace" + ore_name + "OreImpureGravel",
				"Input": one_item(ore_name + "OreImpureGravel"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 120 * 2**material_tier,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": "Furnace" + ore_name + "OreGravel",
				"Input": one_item(ore_name + "OreGravel"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 120 * 2**material_tier,
				"Tier": material_tier,
			})
			if "Macerator" in processing:
				recipes_smelt.append({
					"Name": "Furnace" + processing["Macerator"],
					"Input": one_item(processing["Macerator"]),
					"Output": one_item(processing["Furnace"]),
					"Ticks" : 180 * 2**material_tier,
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
				"Ticks" : 300 * 2**material_tier,
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
				"Ticks" : 200 * 2**material_tier,
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
			"Ticks" : 200 * 2**material_tier,
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
				"Ticks" : 60 * 2**material_tier,
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
				"Ticks" : 60 * 2**material_tier,
				"Tier": material_tier,
			})	

		# Sifter
		if "Sifter" in processing:
			for gravel in {"OreGravel", "OreImpureGravel"}:
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
					"Ticks" : 40 * 2**material_tier,
					"Tier": material_tier,
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
	"Recipes": recipes_ore_washer
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

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/ores.json", data)