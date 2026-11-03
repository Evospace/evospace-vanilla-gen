from Common import *
from Materials import *
from MachinesList import machines

tier_cost_mul = {1: 0.88, 2: 0.44, 3: 0.32, 4: 1.32, 5: 1.81, 6: 2.67}

experiment_ticks = 600

milestones = [
	{
		"Name": "Start",
		"Label": "MineralsScan",
		"Position": [1, 0],
		"Chunks": {"CircuitBoard": [-1, 0], "AutomaticHammer": [1, 0], "Bricks": [1, 0], "FluidTransfer": [0, 1]},
		"Tree": [
			["MineralsScan", ""],
			["Smelting", "MineralsScan"],
			["Metalwork", "Smelting"],
			["Chest", "Smelting"],
			["Container", "Chest"],
			["SingleTypeStorage", "Chest"],
			["InventoryUpgrade", "Chest"],
			["BasicPlatform", "MineralsScan"],
			["Lamp", "Smelting"],
			["PowerGeneration", "Metalwork"],
			["Furnace", "PowerGeneration"],
			["Destroyer", "Furnace"],
			["Oven", "Furnace"],
			["EngineeringLaboratory", "Oven"],
			["DistributedComputing", "PowerGeneration"],
			["CopperWire", "PowerGeneration"],
			["PowerTransmission", "CopperWire"],
			["CircuitBoard", "CopperWire"],
			["WireCover", "CircuitBoard"],
			["Triod", "CircuitBoard"],
			["Circuit", "Triod"],
			["Beacon", "Triod"],
			["LogicNetworking", "Circuit"],
			["LogicDevices", "LogicNetworking"],
			["AdvancedSign", "LogicDevices"],
			["Spotlight", "Circuit"],
			["Flashlight", "Spotlight"],
			["GlassBlock", "Spotlight"],
			["Constructor", "Circuit"],
			["ElectronicsLaboratory", "Constructor"],
			["AutomaticHammer", "Metalwork"],
			["Automatization", "AutomaticHammer"],
			["Conveyor", "Automatization"],
			["AutomaticMining", "Automatization"],
			["Macerator", "AutomaticMining"],
			["Splitter", "Macerator"],
			["Loader", "Splitter"],
			["ConstructionTool", "Splitter"],
			["DeconstructionTool", "ConstructionTool"],
			["UpgradeTool", "DeconstructionTool"],
						["AutomaticFarm", "Splitter"],
			["DrillingRigProductivity", "AutomaticFarm"],
			["Bricks", "Macerator"],
			["Designable", "Bricks"],
			["DecorativeWood", "Designable"],
			["Door", "DecorativeWood"],
			["Sign", "Designable"],
			["StoneTiles", "Bricks"],
			["RedTiles", "StoneTiles"],
			["DarkTiles", "RedTiles"],
			["Terracotta", "RedTiles"],
			["TerracottaTiles", "Terracotta"],
			["TerracottaBricks", "TerracottaTiles"],
			["RedBricks", "Bricks"],
			["DarkBricks", "RedBricks"],
			["MetalBlocks", "DarkBricks"],
			["FluidTransfer", "AutomaticFarm"],
			["Pump", "FluidTransfer"],
			["AtmosphericCondenser", "Pump"],
			["DecorativePaint", "Pump"],
			["Valve", "FluidTransfer"],
			["Steampack", "Valve"],
			["HighCapacitySteampack", "Steampack"],
			["HighPressureSteampack", "HighCapacitySteampack"],
			["HeatTransferring", "FluidTransfer"],
			["KineticHeater", "HeatTransferring"],
			["FluidFurnace", "HeatTransferring"],
		],
		"Exits": [["ElectronicsLaboratory", "Transistor"], ["EngineeringLaboratory", "Steel"]],
		"Experiments": 0,
		"Experiment": [],
	},
	{
		"Name": "Steel",
		"Label": "SteelProduction",
		"Position": [1, 1],
		"Laboratory": "EngineeringLaboratory",
		"Tree": [
			["SteelProduction", ""],
			["AdvancedSmelting", "SteelProduction"],
			["ElectricFurnace", "AdvancedSmelting"],
			["Electrolyzer", "AdvancedSmelting"],
			["Separator", "Electrolyzer"],
			["OreWasher", "Separator"],
			["Mixer", "OreWasher"],
			["BasicFrame", "SteelProduction"],
			["Sorter", "SteelProduction"],
			["Railway", "BasicFrame"],
			["RailSignals", "Railway"],
			["Concrete", "BasicFrame"],
			["ConcreteBricks", "ConcreteTiles"],
			["ConcreteTiles", "Concrete"],
			["ConcreteSmallTiles", "ConcreteTiles"],
			["Roadwork", "Concrete"],
			["MetalDoors", "BasicFrame"],
			["Designable2", "MetalDoors"],
		],
		"Exits": [["Separator", "Aluminium"], ["SteelProduction", "Steam"]],
		"Experiments": 25,
		"Experiment": [["Triod", 1], ["CopperPipe", 2], ["CopperConveyor", 1]],
	},
	{
		"Name": "Steam",
		"Label": "SteamEngine",
		"Rows": 7,
		"Position": [2, 1],
		"Laboratory": "EngineeringLaboratory",
		"Tree": [
			["Boiler", ""],
			["SteamEngine", "Boiler"],
			["Flywheel", "SteamEngine"],
			["Generator", "ElectricEngine"],
			["SteamTurbine", "Generator"],
			["ElectricEngine", "BasicCoil"],
			["BasicCoil", "Boiler"],
			["WindTurbine", "ElectricEngine"],
			["ElectricalSwitch", "Generator"],
			["Diode", "ElectricalSwitch"],
			["SmallSolarPanel", "Diode"],
			["SolarPanel", "SmallSolarPanel"],
			["Dynamo", "SteamTurbine"],
			["RegenerativeFurnace", "Boiler"],
			["SheetRolling", "RegenerativeFurnace"],
			["DecorativeWood2", "SteamEngine"],
			["IndustrialChemReactor", "ElectricEngine"],
			["ChemicalLaboratory", "IndustrialChemReactor"],
		],
		"Exits": [["ChemicalLaboratory", "Chemistry"]],
		"Experiments": 25,
		"Experiment": [["CopperPump", 1], ["SteelPipe", 1]],
	},
	{
		"Name": "Transistor",
		"Label": "Processor",
		"Title": "Microelectronics",
		"Image": "T_Microelectronics",
		"Position": [0, 1],
		"Laboratory": "ElectronicsLaboratory",
		"Tree": [
			["Resistor", ""],
			["Resistor2", "Resistor"],
			["AdvancedCircuit", "Resistor"],
			["NightVision", "AdvancedCircuit"],
			["CircuitBoard2", "AdvancedCircuit"],
			["Transistor", "AdvancedCircuit"],
			["Transistor2", "Transistor"],
			["Circuit2", "Transistor"],
			["Assembler", "Processor"],
			["Processor", "Transistor"],
			["SatelliteAntenna", "Processor"],
			["Capacitor", "Assembler"],
			["Capacitor2", "Capacitor"],
			["InterchangeableParts", "Assembler"],
			["BeltDrive", "InterchangeableParts"],
		],
		"Exits": [["SatelliteAntenna", "SatelliteAntenna"]],
		"Experiments": 25,
		"Experiment": [["Circuit", 4], ["CopperWire", 4]],
	},
	{
		"Name": "SatelliteAntenna",
		"Label": "SatelliteAntenna",
		"Position": [0, 2],
		"Build": "SatelliteAntenna",
		"Tree": [],
		"Exits": [["", "Silicon"]],
		"Experiments": 1,
	},
	{
		"Name": "Aluminium",
		"Label": "AluminiumProduction",
		"Position": [1, 2],
		"Laboratory": "EngineeringLaboratory",
		"Tree": [
			["AluminiumReduction", ""],
			["AluminiumProduction", "AluminiumReduction"],
			["ReinforcedFrame", "AluminiumProduction"],
			["Boat", "ThreePhaseCurrent"],
			["OffroadVehicle", "Boat"],
			["Jetpack", "Boat"],
			["Sifter", "ThreePhaseCurrent"],
			["ReinforcedConcrete", "ReinforcedFrame"],
			["ReinforcedConcreteTiles", "ReinforcedConcrete"],
			["ReinforcedConcreteSmallTiles", "ReinforcedConcreteTiles"],
			["ReinforcedConcreteBricks", "ReinforcedConcreteTiles"],
			["DangerBlock", "ReinforcedConcrete"],
			["DecorativeWood3", "DangerBlock"],
			["Designable3", "DecorativeWood3"],
			["DecorativeWood4", "Designable3"],
			["ThreePhaseCurrent", "AluminiumProduction"],
			["BallBearings", "AluminiumProduction"],
			["AssemblyLine", "BallBearings"],
			["RotaryDrilling", "AssemblyLine"],
			["DieCasting", "ReinforcedFrame"],
		],
		"Exits": [["AluminiumProduction", "StainlessSteel"]],
		"Experiments": 30,
		"Experiment": [["SteelElectrolyzer", 1], ["SteelSeparator", 1]],
	},
	{
		"Name": "Chemistry",
		"Label": "ChemicalBath",
		"Position": [2, 2],
		"Laboratory": "ChemicalLaboratory",
		"Tree": [
			["ChemicalBath", ""],
			["Catalyst", "ChemicalBath"],
			["Catalyst2", "SulfuricAcid"],
			["Polyethylene", "Catalyst"],
			["Sulfur", "ChemicalBath"],
			["SulfuricAcid", "Catalyst"],
			["Battery", "SulfuricAcid"],
			["BatteryBox", "Battery"],
			["Fermentation", "ChemicalBath"],
			["CentrifugalPump", "Fermentation"],
			["WaterTubeBoiler", "ChemicalBath"],
			["MagnesiteRefractories", "WaterTubeBoiler"],
			["PlasticBlock", "Polyethylene"],
		],
		"Exits": [["Catalyst", "Oil"]],
		"Experiments": 25,
		"Experiment": [["Sulfur", 4], ["SteelElectricEngine", 1]],
	},
	{
		"Name": "Silicon",
		"Label": "QuantumCircuit",
		"Position": [0, 3],
		"Laboratory": "ElectronicsLaboratory",
		"Tree": [
			["SiliconWafer", ""],
			["Processor2", "SiliconWafer"],
			["Capacitor3", "Processor2"],
			["Transistor3", "SiliconWafer"],
			["Resistor3", "Transistor3"],
			["RareEarthSludge", "SiliconWafer"],
			["QuantumCore", "RareEarthSludge"],
			["StorageCore", "QuantumCore"],
			["DeepStorage", "StorageCore"],
			["QuantumCircuit", "QuantumCore"],
			["QuantumCircuit2", "QuantumCircuit"],
			["DecisionResonator", "QuantumCircuit"],
			["DecisionResonator2", "DecisionResonator"],
			["QuantumProcessor", "DecisionResonator"],
			["QuantumProcessor2", "QuantumProcessor"],
		],
		"Exits": [["QuantumProcessor", "QuantumBrain"]],
		"Experiments": 50,
		"Experiment": [["Processor", 1], ["AdvancedCircuit", 2]],
	},
	{
		"Name": "StainlessSteel",
		"Label": "StainlessSteelProduction",
		"Position": [1, 3],
		"Laboratory": "EngineeringLaboratory",
		"Tree": [
			["AdvancedAlloys", ""],
			["StainlessSteelProduction", "AdvancedAlloys"],
			["IndustrialSmelting", "StainlessSteelProduction"],
			["IndustrialSteelProduction", "IndustrialSmelting"],
			["ModularFrame", "StainlessSteelProduction"],
			["Monitor", "ModularFrame"],
			["AdvancedNightVision", "Monitor"],
			["AdvancedCoil", "StainlessSteelProduction"],
			["AdvancedJetpack", "AdvancedCoil"],
			["AdvancedSteampack", "AdvancedJetpack"],
			["CementedCarbide", "ModularFrame"],
			["FrothFlotation", "CementedCarbide"],
			["SpotWelding", "ModularFrame"],
			["Hydraulics", "StainlessSteelProduction"],
			["Turbodrilling", "Hydraulics"],
			["SeleniumPhotocell", "AdvancedNightVision"],
		],
		"Exits": [["IndustrialSmelting", "Titanium"]],
		"Experiments": 100,
		"Experiment": [["AluminiumElectricEngine", 1], ["AluminiumPipe", 4], ["AluminiumFoil", 6]],
	},
	{
		"Name": "Oil",
		"Label": "FuelChemistry",
		"Position": [2, 3],
		"Laboratory": "ChemicalLaboratory",
		"Tree": [
			["PyrolysisUnit", ""],
			["PreciseTemperaturePyrolysis", "PyrolysisUnit"],
			["FuelChemistry", "PreciseTemperaturePyrolysis"],
			["FuelChemistry2", "FuelChemistry"],
			["FuelChemistry3", "FuelChemistry2"],
			["FractionatingColumn", "Passivation"],
			["CombustionEngine", "FuelChemistry"],
			["Pumpjack", "PyrolysisUnit"],
			["PumpjackProductivity", "Pumpjack"],
			["InductionMelting", "PyrolysisUnit"],
			["Passivation", "FuelChemistry"],
			["SuperheatedSteam", "FuelChemistry2"],
			["ElectricalSteel", "CombustionEngine"],
			["DecorativePlastic", "PyrolysisUnit"],
		],
		"Exits": [],
		"Experiments": 100,
		"Experiment": [["Battery", 6], ["PolyethyleneSheet", 6]],
	},
	{
		"Name": "QuantumBrain",
		"Label": "QuantumBrain",
		"Position": [0, 5],
		"Laboratory": "ElectronicsLaboratory",
		"Tree": [
			["BrainMatrix", ""],
			["QuantumBrain", "BrainMatrix"],
			["QuantumBrain2", "QuantumBrain"],
			["AntigravityUnit", "QuantumBrain"],
			["DopedSiliconWafer", "BrainMatrix"],
			["Processor3", "DopedSiliconWafer"],
			["Transistor4", "DopedSiliconWafer"],
			["DecisionResonator3", "DopedSiliconWafer"],
			["DecisionResonator4", "DecisionResonator3"],
		],
		"Exits": [],
		"Experiments": 100,
		"Experiment": [["QuantumProcessor", 2], ["QuantumCircuit", 5]],
	},
	{
		"Name": "Titanium",
		"Label": "TitaniumProduction",
		"Position": [1, 4],
		"Laboratory": "EngineeringLaboratory",
		"CostMul": 2,
		"Tree": [
			["NitricAcid", ""],
			["KrollProcess", "NitricAcid"],
			["TitaniumProduction", "KrollProcess"],
			["FastSifting", "MagneticSeparation"],
			["MagneticSeparation", "NumericalControl"],
			["PowerCoil", "TitaniumProduction"],
			["NumericalControl", "PowerCoil"],
			["BigMonitor", "PowerCoil"],
			["Anodizing", "BigMonitor"],
			["IndustrialRobots", "NumericalControl"],
			["DiamondDrilling", "IndustrialRobots"],
			["PlatinumSolution", "NitricAcid"],
			["CircuitBoard3", "PlatinumSolution"],
			["SiliconSolarCell", "CatalyticCracking"],
			["CatalyticCracking", "TitaniumProduction"],
			["VacuumDistillation", "CatalyticCracking"],
			["CrudeTantalum", "NitricAcid"],
			["Capacitor4", "CrudeTantalum"],
			["Resistor4", "CrudeTantalum"],
		],
		"Exits": [["TitaniumProduction", "Composite"], ["FastSifting", "Nuclear"]],
		"Experiments": 125,
		"Experiment": [["ModularFrame", 1], ["AdvancedCoil", 4], ["SiliconMonocrystal", 3]],
	},
	{
		"Name": "Composite",
		"Label": "CompositePlate",
		"Position": [1, 5],
		"Laboratory": "EngineeringLaboratory",
		"Tree": [
			["CarbonFiber", ""],
			["CarbonFiberSheet", "CarbonFiber"],
			["CompositePlate", "CarbonFiberSheet"],
			["PlatinumReflector", "CompositePlate"],
			["HugeMonitor", "CompositePlate"],
			["FilamentWinding", "CompositePlate"],
			["MembraneSeparation", "AutoclaveMolding"],
			["AutoclaveMolding", "FilamentWinding"],
			["InventoryUpgrade5", "AutoclaveMolding"],
			["LaserCutting", "CompositePlate"],
			["XRaySorting", "LaserCutting"],
			["MachineVision", "HugeMonitor"],
			["DirectionalDrilling", "MachineVision"],
			["ThinFilmCells", "PlatinumReflector"],
			["GalliumNitride", "ThinFilmCells"],
			["SupercriticalSteam", "FilamentWinding"],
			["CeramicComposites", "SupercriticalSteam"],
			["PlasmaSpraying", "LaserCutting"],
			["PowerElectronics", "GalliumNitride"],
			["NeodymiumMagnets", "PowerElectronics"],
		],
		"Exits": [["PlatinumReflector", "Fusion"]],
		"Experiments": 150,
		"Experiment": [["PowerCoil", 4], ["TantalumWire", 4], ["PlatinumWire", 8]],
	},
	{
		"Name": "Nuclear",
		"Label": "FissionReactor",
		"Position": [2, 4],
		"Laboratory": "ChemicalLaboratory",
		"CostMul": 2,
		"CostMulOf": {name: 4 for name in ["UraniumCell", "FissionReactor", "ControlCell", "ReflectorCell", "ReactionThrottling", "AdvancedReflection", "AdvancedReflection2", "ThoriumReaction", "PlutoniumReaction", "PlutoniumReaction2"]},
		"Tree": [
			["UraniumCell", ""],
			["FissionReactor", "UraniumCell"],
			["ControlCell", "FissionReactor"],
			["ReflectorCell", "ControlCell"],
			["AdvancedReflection", "ReflectorCell"],
			["ThoriumReaction", "AdvancedReflection"],
			["PlutoniumReaction", "ThoriumReaction"],
			["PlutoniumReaction2", "PlutoniumReaction"],
			["Riteg", "PlutoniumReaction2"],
			["IndustrialBoiler", "FissionReactor"],
			["IndustrialSteamTurbine", "IndustrialBoiler"],
			["IndustrialGenerator", "IndustrialSteamTurbine"],
			["Superalloys", "IndustrialBoiler"],
			["Turbocharging", "IndustrialGenerator"],
			["VacuumArcRemelting", "FissionReactor"],
			["ReactionThrottling", "ControlCell"],
			["AdvancedReflection2", "ThoriumReaction"],
		],
		"Exits": [],
		"Experiments": 125,
		"Experiment": [["QuantumCircuit", 1], ["TitaniumPipe", 5], ["Cell", 9]],
	},
	{
		"Name": "Fusion",
		"Label": "FusionReaction",
		"Position": [1, 6],
		"Laboratory": "EngineeringLaboratory",
		"Tree": [
			["FusionReactor", ""],
			["Rocket", "FusionReactor"],
			["FusionReaction", "Rocket"],
			["CompositePlate2", "FusionReaction"],
			["NeutroniumProduction", "FusionReaction"],
			["NeutroniumProduction2", "UltimateCatalyst"],
			["UltimateCatalyst", "NeutroniumProduction"],
			["FuelChemistry4", "UltimateCatalyst"],
			["Portal", "UltimateCatalyst"],
			["LevitationMelting", "NeutroniumProduction"],
			["ElectronBeamMelting", "LevitationMelting"],
			["DegenerateMatter", "NeutroniumProduction2"],
			["Magnetohydrodynamics", "Superconductivity"],
			["Nanofluids", "Magnetohydrodynamics"],
			["Superconductivity", "NeutroniumProduction"],
			["MagneticBearings", "Superconductivity"],
			["MagneticLevitation", "Superconductivity"],
			["PlasmaDrilling", "MagneticLevitation"],
			["MolecularAssembly", "UltimateCatalyst"],
			["IsotopeSeparation", "MolecularAssembly"],
			["NeutroniumLining", "NeutroniumProduction2"],
			["Superfluidity", "NeutroniumLining"],
			["QuantumDots", "MolecularAssembly"],
			["InventoryUpgrade6", "DegenerateMatter"],
		],
		"Exits": [["Portal", "Infinite"]],
		"Experiments": 200,
		"Experiment": [["QuantumBrain", 1], ["PlatinumReflector", 8], ["CompositePipe", 3]],
	},
	{
		"Name": "Infinite",
		"Label": "DrillingRigProductivity8",
		"Position": [1, 7],
		"Tree": [
			["DrillingRigProductivity8", ""],
			["PumpjackProductivity8", "DrillingRigProductivity8"],
			["InventoryUpgrade7", "DrillingRigProductivity8"],
		],
		"Exits": [],
		"Experiments": 0,
		"Experiment": [],
	},
]

