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

tiered_parts_list = ["Plate", "Dust", "Block", "Parts", "Gearbox", "SolarCell"]

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
		"Name": "LV",
		"Label": "LV",
		"Items": ["Abstract"],
		"Unit": "J",
		"UnitS": "W",
		"UnitMul" : 1,
	},{
		"Name": "MV",
		"Label": "MV",
		"Items": ["Abstract"],
		"Unit": "J",
		"UnitS": "W",
		"UnitMul" : 1,
	},{
		"Name": "HV",
		"Label": "HV",
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
		"Name": "Copper",
		"Label": "Copper",
		"Items": tiered_parts_list + ["Wire"],
		"Smelting": ["Smelter", "ArcFurnace"],
		"Tier": 1,
	},{
		"Name": "Gold",
		"Label": "Gold",
		"Items": ["Plate", "Dust", "Block", "Wire"],
		"Smelting": ["Smelter", "ArcFurnace"],
		"Tier": 2
	},{
		"Name": "Silver",
		"Label": "Silver",
		"Items": ["Dust", "Plate", "Block", "Wire"],
		"Smelting": ["Smelter", "ArcFurnace"],
		"Tier": 3,
	},{
		"Name": "Platinum",
		"Label": "Platinum",
		"Items": ["Plate", "Dust", "Block", "Wire"],
		"Smelting": ["ArcFurnace"],
		"Tier": 5,
	},{
		"Name": "Rhodium",
		"Label": "Rhodium",
		"Items": ["Dust", "Plate", "Block", "Foil"],
		"Smelting": ["ArcFurnace"],
		"Tier": 6,
	},{
		"Name": "RhodiumReflector",
		"Label": "Rhodium Reflector",
		"Items": ["Exact"],
		"Tier": 6,
	},{
		"Name": "PlatinumRhodiumSolution",
		"Label": "Platinum-Rhodium Solution",
		"Items": ["Exact"],
	},{
		"Name": "AmmoniumChloride",
		"Label": "Ammonium Chloride",
		"Items": ["Exact"],
	},{
		"Name": "RhodiumSolution",
		"Label": "Rhodium Solution",
		"Items": ["Fluid"]
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
	},{
		"Name": "Triod",
		"Label": "Triod",
		"Items": ["Exact"],
		"Mesh":"/Game/Models/TriodeCrate"
	},{
		"Name": "Resistor",
		"Label": "Resistor",
		"Items": ["Exact"],
		"Mesh":"/Game/Models/BoardCrate",
		"Materials":["/Game/Materials/Plastic"],
	},{
		"Name": "Transistor",
		"Label": "Transistor",
		"Items": ["Exact"],
		"Mesh":"/Game/Models/BoardCrate",
		"Materials":["/Game/Materials/Plastic"],
	},{
		"Name": "Plastic",
		"Label": "Plastic",
		"Items": ["Exact"],
		"Mesh": "/Game/Models/Ingot",
		"Materials": ["/Game/Materials/GreenPlastic"],
	},{
		"Name": "Steel",
		"Label": "Steel",
		"Smelting": ["ArcFurnace"],
		"Items": tiered_parts_list,
		"Tier": 2,
	},{
		"Name": "Aluminium",
		"Label": "Aluminium",
		"Items": tiered_parts_list + ["Foil"],
		"Smelting": ["ArcFurnace"],
		"Tier": 3,
	},{
		"Name": "AluminiumOxide",
		"Label": "Aluminium Oxide",
		"Items": ["Dust", "Block"],
	},{
		"Name": "StainlessSteel",
		"Label": "Stainless Steel",
		"Smelting": ["ArcFurnace"],
		"Items": tiered_parts_list,
		"Tier": 4,
	},{
		"Name": "Titanium",
		"Label": "Titanium",
		"Smelting": ["InductionFurnace"],
		"Items": tiered_parts_list,
		"Tier": 5,
	},{
		"Name": "TitaniumTetrachloride",
		"Label": "Titanium Tetrachloride",
		"Items": ["Fluid"]
	},{
		"Name": "TitaniumSponge",
		"Label": "Titanium Sponge",
		"Smelting": ["InductionFurnace"],
		"Items": ["Exact"],		
	},{
		"Name": "TitaniumOxide",
		"Label": "Titanium Oxide",
		"Items": ["Dust"],
	},{
		"Name": "PreparedTitaniumOxide",
		"Label": "Prepared Titanium Oxide",
		"Items": ["Dust"],
	},{
		"Name": "HotNeutroniumPlate",
		"Label": "Hot Neutronium Plate",
		"Smelting": ["InductionFurnace"],
		"Items": ["Exact"],
		"Tier": 5,
        "Mesh":"/Game/Models/Ingot",
        "Materials":["/Game/Materials/VeryHotMetal"],
	}
	#,{
	#	"Name": "Rubber",
	#	"Label": "Rubber",
	#	"SmeltLevel": 0,
	#	"IsMetal": True,
	#	"Items": ["Dust"],
	#	"Tier": 2
	#}
	,{
		"Name": "Cobalt",
		"Label": "Cobalt",
		"Smelting": ["InductionFurnace"],
		"Items": ["Dust", "Block"],
		"Tier": 5,
	},{
		"Name": "CobaltOxide",
		"Label": "Cobalt Oxide",
		"Items": ["Dust"],
		"Tier": 5
	},{
		"Name": "Stone",
		"Label": "Stone",
		"Tier": 0,
		"Items": ["Exact"],
	},{
		"Name": "Sulfur",
		"Label": "Sulfur",
		"Tier": 0,
		"Items": ["Exact"],
	},	
	#},{
	#	"Name": "Bronze",
	#	"Label": "Bronze",
	#	"SmeltLevel": 2,
	#	"IsMetal": True,
	#	"Items": ["Dust"],
	#	
	#	"IsBlock": True
	#},{
	#	"Name": "Brass",
	#	"Label": "Brass",
	#	"SmeltLevel": 2,
	#	"IsMetal": True,
	#	"Items": ["Dust"],
	#	
	#	"IsBlock": True
	#},{
	#	"Name": "BrassDetails",
	#	"Label": "Brass Parts",
	#	
	#	"Items": ["Exact"],
	#	"Category": "Component"
	#},{
	#	"Name": "BrassReductor",
	#	"Label": "Brass Reductor",
	#	
	#	"Items": ["Exact"],
	#	"Category": "Component"
	#},
	{
		"Name": "Cement",
		"Label": "Cement",
		"Items": ["Dust"],
	},{
		"Name": "Chromium",
		"Label": "Chromium",
		"Smelting": ["ArcFurnace"],
		"Items": ["Dust", "Plate"],
		"Tier": 3
	},{
		"Name": "Plutonium",
		"Label": "Plutonium",
		"Items": ["Dust", "Block", "Plate"],
	},{
		"Name": "Uranium",
		"Label": "Uranium-238",
		"Items": ["Dust", "Plate"],
	},{
		"Name": "Uranium235",
		"Label": "Uranium-235",
		"Items": ["Dust", "Plate"],
	},{
		"Name": "Uranium233",
		"Label": "Uranium-233",
		"Items": ["Dust", "Plate"],
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
		"Description":[["NuclearFuel", "common"]],
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
		"Items": ["Dust", "Plate", "Block"],
	},{
		"Name": "Steam",
		"Label": "Steam",
		"Items": ["Gas"],
		"Unit": "J",
		"UnitMul": 1,
		"Color":[1,1,1]
	},{
		"Name": "Chlorine",
		"Label": "Chlorine",
		"Items": ["Gas"],
		"Tier": 4,
		"Color": [1,1,0],
	},{
		"Name": "Peat",
		"Label": "Peat",
		"Items": ["Exact"],
		"Burnable": {
			"BurnTime": 400
		},
		"Tier": 0,
		"Color":[0.2,0.2,0.0],
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
		"Color":[0.0,0.0,0.0],
		"Mesh": "/Game/Models/Piece"
	},{
		"Name": "Coke",
		"Label": "Coke",
		"Items": ["Exact"],
		"StackSize": 64,
		"Burnable": {
			"BurnTime": 1200
		},
		"Color":[0.0,0.0,0.0],
		"Mesh": "/Game/Models/Piece"
	},{
		"Name": "Creosote",
		"Label": "Creosote",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 2000
		},
		"Tier": 0,
		"Color":[0.0,0.0,0.0],
		"Mesh": "/Game/Models/Piece"
	},{
		"Name": "ProducerGas",
		"Label": "Producer Gas",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 400
		},
		"Color": [1,1,1],
		"MoreEfficientIn":"GasTurbine"
	},{
		"Name": "CarbonMonoxide",
		"Label": "Carbon Monoxide",
		"Items": ["Gas"],		
		"Burnable": {
			"BurnTime": 200
		},
		"Color": [0.5,0.5,0.5],
		"MoreEfficientIn":"GasTurbine"
	},{
		"Name": "SulfuricAcid",
		"Label": "Sulfuric Acid",
		"Items": ["Fluid"],
		"Tier": 3
	},{
		"Name": "NitricAcid",
		"Label": "Nitric Acid",
		"Items": ["Fluid"],
		"Color": [1.0,0.5,0.0],
	},{
		"Name": "HydrochloricAcid",
		"Label": "Hydrochloric Acid",
		"Items": ["Fluid"],
		"Color": [1.0,0.5,0.0],
	},{
		"Name": "HydrofluoricAcid",
		"Label": "Hydrofluoric Acid",
		"Items": ["Fluid"],
		"Color": [1.0,0.5,0.0],
	},{
		"Name": "AquaRegia",
		"Label": "Aqua Regia",
		"Items": ["Fluid"],
		"Color": [1.0,0.5,0.0],
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
			"BurnTime": 400
		},
		"Tier": 2,
		"Color": [.2,.2,.5],
	},{
		"Name": "Ethanol",
		"Label": "Ethanol",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 500
		},
		"Tier": 2,
		"Color":[0.5,0.2,0.2]
	},{
		"Name": "Methane",
		"Label": "Methane",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 400
		},
		"Tier": 2,
		"Color":[0.5,0.2,0.2]
	},{
		"Name": "Ethylene",
		"Label": "Ethylene",
		"Items": ["Gas"],
		"Burnable": {
			"BurnTime": 400
		},
		"Tier": 2,
		"Color": [.2,.5,.2],
	},{
		"Name": "Acetone",
		"Label": "Acetone",
		"Items": ["Fluid"],
		"Burnable": {
			"BurnTime": 100
		},
		"Tier": 3,
		"Color": [.2,.5,.2],
	},{
		"Name": "MethylIsobutylKetone",
		"Label": "Methyl Isobutyl Ketone",
		"Items": ["Fluid"],
		"Burnable": {
			"BurnTime": 300
		},
		"Tier": 6,
	},{
		"Name": "MesitylOxide",
		"Label": "Mesityl Oxide",
		"Items": ["Fluid"],
		"Burnable": {
			"BurnTime": 200
		},
		"Tier": 4,
		"Color": [.2,.5,.2],
	},{
		"Name": "Polyethylene",
		"Label": "Polyethylene",
		"Items": ["Sheet"],
		"Tier": 3,
		"Color": [.2,.5,.2],
	},{
		"Name": "Fluorine",
		"Label": "Fluorine",
		"Items": ["Fluid"],
		"Tier": 2,
		"Color": [.2,.5,.2],
	},{
		"Name": "Tetrafluoroethylene",
		"Label": "Tetrafluoroethylene",
		"Items": ["Fluid"],
		"Tier": 2,
		"Color": [.2,.5,.2],
	},{
		"Name": "Polytetrafluoroethylene",
		"Label": "Polytetrafluoroethylene",
		"Items": ["Sheet"],
		"Tier": 2,
		"Color": [.2,.5,.2],
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
			"BurnTime": 40
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
		"Items": ["Fluid"]
	},{
		"Name": "Clay",
		"Label": "Clay",
		"Tier": 0,
		"Items": ["Exact"],
		"Mesh": "/Game/Models/Piece"
	},{
		"Name": "RareEarthSludge",
		"Label": "Rare Earth Sludge",
		"Items": ["Exact"],
	},{
		"Name": "Yttrium",
		"Label": "Yttrium",
		"Items": ["Dust", "Block", "Plate", "Wire"],
		"Smelting": ["InductionFurnace"],
		"Tier": 4,
	},{
		"Name": "Neodymium",
		"Label": "Neodymium",
		"Items": ["Dust", "Block", "Plate"],
		"Smelting": ["ArcFurnace"],
		"Tier": 4,
	},{
		"Name": "Niobium",
		"Label": "Niobium",
		"Items": ["Dust", "Block", "Plate", "Wire"],
		"Smelting": ["ArcFurnace"],
		"Tier": 4,
	},{
		"Name": "MicaFlakes",
		"Label": "Mica Flakes",
		"Items": ["Exact"],
		"Tier": 3,
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
			"BurnTime": 400
		},
		"Color":[0.9,0.9,0.9]
	},{
		"Name": "Silicon",
		"Label": "Silicon",
		"Items": ["Exact"],
		"Tier": 3
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
		"Tier": 4
	},{
		"Name": "DopedSiliconWafer",
		"Label": "Doped Silicon Wafer",
		"Items": ["Exact"],
		"Tier": 5
	},{
		"Name": "Capacitor",
		"Label": "Capacitor",
		"Items": ["Exact"],
		"Tier": 3
	},{
		"Name": "Rapeseed",
		"Label": "Rapeseed",
		"Items": ["Exact"],
		"Tier": 0,
		"Color":[0.1,0.1,0.1]
	},{
		"Name": "RapeseedOil",
		"Label": "Rapeseed Oil",
		"Items": ["Fluid"],
		"Tier": 0,
		"Burnable": {
			"BurnTime": 800
		},
		"Color":[0.1,0.1,0.1]
	},
	{
		"Name": "RawOil",
		"Label": "Raw Oil",
		"Items": ["Fluid"],
		"Tier": 0,
		"Burnable": {
			"BurnTime": 400
		},
		"Color":[0.01,0.01,0.01]
	},
	{
		"Name": "MineralWater",
		"Label": "Mineral Water",
		"Items": ["Fluid"],
		"Tier": 0
	},
	{
		"Name": "Gasoline",
		"Label": "Gasoline",
		"Items": ["Gas"],
		"Tier": 1,
		"Burnable": {
			"BurnTime": 400
		},
		"Color":[.5,.5,0.2]
	},{
		"Name": "Diesel",
		"Label": "Diesel",
		"Items": ["Fluid"],
		"Tier": 1,
		"Burnable": {
			"BurnTime": 800
		},
		"Color":[.2,.2,0.2]
	},{
		"Name": "HighCetaneDiesel",
		"Label": "High Cetane Diesel",
		"Items": ["Fluid"],
		"Tier": 1,
		"Color":[.1,.1,0.1],
		"Burnable": {
			"BurnTime": 1600
		}
	},{
		"Name": "Superfuel",
		"Label": "Superfuel",
		"Items": ["Fluid"],
		"Tier": 1,
		"Color":[1,1,0.5],
		"Burnable": {
			"BurnTime": 2000
		}
	},{
		"Name": "RocketFuel",
		"Label": "Rocket Fuel",
		"Items": ["Fluid"],
		"Tier": 1,
		"Color":[0,1,0],
		"Burnable": {
			"BurnTime": 300
		}
	},{
		"Name": "ExtraHeavyOil",
		"Label": "Extra Heavy Oil",
		"Items": ["Gas"],
		"Tier": 2,
		"Burnable": {
			"BurnTime": 800
		},
		"Color":[0.01,.01,0.01]
	},
	{
		"Name": "HeavyOil",
		"Label": "Heavy Oil",
		"Items": ["Gas"],
		"Tier": 2,
		"Burnable": {
			"BurnTime": 400
		},
		"Color":[0.2,.5,0.2]
	},
	{
		"Name": "Battery",
		"Label": "Battery Cell",
		"Items": ["Exact"],
		"Tier": 3
	},
	{
		"Name": "SiliconOxide",
		"Label": "Silicon Oxide",
		"Items": ["Exact"],
		"Tier": 1
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
		"Tier": 4
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
		"Name": "PortalBase",
		"Label": "Portal Base",
		"Items": ["Exact"],
		"Tier": 2
	},{
		"Name": "Signal",
		"Label": "Signal",
		"Items": ["Exact"],
	},{
		"Name": "CopperWire",
		"Label": "Copper Wire",
		"StackSize": 64,
		"Items": ["Exact"],
		"Category": "Parts",
		"Mesh":"/Game/Models/WireCrate",
		"Materials":["/Game/CopperWiresOnCrate"],
	},{
		"Name": "Circuit",
		"Label": "Circuit",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "/Game/Models/CircuitCrate"
	},{
		"Name": "AdvancedCircuit",
		"Label": "Advanced Circuit",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "/Game/Models/Circuit2Crate"
	},{
		"Name": "Processor",
		"Label": "Processor",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "/Game/Models/Circuit3Crate"
	},{
		"Name": "QuantumCircuit",
		"Label": "Quantum Circuit",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "/Game/Models/QuantumCircuitCrate"
	},{
		"Name": "QuantumProcessor",
		"Label": "Quantum Processor",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "/Game/Models/Circuit3Crate"
	},{
		"Name": "QuantumCore",
		"Label": "Quantum Core",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Mesh": "/Game/Models/QuantumCoreCrate"
	},{
		"Name": "DecisionResonator",
		"Label": "Decision Resonator",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Mesh": "/Game/Models/QuantumCoreCrate"
	},{
		"Name": "BrainMatrix",
		"Label": "Brain Matrix",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Mesh": "/Game/Models/QuantumCoreCrate"
	},{
		"Name": "QuantumBrain",
		"Label": "Quantum Brain",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "/Game/Models/Circuit3Crate"
	},{
		"Name": "Cell",
		"Label": "Cell",
		"StackSize": 32,
		"Items": ["Exact"],
		"Category": "Parts",
	},{
		"Name": "Catalyst",
		"Label": "Catalyst Cell",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "UltimateCatalyst",
		"Label": "Ultimate Catalyst Cell",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "MothershipPing",
		"Label": "Mothership Ping",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "PrimitiveBattery",
		"Label": "Primitive Battery",
		"StackSize": 1,
		"Items": ["Exact"],
		"MaxCharge": single_battery_cell_charge / 4
	},{
		"Name": "BasicBattery",
		"Label": "Basic Battery",
		"StackSize": 1,
		"Items": ["Exact"],
		"MaxCharge": single_battery_cell_charge * battery_mul(0)
	},{
		"Name": "AdvancedBattery",
		"Label": "Advanced Battery",
		"StackSize": 1,
		"Items": ["Exact"],
		"MaxCharge": single_battery_cell_charge * battery_mul(1)
	},{
		"Name": "SuperiorBattery",
		"Label": "Superior Battery",
		"StackSize": 1,
		"Items": ["Exact"],
		"MaxCharge": single_battery_cell_charge * battery_mul(2)
	},{
		"Name": "UltimateBattery",
		"Label": "Ultimate Battery",
		"StackSize": 1,
		"Items": ["Exact"],
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
		"Name": "FilteringCell",
		"Label": "Filtering Cell",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "CarbonPrecursor",
		"Label": "Carbon Precursor",
		"Items": ["Fluid"],
	},{
		"Name": "CarbonFiber",
		"Label": "Carbon Fiber",
		"StackSize": 32,
		"Items": ["Exact", "Sheet"],
	},{
		"Name": "Graphene",
		"Label": "Graphene",
		"StackSize": 32,
		"Items": ["Exact"],
	},{
		"Name": "Composite",
		"Label": "Composite",
		"Smelting": ["InductionFurnace"],
		"Items": tiered_parts_list,
		"Tier": 6,
	},{
		"Name": "Neutronium",
		"Label": "Neutronium",
		"Smelting": ["InductionFurnace"],
		"Items": tiered_parts_list,
		"Tier": 7,
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
		"Name": "IncreaseInventorySize",
		"Label": "IncreaseInventorySize",
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