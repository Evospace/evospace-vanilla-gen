from MachinesList import *
from Common import *
from OresGen import *

recipes_mac = [] 
recipes_smelt = []
recipes_ore_washer = [] 
recipes_sep = [] 
recipes_hammer = []
recipes_arc = []

recipes_sep2 = [] 

recipes_sifter = [] 

objects_array = []

for ore_type in ore_types:
	if "NotOre" not in ore_type:
		named_mat = named_material(ore_type["Name"])
	
		recipes_hammer.append({
			"Name": ore_type["Name"] + "Ore",
			"Input":{
				"Items":[
					{
						"Name": ore_type["Name"] + "Ore",
						"Count": 1
					},
				]
			},
			"ResourceInput":{
				"Name": "Kinetic",
				"Count": 8 * ore_type["Hardness"]
			},
			"Output":{
				"Items": [
					{
						"Name": ore_type["Name"] + "ImpureOreGravel",
						"Count": 1
					},
					{
						"Name": ore_type["Name"] + "ImpureOreGravel",
						"Count": 1,
						"Probability": 50,
					}
				]
			},
			"Ticks": 100,
		})
		if "SmeltLevel" in named_mat and named_mat["SmeltLevel"] <= 0:
			recipes_smelt.append({
				"Name": ore_type["Name"] + "Ore",
				"Input":{
					"Items":[
						{
							"Name": ore_type["Name"] + "Ore",
							"Count": 1
						},
						
					]
				},
				"ResourceInput":{
							"Name": "Heat",
							"Count": 10
						},
				"Output":{
					"Items":[
						{
							"Name": ore_type["Name"] + "Ingot",
							"Count": 1
						}
					]
				},
				"Ticks" : 180,
			})
		recipes_mac.append({
			"Name": ore_type["Name"] + "ImpureOreGravel",
			"Input":{
				"Items":[
					{
						"Name": ore_type["Name"] + "ImpureOreGravel",
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
						"Name": ore_type["Name"] + "OreDust",
						"Count": 1
					},
					{
						"Name": ore_type["Name"] + "OreDust",
						"Count": 1,
						"Bonus": True
					}
				]
			},
			"Ticks" : 200,
			"Productivity": 50,
		})
		recipes_mac.append({
			"Name": ore_type["Name"] + "OreGravel",
			"Input":{
				"Items":[
					{
						"Name": ore_type["Name"] + "OreGravel",
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
						"Name": ore_type["Name"] + "OreDust",
						"Count": 1
					},
					{
						"Name": ore_type["Name"] + "OreDust",
						"Count": 1,
						"Bonus": True
					}
				]
			},
			"Ticks" : 200,
			"Productivity": 50,
		})
		if "SmeltLevel" in named_mat and named_mat["SmeltLevel"] <= 0:
			recipes_smelt.append({
				"Name": ore_type["Name"] + "OreDust",
				"Input":{
					"Items":[
						{
							"Name": ore_type["Name"] + "OreDust",
							"Count": 1
						},
					]
				},
				"ResourceInput":{
					"Name": "Heat",
					"Count": 10
				},
				"Output":{
					"Items":[
						{
							"Name": ore_type["Name"] + "Ingot",
							"Count": 1
						}
					]
				},
				"Ticks" : 100,
			})
			recipes_smelt.append({
				"Name": ore_type["Name"] + "ImpureOreGravel",
				"Input":{
					"Items":[
						{
							"Name": ore_type["Name"] + "ImpureOreGravel",
							"Count": 1
						},
					]
				},
				"ResourceInput":{
					"Name": "Heat",
					"Count": 10
				},
				"Output":{
					"Items":[
						{
							"Name": ore_type["Name"] + "Ingot",
							"Count": 1
						}
					]
				},
				"Ticks" : 120,
			})
			recipes_smelt.append({
				"Name": ore_type["Name"] + "OreGravel",
				"Input":{
					"Items":[
						{
							"Name": ore_type["Name"] + "OreGravel",
							"Count": 1
						},
					]
				},
				"ResourceInput":{
					"Name": "Heat",
					"Count": 10
				},
				"Output":{
					"Items":[
						{
							"Name": ore_type["Name"] + "Ingot",
							"Count": 1
						}
					]
				},
				"Ticks" : 120,
			})
		out_items = []
		out_items.append({
			"Name": ore_type["Name"] + "OreGravel",
			"Count": 1
		})
		if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
			oi = {
				"Name": ore_type["Byproducts"][0],
				"Count": 1,
				"Probability": 10,
			}
			
			if "ByproductChanse" in ore_type:
				oi["Probability"] = ore_type["ByproductChanse"][0]
			out_items.append(oi)
				
		out_items.append({
			"Name": "OreWater",
			"Count": 50,
			"Capacity": 32000,
		})
		recipes_ore_washer.append({
			"Name": ore_type["Name"] + "ImpureOreGravel",
			"Input":{
				"Items":[
					{
						"Name": ore_type["Name"] + "ImpureOreGravel",
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
		})
			
		sep2_rec = {
			"Name": ore_type["Name"] + "OreDust",
			"Input":{
				"Items":[
					{
						"Name": ore_type["Name"] + "OreDust",
						"Count": 1
					},
				]
			},
			"ResourceInput":{
				"Name": "Kinetic",
				"Count": 50*4
			},
			"Output":{
				"Items": [{
					"Name": (ore_type["Name"] + "Dust") if "Oxide" not in ore_type else (ore_type["Name"] + "OxideDust"),
					"Count": 1
				}],
			},
			"Ticks" : 60,
			"Productivity": 50
		}
		if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
			sep2_rec["Output"]["Items"].append({
				"Name": ore_type["Byproducts"][0],
				"Count": 1,
				"Bonus": True
			})
		recipes_sep2.append(sep2_rec)	
		
		out_items = []
		if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
			oi = {
				"Name": (ore_type["Name"] + "Dust") if "Oxide" not in ore_type else (ore_type["Name"] + "OxideDust"),
				"Count": 1
			}
			
			if "ByproductChanse" in ore_type:
				oi["Probability"] = ore_type["ByproductChanse"][0]
			
			out_items.append(oi)
				
		recipes_sep.append({
			"Name": ore_type["Name"] + "OreDust",
			"Input":{
				"Items":[
					{
						"Name": ore_type["Name"] + "OreDust",
						"Count": 1
					},
				]
			},
			"ResourceInput":{
				"Name": "Kinetic",
				"Count": 20
			},
			"Output":{
				"Items": out_items
			},
			"Ticks" : 60,
		})	
		for i in {"OreGravel", "ImpureOreGravel"}:
			recipes_sifter.append({
				"Name": ore_type["Name"] + i,
				"Input":{
					"Items":[
						{
							"Name": ore_type["Name"] + i,
							"Count": 1
						},
					]
				},
				"ResourceInput":{
					"Name": "Kinetic",
					"Count": 200
				},
				"Output":{
					"Items": [
						{
							"Name": ore_type["Byproducts"][1][0],
							"Count": 1,
							"Probability": 80,
						},
						{
							"Name": ore_type["Byproducts"][1][1],
							"Count": 1,
							"Probability": 20,
						},
						{
							"Name": ore_type["Byproducts"][1][2],
							"Count": 1,
							"Probability": 2,
						},
					]
				},
				"Ticks" : 40,
			})	
		#out_items = []
		#out_items.append({
		#	"Name": (ore_type["Name"] + "Dust") if "Oxide" not in ore_type else (ore_type["Name"] + "OxideDust"),
		#	"Count": 8
		#})
		#if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
		#	for byp in ore_type["Byproducts"]:
		#		out_items.append({
		#			"Name": byp + "Dust",
		#			"Count": 1,
		#		})
		#recipes_sep2.append({
		#	"Name": ore_type["Name"] + "ImpureOreDustSeparating",
		#	"Input":{
		#		"Items":[
		#			{
		#				"Name": ore_type["Name"] + "OreDust",
		#				"Count": 7
		#			},
		#		]
		#	},
		#	"ResourceInput":{
		#		"Name": "Kinetic",
		#		"Count": 3000 * 8
		#	},
		#	"Output":{
		#		"Items": out_items
		#	},
		#	"Ticks" : 200 * 8,
		#	"Tier": extract_tier(ore_type),
		#})
	
objects_array.append({ "Class": base_recipe,
	"Name": "Macerator" + base_recipe,
	"Recipes": recipes_mac
})
	
objects_array.append({ "Class": base_recipe,
	"Name": "Smelter" + base_recipe,
	"Recipes": recipes_smelt
})	

objects_array.append({ "Class": base_recipe,
	"Name": "OreWasher" + base_recipe,
	"Recipes": recipes_ore_washer
})

objects_array.append({ "Class": base_recipe,
	"Name": "Separator" + base_recipe,
	"Recipes": recipes_sep
})

objects_array.append({ "Class": base_recipe,
	"Name": "IndustrialSeparator" + base_recipe,
	"Recipes": recipes_sep2
})


objects_array.append({ "Class": base_recipe,
	"Name": "AutomaticHammer" + base_recipe,
	"Recipes": recipes_hammer
})

objects_array.append({ "Class": base_recipe,
	"Name": "ArcSmelter" + base_recipe,
	"Recipes": recipes_arc
})

objects_array.append({ "Class": base_recipe,
	"Name": "Sifter" + base_recipe,
	"Recipes": recipes_sifter
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/ores.json", data)