cell_columns = 7
tree_rows = 6
gap_columns = 3
column_pitch = cell_columns + gap_columns
card_step = 2
side_head = (2, 2)

steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
diagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

def objects_of(data):
	if isinstance(data, dict):
		data = data.get("Objects", [])
	return [o for o in data if isinstance(o, dict)] if isinstance(data, list) else []

def sign(value):
	return (value > 0) - (value < 0)

def direction(a, b):
	pa, pb = milestone_by_name[a]["Position"], milestone_by_name[b]["Position"]
	return (sign(pb[0] - pa[0]), sign(pb[1] - pa[1]))

def axis(d):
	return (0, d[1]) if d[1] else d

def add(a, b):
	return (a[0] + b[0], a[1] + b[1])

def scale(d, k):
	return (d[0] * k, d[1] * k)

def bends(points):
	out = []
	for p in points:
		if not out or out[-1] != p:
			out.append(p)
	return out

def through(points):
	cells = []
	for a, b in zip(points, points[1:]):
		d = (sign(b[0] - a[0]), sign(b[1] - a[1]))
		cell = a
		while cell != b:
			cell = add(cell, d)
			cells.append(cell)
	return cells[:-1]

def near(cell, taken):
	return any((cell[0] + dx, cell[1] + dy) in taken for dx in (-1, 0, 1) for dy in (-1, 0, 1))

