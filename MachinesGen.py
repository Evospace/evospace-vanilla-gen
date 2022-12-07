from Common import *
from MachinesList import *
from PartsList import *
import copy

images = []
objects_array = []
objects_wiki_array = {}
recipes_hand = []
recipes_wrench = []
recipes_deconstructor = []
recipes_constructor = []
researches = []

cvs = []
desc_csv = []

researches.append({
	"Name": "Core" + static_research,
	"UnlokedItems": [ "Core" ],
})

def append_recipe(recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]

	level = extract_tier(recipe["Output"]["Items"][0]["Name"]) + 1

	con_recipe = copy.deepcopy(recipe)
	con_recipe["Ticks"] = max(min(item_count * 10, 1200), 20);
	con_recipe["ResourceInput"] = { "Name": "Electricity", "Count": 20 }
	recipes_constructor.append(con_recipe)

	dec_recipe = copy.deepcopy(recipe)

	recipes_hand.append(recipe)
	
	output = copy.deepcopy(dec_recipe["Input"])
	
	dec_recipe["Input"] = copy.deepcopy(dec_recipe["Output"])
	dec_recipe["Ticks"] = max(min(item_count * 10, 1200), 20)
	dec_recipe["ResourceInput"] = { "Name": "Electricity", "Count": 20 }
	dec_recipe["Output"] = copy.deepcopy(output)
	recipes_deconstructor.append(dec_recipe)	

