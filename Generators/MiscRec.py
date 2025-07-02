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
recipes_ferm = []
recipes_toolarm = []
recipes_hammer = []
recipes_mixer = []
recipes_chem = []

pumpjack = []

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

def append_recipe_hand(recipe):
	recipes_hand.append(recipe)	

recipes_industrial_boiler.append({
	"Name":"Boiling",
	"Input": one_item("Water", 2000),
	"Output": no_items(),
	"Ticks" : 200,
})

recipes_industrial_chemreactor.append({
	"Name":"NeutroniumPlate",
	"Input": items([
		["HotNeutroniumPlate"],
		["Mercury", 2000]
	]),
	"Output": items([
		["NeutroniumPlate"],
		["HotMercury", 2000]
	]),
	"Ticks" : 200,
	"Tier": 6
})

recipes_industrial_chemreactor.append({
	"Name":"SynthesisCell",
	"Input": items([
		["Cell"],
		["ProducerGas", 3000]
	]),
	"Output": one_item("SynthesisCell"),
	"Ticks" : 200,
	"Tier": 6
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumPlate1",
	"Input": one_item("SynthesisCell", 2),
	"Output": items([
		["HotNeutroniumPlate"],
		["Cell"],
	]),
	"Ticks" : 200
})

recipes_fusion_reactor.append({
	"Name":"HotNeutroniumPlate2",
	"Input":{
		"Items":[
			{
				"Name": "SynthesisCell",
				"Count": 1
			},{
				"Name": "UltimateCatalyst",
				"Count": 1,
				"Probability":0
			}
		]
	},
	"Output": items([
		["HotNeutroniumPlate"],
		["Cell"],
	]),
	"Ticks" : 200,
})

recipes_smelter.append({
	"Name":"Glass",
	"Input": one_item("SandSurface"),
	"Output": one_item("Glass"),
	"Ticks" : 100,
})

# other		

recipes_hand.append({
	"Name":"CircuitBoard",
	"Input": one_item("Log"),
	"Output": one_item("CircuitBoard"),
	"Ticks" : 20,
	"Tier": 1
})

recipes_assembler.append({
	"Name":"CircuitBoard2",
	"Input": items([
		["Log", 1],
		["PolyethyleneSheet", 2]
	]),
	"Output": one_item("CircuitBoard", 4),
	"Ticks" : 20,
	"Tier": 4
})

recipes_assembler.append({
	"Name":"CircuitBoard3",
	"Input": items([
		["CarbonFiberSheet", 1],
		["PolyethyleneSheet", 2],
	]),
	"Output": one_item("CircuitBoard", 8),
	"Ticks" : 20,
	"Tier": 5
})
		
recipes_hand.append({
	"Name":"Circuit",
	"Input": items([
		["CircuitBoard"],
		["Triod", 3]
	]),
	"Output": one_item("Circuit"),
	"Ticks" : 150,
	"Tier": 1,
})

recipes_assembler.append({
	"Name":"Circuit2",
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
	"Ticks" : 50,
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
	"Name":"Resistor2",
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
	"Name":"Resistor3",
	"Input": items([
		["GoldWire"],
		["PolyethyleneSheet"],
	]),
	"Output": one_item("Resistor", 4),
	"Ticks" : 60,
	"Tier": 3,
})

recipes_assembler.append({
	"Name":"Resistor4",
	"Input": items([
		["TantalumWire"],
		["PolyethyleneSheet"],
	]),
	"Output": one_item("Resistor", 8),
	"Ticks" : 60,
	"Tier": 5
})