def layout(m, columns, rows, head_cell, exit_dirs, entry):
	parent = {name: up for name, up in m["Tree"]}
	children = {name: [] for name, _ in m["Tree"]}
	for name, up in m["Tree"]:
		if up:
			children[up].append(name)
	head = m["Head"]

	size = {}
	def measure(name):
		size[name] = 1 + sum(measure(c) for c in children[name])
		return size[name]
	measure(head)

	def path_to(name):
		path = []
		while name:
			path.append(name)
			name = parent[name]
		return path[::-1]

	inside = lambda c: 0 <= c[0] < columns and 0 <= c[1] < rows
	pos = {head: head_cell}
	taken = {head_cell: head}
	reserved = set(entry)

	def free(cell):
		return inside(cell) and cell not in taken and cell not in reserved

	def room(cell):
		return sum(1 for s in steps if free((cell[0] + s[0], cell[1] + s[1])))

	def put(name, cell):
		pos[name] = cell
		taken[cell] = name

	below = {}
	def collect(name):
		dirs = list(exit_dirs.get(name, []))
		for c in children[name]:
			dirs += collect(c)
		below[name] = dirs
		return dirs
	collect(head)

	centre = (columns - 1) / 2
	middle = (rows - 1) / 2
	distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

	for exit_name in sorted(exit_dirs, key=lambda e: -len(path_to(e))):
		path = path_to(exit_name)
		last = None
		for a, b in zip(path, path[1:]):
			if b in pos:
				last = (pos[b][0] - pos[a][0], pos[b][1] - pos[a][1])
				continue
			d = (sum(v[0] for v in below[b]), sum(v[1] for v in below[b]))
			vertical = abs(d[1]) >= abs(d[0])
			at = pos[a]
			best = None
			for s in steps:
				cell = (at[0] + s[0], at[1] + s[1])
				if not free(cell):
					continue
				toward = s[0] * d[0] + s[1] * d[1]
				off = abs(cell[0] - centre) if vertical else abs(cell[1] - middle)
				score = 10 * toward + (3 if s == last else 0) + room(cell) - (30 if toward < 0 else 0) - 0.8 * off + (0.5 if s == (0, 1) else 0)
				if best is None or score > best[0]:
					best = (score, cell, s)
			if best is None:
				break
			put(b, best[1])
			last = best[2]
		d = axis((sign(sum(v[0] for v in exit_dirs[exit_name])), sign(sum(v[1] for v in exit_dirs[exit_name]))))
		if exit_name in pos:
			cell = (pos[exit_name][0] + d[0], pos[exit_name][1] + d[1])
			while inside(cell):
				reserved.add(cell)
				cell = (cell[0] + d[0], cell[1] + d[1])

	order = [head]
	for name in order:
		order.extend(sorted(children[name], key=lambda c: -size[c]))

	long_links = []
	for name in order:
		up = parent[name]
		if name in pos or up not in pos:
			continue
		at = pos[up]
		best = None
		for group, bonus in ((steps, 100), (diagonals, 0)):
			for s in group:
				cell = (at[0] + s[0], at[1] + s[1])
				if not free(cell):
					continue
				outward = distance(cell, head_cell) - distance(at, head_cell)
				score = bonus + (2 * room(cell) if size[name] > 1 else -room(cell)) + 1.5 * outward - 0.5 * abs(cell[0] - centre)
				if best is None or score > best[0]:
					best = (score, cell)
		if best is None:
			queue, seen = [at], {at}
			while queue and best is None:
				cell = queue.pop(0)
				for s in steps:
					nxt = (cell[0] + s[0], cell[1] + s[1])
					if inside(nxt) and nxt not in seen:
						seen.add(nxt)
						if free(nxt):
							best = (0, nxt)
							break
						queue.append(nxt)
			long_links.append(name)
		if best is None:
			raise Exception(f"Milestones: no room for {name} in {m['Name']}")
		put(name, best[1])

	return pos, long_links

