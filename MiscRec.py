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
recipes_industrial_generator = []
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

recipes_industrial_chemreactor = []

recipes_chemical_bath = []

recipes_centrifuge = []

recipes_riteg = []
	
recipes_industrial_steam_turbine = []	

recipes_fusion_reactor = []

recipes_industrial_boiler = []

recipes_industrial_electric_engine = []

recipes_portal = []

recipes_hand = []

recipes_kinetic_heater = []

oil_crack = []

def append_recipe(recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]

	level = extract_tier(recipe["Output"]["Items"][0]["Name"]) + 1
	
	dec_recipe = copy.deepcopy(recipe)

	recipes_hand.append(recipe)
	
	output = copy.deepcopy(dec_recipe["Input"])
	
	dec_recipe["Ticks"] = max(min(item_count * 10, 400), 20);
	dec_recipe["ResourceInput"] = { "Name": "Electricity" + static_item, "Count": 20 * level }
	recipes_assembler.append(dec_recipe)

def append_recipe_hand_press(recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]
	
	dec_recipe = copy.deepcopy(recipe)

	recipes_hand.append(recipe)
	
	output = copy.deepcopy(dec_recipe["Input"])
	
	dec_recipe["Ticks"] = 60;
	dec_recipe["ResourceInput"] = { "Name": "Kinetic" + static_item, "Count": 100 }
	recipes_press.append(dec_recipe)		

# wrenching

