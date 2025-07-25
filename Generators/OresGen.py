from MachinesList import *
from Common import *

objects_array = []

cvs = []

ore_types = [
	{
		# https://en.wikipedia.org/wiki/List_of_copper_ores
		"Name": "Chalcopyrite",
		"Processing":{
			"OreWasher": "PyriteDust",
			"ChemicalBath": ["Mercury", "ChalcopyriteOreGravel", "GoldDust"],
			"Separator": ["ChalcopyriteDust", "PyriteDust"],
			"Macerator": "ChalcopyriteOreDust",
			"Furnace": "CopperPlate",
		},
		"Formula": "CuFeS2",
		"Color": [0.8/2.0,.3/2.0,.3/2.0],
		"Drops": "ChalcopyriteOre",
		"Tier": 0,
	},{
		# https://en.wikipedia.org/wiki/List_of_copper_ores
		"Name": "Malachite",
		"Processing":{
			"OreWasher": "IronDust",
			"ChemicalBath": ["NitricAcid", "SiliconOxide", "CopperDust"],
			"Separator": ["MalachiteDust", "IronDust"],
			"Macerator": "MalachiteOreDust",
			"Furnace": "CopperPlate",
			"Sifter": ["MalachiteOreDust", "MalachiteDust", "MalachiteCrystal"],
		},
		"Formula": "CuCO3",
		"Crystal": True,
		"Color": [0.8/2.0,.3/2.0,.3/2.0],
		"Drops": "MalachiteOre",
		"Tier": 0,
	},{
		# https://en.wikipedia.org/wiki/Iron_ore
		"Name": "Pyrite",
		"Processing":{
			"OreWasher": "IronDust",
			"ChemicalBath": ["SulfuricAcid", "SiliconOxide", "TantalumSludge"],
			"Separator": ["PyriteDust", "Sulfur"],
			"Macerator": "PyriteOreDust",
			"Furnace": "IronPlate",
		},
		"Formula": "FeS2",
		"Color": [111 / 255./2.0, 106 / 255./2.0, 81 / 255./2.0],
		"Drops": "PyriteOre",
		"Tier": 2,
	},{
		# https://en.wikipedia.org/wiki/Iron_ore
		"Name": "Magnetite",
		"Processing":{
			"OreWasher": "IronDust",
			"ChemicalBath": ["Mercury", "MagnetiteOreGravel", "GoldDust"],
			"Separator": ["MagnetiteDust", "GoldDust"],
			"Macerator": "MagnetiteOreDust",
			"Furnace": "IronPlate",
		},
		"Formula": "Fe3O4+Au",
		"Color": [111 / 255./2.0, 106 / 255./2.0, 81 / 255./2.0],
		"Drops": "MagnetiteOre",
		"Tier": 2,
	},{
		# https://en.wikipedia.org/wiki/Bauxite
		"Name": "Bauxite",
		"Processing":{
			"OreWasher": "BauxiteDust",
			"ChemicalBath": ["NitricAcid", "SiliconOxide", "TitaniumOxideDust"],
			"Separator": ["BauxiteDust", "SiliconOxide"],
			"Macerator": "BauxiteOreDust",
			"Furnace": "BauxiteDust",
		},
		"Formula": "Al2O3+TiO2",
		"Color": [.5/2.0, .5/2.0, 1/2.0],
		"Drops": "BauxiteOre",
		"Tier": 3,
	},{
		"Name": "Ruby",
		"Processing":{
			"OreWasher": "ChromiumDust",
			"Sifter": ["RubyOreDust", "MicaFlakes", "RubyCrystal"],
			"ChemicalBath": ["SulfuricAcid", "SiliconOxide", "ChromiumDust"],
			"Separator": ["RubyDust", "ChromiumDust"],
			"Macerator": "RubyOreDust",
			"Furnace": "RubyDust",
		},
		"Formula": "CrAl203",
		"Crystal": True,
		"CrystalIcoGen": True,
		"Color": [.5/2.0, .5/2.0, 1/2.0],
		"Drops": "BauxiteOre",
		"Tier": 3,
	},{
		"Name": "Cinnabar",
		"Color": [202 / 255., 115 / 512., 43 / 512.],
		"Side": [202 / 255., 115 / 512., 43 / 512.],
		"Item": [202 / 255., 115 / 512.,  43 / 512.],
		"Crystal": True,
		"Drops": "CinnabarOre",
		"Tier": 1,
		"Formula": "HgS",
		"Processing":{
			"OreWasher": "Sulfur",
			"ChemicalBath": ["NitricAcid", "SiliconOxide", "RareEarthSludge"],
			"Separator": ["CinnabarDust", "Sulfur"],
			"Macerator": "CinnabarOreDust",
			"Furnace": "Sulfur",
		},
	},{
		"Name": "Thorianite",
		"Processing":{
			"OreWasher": "UraniumDust",
			"Separator": ["ThoriumDust", "UraniumDust"],
			"ChemicalBath": ["SulfuricAcid", "SiliconOxide", "RareEarthSludge"],
			"Sifter": ["ThoriumDust", "UraniumDust", "ThorianiteCrystal"],
			"Furnace": "ThoriumDust",
			"Macerator": "ThorianiteOreDust",
		},
		"Crystal": True,
		"CrystalIcoGen": True,
		"Color": [0.3/2.0, 0.7/2.0, 0.3/2.0],
		"Drops": "ThorianiteOre",
		"Formula": "ThO2+UO2",
		"Tier": 4,
	},{
		"Name": "Pyroplatite",
		"Processing":{
			"OreWasher": "GoldDust",
			"Separator": ["PyroplatiteDust", "GoldDust"],
			"Washing": "PyroplatiteDust",
			"Furnace": "PyroplatiteDust",
			"Macerator": "PyroplatiteOreDust",
		},
		"Color": [0.3/2.0, 0.7/2.0, 0.3/2.0],
		"Drops": "PyroplatiteOre",
		"Formula": "AuS2+PtS2+RhS2",
		"Tier": 4,
	},{
		"Name": "Coal",
		"Color": [.06, .06, .06],
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
		"Color": [.5,.5,.5],
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
	
	cvs.append([ore_type["Name"]+"Ore", ore_type["Name"]+" Ore"])
	
	item = { "Class": "StaticItem",
		"Name": item_name,
		"Mesh": "/Game/Models/OreCrate",
		"Image": "T_" + ore_type["Name"] + "Ore",
		"StackSize": 64, 
		"Category": "Ore",
		"Label": [ore_type["Name"]+"Ore", "ores"],
		"DescriptionParts": description,
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
		cvs.append([ore_type["Name"]+"OreImpureGravel", ore_type["Name"]+" Impure Ore Gravel"])
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
		}

		objects_array.append(item)
		images.append({
			"Base": "T_" + "Gravel",
			"NewName": "T_" + ore_type["Name"] + "OreImpureGravel",
			"MulMask": "T_Material" + ore_type["Name"],
			"AddMask": ["T_" + "impure_gravel_add", "T_"+"Gravel" + additive_ico]
		})

		# gravel
		cvs.append([ore_type["Name"]+"OreGravel", ore_type["Name"]+" Ore Gravel"])
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
		}

		objects_array.append(item)
		images.append({
			"Base": "T_" + "Gravel",
			"NewName": "T_" + ore_type["Name"] + "OreGravel",
			"MulMask": "T_Material" + ore_type["Name"],
			"AddMask": "T_" + "Gravel" + additive_ico
		})
			
		# impure dust
		cvs.append([ore_type["Name"] + "OreDust", ore_type["Name"]+" Ore Dust"])
		item = { "Class": "StaticItem",
			"Name": ore_type["Name"] + "OreDust",
			"Mesh": "/Game/Models/DustCrate",
			"Image": "T_" + ore_type["Name"] + "OreDust",
			"StackSize": 64,
			"Category": "Ore",
			"Label": [ore_type["Name"]+"OreDust", "ores"],
			"DescriptionParts": description,
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
		cvs.append([ore_type["Name"] + "Dust", ore_type["Name"]+" Dust"])
		item = { "Class": "StaticItem",
			"Name": ore_type["Name"] + "Dust",
			"Mesh": "/Game/Models/DustCrate",
			"Image": "T_" + ore_type["Name"] + "Dust",
			"StackSize": 64,
			"Category": "Ore",
			"Label": [ore_type["Name"]+"Dust", "ores"],
			"DescriptionParts": description,
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
			cvs.append([ore_type["Name"] + "Crystal", ore_type["Name"]+" Crystal"])
			item = { "Class": "StaticItem",
				"Name": ore_type["Name"] + "Crystal",
				
				"Image": "T_" + ore_type["Name"] + "Crystal",
				"StackSize": 64,
				"Category": "Ore",
				"Label": [ore_type["Name"]+"Crystal", "ores"],
				"DescriptionParts": description,
				"Mesh": "/Game/Models/CrystalCrate",
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

cvs.append(["FeS2", "FeS₂"])
cvs.append(["CuFeS2", "CuFeS₂"])
cvs.append(["CuCO3", "CuCO₃"])
cvs.append(["Fe3O4+Au", "Fe₃O₄ + Au"])
cvs.append(["HgS", "HgS"])
cvs.append(["CrAl203", "CrAl₂0₃"])
cvs.append(["C", "C"])
cvs.append(["BeCa2AlPO4", "BeCa₂Al(PO₄)₃"])
cvs.append(["Al2O3+TiO2", "Al₂O₃ + TiO₂"])
cvs.append(["ThO2+UO2", "ThO₂ + UO₂"])
cvs.append(["AuS2+PtS2+RhS2", "AuS₂ + PtS₂ + RhS₂"])
cvs.append(["FeNb2O3+FeTa2O3", "FeNb₂O₃ + FeTa₂O₃"])
cvs.append(["ThPO4+NdPO4+YPO4", "ThPO₄ + NdPO₄ + YPO₄"])

write_file("Generated/Resources/ores.json", data)

write_file("Loc/source/ores.json", cvs)