research_objects = objects_of(get_generated_files()["Generated/Researches/basic.json"])
research_by_name = {r["Name"]: r for r in research_objects}
item_names = {o["Name"] for data in get_generated_files().values() for o in objects_of(data) if o.get("Class", "").startswith("StaticItem")}
milestone_by_name = {m["Name"]: m for m in milestones}
stage_dicts = {o["Name"]: o for data in get_generated_files().values() for o in objects_of(data) if o.get("Class") == r_dict and o.get("Recipes")}
laboratory_tier ={machine["Name"]: machine["StartTier"] for machine in machines if machine.get("BlockLogic") == "ResearchLaboratoryBlockLogic"}

owner = {}
positions = {}
for m in milestones:
	position = tuple(m["Position"])
	if position in positions:
		raise Exception(f"Milestones: {m['Name']} and {positions[position]} share the cell {position}")
	positions[position] = m["Name"]

	built = "Build" in m
	heads = [name for name, up in m["Tree"] if not up]
	if len(heads) != (0 if built else 1):
		raise Exception(f"Milestones: {m['Name']} needs {'no head, it is built' if built else 'exactly one head'}, has {heads}")
	m["Head"] = heads[0] if heads else ""
	m["Researches"] = [name for name, _ in m["Tree"]]
	if built:
		stages = stage_dicts.get(m["Build"] + "Stage" + r_dict)
		if m["Build"] not in item_names or not stages:
			raise Exception(f"Milestones: {m['Name']} is built as {m['Build']}, which has no item or no stages")
		if m["Experiments"] != 1:
			raise Exception(f"Milestones: {m['Name']} is passed by one build, not {m['Experiments']}")
		bill = {}
		for stage in stages["Recipes"]:
			for need in stage["Input"]["Items"]:
				bill[need["Name"]] = bill.get(need["Name"], 0) + need["Count"]
		m["Experiment"] = [[name, count] for name, count in bill.items()]
		m["Stage"] = stages["Recipes"][-1]["Name"]
	for name, up in m["Tree"]:
		if name not in research_by_name:
			raise Exception(f"Milestones: {m['Name']} names an unknown research {name}")
		if up and up not in m["Researches"]:
			raise Exception(f"Milestones: {name} in {m['Name']} hangs on {up}, which is not in the milestone")
		if name in owner:
			raise Exception(f"Milestones: {name} is in both {owner[name]} and {m['Name']}")
		owner[name] = m["Name"]
		research_by_name[name]["Complexity"] *= m.get("CostMulOf", {}).get(name, m.get("CostMul", 1))
	for name in m.get("CostMulOf", {}):
		if name not in m["Researches"]:
			raise Exception(f"Milestones: CostMulOf of {m['Name']} names {name}, which is not in the milestone")
	if m["Label"] not in research_by_name:
		raise Exception(f"Milestones: {m['Name']} takes its label from an unknown research {m['Label']}")
	if m["Experiments"] and not built and m.get("Laboratory") not in laboratory_tier:
		raise Exception(f"Milestones: {m['Name']} runs its experiment in an unknown laboratory {m.get('Laboratory')}")

	for item, count in m["Experiment"]:
		if item not in item_names:
			raise Exception(f"Milestones: experiment of {m['Name']} names an unknown item {item}")
		if not isinstance(count, int) or count < 1:
			raise Exception(f"Milestones: experiment of {m['Name']} takes {count} of {item}, a pack holds whole items")
	if (m["Experiments"] > 0) != bool(m["Experiment"]):
		raise Exception(f"Milestones: {m['Name']} has {m['Experiments']} experiments of {m['Experiment']}")