for machine in machines:
	cvs.append([machine["Name"], machine["Label"]])
	desc_csv.append([machine["Name"], ""])
	for tier in tiers_numlist:
		if machine["StartTier"] <= tier and machine["EndTier"] >= tier:
			item_name = tier_material[tier] +  machine["Name"]
			block_name = tier_material[tier] + machine["Name"]
			
			our_dir = "Develop/" + machine["Name"] + "/"
			
			image = machine["Name"] if "Image" not in machine else machine["Image"]
			
			level = tier - machine["StartTier"]
			
			item = { "Class": static_item,
				"Name": item_name,
				
				"Image": "T_" + tier_material[tier] + image,
				
				"LogicJson": {
					"StaticBlock": block_name,
				},
				"MaxCount": 32,
				"Tag": "Machines",
				"LabelParts": [[tier_material[tier], "common"],[machine["Name"], "machines"]],
				"LabelFormat": ["machines_label_format","common"],
				"DescriptionParts": [[machine["Name"], "description_machines"]],
				"ItemLogic": building_single_logic,
				
				"Category": CamelToSpaces(tier_material[tier]),
			}
			
			conv_speed_d = [1.66,2.5,3.33,5,6.66,10,20]
			arm_speed_d = [300/2,450/2,600/2,900/2,1200/2,1800/2,3600/2]
			
			if "PathFinding" in machine:
				item["LogicJson"]["BuildingMode"]  = "PathFinding"
			
			if "Description" in machine:
				for ss in machine["Description"]:
					if ss == "SpeedBonus":
						if level != 0:
							item["DescriptionParts"].append(["speedbonus", "common", round(1.5**level * 10) / 10])
					elif ss == "PowerOutput": 
						item["DescriptionParts"].append(["power_output", "common", machine["PowerOutput"] * 20 * 2**level])					
					else:
						item["DescriptionParts"].append([ss, "common"])	
			
			if machine["Name"] == "RobotArm" or machine["Name"] == "FilteringRobotArm":
				item["DescriptionParts"].append(["dps", "common", arm_speed_d[level]])
				
			if machine["Name"] == "FluidFurnace" or machine["Name"] == "Furnace" or machine["Name"] == "FissionReactor":
				item["DescriptionParts"].append(["furnace_desc", "common", round(1.5**level)])
				item["DescriptionParts"].append(["furnace_desc2", "common", round(2.0**level)])
			
			if machine["Name"] == "GasTurbine" or machine["Name"] == "CombustionEngine":
				item["DescriptionParts"].append(["furnace_desc", "common", round(1.5**level)])
				item["DescriptionParts"].append(["furnace_desc3", "common", round(2.0**level)])			
				
			if machine["Name"] == "Conveyor":
				item["DescriptionParts"].append(["ips", "common", conv_speed_d[level]])
				
			if machine["Name"] == "QuantumComputer":
				item["DescriptionParts"].append(["computations", "common", 2**level * 150 * 10 / 20.0])
				item["DescriptionParts"].append(["power_input", "common", 2**level * 400 * 20 * 10])
				item["DescriptionParts"].append(["electric_drain", "common", 2**level * 400 * 20])
				
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
				
			if machine["Name"] == "BatteryBox" or machine["Name"] == "SmallBattery":
				item["DescriptionParts"].append(["battery", "common", machine["CustomData"]["BaseCapacity"] + machine["CustomData"]["BonusCapacity"] * level])
			
			if "Tag" in machine:
				item["Tag"] = machine["Tag"]
			
			if "Craftable" in machine:
				item["Craftable"] = False

			# wiki json generation ------------------------------------------------
			objects_array.append(item)

			wiki_item = {}
			wiki_item["DescriptionParts"] = item["DescriptionParts"]
			wiki_item["Level"] = level

			objects_wiki_array[tier_material[tier]+machine["Name"]] = wiki_item

			# wiki json generation
			
			images.append({ "NewName": "T_" + tier_material[tier] + image,
				"Base": "T_" + image,
				"MulMask": "T_" + named_material(tier_material[tier])["Name"],
				"AddMask": "T_" + image + additive_ico,
			})
			
			logic = {
				"Recipes": machine["Recipes"] if "Recipes" in machine else machine["Name"] + recipe_dictionary,
				"Tier": tier,
				"Level": level,
			}
			
			if "CustomData" in machine:
				dict = copy.deepcopy(machine["CustomData"])
				for key, value in dict.items():
					if str(value).find("%Material%") != -1:
						dict[key] = value.replace("%Material%", tier_material[tier])
					if key == "StorageCapacity":
						dict[key] = value* 2**level
				
				logic.update(dict)	
			
			if "BlockCreation" in machine:
				logic["BlockCreation"] = machine["BlockCreation"]
				if logic["BlockCreation"].find("%Material%") != -1:
					logic["BlockCreation"] = logic["BlockCreation"].replace("%Material%", tier_material[tier])
					
				if logic["BlockCreation"].find("%Level%") != -1:
					logic["BlockCreation"] = logic["BlockCreation"].replace("%Level%", str(tier - machine["StartTier"]))
					
				if logic["BlockCreation"].find("%Tier%") != -1:
					logic["BlockCreation"] = logic["BlockCreation"].replace("%Tier%", str(tier))
					
			logic["ActorCreation"] = ""
			
			block = {
				"Name": block_name,
				"Item": item_name,
				"LogicJson": logic,
				"Class": static_block,
				"BlockLogic": machine["Name"] + "BlockLogic",
				"ReplaceTag": machine["Name"],
			}
			
			if "BlockLogic" in machine:
				block["BlockLogic"] = machine["BlockLogic"]
			
			block["Actor"] = "/Game/Blocks/" + machine["Name"] + "BP." + machine["Name"] + "BP_C"
			
			if "Selector" in machine:
				block["Selector"] = machine["Selector"]
				
			if "Positions" in machine:
				block["Positions"] = machine["Positions"]
				
			objects_array.append(block)
			
			if "Unbreakable" not in machine:
				recipes_wrench.append({
					"Name": tier_material[tier] + machine["Name"],
					"Ticks" : 20,
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"],
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"],
								"Count": 1
							}
						]
				}
			})
			
			objects_array.append({ 
				"Class": recipe_dictionary,
				"Name": machine["Name"] + recipe_dictionary,
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
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Beam" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20,
				})
				
			if machine["Name"] == "Corner":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate",
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Corner",
								"Count": 1
							}
						]
					},
					"Tier": tier,
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
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Sign",
								"Count": 1
							}
						]
					},
					"Tier": tier,
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
								"Name": electric_isolators[tier],
								"Count": 1
							},
							{
								"Name": circuits[tier],
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "AdvancedSign",
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "LogicWire":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": wires[tier],
								"Count": 2
							},
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "LogicWire",
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "LogicCircuit" or machine["Name"] == "LogicDisplay" or machine["Name"] == "LogicController" or machine["Name"] == "LogicInterface":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": "SteelPlate",
								"Count": 2
							},
							{
								"Name": circuits[tier],
								"Count": 1
							},
							{
								"Name": "SteelLogicWire" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"],
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "Scaffold":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Parts",
								"Count": 4
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Scaffold",
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "Container":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate",
								"Count": 3
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Container",
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "IndustrialSmelter":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": wires[tier],
								"Count": 32 + level * 16
							},
							{
								"Name": tier_material[tier] + "Parts",
								"Count": 12
							},
							{
								"Name": heat_isolators[tier],
								"Count": 12
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "IndustrialSmelter",
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "PyrolysisUnit":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 5
							},
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 5 + parts_ramp(level, 5)
							},
							{
								"Name": tier_material[tier] + "Container" ,
								"Count": 3
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "PyrolysisUnit" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})	
				
			if machine["Name"] == "Smelter":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate"  if tier > 0 else "StoneSurface" ,
								"Count": 4
							},
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Smelter" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "InductionCoil":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							},
							{
								"Name": "CopperPipe" ,
								"Count": 15 + 15 * level
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "InductionCoil" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "PneumaticInput":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 1
							},
							{
								"Name": "Glass" ,
								"Count": 1
							},
							{
								"Name": "BrassDetails" ,
								"Count": 1
							},
							{
								"Name": "BrassReductor" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "PneumaticInput" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Electrolyzer":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							}, 
							{
								"Name": "Coal" ,
								"Count": 2
							},
							{
								"Name": cables[tier],
								"Count": 2
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Electrolyzer" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "ChemReactor":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							},{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 4 + parts_ramp(level)
							},{
								"Name": tier_material[tier] + "ElectricEngine" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "ChemReactor" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Mixer":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 6
							},{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 6 + parts_ramp(level)
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Mixer" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Press":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 4
							},{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 1 + parts_ramp(level)
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Press" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "ElectricalSwitch":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 1
							},{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 1
							},{
								"Name": cables[tier],
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "ElectricalSwitch" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Tank":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 12
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Tank" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Terminal":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							},
							{
								"Name": cables[tier],
								"Count": 4
							},
							{
								"Name": "Glass" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "Terminal" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "FlatTerminal":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Terminal" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "FlatTerminal" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "BigTerminal":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 6
							},
							{
								"Name": cables[tier],
								"Count": 6
							},
							{
								"Name": "Glass" ,
								"Count": 4
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + "BigTerminal" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "BigFlatTerminal":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "BigTerminal" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "HugeTerminal":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 9
							},
							{
								"Name": cables[tier],
								"Count": 8
							},
							{
								"Name": "Glass" ,
								"Count": 9
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "HugeFlatTerminal":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "HugeTerminal" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "SolarPanel":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 4
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 6 + parts_ramp(level)
							},
							{
								"Name": tier_material[tier] + "ElectricEngine" ,
								"Count": 1
							},
							{
								"Name": "Glass" ,
								"Count": 3
							},
							{
								"Name": "Silicon" ,
								"Count": 3
								
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "StirlingEngine":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 2 + parts_ramp(level)
							},{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 2
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Generator":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": wires[tier],
								"Count": 12 + level * 6
							},{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 4
							},{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 2 + parts_ramp(level)
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "CompactGenerator":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": "CopperIngot" ,
								"Count": 2 + parts_ramp(level)
							},{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 1
							},{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 2 + parts_ramp(level)
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "AutomaticHammer":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 1 + parts_ramp(level)
							},{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 4
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Macerator":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 3 + parts_ramp(level)
							},{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20,
				})
				
			if machine["Name"] == "Chest":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate"  if tier != 0 else "StoneSurface" ,
								"Count": 5
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Boiler":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 1 + parts_ramp(level)
							},{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "IndustrialBoiler":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 25
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 30
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 10 + level * 5
							},
							{
								"Name": circuits[tier],
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 100
				})
				
			
				
			if machine["Name"] == "Oven":
				r = {
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": "StoneSurface" ,
								"Count": 10
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				}
				if tier != 0:
					r["Input"]["Items"].append({
						"Name": tier_material[tier] + "Pipe" ,
						"Count": 6 + parts_ramp(level)
					})
				append_recipe(r)
				
			if machine["Name"] == "BlastFurnace":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 8 + parts_ramp(level)
							},{
								"Name": "StoneSurface" ,
								"Count": 20
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "ElectricFurnace":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							},
							{
								"Name": wires[tier],
								"Count": 6 + level*3
							},
							{
								"Name": heat_isolators[tier],
								"Count": 6
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Furnace":
				recipe = {
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" if tier > 0 else "StoneSurface" ,
								"Count": 4
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				}
				if tier > 0:
					recipe["Input"]["Items"].append({
							"Name": "StoneFurnace" ,
							"Count": 1
						})
				append_recipe(recipe)
			
			if machine["Name"] == "DrillingRig":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 4 + level
							},
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 1 + level
							},
							{
								"Name": tier_material[tier] + "RobotArm" ,
								"Count": 1 + level
							},
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "FluidFurnace":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Furnace" ,
								"Count": 1
							},
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 2 + parts_ramp(level)
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Separator":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 2
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 9
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 4 + parts_ramp(level)
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "IndustrialSeparator":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 6
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 6
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 10 + parts_ramp(level)*2
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Assembler":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "RobotArm" ,
								"Count": 4
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							},
							{
								"Name": circuits[tier],
								"Count": 3 + level
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "Pumpjack":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 5
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 5 + parts_ramp(level)
							},
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 5
							},
							{
								"Name": circuits[tier],
								"Count": 3
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "Flywheel":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 1
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 4
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Deconstructor":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "FilteringRobotArm" ,
								"Count": 4
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 4
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 10 + parts_ramp(level, 10)
							},
							{
								"Name": circuits[tier],
								"Count": 3 + level
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Constructor":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "FilteringRobotArm" ,
								"Count": 4
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 4
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 10 + parts_ramp(level, 5)
							},
							{
								"Name": circuits[tier],
								"Count": 3 + level
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "FissionReactor":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": "CopperHeatPipe" ,
								"Count": 25
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 100
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 100
							},
							{
								"Name": circuits[tier],
								"Count": 20 + 5 * level
							},
							{
								"Name": heat_isolators[tier],
								"Count": 100
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 200
				})
				
			if machine["Name"] == "FusionReactor":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": "CopperHeatPipe" ,
								"Count": 25
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 40
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 100
							},
							{
								"Name": wires[tier],
								"Count": 100
							},
							{
								"Name": circuits[tier],
								"Count": 40 + 10 * level
							},
							{
								"Name": heat_isolators[tier],
								"Count": 50
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 300
				})
				
			if machine["Name"] == "Portal":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": "UltimateCatalyst" ,
								"Count": 10
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 40
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 100
							},
							{
								"Name": wires[tier],
								"Count": 100
							},
							{
								"Name": circuits[tier],
								"Count": 40 + 10 * level
							},
							{
								"Name": heat_isolators[tier],
								"Count": 50
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 300
				})
				
			if machine["Name"] == "Riteg":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": "PlutoniumCell" ,
								"Count": 1,
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 8,
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 20 + 5 * level,
							},
							{
								"Name": heat_isolators[tier],
								"Count": 10
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 100
			})
				
			if machine["Name"] == "RobotArm":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 2 + parts_ramp(level, 3)
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "FilteringRobotArm":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": circuits[tier],
								"Count": 1
							},
							{
								"Name": tier_material[tier] + "RobotArm" ,
								"Count": 1
						}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "FilteringPump":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": circuits[tier],
								"Count": 1
							},
							{
								"Name": tier_material[tier] + "Pump" ,
								"Count": 1
						}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Pump":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "RobotArm" ,
								"Count": 1
							},
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "CuttingMachine":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 4
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 1 + parts_ramp(level)
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "OreWasher":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 7
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 10 + parts_ramp(level)
							},
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 2
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Pipe":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "Vent":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 1
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 2
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Computer":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 2
							},
							{
								"Name": "Glass" ,
								"Count": 1
							},
							{
								"Name": circuits[tier],
								"Count": 5
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "QuantumComputer":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Computer" ,
								"Count": 20
							},
							{
								"Name": cables[tier],
								"Count": 50
							},
							{
								"Name": circuits[tier],
								"Count": 20
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 20
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "Conveyor":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 1,
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 1 + parts_ramp(level, 2),
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1,
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Splitter":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Conveyor" ,
								"Count": 4,
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 5 + parts_ramp(level, 5),
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1,
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Sorter":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Splitter" ,
								"Count": 1,
							},
							{
								"Name": circuits[tier],
								"Count": 6,
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if machine["Name"] == "FluidDump":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 10
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 2 + parts_ramp(level)
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "ArcSmelter":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": heat_isolators[tier],
								"Count": 6
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 4
							},
							{
								"Name": wires[tier],
								"Count": 5 + level * 5
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "Connector":
				append_recipe({
					"Name": "CopperConnector",
					"Input":{
						"Items":[
							{
								"Name": "CopperIngot" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": "CopperConnector" ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "ElectricEngine":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": wires[tier],
								"Count": 5 + level * 3
							},
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 2
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 2
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "IndustrialElectricEngine":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": wires[tier],
								"Count": 50
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 30
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 20 + level * 5
							},
							{
								"Name": circuits[tier],
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 100
				})
				
			if machine["Name"] == "BatteryBox":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": cables[tier],
								"Count": 2
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 2
							},
							{
								"Name": circuits[tier],
								"Count": 1
							},
							{
								"Name": "Battery" ,
								"Count": 5 * level + 10
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
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
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 2
							},
							{
								"Name": "AluminiumParts" ,
								"Count": 5 * level + 10
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
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
								"Name": "Silicon" ,
								"Count": parts_ramp(level, 3),
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 1
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "SteamTurbine":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 8
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 4 + parts_ramp(level)
							},
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 4
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "IndustrialSteamTurbine":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 50
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 50 + level * 10
							},
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 10
							},
							{
								"Name": circuits[tier],
								"Count": 5
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "GasTurbine":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 8
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 8 + parts_ramp(level)
							},
							{
								"Name": tier_material[tier] + "Pipe" ,
								"Count": 4
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "HeatExchanger":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 3
							},
							{
								"Name": "CopperPipe" ,
								"Count": 10
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
				
			if machine["Name"] == "AutomaticFarm":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": "DirtSurface" ,
								"Count": 4
							},
							{
								"Name": tier_material[tier] + "RobotArm" ,
								"Count": 2
							},
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 6
							},
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})

			if machine["Name"] == "ItemRack":
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": "Plank" ,
								"Count": 8
							},
							{
								"Name": tier_material[tier] + "Parts" ,
								"Count": 8
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
			
			if "Craftable" not in machine and not has_hand_recipe(recipes_hand, tier_material[tier] + machine["Name"] ):
				append_recipe({
					"Name": tier_material[tier] + machine["Name"],
					"Input":{
						"Items":[
							{
								"Name": tier_material[tier] + "Plate" ,
								"Count": 4,
							}
						]
					},
					"Output":{
						"Items":[
							{
								"Name": tier_material[tier] + machine["Name"] ,
								"Count": 1,
							}
						]
					},
					"Tier": tier,
					"Ticks" : 20
				})
	
data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/machines.json", data);

objects_array = []

objects_array.append({	
		"Class": ico_generator,
		"Name": "Macerator" + ico_generator,
		"Images": images
	})
	
data = {
	"Objects": objects_array
}

write_file("Generated/Resources/machines.json", data);

objects_array = []

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Hand" + recipe_dictionary,
	"Recipes": recipes_hand
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Deconstructor" + recipe_dictionary,
	"Recipes": recipes_deconstructor
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Constructor" + recipe_dictionary,
	"Recipes": recipes_constructor
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Multitool" + recipe_dictionary,
	"Recipes": recipes_wrench
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/machines.json", data);

data = {
	"Objects": researches
}

write_file("Generated/Researches/machines.json", data);

data = {
	"Objects": objects_wiki_array
}

write_file("Generated/Wiki/machines_wiki.json", data);

write_file("Loc/source/machines.json", cvs)
write_file("Loc/source/description_machines.json", desc_csv)
