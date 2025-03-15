from Common import *
from MachinesList import *
from PartsList import *
import copy
from functools import partial

images = []
objects_array = []
objects_wiki_array = {}
recipes_hand = []

cvs = []

def plate_frame_component(tier, count):
	if tier == 0:
		return {"Name": "StoneSurface", "Count": count}
	else:
		return {"Name": tier_material[tier] + "Plate", "Count": count}

for machine in machines:
	cvs.append([machine["Name"], machine["Label"]])
	for tier in range(machine["StartTier"], machine["EndTier"] + 1):

		def tiered(name):
			return tier_material[tier] + name
		
		def wire():
			return a_wires[tier]
		
		def circuit():
			return circuits[tier]
		
		def pipe():
			return tier_material[tier] + "Pipe"
		
		def plate():
			return tier_material[tier] + "Plate"
		
		def gearbox():
			return tier_material[tier] + "Gearbox"
		
		def robotarm():
			return tier_material[tier] + "RobotArm"
		
		def append_recipe(recipe):
			recipe["Tier"] = tier
			recipes_hand.append(recipe)

		def wire():
			return a_wires[tier]
			
		def wires_count(count):
			return {"Name": a_wires[tier], "Count": count}

		def parts_count(count):
			return {"Name": tier_material[tier] + "Parts", "Count": count}
		
		def isolators_count(count):
			return {"Name": heat_isolators[tier], "Count": count}
		
		def plates_count(count):
			return plate_frame_component(tier, count)

		block_name = machine["Name"] if "ExactName" in machine else (tier_material[tier] + machine["Name"])

		image = machine["Image"] if "Image" in machine else machine["Name"]

		level = tier - machine["StartTier"]

		labelParts = [[tier_material[tier], "common"],[machine["Name"], "machines"]]
		labelFormat = ["machines_label_format","common"]
		if "ExactName" in machine:
			labelParts = [[machine["Name"], "machines"]]
			labelFormat = ""

		item = { "Class": "StaticItem",
			"Name": block_name,
			
			"Image": ("T_" + image) if "ExactName" in machine else ("T_" + tier_material[tier] + image),
			
			"LogicJson": {
				"StaticBlock": block_name,
			},
			"StackSize": 32,
			"LabelParts": labelParts,
			"LabelFormat": labelFormat,
			"DescriptionParts": [["tier", "common", tier],[machine["Name"], "machines_description"]],
			"ItemLogic": building_single_logic if "ItemLogic" not in machine else machine["ItemLogic"],
			
			"Category": machine["Category"] if "Category" in machine else CamelToSpaces(tier_material[tier]),
		}

		conv_speed_d = [1.66,2.5,3.33,5,6.66,10,20]
		arm_speed_d = [300/2,450/2,600/2,900/2,1200/2,1800/2,3600/2]

		if "PathFinding" in machine:
			item["LogicJson"]["BuildingMode"]  = "PathFinding"

		if "Description" in machine:
			for ss in machine["Description"]:
				if ss == "SpeedBonus":
					if level != 0:
						item["DescriptionParts"].append(["speedbonus", "common", round(2**level * 10) / 10])
				elif ss == "PowerOutput": 
					item["DescriptionParts"].append(["power_output", "common", machine["PowerOutput"] * 20 * 2**level])		
				elif ss == "PowerInput": 
					item["DescriptionParts"].append(["power_input", "common", machine["PowerInput"] * 20 * 2**level])			
				else:
					item["DescriptionParts"].append([ss, "common"])	

		if machine["Name"] == "RobotArm":
			item["DescriptionParts"].append(["dps", "common", arm_speed_d[level]])
			
		if machine["Name"] == "FluidFurnace" or machine["Name"] == "Furnace" or machine["Name"] == "FissionReactor":
			item["DescriptionParts"].append(["furnace_desc", "common", round(2**level)])
			item["DescriptionParts"].append(["furnace_desc2", "common", round(2.0**level)])

		if machine["Name"] == "GasTurbine" or machine["Name"] == "CombustionEngine":
			item["DescriptionParts"].append(["furnace_desc", "common", round(2**level)])
			item["DescriptionParts"].append(["furnace_desc3", "common", round(2**level)])			
			
		if machine["Name"] == "Conveyor":
			item["DescriptionParts"].append(["ips", "common", conv_speed_d[level]])

		if machine["Name"] == "ItemRack":
			item["DescriptionParts"].append(["item_rack", "common", 2048*(level+1)])
			
		if machine["Name"] == "Computer":
			item["DescriptionParts"].append(["computations", "common", 2**level * 3 * 10 / 20.0])
			item["DescriptionParts"].append(["power_input", "common", 2**level * 20 * 10])
			item["DescriptionParts"].append(["electric_drain", "common", 2**level * 20])
			
		if machine["Name"] == "DrillingRig":
			item["DescriptionParts"].append(["power_input", "common", 2**level * 20 * 30])
			
		if machine["Name"] == "FissionReactor":
			item["DescriptionParts"].append(["heat_drain", "common", 80*20])
			
		if machine["Name"] == "HeatPipe":
			item["DescriptionParts"].append(["heat_drain", "common", 20])
			
		if machine["Name"] == "Flywheel":
			item["DescriptionParts"].append(["kinetic_drain", "common", 40])
			
		if machine["Name"] == "Chest":
			item["DescriptionParts"].append(["chest", "common", 20+5*level])
			
		if machine["Name"] == "Container":
			item["DescriptionParts"].append(["container", "common", 30*(level+1)])
			
		if machine["Name"] == "SmallBattery":
			item["DescriptionParts"].append(["battery", "common", machine["CustomData"]["BaseCapacity"] + machine["CustomData"]["BonusCapacity"] * level])

		# wiki json generation ------------------------------------------------
		objects_array.append(item)

		wiki_item = {}
		wiki_item["DescriptionParts"] = item["DescriptionParts"]
		wiki_item["Level"] = level

		objects_wiki_array[tier_material[tier]+machine["Name"]] = wiki_item
		# wiki json generation

		if machine["Name"] == "BiElectricEngine":
			images.append({
				"Base": "T_" + "ElectricEngine",
				"NewName": "T_" + tier_material[tier] + "BiElectricEngine",
				"MulMask": "T_Material" + named_material(tier_material[tier])["Name"],
				"AddMask": "T_GreenCircle" + additive_ico,
			})
		else:
			images.append({ 
				"NewName": "T_" + tier_material[tier] + image,
				"Base": "T_" + image,
				"MulMask": "T_Material" + named_material(tier_material[tier])["Name"],
				"AddMask": "T_" + image + additive_ico,
			})

		block = {
			"Name": block_name,
			"Item": block_name,
			"Class": "StaticBlock",
			"BlockLogic": machine["Name"] + "BlockLogic",
			"ReplaceTag": machine["Name"] if "ReplaceTag" not in machine else machine["ReplaceTag"],
			"Minable": {"Result": block_name},
			"Tier": tier,
			"Level": tier - machine["StartTier"]
		}

		if "NoActorRenderable" in machine:
			block["NoActorRenderable"] = True

		if "BlockLogic" in machine and (machine["BlockLogic"] == "SimpleInstancedBlockLogic" or machine["BlockLogic"] == "SelectCrafterInstanced" or machine["BlockLogic"] == "AutoCrafterInstanced"):
			block["Cover"] = tier_material[tier] + machine["Name"] + static_cover

		if "BlockLogic" in machine:
			block["BlockLogic"] = machine["BlockLogic"]

		if "NoActorRenderable" not in machine:
			block["Actor"] = "Blocks/" + machine["Name"] + "BP." + machine["Name"] + "BP_C"

		if "Selector" in machine:
			block["Selector"] = machine["Selector"]

		if "DefaultRotation" in machine:
			block["DefaultRotation"] = machine["DefaultRotation"]
			
		if "Positions" in machine:
			block["Positions"] = machine["Positions"]
			
		objects_array.append(block)

		objects_array.append({ 
			"Class": r_dict,
			"Name": machine["Name"] + r_dict,
			"UsedIn": [{
				"Item": tier_material[tier] + machine["Name"],
				"Tier": tier
			}]
		})

		if machine["Name"] == "Beam":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3),
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20,
			})
			
		if machine["Name"] == "Corner":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(1)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Sign":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Plate" if tier != 0 else "StoneSurface",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "AdvancedSign":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Sign",
							"Count": 1
						},
						{
							"Name": circuits[tier],
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "LogicWire":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": one_item(wire(), 2),
				"Output": one_item(tier_material[tier] + "LogicWire"),
				"Ticks" : 20
			})
			
		if machine["Name"] == "LogicCircuit" or machine["Name"] == "LogicDisplay" or machine["Name"] == "LogicController" or machine["Name"] == "LogicInterface":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(2),
						{
							"Name": circuits[tier],
							"Count": 1
						},
						{
							"Name": "SteelLogicWire",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Scaffold":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						parts_count(4),
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Container":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "IndustrialSmelter":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						wires_count(32 + level * 16),
						parts_count(12),
						isolators_count(12)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 80
			})
			
		if machine["Name"] == "PyrolysisUnit":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(5),
						{
							"Name": "CopperPipe",
							"Count": 5 + parts_ramp(level, 5)
						},
						{
							"Name": tier_material[tier] + "Container",
							"Count": 3
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})	
			
		if machine["Name"] == "InductionCoil":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3),
						{
							"Name": "CopperPipe",
							"Count": 15 + 15 * level
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "PneumaticInput":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3),
						parts_count(1),
						{
							"Name": "BrassDetails",
							"Count": 1
						},
						{
							"Name": "BrassReductor",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Electrolyzer":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3), 
						{
							"Name": "Coal",
							"Count": 2
						},
						{
							"Name": cables[tier],
							"Count": 2 + parts_ramp(level)
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Fermenter":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(2), 
						parts_count(6 + parts_ramp(level))
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "ChemReactor":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3),
						parts_count(4 + parts_ramp(level)),
						{
							"Name": tier_material[tier] + "ElectricEngine",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "IndustrialChemReactor":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(8),
						parts_count(8 + parts_ramp(level)),
						{
							"Name": tier_material[tier] + "ElectricEngine",
							"Count": 2
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 40
			})

		if machine["Name"] == "AtmosphericCondenser":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(5),
						parts_count(2 + parts_ramp(level)),
						{
							"Name": "CopperPipe",
							"Count": 5 + parts_ramp(level)
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "ChemicalBath":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(8),
						parts_count(5 + parts_ramp(level)),
						{
							"Name": tier_material[tier] + "ElectricEngine",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 40
			})

		if machine["Name"] == "Lamp":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(2)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 40
			})

		if machine["Name"] == "Sifter":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(4),
						parts_count(4 + parts_ramp(level)),
						{
							"Name": tier_material[tier] + "ElectricEngine",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 40
			})
			
		if machine["Name"] == "Mixer":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(4),
						parts_count(4 + parts_ramp(level))
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Press":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(4),
						parts_count(1 + parts_ramp(level))
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "ElectricalSwitch":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(1),
						parts_count(1 + parts_ramp(level)),
						{
							"Name": cables[tier],
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Tank":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(12)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Terminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3),
						{
							"Name": cables[tier],
							"Count": 4
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "FlatTerminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Terminal",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "BigTerminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(1),
						{
							"Name": cables[tier],
							"Count": 6
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "BigFlatTerminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "BigTerminal",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "HugeTerminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(9),
						{
							"Name": cables[tier],
							"Count": 8
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "HugeFlatTerminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "HugeTerminal",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "SolarPanel" or machine["Name"] == "SmallSolarPanel":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(4),
						parts_count(4 + parts_ramp(level)),
						{
							"Name": tier_material[tier] + "SolarCell",
							"Count": 1 if machine["Name"] == "SmallSolarPanel" else 10
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "StirlingEngine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						parts_count(2 + parts_ramp(level)),{
							"Name": tier_material[tier] + "Plate",
							"Count": 2
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "SteamEngine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						parts_count(2 + parts_ramp(level)),{
							"Name": tier_material[tier] + "Pipe",
							"Count": 2
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Generator":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						wires_count(12 + level * 6),
						plates_count(4),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "IndustrialGenerator":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						wires_count(32 + level * 12),
						plates_count(8),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 3
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 100
			})
			
		if machine["Name"] == "CompactGenerator":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": "CopperWire",
							"Count": 2 + parts_ramp(level)
						},
						plates_count(1),
						{
							"Name": tier_material[tier] + "Parts",
							"Count": 2 + parts_ramp(level)
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "AutomaticHammer":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(4),
						parts_count(1 + parts_ramp(level))
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Macerator":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 1
						},
						plates_count(2)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Chest":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Plate" if tier != 0 else "StoneSurface",
							"Count": 5
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Boiler":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3),
						parts_count(1 + parts_ramp(level))
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "IndustrialBoiler":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Pipe",
							"Count": 25
						},
						plates_count(30),
						parts_count(10 + level*5),
						{
							"Name": circuits[tier],
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 100
			})
			
		if machine["Name"] == "Oven":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					["StoneSurface", 10],
					[tiered("Pipe"), 10]
				], level),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "BlastFurnace":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					["StoneSurface", 20],
					[tiered("Pipe"), 20]
				], level),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "ElectricFurnace":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3),
						wires_count(6 + level*3),
						isolators_count(6)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Smelter":
			recipe = {
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(4)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			}
			if tier > 0:
				recipe["Input"]["Items"].append({
						"Name": "StoneSmelter",
						"Count": 1
					})
			append_recipe(recipe)
			
		if machine["Name"] == "Furnace":
			recipe = {
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Plate"+ static_item if tier > 0 else "StoneSurface",
							"Count": 4
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			}
			if tier > 0:
				recipe["Input"]["Items"].append({
						"Name": "StoneFurnace",
						"Count": 1
					})
			append_recipe(recipe)

		if machine["Name"] == "DrillingRig":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 4 + level],
					[gearbox(), 3 + parts_ramp(level, 3)],
					[robotarm(), 1 + level]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "OilCrackingTower":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 10+level],
					["StainlessSteelPipe", 10 + parts_ramp(level)],
					[gearbox(), 2 + level * 2],
					[tier_material[tier] + "Pump", 6]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 40
			})

		if machine["Name"] == "FluidFurnace":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[tier_material[tier] + "Furnace"],
					[pipe(), 2 + parts_ramp(level)]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Separator":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[pipe(), 2],
					[gearbox()]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Assembler":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[robotarm(), 4],
					[plate(), 3],
					[circuit(), 3 + level]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Pumpjack":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 5],
					[gearbox(), 2 + parts_ramp(level, 2)],
					[pipe(), 5],
					[circuit(), 3]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Flywheel":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(1),
						parts_count(4 + parts_ramp(level))
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Constructor":
			objects_array.append({ 
				"Class": r_dict,
				"Name": "Hand" + r_dict,
				"UsedIn": [{
					"Item": tier_material[tier] + machine["Name"],
					"Tier": tier
				}]
			})
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "RobotArm",
							"Count": 4
						},
						plates_count(4),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 1 + parts_ramp(level, 1)
						},
						{
							"Name": circuits[tier],
							"Count": 3 + level
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "FissionReactor":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": "CopperHeatPipe",
							"Count": 25
						},
						plates_count(100),
						parts_count(100),
						{
							"Name": circuits[tier],
							"Count": 20 + 5 * level
						},
						isolators_count(100)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "FusionReactor":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": {
					"Items": [
						{
							"Name": "CopperHeatPipe",
							"Count": 25
						},
						plates_count(40),
						parts_count(100),
						wires_count(100),
						{
							"Name": circuits[tier],
							"Count": 40 + 10 * level
						},
						isolators_count(50)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 300
			})
			
		if machine["Name"] == "Portal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": "UltimateCatalyst",
							"Count": 10
						},
						plates_count(40),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 50
						},
						wires_count(100),
						{
							"Name": circuits[tier],
							"Count": 40 + 10 * level
						},
						isolators_count(50)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 300
			})
			
		if machine["Name"] == "Riteg":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": "PlutoniumCell",
							"Count": 1,
						},
						plates_count(8),
						parts_count(20 + 5 * level),
						isolators_count(10)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 100
		})
			
		if machine["Name"] == "RobotArm":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						parts_count(2 + parts_ramp(level, 3)),
						plates_count(1)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "HeatPipe":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": one_item(plate(), 4),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 10
			})

		if machine["Name"] == "OverflowPump":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[circuit(), 3],
					[tier_material[tier] + "Pump"]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Pump":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[robotarm()],
					[pipe()]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "CuttingMachine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(4),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 1
						},
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "OreWasher":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(7),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 3
						},
						{
							"Name": tier_material[tier] + "Pipe",
							"Count": 2
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Pipe":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(1)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 5
			})

		if machine["Name"] == "Vent":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Pipe",
							"Count": 1
						},
						parts_count(2)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Computer":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(1),
						{
							"Name": circuits[tier],
							"Count": 5
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Conveyor":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(1),
						parts_count(1 + parts_ramp(level, 1))
					]
				},
				"Output":{
					"Items":[
						{
							"Name": tier_material[tier] + machine["Name"],
							"Count": 1,
						}
					]
				},
				"Ticks" : 20
			})
			
		if machine["Name"] == "Splitter":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Conveyor",
							"Count": 2,
						},
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 1
						},
					]
				},
				"Output":{
					"Items":[
						{
							"Name": tier_material[tier] + machine["Name"],
							"Count": 1,
						}
					]
				},
				"Ticks" : 20
			})
			
		if machine["Name"] == "Sorter":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Splitter",
							"Count": 1,
						},
						{
							"Name": circuits[tier],
							"Count": 6,
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Destroyer":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(10),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "ArcSmelter":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						isolators_count(6),
						parts_count(4),
						wires_count(5 + level * 5),
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "CopperConnector":
			append_recipe({
				"Name": "CopperConnector",
				"Input":{
					"Items":[
						{
							"Name": "CopperWire",
							"Count": 1
						}
					]
				},
				"Output": one_item(machine["Name"]),
				"Ticks" : 5
			})
			
		if machine["Name"] == "ElectricEngine" or machine["Name"] == "BiElectricEngine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						wires_count(5 + level * 3),
						{
							"Name": tier_material[tier] + "Pipe",
							"Count": 2
						},
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "IndustrialElectricEngine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						wires_count(50),
						plates_count(10),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 3
						},
						{
							"Name": circuits[tier],
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 100
			})

		if machine["Name"] == "CombustionEngine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(10),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 3
						},
						{
							"Name": circuits[tier],
							"Count": 3
						},
						{
							"Name": "Catalyst",
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 100
			})
			
		if machine["Name"] == "BatteryBox":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": cables[tier],
							"Count": 2 * (level + 1)
						},
						plates_count(2),
						{
							"Name": circuits[tier],
							"Count": 1
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "SmallBattery":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": cables[tier],
							"Count": 2
						},
						plates_count(2),
						{
							"Name": "AluminiumParts",
							"Count": 5 * level + 10
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Diode":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": cables[tier],
							"Count": 2
						},
						{
							"Name": "Silicon",
							"Count": parts_ramp(level, 3),
						},
						plates_count(1)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "SteamTurbine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(8),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 2
						},
						{
							"Name": tier_material[tier] + "Pipe",
							"Count": 4
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "IndustrialSteamTurbine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(50),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 4
						},
						{
							"Name": tier_material[tier] + "Pipe",
							"Count": 10
						},
						{
							"Name": circuits[tier],
							"Count": 5
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "GasTurbine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(8),
						{
							"Name": tier_material[tier] + "Gearbox",
							"Count": 2
						},
						{
							"Name": tier_material[tier] + "Pipe",
							"Count": 4
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "HeatExchanger":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3),
						{
							"Name": "CopperPipe",
							"Count": 10
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "KineticHeater":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(3),
						{
							"Name": "CopperPipe",
							"Count": 4 + parts_ramp(level, 4)
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "HandGenerator":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						plates_count(2),
						{
							"Name": "CopperParts",
							"Count": 4
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "AutomaticFarm":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": "DirtSurface",
							"Count": 4
						},
						{
							"Name": tier_material[tier] + "RobotArm",
							"Count": 2
						},
						plates_count(6),
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "ItemRack":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": "Plank",
							"Count": 8
						},
						parts_count(8)
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if not has_hand_recipe(recipes_hand, tier_material[tier] + machine["Name"]):
			print("No recipe for "+machine["Name"])

data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/machines.json", data);

objects_array = []

objects_array.append({	
	"Class": ico_generator,
	"Name": "AllMachines" + ico_generator,
	"Images": images
})
	
data = {
	"Objects": objects_array
}

write_file("Generated/Resources/machines.json", data);

objects_array = []

objects_array.append({ "Class": r_dict,
	"Name": "Hand" + r_dict,
	"Recipes": recipes_hand
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/machines.json", data)

data = {
	"Objects": objects_wiki_array
}

write_file("Generated/Wiki/machines_wiki.json", data)

write_file("Loc/source/machines.json", cvs)