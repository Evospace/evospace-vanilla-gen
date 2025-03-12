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

oil_crack = []

def append_recipe(recipe):
	recipes_hand.append(recipe)
	recipes_assembler.append(recipe)

def append_recipe_hand_press(recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]
	
	dec_recipe = copy.deepcopy(recipe)

	recipes_hand.append(recipe)
	
	output = copy.deepcopy(dec_recipe["Input"])
	
	dec_recipe["Ticks"] = 60
	recipes_press.append(dec_recipe)		

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
	"Input": one_item("Water", 2000),
	"Output":{
		"Items":[
		]
	},
	"Ticks" : 200,
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumPlate1",
	"Input":{
		"Items":[
			{
				"Name": "ProducerGas",
				"Count": 1000
			}
		]
	},
	"Output": one_item("HotNeutroniumPlate", 1),
	"Ticks" : 200,
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumPlate2",
	"Input":{
		"Items":[
			{
				"Name": "ProducerGas",
				"Count": 3000
			}
		]
	},
	"Output": one_item("HotNeutroniumPlate", 3),
	"Ticks" : 300,
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumPlate4",
	"Input":{
		"Items":[
			{
				"Name": "UltimateCatalyst",
				"Count": 1,
				"Probability":0
			}
		]
	},
	"Output": one_item("HotNeutroniumPlate", 1),
	"Ticks" : 200,
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumPlate3",
	"Input":{
		"Items":[
			{
				"Name": "UltimateCatalyst",
				"Count": 3,
				"Probability":0
			}
		]
	},
	"Output": one_item("HotNeutroniumPlate", 3),
	"Ticks" : 300,
})

recipes_smelter.append({
	"Name":"Glass",
	"Input": one_item("SandSurface"),
	"Output": one_item("Glass"),
	"Ticks" : 100,
})

# other		
		
recipes_hand.append({
	"Name":"Circuit",
	"Input": items([
		["CircuitBoard"],
		["Triod", 3]
	]),
	"Output": one_item("Circuit"),
	"Ticks" : 200,
	"Tier": 1,
})

recipes_assembler.append({
	"Name":"AltCircuit",
	"Input": items([
		["CircuitBoard"],
		["Transistor", 2]
	]),
	"Output": one_item("Circuit"),
	"Ticks" : 200,
	"Tier": 2,
})

recipes_hand.append({
	"Name":"Triod",
	"Input": items([
		["Glass"],
		["CopperWire", 3]
	]),
	"Output": one_item("Triod"),
	"Ticks" : 120,
	"Tier": 1,
})

recipes_hand.append({
	"Name":"Resistor",
	"Input": items([
		["CoalDust"],
		["Organics"],
		["CopperWire", 1]
	]),
	"Output": one_item("Resistor"),
	"Ticks" : 60,
	"Tier": 1,
})

recipes_assembler.append({
	"Name":"AltResistor",
	"Input": items([
		["CoalDust"],
		["Organics"],
		["GoldWire"]
	]),
	"Output": one_item("Resistor", 2),
	"Ticks" : 60,
	"Tier": 2,
})

recipes_assembler.append({
	"Name":"AltResistor2",
	"Input": items([
		["PolyethyleneSheet"],
		["GoldWire"]
	]),
	"Output": one_item("Resistor", 4),
	"Ticks" : 60,
	"Tier": 3,
})

recipes_assembler.append({
	"Name":"AltResistor3",
	"Input": items([
		["PTFESheet"],
		["NiobiumWire"]
	]),
	"Output": one_item("Resistor", 8),
	"Ticks" : 60,
	"Tier": 4,
})

recipes_assembler.append({
	"Name":"AltResistor4",
	"Input": items([
		["PTFESheet"],
		["TantalumWire"]
	]),
	"Output": one_item("Resistor", 16),
	"Ticks" : 60,
	"Tier": 5,
})

recipes_hand.append({
	"Name":"AdvancedCircuit",
	"Input": items([
		["CircuitBoard"],
		["Resistor", 2],
		["Circuit", 3]
	]),
	"Output": one_item("AdvancedCircuit"),
	"Ticks" : 200,
	"Tier": 1,
})

