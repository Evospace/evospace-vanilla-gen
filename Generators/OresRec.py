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
recipes_arc_furnace = []

for ore_type in ore_types:
	material_tier = ore_type["Tier"]
	ore_name = ore_type["Name"]
	processing = ore_type["Processing"]
	if "NotOre" not in ore_type:
	
	    # Hammer
		recipes_hammer.append({
			"Name": "Hammer" + ore_name + "Ore",
			"Input": one_item(ore_name + "Ore"),
			"Output": items([
				[ore_name + "OreImpureGravel", 1],
				[ore_name + "OreImpureGravel", 1, True],
			]),
			"Ticks": 100,
			"Tier": max(1, material_tier),
			"Productivity": 50,
		})

		# Smelter
		if "Furnace" in processing:
			recipes_smelt.append({
				"Name": ore_name + "Ore",
				"Input": one_item(ore_name + "Ore"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 180,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": ore_name + "Dust",
				"Input": one_item(ore_name + "Dust"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 50,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": ore_name + "OreDust",
				"Input": one_item(ore_name + "OreDust"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 75,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": ore_name + "OreImpureGravel",
				"Input": one_item(ore_name + "OreImpureGravel"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 120,
				"Tier": material_tier,
			})
			recipes_smelt.append({
				"Name": ore_name + "OreGravel",
				"Input": one_item(ore_name + "OreGravel"),
				"Output": one_item(processing["Furnace"]),
				"Ticks" : 120,
				"Tier": material_tier,
			})
			recipes_arc_furnace.append({
				"Name": ore_name + "OreDust",
				"Input": one_item(ore_name + "OreDust"),
				"Output": one_item(processing["Furnace"]),
				"Tier": material_tier,
				"Ticks" : 120
			})

		# Macerator
		if "Macerator" in processing:
			recipes_mac.append({
				"Name": ore_name + "OreImpureGravel",
				"Input": one_item(ore_name + "OreImpureGravel"),
				"Output": items([
					[processing["Macerator"], 1],
					[processing["Macerator"], 1, True],
				]),
				"Ticks" : 132,
				"Productivity": 50,
				"Tier": material_tier,
			})
			recipes_mac.append({
				"Name": ore_name + "OreGravel",
				"Input": one_item(ore_name + "OreGravel"),
				"ResourceInput":{
					"Name": "Kinetic",
					"Count": 10
				},
				"Output": items([
					[processing["Macerator"], 1],
					[processing["Macerator"], 1, True],
				]),
				"Ticks" : 200,
				"Productivity": 25,
				"Tier": material_tier,
			})

		# OreWasher
		washer_out = [[ore_type["Name"] + "OreGravel", 1]]
		if "OreWasher" in ore_type["Processing"]:
			washer_out.append([ore_type["Processing"]["OreWasher"], 1, True])
		recipes_ore_washer.append({
			"Name": ore_name + "OreImpureGravel",
			"Input": items([
				[ore_name + "OreImpureGravel", 1],
				["Water", 250],
			]),
			"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
			"Output": items(washer_out),
			"Ticks" : 200,
			"Tier": material_tier,
			"Productivity": 50
		})
			
		# Industrial Separator
		if "Separator" in processing:
			recipes_sep.append({
				"Name": "Separator" + ore_name + "OreDust",
				"Input": one_item(ore_name + "OreDust"),
				"Output": items([
					[processing["Separator"][0], 1],
					[processing["Separator"][1], 1, 14],
				]),
				"Ticks" : 60,
				"Tier": material_tier,
			})	

		# ChemicalBath
		if "ChemicalBath" in processing:
			recipes_chemical_bath.append({
				"Name": ore_type["Name"] + "ImpureOreGravel",
				"Input": items([
					[ore_type["Name"] + "OreImpureGravel", ore_type["ExpensiveChemicalBath"] if "ExpensiveChemicalBath" in ore_type else 1 ],
					[processing["ChemicalBath"][0], 500 if "ExpensiveChemicalBath" in ore_type else 250 ]
				]),
				"Output": items([
					[processing["ChemicalBath"][1]],
					[processing["ChemicalBath"][2], ore_type["ExpensiveChemicalBath"] if "ExpensiveChemicalBath" in ore_type else 1 ]
				]),
				"Ticks" : 200,
				"Tier": 3,
			})	

		# Sifter
		if "Sifter" in processing:
			sifter_tier = ore_type["SifterTier"] if "SifterTier" in ore_type else material_tier
			sf = ore_type["Processing"]["Sifter"]
			recipes_sifter.append({
				"Name": ore_type["Name"] + "OreImpureGravel",
				"Input": one_item(ore_type["Name"] + "OreImpureGravel"),
				"Output": items([
					[sf[0], 1, 80],
					[sf[1], 1, 20],
					[sf[2], 1, 2],
				]),
				"Ticks" : 100,
				"Tier": sifter_tier,
			})
			recipes_sifter.append({
				"Name": ore_type["Name"] + "OreImpureGravelDense",
				"Input": one_item(ore_type["Name"] + "OreImpureGravel", 6),
				"Output": items([
					[sf[0], 1, 70],
					[sf[1], 1, 20],
					[sf[2], 1, 11],
				]),
				"Ticks" : 400,
				"Tier": sifter_tier,
			})

		if "Burnable" in ore_type:
			for item, timeMul in [["Dust", 0.9], ["OreDust", 0.8], ["Ore", 0.9], ["OreGravel", 0.9], ["OreImpureGravel", 0.8]]:
				recipes_furnace.append({
					"Name": ore_type["Name"]+item,
					"Input": one_item(ore_type["Name"] + item),
					"Output": no_items(),
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

objects_array.append({ "Class": r_dict,
	"Name": "ArcSmelter" + r_dict,
	"Recipes": recipes_arc_furnace,
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/ores.json", data)