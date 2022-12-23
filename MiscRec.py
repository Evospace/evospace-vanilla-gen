from Common import *
from MachinesList import *
from MiscGen import *
import copy

objects_array = []

recipes_wrench = []
recipes_blast_furnace = []
recipes_oven = []
recipes_smelter = []
recipes_arc_furnace = []
recipes_macerator = []
recipes_boiler = []
recipes_farm = []
recipes_condens = []
recipes_generator = []
recipes_electric_engine = []
recipes_compact_generator = []
recipes_steam_engine = []
recipes_steam_turbine = []
recipes_pump = []
recipes_electrolyzer = []
recipes_cutter = []
recipes_furnace = []
recipes_ferm = []
recipes_toolarm = []
recipes_hammer = []
recipes_mixer = []
recipes_chem = []

recipes_sep = []
recipes_sep2 = []
recipes_press = []

recipes_elfurn = []

recipes_radiator = []
recipes_solar = []
recipes_fission = []

recipes_coil = []

recipes_indu = []

recipes_exch = []
recipes_iexch = []

recipes_freezer = []

recipes_combustion = []

recipes_pyro = []

recipes_computer = []
recipes_q_computer = []

recipes_assembler = []

recipes_gasturb = []

recipes_filtering_unit = []

recipes_chemical_bath = []

recipes_centrifuge = []

recipes_riteg = []
	
recipes_industrial_steam_turbine = []	

recipes_fusion_reactor = []

recipes_industrial_boiler = []

recipes_industrial_electric_engine = []

recipes_portal = []

recipes_hand = []

def append_recipe(recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]

	level = extract_tier(recipe["Output"]["Items"][0]["Name"]) + 1
	
	dec_recipe = copy.deepcopy(recipe)

	recipes_hand.append(recipe)
	
	output = copy.deepcopy(dec_recipe["Input"])
	
	dec_recipe["Ticks"] = max(min(item_count * 10, 400), 20);
	dec_recipe["ResourceInput"] = { "Name": "Electricity", "Count": 20 * level }
	recipes_assembler.append(dec_recipe)

def append_recipe_hand_press(recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]
	
	dec_recipe = copy.deepcopy(recipe)

	recipes_hand.append(recipe)
	
	output = copy.deepcopy(dec_recipe["Input"])
	
	dec_recipe["Ticks"] = 60;
	dec_recipe["ResourceInput"] = { "Name": "Kinetic", "Count": 100 }
	recipes_press.append(dec_recipe)		

# wrenching

recipes_industrial_steam_turbine.append({
	"Name": "Rotating",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Steam",
		"Count": fission_fullpower * 0.9
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Electricity",
		"Count": fission_fullpower * 0.9 * 0.9
	},
	
	"Ticks" : 200,
	"Loss": 10,
})

recipes_industrial_boiler.append({
	"Name":"Boiling",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 2000
			},
		]
	},
	"ResourceInput":{
		"Name":"Heat",
		"Count": fission_fullpower
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name":"Steam",
		"Count": fission_fullpower * 0.9
	},
	"Ticks" : 200,
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumIngot1",
	"Input":{
		"Items":[
			{
				"Name": "ProducerGas",
				"Count": 1000
			}
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": fission_fullpower*0.9*0.9
	},
	"Output":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumIngot2",
	"Input":{
		"Items":[
			{
				"Name": "ProducerGas",
				"Count": 3000
			}
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 2 * fission_fullpower*0.9*0.9
	},
	"Output":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot",
				"Count": 1 * 3
			}
		]
	},
	"Ticks" : 200 * 2,
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumIngot4",
	"Input":{
		"Items":[
			{
				"Name": "UltimateCatalyst",
				"Count": 1,
				"split":0
			}
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": fission_fullpower*0.9*0.9
	},
	"Output":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumIngot3",
	"Input":{
		"Items":[
			{
				"Name": "UltimateCatalyst",
				"Count": 3,
				"split":0
			}
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 2 * fission_fullpower*0.9*0.9
	},
	"Output":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot",
				"Count": 1 * 3
			}
		]
	},
	"Ticks" : 200 * 2,
})

