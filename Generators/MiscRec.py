from Common import *
from MachinesList import *
from MiscGen import *
from PartsList import circuits
import copy

objects_array = []

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

recipes_combustion = []

recipes_pyro = []

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
	
	recipes_assembler.append(dec_recipe)

def append_recipe_hand_press(recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]
	
	dec_recipe = copy.deepcopy(recipe)

	recipes_hand.append(recipe)
	
	output = copy.deepcopy(dec_recipe["Input"])
	
	dec_recipe["Ticks"] = 60
	recipes_press.append(dec_recipe)		

recipes_industrial_generator.append({
	"Name": "Generating",
	"Input":{
		"Items":[
		]
	},
	"Output":{
		"Items":[
		]
	},
	"Ticks" : 200,
	"Loss": 10,
})

recipes_industrial_steam_turbine.append({
	"Name": "Rotating",
	"Input":{
		"Items":[
		]
	},
	"Output":{
		"Items":[
		]
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
	"Output":{
		"Items":[
		]
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
	"Output":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot",
				"Count": 1 * 3
			}
		]
	},
	"Ticks" : 300,
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumIngot4",
	"Input":{
		"Items":[
			{
				"Name": "UltimateCatalyst",
				"Count": 1,
				"Probability":0
			}
		]
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
				"Probability":0
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "HotNeutroniumIngot",
				"Count": 1 * 3
			}
		]
	},
	"Ticks" : 300,
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

# other		
		
