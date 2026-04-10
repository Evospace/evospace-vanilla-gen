from MachinesList import *
from Common import *

objects_array = []

ore_types = [
	{
		# https://en.wikipedia.org/wiki/List_of_copper_ores
		"Name": "Chalcopyrite",
		"Processing":{
			"OreWasher": "PyriteDust",
			"ChemicalBath": ["Mercury", "GoldDust", "ChalcopyriteOreGravel"],
			"Separator": ["ChalcopyriteDust", "PyriteDust"],
			"Macerator": "ChalcopyriteOreDust",
			"Furnace": "CopperPlate",
		},
		"Formula": "CuFeS2",
		"Color": "#994c19",
		"ItemColor": "#b48a3a",
		"Drops": "ChalcopyriteOre",
		"Tier": 0,
	},{
		# https://en.wikipedia.org/wiki/Iron_ore
		"Name": "Pyrite",
		"Processing":{
			"OreWasher": "IronDust",
			"ChemicalBath": ["SulfuricAcid", "TantalumSludge", "SiliconOxide"],
			"Separator": ["PyriteDust", "Sulfur"],
			"Macerator": "PyriteOreDust",
			"Furnace": "IronPlate",
		},
		"Formula": "FeS2",
		"Color": [111 / 255./2.0, 106 / 255./2.0, 81 / 255./2.0],
		"ItemColor": "#c6c6c6",
		"Drops": "PyriteOre",
		"Tier": 2,
		"ExpensiveChemicalBath": 8,
	},{
		# https://en.wikipedia.org/wiki/List_of_copper_ores
		"Name": "Malachite",
		"Processing":{
			"OreWasher": "IronDust",
			"ChemicalBath": ["NitricAcid", "CopperDust", "SiliconOxide"],
			"Separator": ["MalachiteDust", "IronDust"],
			"Macerator": "MalachiteOreDust",
			"Furnace": "CopperPlate",
			"Sifter": ["MalachiteOreDust", "MalachiteDust", "MalachiteCrystal"],
		},
		"Formula": "CuCO3",
		"Crystal": True,
		"Color": "#598a90",
		"ItemColor": "#3aaf6b",
		"Drops": "MalachiteOre",
		"Tier": 0,
	},{
		# https://en.wikipedia.org/wiki/Iron_ore
		"Name": "Magnetite",
		"Processing":{
			"OreWasher": "IronDust",
			"ChemicalBath": ["Mercury", "GoldDust", "MagnetiteOreGravel"],
			"Separator": ["MagnetiteDust", "GoldDust"],
			"Macerator": "MagnetiteOreDust",
			"Furnace": "IronPlate",
		},
		"Formula": "Fe3O4+Au",
		"Color": "#323228",
		"ItemColor": "#585858",
		"Drops": "MagnetiteOre",
		"Tier": 2,
	},{
		# https://en.wikipedia.org/wiki/Bauxite
		"Name": "Bauxite",
		"Processing":{
			"OreWasher": "BauxiteDust",
			"ChemicalBath": ["NitricAcid", "TitaniumOxideDust", "SiliconOxide"],
			"Separator": ["BauxiteDust", "SiliconOxide"],
			"Macerator": "BauxiteOreDust",
			"Furnace": "BauxiteDust",
		},
		"Formula": "Al2O3+TiO2",
		"Color": "#bdad8a",
		"ItemColor": "#8c4a3a",
		"Drops": "BauxiteOre",
		"Tier": 3,
	},{
		"Name": "Ruby",
		"Processing":{
			"OreWasher": "ChromiumDust",
			"Sifter": ["RubyOreDust", "MicaFlakes", "RubyCrystal"],
			"ChemicalBath": ["SulfuricAcid", "ChromiumDust", "SiliconOxide"],
			"Separator": ["RubyDust", "ChromiumDust"],
			"Macerator": "RubyOreDust",
			"Furnace": "RubyDust",
		},
		"Formula": "CrAl203",
		"Crystal": True,
		"CrystalIcoGen": True,
		"Color": "#323228",
		"ItemColor": "#d35a4a",
		"Drops": "RubyOre",
		"Tier": 3,
	},{
		"Name": "Cinnabar",
		"ItemColor": "#e29a2f",
		"Side": [202 / 255., 115 / 512., 43 / 512.],
		"Item": [202 / 255., 115 / 512.,  43 / 512.],
		"Crystal": True,
		"Drops": "CinnabarOre",
		"Tier": 1,
		"Formula": "HgS",
		"Color": "#423228",
		"Processing":{
			"OreWasher": "Sulfur",
			"ChemicalBath": ["NitricAcid", "RareEarthSludge", "SiliconOxide"],
			"Separator": ["CinnabarDust", "Sulfur"],
			"Macerator": "CinnabarOreDust",
			"Furnace": "Sulfur",
		},
		"ExpensiveChemicalBath": 16,
	},{
		"Name": "Thorianite",
		"Processing":{
			"OreWasher": "UraniumDust",
			"Separator": ["ThoriumDust", "UraniumDust"],
			"ChemicalBath": ["SulfuricAcid", "RareEarthSludge", "SiliconOxide"],
			"Sifter": ["ThoriumDust", "UraniumDust", "ThorianiteCrystal"],
			"Furnace": "ThoriumDust",
			"Macerator": "ThorianiteOreDust",
		},
		"ExpensiveChemicalBath": 8,
		"Crystal": True,
		"CrystalIcoGen": True,
		"Color": "#324228",
		"ItemColor": "#2f4b2a",
		"Drops": "ThorianiteOre",
		"Formula": "ThO2+UO2",
		"Tier": 4,
		"SifterTier": 4,
	},{
		"Name": "Pyroplatite",
		"Processing":{
			"OreWasher": "GoldDust",
			"Separator": ["PyroplatiteDust", "GoldDust"],
			"Washing": "PyroplatiteDust",
			"Furnace": "PyroplatiteDust",
			"Macerator": "PyroplatiteOreDust",
		},
		"Color": "#324258",
		"ItemColor": "#2bb9cf",
		"Drops": "PyroplatiteOre",
		"Formula": "AuS2+PtS2+RhS2",
		"Tier": 4,
	},{
		"Name": "Coal",
		"Color": [.06, .06, .06],
		"ItemColor": "#2b2b2b",
		"Side": [.06, .06, .06],
		"Item": [.06, .06, .06],
		"Formula": "C",
		"Processing":{
			"OreWasher": "CoalDust",
			"Separator": ["CoalDust", "CoalDust"],
			"Washing": "CoalDust",
			"Furnace": "Coal",
			"Macerator": "CoalOreDust",
		},
		"Drops": "CoalOre",
		"Tier": 0,
		"Burnable": {
			"BurnTime": 800
		},
	}
]

