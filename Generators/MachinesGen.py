from Common import *
from MachinesList import *
from PartsList import *
import copy
from functools import partial

images = []
objects_array = []
recipes_hand = []

cvs = []

def plate_frame_component(tier, count):
	if tier == 0:
		return {"Name": "BuildingMaterial", "Count": count}
	else:
		return {"Name": tier_material[tier] + "Plate", "Count": count}

for machine in machines:
	cvs.append([machine["Name"], machine["Label"]])
	for tier in range(machine["StartTier"], machine["EndTier"] + 1):
		level = tier - machine["StartTier"]

		def tiered(name):
			return tier_material[tier] + name
		
		def circuit():
			return circuits[tier]
		
		def pipe():
			return tier_material[tier] + "Pipe"
		
		def part_low():
			low_tier = tier - 1
			if low_tier > 2:
				return "SteelParts"
			return tier_material[max(low_tier, 1)] + "Parts"
		
		def part():
			return tier_material[tier] + "Parts"
		
		def plate():
			return tier_material[tier] + "Plate"
	
		
		def coil_pair(mul = 1):
			if tier <= 2:
				return ["CopperWire", 8]

			start_tier = machine["StartTier"]
			global_level = tier - start_tier
			first_coil_level = max(0, 3 - start_tier)
			coil_level = global_level - first_coil_level

			if coil_level <= 0:
				return ["CopperWire", mul*16]
			elif coil_level == 1:
				return ["BasicCoil", mul]
			elif coil_level == 2:
				return ["AdvancedCoil", mul]
			elif coil_level == 3:
				return ["PowerCoil", mul]
			
			return ["PowerCoil", mul*2]
		
		def frame_pair(mul = 1):
			if tier <= 2:
				return [tier_material[tier] + "Parts", 2 ** tier * mul]

			start_tier = machine["StartTier"]
			global_level = tier - start_tier
			first_frame_level = max(0, 3 - start_tier)
			frame_level = global_level - first_frame_level

			if frame_level <= 0:
				return ["BasicFrame", mul]
			elif frame_level == 1:
				return ["ReinforcedFrame", mul]
			elif frame_level == 2:
				return ["ReinforcedFrame", mul*2]
			elif frame_level == 3:
				return ["ModularFrame", mul]
			
			return ["ModularFrame", mul*2]
				
		def engine():
			if tier > 1:
				return tier_material[tier] + "ElectricEngine"
			return "CopperParts"
		
		def robotarm():
			return tier_material[tier] + "RobotArm"
		
		def append_recipe(recipe):
			recipe["Tier"] = tier
			recipes_hand.append(recipe)

		def wire():
			return a_wires[tier][0]
			
		def wire_count(count):
			return [a_wires[tier][0], count * a_wires[tier][1]]

		def parts_count(count):
			return {"Name": tier_material[tier] + "Parts", "Count": count}
		
		def isolators_count(count):
			return {"Name": "BuildingMaterial", "Count": count}
		
		def plates_count(count):
			return plate_frame_component(tier, count)

		block_name = machine["Name"] if "ExactName" in machine else (tier_material[tier] + machine["Name"])

		image = machine["Image"] if "Image" in machine else machine["Name"]

		labelParts = ["machines_label_format", "common", [tier_material[tier], "common"], [machine["Name"], "machines"]]
		if "ExactName" in machine:
			labelParts = [machine["Name"], "machines"]

		item = { "Class": "StaticItem",
			"Name": block_name,
			"Image": ("T_" + image) if "ExactName" in machine else ("T_" + tier_material[tier] + image),
			"Block": block_name,
			"StackSize": 32,
			"Label": labelParts,
			"DescriptionParts": [[machine["Name"], "description"]],
			"ItemLogic": building_single_logic if "ItemLogic" not in machine else machine["ItemLogic"],
			"Tier": tier,
			"Category": machine["Category"] if "Category" in machine else tier_material[tier],
		}

		conv_speed_d = [1.66,2.5,3.33,5,6.66,10,20]
		arm_speed_d = [300/2,450/2,600/2,900/2,1200/2,1800/2,3600/2]

		if "Description" in machine:
			for ss in machine["Description"]:
				if ss == "SpeedBonus":
					if level != 0:
						item["DescriptionParts"].append(["speedbonus", "common", round(2**level * 10) / 10])
				elif ss == "PowerOutput": 
					item["DescriptionParts"].append(["power_output", "common", [block_name, "data"]])		
				elif ss == "PowerInput": 
					item["DescriptionParts"].append(["power_input", "common", [block_name, "data"]])			
				else:
					item["DescriptionParts"].append([ss, "common"])	

		if machine["Name"] == "RobotArm":
			item["DescriptionParts"].append(["dps", "common", arm_speed_d[level]])		
			
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

		objects_array.append(item)

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

		if "PathFinding" in machine:
			block["BuildingMode"]  = "PathFinding"

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
				"Item": block_name,
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
							"Name": tier_material[tier] + "Plate" if tier != 0 else "BuildingMaterial",
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
				"Input": items([
					wire_count(32),
					[plate(), 12],
					frame_pair(3),
					["BuildingMaterial", 64]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 80
			})
			
		if machine["Name"] == "PyrolysisUnit":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 6],
					["CopperPipe", 5 + parts_ramp(level, 5)],
					frame_pair(2)
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})	
			
		if machine["Name"] == "PneumaticInput":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 3],
					[part(), 1],
					["BrassDetails", 1],
					["BrassReductor", 1]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Electrolyzer":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 3],
					["Coal", 2],
					[cables[tier], 2 + parts_ramp(level)]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Fermenter":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 2],
					[part(), 6 + parts_ramp(level)]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "IndustrialChemReactor":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 15],
					["Glass", 10],
					frame_pair(2),
					[engine(), 2]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 40
			})

		if machine["Name"] == "AtmosphericCondenser":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 5],
					[part(), 2],
					frame_pair(1),
					["CopperPipe", 5 + parts_ramp(level)]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "ChemicalBath":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 8],
					[part(), 10],
					frame_pair(2),
					[engine(), 1]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 40
			})

		if machine["Name"] == "Lamp":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": one_item(plate(), 2),
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
				"Input": items([
					[plate(), 4],
					[part(), 5],
					frame_pair(2),
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "ElectricalSwitch":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 4],
					[part(), 1 + parts_ramp(level)],
					[cables[tier]]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Tank":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": one_item(plate(), 12),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Terminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 3],
					["Glass", 4],
					[cables[tier], 1]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "FlatTerminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 3],
					["Glass", 4],
					[cables[tier], 1]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "BigTerminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 6],
					["Glass", 8],
					[cables[tier], 2]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "BigFlatTerminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 6],
					["Glass", 8],
					[cables[tier], 2]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "HugeTerminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 9],
					["Glass", 12],
					[cables[tier], 3]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "HugeFlatTerminal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 9],
					["Glass", 12],
					[cables[tier], 3]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "SolarPanel" or machine["Name"] == "SmallSolarPanel":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 4],
					frame_pair(1 if machine["Name"] == "SmallSolarPanel" else 3),
					[tier_material[tier] + "SolarCell", 1 if machine["Name"] == "SmallSolarPanel" else 10]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "StirlingEngine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[part_low(), 2 + parts_ramp(level, 2)],
					[plate(), 2]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "SteamEngine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[part_low(), 2 + parts_ramp(level, 2)],
					[tier_material[tier] + "Pipe", 2]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Generator" or machine["Name"] == "IndustrialGenerator":
			count_mul = 1 if machine["Name"] == "Generator" else 3
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 8 * count_mul],
					wire_count(12 * count_mul),
					frame_pair(count_mul),
					[circuit(), 1 * count_mul]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "CompactGenerator":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 1],
					wire_count(2),
					frame_pair(),
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "AutomaticHammer":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 4],
					[part(), 1 + parts_ramp(level)],
					frame_pair(),
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Macerator":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 2],
					frame_pair(),
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Chest":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": tier_material[tier] + "Plate" if tier != 0 else "BuildingMaterial",
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
					["BuildingMaterial", 10],
					[tiered("Pipe"), 10]
				], level),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "BlastFurnace":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					["BuildingMaterial", 20],
					[tiered("Pipe"), 20]
				], level),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "ElectricFurnace":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 3],
					[wire(), 6 + level*3],
					["BuildingMaterial", 6]
				]),
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
							"Name": tier_material[tier] + "Plate"+ static_item if tier > 0 else "BuildingMaterial",
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
					[plate(), 4],
					[robotarm(), 1 + level],
					frame_pair(3),
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "FractionatingColumn":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 10+level],
					["StainlessSteelPipe", 10 + parts_ramp(level)],
					frame_pair(2),
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
					frame_pair()
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
					frame_pair(2),
					[circuit(), 3 + level*2]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Pumpjack":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 5],
					[part(), (2 + parts_ramp(level, 2))*8],
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
				"Input": items([
					[robotarm(), 1],
					[plate(), 3],
					frame_pair(1),
					[circuit(), 1 + level]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "FissionReactor":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					["CopperHeatPipe", 25],
					[plate(), 100],
					[part(), 100],
					[circuit(), 10 + 5 * level],
					["BuildingMaterial", 128]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "FusionReactor":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					["CopperHeatPipe", 25],
					[plate(), 40],
					[wire(), 100],
					[circuit(), 15 + 5 * level],
					["PlatinumReflector", 40],
					["BuildingMaterial", 128]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 300
			})
			
		if machine["Name"] == "Portal":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					["UltimateCatalyst", 10],
					[plate(), 40],
					["ModularFrame", 20],
					[wire(), 100],
					[circuit(), 15 + 5 * level],
					["BuildingMaterial", 256]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 300
			})
			
		if machine["Name"] == "Riteg":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					["PlutoniumCell"],
					frame_pair(2),
					[plate(), 8],
					["CopperPipe", 20 + 5 * level]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 100
		})
			
		if machine["Name"] == "RobotArm":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 1],
					[part_low(), 2**(level+1)]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Loader":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[robotarm(), 5],
					[engine(), 1],
					[circuit(), 2],
					frame_pair()
				]),
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
			
		if machine["Name"] == "OreWasher":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 7],
					[pipe(), 2],
					frame_pair(2)
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "Pipe":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": one_item(plate()),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 5
			})

		if machine["Name"] == "Vent":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[pipe()],
					[part(), 2]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "Spawner":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 10]
				]),
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
				"Input": items([
					[plate()],
					[part(), 1 + parts_ramp(level, 1)]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
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
							"Name": tier_material[tier] + "Parts",
							"Count": 8
						},
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
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
							"Name": tier_material[tier] + "Parts",
							"Count": 8
						}
					]
				},
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "ArcSmelter":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					["BuildingMaterial", 32],
					[part(), 4],
					wire_count(5)
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})
			
		if machine["Name"] == "CopperConnector":
			append_recipe({
				"Name": machine["Name"],
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

		if machine["Name"] == "ElectricEngine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					frame_pair(),
					[plate(), 2],
					coil_pair(),
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "CombustionEngine":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input": items([
					[plate(), 10],
					[part(), 3*8],
					[circuit(), 3],
					["Catalyst"]
				]),
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
							"Name": tier_material[tier] + "Parts",
							"Count": 2*8
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
							"Name": tier_material[tier] + "Parts",
							"Count": 4*8
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
				"Input": items([
					["DirtSurface", 4],
					[tier_material[tier] + "RobotArm", 2],
					frame_pair(2),
					[] if tier <= 4 else [circuit(), 4]
				]),
				"Output": one_item(tier_material[tier] + machine["Name"]),
				"Ticks" : 20
			})

		if machine["Name"] == "ItemRack":
			append_recipe({
				"Name": tier_material[tier] + machine["Name"],
				"Input":{
					"Items":[
						{
							"Name": "Log",
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

write_file("Generated/Resources/machines.json", data)

objects_array = []

objects_array.append({ "Class": r_dict,
	"Name": "Hand" + r_dict,
	"Recipes": recipes_hand
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/machines.json", data)

write_file("Loc/source/machines.json", cvs)