append_recipe({
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

append_recipe({
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

append_recipe({
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

append_recipe({
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
				"Count": 2
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

append_recipe({
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

append_recipe({
	"Name":"QuantumCircuit",
	"Input":{
		"Items":[
			{
				"Name": "QuantumCore",
				"Count": 2
			},	
			{
				"Name": "Processor",
				"Count": 1
			}
		]
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

append_recipe({
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
	"Output":{
		"Items":[
			{
				"Name": "CopperWire",
				"Count": 2
			}
		]
	},
	"Ticks" : 40,
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

append_recipe({
	"Name": "PrimitiveBattery",
	"Input":{
		"Items":[
			{
				"Name": "Coke",
				"Count": 1
			},
			{
				"Name": "AluminiumParts",
				"Count": 1
			},
			{
				"Name": "SteelPlate",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "PrimitiveBattery",
				"Count": 1
			}
		]
	},
	"Ticks" : 100,
})
		
for level, name, copm_name in zip(range(0, 4), ["BasicBattery", "AdvancedBattery", "SuperiorBattery", "UltimateBattery"], ["Battery", "BasicBattery", "AdvancedBattery", "SuperiorBattery"]):
	append_recipe({
		"Name": name,
		"Input":{
			"Items":[
				{
					"Name": copm_name,
					"Count": battery_mul(0) if level == 0 else 4
				},
				{
					"Name": circuits[level + 1],
					"Count": 1
				}
			]
		},
		"Output":{
			"Items":[
				{
					"Name": name,
					"Count": 1
				}
			]
		},
		"Ticks" : 100 * (level + 1),
	})

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

recipes_assembler.append({
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
	"Ticks" : 200*3
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
				"Name": "SteelPlate",
				"Count": 1
			},
		]
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
	"Name":"LithiumBattery",
	"Input":{
		"Items":[
			{
				"Name": "SulfuricAcid",
				"Count": 200
			},
			{
				"Name": "LithiumPlate",
				"Count": 1
			},
			{
				"Name": "CopperParts",
				"Count": 3
			},
			{
				"Name": "SteelPlate",
				"Count": 3
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Battery",
				"Count": 10
			}
		]
	},
	"Ticks" : 300,
	
})

recipes_assembler.append({
	"Name":"AdvancedFrame",
	"Input":{
		"Items":[
			{
				"Name": "TitaniumParts",
				"Count": 4
			},
			{
				"Name": "CarbonFiberSheet",
				"Count": 1
			},
			{
				"Name": "LithiumPlate",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedFrame",
				"Count": 1
			}
		]
	},
	"Ticks" : 300,
	
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
				"Name": "RareEarthElement",
				"Count": 3
			},
		]
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
				"Count": 500
			}
		]
	},
	"Ticks" : 40,
})

recipes_condens.append({
	"Name":"Oxygen",
	"Input":{
		"Items":[
		]
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
	"Ticks" : 2000,
})

recipes_farm.append({
	"Name":"Grass",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 100
			},
			{
				"Name": "DirtSurface",
				"Count": 5
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "GrassSurface",
				"Count": 5
			}
		]
	},
	"Ticks" : 200,
})

recipes_farm.append({
	"Name":"Rapeseed",
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
				"Name": "Rapeseed",
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
				"Probability": 10,
			}
		]
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
				"Probability": 0,
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
				"Probability": 0,
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
				"Probability": 0,
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
				"Probability": 0,
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
				"Probability": 0,
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
				"Probability": 0,
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
				"Probability": 0,
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
				"Probability": 0,
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
				"Probability": 0,
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
				"Probability": 0,
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
				"Probability": 0,
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
	"Ticks" : 200,
})

recipes_industrial_chemreactor.append({
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
	"Output":{
		"Items":[
		]
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
	"Output":{
		"Items":[
		]
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
	"Output":{
		"Items":[
		]
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
	"Output":{
		"Items":[
		]
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
	"Output":{
		"Items":[
		]
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
	"Output":{
		"Items":[
		]
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
	"Output":{
		"Items":[
		]
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
	"Output":{
		"Items":[
		]
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
	"Ticks": 5*2*20,
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
	"Ticks": 5*2*20,
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
	"Ticks": 3*2*20,
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
	"Ticks": 2*2*20,
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
	"Ticks": 100,
})

for fuel_type, bonus in zip(["Coke"], [1.0]):	
	recipes_blast_furnace.append({
		"Name": "IronOreSmelting",
		"Input":{
			"Items":[
				{
					"Name": fuel_type,
					"Count": 30
				},
				{
					"Name": "IronOre",
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
		"Ticks" : 10*5*20
	})
	recipes_blast_furnace.append({
		"Name": "IronImpureOreGravelSmelting",
		"Input":{
			"Items":[
				{
					"Name": fuel_type,
					"Count": 25
				},
				{
					"Name": "IronImpureOreGravel",
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
		"Ticks" : 10*5*20
	})
	recipes_blast_furnace.append({
		"Name": "IronOreGravelSmelting",
		"Input":{
			"Items":[
				{
					"Name": fuel_type,
					"Count": 20
				},
				{
					"Name": "IronOreGravel",
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
		"Ticks" : 10*5*20
	})
	recipes_blast_furnace.append({
		"Name": "IronOreDustSmelting",
		"Input":{
			"Items":[
				{
					"Name": fuel_type,
					"Count": 15
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
		"Ticks" : 10*5*20
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
		"Ticks" : 10*5*20
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
				"Count": 4
			},
			{
				"Name": "ChromiumDust",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "StainlessSteelDust",
				"Count": 4
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
				"Count": 4
			},
			{
				"Name": "ChromiumDust",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "StainlessSteelDust",
				"Count": 4
			}
		]
	},
	
	"Ticks" : 600,
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
	"Output":{
		"Items": [
			{
				"Name":"Cell"+static_item,
				"Count":1
			},
			{
				"Name": "PlutoniumDust",
				"Count": 1,
				"Probability":50
			}
		]
	},
	"Ticks": 400,
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
	"Output":{
		"Items":[
			{
				"Name": "SiliconOxide",
				"Count": 1
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
	"Name": "Rapeseed",
	"Input":{
		"Items":[
			{
				"Name": "Rapeseed",
				"Count": 2
			},
		]
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
	"Output":{
		"Items":[
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
	"Name": "Clay",
	"Input":{
		"Items":[
			{
				"Name": "DirtSurface",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Clay",
				"Count": 1
			}
		]
	},
	
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
	"Output":{
		"Items":[
			{
				"Name": "SandSurface",
				"Count": 1
			}
		]
	},
	"Ticks" : 100
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
			{
				"Name": "Mercury",
				"Count": 1000
			},
		],
	},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumIngot",
				"Count": 1
			},
			{
				"Name": "HotMercury",
				"Count": 1000
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
			{
				"Name": "Mercury",
				"Count": 300
			},
		],
	},
	"Output":{
		"Items":[
			{
				"Name": "SuperconductorIngot",
				"Count": 1
			},
			{
				"Name": "HotMercury",
				"Count": 300
			},
		]
	},
	"Tier": 5,
	"Ticks" : 100,
})
	
recipes_indu.append({
	"Name":"TDustToIngot",
	"Input":{
		"Items":[
			{
				"Name": "TitaniumDust",
				"Count": 1
			},
			{
				"Name": "Mercury",
				"Count": 100
			},
		],
	},
	"Output":{
		"Items":[
			{
				"Name": "TitaniumIngot",
				"Count": 1
			},
			{
				"Name": "HotMercury",
				"Count": 100
			},
		]
	},
	"Tier": 5,
	"Ticks" : 100,
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
	"Output":{
		"Items":[
			{
				"Name": "SiliconOxide",
				"Count": 1
			}
		]
	},
	"Ticks" : 10*20
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
	"Name":"SandElectrolyze",
	"Input":{
		"Items":[
			{
				"Name": "SiliconOxide",
				"Count": 1
			}
		]
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
	"Name":"SaltElectrolyze",
	"Input":{
		"Items":[
			{
				"Name": "Salt",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Chlorine",
				"Count": 1000
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
	"Name": "CircuitBoard",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 1
			},
		]
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
	"Output":{
		"Items":[
		],
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
	"Output":{
		"Items":[
		],
	},
	"Ticks" : 200,
	"Loss" : 10
})

recipes_ferm.append({
	"Name": "Dirt",
	"Input":{
		"Items":[
			{
				"Name": "SandSurface",
				"Count": 1
			},
			{
				"Name": "Organics",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DirtSurface",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 200
})

recipes_ferm.append({
	"Name": "Rapseed",
	"Input":{
		"Items":[
			{
				"Name": "Rapeseed",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "RapeseedOil",
				"Count": 500
			}
		]
	},
	
	"Ticks" : 200
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
	"Output":{
		"Items":[
			{
				"Name": "Methane",
				"Count": 500
			},
			{
				"Name": "FermentedBiomass",
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
				"Name": "FermentedBiomass",
				"Count": 1000
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Ethanol",
				"Count": 500
			},
			{
				"Name": "Water",
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
				"Name": "Pumpkin",
				"Count": 1
			},
		]
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
	"Ticks" : 60,
})

recipes_chem.append({
	"Name": "MineralWater",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 1000
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Salt",
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
				"Name": "Water",
				"Count": 1000
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "BoraxDust",
				"Count": 1,
				"Probability": 10
			}
		]
	},
	
	"Ticks" : 100,
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

recipes_industrial_chemreactor.append({
	"Name": "HotMercury",
	"Input":{
		"Items":[
			{
				"Name": "HotMercury",
				"Count": 1000
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Mercury",
				"Count": 1000
			}
		]
	},
	"Ticks" : 600,
	"Colors": [[20,5,0],[0.5,0.5,0.5]]
})

recipes_industrial_chemreactor.append({
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
	"Output":{
		"Items":[
			{
				"Name": "TitaniumTetrachloride",
				"Count": 1000
			}
		]
	},
	"Ticks" : 200,
	"Colors": [[0.8,0.8,0,0.3],[.3,0,0.3]]
})

recipes_industrial_chemreactor.append({
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
	"Output":{
		"Items":[
			{
				"Name": "TitaniumSponge",
				"Count": 1
			},
		],
	},
	"Ticks" : 200
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

for i in {"ProducerGas", "Methane", "Hydrogen"}:
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
		"Ticks" : named_material(i)["Burnable"]["BurnTime"],
		"Name": i,
	})
	
	recipes_combustion.append({
		"Name": i,
		"Input":{
			"Items":[
				{
					"Name": i,
					"Count": 1000 * 5 / 10.0
				}			
			]
		},
		"Output":{
			"Items":[
			]
		},
		"Ticks" : named_material(i)["Burnable"]["BurnTime"] / 10.0
	})

for i in {"Gasoline", "Diesel", "HighCetaneDiesel", "Superfuel"}:
	recipes_combustion.append({
		"Input":{
			"Items":[
				{
					"Name": i,
					"Count": 1000 * 5 / 10.0
				}
			]
		},
		"Output":{
			"Items":[
			]
		},
		"Ticks" : named_material(i)["Burnable"]["BurnTime"] / 10.0,
		"Name": i,
	})

for i in {"Gasoline", "Diesel", "HighCetaneDiesel", "Superfuel"}:
	recipes_combustion.append({
		"Input":{
			"Items":[
				{
					"Name": i,
					"Count": 1000 * 5 * 2 / 10.0
				}
			]
		},
		"Output":{
			"Items":[
			]
		},
		"Ticks" : named_material(i)["Burnable"]["BurnTime"] / 10.0,
		"Name": "Double"+i,
	})

oil_crack.append({
	"Name": "RawOil",
	"Input":{
		"Items":[
			{
				"Name": "RawOil",
				"Count": 15000
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "ExtraHeavyOil",
				"Count": 800
			},
			{
				"Name": "HeavyOil",
				"Count": 1000
			},
			{
				"Name": "Diesel",
				"Count": 4000
			},
			{
				"Name": "Gasoline",
				"Count": 1000
			},
			{
				"Name": "Ethylene",
				"Count": 5000
			},
			{
				"Name": "Methane",
				"Count": 5000
			},
			{
				"Name": "Hydrogen",
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
				"Name": "Coal",
				"Count": 1
			},
			
		]
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
	"Name": "PrimitiveRawOil",
	"Input":{
		"Items":[
			{
				"Name": "RawOil",
				"Count": 2000
			},
			
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "HeavyOil",
				"Count": 500
			}		
		]
	},
	"Ticks" : 150
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
	"Name": "HeavyOilSteam",
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
	"Name": "GasolineSteam",
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
	"Name": "MethaneSteam",
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


recipes_pyro.append({
	"Name": "BioToAmmonia",
	"Input":{
		"Items":[
			{
				"Name": "FermentedBiomass",
				"Count": 1000
			}
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "Ammonia",
				"Count": 500
			},	
			{
				"Name": "Ash",
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
				"Name": "Chlorine",
				"Count": 1000
			},{
				"Name": "Ammonia",
				"Count": 1000
			},{
				"Name": "Ethanol",
				"Count": 2000
			},{
				"Name": "Gasoline",
				"Count": 4000
			},
			{
				"Name": "Catalyst",
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "RocketFuel",
				"Count": 6000,
			},		
		]
	},
	"Ticks" : 1500,
	"Colors": [[0.3,0.2,0,1],[1,1,0.5,1]]
})

recipes_industrial_chemreactor.append({
	"Name": "RocketFuel2",
	"Input":{
		"Items":[
			{
				"Name": "Chlorine",
				"Count": 1000
			},{
				"Name": "Ammonia",
				"Count": 1000
			},{
				"Name": "Ethanol",
				"Count": 2000
			},{
				"Name": "Gasoline",
				"Count": 3000
			},
			{
				"Name": "UltimateCatalyst",
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "RocketFuel",
				"Count": 8000,
			},		
		]
	},
	"Ticks" : 1500,
	"Colors": [[0.3,0.2,0,1],[1,1,0.5,1]]
})

recipes_industrial_chemreactor.append({
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
				"Probability": 0,
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "Ethylene",
				"Count": 1000,
			},		
		]
	},
	"Ticks" : 200,
	"Colors": [[0.2,0.2,0.2,0.5],[0.2,0.5,0.2,0.5]]
})

recipes_industrial_chemreactor.append({
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
	"Output":{
		"Items":[	
			{
				"Name": "Sulfur",
				"Count": 1
			},		
		]
	},
	"Ticks" : 200,
	"Colors": [[0.0,0.2,0.0,0.9],[0.0,0.0,0.0,0.2]]
})

recipes_industrial_chemreactor.append({
	"Name": "SulfuricAcid",
	"Input":{
		"Items":[
			{
				"Name": "Sulfur",
				"Count": 1
			},
			{
				"Name": "Catalyst",
				"Count": 1,
				"Probability": 0
			},
			{
				"Name": "Water",
				"Count": 1000
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "SulfuricAcid",
				"Count": 300
			},		
		]
	},
	"Ticks" : 200,
	"Colors": [[0.0,0.0,0.3,0.2],[0.8,0.8,0.1,0.3]]
})

recipes_industrial_chemreactor.append({
	"Name": "RapeseedOil",
	"Input":{
		"Items":[
			{
				"Name": "RapeseedOil",
				"Count": 1000
			},
			{
				"Name": "Ethanol",
				"Count": 150
			},
			{
				"Name": "SodiumHydroxideDust",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "Diesel",
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
				"Name": "Ethylene",
				"Count": 1000
			},
			{
				"Name": "Coal",
				"Count": 1
			},
		]
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

recipes_chem.append({
	"Name": "Coal",
	"Input":{
		"Items":[
			{
				"Name": "Ash",
				"Count": 3
			},
			
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "Coal",
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
				"Name": "Nitrogen",
				"Count": 250
			},
			{
				"Name": "Hydrogen",
				"Count": 750
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "Ammonia",
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
				"Name": "CarbonMonoxide",
				"Count": 250
			},
			{
				"Name": "Hydrogen",
				"Count": 750
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "Ethanol",
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
				"Name": "Oxygen",
				"Count": 250
			},
			{
				"Name": "Ammonia",
				"Count": 750
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "NitricAcid",
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
				"Name": "Diesel",
				"Count": 900
			},
			{
				"Name": "NitricAcid",
				"Count": 100
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "HighCetaneDiesel",
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
				"Name": "HighCetaneDiesel",
				"Count": 1000
			},
			{
				"Name": "FilteringCell",
				"Count": 32,
				"Probability": 0,
			},
			{
				"Name": "Catalyst",
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "Superfuel",
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
				"Name": "HighCetaneDiesel",
				"Count": 1000
			},
			{
				"Name": "FilteringCell",
				"Count": 32,
				"Probability": 0,
			},
			{
				"Name": "UltimateCatalyst",
				"Count": 1,
				"Probability": 0,
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "Superfuel",
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
				"Name": "OreWater",
				"Count": 500
			},
			
		]
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

recipes_industrial_chemreactor.append({
	"Name": "OreWaterAll",
	"Input":{
		"Items":[
			{
				"Name": "OreWater",
				"Count": 1000
			},
			{
				"Name": "FilteringCell",
				"Count": 32,
				"Probability": 0
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "CopperOreDust",
				"Count": 1,
				"Probability": 10
			},{
				"Name": "IronOreDust",
				"Count": 1,
				"Probability": 10
			},{
				"Name": "UraniumOreDust",
				"Count": 1,
				"Probability": 5
			},{
				"Name": "AluminiumOreDust",
				"Count": 1,
				"Probability": 5
			}				
		]
	},
	"Ticks" : 400,
	"Colors": [[0.02,0.02,0.00,1.5],[0.1,0.1,0.1,0.1]]
})

for i in {"IronOreDust", "CopperOreDust"}:
	recipes_industrial_chemreactor.append({
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
		"Output":{
			"Items":[	
				{
					"Name": "GoldDust",
					"Count": 1,
				},		
			]
		},
		"Ticks" : 200,
		"Colors": [[0.4,0.4,0.1,0.8],[0.2,0.2,0.1,0.2]]
	})
	
recipes_industrial_chemreactor.append({
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
	"Output":{
		"Items":[
			{
				"Name": "RareEarthElement",
				"Count": 1
			}
		]
	},
	"Ticks" : 500,
	"Colors": [[0.8,0.8,0.1,0.3],[0.7,0.2,0.7,0.8]]
})

recipes_industrial_chemreactor.append({
	"Name": "LithiumPlate",
	"Input":{
		"Items":[
			{
				"Name": "IronOreDust",
				"Count": 3
			},
			{
				"Name": "Salt",
				"Count": 1
			},
			{
				"Name": "NitricAcid",
				"Count": 500
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "LithiumPlate",
				"Count": 1
			}
		]
	},
	"Ticks" : 200
})

recipes_industrial_chemreactor.append({
	"Name": "CarbonPrecursor",
	"Input":{
		"Items":[
			{
				"Name": "HeavyOil",
				"Count": 1000
			},
			{
				"Name": "SulfuricAcid",
				"Count": 100
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "CarbonPrecursor",
				"Count": 1000
			}
		]
	},
	"Ticks" : 200
})

recipes_pyro.append({
	"Name": "CarbonFiber",
	"Input":{
		"Items":[
			{
				"Name": "CarbonPrecursor",
				"Count": 500
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "CarbonFiber",
				"Count": 1
			}
		]
	},
	"Ticks" : 200
})

append_recipe({
	"Name": "CarbonFiberSheet",
	"Input":{
		"Items":[
			{
				"Name": "CarbonFiber",
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "CarbonFiberSheet",
				"Count": 1
			}
		]
	},
	"Ticks" : 200
})

recipes_portal.append({
	"Name":"Ping",
	"Input":{
		"Items":[
		]
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

for name in ("DangerBlock", "ConcreteRamp", "ConcreteRamp2", "ConcreteRamp3", "ConcreteBeam", "ConcreteBeam2"):
	append_recipe_hand_press({
		"Name": name,
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
					"Name": name,
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

objects_array.append({ "Class": r_dict,
	"Name": "BlastFurnace" + r_dict,
	"Recipes": recipes_blast_furnace
})

objects_array.append({ "Class": r_dict,
	"Name": "Oven" + r_dict,
	"Recipes": recipes_oven
})

objects_array.append({ "Class": r_dict,
	"Name": "Smelter" + r_dict,
	"Recipes": recipes_smelter
})

objects_array.append({ "Class": r_dict,
	"Name": "Macerator" + r_dict,
	"Recipes": recipes_macerator
})

objects_array.append({ "Class": r_dict,
	"Name": "Boiler" + r_dict,
	"Recipes": recipes_boiler
})

objects_array.append({ "Class": r_dict,
	"Name": "Generator" + r_dict,
	"Recipes": recipes_generator
})

objects_array.append({ "Class": r_dict,
	"Name": "IndustrialGenerator" + r_dict,
	"Recipes": recipes_industrial_generator
})

objects_array.append({ "Class": r_dict,
	"Name": "ElectricEngine" + r_dict,
	"Recipes": recipes_electric_engine
})

objects_array.append({ "Class": r_dict,
	"Name": "StirlingEngine" + r_dict,
	"Recipes": recipes_steam_engine
})

objects_array.append({ "Class": r_dict,
	"Name": "Pump" + r_dict,
	"Recipes": recipes_pump
})

objects_array.append({ "Class": r_dict,
	"Name": "Separator" + r_dict,
	"Recipes": recipes_sep
})

objects_array.append({ "Class": r_dict,
	"Name": "IndustrialSeparator" + r_dict,
	"Recipes": recipes_sep2
})

objects_array.append({ "Class": r_dict,
	"Name": "Press" + r_dict,
	"Recipes": recipes_press
})

objects_array.append({ "Class": r_dict,
	"Name": "ArcSmelter" + r_dict,
	"Recipes": recipes_arc_furnace
})

objects_array.append({ "Class": r_dict,
	"Name": "SteamTurbine" + r_dict,
	"Recipes": recipes_steam_turbine
})

objects_array.append({ "Class": r_dict,
	"Name": "Electrolyzer" + r_dict,
	"Recipes": recipes_electrolyzer
})

objects_array.append({ "Class": r_dict,
	"Name": "CuttingMachine" + r_dict,
	"Recipes": recipes_cutter
})

objects_array.append({ "Class": r_dict,
	"Name": "Furnace" + r_dict,
	"Recipes": recipes_furnace
})

objects_array.append({ "Class": r_dict,
	"Name": "ElectricFurnace" + r_dict,
	"Recipes": recipes_elfurn
})

objects_array.append({ "Class": r_dict,
	"Name": "Fermenter" + r_dict,
	"Recipes": recipes_ferm
})

objects_array.append({ "Class": r_dict,
	"Name": "MultitoolRobotArm" + r_dict,
	"Recipes": recipes_toolarm
})

objects_array.append({ "Class": r_dict,
	"Name": "AutomaticHammer" + r_dict,
	"Recipes": recipes_hammer
})

objects_array.append({ "Class": r_dict,
	"Name": "Mixer" + r_dict,
	"Recipes": recipes_mixer
})

objects_array.append({ "Class": r_dict,
	"Name": "Radiator" + r_dict,
	"Recipes": recipes_radiator
})

objects_array.append({ "Class": r_dict,
	"Name": "SolarPanel" + r_dict,
	"Recipes": recipes_solar
})

objects_array.append({ "Class": r_dict,
	"Name": "ChemReactor" + r_dict,
	"Recipes": recipes_chem
})

objects_array.append({ "Class": r_dict,
	"Name": "InductionCoil" + r_dict,
	"Recipes": recipes_coil
})

objects_array.append({ "Class": r_dict,
	"Name": "IndustrialSmelter" + r_dict,
	"Recipes": recipes_indu
})

objects_array.append({ "Class": r_dict,
	"Name": "HeatExchanger" + r_dict,
	"Recipes": recipes_exch
})

objects_array.append({ "Class": r_dict,
	"Name": "InverseHeatExchanger" + r_dict,
	"Recipes": recipes_iexch
})

objects_array.append({ "Class": r_dict,
	"Name": "CombustionEngine" + r_dict,
	"Recipes": recipes_combustion
})

objects_array.append({ "Class": r_dict,
	"Name": "PyrolysisUnit" + r_dict,
	"Recipes": recipes_pyro
})

objects_array.append({ "Class": r_dict,
	"Name": "CompactGenerator" + r_dict,
	"Recipes": recipes_compact_generator
})

objects_array.append({ "Class": r_dict,
	"Name": "FissionReactor" + r_dict,
	"Recipes": recipes_fission
})

objects_array.append({ "Class": r_dict,
	"Name": "AutomaticFarm" + r_dict,
	"Recipes": recipes_farm
})

objects_array.append({ "Class": r_dict,
	"Name": "AtmosphericCondenser" + r_dict,
	"Recipes": recipes_condens
})

objects_array.append({ "Class": r_dict,
	"Name": "Assembler" + r_dict,
	"Recipes": recipes_assembler
})

objects_array.append({ "Class": r_dict,
	"Name": "GasTurbine" + r_dict,
	"Recipes": recipes_gasturb
})

objects_array.append({ "Class": r_dict,
	"Name": "IndustrialChemReactor" + r_dict,
	"Recipes": recipes_industrial_chemreactor
})

objects_array.append({ "Class": r_dict,
	"Name": "Portal" + r_dict,
	"Recipes": recipes_portal
})

objects_array.append({ "Class": r_dict,
	"Name": "ChemicalBath" + r_dict,
	"Recipes": recipes_chemical_bath
})

objects_array.append({ "Class": r_dict,
	"Name": "Riteg" + r_dict,
	"Recipes": recipes_riteg
})

objects_array.append({ "Class": r_dict,
	"Name": "IndustrialSteamTurbine" + r_dict,
	"Recipes": recipes_industrial_steam_turbine
})

objects_array.append({ "Class": r_dict,
	"Name": "FusionReactor" + r_dict,
	"Recipes": recipes_fusion_reactor
})

objects_array.append({ "Class": r_dict,
	"Name": "IndustrialBoiler" + r_dict,
	"Recipes": recipes_industrial_boiler
})

objects_array.append({ "Class": r_dict,
	"Name": "IndustrialElectricEngine" + r_dict,
	"Recipes": recipes_industrial_electric_engine
})

objects_array.append({ "Class": r_dict,
	"Name": "KineticHeater" + r_dict,
	"Recipes": recipes_kinetic_heater
})

objects_array.append({ "Class": r_dict,
	"Name": "OilCrackingTower" + r_dict,
	"Recipes": oil_crack
})

objects_array.append({ "Class": r_dict,
	"Name": "Hand" + r_dict,
	"Recipes": recipes_hand
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/misc.json", data);