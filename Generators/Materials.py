from Common import *

material_array_metal1 = [
	"/Game/Materials/Stone",
	"/Game/Materials/Copper",
	"/Game/Materials/Steel",
	"/Game/Materials/Aluminium",
	"/Game/Materials/StainlessSteel",
	"/Game/Materials/Titanium",
	"/Game/Materials/Composite",
	"/Game/Materials/Neutronium"
]

tier_material = [
	"Stone",
	"Copper",
	"Steel",
	"Aluminium",
	"StainlessSteel",
	"Titanium",
	"Composite",
	"Neutronium",
	"Neutronium"
]

def extract_tier(something):
	if isinstance(something, int):
		return something
	
	if isinstance(something, dict):	
		if "Tier" in something:
			return something["Tier"]
			
	if isinstance(something, str):
		for i in range(0,7):
			if something.find(tier_material[i]) != -1:
				return i
			
	raise Exception(f"{something} is not a dict with Tier or not a tier string")

def named_material(name):
	list = [x for x in materials if x["Name"] == name]
	if len(list) > 0:
		return list[0]
	
	raise Exception(f"{name} is not a material")
	
# https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D1%82%D1%80%D0%B8%D0%B4_%D0%B1%D0%BE%D1%80%D0%B0 BoronNitride
# https://en.wikipedia.org/wiki/Neutronium

# https://ru.wikipedia.org/wiki/%D0%A3%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%82%D0%B5%D0%BF%D0%BB%D0%BE%D1%82%D0%B0_%D1%81%D0%B3%D0%BE%D1%80%D0%B0%D0%BD%D0%B8%D1%8F burning

tiered_parts_list_no_dust = ["Plate", "Block", "Parts", "SolarCell"]
tiered_parts_list = tiered_parts_list_no_dust + ["Dust"]