recipes_smelter.append({
	"Name":"Glass",
	"Input":{
		"Items":[
			{
				"Name": "SandSurface",
				"Count": 1
			},
		]
	},
	"ResourceInput": {
		"Name": "Heat",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Glass",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
})
	
for list in (simple_deco, wooden_misc, simple_single, simple_blocks, static_mesh_block):	
	for one in list:
		recipes_wrench.append({
			"Name": one["Name"] + "Wrenching",
			"Ticks" : 20,
			"Input":{
				"Items":[
					{
						"Name": one["Name"],
						"Count": 1
					}
				]
			},
			"Output":{
				"Items":[
					{
						"Name": one["Name"],
						"Count": 1
					}
				]
			}
		})

# other		

append_recipe({
	"Name":"Cell",
	"Input":{
		"Items":[
			{
				"Name": "StainlessSteelPlate",
				"Count": 1
			},
			{
				"Name": "StainlessSteelParts",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Cell",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

append_recipe({
	"Name":"Cell2",
	"Input":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Cell",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

append_recipe({
	"Name":"UraniumCell",
	"Input":{
		"Items":[
			{
				"Name": "Uranium235Dust",
				"Count": 3
			},
			{
				"Name": "UraniumDust",
				"Count": 20
			},
			{
				"Name": "Cell",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "UraniumCell",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

append_recipe({
	"Name":"ThoriumCell",
	"Input":{
		"Items":[
			{
				"Name": "ThoriumDust",
				"Count": 20
			},
			{
				"Name": "Cell",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ThoriumCell",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

append_recipe({
	"Name":"Uranium233Cell",
	"Input":{
		"Items":[
			{
				"Name": "Uranium233Dust",
				"Count": 3
			},
			{
				"Name": "Cell",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Uranium233Cell",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

append_recipe({
	"Name":"PlutoniumCell",
	"Input":{
		"Items":[
			{
				"Name": "PlutoniumDust",
				"Count": 3
			},
			{
				"Name": "Cell",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "PlutoniumCell",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

append_recipe({
	"Name":"FilteringCell",
	"Input":{
		"Items":[
			{
				"Name": "Coal",
				"Count": 10
			},
			{
				"Name": "Cell",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "FilteringCell",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name":"Circuit",
	"Input":{
		"Items":[
			{
				"Name": "CircuitBoard",
				"Count": 1
			},
			{
				"Name": "CopperWire",
				"Count": 6
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Circuit",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name":"AdvancedCircuit",
	"Input":{
		"Items":[
			{
				"Name": "Silicon",
				"Count": 1
			},	
			{
				"Name": "Circuit",
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 30
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedCircuit",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name":"SiliconWafer",
	"Input":{
		"Items":[
			{
				"Name": "Silicon",
				"Count": 1
			},	
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "SiliconWafer",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name":"Processor",
	"Input":{
		"Items":[
			{
				"Name": "SiliconWafer",
				"Count": 1
			},	
			{
				"Name": "AdvancedCircuit",
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 80
	},
	"Output":{
		"Items":[
			{
				"Name": "Processor",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
})

recipes_assembler.append({
	"Name":"QuantumBrain",
	"Input":{
		"Items":[	
			{
				"Name": "QuantumProcessor",
				"Count": 2
			},
			{
				"Name": "UltimateCatalyst",
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 1000
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumBrain",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
})

append_recipe({
	"Name":"Catalyst",
	"Input":{
		"Items":[
			{
				"Name": "Cell",
				"Count": 1
			},	
			{
				"Name": "GoldWire",
				"Count": 10
			},	
			{
				"Name": "Coal",
				"Count": 4
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Catalyst",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

append_recipe({
	"Name":"UltimateCatalyst",
	"Input":{
		"Items":[
			{
				"Name": "Cell",
				"Count": 1
			},	
			{
				"Name": "NeutroniumParts",
				"Count": 8
			},	
			{
				"Name": "Coke",
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "UltimateCatalyst",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name": "AdvancedCircuitBoard",
	"Input":{
		"Items":[
			{
				"Name": "Plastic",
				"Count": 1
			},
			{
				"Name": "GoldWire",
				"Count": 3
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedCircuitBoard",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 80,
	
})

recipes_assembler.append({
	"Name":"Processor2",
	"Input":{
		"Items":[
			{
				"Name": "SiliconWafer",
				"Count": 1
			},	
			{
				"Name": "AdvancedCircuitBoard",
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 80
	},
	"Output":{
		"Items":[
			{
				"Name": "Processor",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name":"QuantumCore",
	"Input":{
		"Items":[
			{
				"Name": "RareEarthElement",
				"Count": 1
			},	
			{
				"Name": "CopperParts",
				"Count": 2
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 1000
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumCore",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name":"QuantumCircuit",
	"Input":{
		"Items":[
			{
				"Name": "QuantumCore",
				"Count": 2
			},	
			{
				"Name": "AdvancedCircuitBoard",
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 1000 / 7
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumCircuit",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name":"QuantumProcessor",
	"Input":{
		"Items":[
			{
				"Name": "QuantumCircuit",
				"Count": 1
			},	
			{
				"Name": "Processor",
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 2000 / 13
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumProcessor",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name":"CopperWire",
	"Input":{
		"Items":[
			{
				"Name": "CopperIngot",
				"Count": 1
			},
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperWire",
				"Count": 2
			}
		]
	},
	"Ticks" : 100,
})

recipes_assembler.append({
	"Name":"SuperconductorWire",
	"Input":{
		"Items":[
			{
				"Name": "SuperconductorIngot",
				"Count": 1
			},
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "SuperconductorWire",
				"Count": 2
			}
		]
	},
	"Ticks" : 100,
})

recipes_assembler.append({
	"Name":"Battery",
	"Input":{
		"Items":[
			{
				"Name": "SulfuricAcid",
				"Count": 100
			},
			{
				"Name": "CopperParts",
				"Count": 1
			},
			{
				"Name": "StainlessSteelPlate",
				"Count": 1
			},
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Battery",
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name":"GoldWire",
	"Input":{
		"Items":[
			{
				"Name": "GoldIngot",
				"Count": 1
			},
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "GoldWire",
				"Count": 2
			}
		]
	},
	"Ticks" : 100,
})

append_recipe({
	"Name":"ReflectorCell",
	"Input":{
		"Items":[
			{
				"Name": "Cell",
				"Count": 1
			},
			{
				"Name": "BerylliumDust",
				"Count": 3
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ReflectorCell",
				"Count": 1
			}
		]
	},
	"Ticks" : 100,
})

append_recipe({
	"Name":"ControlCell",
	"Input":{
		"Items":[
			{
				"Name": "Cell",
				"Count": 1
			},
			{
				"Name": "BoronDust",
				"Count": 3
			},
		]
	},
	"ResourceInput": {
		"Name": "Electricity",
		"Count": 1000 / 9
	},
	"Output":{
		"Items":[
			{
				"Name": "ControlCell",
				"Count": 1
			}
		]
	},
	"Ticks" : 100,
})

recipes_condens.append({
	"Name":"Water",
	"Input":{
		"Items":[
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Water",
				"Count": 250
			}
		]
	},
	"Ticks" : 200,
})

recipes_condens.append({
	"Name":"Oxygen",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput": {
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "Oxygen",
				"Count": 250
			}
		]
	},
	"Ticks" : 200,
})

recipes_condens.append({
	"Name":"Nitrogen",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput": {
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "Nitrogen",
				"Count": 1000
			}
		]
	},
	"Ticks" : 200,
})

recipes_condens.append({
	"Name":"Helium",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput": {
		"Name": "Kinetic",
		"Count": 40
	},
	"Output":{
		"Items":[
			{
				"Name": "Helium",
				"Count": 100
			}
		]
	},
	"Ticks" : 200,
})

recipes_condens.append({
	"Name":"Methane",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput": {
		"Name": "Kinetic",
		"Count": 40
	},
	"Output":{
		"Items":[
			{
				"Name": "Methane",
				"Count": 80
			}
		]
	},
	"Ticks" : 200,
})

recipes_condens.append({
	"Name":"Hydrogen",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput": {
		"Name": "Kinetic",
		"Count": 40
	},
	"Output":{
		"Items":[
			{
				"Name": "Hydrogen",
				"Count": 50
			}
		]
	},
	"Ticks" : 200,
})

recipes_farm.append({
	"Name":"Logs",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 625
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Log",
				"Count": 15
			}
		]
	},
	"Ticks" : 2000,
})

recipes_farm.append({
	"Name":"Pumpkin",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 625
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Pumpkin",
				"Count": 10
			}
		]
	},
	"Ticks" : 1000,
})

recipes_centrifuge.append({
	"Name":"DepletedUraniumCell",
	"Input":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "PlutoniumDust",
				"Count": 1,
				"split": 10,
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 100
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"UraniumCell",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 1
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 7100
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"UraniumCell2",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell",
				"Count": 2
			},
			{
				"Name": "ControlCell",
				"Count": 1,
				"split": 0,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 2
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 7100 * 2.2
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"UraniumCell3",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell",
				"Count": 3
			},
			{
				"Name": "ControlCell",
				"Count": 1,
				"split": 0,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 3
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 7100 * 3.3
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"UraniumCell4",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell",
				"Count": 3
			},
			{
				"Name": "ControlCell",
				"Count": 5,
				"split": 0,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 3
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 7100 * 3.3 / 2
	},
	"Ticks" : 2000 * 2,
})

recipes_fission.append({
	"Name":"ControlCell3",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell",
				"Count": 1
			},
			{
				"Name": "ControlCell",
				"Count": 3,
				"split": 0,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 1
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 7100 / 4
	},
	"Ticks" : 8000 * .9 * .9,
})

recipes_fission.append({
	"Name":"ThoriumCell",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell",
				"Count": 3,
			},
			{
				"Name": "ReflectorCell",
				"Count": 1,
				"split": 0,
			},
			{
				"Name": "ThoriumCell",
				"Count": 2,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 3
			},
			{
				"Name": "Uranium233Cell",
				"Count": 2,
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 200
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"PlutoniumCell",
	"Input":{
		"Items":[
			{
				"Name": "PlutoniumCell",
				"Count": 1,
			},
			{
				"Name": "ReflectorCell",
				"Count": 1,
				"split": 0,
			},
			{
				"Name": "ThoriumCell",
				"Count": 3,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Uranium233Cell",
				"Count": 3,
			},
			{
				"Name": "DepletedUraniumCell",
				"Count": 1
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 200
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"PlutoniumCell2",
	"Input":{
		"Items":[
			{
				"Name": "PlutoniumCell",
				"Count": 1,
			},
			{
				"Name": "ReflectorCell",
				"Count": 2,
				"split": 0,
			},
			{
				"Name": "ThoriumCell",
				"Count": 6,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Uranium233Cell",
				"Count": 6,
			},
			{
				"Name": "DepletedUraniumCell",
				"Count": 1
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 200
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"ControlCell",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell",
				"Count": 1
			},
			{
				"Name": "ControlCell",
				"Count": 1,
				"split": 0,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 1
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 7100 / 2
	},
	"Ticks" : 4000 * 0.9,
})

recipes_fission.append({
	"Name":"Uranium233Cell",
	"Input":{
		"Items":[
			{
				"Name": "Uranium233Cell",
				"Count": 1,
			},
			{
				"Name": "ControlCell",
				"Count": 1,
				"split": 0,
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 1,
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 7100 * 3.3
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"Uranium233Cell2",
	"Input":{
		"Items":[
			{
				"Name": "Uranium233Cell",
				"Count": 2,
			},
			{
				"Name": "ControlCell",
				"Count": 1,
				"split": 0,
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 2,
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": fission_fullpower / 2
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"Uranium233Cell3",
	"Input":{
		"Items":[
			{
				"Name": "Uranium233Cell",
				"Count": 4,
			},
			{
				"Name": "ControlCell",
				"Count": 1,
				"split": 0,
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 4,
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": fission_fullpower
	},
	"Ticks" : 2000,
})

recipes_chem.append({
	"Name":"AluminothermicChromiumDust",
	"Input":{
		"Items":[
			{
				"Name": "AluminiumDust",
				"Count": 1
			},
			{
				"Name": "ChromiumOxideDust",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ChromiumDust",
				"Count": 1
			}
		],
		
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10,
	},
	"Ticks" : 200,
})

recipes_chem.append({
	"Name":"CinnabarDust",
	"Input":{
		"Items":[
			{
				"Name": "CinnabarDust",
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Mercury",
				"Count": 1000
			},
			{
				"Name": "Sulfur",
				"Count": 1
			}
		],
		
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10,
	},
	"Ticks" : 200,
})
		
recipes_boiler.append({
	"Name": "Boiling",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 50
			}
		],
		
	},
	"ResourceInput":{
			"Name": "Heat",
			"Count": 110,
		},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Steam",
		"Count": 100,
		#"Capacity": 32000,
	},
	
	"Ticks" : 200,
	"Loss": 10,
})

recipes_steam_turbine.append({
	"Name": "Rotating",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Steam",
		"Count": 300
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Kinetic",
		"Count": 270
	},
	
	"Ticks" : 200,
	"Loss": 10,
})

recipes_generator.append({
	"Name": "Generating",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 270
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Electricity",
		"Count": 243
	},
	
	"Ticks" : 200,
	"Loss": 10,
})

recipes_electric_engine.append({
	"Name": "Rotating",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 55
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Kinetic",
		"Count": 50
	},
	
	"Loss": 10,
	
	"Ticks": 200,
})

recipes_industrial_electric_engine.append({
	"Name": "Rotating",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 55*50
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Kinetic",
		"Count": 50*50
	},
	
	"Loss": 10,
	
	"Ticks": 200,
})

recipes_compact_generator.append({
	"Name": "Rotating",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Electricity",
		"Count": 18
	},
	
	"Loss": 10,
	
	"Ticks": 200,
})

recipes_steam_engine.append({
	"Name": "Rotating",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Heat",
		"Count": 11
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Kinetic",
		"Count": 10
	},
	
	"Ticks": 200,
	"Loss": 10
})

recipes_oven.append({
	"Name": "CoalPieceToCoke",
	"Input":{
		"Items":[
			{
				"Name": "Coal",
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Coke",
				"Count": 10
			},
			{
				"Name": "Creosote",
				"Count": 250,
				"Capacity": 32000,
			},
		]
	},
	
	"Ticks": 2000,
})

recipes_oven.append({
	"Name": "LogToCoal",
	"Input":{
		"Items":[
			{
				"Name": "Log",
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Coal",
				"Count": 10
			},
			{
				"Name": "Creosote",
				"Count": 100,
				"Capacity": 32000,
			},
		]
	},
	
	"Ticks": 2000,
})

recipes_oven.append({
	"Name": "PlankToCoal",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Coal",
				"Count": 3
			},
			{
				"Name": "Creosote",
				"Count": 30,
				"Capacity": 32000,
			},
		]
	},
	
	"Ticks": 500,
})

recipes_oven.append({
	"Name": "OrgToCoal",
	"Input":{
		"Items":[
			{
				"Name": "Organics",
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Coal",
				"Count": 2
			},
			{
				"Name": "Creosote",
				"Count": 20,
				"Capacity": 32000,
			},
		]
	},
	
	"Ticks": 500,
})

recipes_oven.append({
	"Name": "Terracotta",
	"Input":{
		"Items":[
			{
				"Name": "Clay",
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Terracotta",
				"Count": 10
			},
		]
	},
	
	"Ticks": 1000,
})

for fuel_type, bonus in zip(["Coke"], [1.0]):
	recipes_blast_furnace.append({
		"Name": "IronIngotSmelting",
		"Input":{
			"Items":[
				{
					"Name": fuel_type,
					"Count": 15
				},
				{
					"Name": "IronIngot",
					"Count": 10
				},
			]
		},
		"Output":{
			"Items":[
				{
					"Name": "SteelIngot",
					"Count": 10
				}
			]
		},
		
		"Ticks" : 2000
	})

	recipes_blast_furnace.append({
		"Name": "IronDustSmelting",
		"Input":{
			"Items":[
				{
					"Name": fuel_type,
					"Count": 10
				},
				{
					"Name": "IronDust",
					"Count": 10
				},
			]
		},
		"Output":{
			"Items":[
				{
					"Name": "SteelIngot",
					"Count": 10
				}
			]
		},
		
		"Ticks" : 2000
	})
	
	recipes_blast_furnace.append({
		"Name": "IronOreDustSmelting",
		"Input":{
			"Items":[
				{
					"Name": fuel_type,
					"Count": 20
				},
				{
					"Name": "IronOreDust",
					"Count": 10
				},
			]
		},
		"Output":{
			"Items":[
				{
					"Name": "SteelIngot",
					"Count": 10
				}
			]
		},
		
		"Ticks" : 2000
	})
	
	
	recipes_blast_furnace.append({
		"Name": "IronOreDustSmelting" + fuel_type,
		"Input":{
			"Items":[
				{
					"Name": fuel_type,
					"Count": 1
				},
				{
					"Name": "SteelDust",
					"Count": 10
				},
			]
		},
		"Output":{
			"Items":[
				{
					"Name": "SteelIngot",
					"Count": 10
				}
			]
		},
		
		"Ticks" : 2000
	})

recipes_mixer.append({
	"Name": "ReinforcedConcrete",
	"Input":{
		"Items":[
			{
				"Name": "Concrete",
				"Count": 10
			},
			{
				"Name": "SteelParts",
				"Count": 8
			},
			{
				"Name": "Water",
				"Count": 100
			},
			
		]
	},
	"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcrete",
				"Count": 5
			}
		]
	},
	
	"Ticks" : 300,
})
recipes_mixer.append({
	"Name": "Concrete",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface",
				"Count": 5
			},
			{
				"Name": "Water",
				"Count": 100
			},
			
		]
	},
	"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "Concrete",
				"Count": 10
			}
		]
	},
	
	"Ticks" : 300,
})
recipes_mixer.append({
	"Name": "SSCraft",
	"Input":{
		"Items":[
			{
				"Name": "IronDust",
				"Count": 10
			},
			{
				"Name": "ChromiumDust",
				"Count": 3
			}
		]
	},
	"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "StainlessSteelDust",
				"Count": 10
			}
		]
	},
	
	"Ticks" : 400,
})
recipes_mixer.append({
	"Name": "SSCraft2",
	"Input":{
		"Items":[
			{
				"Name": "IronOreDust",
				"Count": 10
			},
			{
				"Name": "ChromiumDust",
				"Count": 3
			}
		]
	},
	"ResourceInput":{
				"Name": "Kinetic",
				"Count": 40
			},
	"Output":{
		"Items":[
			{
				"Name": "StainlessSteelDust",
				"Count": 10
			}
		]
	},
	
	"Ticks" : 500,
})

recipes_mixer.append({
	"Name": "PreparedTitaniumOxideCraft",
	"Input":{
		"Items":[
			{
				"Name": "TitaniumOxideDust",
				"Count": 1
			},
			{
				"Name": "Coke",
				"Count": 2
			},
		],
		
	},
	"ResourceInput":{
			"Name": "Kinetic",
			"Count": 10,
		},
	"Output":{
		"Items":[
			{
				"Name": "PreparedTitaniumOxideDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200,
	"Scaled": False,
})

#recipes_sep2.append({
#	"Name": "RareSeparating",
#	"Input":{
#		"Items":[
#			{
#				"Name": "RareEarthDust",
#				"Count": 10
#			},
#			
#		]
#	},
#	"ResourceInput":{
#		"Name": "Kinetic",
#		"Count": 50000
#	},
#	"Output":{
#		"Items": [
#			{
#				"Name": "RareMetalsDust",
#				"Count": 1
#			},
#			{
#				"Name": "YttriumDust",
#				"Count": 1
#			},
#			{
#				"Name": "LutetiumDust",
#				"Count": 1
#			},
#			{
#				"Name": "DysprosiumDust",
#				"Count": 1
#			}
#		]
#	},
#	
#	"Ticks": 1000,
#})

# recipes_sep2.append({
	# "Name": "OreWater",
	# "Input":{
		# "Items":[
			# {
				# "Name": "OreWater",
				# "Count": 1000
			# },
		# ]
	# },
	# "ResourceInput":{
		# "Name": "Kinetic",
		# "Count": 30
	# },
	# "Output":{
		# "Items": [
			# {
				# "Name": "Clay",
				# "Count": 1
			# },
		# ]
	# },
	
	# "Ticks": 200,
# })	

recipes_sep2.append({
	"Name": "PlutoniumDust",
	"Input":{
		"Items":[
			{
				"Name": "DepletedUraniumCell",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 30*90
	},
	"Output":{
		"Items": [
			{
				"Name":"Cell",
				"Count":1
			},
			{
				"Name": "PlutoniumDust",
				"Count": 1,
				"split":2
			}
		]
	},
	
	"Ticks": 400,
})	

recipes_sep2.append({
	"Name": "Granite",
	"Input":{
		"Items":[
			{
				"Name": "GraniteSurface",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 30*90
	},
	"Output":{
		"Items": [
			{
				"Name": "SandSurface",
				"Count": 1
			},
			{
				"Name": "TungstenOxideDust",
				"Count": 1,
				"split":10,
			},
		]
	},
	
	"Ticks": 40,
})	

recipes_sep2.append({
	"Name": "Stone",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 30
	},
	"Output":{
		"Items": [
			{
				"Name": "SandSurface",
				"Count": 1
			},
			{
				"Name": "AluminiumOxideDust",
				"Count": 1,
				"split":10,
			},
		]
	},
	
	"Ticks" : 100
})	

recipes_sep2.append({
	"Name": "Basalt",
	"Input":{
		"Items":[
			{
				"Name": "BasaltSurface",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 30*25
	},
	"Output":{
		"Items": [
			{
				"Name": "SandSurface",
				"Count": 1
			},
			{
				"Name": "AluminiumOxideDust",
				"Count": 1,
				"split": 5,
			},
			{
				"Name": "TitaniumOxideDust",
				"Count": 1,
				"split": 10,
			}
		]
	},
	
	"Ticks" : 40
})

recipes_sep2.append({
	"Name":"Sand",
	"Input":{
		"Items":[
			{
				"Name": "SandSurface",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 30
	},
	"Output":{
		"Items":[
			{
				"Name": "SiliconOxide",
				"Count": 1,
				"split": 2,
			}
		]
	},
	
	"Ticks" : 100
})

recipes_arc_furnace.append({
	"Name": "CopperOreDust",
	"Input":{
		"Items":[
			{
				"Name": "CopperOreDust",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 20,
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperIngot",
				"Count": 1
			}
		]
	},
	"Ticks" : 200
})

recipes_arc_furnace.append({
	"Name": "SandSurfaceSmelting",
	"Input":{
		"Items":[
			{
				"Name": "SandSurface",
				"Count": 1
			},
		],
		
	},
	"ResourceInput":{
			"Name": "Electricity",
			"Count": 20,
		},
	"Output":{
		"Items":[
			{
				"Name": "Glass",
				"Count": 1
			}
		]
	},
	"Ticks" : 100
})	

for material in materials:
	if "IsIngot" in material:
		if "SmeltLevel" in material and material["SmeltLevel"] <= 3:
			recipes_arc_furnace.append({
				"Name": material["Name"] + "Ingot",
				"Input":{
					"Items":[
						{
							"Name": material["Name"] + "Dust",
							"Count": 1
						},
					]
				},
				"ResourceInput":{
					"Name": "Electricity",
					"Count": 20 if material["Name"] != "StainlessSteel" else 100,
				},
				"Output":{
					"Items":[
						{
							"Name": material["Name"] + "Ingot",
							"Count": 1
						}
					]
				},
				"Tier": extract_tier(material),
				"Ticks" : 200
			})

recipes_macerator.append({
	"Name": "Pumpkin",
	"Input":{
		"Items":[
			{
				"Name": "Pumpkin",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Organics",
				"Count": 1
			}
		]
	},
	"Tier": 0,
	"Ticks" : 200
})

recipes_macerator.append({
	"Name": "Emerald",
	"Input":{
		"Items":[
			{
				"Name": "Emerald",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 50
	},
	"Output":{
		"Items":[
			{
				"Name": "EmeraldDust",
				"Count": 1
			}
		]
	},
	"Tier": 0,
	"Ticks" : 100
})

recipes_macerator.append({
	"Name": "MalachiteCrystal",
	"Input":{
		"Items":[
			{
				"Name": "MalachiteCrystal",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperOreDust",
				"Count": 2
			}
		]
	},
	"Tier": 0,
	"Ticks" : 200
})

recipes_macerator.append({
	"Name": "MalachiteCluster",
	"Input":{
		"Items":[
			{
				"Name": "MalachiteCluster",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperOreDust",
				"Count": 5
			}
		]
	},
	"Tier": 0,
	"Ticks" : 200
})

recipes_macerator.append({
	"Name": "RutileCrystal",
	"Input":{
		"Items":[
			{
				"Name": "RutileCrystal",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumOxideDust",
				"Count": 2
			}
		]
	},
	"Tier": 0,
	"Ticks" : 200
})

recipes_macerator.append({
	"Name": "CinnabarCrystal",
	"Input":{
		"Items":[
			{
				"Name": "CinnabarCrystal",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CinnabarDust",
				"Count": 2
			}
		]
	},
	"Tier": 0,
	"Ticks" : 200
})

recipes_macerator.append({
	"Name": "CinnabarCluster",
	"Input":{
		"Items":[
			{
				"Name": "CinnabarCluster",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CinnabarDust",
				"Count": 5
			}
		]
	},
	"Tier": 0,
	"Ticks" : 200
})

recipes_macerator.append({
	"Name": "UraniniteCrystal",
	"Input":{
		"Items":[
			{
				"Name": "UraniniteCrystal",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "UraniumDust",
				"Count": 2
			}
		]
	},
	"Tier": 0,
	"Ticks" : 200
})

recipes_macerator.append({
	"Name": "UraniniteCluster",
	"Input":{
		"Items":[
			{
				"Name": "UraniniteCluster",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "UraniumDust",
				"Count": 5
			},
			{
				"Name": "Uranium235Dust",
				"Count": 1
			}
		]
	},
	"Tier": 0,
	"Ticks" : 200
})
			
recipes_macerator.append({
	"Name": "GravelToSand",
	"Input":{
		"Items":[
			{
				"Name": "GravelSurface",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "SandSurface",
				"Count": 1
			}
		]
	},
	"Tier": 0,
	"Ticks" : 200
})

recipes_hammer.append({
	"Name": "StoneToGravel",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "GravelSurface",
				"Count": 1
			}
		]
	},
	"Tier": 0,
	"Ticks": 100,
})

recipes_pump.append({
	"Name":"Water",
	"Input":{
		"Items":[
		]
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Water",
		"Count": 600
	},
	"Ticks" : 6*20,
})

recipes_indu.append({
	"Name":"SpongeToIngot",
	"Input":{
		"Items":[
			{
				"Name": "TitaniumSponge",
				"Count": 1
			},
		],
		
	},
	"ResourceInput":{
				"Name": "Heat",
				"Count": 350,
			},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumIngot",
				"Count": 1
			},
		]
	},
	"Tier": 5,
	"Ticks" : 200,
})

recipes_indu.append({
	"Name":"SuperconductorDust",
	"Input":{
		"Items":[
			{
				"Name": "SuperconductorDust",
				"Count": 1
			},
		],
		
	},
	"ResourceInput":{
				"Name": "Heat",
				"Count": 100,
			},
	"Output":{
		"Items":[
			{
				"Name": "SuperconductorIngot",
				"Count": 1
			},
		]
	},
	"Tier": 5,
	"Ticks" : 200,
})
	
recipes_indu.append({
	"Name":"TDustToIngot",
	"Input":{
		"Items":[
			{
				"Name": "TitaniumDust",
				"Count": 1
			},
		],
		
	},
	"ResourceInput":{
				"Name": "Heat",
				"Count": 350,
			},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumIngot",
				"Count": 1
			},
		]
	},
	"Tier": 5,
	"Ticks" : 200,
})

recipes_indu.append({
	"Name":"HardMetalDustToIngot",
	"Input":{
		"Items":[
			{
				"Name": "HardMetalDust",
				"Count": 1
			},
		],
		
	},
	"ResourceInput":{
			"Name": "Heat",
			"Count": 900,
		},
	"Output":{
		"Items":[
			{
				"Name": "HotHardMetalIngot",
				"Count": 1
			},
		]
	},
	
	"Ticks" : 200,
})

recipes_sep.append({
	"Name":"SiliconOxide",
	"Input":{
		"Items":[
			{
				"Name": "SandSurface",
				"Count": 2
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "SiliconOxide",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 1000
})

recipes_mixer.append({
	"Name": "Organics",
	"Input":{
		"Items":[
			{
				"Name": "Organics",
				"Count": 1
			},
			{
				"Name": "Water",
				"Count": 500
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Biomass",
				"Count": 500
			}
		]
	},
	
	"Ticks": 200,
})

recipes_mixer.append({
	"Name": "HardMetalDust",
	"Input":{
		"Items":[
			{
				"Name": "TungstenCarbideDust",
				"Count": 4
			},
			{
				"Name": "CobaltDust",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "HardMetalDust",
				"Count": 5
			}
		]
	},
	
	"Ticks": 1000,
})

recipes_mixer.append({
	"Name": "SuperconductorDust",
	"Input":{
		"Items":[
			{
				"Name": "GoldDust",
				"Count": 3
			},
			{
				"Name": "RareEarthElement",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "SuperconductorDust",
				"Count": 3
			}
		]
	},
	
	"Ticks": 300,
})

recipes_electrolyzer.append({
	"Name":"AluminiumOxideDust",
	"Input":{
		"Items":[
			{
				"Name": "AluminiumOxideDust",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 50,
	},
	"Output":{
		"Items":[
			{
				"Name": "AluminiumDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200
})

recipes_electrolyzer.append({
	"Name":"EmeraldDust",
	"Input":{
		"Items":[
			{
				"Name": "EmeraldDust",
				"Count": 2
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 70,
	},
	"Output":{
		"Items":[
			{
				"Name": "BerylliumDust",
				"Count": 1
			},
			{
				"Name": "AluminiumOxideDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200
})

recipes_electrolyzer.append({
	"Name":"AluminiumOreDust",
	"Input":{
		"Items":[
			{
				"Name": "AluminiumOreDust",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 30,
	},
	"Output":{
		"Items":[
			{
				"Name": "AluminiumDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 500
})

recipes_electrolyzer.append({
	"Name":"Clay",
	"Input":{
		"Items":[
			{
				"Name": "Clay",
				"Count": 6
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 1300,
	},
	"Output":{
		"Items":[
			{
				"Name": "SandSurface",
				"Count": 4
			},{
				"Name": "AluminiumOxideDust",
				"Count": 1
			},{
				"Name": "SodiumDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 40
})

recipes_electrolyzer.append({
	"Name":"SandElectrolyze",
	"Input":{
		"Items":[
			{
				"Name": "SiliconOxide",
				"Count": 1
			}
		]
	},
	"ResourceInput":
	{
		"Name": "Electricity",
		"Count": 60
	},
	"Output":{
		"Items":[
			{
				"Name": "Silicon",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200
})

recipes_electrolyzer.append({
	"Name":"WaterElectrolyze",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 100
			}
			
		]
	},
	"ResourceInput":{
				"Name": "Electricity",
				"Count": 280 
			},
	"Output":{
		"Items":[
			{
				"Name": "Hydrogen",
				"Count": 100
			},
			{
				"Name": "Oxygen",
				"Count": 200
			}
		]
	},
	"Ticks" : 100
})

recipes_electrolyzer.append({
	"Name":"SaltElectrolyze",
	"Input":{
		"Items":[
			{
				"Name": "SaltDust",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10,
	},
	"Output":{
		"Items":[
			{
				"Name": "SodiumDust",
				"Count": 1
			},
			{
				"Name": "Chlorine",
				"Count": 1000
			}
			
		]
	},
	
	"Ticks" : 200
})

recipes_electrolyzer.append({
	"Name":"PotassiumChloride",
	"Input":{
		"Items":[
			{
				"Name": "PotassiumChlorideDust",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10,
	},
	"Output":{
		"Items":[
			{
				"Name": "PotassiumDust",
				"Count": 1
			},
			{
				"Name": "Chlorine",
				"Count": 1000
			}
			
		]
	},
	
	"Ticks" : 200
})

recipes_electrolyzer.append({
	"Name":"Borax",
	"Input":{
		"Items":[
			{
				"Name": "BoraxDust",
				"Count": 2
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 50,
	},
	"Output":{
		"Items":[
			{
				"Name": "SodiumDust",
				"Count": 1
			},
			{
				"Name": "BoronDust",
				"Count": 1
			}
			
		]
	},
	
	"Ticks" : 200
})

# wood

recipes_cutter.append({
	"Name": "LogCutting",
	"Input":{
		"Items":[
			{
				"Name": "Log",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 4
			}
		]
	},
	
	"Ticks" : 80,
})
recipes_cutter.append({
	"Name": "StoneLogCutting",
	"Input":{
		"Items":[
			{
				"Name": "StoneLog",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 4
			}
		]
	},
	
	"Ticks" : 200
})
recipes_cutter.append({
	"Name": "CircuitBoard",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CircuitBoard",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 80,
})
recipes_cutter.append({
	"Name":"StoneTiles",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface",
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "StoneTiles",
				"Count": 1
			}
		]
	},
	"Ticks" : 100
})
recipes_cutter.append({
	"Name":"DarkTiles",
	"Input":{
		"Items":[
			{
				"Name": "DarkStoneSurface",
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "DarkTiles",
				"Count": 1
			}
		]
	},
	"Ticks" : 100
})
recipes_cutter.append({
	"Name":"RedTiles",
	"Input":{
		"Items":[
			{
				"Name": "RedStoneSurface",
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "RedTiles",
				"Count": 1
			}
		]
	},
	"Ticks" : 100
})
recipes_cutter.append({
	"Name":"Bricks",
	"Input":{
		"Items":[
			{
				"Name": "StoneTiles",
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "Bricks",
				"Count": 1
			}
		]
	},
	"Ticks" : 100
})
recipes_cutter.append({
	"Name":"RedBricks",
	"Input":{
		"Items":[
			{
				"Name": "RedTiles",
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "RedBricks",
				"Count": 1
			}
		]
	},
	"Ticks" : 100
})
recipes_cutter.append({
	"Name":"DarkBricks",
	"Input":{
		"Items":[
			{
				"Name": "DarkTiles",
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "DarkBricks",
				"Count": 1
			}
		]
	},
	"Ticks" : 100
})
recipes_cutter.append({
	"Name":"TerracottaTiles",
	"Input":{
		"Items":[
			{
				"Name": "Terracotta",
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "TerracottaTiles",
				"Count": 1
			}
		]
	},
	"Ticks" : 100
})
recipes_cutter.append({
	"Name":"TerracottaBricks",
	"Input":{
		"Items":[
			{
				"Name": "TerracottaTiles",
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "TerracottaBricks",
				"Count": 1
			}
		]
	},
	"Ticks" : 100
})
recipes_cutter.append({
	"Name": "ConcreteTiles",
	"Input":{
		"Items":[
			{
				"Name": "Concrete",
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteTiles",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 100,
})
recipes_cutter.append({
	"Name": "ConcreteSmallTiles",
	"Input":{
		"Items":[
			{
				"Name": "ConcreteTiles",
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteSmallTiles",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 100,
})
recipes_cutter.append({
	"Name": "ConcreteBricks",
	"Input":{
		"Items":[
			{
				"Name": "ConcreteSmallTiles",
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteBricks",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 100,
})
recipes_cutter.append({
	"Name": "ReinforcedConcreteTiles",
	"Input":{
		"Items":[
			{
				"Name": "ReinforcedConcrete",
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteTiles",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 100,
})
recipes_cutter.append({
	"Name": "ReinforcedConcreteSmallTiles",
	"Input":{
		"Items":[
			{
				"Name": "ReinforcedConcreteTiles",
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteSmallTiles",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 100,
})
recipes_cutter.append({
	"Name": "ReinforcedConcreteBricks",
	"Input":{
		"Items":[
			{
				"Name": "ReinforcedConcreteSmallTiles",
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteBricks",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 100,
})
# burning

recipes_elfurn.append({
	"Name": "Working",
	"Input":{
		"Items":[
			
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 55,
	},
	"Output":{
		"Items":[
		],
		
	},
	"ResourceOutput":{
			"Name": "Heat",
			"Count": 50,
		},
	
	"Ticks" : 200,
	"Loss": 10,
})

recipes_coil.append({
	"Name": "Working",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 380
	},
	"Output":{
		"Items":[
		],
		
	},
	"ResourceOutput":{
			"Name": "Heat",
			"Count": 342,
		},
	"Ticks" : 200,
	"Loss" : 10
})

recipes_ferm.append({
	"Name": "MethaneFromBiomass",
	"Input":{
		"Items":[
			{
				"Name": "Biomass",
				"Count": 500
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Methane",
				"Count": 500
			}
		]
	},
	
	"Ticks" : 200
})

recipes_ferm.append({
	"Name": "MethaneFromPumpkin",
	"Input":{
		"Items":[
			{
				"Name": "Pumpkin",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Methane",
				"Count": 200
			}
		]
	},
	
	"Ticks" : 200
})

recipes_radiator.append({
	"Name": "Working",
	"Input":{
		"Items":[
		],
		
	},
	"ResourceInput":{
			"Name": "Heat",
			"Count": 500,
		},
	"Output":{
		"Items":[
		]
	},
	"Ticks" : 200,
})

recipes_solar.append({
	"Name": "Working",
	"Input":{
		"Items":[
		]
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Electricity",
		"Count": 50,
	},
	"Ticks" : 60,
})

recipes_riteg.append({
	"Name": "Working",
	"Input":{
		"Items":[
		]
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Heat",
		"Count": 500,
	},
	"Ticks" : 60,
})

recipes_chem.append({
	"Name": "MineralWater",
	"Input":{
		"Items":[
			{
				"Name": "MineralWater",
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "SaltDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 400,
})

recipes_chem.append({
	"Name": "MineralWater3",
	"Input":{
		"Items":[
			{
				"Name": "MineralWater",
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 60
	},
	"Output":{
		"Items":[
			{
				"Name": "BoraxDust",
				"Count": 1,
				"split": 10
			}
		]
	},
	
	"Ticks" : 100,
})

recipes_chem.append({
	"Name": "MineralWater2",
	"Input":{
		"Items":[
			{
				"Name": "MineralWater",
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "PotassiumChlorideDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 400,
})

recipes_chem.append({
	"Name": "TungstenCarbideDust",
	"Input":{
		"Items":[
			{
				"Name": "TungstenDust",
				"Count": 1
			},
			{
				"Name": "Coke",
				"Count": 2
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "TungstenCarbideDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200,
})

recipes_chem.append({
	"Name": "TitaniumTetrachloride",
	"Input":{
		"Items":[
			{
				"Name": "PreparedTitaniumOxideDust",
				"Count": 1
			},
			{
				"Name": "Chlorine",
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumTetrachloride",
				"Count": 1000
			}
		]
	},
	
	"Ticks" : 200,
	"Scaled": False,
})

recipes_chem.append({
	"Name": "TitaniumSponge",
	"Input":{
		"Items":[
			{
				"Name": "TitaniumTetrachloride",
				"Count": 1000
			},
			{
				"Name": "AluminiumDust",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumSponge",
				"Count": 1
			},
		],
	},
	
	"Ticks" : 200,
	"Scaled": False,
})

recipes_chem.append({
	"Name": "TungstenOxide",
	"Input":{
		"Items":[
			{
				"Name": "TungstenOxideDust",
				"Count": 1
			},
			{
				"Name": "Hydrogen",
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "TungstenDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200,
})

recipes_chem.append({
	"Name": "CobaltOxide",
	"Input":{
		"Items":[
			{
				"Name": "CobaltOxideDust",
				"Count": 1
			},
			{
				"Name": "Hydrogen",
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CobaltDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200,
	"Scaled": False,
})

for i in {"ProducerGas", "Methane", "Hydrogen", "Gasoline"}:
	recipes_gasturb.append({
		"Input":{
			"Items":[
				{
					"Name": i,
					"Count": 14 * 1000
				}
			]
		},
		"Output":{
			"Items":[
			]
		},
		"ResourceOutput":{
				"Name": "Kinetic",
				"Count": named_material(i)["Burnable"]["HeatPerTick"] * 14
			},
		"Ticks" : named_material(i)["Burnable"]["BurnTime"],
		"Name": i,
	})
	
	recipes_combustion.append({
		"Name": i,
		"Input":{
			"Items":[
				{
					"Name": i,
					"Count": 1000
				}			
			]
		},
		"Output":{
			"Items":[
			]
		},
		"ResourceOutput":{
				"Name": "Kinetic",
				"Count": named_material(i)["Burnable"]["HeatPerTick"]
			},
		
		"Ticks" : named_material(i)["Burnable"]["BurnTime"],
	})

recipes_pyro.append({
	"Name": "Coal",
	"Input":{
		"Items":[
			{
				"Name": "Coal",
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
				"Name": "Coke",
				"Count": 1
			},
			{
				"Name": "RawOil",
				"Count": 100
			},
			{
				"Name": "ProducerGas",
				"Count": 100
			},
			
		]
	},
	"Ticks" : 400
})

recipes_pyro.append({
	"Name": "CoalSteam",
	"Input":{
		"Items":[
			{
				"Name": "Coal",
				"Count": 1
			},
			{
				"Name": "Steam",
				"Count": 200
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
				"Name": "Coke",
				"Count": 1
			},
			{
				"Name": "ProducerGas",
				"Count": 500
			},
			
		]
	},
	"Ticks" : 400
})

recipes_pyro.append({
	"Name": "RawOil",
	"Input":{
		"Items":[
			{
				"Name": "RawOil",
				"Count": 2000
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Heat",
			"Count": 15
		},
	"Output":{
		"Items":[	
			{
				"Name": "HeavyOil",
				"Count": 500
			},
			{
				"Name": "Gasoline",
				"Count": 100
			},
{
				"Name": "Methane",
				"Count": 500
			},			
		]
	},
	
	"Ticks" : 200
})

recipes_pyro.append({
	"Name": "RawOilSteam",
	"Input":{
		"Items":[
			{
				"Name": "RawOil",
				"Count": 1000*5
			},
			{
				"Name": "Steam",
				"Count": 1000
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Heat",
			"Count": 100
		},
	"Output":{
		"Items":[	
			{
				"Name": "HeavyOil",
				"Count": 150*2
			},
			{
				"Name": "Gasoline",
				"Count": 400*2
			},
{
				"Name": "Methane",
				"Count": 500*2
			},			
		]
	},
	
	"Ticks" : 200
})

recipes_pyro.append({
	"Name": "HeavyOil",
	"Input":{
		"Items":[
			{
				"Name": "HeavyOil",
				"Count": 1000
			},
			{
				"Name": "Steam",
				"Count": 200
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
				"Name": "Gasoline",
				"Count": 750
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_pyro.append({
	"Name": "Gasoline",
	"Input":{
		"Items":[
			{
				"Name": "Gasoline",
				"Count": 1000
			},
			{
				"Name": "Steam",
				"Count": 200
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
				"Name": "Methane",
				"Count": 750
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_pyro.append({
	"Name": "Methane",
	"Input":{
		"Items":[
			{
				"Name": "Methane",
				"Count": 800*5
			},
			{
				"Name": "Steam",
				"Count": 200*20
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Heat",
			"Count": 100
		},
	"Output":{
		"Items":[	
			{
				"Name": "ProducerGas",
				"Count": 1000*5
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_pyro.append({
	"Name": "Methane2",
	"Input":{
		"Items":[
			{
				"Name": "Methane",
				"Count": 800*5
			}
		]
	},
	"ResourceInput":{
			"Name": "Heat",
			"Count": 50
		},
	"Output":{
		"Items":[	
			{
				"Name": "ProducerGas",
				"Count": 500*5
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_chem.append({
	"Name": "Ethylene",
	"Input":{
		"Items":[
			{
				"Name": "ProducerGas",
				"Count": 1000
			},
			{
				"Name": "Catalyst",
				"Count": 1,
				"split": 0,
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Ethylene",
				"Count": 1000,
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_chem.append({
	"Name": "Sulfur",
	"Input":{
		"Items":[
			{
				"Name": "HeavyOil",
				"Count": 150
			},
			{
				"Name": "Water",
				"Count": 250
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Sulfur",
				"Count": 1
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_chem.append({
	"Name": "SulfuricAcid",
	"Input":{
		"Items":[
			{
				"Name": "Sulfur",
				"Count": 1
			},
			{
				"Name": "Oxygen",
				"Count": 250
			},
			{
				"Name": "Water",
				"Count": 250
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "SulfuricAcid",
				"Count": 1000
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_chem.append({
	"Name": "Plastic1",
	"Input":{
		"Items":[
			{
				"Name": "Ethylene",
				"Count": 1000
			},
			{
				"Name": "Coal",
				"Count": 1
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Plastic",
				"Count": 1
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_chem.append({
	"Name": "Plastic2",
	"Input":{
		"Items":[
			{
				"Name": "Ethylene",
				"Count": 1000
			},
			{
				"Name": "HeavyOil",
				"Count": 150
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Plastic",
				"Count": 1
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_chem.append({
	"Name": "ProducerGas",
	"Input":{
		"Items":[
			{
				"Name": "ProducerGas",
				"Count": 1000
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Electricity",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Hydrogen",
				"Count": 750
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_filtering_unit.append({
	"Name": "OreWater",
	"Input":{
		"Items":[
			{
				"Name": "OreWater",
				"Count": 500
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Kinetic",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Clay",
				"Count": 1
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_filtering_unit.append({
	"Name": "OreWater2",
	"Input":{
		"Items":[
			{
				"Name": "OreWater",
				"Count": 500
			},
			{
				"Name": "FilteringCell",
				"Count": 1,
				"split": 10
			},
		]
	},
	"ResourceInput":{
			"Name": "Kinetic",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "AluminiumOreDust",
				"Count": 1,
				"split": 2
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_filtering_unit.append({
	"Name": "OreWater3",
	"Input":{
		"Items":[
			{
				"Name": "OreWater",
				"Count": 500
			},
			{
				"Name": "FilteringCell",
				"Count": 1,
				"split": 10
			},
		]
	},
	"ResourceInput":{
			"Name": "Kinetic",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "CopperOreDust",
				"Count": 1,
				"split": 2
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_filtering_unit.append({
	"Name": "OreWater4",
	"Input":{
		"Items":[
			{
				"Name": "OreWater",
				"Count": 500
			},
			{
				"Name": "FilteringCell",
				"Count": 1,
				"split": 10
			},
		]
	},
	"ResourceInput":{
			"Name": "Kinetic",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "UraniumOreDust",
				"Count": 1,
				"split": 2
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_filtering_unit.append({
	"Name": "OreWater5",
	"Input":{
		"Items":[
			{
				"Name": "OreWater",
				"Count": 500
			},
			{
				"Name": "FilteringCell",
				"Count": 1,
				"split": 10
			},
		]
	},
	"ResourceInput":{
			"Name": "Kinetic",
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "IronOreDust",
				"Count": 1,
				"split": 2
			},		
		]
	},
	
	"Ticks" : 200
})

for i in {"IronOreDust", "CopperOreDust"}:
	recipes_chemical_bath.append({
		"Name": i,
		"Input":{
			"Items":[
				{
					"Name": "Mercury",
					"Count": 500
				},
				{
					"Name": i,
					"Count": 2,
				},
			]
		},
		"ResourceInput":{
				"Name": "Kinetic",
				"Count": 10
			},
		"Output":{
			"Items":[	
				{
					"Name": "GoldDust",
					"Count": 1,
				},		
			]
		},
		
		"Ticks" : 200
	})
	
recipes_chemical_bath.append({
	"Name":"RareEarthElement",
	"Input":{
		"Items":[
			{
				"Name": "AluminiumOreDust",
				"Count": 10
			},
			{
				"Name": "SulfuricAcid",
				"Count": 1000
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 30
	},
	"Output":{
		"Items":[
			{
				"Name": "RareEarthElement",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 1000
})

recipes_chemical_bath.append({
	"Name":"CobaltOxideDust",
	"Input":{
		"Items":[
			{
				"Name": "IronOreDust",
				"Count": 10
			},
			{
				"Name": "SulfuricAcid",
				"Count": 1000
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 30
	},
	"Output":{
		"Items":[
			{
				"Name": "CobaltOxideDust",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 1000
})

recipes_freezer.append({
	"Name":"HotHardmetalIngot",
	"Input":{
		"Items":[
			{
				"Name": "HotHardMetalIngot",
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "HardMetalIngot",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200
})

recipes_freezer.append({
	"Name":"HotNeutroniumIngot",
	"Input":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot",
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic",
		"Count": 1000
	},
	"Output":{
		"Items":[
			{
				"Name": "NeutroniumIngot",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200
})

recipes_computer.append({
	"Name":"Computations",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Computations",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 40
})

recipes_q_computer.append({
	"Name":"QuantumComputations",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "Computations",
				"Count": 40
			}
		]
	},
	
	"Ticks" : 40
})

recipes_portal.append({
	"Name":"Ping",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Electricity",
		"Count": 2 * fission_fullpower*0.9*0.9
	},
	"Output":{
		"Items":[
			{
				"Name": "MothershipPing",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 1000
})

append_recipe_hand_press({
	"Name": "Column",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Column",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

append_recipe_hand_press({
	"Name": "FluetedColumn",
	"Input":{
		"Items":[
			{
				"Name": "Column",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "FluetedColumn",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

append_recipe_hand_press({
	"Name":"GlassBlock",
	"Input":{
		"Items":[
			{
				"Name": "Glass",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "GlassBlock",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 10
})

append_recipe_hand_press({
	"Name":"PlasticBlock",
	"Input":{
		"Items":[
			{
				"Name": "Plastic",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "PlasticBlock",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 10
})

append_recipe_hand_press({
	"Name":"DangerBlock",
	"Input":{
		"Items":[
			{
				"Name": "Concrete",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DangerBlock",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

append_recipe_hand_press({
	"Name": "BasicPlatform",
	"Input":{
		"Items":[
			{
				"Name": "SandSurface",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "BasicPlatform",
				"Count": 1
			}
		]
	},
	"Ticks" : 10
})

append_recipe_hand_press({
	"Name":"RustyCopperCasing",
	"Input":{
		"Items":[
			{
				"Name": "CopperCasing",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "RustyCopperCasing",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

append_recipe_hand_press({
	"Name":"RustyIronCasing",
	"Input":{
		"Items":[
			{
				"Name": "SteelCasing",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "RustyIronCasing",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

for i in ["Circuit", "AdvancedCircuit", "Processor", "QuantumCircuit", "QuantumProcessor", "QuantumBrain"]:
	recipes_computer.append(
	{
		"Name": i,
		"Input":{
			"Items":[
				{
					"Name": i,
					"Count": 1
				}
			]
		},
		"ResourceInput":{
			"Name": "Electricity",
			"Count": 40
		},
		"Output":{
			"Items":[
				{
					"Name": i,
					"Count": 1
				}
			]
		},
		
		"Ticks" : 40
	})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Multitool",
	"Recipes": recipes_wrench
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "BlastFurnace",
	"Recipes": recipes_blast_furnace
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Oven",
	"Recipes": recipes_oven
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Smelter",
	"Recipes": recipes_smelter
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Macerator",
	"Recipes": recipes_macerator
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Boiler",
	"Recipes": recipes_boiler
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Generator",
	"Recipes": recipes_generator
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "ElectricEngine",
	"Recipes": recipes_electric_engine
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "StirlingEngine",
	"Recipes": recipes_steam_engine
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Pump",
	"Recipes": recipes_pump
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Separator",
	"Recipes": recipes_sep
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "IndustrialSeparator",
	"Recipes": recipes_sep2
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Press",
	"Recipes": recipes_press
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "ArcSmelter",
	"Recipes": recipes_arc_furnace
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "SteamTurbine",
	"Recipes": recipes_steam_turbine
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Electrolyzer",
	"Recipes": recipes_electrolyzer
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "CuttingMachine",
	"Recipes": recipes_cutter
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Furnace",
	"Recipes": recipes_furnace
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "ElectricFurnace",
	"Recipes": recipes_elfurn
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Fermenter",
	"Recipes": recipes_ferm
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "MultitoolRobotArm",
	"Recipes": recipes_toolarm
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "AutomaticHammer",
	"Recipes": recipes_hammer
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Mixer",
	"Recipes": recipes_mixer
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Radiator",
	"Recipes": recipes_radiator
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "SolarPanel",
	"Recipes": recipes_solar
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "ChemReactor",
	"Recipes": recipes_chem
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "InductionCoil",
	"Recipes": recipes_coil
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "IndustrialSmelter",
	"Recipes": recipes_indu
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "HeatExchanger",
	"Recipes": recipes_exch
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "InverseHeatExchanger",
	"Recipes": recipes_iexch
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Freezer",
	"Recipes": recipes_freezer
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "CombustionEngine",
	"Recipes": recipes_combustion
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "PyrolysisUnit",
	"Recipes": recipes_pyro
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Computer",
	"Recipes": recipes_computer
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "CompactGenerator",
	"Recipes": recipes_compact_generator
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "FissionReactor",
	"Recipes": recipes_fission
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "AutomaticFarm",
	"Recipes": recipes_farm
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "AtmosphericCondenser",
	"Recipes": recipes_condens
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Assembler",
	"Recipes": recipes_assembler
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "GasTurbine",
	"Recipes": recipes_gasturb
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "FilteringUnit",
	"Recipes": recipes_filtering_unit
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Portal",
	"Recipes": recipes_portal
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "ChemicalBath",
	"Recipes": recipes_chemical_bath
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Riteg",
	"Recipes": recipes_riteg
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "IndustrialSteamTurbine",
	"Recipes": recipes_industrial_steam_turbine
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "FusionReactor",
	"Recipes": recipes_fusion_reactor
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "IndustrialBoiler",
	"Recipes": recipes_industrial_boiler
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "IndustrialElectricEngine",
	"Recipes": recipes_industrial_electric_engine
})

objects_array.append({ "Class": recipe_dictionary,
	"Name": "Hand",
	"Recipes": recipes_hand
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/misc.json", data);