recipes_assembler.append({
	"Name":"AltAdvancedCircuit",
	"Input": items([
		["CircuitBoard"],
		["Transistor", 2],
		["Resistor", 3],
	]),
	"Output": one_item("AdvancedCircuit"),
	"Ticks" : 200,
	"Tier": 2,
})

recipes_assembler.append({
	"Name":"SiliconWafer",
	"Input": one_item("SiliconMonocrystal"),
	"Output": one_item("SiliconWafer", 16),
	"Ticks" : 200,
	"Tier": 3,
})

recipes_assembler.append({
	"Name":"DopedSiliconWafer",
	"Input": one_item("DopedSiliconMonocrystal"),
	"Output": one_item("DopedSiliconWafer", 16),
	"Ticks" : 200,
	"Tier": 4,
})

recipes_assembler.append({
	"Name":"IntegratedCircuit",
	"Input": one_item("SiliconWafer"),
	"Output": one_item("IntegratedCircuit", 4),
	"Ticks" : 200,
	"Tier": 3,
})

recipes_assembler.append({
	"Name":"AltIntegratedCircuit",
	"Input": one_item("DopedSiliconWafer"),
	"Output": one_item("IntegratedCircuit", 8),
	"Ticks" : 200,
	"Tier": 3,
})

recipes_assembler.append({
	"Name":"SystemOnChip",
	"Input": one_item("DopedSiliconWafer"),
	"Output": one_item("SystemOnChip", 4),
	"Ticks" : 200,
	"Tier": 3,
})

recipes_hand.append({
	"Name":"Processor",
	"Input": items([
		["CircuitBoard"],
		["AdvancedCircuit", 3],
		["Capacitor", 1],
	]),
	"Output": one_item("Processor"),
	"Ticks" : 200,
	"Tier": 3,
})

recipes_assembler.append({
	"Name":"AltProcessor",
	"Input": items([
		["CircuitBoard"],
		["AdvancedCircuit", 1],
		["IntegratedCircuit", 2],
		["Capacitor", 2],
	]),
	"Output": one_item("Processor"),
	"Ticks" : 200,
	"Tier": 4,
})

recipes_assembler.append({
	"Name":"AltProcessor2",
	"Input": items([
		["CircuitBoard"],
		["SystemOnChip", 1],
		["Capacitor", 3],
	]),
	"Output": one_item("Processor"),
	"Ticks" : 200,
	"Tier": 5,
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
	"Output": one_item("AdvancedCircuitBoard"),
	"Ticks" : 80,
	"Tier": 3,
})

append_recipe({
	"Name":"QuantumCore",
	"Input":{
		"Items":[
			{
				"Name": "YttriumDust",
				"Count": 1
			},	
			{
				"Name": "CopperParts",
				"Count": 2
			}
		]
	},
	"Output": one_item("QuantumCore"),
	"Ticks" : 200,
	"Tier": 4,
	
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
	"Output": one_item("QuantumCircuit"),
	"Ticks" : 200,
	"Tier": 4,
})

append_recipe({
	"Name":"QuantumProcessor",
	"Input":{
		"Items":[
			{
				"Name": "QuantumCircuit",
				"Count": 2
			},	
			{
				"Name": "DecisionResonator",
				"Count": 1
			}
		]
	},
	"Output": one_item("QuantumProcessor"),
	"Ticks" : 200,
	"Tier": 5,
})

recipes_industrial_chemreactor.append({
	"Name":"Tetrafluoroethylene",
	"Input":{
		"Items":[
			{
				"Name": "Fluorine",
				"Count": 500
			},	
			{
				"Name": "Ethylene",
				"Count": 1000
			}
		]
	},
	"Output": one_item("Tetrafluoroethylene", 1000),
	"Ticks" : 200,
	"Tier": 5,
})

recipes_industrial_chemreactor.append({
	"Name":"PTFE",
	"Input":{
		"Items":[
			{
				"Name": "Tetrafluoroethylene",
				"Count": 1000
			},	
			{
				"Name": "Oxygen",
				"Count": 500
			}
		]
	},
	"Output": one_item("PTFE", 1000),
	"Ticks" : 600,
	"Tier": 5,
})

