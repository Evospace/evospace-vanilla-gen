technology_lines = {
	"Smelting": [
		(2, "RegenerativeFurnace"),
		(3, "MagnesiteRefractories"),
		(4, "InductionMelting"),
		(5, "VacuumArcRemelting"),
		(6, "PlasmaSpraying"),
		(7, "LevitationMelting"),
	],
	"Mechanics": [
		(2, "InterchangeableParts"),
		(3, "BallBearings"),
		(4, "CementedCarbide"),
		(5, "NumericalControl"),
		(6, "LaserCutting"),
		(7, "MolecularAssembly"),
	],
	"Heat": [
		(3, "WaterTubeBoiler"),
		(4, "SuperheatedSteam"),
		(5, "Superalloys"),
		(6, "SupercriticalSteam"),
		(7, "Magnetohydrodynamics"),
	],
	"Chemistry": [
		(3, "CentrifugalPump"),
		(4, "Passivation"),
		(5, "CatalyticCracking"),
		(6, "FilamentWinding"),
		(7, "NeutroniumLining"),
	],
	"Generation": [
		(2, "Dynamo"),
		(3, "ThreePhaseCurrent"),
		(4, "ElectricalSteel"),
		(5, "Turbocharging"),
		(6, "PowerElectronics"),
		(7, "Superconductivity"),
	],
	"Electronics": [
		(4, "SeleniumPhotocell"),
		(5, "SiliconSolarCell"),
		(6, "ThinFilmCells"),
		(7, "QuantumDots"),
	],
	"Logistics": [
		(2, "BeltDrive"),
		(3, "AssemblyLine"),
		(4, "Hydraulics"),
		(5, "IndustrialRobots"),
		(6, "MachineVision"),
		(7, "MagneticLevitation"),
	],
	"Storage": [
		(2, "SheetRolling"),
		(3, "DieCasting"),
		(4, "SpotWelding"),
		(5, "Anodizing"),
		(6, "AutoclaveMolding"),
		(7, "DegenerateMatter"),
	],
}

technology_images = {
	"RegenerativeFurnace",
	"InterchangeableParts",
	"BeltDrive",
	"Dynamo",
	"SheetRolling",
	"MagnesiteRefractories",
	"BallBearings",
	"WaterTubeBoiler",
	"CentrifugalPump",
	"ThreePhaseCurrent",
	"DieCasting",
}

technology_line_roots = {
	"Heat": "RegenerativeFurnace",
	"Chemistry": "InterchangeableParts",
	"Electronics": "ThreePhaseCurrent",
}

technology_metal = {
	2: "SteelProduction",
	3: "AluminiumProduction",
	4: "StainlessSteelProduction",
	5: "TitaniumProduction",
	6: "CompositePlate",
	7: "NeutroniumProduction",
}

technology_splits = {
	"AssemblyLine": ("RotaryDrilling", {"AutomaticMining", "Pumpjack", "AutomaticFarm"}),
	"Hydraulics": ("Turbodrilling", {"AutomaticMining", "Pumpjack", "AutomaticFarm"}),
	"IndustrialRobots": ("DiamondDrilling", {"AutomaticMining", "Pumpjack", "AutomaticFarm"}),
	"CementedCarbide": ("FrothFlotation", {"Sifter", "Separator", "OreWasher"}),
	"NumericalControl": ("MagneticSeparation", {"Sifter", "Separator", "OreWasher"}),
	"LaserCutting": ("XRaySorting", {"Sifter", "Separator", "OreWasher"}),
	"MolecularAssembly": ("IsotopeSeparation", {"Sifter", "Separator", "OreWasher"}),
	"SupercriticalSteam": ("CeramicComposites", {"KineticHeater", "Boiler", "SteamEngine", "SteamTurbine"}),
	"Magnetohydrodynamics": ("Nanofluids", {"KineticHeater", "Boiler", "SteamEngine", "SteamTurbine"}),
	"CatalyticCracking": ("VacuumDistillation", {"Pump", "AtmosphericCondenser", "FractionatingColumn"}),
	"PowerElectronics": ("NeodymiumMagnets", {"ElectricEngine", "WindTurbine", "CombustionEngine"}),
	"FilamentWinding": ("MembraneSeparation", {"Pump", "AtmosphericCondenser", "FractionatingColumn"}),
	"ThinFilmCells": ("GalliumNitride", {"Diode", "DistributedComputing", "ResearchLaboratory"}),
	"MachineVision": ("DirectionalDrilling", {"AutomaticMining", "Pumpjack", "AutomaticFarm"}),
	"LevitationMelting": ("ElectronBeamMelting", {"ElectricFurnace", "AdvancedSmelting", "IndustrialSmelting"}),
	"MagneticLevitation": ("PlasmaDrilling", {"AutomaticMining", "Pumpjack", "AutomaticFarm"}),
	"NeutroniumLining": ("Superfluidity", {"Pump", "AtmosphericCondenser", "FractionatingColumn"}),
	"Superconductivity": ("MagneticBearings", {"ElectricEngine", "WindTurbine", "CombustionEngine"}),
}