recipes_industrial_steam_turbine.append({
	"Name": "Rotating",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Steam" + static_item,
		"Count": fission_fullpower * 0.9
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Kinetic" + static_item,
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
				"Name": "Water" + static_item,
				"Count": 2000
			},
		]
	},
	"ResourceInput":{
		"Name":"Heat" + static_item,
		"Count": fission_fullpower
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name":"Steam" + static_item,
		"Count": fission_fullpower * 0.9
	},
	"Ticks" : 200,
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumIngot1",
	"Input":{
		"Items":[
			{
				"Name": "ProducerGas" + static_item,
				"Count": 1000
			}
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": fission_fullpower*0.9*0.9
	},
	"Output":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot" + static_item,
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
				"Name": "ProducerGas" + static_item,
				"Count": 3000
			}
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 2 * fission_fullpower*0.9*0.9
	},
	"Output":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot" + static_item,
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
				"Name": "UltimateCatalyst" + static_item,
				"Count": 1,
				"Probability":0
			}
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": fission_fullpower*0.9*0.9
	},
	"Output":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot" + static_item,
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
				"Name": "UltimateCatalyst" + static_item,
				"Count": 3,
				"Probability":0
			}
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 2 * fission_fullpower*0.9*0.9
	},
	"Output":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot" + static_item,
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
				"Name": "SandSurface" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput": {
		"Name": "Heat" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Glass" + static_item,
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
						"Name": one["Name"] + static_item,
						"Count": 1
					}
				]
			},
			"Output":{
				"Items":[
					{
						"Name": one["Name"] + static_item,
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
				"Name": "StainlessSteelPlate" + static_item,
				"Count": 1
			},
			{
				"Name": "StainlessSteelParts" + static_item,
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Cell" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 200,
	
})

recipes_assembler.append({
	"Name":"Cell2",
	"Input":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Cell" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 200*3,
	"ResourceInput": { "Name": "Electricity" + static_item, "Count": 10 }
})

append_recipe({
	"Name":"UraniumCell",
	"Input":{
		"Items":[
			{
				"Name": "Uranium235Dust" + static_item,
				"Count": 3
			},
			{
				"Name": "UraniumDust" + static_item,
				"Count": 20
			},
			{
				"Name": "Cell" + static_item,
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "UraniumCell" + static_item,
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
				"Name": "ThoriumDust" + static_item,
				"Count": 20
			},
			{
				"Name": "Cell" + static_item,
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ThoriumCell" + static_item,
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
				"Name": "Uranium233Dust" + static_item,
				"Count": 3
			},
			{
				"Name": "Cell" + static_item,
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Uranium233Cell" + static_item,
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
				"Name": "PlutoniumDust" + static_item,
				"Count": 3
			},
			{
				"Name": "Cell" + static_item,
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "PlutoniumCell" + static_item,
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
				"Name": "Coal" + static_item,
				"Count": 10
			},
			{
				"Name": "Cell" + static_item,
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "FilteringCell" + static_item,
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
				"Name": "CircuitBoard" + static_item,
				"Count": 1
			},
			{
				"Name": "CopperWire" + static_item,
				"Count": 6
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Circuit" + static_item,
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
				"Name": "Silicon" + static_item,
				"Count": 1
			},	
			{
				"Name": "Circuit" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 30
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedCircuit" + static_item,
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
				"Name": "Silicon" + static_item,
				"Count": 1
			},	
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "SiliconWafer" + static_item,
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
				"Name": "SiliconWafer" + static_item,
				"Count": 1
			},	
			{
				"Name": "AdvancedCircuit" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 80
	},
	"Output":{
		"Items":[
			{
				"Name": "Processor" + static_item,
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
				"Name": "QuantumProcessor" + static_item,
				"Count": 2
			},
			{
				"Name": "UltimateCatalyst" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 1000
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumBrain" + static_item,
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
				"Name": "Cell" + static_item,
				"Count": 1
			},	
			{
				"Name": "GoldWire" + static_item,
				"Count": 10
			},	
			{
				"Name": "Coal" + static_item,
				"Count": 4
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Catalyst" + static_item,
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
				"Name": "Cell" + static_item,
				"Count": 1
			},	
			{
				"Name": "NeutroniumParts" + static_item,
				"Count": 8
			},	
			{
				"Name": "Coke" + static_item,
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "UltimateCatalyst" + static_item,
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
				"Name": "Plastic" + static_item,
				"Count": 1
			},
			{
				"Name": "GoldWire" + static_item,
				"Count": 3
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedCircuitBoard" + static_item,
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
				"Name": "SiliconWafer" + static_item,
				"Count": 1
			},	
			{
				"Name": "AdvancedCircuitBoard" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 80
	},
	"Output":{
		"Items":[
			{
				"Name": "Processor" + static_item,
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
				"Name": "RareEarthElement" + static_item,
				"Count": 1
			},	
			{
				"Name": "CopperParts" + static_item,
				"Count": 2
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 1000
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumCore" + static_item,
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
				"Name": "QuantumCore" + static_item,
				"Count": 2
			},	
			{
				"Name": "AdvancedCircuitBoard" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 1000 / 7
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumCircuit" + static_item,
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
				"Name": "QuantumCircuit" + static_item,
				"Count": 1
			},	
			{
				"Name": "Processor" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 2000 / 13
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumProcessor" + static_item,
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
				"Name": "CopperIngot" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperWire" + static_item,
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
				"Name": "SuperconductorIngot" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "SuperconductorWire" + static_item,
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
				"Name": "SulfuricAcid" + static_item,
				"Count": 100
			},
			{
				"Name": "CopperParts" + static_item,
				"Count": 1
			},
			{
				"Name": "StainlessSteelPlate" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Battery" + static_item,
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
				"Name": "GoldIngot" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "GoldWire" + static_item,
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
				"Name": "Cell" + static_item,
				"Count": 1
			},
			{
				"Name": "BerylliumDust" + static_item,
				"Count": 3
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ReflectorCell" + static_item,
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
				"Name": "Cell" + static_item,
				"Count": 1
			},
			{
				"Name": "BoronDust" + static_item,
				"Count": 3
			},
		]
	},
	"ResourceInput": {
		"Name": "Electricity" + static_item,
		"Count": 1000 / 9
	},
	"Output":{
		"Items":[
			{
				"Name": "ControlCell" + static_item,
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
				"Name": "Water" + static_item,
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
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "Oxygen" + static_item,
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
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "Nitrogen" + static_item,
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
		"Name": "Kinetic" + static_item,
		"Count": 40
	},
	"Output":{
		"Items":[
			{
				"Name": "Helium" + static_item,
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
		"Name": "Kinetic" + static_item,
		"Count": 40
	},
	"Output":{
		"Items":[
			{
				"Name": "Methane" + static_item,
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
		"Name": "Kinetic" + static_item,
		"Count": 40
	},
	"Output":{
		"Items":[
			{
				"Name": "Hydrogen" + static_item,
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
				"Name": "Water" + static_item,
				"Count": 625
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Log" + static_item,
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
				"Name": "Water" + static_item,
				"Count": 625
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Pumpkin" + static_item,
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
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "PlutoniumDust" + static_item,
				"Count": 1,
				"Probability": 0.1,
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 100
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"UraniumCell",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 7100
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"UraniumCell2",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell" + static_item,
				"Count": 2
			},
			{
				"Name": "ControlCell" + static_item,
				"Count": 1,
				"Probability": 0,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 2
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 7100 * 2.2
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"UraniumCell3",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell" + static_item,
				"Count": 3
			},
			{
				"Name": "ControlCell" + static_item,
				"Count": 1,
				"Probability": 0,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 3
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 7100 * 3.3
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"UraniumCell4",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell" + static_item,
				"Count": 3
			},
			{
				"Name": "ControlCell" + static_item,
				"Count": 5,
				"Probability": 0,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 3
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 7100 * 3.3 / 2
	},
	"Ticks" : 2000 * 2,
})

recipes_fission.append({
	"Name":"ControlCell3",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell" + static_item,
				"Count": 1
			},
			{
				"Name": "ControlCell" + static_item,
				"Count": 3,
				"Probability": 0,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 7100 / 4
	},
	"Ticks" : 8000 * .9 * .9,
})

recipes_fission.append({
	"Name":"ThoriumCell",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell" + static_item,
				"Count": 3,
			},
			{
				"Name": "ReflectorCell" + static_item,
				"Count": 1,
				"Probability": 0,
			},
			{
				"Name": "ThoriumCell" + static_item,
				"Count": 2,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 3
			},
			{
				"Name": "Uranium233Cell" + static_item,
				"Count": 2,
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 200
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"PlutoniumCell",
	"Input":{
		"Items":[
			{
				"Name": "PlutoniumCell" + static_item,
				"Count": 1,
			},
			{
				"Name": "ReflectorCell" + static_item,
				"Count": 1,
				"Probability": 0,
			},
			{
				"Name": "ThoriumCell" + static_item,
				"Count": 3,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Uranium233Cell" + static_item,
				"Count": 3,
			},
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 200
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"PlutoniumCell2",
	"Input":{
		"Items":[
			{
				"Name": "PlutoniumCell" + static_item,
				"Count": 1,
			},
			{
				"Name": "ReflectorCell" + static_item,
				"Count": 2,
				"Probability": 0,
			},
			{
				"Name": "ThoriumCell" + static_item,
				"Count": 6,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Uranium233Cell" + static_item,
				"Count": 6,
			},
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 200
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"ControlCell",
	"Input":{
		"Items":[
			{
				"Name": "UraniumCell" + static_item,
				"Count": 1
			},
			{
				"Name": "ControlCell" + static_item,
				"Count": 1,
				"Probability": 0,
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 7100 / 2
	},
	"Ticks" : 4000 * 0.9,
})

recipes_fission.append({
	"Name":"Uranium233Cell",
	"Input":{
		"Items":[
			{
				"Name": "Uranium233Cell" + static_item,
				"Count": 1,
			},
			{
				"Name": "ControlCell" + static_item,
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 1,
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 7100 * 3.3
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"Uranium233Cell2",
	"Input":{
		"Items":[
			{
				"Name": "Uranium233Cell" + static_item,
				"Count": 2,
			},
			{
				"Name": "ControlCell" + static_item,
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 2,
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": fission_fullpower / 2
	},
	"Ticks" : 2000,
})

recipes_fission.append({
	"Name":"Uranium233Cell3",
	"Input":{
		"Items":[
			{
				"Name": "Uranium233Cell" + static_item,
				"Count": 4,
			},
			{
				"Name": "ControlCell" + static_item,
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 4,
			}
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": fission_fullpower
	},
	"Ticks" : 2000,
})

recipes_chem.append({
	"Name":"AluminothermicChromiumDust",
	"Input":{
		"Items":[
			{
				"Name": "AluminiumDust" + static_item,
				"Count": 1
			},
			{
				"Name": "ChromiumOxideDust" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ChromiumDust" + static_item,
				"Count": 1
			}
		],
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10,
	},
	"Ticks" : 200,
})

recipes_chem.append({
	"Name":"CinnabarDust",
	"Input":{
		"Items":[
			{
				"Name": "CinnabarDust" + static_item,
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Mercury" + static_item,
				"Count": 1000
			},
			{
				"Name": "Sulfur" + static_item,
				"Count": 1
			}
		],
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10,
	},
	"Ticks" : 200,
})
recipes_boiler.append({
	"Name": "Boiling",
	"Input":{
		"Items":[
			{
				"Name": "Water" + static_item,
				"Count": 50
			}
		],
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 110,
		},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Steam" + static_item,
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
		"Name": "Steam" + static_item,
		"Count": 300
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Kinetic" + static_item,
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
		"Name": "Kinetic" + static_item,
		"Count": 270
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Electricity" + static_item,
		"Count": 243
	},
	
	"Ticks" : 200,
	"Loss": 10,
})

recipes_industrial_generator.append({
	"Name": "Generating",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 270*20
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Electricity" + static_item,
		"Count": 243*20
	},
	
	"Ticks" : 200,
	"Loss": 10,
})

recipes_kinetic_heater.append({
	"Name": "Generating",
	"Input":{
		"Items":[
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Heat" + static_item,
		"Count": 9
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
		"Name": "Electricity" + static_item,
		"Count": 55
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Kinetic" + static_item,
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
		"Name": "Electricity" + static_item,
		"Count": 55*50
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Kinetic" + static_item,
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
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Electricity" + static_item,
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
		"Name": "Heat" + static_item,
		"Count": 11
	},
	"Output":{
		"Items":[
		]
	},
	"ResourceOutput":{
		"Name": "Kinetic" + static_item,
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
				"Name": "Coal" + static_item,
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Coke" + static_item,
				"Count": 10
			},
			{
				"Name": "Creosote" + static_item,
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
				"Name": "Log" + static_item,
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Coal" + static_item,
				"Count": 10
			},
			{
				"Name": "Creosote" + static_item,
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
				"Name": "Plank" + static_item,
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Coal" + static_item,
				"Count": 3
			},
			{
				"Name": "Creosote" + static_item,
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
				"Name": "Organics" + static_item,
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Coal" + static_item,
				"Count": 2
			},
			{
				"Name": "Creosote" + static_item,
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
				"Name": "Clay" + static_item,
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Terracotta" + static_item,
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
					"Name": fuel_type + static_item,
					"Count": 15
				},
				{
					"Name": "IronIngot" + static_item,
					"Count": 10
				},
			]
		},
		"Output":{
			"Items":[
				{
					"Name": "SteelIngot" + static_item,
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
					"Name": fuel_type + static_item,
					"Count": 10
				},
				{
					"Name": "IronDust" + static_item,
					"Count": 10
				},
			]
		},
		"Output":{
			"Items":[
				{
					"Name": "SteelIngot" + static_item,
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
					"Name": fuel_type + static_item,
					"Count": 20
				},
				{
					"Name": "IronOreDust" + static_item,
					"Count": 10
				},
			]
		},
		"Output":{
			"Items":[
				{
					"Name": "SteelIngot" + static_item,
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
					"Name": fuel_type + static_item,
					"Count": 1
				},
				{
					"Name": "SteelDust" + static_item,
					"Count": 10
				},
			]
		},
		"Output":{
			"Items":[
				{
					"Name": "SteelIngot" + static_item,
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
				"Name": "Concrete" + static_item,
				"Count": 10
			},
			{
				"Name": "SteelParts" + static_item,
				"Count": 8
			},
			{
				"Name": "Water" + static_item,
				"Count": 100
			},
			
		]
	},
	"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcrete" + static_item,
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
				"Name": "StoneSurface" + static_item,
				"Count": 5
			},
			{
				"Name": "Water" + static_item,
				"Count": 100
			},
			
		]
	},
	"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "Concrete" + static_item,
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
				"Name": "IronDust" + static_item,
				"Count": 10
			},
			{
				"Name": "ChromiumDust" + static_item,
				"Count": 3
			}
		]
	},
	"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "StainlessSteelDust" + static_item,
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
				"Name": "IronOreDust" + static_item,
				"Count": 10
			},
			{
				"Name": "ChromiumDust" + static_item,
				"Count": 3
			}
		]
	},
	"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 40
			},
	"Output":{
		"Items":[
			{
				"Name": "StainlessSteelDust" + static_item,
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
				"Name": "TitaniumOxideDust" + static_item,
				"Count": 1
			},
			{
				"Name": "Coke" + static_item,
				"Count": 2
			},
		],
	},
	"ResourceInput":{
			"Name": "Kinetic" + static_item,
			"Count": 10,
		},
	"Output":{
		"Items":[
			{
				"Name": "PreparedTitaniumOxideDust" + static_item,
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
#				"Name": "RareEarthDust" + static_item,
#				"Count": 10
#			},
#			
#		]
#	},
#	"ResourceInput":{
#		"Name": "Kinetic" + static_item,
#		"Count": 50000
#	},
#	"Output":{
#		"Items": [
#			{
#				"Name": "RareMetalsDust" + static_item,
#				"Count": 1
#			},
#			{
#				"Name": "YttriumDust" + static_item,
#				"Count": 1
#			},
#			{
#				"Name": "LutetiumDust" + static_item,
#				"Count": 1
#			},
#			{
#				"Name": "DysprosiumDust" + static_item,
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
				# "Name": "OreWater" + static_item,
				# "Count": 1000
			# },
		# ]
	# },
	# "ResourceInput":{
		# "Name": "Kinetic" + static_item,
		# "Count": 30
	# },
	# "Output":{
		# "Items": [
			# {
				# "Name": "Clay" + static_item,
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
				"Name": "DepletedUraniumCell" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 30*90
	},
	"Output":{
		"Items": [
			{
				"Name":"Cell"+static_item,
				"Count":1
			},
			{
				"Name": "PlutoniumDust" + static_item,
				"Count": 1,
				"Probability":0.5
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
				"Name": "GraniteSurface" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 30*90
	},
	"Output":{
		"Items": [
			{
				"Name": "SandSurface" + static_item,
				"Count": 1
			},
			{
				"Name": "TungstenOxideDust" + static_item,
				"Count": 1,
				"Probability":0.1,
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
				"Name": "StoneSurface" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 30
	},
	"Output":{
		"Items": [
			{
				"Name": "SandSurface" + static_item,
				"Count": 1
			},
			{
				"Name": "AluminiumOxideDust" + static_item,
				"Count": 1,
				"Probability":0.1,
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
				"Name": "BasaltSurface" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 30*25
	},
	"Output":{
		"Items": [
			{
				"Name": "SandSurface" + static_item,
				"Count": 1
			},
			{
				"Name": "AluminiumOxideDust" + static_item,
				"Count": 1,
				"Probability": 0.2,
			},
			{
				"Name": "TitaniumOxideDust" + static_item,
				"Count": 1,
				"Probability": 0.1,
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
				"Name": "SandSurface" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 30
	},
	"Output":{
		"Items":[
			{
				"Name": "SiliconOxide" + static_item,
				"Count": 1,
				"Probability": 0.5,
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
				"Name": "CopperOreDust" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 20,
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperIngot" + static_item,
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
				"Name": "SandSurface" + static_item,
				"Count": 1
			},
		],
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 20,
		},
	"Output":{
		"Items":[
			{
				"Name": "Glass" + static_item,
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
							"Name": material["Name"] + "Dust" + static_item,
							"Count": 1
						},
					]
				},
				"ResourceInput":{
					"Name": "Electricity" + static_item,
					"Count": 20 if material["Name"] != "StainlessSteel" else 100,
				},
				"Output":{
					"Items":[
						{
							"Name": material["Name"] + "Ingot" + static_item,
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
				"Name": "Pumpkin" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Organics" + static_item,
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
				"Name": "Emerald" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 50
	},
	"Output":{
		"Items":[
			{
				"Name": "EmeraldDust" + static_item,
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
				"Name": "MalachiteCrystal" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperOreDust" + static_item,
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
				"Name": "MalachiteCluster" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperOreDust" + static_item,
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
				"Name": "RutileCrystal" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumOxideDust" + static_item,
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
				"Name": "CinnabarCrystal" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CinnabarDust" + static_item,
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
				"Name": "CinnabarCluster" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CinnabarDust" + static_item,
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
				"Name": "UraniniteCrystal" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "UraniumDust" + static_item,
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
				"Name": "UraniniteCluster" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "UraniumDust" + static_item,
				"Count": 5
			},
			{
				"Name": "Uranium235Dust" + static_item,
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
				"Name": "GravelSurface" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "SandSurface" + static_item,
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
				"Name": "StoneSurface" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "GravelSurface" + static_item,
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
		"Name": "Water" + static_item,
		"Count": 600
	},
	"Ticks" : 6*20,
})

recipes_indu.append({
	"Name":"SpongeToIngot",
	"Input":{
		"Items":[
			{
				"Name": "TitaniumSponge" + static_item,
				"Count": 1
			},
		],
	},
	"ResourceInput":{
				"Name": "Heat" + static_item,
				"Count": 350,
			},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumIngot" + static_item,
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
				"Name": "SuperconductorDust" + static_item,
				"Count": 1
			},
		],
	},
	"ResourceInput":{
				"Name": "Heat" + static_item,
				"Count": 100,
			},
	"Output":{
		"Items":[
			{
				"Name": "SuperconductorIngot" + static_item,
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
				"Name": "TitaniumDust" + static_item,
				"Count": 1
			},
		],
	},
	"ResourceInput":{
				"Name": "Heat" + static_item,
				"Count": 350,
			},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumIngot" + static_item,
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
				"Name": "HardMetalDust" + static_item,
				"Count": 1
			},
		],
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 900,
		},
	"Output":{
		"Items":[
			{
				"Name": "HotHardMetalIngot" + static_item,
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
				"Name": "SandSurface" + static_item,
				"Count": 2
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "SiliconOxide" + static_item,
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
				"Name": "Organics" + static_item,
				"Count": 1
			},
			{
				"Name": "Water" + static_item,
				"Count": 500
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Biomass" + static_item,
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
				"Name": "TungstenCarbideDust" + static_item,
				"Count": 4
			},
			{
				"Name": "CobaltDust" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "HardMetalDust" + static_item,
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
				"Name": "GoldDust" + static_item,
				"Count": 3
			},
			{
				"Name": "RareEarthElement" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "SuperconductorDust" + static_item,
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
				"Name": "AluminiumOxideDust" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 50,
	},
	"Output":{
		"Items":[
			{
				"Name": "AluminiumDust" + static_item,
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
				"Name": "EmeraldDust" + static_item,
				"Count": 2
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 70,
	},
	"Output":{
		"Items":[
			{
				"Name": "BerylliumDust" + static_item,
				"Count": 1
			},
			{
				"Name": "AluminiumOxideDust" + static_item,
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
				"Name": "AluminiumOreDust" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 30,
	},
	"Output":{
		"Items":[
			{
				"Name": "AluminiumDust" + static_item,
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
				"Name": "Clay" + static_item,
				"Count": 6
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 1300,
	},
	"Output":{
		"Items":[
			{
				"Name": "SandSurface" + static_item,
				"Count": 4
			},{
				"Name": "AluminiumOxideDust" + static_item,
				"Count": 1
			},{
				"Name": "SodiumDust" + static_item,
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
				"Name": "SiliconOxide" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":
	{
		"Name": "Electricity" + static_item,
		"Count": 60
	},
	"Output":{
		"Items":[
			{
				"Name": "Silicon" + static_item,
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
				"Name": "Water" + static_item,
				"Count": 100
			}
			
		]
	},
	"ResourceInput":{
				"Name": "Electricity" + static_item,
				"Count": 280 
			},
	"Output":{
		"Items":[
			{
				"Name": "Hydrogen" + static_item,
				"Count": 100
			},
			{
				"Name": "Oxygen" + static_item,
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
				"Name": "SaltDust" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10,
	},
	"Output":{
		"Items":[
			{
				"Name": "SodiumDust" + static_item,
				"Count": 1
			},
			{
				"Name": "Chlorine" + static_item,
				"Count": 1000
			}
			
		]
	},
	
	"Ticks" : 200
})

recipes_electrolyzer.append({
	"Name":"MineralWater",
	"Input":{
		"Items":[
			{
				"Name": "MineralWater" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10,
	},
	"Output":{
		"Items":[
			{
				"Name": "SodiumHydroxideDust" + static_item,
				"Count": 1
			},
			{
				"Name": "Chlorine" + static_item,
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
				"Name": "PotassiumChlorideDust" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10,
	},
	"Output":{
		"Items":[
			{
				"Name": "PotassiumDust" + static_item,
				"Count": 1
			},
			{
				"Name": "Chlorine" + static_item,
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
				"Name": "BoraxDust" + static_item,
				"Count": 2
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 50,
	},
	"Output":{
		"Items":[
			{
				"Name": "SodiumDust" + static_item,
				"Count": 1
			},
			{
				"Name": "BoronDust" + static_item,
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
				"Name": "Log" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Plank" + static_item,
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
				"Name": "StoneLog" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Plank" + static_item,
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
				"Name": "Plank" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CircuitBoard" + static_item,
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
				"Name": "StoneSurface" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "StoneTiles" + static_item,
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
				"Name": "DarkStoneSurface" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "DarkTiles" + static_item,
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
				"Name": "RedStoneSurface" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "RedTiles" + static_item,
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
				"Name": "StoneTiles" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "Bricks" + static_item,
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
				"Name": "RedTiles" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "RedBricks" + static_item,
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
				"Name": "DarkTiles" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "DarkBricks" + static_item,
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
				"Name": "Terracotta" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "TerracottaTiles" + static_item,
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
				"Name": "TerracottaTiles" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 20
	},
	"Output":{
		"Items":[
			{
				"Name": "TerracottaBricks" + static_item,
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
				"Name": "Concrete" + static_item,
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteTiles" + static_item,
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
				"Name": "ConcreteTiles" + static_item,
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteSmallTiles" + static_item,
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
				"Name": "ConcreteSmallTiles" + static_item,
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteBricks" + static_item,
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
				"Name": "ReinforcedConcrete" + static_item,
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteTiles" + static_item,
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
				"Name": "ReinforcedConcreteTiles" + static_item,
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteSmallTiles" + static_item,
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
				"Name": "ReinforcedConcreteSmallTiles" + static_item,
				"Count": 1
			},		
		]
	},
	"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 10
			},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteBricks" + static_item,
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
		"Name": "Electricity" + static_item,
		"Count": 55,
	},
	"Output":{
		"Items":[
		],
	},
	"ResourceOutput":{
			"Name": "Heat" + static_item,
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
		"Name": "Electricity" + static_item,
		"Count": 380
	},
	"Output":{
		"Items":[
		],
	},
	"ResourceOutput":{
			"Name": "Heat" + static_item,
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
				"Name": "Biomass" + static_item,
				"Count": 500
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Methane" + static_item,
				"Count": 500
			},
			{
				"Name": "FermentedBiomass" + static_item,
				"Count": 500
			}
		]
	},
	
	"Ticks" : 200
})

recipes_ferm.append({
	"Name": "EthanolFromFB",
	"Input":{
		"Items":[
			{
				"Name": "FermentedBiomass" + static_item,
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Ethanol" + static_item,
				"Count": 500
			},
			{
				"Name": "Water" + static_item,
				"Count": 500
			}
		]
	},
	
	"Ticks" : 200*3
})

recipes_ferm.append({
	"Name": "MethaneFromPumpkin",
	"Input":{
		"Items":[
			{
				"Name": "Pumpkin" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Methane" + static_item,
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
			"Name": "Heat" + static_item,
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
		"Name": "Electricity" + static_item,
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
		"Name": "Heat" + static_item,
		"Count": 500,
	},
	"Ticks" : 60,
})

recipes_chem.append({
	"Name": "MineralWater",
	"Input":{
		"Items":[
			{
				"Name": "MineralWater" + static_item,
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "SaltDust" + static_item,
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
				"Name": "MineralWater" + static_item,
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 60
	},
	"Output":{
		"Items":[
			{
				"Name": "BoraxDust" + static_item,
				"Count": 1,
				"Probability": 0.1
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
				"Name": "MineralWater" + static_item,
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "PotassiumChlorideDust" + static_item,
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
				"Name": "TungstenDust" + static_item,
				"Count": 1
			},
			{
				"Name": "Coke" + static_item,
				"Count": 2
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "TungstenCarbideDust" + static_item,
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
				"Name": "PreparedTitaniumOxideDust" + static_item,
				"Count": 1
			},
			{
				"Name": "Chlorine" + static_item,
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumTetrachloride" + static_item,
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
				"Name": "TitaniumTetrachloride" + static_item,
				"Count": 1000
			},
			{
				"Name": "AluminiumDust" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumSponge" + static_item,
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
				"Name": "TungstenOxideDust" + static_item,
				"Count": 1
			},
			{
				"Name": "Hydrogen" + static_item,
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "TungstenDust" + static_item,
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
				"Name": "CobaltOxideDust" + static_item,
				"Count": 1
			},
			{
				"Name": "Hydrogen" + static_item,
				"Count": 1000
			},
		]
	},
	"ResourceInput":{
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "CobaltDust" + static_item,
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200,
	"Scaled": False,
})

for i in {"ProducerGas", "Methane", "Hydrogen"}:
	recipes_gasturb.append({
		"Input":{
			"Items":[
				{
					"Name": i + static_item,
					"Count": 14 * 1000
				}
			]
		},
		"Output":{
			"Items":[
			]
		},
		"ResourceOutput":{
				"Name": "Kinetic" + static_item,
				"Count": named_material(i)["Burnable"]["HeatPerTick"] * 14 * 2
			},
		"Ticks" : named_material(i)["Burnable"]["BurnTime"],
		"Name": i,
	})
	
	recipes_combustion.append({
		"Name": i,
		"Input":{
			"Items":[
				{
					"Name": i + static_item,
					"Count": 1000 * 5 / 10.0
				}			
			]
		},
		"Output":{
			"Items":[
			]
		},
		"ResourceOutput":{
				"Name": "Kinetic" + static_item,
				"Count": named_material(i)["Burnable"]["HeatPerTick"] * 5
			},
		"Ticks" : named_material(i)["Burnable"]["BurnTime"] / 10.0
	})

for i in {"Gasoline", "Diesel", "HighCetaneDiesel", "Superfuel"}:
	recipes_combustion.append({
		"Input":{
			"Items":[
				{
					"Name": i + static_item,
					"Count": 1000 * 5 / 10.0
				}
			]
		},
		"Output":{
			"Items":[
			]
		},
		"ResourceOutput":{
				"Name": "Kinetic" + static_item,
				"Count": named_material(i)["Burnable"]["HeatPerTick"] * 5 * 5
			},
		"Ticks" : named_material(i)["Burnable"]["BurnTime"] / 10.0,
		"Name": i,
	})

for i in {"Gasoline", "Diesel", "HighCetaneDiesel", "Superfuel"}:
	recipes_combustion.append({
		"Input":{
			"Items":[
				{
					"Name": i + static_item,
					"Count": 1000 * 5 * 2 / 10.0
				}
			]
		},
		"Output":{
			"Items":[
			]
		},
		"ResourceOutput":{
				"Name": "Kinetic" + static_item,
				"Count": named_material(i)["Burnable"]["HeatPerTick"] * 5 * 5 * 0.95 * 2
			},
		"Ticks" : named_material(i)["Burnable"]["BurnTime"] / 10.0,
		"Name": "Double"+i,
	})

oil_crack.append({
	"Name": "RawOil",
	"Input":{
		"Items":[
			{
				"Name": "RawOil" + static_item,
				"Count": 15000
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 150
		},
	"Output":{
		"Items":[	
			{
				"Name": "ExtraHeavyOil" + static_item,
				"Count": 800
			},
			{
				"Name": "HeavyOil" + static_item,
				"Count": 1000
			},
			{
				"Name": "Diesel" + static_item,
				"Count": 4000
			},
			{
				"Name": "Gasoline" + static_item,
				"Count": 1000
			},
			{
				"Name": "Ethylene" + static_item,
				"Count": 5000
			},
			{
				"Name": "Methane" + static_item,
				"Count": 5000
			},
			{
				"Name": "Hydrogen" + static_item,
				"Count": 2500
			}				
		]
	},
	
	"Ticks" : 600
})

recipes_pyro.append({
	"Name": "Coal",
	"Input":{
		"Items":[
			{
				"Name": "Coal" + static_item,
				"Count": 1
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[
			{
				"Name": "Coke" + static_item,
				"Count": 1
			},
			{
				"Name": "RawOil" + static_item,
				"Count": 100
			},
			{
				"Name": "ProducerGas" + static_item,
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
				"Name": "Coal" + static_item,
				"Count": 1
			},
			{
				"Name": "Steam" + static_item,
				"Count": 200
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[
			{
				"Name": "Coke" + static_item,
				"Count": 1
			},
			{
				"Name": "ProducerGas" + static_item,
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
				"Name": "RawOil" + static_item,
				"Count": 2000
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 15
		},
	"Output":{
		"Items":[	
			{
				"Name": "HeavyOil" + static_item,
				"Count": 500
			},
			{
				"Name": "Gasoline" + static_item,
				"Count": 100
			},
{
				"Name": "Methane" + static_item,
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
				"Name": "RawOil" + static_item,
				"Count": 1000*5
			},
			{
				"Name": "Steam" + static_item,
				"Count": 1000
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 100
		},
	"Output":{
		"Items":[	
			{
				"Name": "HeavyOil" + static_item,
				"Count": 150*2
			},
			{
				"Name": "Gasoline" + static_item,
				"Count": 400*2
			},
{
				"Name": "Methane" + static_item,
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
				"Name": "HeavyOil" + static_item,
				"Count": 1000
			},
			{
				"Name": "Steam" + static_item,
				"Count": 200
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Gasoline" + static_item,
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
				"Name": "Gasoline" + static_item,
				"Count": 1000
			},
			{
				"Name": "Steam" + static_item,
				"Count": 200
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Methane" + static_item,
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
				"Name": "Methane" + static_item,
				"Count": 800*5
			},
			{
				"Name": "Steam" + static_item,
				"Count": 200*20
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 100
		},
	"Output":{
		"Items":[	
			{
				"Name": "ProducerGas" + static_item,
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
				"Name": "Methane" + static_item,
				"Count": 800*5
			}
		]
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 50
		},
	"Output":{
		"Items":[	
			{
				"Name": "ProducerGas" + static_item,
				"Count": 500*5
			},		
		]
	},
	"Ticks" : 200
})


recipes_pyro.append({
	"Name": "BioToAmmonia",
	"Input":{
		"Items":[
			{
				"Name": "FermentedBiomass" + static_item,
				"Count": 1000
			}
		]
	},
	"ResourceInput":{
			"Name": "Heat" + static_item,
			"Count": 50
		},
	"Output":{
		"Items":[	
			{
				"Name": "Ammonia" + static_item,
				"Count": 500
			},	
			{
				"Name": "Ash" + static_item,
				"Count": 1
			},	
		]
	},
	"Ticks" : 200
})

recipes_industrial_chemreactor.append({
	"Name": "RocketFuel",
	"Input":{
		"Items":[
			{
				"Name": "Chlorine" + static_item,
				"Count": 1000
			},{
				"Name": "Ammonia" + static_item,
				"Count": 3000
			},{
				"Name": "Methanol" + static_item,
				"Count": 4000
			},
			{
				"Name": "Catalyst" + static_item,
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "RocketFuel" + static_item,
				"Count": 5000,
			},		
		]
	},
	"Ticks" : 200,
	"Colors": [[0.3,0.2,0,1],[1,1,0.5,1]]
})

recipes_industrial_chemreactor.append({
	"Name": "RocketFuel2",
	"Input":{
		"Items":[
			{
				"Name": "Chlorine" + static_item,
				"Count": 1000
			},{
				"Name": "Ammonia" + static_item,
				"Count": 3000
			},{
				"Name": "Methanol" + static_item,
				"Count": 4000
			},
			{
				"Name": "UltimateCatalyst" + static_item,
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "RocketFuel" + static_item,
				"Count": 7000,
			},		
		]
	},
	"Ticks" : 200,
	"Colors": [[0.3,0.2,0,1],[1,1,0.5,1]]
})

recipes_industrial_chemreactor.append({
	"Name": "Ethylene",
	"Input":{
		"Items":[
			{
				"Name": "ProducerGas" + static_item,
				"Count": 1000
			},
			{
				"Name": "Catalyst" + static_item,
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Ethylene" + static_item,
				"Count": 1000,
			},		
		]
	},
	"Ticks" : 200,
	"Colors": [[0.2,0.2,0.2,0.5],[0.2,0.5,0.2,0.5]]
})

recipes_chem.append({
	"Name": "Sulfur",
	"Input":{
		"Items":[
			{
				"Name": "HeavyOil" + static_item,
				"Count": 150
			},
			{
				"Name": "Water" + static_item,
				"Count": 250
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Sulfur" + static_item,
				"Count": 1
			},		
		]
	},
	"Ticks" : 200
})

recipes_industrial_chemreactor.append({
	"Name": "SulfuricAcid",
	"Input":{
		"Items":[
			{
				"Name": "Sulfur" + static_item,
				"Count": 1
			},
			{
				"Name": "Oxygen" + static_item,
				"Count": 250
			},
			{
				"Name": "Water" + static_item,
				"Count": 250
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "SulfuricAcid" + static_item,
				"Count": 1000
			},		
		]
	},
	"Ticks" : 200,
	"Colors": [[0.4,0.4,0.8,0.5],[1.0,0.7,0.1,0.5]]
})

recipes_industrial_chemreactor.append({
	"Name": "RapeseedOil",
	"Input":{
		"Items":[
			{
				"Name": "RapeseedOil" + static_item,
				"Count": 1000
			},
			{
				"Name": "Ethanol" + static_item,
				"Count": 150
			},
			{
				"Name": "SodiumHydroxideDust" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Diesel" + static_item,
				"Count": 400
			}
		]
	},
	"Ticks" : 400,
	"Colors": [[0.4,0.4,0.0,1.0],[0.4,0.4,0.0,0.15]]
})

recipes_chem.append({
	"Name": "Plastic1",
	"Input":{
		"Items":[
			{
				"Name": "Ethylene" + static_item,
				"Count": 1000
			},
			{
				"Name": "Coal" + static_item,
				"Count": 1
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Plastic" + static_item,
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
				"Name": "Ethylene" + static_item,
				"Count": 1000
			},
			{
				"Name": "HeavyOil" + static_item,
				"Count": 150
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Plastic" + static_item,
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
				"Name": "ProducerGas" + static_item,
				"Count": 1000
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Hydrogen" + static_item,
				"Count": 750
			},		
		]
	},
	"Ticks" : 200
})

recipes_chem.append({
	"Name": "Coal",
	"Input":{
		"Items":[
			{
				"Name": "Ash" + static_item,
				"Count": 3
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Coal" + static_item,
				"Count": 1
			},		
		]
	},
	"Ticks" : 10
})

recipes_industrial_chemreactor.append({
	"Name": "Ammonia",
	"Input":{
		"Items":[
			{
				"Name": "Nitrogen" + static_item,
				"Count": 250
			},
			{
				"Name": "Hydrogen" + static_item,
				"Count": 750
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 20
		},
	"Output":{
		"Items":[	
			{
				"Name": "Ammonia" + static_item,
				"Count": 1000
			},		
		]
	},
	"Ticks" : 200,
	"Colors": [[0.4,0.4,0.8,0.5],[0.5,0.2,0.5,0.3]]
})

recipes_industrial_chemreactor.append({
	"Name": "Methanol",
	"Input":{
		"Items":[
			{
				"Name": "CarbonMonoxide" + static_item,
				"Count": 250
			},
			{
				"Name": "Hydrogen" + static_item,
				"Count": 750
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 50
		},
	"Output":{
		"Items":[	
			{
				"Name": "Methanol" + static_item,
				"Count": 1000
			},		
		]
	},
	"Ticks" : 100
})

recipes_industrial_chemreactor.append({
	"Name": "NitricAcid",
	"Input":{
		"Items":[
			{
				"Name": "Oxygen" + static_item,
				"Count": 250
			},
			{
				"Name": "Ammonia" + static_item,
				"Count": 750
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 20
		},
	"Output":{
		"Items":[	
			{
				"Name": "NitricAcid" + static_item,
				"Count": 1000
			},		
		]
	},
	"Ticks" : 150,
	"Colors": [[0.5,0.2,0.5,0.3],[0.0,0.5,0.25,0.3]]
})

recipes_industrial_chemreactor.append({
	"Name": "HighCetaneDiesel",
	"Input":{
		"Items":[
			{
				"Name": "Diesel" + static_item,
				"Count": 900
			},
			{
				"Name": "NitricAcid" + static_item,
				"Count": 100
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "HighCetaneDiesel" + static_item,
				"Count": 1000
			},		
		]
	},
	"Ticks" : 300,
	"Colors": [[0.4,0.4,0.0,0.15],[0.4,0.2,0.0,0.15]]
})

recipes_industrial_chemreactor.append({
	"Name": "Superfuel",
	"Input":{
		"Items":[
			{
				"Name": "HighCetaneDiesel" + static_item,
				"Count": 1000
			},
			{
				"Name": "FilteringCell" + static_item,
				"Count": 32,
				"Probability": 0,
			},
			{
				"Name": "Catalyst" + static_item,
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Superfuel" + static_item,
				"Count": 800
			},		
		]
	},
	"Ticks" : 300,
	"Colors": [[0.4,0.2,0.0,0.15],[0.7,0.6,0.25,0.15]]
})

recipes_industrial_chemreactor.append({
	"Name": "Superfuel2",
	"Input":{
		"Items":[
			{
				"Name": "HighCetaneDiesel" + static_item,
				"Count": 1000
			},
			{
				"Name": "FilteringCell" + static_item,
				"Count": 32,
				"Probability": 0,
			},
			{
				"Name": "UltimateCatalyst" + static_item,
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Superfuel" + static_item,
				"Count": 1000
			},		
		]
	},
	"Ticks" : 300,
	"Colors": [[0.4,0.2,0.0,0.15],[0.7,0.6,0.25,0.15]]
})

recipes_chem.append({
	"Name": "OreWater",
	"Input":{
		"Items":[
			{
				"Name": "OreWater" + static_item,
				"Count": 500
			},
			
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "Clay" + static_item,
				"Count": 1
			},		
		]
	},
	
	"Ticks" : 200
})

recipes_industrial_chemreactor.append({
	"Name": "OreWaterAll",
	"Input":{
		"Items":[
			{
				"Name": "OreWater" + static_item,
				"Count": 1000
			},
			{
				"Name": "FilteringCell" + static_item,
				"Count": 32,
				"Probability": 0
			},
		]
	},
	"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 10
		},
	"Output":{
		"Items":[	
			{
				"Name": "CopperOreDust" + static_item,
				"Count": 1,
				"Probability": .1
			},{
				"Name": "IronOreDust" + static_item,
				"Count": 1,
				"Probability": .1
			},{
				"Name": "UraniumOreDust" + static_item,
				"Count": 1,
				"Probability": .05
			},{
				"Name": "AluminiumOreDust" + static_item,
				"Count": 1,
				"Probability": .05
			}				
		]
	},
	"Ticks" : 400,
	"Colors": [[0.02,0.02,0.00,1.5],[0.1,0.1,0.1,0.1]]
})

for i in {"IronOreDust", "CopperOreDust"}:
	recipes_chemical_bath.append({
		"Name": i,
		"Input":{
			"Items":[
				{
					"Name": "Mercury" + static_item,
					"Count": 500
				},
				{
					"Name": i + static_item,
					"Count": 2,
				},
			]
		},
		"ResourceInput":{
				"Name": "Kinetic" + static_item,
				"Count": 10
			},
		"Output":{
			"Items":[	
				{
					"Name": "GoldDust" + static_item,
					"Count": 1,
				},		
			]
		},
		"Ticks" : 200,
		"Colors": [[0.4,0.4,0.1,0.8],[0.2,0.2,0.1,0.2]]
	})
	
recipes_chemical_bath.append({
	"Name":"RareEarthElement",
	"Input":{
		"Items":[
			{
				"Name": "AluminiumOreDust" + static_item,
				"Count": 10
			},
			{
				"Name": "SulfuricAcid" + static_item,
				"Count": 1000
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 30
	},
	"Output":{
		"Items":[
			{
				"Name": "RareEarthElement" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 1000,
	"Colors": [[0.4,0.4,0.1,0.8],[0.2,0.2,0.1,0.2]]
})

recipes_chemical_bath.append({
	"Name":"CobaltOxideDust",
	"Input":{
		"Items":[
			{
				"Name": "IronOreDust" + static_item,
				"Count": 10
			},
			{
				"Name": "SulfuricAcid" + static_item,
				"Count": 1000
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 30
	},
	"Output":{
		"Items":[
			{
				"Name": "CobaltOxideDust" + static_item,
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
				"Name": "HotHardMetalIngot" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "HardMetalIngot" + static_item,
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
				"Name": "HotNeutroniumIngot" + static_item,
				"Count": 1
			}
		]
	},
	"ResourceInput":{
		"Name": "Kinetic" + static_item,
		"Count": 1000
	},
	"Output":{
		"Items":[
			{
				"Name": "NeutroniumIngot" + static_item,
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
		"Name": "Electricity" + static_item,
		"Count": 10
	},
	"Output":{
		"Items":[
			{
				"Name": "Computations" + static_item,
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
		"Name": "Electricity" + static_item,
		"Count": 100
	},
	"Output":{
		"Items":[
			{
				"Name": "Computations" + static_item,
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
		"Name": "Electricity" + static_item,
		"Count": 2 * fission_fullpower*0.9*0.9
	},
	"Output":{
		"Items":[
			{
				"Name": "MothershipPing" + static_item,
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
				"Name": "StoneSurface" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Column" + static_item,
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
				"Name": "Column" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "FluetedColumn" + static_item,
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
				"Name": "Glass" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "GlassBlock" + static_item,
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
				"Name": "Plastic" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "PlasticBlock" + static_item,
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
				"Name": "Concrete" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DangerBlock" + static_item,
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
				"Name": "SandSurface" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "BasicPlatform" + static_item,
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
				"Name": "CopperCasing" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "RustyCopperCasing" + static_item,
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
				"Name": "SteelCasing" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "RustyIronCasing" + static_item,
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
					"Name": i + static_item,
					"Count": 1
				}
			]
		},
		"ResourceInput":{
			"Name": "Electricity" + static_item,
			"Count": 40
		},
		"Output":{
			"Items":[
				{
					"Name": i + static_item,
					"Count": 1
				}
			]
		},
		"Ticks" : 40
	})

objects_array.append({ "Class": base_recipe,
	"Name": "Multitool" + base_recipe,
	"Recipes": recipes_wrench
})

objects_array.append({ "Class": base_recipe,
	"Name": "BlastFurnace" + base_recipe,
	"Recipes": recipes_blast_furnace
})

objects_array.append({ "Class": base_recipe,
	"Name": "Oven" + base_recipe,
	"Recipes": recipes_oven
})

objects_array.append({ "Class": base_recipe,
	"Name": "Smelter" + base_recipe,
	"Recipes": recipes_smelter
})

objects_array.append({ "Class": base_recipe,
	"Name": "Macerator" + base_recipe,
	"Recipes": recipes_macerator
})

objects_array.append({ "Class": base_recipe,
	"Name": "Boiler" + base_recipe,
	"Recipes": recipes_boiler
})

objects_array.append({ "Class": base_recipe,
	"Name": "Generator" + base_recipe,
	"Recipes": recipes_generator
})

objects_array.append({ "Class": base_recipe,
	"Name": "IndustrialGenerator" + base_recipe,
	"Recipes": recipes_industrial_generator
})

objects_array.append({ "Class": base_recipe,
	"Name": "ElectricEngine" + base_recipe,
	"Recipes": recipes_electric_engine
})

objects_array.append({ "Class": base_recipe,
	"Name": "StirlingEngine" + base_recipe,
	"Recipes": recipes_steam_engine
})

objects_array.append({ "Class": base_recipe,
	"Name": "Pump" + base_recipe,
	"Recipes": recipes_pump
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
	"Name": "Press" + base_recipe,
	"Recipes": recipes_press
})

objects_array.append({ "Class": base_recipe,
	"Name": "ArcSmelter" + base_recipe,
	"Recipes": recipes_arc_furnace
})

objects_array.append({ "Class": base_recipe,
	"Name": "SteamTurbine" + base_recipe,
	"Recipes": recipes_steam_turbine
})

objects_array.append({ "Class": base_recipe,
	"Name": "Electrolyzer" + base_recipe,
	"Recipes": recipes_electrolyzer
})

objects_array.append({ "Class": base_recipe,
	"Name": "CuttingMachine" + base_recipe,
	"Recipes": recipes_cutter
})

objects_array.append({ "Class": base_recipe,
	"Name": "Furnace" + base_recipe,
	"Recipes": recipes_furnace
})

objects_array.append({ "Class": base_recipe,
	"Name": "ElectricFurnace" + base_recipe,
	"Recipes": recipes_elfurn
})

objects_array.append({ "Class": base_recipe,
	"Name": "Fermenter" + base_recipe,
	"Recipes": recipes_ferm
})

objects_array.append({ "Class": base_recipe,
	"Name": "MultitoolRobotArm" + base_recipe,
	"Recipes": recipes_toolarm
})

objects_array.append({ "Class": base_recipe,
	"Name": "AutomaticHammer" + base_recipe,
	"Recipes": recipes_hammer
})

objects_array.append({ "Class": base_recipe,
	"Name": "Mixer" + base_recipe,
	"Recipes": recipes_mixer
})

objects_array.append({ "Class": base_recipe,
	"Name": "Radiator" + base_recipe,
	"Recipes": recipes_radiator
})

objects_array.append({ "Class": base_recipe,
	"Name": "SolarPanel" + base_recipe,
	"Recipes": recipes_solar
})

objects_array.append({ "Class": base_recipe,
	"Name": "ChemReactor" + base_recipe,
	"Recipes": recipes_chem
})

objects_array.append({ "Class": base_recipe,
	"Name": "InductionCoil" + base_recipe,
	"Recipes": recipes_coil
})

objects_array.append({ "Class": base_recipe,
	"Name": "IndustrialSmelter" + base_recipe,
	"Recipes": recipes_indu
})

objects_array.append({ "Class": base_recipe,
	"Name": "HeatExchanger" + base_recipe,
	"Recipes": recipes_exch
})

objects_array.append({ "Class": base_recipe,
	"Name": "InverseHeatExchanger" + base_recipe,
	"Recipes": recipes_iexch
})

objects_array.append({ "Class": base_recipe,
	"Name": "Freezer" + base_recipe,
	"Recipes": recipes_freezer
})

objects_array.append({ "Class": base_recipe,
	"Name": "CombustionEngine" + base_recipe,
	"Recipes": recipes_combustion
})

objects_array.append({ "Class": base_recipe,
	"Name": "PyrolysisUnit" + base_recipe,
	"Recipes": recipes_pyro
})

objects_array.append({ "Class": base_recipe,
	"Name": "Computer" + base_recipe,
	"Recipes": recipes_computer
})

objects_array.append({ "Class": base_recipe,
	"Name": "CompactGenerator" + base_recipe,
	"Recipes": recipes_compact_generator
})

objects_array.append({ "Class": base_recipe,
	"Name": "FissionReactor" + base_recipe,
	"Recipes": recipes_fission
})

objects_array.append({ "Class": base_recipe,
	"Name": "AutomaticFarm" + base_recipe,
	"Recipes": recipes_farm
})

objects_array.append({ "Class": base_recipe,
	"Name": "AtmosphericCondenser" + base_recipe,
	"Recipes": recipes_condens
})

objects_array.append({ "Class": base_recipe,
	"Name": "Assembler" + base_recipe,
	"Recipes": recipes_assembler
})

objects_array.append({ "Class": base_recipe,
	"Name": "GasTurbine" + base_recipe,
	"Recipes": recipes_gasturb
})

objects_array.append({ "Class": base_recipe,
	"Name": "IndustrialChemReactor" + base_recipe,
	"Recipes": recipes_industrial_chemreactor
})

objects_array.append({ "Class": base_recipe,
	"Name": "Portal" + base_recipe,
	"Recipes": recipes_portal
})

objects_array.append({ "Class": base_recipe,
	"Name": "ChemicalBath" + base_recipe,
	"Recipes": recipes_chemical_bath
})

objects_array.append({ "Class": base_recipe,
	"Name": "Riteg" + base_recipe,
	"Recipes": recipes_riteg
})

objects_array.append({ "Class": base_recipe,
	"Name": "IndustrialSteamTurbine" + base_recipe,
	"Recipes": recipes_industrial_steam_turbine
})

objects_array.append({ "Class": base_recipe,
	"Name": "FusionReactor" + base_recipe,
	"Recipes": recipes_fusion_reactor
})

objects_array.append({ "Class": base_recipe,
	"Name": "IndustrialBoiler" + base_recipe,
	"Recipes": recipes_industrial_boiler
})

objects_array.append({ "Class": base_recipe,
	"Name": "IndustrialElectricEngine" + base_recipe,
	"Recipes": recipes_industrial_electric_engine
})

objects_array.append({ "Class": base_recipe,
	"Name": "KineticHeater" + base_recipe,
	"Recipes": recipes_kinetic_heater
})

objects_array.append({ "Class": base_recipe,
	"Name": "OilCrackingTower" + base_recipe,
	"Recipes": oil_crack
})

objects_array.append({ "Class": base_recipe,
	"Name": "Hand" + base_recipe,
	"Recipes": recipes_hand
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/misc.json", data);