entries = {m["Name"]: [] for m in milestones}
for m in milestones:
	for research, target in m["Exits"]:
		if research not in m["Researches"] and (research or m["Tree"]):
			raise Exception(f"Milestones: exit {research} of {m['Name']} is not one of its researches")
		if target not in milestone_by_name:
			raise Exception(f"Milestones: exit of {m['Name']} leads to an unknown milestone {target}")
		entries[target].append((m["Name"], research))

roots = [m["Name"] for m in milestones if not entries[m["Name"]]]
if len(roots) != 1:
	raise Exception(f"Milestones: the map needs one root, has {roots}")

boxes = {}
box_of = {}
chunk_heads = set()
for m in milestones:
	parent = {name: up for name, up in m["Tree"]}
	chunks = {name: tuple(d) for name, d in m.get("Chunks", {}).items()}
	for name in chunks:
		if not parent.get(name):
			raise Exception(f"Milestones: chunk {name} of {m['Name']} is not a research hanging in it")
	chunk_heads.update(chunks)

	def top(name):
		while name != m["Head"] and name not in chunks:
			name = parent[name]
		return name

	key_of = lambda head: m["Name"] if head == m["Head"] else m["Name"] + ":" + head
	for head in [m["Head"]] + list(chunks):
		boxes[key_of(head)] = {"Milestone": m["Name"], "Head": head, "Exits": [], "Tree": [[name, "" if name == head else up] for name, up in m["Tree"] if top(name) == head]}
	for name, _ in m["Tree"]:
		box_of[name] = key_of(top(name))
	for head, d in chunks.items():
		boxes[key_of(head)]["Entry"] = (box_of[parent[head]], parent[head], d)
		boxes[box_of[parent[head]]]["Exits"].append((parent[head], d))