def technology_whole(name):
	for whole, (half, _) in technology_splits.items():
		if half == name:
			return whole
	return name

def technology_names(whole):
	return [whole] + ([technology_splits[whole][0]] if whole in technology_splits else [])

series_lines = {
	"Furnace": "Smelting",
	"Smelting": "Smelting",
	"Oven": "Smelting",
	"SteelProduction": "Smelting",
	"AdvancedSmelting": "Smelting",
	"ElectricFurnace": "Smelting",
	"IndustrialSmelting": "Smelting",
	"FluidFurnace": "Smelting",
	"KineticHeater": [(2, "Smelting"), (3, "Heat")],

	"Boiler": "Heat",
	"IndustrialBoiler": "Heat",
	"SteamEngine": "Heat",
	"SteamTurbine": "Heat",
	"IndustrialSteamTurbine": "Heat",
	"FissionReactor": "Heat",
	"Riteg": "Heat",
	"FusionReactor": "Heat",

	"BasicMachines": "Mechanics",
	"Macerator": "Mechanics",
	"Constructor": "Mechanics",
	"Assembler": "Mechanics",
	"Mixer": "Mechanics",
	"Separator": "Mechanics",
	"Sifter": "Mechanics",
	"OreWasher": "Mechanics",
	"Pump": [(2, "Mechanics"), (3, "Chemistry")],
	"AtmosphericCondenser": [(2, "Mechanics"), (3, "Chemistry")],

	"ChemicalBath": "Chemistry",
	"IndustrialChemReactor": "Chemistry",
	"Fermentation": "Chemistry",
	"PyrolysisUnit": "Chemistry",
	"FractionatingColumn": "Chemistry",
	"Electrolyzer": "Chemistry",

	"ElectricEngine": "Generation",
	"PowerGeneration": "Generation",
	"Generator": "Generation",
	"IndustrialGenerator": "Generation",
	"CombustionEngine": "Generation",
	"WindTurbine": "Generation",
	"Diode": [(2, "Generation"), (4, "Electronics")],
	"DistributedComputing": [(2, "Generation"), (4, "Electronics")],
	"ResearchLaboratory": [(2, "Generation"), (4, "Electronics")],
	"BatteryBox": "Electronics",
	"SmallSolarPanel": "Electronics",
	"SolarPanel": "Electronics",

	"Automatization": "Logistics",
	"Conveyor": "Logistics",
	"Splitter": "Logistics",
	"Loader": "Logistics",
	"Sorter": "Logistics",
	"AutomaticMining": "Logistics",
	"AutomaticFarm": "Logistics",
	"Pumpjack": "Logistics",

	"Chest": "Storage",
	"Container": "Storage",
	"SingleTypeStorage": "Storage",
	"DeepStorage": "Storage",
	"Destroyer": "Storage",
	"Lamp": "Storage",
	"Sign": "Storage",
	"AdvancedSign": "Storage",
	"MetalBlocks": "Storage",
	"InventoryUpgrade": "Storage",
}

def technology_line(series, tier):
	line = series_lines.get(series)
	if line is None:
		raise Exception(f"Technologies: series {series} has tier versions but no technology line")
	if isinstance(line, list):
		line = [name for start, name in line if start <= tier][-1]
	return line

def technology_for(series, tier):
	line = technology_line(series, tier)
	for line_tier, name in technology_lines[line]:
		if line_tier == tier:
			split = technology_splits.get(name)
			return split[0] if split and series in split[1] else name
	raise Exception(f"Technologies: line {line} has no technology for tier {tier}, needed by {series}")

def technology_previous(name):
	whole = technology_whole(name)
	for line, entries in technology_lines.items():
		for index, (tier, entry) in enumerate(entries):
			if entry == whole:
				previous = entries[index - 1][1] if index > 0 else technology_line_roots.get(line)
				if whole != name and previous in technology_splits and technology_splits[previous][1] & technology_splits[whole][1]:
					return technology_splits[previous][0]
				return previous
	raise Exception(f"Technologies: {name} is in no line")

def technology_tier(name):
	whole = technology_whole(name)
	for entries in technology_lines.values():
		for tier, entry in entries:
			if entry == whole:
				return tier
	raise Exception(f"Technologies: {name} is in no line")