materials = [
	{
		"Name": "Hand",
		"Label": "Hand",
		"Items": ["Exact"],
	},{
		"Name": "NoMaterial",
		"Label": "NoMaterial",
	},{
		"Name":"Computations",
		"Label":"Computations",
		"Items": ["Abstract"],
		"Description" : [["calculations", "common"]],
	},{
		"Name": "Heat",
		"Label": "Heat",
		"Items": ["Abstract"],
		"Unit": "J",
		"UnitS": "W",
		"UnitMul" : 1,
	},{
		"Name": "Electricity",
		"Label": "Electricity",
		"Items": ["Abstract"],
		"Unit": "J",
		"UnitS": "W",
		"UnitMul" : 1,
	},{
		"Name": "Kinetic",
		"Label": "Kinetic",
		"Items": ["Abstract"],
		"Unit": "J",
		"UnitS": "W",
		"UnitMul" : 1,
	},{
		"Name": "BasicCoil",
		"Label": "Basic Coil",
		"Items": ["Exact"],
		"Category": "Parts",
		"Tier": 2,
	},{
		"Name": "AdvancedCoil",
		"Label": "Advanced Coil",
		"Items": ["Exact"],
		"Category": "Parts",
		"Tier": 3,
	},{
		"Name": "PowerCoil",
		"Label": "Power Coil",
		"Items": ["Exact"],
		"Category": "Parts",
		"Tier": 4,
	},{
		"Name": "BasicFrame",
		"Label": "Basic Frame",
		"Items": ["Exact"],
		"Tier": 2,
		"Mesh": "/Game/Models/FrameCrate",
		"Materials": ["", ""],
		"Category": "Parts",
	},{
		"Name": "ReinforcedFrame",
		"Label": "Reinforced Frame",
		"Items": ["Exact"],
		"Tier": 3,
		"Mesh": "/Game/Models/FrameCrate",
		"Materials": ["", "/Game/Materials/BlackSteel"],
		"Category": "Parts",
	},{
		"Name": "ModularFrame",
		"Label": "Modular Frame",
		"Items": ["Exact"],
		"Tier": 4,
		"Mesh": "/Game/Models/FrameCrate",
		"Materials": ["", "/Game/Materials/StainlessSteel"],
		"Category": "Parts",
	},{
		"Name": "Copper",
		"Label": "Copper",
		"Items": tiered_parts_list + ["Wire"],
		"Smelting": ["Smelter", "ArcFurnace"],
		"Tier": 0,
	},{
		"Name": "Gold",
		"Label": "Gold",
		"Items": ["Plate", "Dust", "Block", "Wire"],
		"Smelting": ["Smelter", "ArcFurnace"],
		"Tier": 2
	},{
		"Name": "Platinum",
		"Label": "Platinum",
		"Items": ["Plate", "Dust", "Block", "Wire", "Foil"],
		"Smelting": ["ArcFurnace"],
		"Tier": 5,
	},{
		"Name": "PlatinumReflector",
		"Label": "Platinum Reflector",
		"Items": ["Exact"],
		"Tier": 6,
	},{
		"Name": "PlatinumSolution",
		"Label": "Platinum Solution",
		"Items": ["Fluid"],
		"Tier": 5,
	},{
		"Name": "AmmoniumChloride",
		"Label": "Ammonium Chloride",
		"Items": ["Exact"],
		"Tier": 5,
	},{
		"Name": "Iron",
		"Label": "Iron",
		"Items": ["Plate", "Dust", "Block"],
		"Smelting": ["Smelter", "ArcFurnace"],
		"Tier": 2,
	},{
		"Name": "CircuitBoard",
		"Label": "Circuit Board",
		"Items": ["Exact"],
		"Mesh":"/Game/Models/BoardCrate",
		"Materials":["/Game/Materials/Plastic"],
		"Tier": 1,
		"Category": "Parts",
	},{
		"Name": "Triod",
		"Label": "Triod",
		"Items": ["Exact"],
		"Mesh":"/Game/Models/TriodeCrate",
		"Tier": 1,
		"Category": "Parts",
	},{
		"Name": "Resistor",
		"Label": "Resistor",
		"Items": ["Exact"],
		"Mesh":"/Game/Models/ResistorCrate",
		"Materials":[],
		"Tier": 1,
		"Category": "Parts",
	},{
		"Name": "Transistor",
		"Label": "Transistor",
		"Items": ["Exact"],
		"Mesh":"/Game/Models/TransistorCrate",
		"Tier": 1,
		"Category": "Parts",
	},{
		"Name": "Steel",
		"Label": "Steel",
		"Smelting": ["ArcFurnace"],
		"Items": tiered_parts_list,
		"Tier": 1,
	},{
		"Name": "Aluminium",
		"Label": "Aluminium",
		"Items": tiered_parts_list + ["Foil"],
		"Smelting": ["ArcFurnace"],
		"Tier": 2,
	},{
		"Name": "AluminiumOxide",
		"Label": "Aluminium Oxide",
		"Items": ["Dust", "Block"],
	},{
		"Name": "StainlessSteel",
		"Label": "Stainless Steel",
		"Smelting": ["ArcFurnace"],
		"Items": tiered_parts_list,
		"Tier": 3,
	},{
		"Name": "Titanium",
		"Label": "Titanium",
		"Smelting": ["InductionFurnace"],
		"Items": tiered_parts_list,
		"Tier": 4,
	},{
		"Name": "TitaniumTetrachloride",
		"Label": "Titanium Tetrachloride",
		"Items": ["Fluid"],
		"Tier": 4,
	},{
		"Name": "TitaniumSponge",
		"Label": "Titanium Sponge",
		"Smelting": [],
		"Items": ["Exact"],		
		"Mesh":"/Game/Models/SpongeCrate",
        "Materials":["", "/Game/Materials/TitaniumOreGravel"],
		"Tier": 4,
	},{
		"Name": "TitaniumOxide",
		"Label": "Titanium Oxide",
		"Items": ["Dust"],
		"Tier": 4,
	},{
		"Name": "PreparedTitaniumOxide",
		"Label": "Prepared Titanium Oxide",
		"Items": ["Dust"],
		"Tier": 4,
	},{
		"Name": "HotNeutroniumPlate",
		"Label": "Hot Neutronium Plate",
		"Smelting": [],
		"Items": ["Exact"],
		"Tier": 6,
        "Mesh":"/Game/Models/Ingot",
        "Materials":["", "/Game/Materials/VeryHotMetal"],
	},{
		"Name": "Stone",
		"Label": "Stone",
		"Tier": 0,
		"Items": ["Exact"],
	},{
		"Name": "BuildingMaterial",
		"Label": "Building Material",
		"Tier": 0,
		"Items": ["Exact"],
		"StackSize": 999,
		"Tier": 0,
	},{
		"Name": "Sulfur",
		"Label": "Sulfur",
		"Tier": 4,
		"Burnable": {
			"BurnTime": 600
		},
		"Items": ["Exact"],
		"Mesh": "/Game/Models/DustCrate",
		"Materials": ["", "/Game/Materials/Sulfur"],
		"Tier": 1,
	},{
		"Name": "Chromium",
		"Label": "Chromium",
		"Smelting": ["ArcFurnace"],
		"Items": ["Dust"],
		"Tier": 3
	},{
		"Name": "Plutonium",
		"Label": "Plutonium",
		"Items": ["Dust", "Block"],
	},{
		"Name": "Uranium",
		"Label": "Uranium-238",
		"Items": ["Dust"],
	},{
		"Name": "Uranium235",
		"Label": "Uranium-235",
		"Items": ["Dust"],
	},{
		"Name": "Uranium233",
		"Label": "Uranium-233",
		"Items": ["Dust"],
	},{
		"Name": "Uranium233Cell",
		"Label": "Uranium 233 Cell",
		"Tier": 5,
		"Items": ["Exact"],
		"StackSize": 32,
		"Description":[["NuclearFuel", "common"]],
	},{
		"Name": "UraniumCell",
		"Label": "Uranium Cell",
		"Tier": 5,
		"Items": ["Exact"],
		"StackSize": 32,
		"Description":[["NuclearFuel", "common"], ["Burnable", "common", uranium_rod_output() * 20]],
	},{
		"Name": "PlutoniumCell",
		"Label": "Plutonium Cell",
		"Tier": 5,
		"Items": ["Exact"],
		"StackSize": 32,
		"Description":[["NuclearFuel", "common"]],
	},{
		"Name": "DepletedUraniumCell",
		"Label": "Depleted Uranium Cell",
		"Tier": 5,
		"Items": ["Exact"],
		"StackSize": 32,
		"Description":[["NuclearFuel", "common"]],
	},{
		"Name": "Thorium",
		"Label": "Thorium",
		"Items": ["Dust", "Block"],
	},{
		"Name": "Steam",
		"Label": "Steam",
		"Items": ["Gas"],
		"Unit": "J",
		"UnitMul": 1,
		"Tier": 2,
	},{
		"Name": "Chlorine",
		"Label": "Chlorine",
		"Items": ["Gas"],
		"Tier": 4,
		"Tier": 2,
	},{
		"Name": "Peat",
		"Label": "Peat",
		"Items": ["Exact"],
		"Burnable": {
			"BurnTime": 600
		},
		"Tier": 0,
		"Mesh": "/Game/Models/Piece"
	},{
		"Name": "Coal",
		"Label": "Coal",
		"Items": ["Exact"],
		"Burnable": {
			"BurnTime": 800
		},
		"Tier": 0,
		"StackSize": 64,
		"Mesh": "/Game/Models/Piece",
		"Tier": 0,
	},{
		"Name": "Coke",
		"Label": "Coke",
		"Items": ["Exact"],
		"StackSize": 64,
		"Burnable": {
			"BurnTime": 1200
		},
		"Mesh": "/Game/Models/Piece",
		"Tier": 1,
	},{
		"Name": "Creosote",
		"Label": "Creosote",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 800
		},
		"Tier": 0,
		"Mesh": "/Game/Models/Piece",
		"Tier": 1,
	},{
		"Name": "ProducerGas",
		"Label": "Producer Gas",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 400
		},
		"Tier": 3,
	},{
		"Name": "CarbonMonoxide",
		"Label": "Carbon Monoxide",
		"Items": ["Gas"],		
		"Burnable": {
			"BurnTime": 200
		},
	},{
		"Name": "SulfuricAcid",
		"Label": "Sulfuric Acid",
		"Items": ["Fluid"],
		"Tier": 4
	},{
		"Name": "NitricAcid",
		"Label": "Nitric Acid",
		"Items": ["Fluid"],
		"Tier": 4,
	},{
		"Name": "Ash",
		"Label": "Ash",
		"Items": ["Exact"],
		"Tier": 0
	},{
		"Name": "Hydrogen",
		"Label": "Hydrogen",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 500
		},
		"Tier": 3,
	},{
		"Name": "Ethanol",
		"Label": "Ethanol",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 700
		},
		"Tier": 2,
	},{
		"Name": "Methane",
		"Label": "Methane",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 600
		},
		"Tier": 2,
	},{
		"Name": "Ethylene",
		"Label": "Ethylene",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 600
		},
		"Tier": 2,
	},{
		"Name": "Polyethylene",
		"Label": "Polyethylene",
		"Items": ["Sheet"],
		"Tier": 3,
		"Materials":["", "/Game/Materials/Polyethylene"],
	},
	#,{
	#	"Name": "Nickel",
	#	"Label": "Nickel",
	#	"SmeltLevel": 0,
	#	"IsMetal": True,
	#	"Items": ["Dust"],
	#	"IsLiquidMetal": True,
	#	"IsBlock": True,
	#	"Tier": 3
	#}
	{
		"Name": "Water",
		"Label": "Water",
		"Items": ["Fluid"],
		"Tier": 0
	},{
		"Name": "Glass",
		"Label": "Glass",
		"Items": ["Exact"],
		"Tier": 0,
	},{
		"Name": "Lense",
		"Label": "Lense",
		"Items": ["Exact"],
		"Tier": 0,
	},{
		"Name": "Organics",
		"Label": "Organics",
		"Items": ["Exact"],
		"Tier": 0,
		"Mesh": "/Game/Models/Piece",
		"Description":[["Organics","common"]],
		"Burnable": {
			"BurnTime": 60
		},
	},{
		"Name": "Biomass",
		"Label": "Biomass",
		"Items": ["Fluid"]
	},{
		"Name": "FermentedBiomass",
		"Label": "Fermented Biomass",
		"Items": ["Fluid"]
	},{
		"Name": "Ammonia",
		"Label": "Ammonia",
		"Items": ["Fluid"],
		"Tier": 3,
	},{
		"Name": "RareEarthSludge",
		"Label": "Rare Earth Sludge",
		"Items": ["Exact"],
		"Mesh":"/Game/Models/SpongeCrate",
        "Materials":["/Game/Materials/GreenPlastic", "/Game/Materials/RareEarthElement"],
	},{
		"Name": "Yttrium",
		"Label": "Yttrium",
		"Items": ["Dust", "Block", "Plate", "Wire"],
		"Smelting": ["InductionFurnace"],
		"Tier": 4,
	},{
		"Name": "Tantalum",
		"Label": "Tantalum",
		"Items": ["Dust", "Block", "Plate", "Wire", "Foil"],
		"Smelting": ["InductionFurnace"],
		"Tier": 5,
	},{
		"Name": "TantalumSludge",
		"Label": "Tantalum Sludge",
		"Items": ["Exact"],
		"Tier": 6,
		"Mesh":"/Game/Models/SpongeCrate",
        "Materials":["/Game/Materials/GreenPlastic", "/Game/Materials/Tantalum"],
	},{
		"Name": "TantalumSolution",
		"Label": "Tantalum Solution",
		"Items": ["Exact"],
		"Tier": 6,
	},{
		"Name": "Log",
		"Label": "Log",
		"Items": ["Exact"],
		"Tier": 0,
		"Burnable": {
			"BurnTime": 200
		},
		"Mesh":"/Game/Models/LogCrate",
	},{
		"Name": "SiliconOxide",
		"Label": "Silicon Oxide",
		"Items": ["Exact"],
		"Tier": 1,
		"Mesh": "/Game/Models/CrystalCrate",
		"Materials" : [
			"",
			"/Game/Materials/SiliconOxide"
		],
	},{
		"Name": "Silicon",
		"Label": "Silicon",
		"Items": ["Exact"],
		"Tier": 3,
		"Mesh": "/Game/Models/CrystalCrate",
		"Materials" : [
			"",
			"/Game/Materials/Silicon"
		],
	},{
		"Name": "SiliconMonocrystal",
		"Label": "Silicon Monocrystal",
		"Items": ["Exact"],
		"Tier": 3
	},{
		"Name": "DopedSiliconMonocrystal",
		"Label": "Doped Silicon Monocrystal",
		"Items": ["Exact"],
		"Tier": 4
	},{
		"Name": "SiliconWafer",
		"Label": "Silicon Wafer",
		"Items": ["Exact"],
		"Tier": 4,
		"Mesh": "/Game/Models/WaferCrate",
	},{
		"Name": "DopedSiliconWafer",
		"Label": "Doped Silicon Wafer",
		"Items": ["Exact"],
		"Tier": 5,
		"Mesh": "/Game/Models/WaferCrate",
		"Materials": ["", "/Game/Materials/GrayMirror"]
	},{
		"Name": "Capacitor",
		"Label": "Capacitor",
		"Items": ["Exact"],
		"Tier": 3,
		"Mesh":"/Game/Models/CapacitorCrate",
		"Category": "Parts",
	},{
		"Name": "Rapeseed",
		"Label": "Rapeseed",
		"Items": ["Exact"],
		"Tier": 0
	},{
		"Name": "RapeseedOil",
		"Label": "Rapeseed Oil",
		"Items": ["Fluid"],
		"Tier": 0,
		"Burnable": {
			"BurnTime": 300 * 10
		}
	},{
		"Name": "MineralWater",
		"Label": "Mineral Water",
		"Items": ["Fluid"],
		"Tier": 0
	},{
		"Name": "RawOil",
		"Label": "Raw Oil",
		"Items": ["Fluid"],
		"Tier": 0,
		"Burnable": {
			"BurnTime": 500 * 15
		},
		"Tier": 4
	},{
		"Name": "Gasoline",
		"Label": "Gasoline",
		"Items": ["Gas"],
		"Tier": 1,
		"Burnable": {
			"BurnTime": 800 * 30
		},
		"Tier": 4
	},{
		"Name": "Diesel",
		"Label": "Diesel",
		"Items": ["Fluid"],
		"Tier": 1,
		"Burnable": {
			"BurnTime": 1200 * 30
		},
		"Tier": 4,
	},{
		"Name": "HighCetaneDiesel",
		"Label": "High Cetane Diesel",
		"Items": ["Fluid"],
		"Tier": 1,
		"Burnable": {
			"BurnTime": 2000 * 30
		},
		"Tier": 5
	},{
		"Name": "Superfuel",
		"Label": "Superfuel",
		"Items": ["Fluid"],
		"Tier": 1,
		"Burnable": {
			"BurnTime": 2800 * 30
		},
		"Tier": 6
	},{
		"Name": "RocketFuel",
		"Label": "Rocket Fuel",
		"Items": ["Fluid"],
		"Tier": 1,
		"Burnable": {
			"BurnTime": 400 * 30
		},
		"Tier": 4
	},
	{
		"Name": "HeavyOil",
		"Label": "Heavy Oil",
		"Items": ["Gas"],
		"Tier": 2,
		"Burnable": {
			"BurnTime": 800 * 10
		}
	},
	{
		"Name": "Battery",
		"Label": "Battery Cell",
		"Items": ["Exact"],
		"Tier": 3
	},{
		"Name": "Pumpkin",
		"Label": "Pumpkin",
		"Items": ["Exact"],
		"Tier": 0
	},{
		"Name": "Oxygen",
		"Label": "Oxygen",
		"Items": ["Gas"],
		"Tier": 4
	},{
		"Name": "Nitrogen",
		"Label": "Nitrogen",
		"Items": ["Gas"],
		"Tier": 1
	},{
		"Name": "Beryllium",
		"Label": "Beryllium",
		"Items": ["Dust"],
		"Tier": 4
	},{
		"Name": "Helium",
		"Label": "Helium",
		"Items": ["Gas", "Plasma"],
		"Tier": 4
	},{
		"Name": "Salt",
		"Label": "Salt",
		"Items": ["Exact"],
		"Tier": 4
	},{
		"Name": "MicaFlakes",
		"Label": "Mica Flakes",
		"Items": ["Exact"],
		"Tier": 4
	},{
		"Name": "Signal",
		"Label": "Signal",
		"Items": ["Exact"],
	},{
		"Name": "Circuit",
		"Label": "Circuit",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Circuit": True,
		"Mesh": "/Game/Models/CircuitCrate",
		"Tier": 1,
	},{
		"Name": "AdvancedCircuit",
		"Label": "Advanced Circuit",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Circuit": True,
		"Mesh": "/Game/Models/Circuit2Crate",
		"Tier": 2,
	},{
		"Name": "Processor",
		"Label": "Processor",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Circuit": True,
		"Mesh": "/Game/Models/Circuit3Crate",
		"Tier": 3,
	},{
		"Name": "QuantumCircuit",
		"Label": "Quantum Circuit",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Circuit": True,
		"Mesh": "/Game/Models/QuantumCircuitCrate",
		"Tier": 4,
	},{
		"Name": "QuantumProcessor",
		"Label": "Quantum Processor",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Circuit": True,
		"Mesh": "/Game/Models/Circuit3Crate",
		"Tier": 5,
	},{
		"Name": "QuantumCore",
		"Label": "Quantum Core",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Mesh": "/Game/Models/QuantumCoreCrate",
		"Tier": 4,
	},{
		"Name": "DecisionResonator",
		"Label": "Decision Resonator",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Mesh": "/Game/Models/QuantumCoreCrate",
		"Materials": ["/Game/Materials/BlackSteel", "/Game/Materials/ArrowWhite"],
		"Tier": 5,
	},{
		"Name": "BrainMatrix",
		"Label": "Brain Matrix",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Mesh": "/Game/Models/QuantumCoreCrate",
		"Tier": 6,
	},{
		"Name": "QuantumBrain",
		"Label": "Quantum Brain",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Circuit": True,
		"Mesh": "/Game/Models/Circuit3Crate",
		"Tier": 6,
	},{
		"Name": "Cell",
		"Label": "Cell",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Tier": 3,
	},{
		"Name": "SynthesisCell",
		"Label": "Synthesis Cell",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Tier": 6,
	},{
		"Name": "Catalyst",
		"Label": "Catalyst Cell",
		"StackSize": 32,
		"Items": ["Exact"],
		"Tier": 3
	},{
		"Name": "UltimateCatalyst",
		"Label": "Ultimate Catalyst Cell",
		"StackSize": 32,
		"Items": ["Exact"],
		"Tier": 7
	},{
		"Name": "MothershipPing",
		"Label": "Mothership Ping",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "Canister",
		"Label": "Canister",
		"StackSize": 1,
		"Items": ["Exact"],
		"CustomData": True,
		"MaxCharge": single_canister_capacity
	},{
		"Name": "PrimitiveBattery",
		"Label": "Primitive Battery",
		"StackSize": 1,
		"Items": ["Exact"],
		"CustomData": True,
		"MaxCharge": single_battery_cell_charge / 4
	},{
		"Name": "BasicBattery",
		"Label": "Basic Battery",
		"StackSize": 1,
		"Items": ["Exact"],
		"CustomData": True,
		"MaxCharge": single_battery_cell_charge * battery_mul(0)
	},{
		"Name": "AdvancedBattery",
		"Label": "Advanced Battery",
		"StackSize": 1,
		"Items": ["Exact"],
		"CustomData": True,
		"MaxCharge": single_battery_cell_charge * battery_mul(1)
	},{
		"Name": "SuperiorBattery",
		"Label": "Superior Battery",
		"StackSize": 1,
		"Items": ["Exact"],
		"CustomData": True,
		"MaxCharge": single_battery_cell_charge * battery_mul(2)
	},{
		"Name": "UltimateBattery",
		"Label": "Ultimate Battery",
		"StackSize": 1,
		"Items": ["Exact"],
		"CustomData": True,
		"MaxCharge": single_battery_cell_charge * battery_mul(3)
	},{
		"Name": "ControlCell",
		"Label": "Control Cell",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "ReflectorCell",
		"Label": "Reflector Cell",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "ThoriumCell",
		"Label": "Thorium Cell",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "MixedOxideCell",
		"Label": "Mixed-Oxide Cell",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "Mercury",
		"Label": "Mercury",
		"Items": ["Fluid"]
	},{
		"Name": "HotMercury",
		"Label": "Hot Mercury",
		"Items": ["Fluid"]
	},{
		"Name": "CarbonPrecursor",
		"Label": "Carbon Precursor",
		"Items": ["Fluid"],
		"Tier": 5,
	},{
		"Name": "CarbonFiber",
		"Label": "Carbon Fiber",
		"StackSize": 32,
		"Tier": 5,
		"Items": ["Exact", "Sheet"],
		"Materials":["", "/Game/Materials/CarbonFiber"],
	},{
		"Name": "Graphene",
		"Label": "Graphene",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "Composite",
		"Label": "Composite",
		"Smelting": ["InductionFurnace"],
		"Items": tiered_parts_list_no_dust,
		"Tier": 5,
	},{
		"Name": "Neutronium",
		"Label": "Neutronium",
		"Smelting": ["InductionFurnace"],
		"Items": tiered_parts_list_no_dust,
		"Tier": 6,
	},{
		"Name": "Capacity",
		"Label": "Capacity",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "InputError",
		"Label": "Input Error",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "OutputError",
		"Label": "Output Error",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "Progress",
		"Label": "Progress",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "SwitchOn", 
		"Label": "Switch On",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "Drain",
		"Label": "Drain",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "HeatLoss",
		"Label": "Heat Loss",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "Storage",
		"Label": "Storage",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "Percent",
		"Label": "Percent",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "Anything",
		"Label": "Anything",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "Everything",
		"Label": "Everything",
		"Items": ["Exact"],
		"Category": "Signal"
	},{
		"Name": "Empty",
		"Label": "Empty",
		"Items": ["Exact"],
		"Category": "Signal"
	}
]

import string

for a in list(string.ascii_uppercase):
	materials.append({
		"Name": a,
		"Label": a,
		"Items": ["Exact"],
		"Category": "Signal",
	})

materials.append({
	"Name": "ErrorString",
	"Label": "Error String",
	"Items": ["Exact"],
	"Category": "Signal"
})