images = []

for ore_type in ore_types:
	item_name = ore_type["Name"] + "Ore"
	description = [[ore_type["Formula"], "ores"]] if "Formula" in ore_type else []
	
	item = { "Class": "StaticItem",
		"Name": item_name,
		"Mesh": "/Game/Models/OreCrate",
		"Image": "T_" + ore_type["Name"] + "Ore",
		"StackSize": 64, 
		"Category": "Ore",
		"Label": [ore_type["Name"]+"Ore", "ores"],
		"DescriptionParts": description,
		"Color": ore_type["ItemColor"],
		"Materials" : [
			"",
			"/Game/Materials/" + ore_type["Name"]
		],
	}
	
	objects_array.append(item)
	objects_array.append({ "Class": "TesselatorMarching",
		"Name": ore_type["Name"] + "Ore" + tesselator,
		"Material": "/Game/Materials/Triplanar/" + ore_type["Name"] + "OreMaterial"
	})
	objects_array.append({ "Class": "StaticBlock",
		"Name": ore_type["Name"] + "Ore" + static_surface,
		"Tesselator": ore_type["Name"] + "Ore" + tesselator,
		"Item": item_name,
		"ColorSide": ore_type["Color"],
		"ColorTop": ore_type["Color"],
		"Minable": {"Result": ore_type["Drops"]},
		"Surface": True
	})
	images.append({
		"Base": "T_" + "Ore",
		"NewName": "T_" + ore_type["Name"] + "Ore",
		"MulMask": "T_Material" + ore_type["Name"],
		"AddMask": "T_" + "OreAdditive"
	})

	if "NotOre" not in ore_type:		
		# impure gravel		
		item = { "Class": "StaticItem",
			"Name": ore_type["Name"] + "OreImpureGravel",
			"Mesh": "/Game/Models/Gravel",
			"Image": "T_" + ore_type["Name"] + "OreImpureGravel",
			"StackSize": 64, 
			"Materials" : [
				"/Game/Materials/" + ore_type["Name"] + "OreImpureGravel"
			],
			"Category": "Ore",
			"Label": [ore_type["Name"]+"OreImpureGravel", "ores"],
			"DescriptionParts": description,
			"Color": ore_type["ItemColor"],
		}

		objects_array.append(item)
		images.append({
			"Base": "T_" + "Gravel",
			"NewName": "T_" + ore_type["Name"] + "OreImpureGravel",
			"MulMask": "T_Material" + ore_type["Name"],
			"AddMask": ["T_" + "impure_gravel_add", "T_"+"Gravel" + additive_ico]
		})

		# gravel
		item = { "Class": "StaticItem",
			"Name": ore_type["Name"] + "OreGravel",
			"Mesh": "/Game/Models/Gravel",
			"Image": "T_" + ore_type["Name"] + "OreGravel",
			"StackSize": 64,
			"Materials" : [
				"/Game/Materials/" + ore_type["Name"] + "OreGravel"
			],
			"Category": "Ore",
			"Label": [ore_type["Name"]+"OreGravel", "ores"],
			"DescriptionParts": description,
			"Color": ore_type["ItemColor"],
		}

		objects_array.append(item)
		images.append({
			"Base": "T_" + "Gravel",
			"NewName": "T_" + ore_type["Name"] + "OreGravel",
			"MulMask": "T_Material" + ore_type["Name"],
			"AddMask": "T_" + "Gravel" + additive_ico
		})
			
		# impure dust
		item = { "Class": "StaticItem",
			"Name": ore_type["Name"] + "OreDust",
			"Mesh": "/Game/Models/DustCrate",
			"Image": "T_" + ore_type["Name"] + "OreDust",
			"StackSize": 64,
			"Category": "Ore",
			"Label": [ore_type["Name"]+"OreDust", "ores"],
			"DescriptionParts": description,
			"Color": ore_type["ItemColor"],
			"Materials" : [
				"",
				"/Game/Materials/" + ore_type["Name"] + "Dust"
			],
		}

		objects_array.append(item)
		images.append({
			"Base": "T_" + "Dust",
			"NewName": "T_" + ore_type["Name"] + "OreDust",
			"MulMask": "T_Material" + ore_type["Name"],
			"AddMask": "T_" + "ImpureDustAdditive"
		})

		# dust
		item = { "Class": "StaticItem",
			"Name": ore_type["Name"] + "Dust",
			"Mesh": "/Game/Models/DustCrate",
			"Image": "T_" + ore_type["Name"] + "Dust",
			"StackSize": 64,
			"Category": "Ore",
			"Label": [ore_type["Name"]+"Dust", "ores"],
			"DescriptionParts": description,
			"Color": ore_type["ItemColor"],
			"Materials" : [
				"",
				"/Game/Materials/" + ore_type["Name"] + "Dust"
			],
		}

		objects_array.append(item)
		images.append({
			"Base": "T_" + "Dust",
			"NewName": "T_" + ore_type["Name"] + "Dust",
			"MulMask": "T_Material" + ore_type["Name"],
			"AddMask": "T_" + "DustAdditive"
		})
		if "Burnable" in ore_type:
			item["DescriptionParts"] = [["burnable", "common"]]

		# crystal
		if "Crystal" in ore_type:
			item = { "Class": "StaticItem",
				"Name": ore_type["Name"] + "Crystal",
				
				"Image": "T_" + ore_type["Name"] + "Crystal",
				"StackSize": 64,
				"Category": "Ore",
				"Label": [ore_type["Name"]+"Crystal", "ores"],
				"DescriptionParts": description,
				"Mesh": "/Game/Models/CrystalCrate",
				"Color": ore_type["ItemColor"],
				"Materials" : [
					"",
					"/Game/Materials/" + ore_type["Name"]
				],
			}
			objects_array.append(item)
			if "CrystalIcoGen" in ore_type:
				images.append({
					"Base": "T_" + "Crystal",
					"NewName": "T_" + ore_type["Name"] + "Crystal",
					"MulMask": "T_Material" + ore_type["Name"],
					"AddMask": "T_" + "CrystalAdditive"
				})
			
data = {
	"Objects": objects_array
}
filename = "Generated/Mixed/ores.json"

write_file(filename, data)
 
objects_array = []

objects_array.append({	
		"Class": ico_generator,
		"Name": "Ores" + ico_generator,
		"Images": images
	})
	
data = {
	"Objects": objects_array
}

write_file("Generated/Resources/ores.json", data)