recipes_assembler.append({
	"Name":"Resistor5",
	"Input": items([
		["TantalumWire"],
		["CarbonFiberSheet"],
		["PolyethyleneSheet"],
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
	"Name":"AdvancedCircuit2",
	"Input": items([
		["CircuitBoard"],
		["Transistor", 2],
		["Resistor", 3],
	]),
	"Output": one_item("AdvancedCircuit"),
	"Ticks" : 200,
	"Tier": 2,
})

recipes_hand.append({
    "Name": "Transistor",
    "Input": items([
        ["Silicon", 1],
        ["CopperWire", 2]
    ]),
    "Output": one_item("Transistor"),
    "Ticks": 80,
    "Tier": 1,
})

recipes_assembler.append({
    "Name": "Transistor2",
    "Input": items([
        ["Silicon", 1],
        ["GoldWire", 1],
        ["PolyethyleneSheet", 1]
    ]),
    "Output": one_item("Transistor", 2),
    "Ticks": 60,
    "Tier": 2,
})

recipes_assembler.append({
    "Name": "Transistor3",
    "Input": items([
        ["SiliconWafer", 1],
        ["GoldWire", 4],
        ["PolyethyleneSheet", 1]
    ]),
    "Output": one_item("Transistor", 8),
    "Ticks": 60,
    "Tier": 3,
})

recipes_assembler.append({
    "Name": "Transistor4",
    "Input": items([
        ["DopedSiliconWafer", 1],
        ["PlatinumWire", 2],
        ["PolyethyleneSheet", 1]
    ]),
    "Output": one_item("Transistor", 16),
    "Ticks": 60,
    "Tier": 4,
})

recipes_hand.append({
    "Name": "Capacitor",
    "Input": items([
        ["AluminiumFoil", 2],
        ["Log", 1]
    ]),
    "Output": one_item("Capacitor"),
    "Ticks": 80,
    "Tier": 1,
})

recipes_assembler.append({
    "Name": "Capacitor2",
    "Input": items([
        ["AluminiumFoil", 2],
        ["MicaFlakes", 1]
    ]),
    "Output": one_item("Capacitor", 2),
    "Ticks": 60,
    "Tier": 2,
})

recipes_assembler.append({
    "Name": "Capacitor3",
    "Input": items([
        ["TantalumFoil", 2],
        ["PolyethyleneSheet", 1]
    ]),
    "Output": one_item("Capacitor", 4),
    "Ticks": 60,
    "Tier": 5,
})

recipes_assembler.append({
    "Name": "Capacitor4",
    "Input": items([
        ["TantalumFoil", 2],
		["CarbonFiberSheet", 1],
        ["PolyethyleneSheet", 1]
    ]),
    "Output": one_item("Capacitor", 8),
    "Ticks": 60,
    "Tier": 5,
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

recipes_hand.append({
	"Name":"Processor",
	"Input": items([
		["CircuitBoard"],
		["AdvancedCircuit", 3],
		["Resistor", 2],
	]),
	"Output": one_item("Processor"),
	"Ticks" : 200,
	"Tier": 3,
})

recipes_assembler.append({
	"Name":"Processor2",
	"Input": items([
		["CircuitBoard"],
		["AdvancedCircuit", 2],
		["SiliconWafer", 1],
		["Capacitor", 2],
	]),
	"Output": one_item("Processor"),
	"Ticks" : 200,
	"Tier": 4,
})

recipes_assembler.append({
	"Name":"Processor3",
	"Input": items([
		["CircuitBoard"],
		["DopedSiliconWafer", 1],
		["Resistor", 2],
		["Capacitor", 3],
	]),
	"Output": one_item("Processor", 2),
	"Ticks" : 200,
	"Tier": 5,
})

recipes_hand.append({
	"Name":"QuantumCore",
	"Input":items([
		["YttriumDust", 1],
		["CopperParts", 3]
	]),
	"Output": one_item("QuantumCore"),
	"Ticks" : 100,
	"Tier": 4,
})
recipes_assembler.append({
	"Name":"QuantumCore",
	"Input":items([
		["YttriumDust", 2],
		["CompositePlate", 1]
	]),
	"Output": one_item("QuantumCore", 2),
	"Ticks" : 100,
	"Tier": 5,
})

recipes_hand.append({
	"Name":"QuantumCircuit",
	"Input": items([
		["QuantumCore", 2],
		["Processor", 3],
		["Resistor", 6]
	]),
	"Output": one_item("QuantumCircuit"),
	"Ticks" : 200,
	"Tier": 4,
})

recipes_assembler.append({
	"Name":"QuantumCircuit2",
	"Input": items([
		["QuantumCore", 2],
		["Processor", 2],
		["Resistor", 6],
		["Transistor", 6]
	]),
	"Output": one_item("QuantumCircuit"),
	"Ticks" : 200,
	"Tier": 4,
})

recipes_hand.append({
	"Name":"QuantumProcessor",
	"Input": items([
		["QuantumCircuit", 3],
		["DecisionResonator", 1],
		["Capacitor", 6]
	]),
	"Output": one_item("QuantumProcessor"),
	"Ticks" : 200,
	"Tier": 5,
})

recipes_assembler.append({
	"Name":"QuantumProcessor2",
	"Input": items([
		["QuantumCircuit", 2],
		["DecisionResonator", 1],
		["Capacitor", 6],
		["Transistor", 6]
	]),
	"Output": one_item("QuantumProcessor"),
	"Ticks" : 200,
	"Tier": 5,
})

recipes_industrial_chemreactor.append({
	"Name":"PolyethyleneSheet",
	"Input": items([
		["Ethylene", 1000],
		["Catalyst", 1, 0]
	]),
	"Output": one_item("PolyethyleneSheet", 10),
	"Ticks" : 600,
	"Tier": 3,
})

recipes_hand.append({
	"Name":"QuantumBrain",
	"Input": items([
		["QuantumProcessor", 3],
		["BrainMatrix"],
		["Resistor", 10]
	]),
	"Output": one_item("QuantumBrain"),
	"Ticks" : 200,
	"Tier": 6,
})

recipes_assembler.append({
	"Name":"QuantumBrain2",
	"Input": items([
		["QuantumProcessor", 2],
		["BrainMatrix"],
		["Resistor", 10],
		["UltimateCatalyst"]
	]),
	"Output": one_item("QuantumBrain"),
	"Ticks" : 200,
	"Tier": 6,
})

recipes_hand.append({
	"Name":"UltimateCatalyst",
	"Input": items([
		["Cell"],
		["NeutroniumParts", 2],
		["Coke", 10]
	]),
	"Output": one_item("UltimateCatalyst"),
	"Ticks" : 200,
	"Tier": 7,
})

recipes_hand.append({
	"Name":"Catalyst",
	"Input": items([
		["Cell"],
		["CopperWire", 40],
		["Coal", 4]
	]),
	"Output": one_item("Catalyst"),
	"Ticks" : 200,
	"Tier": 3
})

recipes_assembler.append({
	"Name":"Catalyst2",
	"Input": items([
		["Cell"],
		["GoldWire", 10],
		["Coal", 4]
	]),
	"Output": one_item("Catalyst"),
	"Ticks" : 200,
	"Tier": 4
})

recipes_hand.append({
	"Name": "PrimitiveBattery",
	"Input": items([
		["Coke"],
		["AluminiumParts"],
		["SteelPlate"]
	]),
	"Output": one_item("PrimitiveBattery"),
	"Ticks" : 100,
	"Tier": 3
})

for miscBlock in ["BasicPlatform", "Bricks", "GlassBlock", "WoodenPlanks", "StoneTiles", "RedTiles", "DarkTiles", "Terracotta", "TerracottaTiles", "RedBricks", "DarkBricks", "TerracottaBricks"]:
	recipes_hand.append({
		"Name": miscBlock,
		"Input": items([
			["BuildingMaterial", 2]
		]),
		"Output": one_item(miscBlock),
		"Ticks" : 10,
		"Tier": 1
	})
for miscBlock in ["Concrete", "ConcreteBricks", "ConcreteTiles", "ConcreteSmallTiles", "PlasticBlock"]:
	recipes_hand.append({
		"Name": miscBlock,
		"Input": items([
			["BuildingMaterial", 4]
		]),
		"Output": one_item(miscBlock),
		"Ticks" : 10,
		"Tier": 2
	})
for miscBlock in ["ReinforcedConcrete", "ReinforcedConcreteTiles", "ReinforcedConcreteSmallTiles", "ReinforcedConcreteBricks", "DangerBlock"]:
	recipes_hand.append({
		"Name": miscBlock,
		"Input": items([
			["BuildingMaterial", 8]
		]),
		"Output": one_item(miscBlock),
		"Ticks" : 10,
		"Tier": 3
	})

for miscBlock in ["Column", "FluetedColumn", "Chair", "CopperChair", "Ladder", "Door", "Window", "PlasticWindow", "Table", "Bed", "Rack", "WoodenStairs", "Fence", "SteelFence", "StainlessSteelFence"]:
	recipes_hand.append({
		"Name": miscBlock,
		"Input": items([
			["BuildingMaterial", 3]
		]),
		"Output": one_item(miscBlock),
		"Ticks" : 20,
		"Tier": 1
	})
		
for level, name, copm_name in zip(range(0, 4), ["BasicBattery", "AdvancedBattery", "SuperiorBattery", "UltimateBattery"], ["Battery", "BasicBattery", "AdvancedBattery", "SuperiorBattery"]):
	recipes_hand.append({
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

recipes_hand.append({
	"Name":"Cell",
	"Input": items([
		["AluminiumPlate"],
		["AluminiumParts"]
	]),
	"Output": one_item("Cell"),
	"Ticks": 200,
	"Tier": 3
})

recipes_hand.append({
	"Name":"BasicCoil",
	"Input": items([
		["CopperWire", 16],
		["SteelPlate", 2]
	]),
	"Output": one_item("BasicCoil"),
	"Ticks" : 200,
	"Tier": 2,
})

recipes_hand.append({
	"Name":"AdvancedCoil",
	"Input": items([
		["BasicCoil", 3],
		["StainlessSteelPlate", 2]
	]),
	"Output": one_item("AdvancedCoil"),
	"Ticks" : 200,
	"Tier": 3,
})

recipes_hand.append({
	"Name":"PowerCoil",
	"Input": items([
		["AdvancedCoil", 3],
		["Processor", 2]
	]),
	"Output": one_item("PowerCoil"),
	"Ticks" : 200,
	"Tier": 5,
})

recipes_hand.append({
	"Name":"BasicFrame",
	"Input": items([
		["SteelPlate", 4],
		["SteelParts", 4]
	]),
	"Output": one_item("BasicFrame"),
	"Ticks" : 200,
	"Tier": 2,
})

recipes_hand.append({
	"Name":"ReinforcedFrame",
	"Input": items([
		["BasicFrame", 3],
		["AluminiumParts", 6]
	]),
	"Output": one_item("ReinforcedFrame"),
	"Ticks" : 200,
	"Tier": 3,
})

recipes_hand.append({
	"Name":"ModularFrame",
	"Input": items([
		["ReinforcedFrame", 3],
		["StainlessSteelParts", 10]
	]),
	"Output": one_item("ModularFrame"),
	"Ticks" : 200,
	"Tier": 5,
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
	"Ticks" : 200*3,
	"Tier": 5,
})

recipes_hand.append({
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
	"Tier": 5,
})

recipes_hand.append({
	"Name":"ThoriumCell",
	"Input":{
		"Items":[
			{
				"Name": "ThoriumDust",
				"Count": 40
			},
			{
				"Name": "Cell",
				"Count": 1
			},
		]
	},
	"Output": one_item("ThoriumCell"),
	"Ticks" : 200,
	"Tier": 6,
})

recipes_hand.append({
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

recipes_hand.append({
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

recipes_assembler.append({
	"Name":"Battery",
	"Input": items([
		["SulfuricAcid", 100],
		["CopperParts"],
		["SteelPlate"]
	]),
	"Output": one_item("Battery"),
	"Ticks" : 200,
	"Tier": 4,
})

recipes_assembler.append({
	"Name":"CompositePlate",
	"Input": items([
		["TitaniumPlate", 1],
		["CarbonFiberSheet", 1],
		["PolyethyleneSheet", 1]
	]),
	"Output": one_item("CompositePlate"),
	"Ticks" : 300,
	"Tier": 6,
})

recipes_assembler.append({
	"Name":"CompositePlate2",
	"Input": items([
		["TitaniumPlate", 1],
		["CarbonFiberSheet", 1],
		["PolyethyleneSheet", 1],
		["NeutroniumParts", 1]
	]),
	"Output": one_item("CompositePlate", 4),
	"Ticks" : 300,
	"Tier": 7,
})

recipes_assembler.append({
	"Name":"GoldWire",
	"Input": one_item("GoldPlate"),
	"Output": one_item("GoldWire", 2),
	"Ticks" : 100,
})

recipes_hand.append({
	"Name":"ReflectorCell",
	"Input": items([
		["Cell"],
		["BerylliumDust", 3]
	]),
	"Output": one_item("ReflectorCell"),
	"Ticks" : 100,
})

recipes_hand.append({
	"Name":"PlatinumReflector",
	"Input": items([
		["Cell"],
		["PlatinumFoil"]
	]),
	"Output": one_item("PlatinumReflector"),
	"Ticks" : 100,
	"Tier": 6
})

recipes_hand.append({
	"Name":"BrainMatrix",
	"Input": items([
		["CarbonFiberSheet"],
		["PlatinumFoil"]
	]),
	"Output": one_item("BrainMatrix"),
	"Ticks" : 100,
	"Tier": 6
})

recipes_hand.append({
	"Name":"DecisionResonator",
	"Input": items([
		["StainlessSteelParts", 4],
		["MicaFlakes"]
	]),
	"Output": one_item("DecisionResonator"),
	"Ticks" : 100,
	"Tier": 5
})

recipes_assembler.append({
	"Name":"DecisionResonator2",
	"Input": items([
		["StainlessSteelParts", 4],
		["RubyCrystal"]
	]),
	"Output": one_item("DecisionResonator", 2),
	"Ticks" : 100,
	"Tier": 5
})

recipes_assembler.append({
	"Name":"DecisionResonator3",
	"Input": items([
		["StainlessSteelParts", 4],
		["SiliconWafer"],
		["CompositePlate"]
	]),
	"Output": one_item("DecisionResonator", 2),
	"Ticks" : 100,
	"Tier": 5
})

recipes_assembler.append({
	"Name":"DecisionResonator4",
	"Input": items([
		["StainlessSteelParts", 4],
		["DopedSiliconWafer"],
		["CompositePlate"]
	]),
	"Output": one_item("DecisionResonator", 4),
	"Ticks" : 100,
	"Tier": 5
})

#TODO: remove
append_recipe({
	"Name":"ControlCell",
	"Input":  items([
		["Cell"],
		["YttriumDust", 3]
	]),
	"Output": one_item("ControlCell"),
	"Ticks" : 100,
})

recipes_condens.append({
	"Name":"Water",
	"Input": no_items(),
	"Output": one_item("Water", 500),
	"Ticks" : 40,
})

recipes_condens.append({
	"Name":"Nitrogen",
	"Input": no_items(),
	"Output" :one_item("Nitrogen", 500),
	"Ticks" : 20,
})

recipes_farm.append({
	"Name":"Logs",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 1000
			}
		]
	},
	"Output": one_item("Log", 15),
	"Ticks" : 1200,
})

recipes_farm.append({
	"Name":"Pumpkin",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 1000
			}
		]
	},
	"Output": one_item("Pumpkin", 10),
	"Ticks" : 1200,
})

recipes_farm.append({
	"Name":"Grass",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 1000
			},
			{
				"Name": "DirtSurface",
				"Count": 15
			}
		]
	},
	"Output": one_item("GrassSurface", 15),
	"Ticks" : 1200,
})

recipes_farm.append({
	"Name":"Rapeseed",
	"Input":{
		"Items":[
			{
				"Name": "Water",
				"Count": 1000
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Rapeseed",
				"Count": 15
			}
		]
	},
	"Ticks" : 1200,
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
	"Tier": 5,
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
	"Ticks" : uranium_rod_output() / fission_output(),
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
	"Ticks" : (uranium_rod_output() / fission_output()) * 2.1,
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
				"Count": 2,
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
	"Ticks" : (uranium_rod_output() / fission_output()) * 3.2,
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
	"Ticks" : 1000,
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
	"Ticks" : 400,
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
	"Ticks" : 400,
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
	"Ticks" : (uranium_rod_output() / fission_output()) * 1.07,
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
	"Output": one_item("DepletedUraniumCell"),
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
	"Output": one_item("DepletedUraniumCell", 2),
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
	"Output": one_item("DepletedUraniumCell", 4),
	"Ticks" : 2000,
})

recipes_electrolyzer.append({
	"Name":"Hydrogen",
	"Input": one_item("Water", 800),
	"Output": one_item("Hydrogen", 400),
	"Ticks" : 200,
	"Tier": 4,
})
recipes_electrolyzer.append({
	"Name":"Oxygen",
	"Input": one_item("Water", 800),
	"Output": one_item("Oxygen", 200),
	"Ticks" : 200,
	"Tier": 4,
})
recipes_electrolyzer.append({
	"Name":"CinnabarDust",
	"Input": one_item("CinnabarDust", 2),
	"Output":{
		"Items":[
			{
				"Name": "Sulfur",
				"Count": 1
			},{
				"Name": "Mercury",
				"Count": 200
			}
		],
	},
	"Ticks" : 200,
	"Tier":2,
})
recipes_boiler.append({
	"Name": "Boiling",
	"Input": one_item("Water", 50),
	"Output": no_items(),
	"Ticks" : 200,
	"Loss": 10,
})

# Using this for all converters
recipes_generator.append({
	"Name": "Generating",
	"Input": no_items(),
	"Output": no_items(),
	"Ticks" : 200,
	"Loss": 10,
})

recipes_industrial_electric_engine.append({
	"Name": "Rotating",
	"Input": no_items(),
	"Output": no_items(),
	"Loss": 10,
	"Ticks": 200,
})

for item, mul in [["Coal", 1], ["CoalDust", 1], ["CoalOreDust", 1], ["CoalOreGravel", 1.5], ["CoalOreImpureGravel", 1.5], ["CoalOre", 2]]:
	recipes_oven.append({
		"Name": item+"ToCoke",
		"Input": one_item(item, 10),
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
	"Input": one_item("Log", 10),
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
	"Name": "BuildingMaterial2",
	"Input": items([
		["GravelSurface"],
		["SandSurface"],
		["Water", 500]
	]),
	"Output": one_item("BuildingMaterial", 10),
	"Ticks" : 60,
	"Tier": 2,
})

recipes_mixer.append({
	"Name": "BuildingMaterial3",
	"Input": items([
		["GravelSurface"],
		["SandSurface"],
		["Water", 500],
		["SteelParts", 2]
	]),
	"Output": one_item("BuildingMaterial", 20),
	"Ticks" : 60,
	"Tier": 3,
})

recipes_mixer.append({
	"Name": "BuildingMaterial4",
	"Input": items([
		["GravelSurface"],
		["SandSurface"],
		["Water", 500],
		["TitaniumParts", 2]
	]),
	"Output": one_item("BuildingMaterial", 40),
	"Ticks" : 60,
	"Tier": 4,
})

recipes_mixer.append({
	"Name": "BuildingMaterial5",
	"Input": items([
		["GravelSurface"],
		["SandSurface"],
		["Water", 500],
		["CompositeParts", 2]
	]),
	"Output": one_item("BuildingMaterial", 80),
	"Ticks" : 60,
	"Tier": 5,
})

recipes_mixer.append({
	"Name": "BuildingMaterial6",
	"Input": items([
		["GravelSurface"],
		["SandSurface"],
		["Water", 500],
		["NeutroniumParts", 2]
	]),
	"Output": one_item("BuildingMaterial", 160),
	"Ticks" : 60,
	"Tier": 6,
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
	"Tier": 5,
})	

recipes_sep.append({
	"Name":"Sand",
	"Input": one_item("SandSurface"),
	"Output": one_item("SiliconOxide"),
	"Ticks" : 100
})

pumpjack.append({
	"Name": "RawOil",
	"Input": no_items(),
	"Output": one_item("RawOil", 200),
	"Ticks" : 20
})	

recipes_arc_furnace.append({
	"Name": "SandSurfaceSmelting",
	"Input": one_item("SandSurface", 10),
	"Output": one_item("Glass", 10),
	"Ticks" : 100
})	

for material in materials:
	if "Items" in material and "Plate" in material["Items"]:
		if "Smelting" in material and "ArcFurnace" in material["Smelting"]:
			mul = 10 if (material["Name"] == "Iron" or material["Name"] == "Gold" or material["Name"] == "Copper") else 1
			recipes_arc_furnace.append({
				"Name": material["Name"] + "Plate",
				"Input": one_item(material["Name"] + "Dust", mul),
				"Output": one_item(material["Name"] + "Plate", mul),
				"Tier": extract_tier(material),
				"Ticks" : 100
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

recipes_electrolyzer.append({
	"Name": "MalachiteCrystal",
	"Input": one_item("MalachiteCrystal"),
	"Output": items([
		["MalachiteDust", 3],
		["BerylliumDust"]
	]),
	"Tier": 3,
	"Ticks" : 80,
})

recipes_electrolyzer.append({
	"Name": "ThorianiteCrystal",
	"Input": one_item("ThorianiteCrystal"),
	"Output": items([
		["UraniumDust", 3],
		["Uranium235Dust"]
	]),
	"Tier": 3,
	"Ticks" : 80,
})

for material in {"Ruby"}:
	recipes_macerator.append({
		"Name": material+"Crystal",
		"Input": one_item(material+"Crystal"),
		"Output": one_item(material+"Dust", 4),
		"Tier": 3,
		"Ticks" : 80,
	})
recipes_macerator.append({
	"Name": "Coal",
	"Input": one_item("Coal"),
	"Output": one_item("CoalDust"),
	"Ticks" : 100,
	"Tier": 0
})
			
recipes_macerator.append({
	"Name": "GravelToSand",
	"Input": one_item("GravelSurface"),
	"Output": one_item("SandSurface"),
	"Ticks" : 100
})

recipes_hammer.append({
	"Name": "StoneToGravel",
	"Input": one_item("StoneSurface"),
	"Output": one_item("GravelSurface"),
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
	"Name":"Steel",
	"Input": items([
		["IronDust", 10],
		["CoalDust", 5],
		["Oxygen", 1000]
	]),
	"Output": items([
		["SteelPlate", 10]
	]),
	"Ticks" : 200,
})

recipes_indu.append({
	"Name":"RawHotMercury",
	"Input": items([
			["CinnabarDust", 10]
		]),
	"Output": items([
			["HotMercury", 1000]
		]),
	"Ticks" : 200,
})

recipes_indu.append({
	"Name":"SiliconMonocrystal",
	"Input": items([
			["Silicon", 16],
			["Mercury", 1000]
		]),
	"Output": items([
			["SiliconMonocrystal"],
			["HotMercury", 1000]
		]),
	"Ticks" : 2000,
})

recipes_indu.append({
	"Name":"DopedSiliconMonocrystal",
	"Input": items([
			["Silicon", 16],
			["PlatinumDust", 1],
			["Mercury", 1000]
		]),
	"Output": items([
			["DopedSiliconMonocrystal"],
			["HotMercury", 1000]
		]),
	"Ticks" : 3000,
})

recipes_indu.append({
	"Name":"TantalumSludge",
	"Input": items([
			["TantalumSludge", 2],
			["AluminiumDust"],
			["Mercury", 1000]
		]),
	"Output": items([
			["TantalumPlate"],
			["HotMercury", 1000]
		]),
	"Ticks" : 200,
	"Tier": 5
})

recipes_indu.append({
	"Name":"SpongeToPlate",
	"Input": items([
			["TitaniumSponge"],
			["Mercury", 1000]
		]),
	"Output": items([
			["TitaniumPlate"],
			["HotMercury", 1000]
		]),
	"Tier": 5,
	"Ticks" : 200 * 2,
})

for material in materials:
	if "Smelting" in material and "InductionFurnace" in material["Smelting"]:
		m_name = material["Name"]
		recipes_indu.append({
			"Name": m_name+"Dust",
			"Input": items([
				[m_name + "Dust"],
				["Mercury", 300]
			]),
			"Output": items([
				[m_name + "Plate"],
				["HotMercury", 300]
			]),
			"Tier": 5,
			"Ticks" : 200,
		})

recipes_sep.append({
	"Name":"SiliconOxide",
	"Input": one_item("SandSurface", 2),
	"Output": one_item("SiliconOxide"),
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
	"Output": one_item("Biomass", 500),
	"Ticks": 200,
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
	"Tier":2,
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
	"Tier":2,
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
	"Tier":2,
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
	"Tier":2,
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
	"Tier":2,
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
	"Tier":2,
})

recipes_electrolyzer.append({
	"Name":"AluminiumOxideDust",
	"Input": one_item("AluminiumOxideDust"),
	"Output": one_item("AluminiumDust"),
	"Ticks" : 200,
	"Tier":2,
})

recipes_electrolyzer.append({
	"Name":"SandElectrolyze",
	"Input": one_item("SiliconOxide"),
	"Output": one_item("Silicon"),
	"Ticks" : 200,
	"Tier":2,
})

recipes_electrolyzer.append({
	"Name":"SaltElectrolyze",
	"Input": one_item("Salt"),
	"Output": one_item("Chlorine", 1000),
	"Ticks" : 200,
	"Tier":2,
})

# burning

recipes_hand.append({
	"Name": "Dirt",
	"Input": items([
		["SandSurface"],
		["Organics"]
	]),
	"Output": one_item("DirtSurface"),
	"Ticks" : 200
})

recipes_ferm.append({
	"Name": "Rapseed",
	"Input": one_item("Rapeseed"),
	"Output": one_item("RapeseedOil", 750),  # Increased from 500 to 750 to make it more competitive
	"Ticks" : 200
})

recipes_ferm.append({
	"Name": "MethaneFromBiomass",
	"Input": one_item("Biomass", 500),
	"Output":{
		"Items":[
			{
				"Name": "Methane",
				"Count": 750  # Increased from 500 to 750 to make it more competitive
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
	"Name": "MethaneFromPumpkin",
	"Input": one_item("Pumpkin"),
	"Output": one_item("Methane", 300),  # Increased from 200 to 300 to make it more competitive
	"Ticks" : 200
})

recipes_radiator.append({
	"Name": "Working",
	"Input": no_items(),
	"Output": no_items(),
	"Ticks" : 200,
})

recipes_solar.append({
	"Name": "Working",
	"Input": no_items(),
	"Output": no_items(),
	"Ticks" : 60,
})

recipes_industrial_chemreactor.append({
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
	"Output": one_item("Mercury", 1000),
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
	"Output": one_item("TitaniumTetrachloride", 1000),
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
	"Output": one_item("TitaniumSponge"),
	"Ticks" : 200
})

oil_crack.append({
	"Name": "RawOil",
	"Input": one_item("RawOil", 15000),
	"Output":{
		"Items": oil_crack_recipe(-1, 15000)
	},
	
	"Ticks" : 600,
	"Tier": 4
})

recipes_industrial_chemreactor.append({
	"Name": "ProducerGas",
	"Input": one_item("Coal"),
	"Output": items([
		["Ash"],
		["ProducerGas", 200]
	]),
	"Ticks" : 400,
	"Tier": 3,
})

recipes_pyro.append({
	"Name": "Coal",
	"Input": one_item("Coal"),
	"Output":{
		"Items":[
			{
				"Name": "Coke",
				"Count": 1
			},
			{
				"Name": "RawOil",
				"Count": 150  # Increased from 100 to 150 to make it more rewarding
			},
			{
				"Name": "ProducerGas",
				"Count": 150  # Increased from 100 to 150 to make it more rewarding
			},
			
		]
	},
	"Ticks" : 400,
	"Tier": 3,
})

recipes_pyro.append({
	"Name": "HeavyOilPyrolysis",
	"Input": one_item("HeavyOil", 1000),
	"Output":{
		"Items":[
			{
				"Name": "ProducerGas",
				"Count": 1300  # Balanced to provide same total burn time as input HeavyOil
			},
			{
				"Name": "Ash",
				"Count": 2  # Small amount of ash as byproduct
			}
		]
	},
	"Ticks" : 200,  # Relatively quick process
	"Tier": 3,  # Same tier as other pyrolysis recipes
})

for i in range(0, len(oil_crack_array(0))):
	recipes_pyro.append({
		"Name": "RawOil"+str(i),
		"Input": one_item("RawOil", 2000),
		"Output": { "Items":[ oil_crack_recipe(i, 2000) ] },
		"Ticks" : 120,  # Reduced from 150 to 120 to make it more efficient
		"Tier": 3,
	})

recipes_pyro.append({
	"Name": "Methane2",
	"Input": one_item("Methane", 800*5),
	"Output": one_item("ProducerGas", 500*5),
	"Ticks" : 200,
	"Tier": 3,
})
recipes_pyro.append({
	"Name": "FbToAmmonia",
	"Input": one_item("FermentedBiomass", 1000),
	"Output": items([
		["Ammonia", 500],
		["Ash"]
	]),
	"Tier": 3,
	"Ticks" : 200,
	"Tier": 3,
})
recipes_pyro.append({
	"Name": "FbToEthanol",
	"Input": one_item("FermentedBiomass", 1000),
	"Output": items([
		["Ethanol", 200],
		["Ash", 2]
	]),
	"Tier": 4,
	"Ticks" : 200,
	"Tier": 3,
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
	"Colors": [[0.0,0.2,0.0,0.9],[0.0,0.0,0.0,0.2]],
	"Tier": 4,
})

recipes_industrial_chemreactor.append({
	"Name": "SulfuricAcid",
	"Input": {
		"Items":[
			{
				"Name": "Sulfur",
				"Count": 1
			},
			{
				"Name": "Water",
				"Count": 1000
			},
			{
				"Name": "Catalyst",
				"Count": 1,
				"Probability": 0
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
	"Colors": [[0.0,0.0,0.3,0.2],[0.8,0.8,0.1,0.3]],
	"Tier": 4,
})

recipes_industrial_chemreactor.append({
	"Name": "RapeseedOil",
	"Input": items([
		["RapeseedOil", 1000],
		["Ethanol", 150],
		["Catalyst", 1, 0]
	]),
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

recipes_industrial_chemreactor.append({
	"Name": "Hydrogen",
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

recipes_industrial_chemreactor.append({
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
	"Input": items([
		["Nitrogen", 250],
		["Hydrogen", 750]
	]),
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
	"Input": items([
		["CoalDust"],
		["Oxygen", 500]
	]),
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
	"Input": items([
		["Ammonia", 500],
		["Chlorine", 500]
	]),
	"Output": one_item("AmmoniumChloride"),
	"Ticks" : 100,
	"Tier": 5,
})

recipes_industrial_chemreactor.append({
	"Name": "Methanol",
	"Input": items([
		["CarbonMonoxide", 250],
		["Hydrogen", 750]
	]),
	"Output": one_item("Ethanol", 1000),
	"Ticks" : 100
})

recipes_industrial_chemreactor.append({
	"Name": "NitricAcid",
	"Input": items([
		["Oxygen", 250],
		["Ammonia", 750]
	]),
	"Output": one_item("NitricAcid", 1000),
	"Ticks" : 150,
	"Colors": [[0.5,0.2,0.5,0.3],[0.0,0.5,0.25,0.3]]
})

recipes_industrial_chemreactor.append({
	"Name": "PlatinumSolution",
	"Input": items([
		["PyroplatiteDust", 10],
		["NitricAcid", 1000]
	]),
	"Output": one_item("PlatinumSolution", 1),
	"Ticks" : 800,
	"Colors": [[0.0,0.5,0.25,0.3],[0.9,0.5,0.25,0.3]],
	"Tier": 5,
})

recipes_industrial_chemreactor.append({
	"Name": "Platinum",
	"Input": items([
		["PlatinumSolution", 1300],
		["AmmoniumChloride"]
	]),
	"Output": items([
		["PlatinumDust"]
	]),
	"Ticks" : 400,
	"Tier": 5,
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
	"Tier":4,
	"Ticks" : 200,
	"Colors": [[0.8,0.8,0.1,0.3],[0.7,0.2,0.7,0.8]]
})

recipes_industrial_chemreactor.append({
	"Name": "CarbonPrecursor",
	"Input": items([
		["HeavyOil", 1000],
		["SulfuricAcid", 100]
	]),
	"Output": one_item("CarbonPrecursor", 1000),
	"Ticks" : 200
})

recipes_pyro.append({
	"Name": "CarbonFiber",
	"Input": one_item("CarbonPrecursor", 500),
	"Output": one_item("CarbonFiber"),
	"Ticks" : 200,
	"Tier": 5,
})

append_recipe_hand({
	"Name": "CarbonFiberSheet",
	"Input": one_item("CarbonFiber", 2),
	"Output": one_item("CarbonFiberSheet"),
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

append_recipe_hand({
	"Name": "BuildingMaterial",
	"Input": one_item("StoneSurface"),
	"Output": one_item("BuildingMaterial"),
	"Ticks" : 10
})

objects_array.append({ "Class": r_dict,
	"Name": "BlastFurnace" + r_dict,
	"Recipes": recipes_blast_furnace,
})

objects_array.append({ "Class": r_dict,
	"Name": "Oven" + r_dict,
	"Recipes": recipes_oven
})

objects_array.append({ "Class": r_dict,
	"Name": "Smelter" + r_dict,
	"Recipes": recipes_smelter
})

FixMinTier(recipes_macerator, 1)
objects_array.append({ "Class": r_dict,
	"Name": "Macerator" + r_dict,
	"Recipes": recipes_macerator,
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
	"Recipes": recipes_sep,
})

objects_array.append({ "Class": r_dict,
	"Name": "ArcSmelter" + r_dict,
	"Recipes": recipes_arc_furnace,
})

objects_array.append({ "Class": r_dict,
	"Name": "Electrolyzer" + r_dict,
	"Recipes": recipes_electrolyzer,
})

objects_array.append({ "Class": r_dict,
	"Name": "CuttingMachine" + r_dict,
	"Recipes": recipes_cutter
})


objects_array.append({ "Class": r_dict,
	"Name": "ElectricFurnace" + r_dict,
	"Recipes": recipes_elfurn
})

objects_array.append({ "Class": r_dict,
	"Name": "Fermenter" + r_dict,
	"Recipes": recipes_ferm,
})

objects_array.append({ "Class": r_dict,
	"Name": "MultitoolRobotArm" + r_dict,
	"Recipes": recipes_toolarm
})

FixMinTier(recipes_hammer, 1)
objects_array.append({ "Class": r_dict,
	"Name": "AutomaticHammer" + r_dict,
	"Recipes": recipes_hammer,
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
	"Recipes": recipes_chem,
})

objects_array.append({ "Class": r_dict,
	"Name": "InductionCoil" + r_dict,
	"Recipes": recipes_coil
})

objects_array.append({ "Class": r_dict,
	"Name": "IndustrialSmelter" + r_dict,
	"Recipes": recipes_indu,
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
	"Recipes": recipes_assembler,
})

objects_array.append({ "Class": r_dict,
	"Name": "IndustrialChemReactor" + r_dict,
	"Recipes": recipes_industrial_chemreactor,
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
	"Name": "FractionatingColumn" + r_dict,
	"Recipes": oil_crack
})

objects_array.append({ "Class": r_dict,
	"Name": "Pumpjack" + r_dict,
	"Recipes": pumpjack
})

objects_array.append({ "Class": r_dict,
	"Name": "Hand" + r_dict,
	"Recipes": recipes_hand,
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/misc.json", data)