recipes_industrial_chemreactor.append({
	"Name":"BrainMatrix",
	"Input":{
		"Items":[
			{
				"Name": "CarbonFiberSheet",
				"Count": 1
			},	
			{
				"Name": "PTFE",
				"Count": 1
			}
		]
	},
	"Output": one_item("BrainMatrix"),
	"Ticks" : 200,
	"Tier": 5,
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
				"Name": "BrainMatrix",
				"Count": 1
			}
		]
	},
	"Output": one_item("QuantumBrain"),
	"Ticks" : 200,
	"Tier": 6,
})

recipes_assembler.append({
	"Name":"SuperconductorWire",
	"Input":{
		"Items":[
			{
				"Name": "SuperconductorPlate",
				"Count": 1
			},
		]
	},
	"Output": one_item("SuperconductorWire", 2),
	"Ticks" : 100,
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
	"Output": one_item("UltimateCatalyst"),
	"Ticks" : 200,
	"Tier": 7,
})

append_recipe({
	"Name":"Catalyst",
	"Input": items([
		["Cell"],
		["GoldWire", 10],
		["Coal", 4]
	]),
	"Output": one_item("Catalyst"),
	"Ticks" : 200,
	
})

append_recipe({
	"Name": "PrimitiveBattery",
	"Input": items([
		["Coke"],
		["AluminiumParts"],
		["SteelPlate"]
	]),
	"Output": one_item("PrimitiveBattery"),
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
		"Output": one_item(name),
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
	"Output": one_item("Cell"),
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
	"Output": one_item("ThoriumCell"),
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
	"Output": one_item("Uranium233Cell"),
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
	"Output": one_item("PlutoniumCell"),
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
	"Output": one_item("Battery"),
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
	"Output": one_item("Battery", 10),
	"Ticks" : 300,
	
})

recipes_assembler.append({
	"Name":"CompositePlate",
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
	"Output": one_item("CompositePlate"),
	"Ticks" : 300,
	
})

recipes_assembler.append({
	"Name":"GoldWire",
	"Input": one_item("GoldPlate"),
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
	"Output": one_item("ReflectorCell"),
	"Ticks" : 100,
})

#TODO: remove
append_recipe({
	"Name":"ControlCell",
	"Input":{
		"Items":[
			{
				"Name": "Cell",
				"Count": 1
			},
			{
				"Name": "YttriumDust",
				"Count": 3
			},
		]
	},
	"Output": one_item("ControlCell"),
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
	"Name":"Air",
	"Input":{
		"Items":[
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Air",
				"Count": 500
			}
		]
	},
	"Ticks" : 20,
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
	"Input": one_item("DepletedUraniumCell"),
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
	"Output": one_item("DepletedUraniumCell"),
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
				"Count": 4,
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
				"Count": 4,
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
				"Count": 8,
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
	"Output": one_item("DepletedUraniumCell"),
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

recipes_electrolyzer.append({
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
				"Name": "Sulfur",
				"Count": 1
			},{
				"Name": "Mercury",
				"Count": 1000
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

# Using this for all converters
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

for item, mul in [["Coal", 1], ["CoalDust", 1], ["CoalOreDust", 1], ["CoalOreGravel", 1.5], ["CoalOreImpureGravel", 1.5], ["CoalOre", 2]]:
	recipes_oven.append({
		"Name": item+"ToCoke",
		"Input":{
			"Items":[
				{
					"Name": item,
					"Count": 10
				}
			]
		},
		"Output":{
			"Items":[
				{
					"Name": "Coke",
					"Count": 10 * mul
				},
				{
					"Name": "Creosote",
					"Count": 500 * mul
				},
			]
		},
		"Ticks": 5*2*20*3 * mul,
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
				"Count": 250
			},
		]
	},
	"Ticks": 5*2*20*3,
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
				"Count": 150
			},
		]
	},
	"Ticks": 3*2*20*3,
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
				"Count": 100
			},
		]
	},
	"Ticks": 2*2*20*3,
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
					"Name": "SteelPlate",
					"Count": 10
				}
			]
		},
		"Ticks" : 10*5*20*2
	})
	recipes_blast_furnace.append({
		"Name": "IronPlateSmelting",
		"Input":{
			"Items":[
				{
					"Name": fuel_type,
					"Count": 10
				},
				{
					"Name": "IronPlate",
					"Count": 10
				},
			]
		},
		"Output":{
			"Items":[
				{
					"Name": "SteelPlate",
					"Count": 10
				}
			]
		},
		"Ticks" : 10*5*20*2
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
	"Output": one_item("PreparedTitaniumOxideDust"),
	"Ticks" : 200,
	"Scaled": False,
})

