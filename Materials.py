from Common import *

material_array_metal1 = [
	"Materials/Stone",
	"Materials/Copper",
	"Materials/Steel",
	"Materials/Aluminium",
	"Materials/StainlessSteel",
	"Materials/Titanium",
	"Materials/HardMetal",
	"Materials/Neutronium"
]

tier_material = [
	"Stone",
	"Copper",
	"Steel",
	"Aluminium",
	"StainlessSteel",
	"Titanium",
	"HardMetal",
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
			
	return 0

def named_material(name):
	list = [x for x in materials if x["Name"] == name]
	if len(list) > 0:
		return list[0]
	return materials[0]
	
# https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D1%82%D1%80%D0%B8%D0%B4_%D0%B1%D0%BE%D1%80%D0%B0 BoronNitride
# https://en.wikipedia.org/wiki/Neutronium

# https://ru.wikipedia.org/wiki/%D0%A3%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%82%D0%B5%D0%BF%D0%BB%D0%BE%D1%82%D0%B0_%D1%81%D0%B3%D0%BE%D1%80%D0%B0%D0%BD%D0%B8%D1%8F burning

materials = [
	{
		"Name" : "Hand",
		"Label" : "Hand",
		"Craftable": False,
		"IsExact": True,
	},{
		"Name" : "NoMaterial",
		"Label" : "NoMaterial",
		"Craftable": False,
	},{
		"Name":"Computations",
		"Label":"Computations",
		"IsAbstract": True,
		"Description" : [["calculations", "common"]],
	},{
		"Name" : "Heat",
		"Label" : "Heat",
		"IsAbstract": True,
		"Unit": "J",
		"UnitS": "W",
		"UnitMul" : 1,
	},{
		"Name" : "Electricity",
		"Label" : "Electricity",
		"IsAbstract": True,
		"Unit": "J",
		"UnitS": "W",
		"UnitMul" : 1,
	},{
		"Name" : "Kinetic",
		"Label" : "Kinetic",
		"IsAbstract": True,
		"Unit": "J",
		"UnitS": "W",
		"UnitMul" : 1,
	},{
		"Name" : "Copper",
		"Label" : "Copper",
		"IsIngot": True,
		"IsDust": True,
		"SmeltLevel": 0,
		"IsBlock": True,
	},{
		"Name" : "Gold",
		"Label" : "Gold",
		"IsDust": True,
		"IsIngot": True,
		"SmeltLevel": 0,
		"IsBlock": True,
	},{
		"Name" : "Superconductor",
		"Label" : "Superconductor",
		"IsDust": True,
		"IsIngot": True,
		"SmeltLevel": 4,
		"IsBlock": True,
	},{
		"Name" : "Iron",
		"Label" : "Iron",
		"IsDust": True,
		"IsIngot": True,
		"SmeltLevel": 0,
		"IsBlock": True,
	},{
		"Name" : "CircuitBoard",
		"Label" : "Circuit Board",
		"IsExact": True,
		"Mesh":"Models/BoardCrate",
		"Materials":["Materials/Plastic"],
	},{
		"Name" : "AdvancedCircuitBoard",
		"Label" : "Advanced Circuit Board",
		"IsExact": True,
		"Mesh":"Models/BoardCrate",
		"Materials":["Materials/DarkGreenPlastic"],
	},{
		"Name" : "Plastic",
		"Label" : "Plastic",
		"IsExact": True,
	},{
		"Name" : "Steel",
		"Label" : "Steel",
		"IsIngot": True,
		"IsDust": True,
		"SmeltLevel": 1,
		"IsBlock": True,
	},{
		"Name" : "Aluminium",
		"Label" : "Aluminium",
		"IsDust": True,
		"IsIngot": True,
		"SmeltLevel": 3,
		"IsBlock": True,
	},{
		"Name" : "AluminiumOxide",
		"Label" : "Aluminium Oxide",
		"IsDust": True,
		"SmeltLevel": 3,
		"IsBlock": True,
	},{
		"Name" : "StainlessSteel",
		"Label" : "Stainless Steel",
		"SmeltLevel": 3,
		"IsIngot": True,
		"IsDust": True,
		"IsBlock": True,
	},{
		"Name" : "Titanium",
		"Label" : "Titanium",
		"SmeltLevel": 4,
		"IsIngot": True,
		"IsDust": True,
		"IsBlock": True,
	},{
		"Name" : "TitaniumTetrachloride",
		"Label" : "Titanium Tetrachloride",
		"SmeltLevel": 4,
		"IsFluid": True,
	},{
		"Name" : "TitaniumSponge",
		"Label" : "Titanium Sponge",
		"SmeltLevel": 4,
		"IsExact": True,		
	},{
		"Name" : "TitaniumOxide",
		"Label" : "Titanium Oxide",
		"IsDust": True,
	},{
		"Name" : "PreparedTitaniumOxide",
		"Label" : "Prepared Titanium Oxide",
		"IsDust": True,
	},{
		"Name": "Zink",
		"Label": "Zink",
		"SmeltLevel": 0,
		"IsMetal": True,
		"IsDust": True,
		"IsBlock": True,
	},{
		"Name": "Lithium",
		"Label": "Lithium",
		"SmeltLevel": 0,
		"IsMetal": True,
		"IsDust": True,
		"Burnable": {
			"BurnTime": 18*20,
			"HeatPerTick": 18,
			"TotalAsh": 0.06
		},
		"IsBlock": True
	},{
		"Name": "Tungsten",
		"Label": "Tungsten",
		"SmeltLevel": 4,
		"IsDust": True,
		"Tier": 5,
	},{
		"Name": "TungstenOxide",
		"Label": "Tungsten Oxide",
		"SmeltLevel": 4,
		"IsDust": True,
		"Tier": 5,
	},{
		"Name": "TungstenCarbide",
		"Label": "Tungsten Carbide",
		"IsDust": True,
		"Tier": 5,
	},{
		"Name": "HardMetal",
		"Label": "Hard Metal",
		"SmeltLevel": 4,
		"IsIngot": True,
		"IsDust": True,
		"Tier": 5,
		"IsBlock": True,
	},{
		"Name": "HotHardMetalIngot",
		"Label": "Hot Hard Metal Ingot",
		"SmeltLevel": 4,
		"IsExact": True,
		"Tier": 5,
        "Mesh":"Models/Ingot",
        "Materials":["Materials/HotMetal"],
	},{
		"Name": "HotNeutroniumIngot",
		"Label": "Hot Neutronium Ingot",
		"SmeltLevel": 4,
		"IsExact": True,
		"Tier": 5,
        "Mesh":"Models/Ingot",
        "Materials":["Materials/VeryHotMetal"],
	}
	#,{
	#	"Name": "Rubber",
	#	"Label": "Rubber",
	#	"SmeltLevel": 0,
	#	"IsMetal": True,
	#	"IsDust": True,
	#	"Tier": 2
	#}
	,{
		"Name": "Cobalt",
		"Label": "Cobalt",
		"SmeltLevel": 4,
		"IsDust": True,
		"Tier": 5,
		"IsBlock": True,
	},{
		"Name": "CobaltOxide",
		"Label": "Cobalt Oxide",
		"IsDust": True,
		"Tier": 5
	},{
		"Name": "Stone",
		"Label": "Stone",
		"Tier": 0,
	},	
	#},{
	#	"Name": "Bronze",
	#	"Label": "Bronze",
	#	"SmeltLevel": 2,
	#	"IsMetal": True,
	#	"IsDust": True,
	#	
	#	"IsBlock": True
	#},{
	#	"Name": "Brass",
	#	"Label": "Brass",
	#	"SmeltLevel": 2,
	#	"IsMetal": True,
	#	"IsDust": True,
	#	
	#	"IsBlock": True
	#},{
	#	"Name": "BrassDetails",
	#	"Label": "Brass Parts",
	#	
	#	"IsExact": True,
	#	"Category": "Component"
	#},{
	#	"Name": "BrassReductor",
	#	"Label": "Brass Reductor",
	#	
	#	"IsExact": True,
	#	"Category": "Component"
	#},
	{
		"Name": "Cement",
		"Label": "Cement",
		"IsDust": True,
	},{
		"Name": "Neutronium",
		"Label": "Neutronium",
		"IsIngot": True,
		"IsDust": True,
		"Tier": 6
	},{
		"Name": "Chromium",
		"Label": "Chromium",
		"SmeltLevel": 0,
		"IsDust": True,
		"Tier": 3
	},{
		"Name": "Plutonium",
		"Label": "Plutonium",
		"IsBlock": True,
		"IsDust": True,
	},{
		"Name": "Uranium",
		"Label": "Uranium-238",
		"IsBlock": True,
		"IsDust": True,
	},{
		"Name": "Uranium235",
		"Label": "Uranium-235",
		"IsBlock": True,
		"IsDust": True,
	},{
		"Name": "Uranium233",
		"Label": "Uranium-233",
		"IsBlock": True,
		"IsDust": True,
	},{
		"Name": "Uranium233Cell",
		"Label": "Uranium 233 Cell",
		"Tier": 5,
		"IsExact": True,
		"Stack": 32,
		"Description":[["NuclearFuel", "common"]],
	},{
		"Name": "UraniumCell",
		"Label": "Uranium Cell",
		"Tier": 5,
		"IsExact": True,
		"Stack": 32,
		"Description":[["NuclearFuel", "common"]],
	},{
		"Name": "PlutoniumCell",
		"Label": "Plutonium Cell",
		"Tier": 5,
		"IsExact": True,
		"Stack": 32,
		"Description":[["NuclearFuel", "common"]],
	},{
		"Name": "DepletedUraniumCell",
		"Label": "Depleted Uranium Cell",
		"Tier": 5,
		"IsExact": True,
		"Stack": 32,
		"Description":[["NuclearFuel", "common"]],
	},{
		"Name": "Thorium",
		"Label": "Thorium",
		"IsBlock": True,
		"IsDust": True,
	},{
		"Name": "Sodium",
		"Label": "Sodium",
		"IsDust": True,
		"Tier": 3,
		"IsBlock": True,
	},{
		"Name": "SodiumHydroxide",
		"Label": "Sodium Hydroxide",
		"IsDust": True,
		"Tier": 3,
		"IsBlock": True,
	},{
		"Name": "Potassium",
		"Label": "Potassium",
		"IsDust": True,
		"Tier": 3,
		"IsBlock": True,
	},{
		"Name": "Sulfur",
		"Label": "Sulfur",
		"IsExact": True,
		"Mesh": "Models/Dust",
	},{
		"Name": "Steam",
		"Label": "Steam",
		"IsGas": True,
		"Unit": "J",
		"UnitMul": 1,
		"Color":[1,1,1]
	},{
		"Name": "Chlorine",
		"Label": "Chlorine",
		"IsGas": True,
		"Tier": 4,
		"Color": [1,1,0],
	},{
		"Name": "Peat",
		"Label": "Peat",
		"IsExact": True,
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 10,
			"TotalAsh": 0.24
		},
		"Tier": 0,
		"Color":[0.2,0.2,0.0],
		"Mesh": "Models/Piece"
	},{
		"Name": "Coal",
		"Label": "Coal",
		"IsExact": True,
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 20,
			"TotalAsh": 0.12
		},
		"Tier": 0,
		"Color":[0.0,0.0,0.0],
		"Mesh": "Models/Piece"
	},{
		"Name": "Coke",
		"Label": "Coke",
		"IsExact": True,
		"Burnable": {
			"BurnTime": 400/1.5,
			"HeatPerTick": 30*1.5,
			"TotalAsh": 0.06
		},
		"Color":[0.0,0.0,0.0],
		"Mesh": "Models/Piece"
	},{
		"Name": "Creosote",
		"Label": "Creosote",
		"IsGas": True,
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 20,
		},
		"Tier": 0,
		"Color":[0.0,0.0,0.0],
		"Mesh": "Models/Piece"
	},{
		"Name": "ProducerGas",
		"Label": "Producer Gas",
		"IsGas": True,		
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 80,
			"TotalAsh": 0
		},
		"Color": [1,1,1],
		"MoreEfficientIn":"GasTurbine"
	},{
		"Name": "CarbonMonoxide",
		"Label": "Carbon Monoxide",
		"IsGas": True,		
		"Burnable": {
			"BurnTime": 200,
			"HeatPerTick": 40,
			"TotalAsh": 0
		},
		"Color": [0.5,0.5,0.5],
		"MoreEfficientIn":"GasTurbine"
	},{
		"Name": "NitricAcid",
		"Label": "Nitric Acid",
		"IsFluid": True,		
		"Color": [1.0,0.5,0.0],
	},{
		"Name": "Ash",
		"Label": "Ash",
		"IsExact": True,
		"Tier": 0
	},{
		"Name": "Hydrogen",
		"Label": "Hydrogen",
		"IsGas": True,
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 160,
			"TotalAsh": 0
		},
		"Tier": 2,
		"Color": [.2,.2,.5],
	},{
		"Name": "Ethanol",
		"Label": "Ethanol",
		"IsGas": True,
		"Burnable": {
			"BurnTime": 500,
			"HeatPerTick": 45,
			"TotalAsh": 0
		},
		"Tier": 2,
		"Color":[0.5,0.2,0.2]
	},{
		"Name": "Methane",
		"Label": "Methane",
		"IsGas": True,
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 40,
			"TotalAsh": 0
		},
		"Tier": 2,
		"Color":[0.5,0.2,0.2]
	},{
		"Name": "Ethylene",
		"Label": "Ethylene",
		"IsGas": True,
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 50,
			"TotalAsh": 0
		},
		"Tier": 2,
		"Color": [.2,.5,.2],
	},
	#,{
	#	"Name": "Nickel",
	#	"Label": "Nickel",
	#	"SmeltLevel": 0,
	#	"IsMetal": True,
	#	"IsDust": True,
	#	"IsLiquidMetal": True,
	#	"IsBlock": True,
	#	"Tier": 3
	#}
	{
		"Name": "Water",
		"Label": "Water",
		"IsFluid": True,
		"Tier": 0
	},{
		"Name": "Glass",
		"Label": "Glass",
		"IsExact": True,
		"Tier": 0,
	},{
		"Name": "Lense",
		"Label": "Lense",
		"IsExact": True,
		"Tier": 0,
	},{
		"Name": "Organics",
		"Label": "Organics",
		"IsExact": True,
		"Tier": 0,
		"Mesh": "Models/Piece",
		"Description":[["Organics","common"]],
	},{
		"Name": "Biomass",
		"Label": "Biomass",
		"IsFluid": True,
	},{
		"Name": "FermentedBiomass",
		"Label": "Fermented Biomass",
		"IsFluid": True,
	},{
		"Name": "Ammonia",
		"Label": "Ammonia",
		"IsFluid": True,
	},{
		"Name": "Clay",
		"Label": "Clay",
		"Tier": 0,
		"IsExact": True,
		"Mesh": "Models/Piece"
	},{
		"Name": "OreWater",
		"Label": "Ore Water",
		"IsFluid": True,
	},{
		"Name": "RareEarthElement",
		"Label": "Rare Earth Element",
		"IsExact": True,
		"Mesh": "Models/Dust",
	},{
		"Name": "Log",
		"Label": "Log",
		"IsExact": True,
		"Tier": 0,
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 10, #5.5kwh
			"TotalAsh": 0.24
		},
		"Color":[0.9,0.9,0.9]
	},{
		"Name": "StoneLog",
		"Label": "Stone Log",
		"IsExact": True,
		"Tier": 0,
		"Burnable": {
			"BurnTime": 800,
			"HeatPerTick": 10,
			"TotalAsh": 0.5
		},
	},{
		"Name": "Plank",
		"Label": "Plank",
		"IsExact": True,
		"Tier": 0,
		"Burnable": {
			"BurnTime": 100,
			"HeatPerTick": 10,
			"TotalAsh": 0.24
		},
	},
	{
		"Name": "Silicon",
		"Label": "Silicon",
		"IsExact": True,
		"Tier": 3
	},
	{
		"Name": "SiliconWafer",
		"Label": "Silicon Wafer",
		"IsExact": True,
		"Tier": 4
	},
	{
		"Name": "SulfuricAcid",
		"Label": "Sulfuric Acid",
		"IsFluid": True,
		"Tier": 3
	},
	{
		"Name": "Rapeseed",
		"Label": "Rapeseed",
		"IsExact": True,
		"Tier": 0,
		"Color":[0.1,0.1,0.1]
	},
	{
		"Name": "RapeseedOil",
		"Label": "Rapeseed Oil",
		"IsFluid": True,
		"Tier": 0,
		"Burnable": {
			"BurnTime": 800,
			"HeatPerTick": 5,
			"TotalAsh": 2
		},
		"Color":[0.1,0.1,0.1]
	},
	{
		"Name": "RawOil",
		"Label": "Raw Oil",
		"IsFluid": True,
		"Tier": 0,
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 10,
			"TotalAsh": 1
		},
		"Color":[0.01,0.01,0.01]
	},
	{
		"Name": "MineralWater",
		"Label": "Mineral Water",
		"IsFluid": True,
		"Tier": 0
	},
	{
		"Name": "Gasoline",
		"Label": "Gasoline",
		"IsGas": True,
		"Tier": 1,
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 40,
			"TotalAsh": 0
		},
		"Color":[.5,.5,0.2]
	},{
		"Name": "Diesel",
		"Label": "Diesel",
		"IsFluid": True,
		"Tier": 1,
		"Burnable": {
			"BurnTime": 800,
			"HeatPerTick": 30,
			"TotalAsh": 0
		},
		"Color":[.2,.2,0.2]
	},{
		"Name": "HighCetaneDiesel",
		"Label": "High Cetane Diesel",
		"IsFluid": True,
		"Tier": 1,
		"Color":[.1,.1,0.1],
		"Burnable": {
			"BurnTime": 1000,
			"HeatPerTick": 50,
			"TotalAsh": 0
		}
	},{
		"Name": "Superfuel",
		"Label": "Superfuel",
		"IsFluid": True,
		"Tier": 1,
		"Color":[1,1,0.5],
		"Burnable": {
			"BurnTime": 2000,
			"HeatPerTick": 100,
			"TotalAsh": 0
		}
	},{
		"Name": "RocketFuel",
		"Label": "Rocket Fuel",
		"IsFluid": True,
		"Tier": 1,
		"Color":[0,1,0],
		"Burnable": {
			"BurnTime": 300,
			"HeatPerTick": 1000,
			"TotalAsh": 0
		}
	},{
		"Name": "ExtraHeavyOil",
		"Label": "Extra Heavy Oil",
		"IsGas": True,
		"Tier": 2,
		"Burnable": {
			"BurnTime": 800,
			"HeatPerTick": 10,
			"TotalAsh": 0
		},
		"Color":[0.01,.01,0.01]
	},
	{
		"Name": "HeavyOil",
		"Label": "Heavy Oil",
		"IsGas": True,
		"Tier": 2,
		"Burnable": {
			"BurnTime": 400,
			"HeatPerTick": 20,
			"TotalAsh": 0
		},
		"Color":[0.2,.5,0.2]
	},
	{
		"Name": "Battery",
		"Label": "Battery",
		"IsExact": True,
		"Tier": 3
	},
	{
		"Name": "SiliconOxide",
		"Label": "Silicon Oxide",
		"IsExact": True,
		"Tier": 1
	},{
		"Name": "Pumpkin",
		"Label": "Pumpkin",
		"IsExact": True,
		"Tier": 0
	},{
		"Name": "Oxygen",
		"Label": "Oxygen",
		"IsGas": True,
		"Tier": 4
	},{
		"Name": "Nitrogen",
		"Label": "Nitrogen",
		"IsGas": True,
		"Tier": 4
	},{
		"Name": "ChromiumOxide",
		"Label": "Chromium Oxide",
		"IsDust": True,
		"Tier": 3
	},{
		"Name": "PotassiumChloride",
		"Label": "Potassium Chloride",
		"IsDust": True,
		"Tier": 3
	},{
		"Name": "Beryllium",
		"Label": "Beryllium",
		"IsDust": True,
		"Tier": 4
	},{
		"Name": "Yttrium",
		"Label": "Yttrium",
		"IsDust": True,
		"Tier": 3
	},{
		"Name": "Helium",
		"Label": "Helium",
		"IsGas": True,
		"IsPlasma": True,
		"Tier": 4
	},{
		"Name": "Salt",
		"Label": "Salt",
		"IsDust": True,
		"Tier": 4
	},{
		"Name": "PortalBase",
		"Label": "Portal Base",
		"IsExact": True,
		"Tier": 2
	},{
		"Name": "Signal",
		"Label": "Signal",
		"IsExact": True
	},{
		"Name" : "CopperWire",
		"Label" : "Copper Wire",
		"Stack": 64,
		"IsExact": True,
		"Category": "Parts",
		"Mesh":"Models/WireCrate",
		"Materials":["Materials/CopperWiresOnCrate"],
	},{
		"Name" : "GoldWire",
		"Label" : "Gold Wire",
		"Stack": 64,
		"IsExact": True,
		"Category": "Parts",
		"Mesh":"Models/WireCrate",
		"Materials":["Materials/GoldWiresOnCrate"],
	},{
		"Name" : "SuperconductorWire",
		"Label" : "Superconductor Wire",
		"Stack": 64,
		"IsExact": True,
		"Category": "Parts",
		"Mesh":"Models/WireCrate",
		"Materials":["Materials/SuperWiresOnCrate"],
	},{
		"Name" : "Circuit",
		"Label" : "Circuit",
		"Stack": 32,
		"IsExact": True,
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "Models/CircuitCrate"
	},{
		"Name" : "AdvancedCircuit",
		"Label" : "Advanced Circuit",
		"Stack": 32,
		"IsExact": True,
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "Models/Circuit2Crate"
	},{
		"Name" : "Processor",
		"Label" : "Processor",
		"Stack": 32,
		"IsExact": True,
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "Models/Circuit3Crate"
	},{
		"Name" : "QuantumCircuit",
		"Label" : "Quantum Circuit",
		"Stack": 32,
		"IsExact": True,
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "Models/Circuit3Crate"
	},{
		"Name" : "QuantumProcessor",
		"Label" : "Quantum Processor",
		"Stack": 32,
		"IsExact": True,
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "Models/Circuit3Crate"
	},{
		"Name" : "QuantumCore",
		"Label" : "Quantum Core",
		"Stack": 32,
		"IsExact": True,
		"Category": "Parts",
		"Mesh": "Models/Circuit3Crate"
	},{
		"Name" : "QuantumBrain",
		"Label" : "Quantum Brain",
		"Stack": 32,
		"IsExact": True,
		"Category": "Parts",
		"Description":[["Circuit","common"]],
		"Mesh": "Models/Circuit3Crate"
	},{
		"Name" : "Cell",
		"Label" : "Cell",
		"Stack": 32,
		"IsExact": True,
		"Category": "Parts",
	},{
		"Name" : "Catalyst",
		"Label" : "Catalyst Cell",
		"Stack": 32,
		"IsExact": True,
	},{
		"Name" : "UltimateCatalyst",
		"Label" : "Ultimate Catalyst Cell",
		"Stack": 32,
		"IsExact": True,
	},{
		"Name" : "MothershipPing",
		"Label" : "Mothership Ping",
		"Stack": 32,
		"IsExact": True,
	},{
		"Name" : "ControlCell",
		"Label" : "Control Cell",
		"Stack": 32,
		"IsExact": True,
	},{
		"Name" : "ReflectorCell",
		"Label" : "Reflector Cell",
		"Stack": 32,
		"IsExact": True,
	},{
		"Name" : "ThoriumCell",
		"Label" : "Thorium Cell",
		"Stack": 32,
		"IsExact": True,
	},{
		"Name" : "MixedOxideCell",
		"Label" : "Mixed-Oxide Cell",
		"Stack": 32,
		"IsExact": True,
	},{
		"Name" : "RutileCrystal",
		"Label" : "Rutile Crystal",
		"Stack": 32,
		"IsExact": True,
		"Category": "Mineral",
	},{
		"Name" : "UraniniteCrystal",
		"Label" : "Uraninite Crystal",
		"Stack": 32,
		"IsExact": True,
		"Category": "Mineral",
	},{
		"Name" : "UraniniteCluster",
		"Label" : "Uraninite Cluster",
		"Stack": 32,
		"IsExact": True,
		"Category": "Mineral",
	},{
		"Name" : "Cinnabar",
		"Label" : "Cinnabar",
		"Stack": 32,
		"IsDust": True,
		"Category": "Mineral",
	},{
		"Name" : "CinnabarCrystal",
		"Label" : "Cinnabar Crystal",
		"Stack": 32,
		"IsExact": True,
		"Category": "Mineral",
	},{
		"Name" : "CinnabarCluster",
		"Label" : "Cinnabar Cluster",
		"Stack": 32,
		"IsExact": True,
		"Category": "Mineral",
	},{
		"Name" : "Malachite",
		"Label" : "Malachite",
		"Stack": 32,
		"IsDust": True,
		"Category": "Mineral",
	},{
		"Name" : "MalachiteCrystal",
		"Label" : "Malachite Crystal",
		"Stack": 32,
		"IsExact": True,
		"Category": "Mineral",
	},{
		"Name" : "MalachiteCluster",
		"Label" : "Malachite Cluster",
		"Stack": 32,
		"IsExact": True,
		"Category": "Mineral",
	},{
		"Name" : "Mercury",
		"Label" : "Mercury",
		"IsFluid": True,
	},{
		"Name" : "FilteringCell",
		"Label" : "Filtering Cell",
		"Stack": 32,
		"IsExact": True,
	},{
		"Name": "Boron",
		"Label": "Boron",
		"IsDust": True,
		"Tier": 4
	},{
		"Name" : "Borax",
		"Label" : "Borax",
		"Stack": 32,
		"IsDust": True,
		"Category": "Mineral",
	},{
		"Name" : "Emerald",
		"Label" : "Emerald",
		"Stack": 32,
		"IsExact": True,
		"IsDust": True,
		"Category": "Mineral",
	},{
		"Name" : "Capacity",
		"Label" : "Capacity",
		"Craftable": False,
		"IsExact": True,
		"Category": "Signal"
	},{
		"Name" : "InputError",
		"Label" : "Input Error",
		"Craftable": False,
		"IsExact": True,
		"Category": "Signal"
	},{
		"Name" : "OutputError",
		"Label" : "Output Error",
		"Craftable": False,
		"IsExact": True,
		"Category": "Signal"
	},{
		"Name" : "Progress",
		"Label" : "Progress",
		"Craftable": False,
		"IsExact": True,
		"Category": "Signal"
	},{
		"Name" : "SwitchedOn", 
		"Label" : "Switched On",
		"Craftable": False,
		"IsExact": True,
		"Category": "Signal"
	},{
		"Name": "Drain",
		"Label": "Drain",
		"IsExact": True,
		"Craftable": False,
		"Category": "Signal"
	},{
		"Name": "Percent",
		"Label": "Percent",
		"IsExact": True,
		"Craftable": False,
		"Category": "Signal"
	}
]

import string

for a in list(string.ascii_uppercase):
	materials.append({
		"Name": a,
		"Label": a,
		"IsExact": True,
		"Craftable": False,
		"Category": "Signal",
	})

materials.append({
	"Name": "ErrorString",
	"Label": "Error String",
	"IsExact": True,
	"Craftable": False,
	"Category": "Signal"
})