def exit_box(milestone, research):
	return box_of[research] if research else milestone

for m in milestones:
	for research, target in m["Exits"]:
		boxes[exit_box(m["Name"], research)]["Exits"].append((research, direction(m["Name"], target)))
	if entries[m["Name"]]:
		source, research = entries[m["Name"]][0]
		boxes[m["Name"]]["Entry"] = (exit_box(source, research), research, axis(direction(source, m["Name"])))

cell_of = {}
origin_x = {}
card_of = {}
paths = {m["Name"]: [] for m in milestones}
node_at = {}
card_at = set()
line_at = set()
long_links = []

def fits(nodes, cards, line):
	for cell in nodes:
		if near(cell, node_at) or near(cell, card_at) or cell in line_at:
			return False
	for cell in cards:
		if near(cell, node_at) or near(cell, card_at) or cell in line_at:
			return False
	for cell in line:
		if cell in node_at or cell in card_at or cell in line_at or cell in nodes:
			return False
	return True

def exit_cell_of(source, research):
	return cell_of[research] if research else card_of[source]

def gap_column(source, e):
	x = origin_x[source]
	return x + cell_columns + gap_columns // 2 if e[0] > 0 else x - gap_columns // 2 - 1

queue = roots[:]
done = []
while queue:
	key = queue.pop(0)
	box = boxes[key]
	entry = box.get("Entry")
	if entry and entry[0] not in origin_x:
		queue.append(key)
		continue
	done.append(key)
	carded = key in milestone_by_name
	rows = milestone_by_name[key].get("Rows", tree_rows) if carded else tree_rows
	reach = card_step if carded else 0
	exit_dirs = {}
	for research, d in box["Exits"]:
		exit_dirs.setdefault(research, []).append(d)

	if entry:
		source, research, e = entry
		exit_cell = exit_cell_of(source, research)
		if e[0] == 0:
			head_local = (cell_columns // 2, 0 if e[1] > 0 else rows - 1)
			x0 = exit_cell[0] - head_local[0]
		else:
			head_local = (side_head[0] if e[0] > 0 else cell_columns - 1 - side_head[0], side_head[1])
			x0 = gap_column(source, e) + e[0] * reach - head_local[0]
	else:
		e = (0, 1)
		head_local = (cell_columns // 2, 0)
		x0 = milestone_by_name[key]["Position"][0] * column_pitch
	anchor_local = add(head_local, scale(e, -reach))
	reserved = through([anchor_local, head_local]) + [(x, head_local[1]) for x in range(cell_columns) if (x - head_local[0]) * e[0] < 0]
	if carded:
		reserved += [add(anchor_local, (dx, dy)) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
	local, missed = layout({"Name": key, "Tree": box["Tree"], "Head": box["Head"]}, cell_columns, rows, head_local, exit_dirs, reserved) if box["Tree"] else ({}, [])
	long_links += [f"{key}:{n}" for n in missed]

	for k in range(1000):
		if not entry:
			anchor = (x0 + head_local[0], k)
			points = []
		elif e[0] == 0:
			anchor = (x0 + head_local[0], exit_cell[1] + e[1] * (card_step + k))
			points = [exit_cell, anchor]
		else:
			anchor = (gap_column(source, e), exit_cell[1] + k)
			points = bends([exit_cell, (anchor[0], exit_cell[1]), anchor])
		head = add(anchor, scale(e, reach))
		nodes = {name: add(head, (cell[0] - head_local[0], cell[1] - head_local[1])) for name, cell in local.items()}
		cards = [anchor] if carded else []
		line = through(points) + (through([anchor, head]) if box["Tree"] else [])
		if fits(set(nodes.values()), cards, line):
			break
	else:
		raise Exception(f"Milestones: no room for {key}")

	cell_of.update(nodes)
	origin_x[key] = x0
	if carded:
		card_of[key] = anchor
	if points:
		paths[box["Milestone"]].append(points)
	node_at.update({cell: key for cell in nodes.values()})
	card_at.update(cards)
	line_at.update(line)
	for next_key, next_box in boxes.items():
		if next_box.get("Entry", (None,))[0] == key and next_key not in queue and next_key not in done:
			queue.append(next_key)

if len(done) != len(boxes):
	raise Exception(f"Milestones: not reachable from {roots[0]}: {[key for key in boxes if key not in done]}")

crossing = []
for m in milestones:
	for source, research in entries[m["Name"]][1:]:
		e = axis(direction(source, m["Name"]))
		exit_cell = exit_cell_of(source, research)
		card = card_of[m["Name"]]
		if e[0] == 0:
			points = bends([exit_cell, (exit_cell[0], card[1]), card])
		else:
			gx = gap_column(exit_box(source, research), e)
			points = bends([exit_cell, (gx, exit_cell[1]), (gx, card[1]), card])
		line = through(points)
		if any(cell in node_at or cell in card_at for cell in line):
			crossing.append(f"{source}->{m['Name']}")
		line_at.update(line)
		paths[m["Name"]].append(points)

lengths = sorted(((sum(abs(b[0] - a[0]) + abs(b[1] - a[1]) for a, b in zip(p, p[1:])), name) for name in paths for p in paths[name]), reverse=True)
outside = [r["Name"] for r in research_objects if r["Name"] not in owner]
diagonal = sum(1 for m in milestones for name, up in m["Tree"] if up and abs(cell_of[name][0] - cell_of[up][0]) == 1 and abs(cell_of[name][1] - cell_of[up][1]) == 1)
print(f"Milestones: {len(milestones)} milestones, {sum(len(m['Researches']) for m in milestones)} researches on the grid, {len(outside)} outside, {diagonal} diagonal links, long links {long_links}")
print(f"Milestones: lines into milestones {sum(n for n, _ in lengths)} cells, longest {lengths[:3]}, crossing {crossing}")

own_lines = sum(1 for m in milestones for name, up in m["Tree"] if up in (research_by_name[name].get("RequiredResearch") or []))
for m in milestones:
	for name, up in m["Tree"]:
		research_by_name[name]["RequiredResearch"] = [up] if up else []
print(f"Milestones: a research opens by its line, {own_lines} of {sum(len(m['Tree']) - 1 for m in milestones)} lines are its own requirement")

milestone_tier = {}
for name in (key for key in done if key in milestone_by_name):
	m = milestone_by_name[name]
	own = sorted(research_by_name[r]["Tier"] for r in m["Researches"])
	milestone_tier[name] = max(own[len(own) // 2:len(own) // 2 + 1] + [milestone_tier.get(source, 0) for source, _ in entries[name]])

def price(m, name, floor):
	research = research_by_name[name]
	tier = milestone_tier[m["Name"]]
	cost = max(floor, research["Complexity"])
	research["Tier"] = tier
	research["Complexity"] = cost
	for child, up in m["Tree"]:
		if up == name:
			price(m, child, cost)

for m in milestones:
	if m["Head"]:
		price(m, m["Head"], 0)
	for name in m["Researches"]:
		research_by_name[name]["Complexity"] = round(research_by_name[name]["Complexity"] * tier_cost_mul.get(milestone_tier[m["Name"]], 1))
print(f"Milestones: tiers {milestone_tier}")

objects = []
for m in milestones:
	built = "Build" in m
	objects.append({
		"Class": "StaticMilestone",
		"Name": m["Name"],
		"Label": [m["Title"], "researches"] if "Title" in m else research_by_name[m["Label"]]["Label"],
		"Icon": m["Label"],
		"Tier": milestone_tier[m["Name"]],
		"Position": m["Position"],
		"Head": m["Head"],
		"Researches": m["Researches"],
		"Layout": [[name, cell_of[name][0], cell_of[name][1], "" if name in chunk_heads else up] for name, up in m["Tree"]],
		"Card": list(card_of[m["Name"]]),
		"Paths": [[list(p) for p in points] for points in paths[m["Name"]]],
		"Exits": m["Exits"],
		"Experiments": m["Experiments"],
		"Experiment": m["Experiment"],
		"Recipe": [m["Build"] + "Stage" + r_dict, m["Stage"]] if built else [m["Laboratory"] + r_dict, m["Name"] + "Experiment"] if m["Experiments"] else [],
	})
	if "Image" in m:
		objects[-1]["Image"] = m["Image"]
	if built:
		objects[-1]["Build"] = m["Build"]
		del objects[-1]["Head"]

write_file("Generated/Researches/milestones.json", {"Objects": objects})

write_file("Generated/Recipes/laboratory.json", {"Objects": [{
	"Class": r_dict,
	"Name": laboratory + r_dict,
	"StartTier": 0,
	"UsedIn": [{"Item": tier_material[tier] + laboratory, "Tier": tier}],
	"Recipes": [{
		"Name": m["Name"] + "Experiment",
		"Input": items(m["Experiment"]),
		"Output": no_items(),
		"Ticks": experiment_ticks,
	} for m in milestones if m.get("Laboratory") == laboratory],
} for laboratory, tier in laboratory_tier.items()]})