recipes_sep.append({
	"Name": "PlutoniumDust",
	"Input": one_item("DepletedUraniumCell"),
	"Output":{
		"Items": [
			{
				"Name":"Cell",
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

recipes_sep.append({
	"Name":"Sand",
	"Input": one_item("SandSurface"),
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
	"Name": "SandSurfaceSmelting",
	"Input": one_item("SandSurface"),
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
	if "Parts" in material and "Plate" in material["Parts"]:
		if "SmeltLevel" in material and material["SmeltLevel"] <= 3:
			recipes_arc_furnace.append({
				"Name": material["Name"] + "Plate",
				"Input": one_item(material["Name"] + "Dust"),
				"Output":{
					"Items":[
						{
							"Name": material["Name"] + "Plate",
							"Count": 1
						}
					]
				},
				"Tier": extract_tier(material),
				"Ticks" : 200
			})

recipes_macerator.append({
	"Name": "Pumpkin",
	"Input": one_item("Pumpkin"),
	"Output": one_item("Organics"),
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
	"Output": one_item("Organics"),
	"Tier": 0,
	"Ticks" : 200
})

recipes_macerator.append({
	"Name": "Emerald",
	"Input": one_item("EmeraldCrystal"),
	"Output": one_item("EmeraldDust", 4),
	"Tier": 5,
	"Ticks" : 80,
})

for material in {"Ruby", "Malachite"}:
	recipes_macerator.append({
		"Name": material+"Crystal",
		"Input": one_item(material+"Crystal"),
		"Output": one_item(material+"Dust", 4),
		"Tier": 3,
		"Ticks" : 80,
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
	"Tier": 1,
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
	"Name":"SpongeToPlate",
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
				"Name": "TitaniumPlate",
				"Count": 1
			},
			{
				"Name": "HotMercury",
				"Count": 1000
			},
		]
	},
	"Tier": 5,
	"Ticks" : 200 * 2,
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
				"Name": "SuperconductorPlate",
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
	"Name":"TDustToPlate",
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
				"Name": "TitaniumPlate",
				"Count": 1
			},
			{
				"Name": "HotMercury",
				"Count": 100
			},
		]
	},
	"Tier": 5,
	"Ticks" : 40 * 2,
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

#TODO: remove
recipes_mixer.append({
	"Name": "SuperconductorDust",
	"Input":{
		"Items":[
			{
				"Name": "GoldDust",
				"Count": 3
			},
			{
				"Name": "YttriumDust",
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
	"Name": "ElectrolyzerPyriteDust",
	"Input": one_item("PyriteDust", 2),
	"Output":{
		"Items": [
			{
				"Name": "IronDust",
				"Count": 1
			},{
				"Name": "Sulfur",
				"Count": 1
			}
		]
	},
	"Ticks": 200,
})	
recipes_electrolyzer.append({
	"Name": "ElectrolyzerChalcopyriteDust",
	"Input": one_item("ChalcopyriteDust", 2),
	"Output":{
		"Items": [
			{
				"Name": "CopperDust",
				"Count": 1
			},{
				"Name": "Sulfur",
				"Count": 1
			}
		]
	},
	"Ticks": 100*2,
})
recipes_electrolyzer.append({
	"Name": "ElectrolyzerMagnetiteDust",
	"Input": one_item("MagnetiteDust", 2),
	"Output":{
		"Items": [
			{
				"Name": "IronDust",
				"Count": 1
			},{
				"Name": "Oxygen",
				"Count": 1000
			}
		]
	},
	"Ticks": 200,
})
recipes_electrolyzer.append({
	"Name": "ElectrolyzerMalachiteDust",
	"Input": one_item("MalachiteDust", 2),
	"Output":{
		"Items": [
			{
				"Name": "CopperDust",
				"Count": 1
			},{
				"Name": "Oxygen",
				"Count": 1000
			}
		]
	},
	"Ticks": 200,
})
recipes_electrolyzer.append({
	"Name": "ElectrolyzerBauxiteDust",
	"Input": one_item("BauxiteDust", 12),
	"Output":{
		"Items": [
			{
				"Name": "AluminiumOxideDust",
				"Count": 6
			},{
				"Name": "TitaniumOxideDust",
				"Count": 1
			},{
				"Name": "Oxygen",
				"Count": 5000
			}
		]
	},
	"Ticks": 200,
})
recipes_electrolyzer.append({
	"Name": "ElectrolyzerRubyDust",
	"Input": one_item("RubyDust", 8),
	"Output":{
		"Items": [
			{
				"Name": "AluminiumOxideDust",
				"Count": 4
			},{
				"Name": "ChromiumDust",
				"Count": 1
			},{
				"Name": "Oxygen",
				"Count": 3000
			}
		]
	},
	"Ticks": 200,
})

recipes_electrolyzer.append({
	"Name":"AluminiumOxideDust",
	"Input": one_item("AluminiumOxideDust"),
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
	"Input": one_item("EmeraldDust", 11),
	"Output":{
		"Items":[
			{
				"Name": "BerylliumDust",
				"Count": 3
			},
			{
				"Name": "AluminiumOxideDust",
				"Count": 2
			},
			{
				"Name": "SiliconOxide",
				"Count": 6
			}
		]
	},
	"Ticks" : 200
})

recipes_electrolyzer.append({
	"Name":"SandElectrolyze",
	"Input": one_item("SiliconOxide"),
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
	"Input": one_item("Salt"),
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
	"Input": one_item("Log"),
	"Output": one_item("Plank", 4),
	"Ticks" : 80,
})

recipes_cutter.append({
	"Name": "PlankToCircuitBoard",
	"Input": one_item("Plank"),
	"Output": one_item("CircuitBoard"),
	"Ticks": 80,
	"Tier": 1
})
recipes_cutter.append({
	"Name": "PlasticToCircuitBoard",
	"Input": one_item("Plastic"),
	"Output": one_item("CircuitBoard", 4),
	"Ticks": 80,
	"Tier": 3,
})
recipes_cutter.append({
	"Name":"StoneTiles",
	"Input": one_item("StoneSurface"),
	"Output": one_item("StoneTiles"),
	"Ticks" : 100
})
recipes_cutter.append({
	"Name":"DarkTiles",
	"Input": one_item("DarkStoneSurface"),
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
	"Input": one_item("RedStoneSurface"),
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
	"Input": one_item("StoneTiles"),
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
	"Input": one_item("RedTiles"),
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
	"Input": one_item("DarkTiles"),
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
	"Input": one_item("Terracotta"),
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
	"Input": one_item("TerracottaTiles"),
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
	"Input": one_item("Concrete"),
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
	"Input": one_item("ConcreteTiles"),
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
	"Input": one_item("ConcreteSmallTiles"),
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
	"Input": one_item("ReinforcedConcrete"),
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
	"Input": one_item("ReinforcedConcreteTiles"),
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
	"Input": one_item("ReinforcedConcreteSmallTiles"),
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
	"Input": one_item("Rapeseed"),
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
				"Count": 100
			},
			{
				"Name": "Water",
				"Count": 900
			}
		]
	},
	
	"Ticks" : 200*3
})

recipes_ferm.append({
	"Name": "MethaneFromPumpkin",
	"Input": one_item("Pumpkin"),
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
	"Input": one_item("RawOil", 2000),
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
	"Input": one_item("RawOil", 2000),
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
	"Input": one_item("Methane", 800*5),
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
	"Input": one_item("FermentedBiomass", 1000),
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
	"Input": one_item("ProducerGas", 1000),
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
	"Input": one_item("Ash", 3),
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
	"Name": "CarbonMonoxide",
	"Input":{
		"Items":[
			{
				"Name": "CoalDust",
				"Count": 1
			},
			{
				"Name": "Oxygen",
				"Count": 500
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "CarbonMonoxide",
				"Count": 250
			},		
		]
	},
	"Ticks" : 100
})

recipes_industrial_chemreactor.append({
	"Name": "AmmoniumChloride",
	"Input":{
		"Items":[
			{
				"Name": "Ammonia",
				"Count": 500
			},
			{
				"Name": "Chlorine",
				"Count": 500
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "AmmoniumChloride",
				"Count": 1
			},		
		]
	},
	"Ticks" : 100
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
	"Name": "AquaRegia",
	"Input":{
		"Items":[
			{
				"Name": "NitricAcid",
				"Count": 500
			},
			{
				"Name": "HydrochloricAcid",
				"Count": 1500
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "AquaRegia",
				"Count": 1000
			},		
		]
	},
	"Ticks" : 60,
	"Colors": [[0.0,0.5,0.25,0.3],[0.9,0.5,0.25,0.3]]
})

recipes_industrial_chemreactor.append({
	"Name": "PlatinumRhodiumSolution",
	"Input":{
		"Items":[
			{
				"Name": "PyroplatiteDust",
				"Count": 10
			},
			{
				"Name": "AquaRegia",
				"Count": 1000
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "PlatinumRhodiumSolution",
				"Count": 1000
			},		
		]
	},
	"Ticks" : 800,
	"Colors": [[0.0,0.5,0.25,0.3],[0.9,0.5,0.25,0.3]]
})

recipes_industrial_chemreactor.append({
	"Name": "RhodiumSolution",
	"Input":{
		"Items":[
			{
				"Name": "PlatinumRhodiumSolution",
				"Count": 1300
			},
			{
				"Name": "AmmoniumChloride",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "PlatinumDust",
				"Count": 1
			},
			{
				"Name": "RhodiumSolution",
				"Count": 300
			},		
		]
	},
	"Ticks" : 400,
	"Colors": [[0.0,0.5,0.25,0.3],[0.9,0.5,0.25,0.3]]
})

recipes_electrolyzer.append({
	"Name": "RhodiumDust",
	"Input":{
		"Items":[
			{
				"Name": "RhodiumSolution",
				"Count": 1000
			}
		]
	},
	"Output":{
		"Items":[	
			{
				"Name": "RhodiumDust",
				"Count": 1
			}	
		]
	},
	"Ticks" : 400,
	"Colors": [[0.0,0.5,0.25,0.3],[0.9,0.5,0.25,0.3]]
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
	
recipes_chemical_bath.append({
	"Name":"RareEarthSludge",
	"Input":{
		"Items":[
			{
				"Name": "ClayDust",
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
				"Name": "RareEarthSludge",
				"Count": 2
			}
		]
	},
	"Ticks" : 500,
	"Colors": [[0.8,0.8,0.1,0.3],[0.7,0.2,0.7,0.8]]
})

recipes_chemical_bath.append({
	"Name":"RareEarthSludge",
	"Input":{
		"Items":[
			{
				"Name": "RareEarthSludge",
				"Count": 1
			},
			{
				"Name": "Ammonia",
				"Count": 300
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "YttriumDust",
				"Count": 2
			}
		]
	},
	"Ticks" : 200,
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
	"Output": one_item("MothershipPing"),
	"Ticks" : 1000
})

append_recipe_hand_press({
	"Name": "Column",
	"Input": one_item("StoneSurface"),
	"Output": one_item("Column"),
	"Ticks" : 20
})

append_recipe_hand_press({
	"Name": "FluetedColumn",
	"Input": one_item("Column"),
	"Output": one_item("FluetedColumn"),
	"Ticks" : 20
})

append_recipe_hand_press({
	"Name":"GlassBlock",
	"Input": one_item("Glass"),
	"Output": one_item("GlassBlock"),
	"Ticks" : 10
})

append_recipe_hand_press({
	"Name":"PlasticBlock",
	"Input": one_item("Plastic"),
	"Output": one_item("PlasticBlock"),
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
	"Input": one_item("SandSurface"),
	"Output": one_item("BasicPlatform"),
	"Ticks" : 10
})

append_recipe_hand_press({
	"Name":"RustyCopperCasing",
	"Input": one_item("CopperCasing"),
	"Output": one_item("RustyCopperCasing"),
	"Ticks" : 20
})

append_recipe_hand_press({
	"Name":"RustyIronCasing",
	"Input": one_item("SteelCasing"),
	"Output": one_item("RustyIronCasing"),
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
	"Name": "Pump" + r_dict,
	"Recipes": recipes_pump
})

objects_array.append({ "Class": r_dict,
	"Name": "Separator" + r_dict,
	"Recipes": recipes_sep
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
	"Name": assembler_r_dict,
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