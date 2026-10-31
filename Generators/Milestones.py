from Common import *
from Materials import *

metal_milestones = {
	0: "Start",
	1: "Automation",
	2: "Steel",
	3: "Aluminium",
	4: "StainlessSteel",
	5: "Titanium",
	6: "Composite",
	7: "Fusion",
	8: "Infinite",
}

tier_cost_mul = {2: 0.6, 3: 0.4, 4: 1.4, 5: 2, 6: 3}

laboratory_r_dict = "ResearchLaboratory" + r_dict
experiment_ticks = 600

milestones = [
	{
		"Name": "Start",
		"Label": "MineralsScan",
		"Position": [1, 0],
		"Tree": [
			["MineralsScan", ""],
			["Smelting", "MineralsScan"],
			["Metalwork", "Smelting"],
			["Chest", "Smelting"],
			["Container", "Chest"],
			["SingleTypeStorage", "Chest"],
			["InventoryUpgrade", "Chest"],
			["BasicPlatform", "MineralsScan"],
			["Furnace", "PowerGeneration"],
			["Destroyer", "Furnace"],
			["PowerGeneration", "Metalwork"],
			["DistributedComputing", "PowerGeneration"],
			["CopperWire", "DistributedComputing"],
			["PowerTransmission", "CopperWire"],
			["Lamp", "Smelting"],
			["ResearchLaboratory", "CopperWire"],
		],
		"Exits": [["ResearchLaboratory", "Machines"]],
		"Experiments": 0,
		"Experiment": [],
	},
	{
		"Name": "Machines",
		"Label": "BasicMachines",
		"Position": [1, 1],
		"Tree": [
			["BasicMachines", ""],
			["Automatization", "BasicMachines"],
			["Conveyor", "Automatization"],
			["AutomaticMining", "Automatization"],
		],
		"Exits": [["AutomaticMining", "Automation"]],
		"Experiments": 10,
		"Experiment": [["CopperStirlingEngine", 1], ["Coal", 2]],
	},
	{
		"Name": "Automation",
		"Label": "Automatization",
		"Position": [1, 2],
		"Tree": [
			["Macerator", ""],
			["Splitter", "Macerator"],
			["Loader", "Splitter"],
			["ConstructionTool", "Loader"],
			["DeconstructionTool", "ConstructionTool"],
			["UpgradeTool", "DeconstructionTool"],
			["Constructor", "Macerator"],
			["AutomaticFarm", "Splitter"],
			["DrillingRigProductivity", "AutomaticFarm"],
			["Bricks", "Constructor"],
			["DecorativeWood", "Designable"],
			["Door", "DecorativeWood"],
			["Designable", "Bricks"],
			["Sign", "Constructor"],
			["StoneTiles", "Bricks"],
			["RedTiles", "StoneTiles"],
			["DarkTiles", "RedTiles"],
			["RedBricks", "Bricks"],
			["DarkBricks", "RedBricks"],
			["MetalBlocks", "DarkBricks"],
		],
		"Exits": [["Loader", "Steel"], ["AutomaticFarm", "Pipes"], ["Sign", "Circuit"]],
		"Experiments": 10,
		"Experiment": [["CopperConveyor", 1], ["CopperRobotArm", 1]],
	},
	{
		"Name": "Pipes",
		"Label": "FluidTransfer",
		"Position": [2, 2],
		"Tree": [
			["FluidTransfer", ""],
			["Pump", "FluidTransfer"],
			["AtmosphericCondenser", "Pump"],
			["Valve", "FluidTransfer"],
			["Steampack", "Valve"],
			["HighCapacitySteampack", "Steampack"],
			["HighPressureSteampack", "HighCapacitySteampack"],
			["HeatTransferring", "FluidTransfer"],
			["KineticHeater", "HeatTransferring"],
			["FluidFurnace", "HeatTransferring"],
			["Terracotta", "KineticHeater"],
			["TerracottaTiles", "Terracotta"],
			["TerracottaBricks", "TerracottaTiles"],
			["DecorativePaint", "Pump"],
		],
		"Exits": [["Pump", "Steam"]],
		"Experiments": 20,
		"Experiment": [["CopperPlate", 2], ["BuildingMaterial", 1]],
	},
	{
		"Name": "Circuit",
		"Label": "Circuit",
		"Position": [0, 2],
		"Tree": [
			["CircuitBoard", ""],
			["Triod", "CircuitBoard"],
			["Circuit", "Triod"],
			["Circuit2", "Circuit"],
			["LogicNetworking", "Circuit"],
			["LogicDevices", "LogicNetworking"],
			["AdvancedSign", "LogicDevices"],
			["WireCover", "CircuitBoard"],
			["Spotlight", "Circuit"],
			["Flashlight", "Spotlight"],
			["GlassBlock", "Spotlight"],
		],
		"Exits": [["Circuit", "Transistor"]],
		"Experiments": 10,
		"Experiment": [["CopperWire", 5], ["Glass", 3], ["CopperPlate", 4]],
	},
	{
		"Name": "Steel",
		"Label": "SteelProduction",
		"Position": [1, 3],
		"Tree": [
			["Oven", ""],
			["SteelProduction", "Oven"],
			["AdvancedSmelting", "SteelProduction"],
			["ElectricFurnace", "AdvancedSmelting"],
			["BasicFrame", "SteelProduction"],
			["Sorter", "Oven"],
			["Railway", "BasicFrame"],
			["RailSignals", "Railway"],
			["Concrete", "BasicFrame"],
			["ConcreteBricks", "ConcreteTiles"],
			["ConcreteTiles", "Concrete"],
			["ConcreteSmallTiles", "ConcreteTiles"],
			["Roadwork", "Concrete"],
			["MetalDoors", "BasicFrame"],
			["Designable2", "Concrete"],
		],
		"Exits": [["AdvancedSmelting", "Aluminium"], ["SteelProduction", "Steam"]],
		"Experiments": 25,
		"Experiment": [["Triod", 1], ["CopperPipe", 2], ["CopperConveyor", 1]],
	},
	{
		"Name": "Steam",
		"Label": "SteamEngine",
		"Position": [2, 3],
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
		],
		"Exits": [["ElectricEngine", "Chemistry"]],
		"Experiments": 25,
		"Experiment": [["CopperPump", 1], ["SteelPipe", 1]],
	},
	{
		"Name": "Transistor",
		"Label": "Processor",
		"Position": [0, 3],
		"Tree": [
			["Resistor", ""],
			["Resistor2", "Resistor"],
			["AdvancedCircuit", "Resistor"],
			["NightVision", "AdvancedCircuit"],
			["CircuitBoard2", "AdvancedCircuit"],
			["Transistor", "AdvancedCircuit"],
			["Transistor2", "Transistor"],
			["Assembler", "Processor"],
			["Processor", "Transistor"],
			["Capacitor", "Assembler"],
			["Capacitor2", "Capacitor"],
			["InterchangeableParts", "Assembler"],
			["BeltDrive", "InterchangeableParts"],
		],
		"Exits": [["Processor", "Silicon"]],
		"Experiments": 25,
		"Experiment": [["Circuit", 4], ["CopperWire", 4]],
	},
	{
		"Name": "Aluminium",
		"Label": "AluminiumProduction",
		"Position": [1, 4],
		"Tree": [
			["Electrolyzer", ""],
			["AluminiumReduction", "Electrolyzer"],
			["AluminiumProduction", "AluminiumReduction"],
			["ReinforcedFrame", "AluminiumProduction"],
			["Boat", "ThreePhaseCurrent"],
			["OffroadVehicle", "Boat"],
			["Jetpack", "Boat"],
			["OreWasher", "Separator"],
			["Separator", "Electrolyzer"],
			["Sifter", "ThreePhaseCurrent"],
			["ReinforcedConcrete", "ReinforcedFrame"],
			["ReinforcedConcreteTiles", "ReinforcedConcrete"],
			["ReinforcedConcreteSmallTiles", "ReinforcedConcreteTiles"],
			["ReinforcedConcreteBricks", "ReinforcedConcreteTiles"],
			["DangerBlock", "ReinforcedConcrete"],
			["DecorativeWood3", "ReinforcedFrame"],
			["Designable3", "DecorativeWood3"],
			["DecorativeWood4", "Designable3"],
			["ThreePhaseCurrent", "AluminiumProduction"],
			["BallBearings", "AluminiumProduction"],
			["AssemblyLine", "BallBearings"],
			["RotaryDrilling", "AssemblyLine"],
			["DieCasting", "ReinforcedFrame"],
		],
		"Exits": [["AluminiumProduction", "StainlessSteel"]],
		"Experiments": 50,
		"Experiment": [["SteelRail", 1], ["Coke", 2]],
	},
	{
		"Name": "Chemistry",
		"Label": "IndustrialChemReactor",
		"Position": [2, 4],
		"Tree": [
			["IndustrialChemReactor", ""],
			["Catalyst", "IndustrialChemReactor"],
			["Catalyst2", "SulfuricAcid"],
			["Polyethylene", "Catalyst"],
			["ChemicalBath", "IndustrialChemReactor"],
			["Sulfur", "ChemicalBath"],
			["SulfuricAcid", "Catalyst"],
			["Battery", "SulfuricAcid"],
			["BatteryBox", "Battery"],
			["Fermentation", "IndustrialChemReactor"],
			["CentrifugalPump", "Fermentation"],
			["WaterTubeBoiler", "IndustrialChemReactor"],
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
		"Position": [0, 5],
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
		"Position": [1, 5],
		"Tree": [
			["Mixer", ""],
			["AdvancedAlloys", "Mixer"],
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
			["SpotWelding", "CementedCarbide"],
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
		"Position": [2, 5],
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
		"Position": [0, 7],
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
		"Position": [1, 6],
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
		"Position": [1, 7],
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
		"Position": [2, 6],
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
		"Position": [1, 8],
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
		"Position": [1, 9],
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
cell_pitch = 132
tree_top = 130
tree_bottom = 966
tree_rows = (tree_bottom - tree_top) // cell_pitch

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

def face_cell(d, along, rows):
	col = along if d[0] == 0 else (cell_columns - 1 if d[0] > 0 else 0)
	row = along if d[1] == 0 else (rows - 1 if d[1] > 0 else 0)
	return (max(0, min(cell_columns - 1, col)), max(0, min(rows - 1, row)))

def layout(m, rows, head_cell, exit_dirs, entry_corridor):
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

	inside = lambda c: 0 <= c[0] < cell_columns and 0 <= c[1] < rows
	pos = {head: head_cell}
	taken = {head_cell: head}
	reserved = set(entry_corridor)

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

	centre = (cell_columns - 1) / 2
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
				axis = abs(cell[0] - centre) if vertical else abs(cell[1] - middle)
				score = 10 * toward + (3 if s == last else 0) + room(cell) - (30 if toward < 0 else 0) - 0.8 * axis + (0.5 if s == (0, 1) else 0)
				if best is None or score > best[0]:
					best = (score, cell, s)
			if best is None:
				break
			put(b, best[1])
			last = best[2]
		d = (sign(sum(v[0] for v in exit_dirs[exit_name])), sign(sum(v[1] for v in exit_dirs[exit_name])))
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

owner = {}
positions = {}
for m in milestones:
	position = tuple(m["Position"])
	if position in positions:
		raise Exception(f"Milestones: {m['Name']} and {positions[position]} share the cell {position}")
	positions[position] = m["Name"]

	heads = [name for name, up in m["Tree"] if not up]
	if len(heads) != 1:
		raise Exception(f"Milestones: {m['Name']} needs exactly one head, has {heads}")
	m["Head"] = heads[0]
	m["Researches"] = [name for name, _ in m["Tree"]]
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
		if research not in m["Researches"]:
			raise Exception(f"Milestones: exit {research} of {m['Name']} is not one of its researches")
		if target not in milestone_by_name:
			raise Exception(f"Milestones: exit of {m['Name']} leads to an unknown milestone {target}")
		d = direction(m["Name"], target)
		span = max(abs(milestone_by_name[target]["Position"][0] - m["Position"][0]), abs(milestone_by_name[target]["Position"][1] - m["Position"][1]))
		between = [(m["Position"][0] + d[0] * k, m["Position"][1] + d[1] * k) for k in range(1, span)]
		if d == (0, 0) or (span > 1 and (0 not in d or any(cell in positions for cell in between))):
			raise Exception(f"Milestones: {m['Name']} and {target} are neither neighbours on the grid nor joined straight over empty cells")
		entries[target].append((m["Name"], research))

roots = [m["Name"] for m in milestones if not entries[m["Name"]]]
if len(roots) != 1:
	raise Exception(f"Milestones: the map needs one root, has {roots}")

cells = {}
rows_of = {}
long_links = []
queue = roots[:]
done = []
while queue:
	name = queue.pop(0)
	m = milestone_by_name[name]
	if any(source not in cells for source, _ in entries[name][:1]):
		queue.append(name)
		continue
	done.append(name)
	exit_dirs = {}
	for research, target in m["Exits"]:
		exit_dirs.setdefault(research, []).append(direction(name, target))
	rows = tree_rows
	if entries[name]:
		source, research = entries[name][0]
		d = direction(name, source)
		source_cell = cells[source][research]
		entry_corridor = []
		if d[0] == 0:
			head_cell = face_cell(d, source_cell[0], rows)
		else:
			head_cell = (cell_columns // 2, max(0, min(rows - 1, source_cell[1])))
			face = face_cell(d, head_cell[1], rows)
			entry_corridor = [(x, head_cell[1]) for x in range(min(face[0], head_cell[0]), max(face[0], head_cell[0]) + 1) if x != head_cell[0]]
	else:
		head_cell = (cell_columns // 2, 0)
		entry_corridor = []
	pos, missed = layout(m, rows, head_cell, exit_dirs, entry_corridor)
	cells[name] = pos
	rows_of[name] = rows
	long_links += [f"{name}:{n}" for n in missed]
	for research, target in m["Exits"]:
		if target not in queue and target not in done:
			queue.append(target)

if len(done) != len(milestones):
	raise Exception(f"Milestones: not reachable from {roots[0]}: {[m['Name'] for m in milestones if m['Name'] not in done]}")

outside = [r["Name"] for r in research_objects if r["Name"] not in owner]
diagonal = sum(1 for m in milestones for name, up in m["Tree"] if up and abs(cells[m["Name"]][name][0] - cells[m["Name"]][up][0]) == 1 and abs(cells[m["Name"]][name][1] - cells[m["Name"]][up][1]) == 1)
print(f"Milestones: {len(milestones)} milestones, {sum(len(m['Researches']) for m in milestones)} researches on the grid, {len(outside)} outside, {diagonal} diagonal links, long links {long_links}")

metal_rows = [milestone_by_name[metal_milestones[tier]]["Position"][1] for tier in sorted(metal_milestones)]
if any(a >= b for a, b in zip(metal_rows, metal_rows[1:])):
	raise Exception(f"Milestones: metal milestones must go down a row per tier, rows {metal_rows}")
last_row = max(m["Position"][1] for m in milestones)
epochs = []
for stage in sorted((r for r in research_objects if r["Class"] == "StaticResearchMilestone"), key=lambda r: r["Tier"]):
	tier = stage["Tier"]
	if tier not in metal_milestones:
		raise Exception(f"Milestones: epoch {stage['Name']} has tier {tier}, which has no metal milestone")
	epochs.append((stage["Name"], metal_rows[tier + 1] - 1 if tier + 1 < len(metal_rows) else last_row))
print(f"Milestones: epochs below rows {[row for _, row in epochs]}")

own_lines = sum(1 for m in milestones for name, up in m["Tree"] if up in (research_by_name[name].get("RequiredResearch") or []))
for m in milestones:
	for name, up in m["Tree"]:
		research_by_name[name]["RequiredResearch"] = [up] if up else []
print(f"Milestones: a research opens by its line, {own_lines} of {sum(len(m['Tree']) - 1 for m in milestones)} lines are its own requirement")

milestone_tier = {m["Name"]: sum(1 for _, row in epochs if row < m["Position"][1]) for m in milestones}
for name in owner:
	research_by_name[name]["Complexity"] = round(research_by_name[name]["Complexity"] * tier_cost_mul.get(milestone_tier[owner[name]], 1))

objects = []
for name, row in epochs:
	objects.append({
		"Class": "StaticEpoch",
		"Name": "Epoch" + name,
		"Research": name,
		"Row": row,
	})
for m in milestones:
	objects.append({
		"Class": "StaticMilestone",
		"Name": m["Name"],
		"Label": research_by_name[m["Label"]]["Label"],
		"Position": m["Position"],
		"Head": m["Head"],
		"Researches": m["Researches"],
		"Layout": [[name, cells[m["Name"]][name][0], cells[m["Name"]][name][1], up] for name, up in m["Tree"]],
		"Rows": rows_of[m["Name"]],
		"Exits": m["Exits"],
		"Experiments": m["Experiments"],
		"Experiment": m["Experiment"],
		"Recipe": [laboratory_r_dict, m["Name"] + "Experiment"] if m["Experiments"] else [],
	})

write_file("Generated/Researches/milestones.json", {"Objects": objects})

write_file("Generated/Recipes/laboratory.json", {"Objects": [{
	"Class": r_dict,
	"Name": laboratory_r_dict,
	"StartTier": 0,
	"UsedIn": [{"Item": tier_material[tier] + "ResearchLaboratory", "Tier": tier} for tier in range(1, 8)],
	"Recipes": [{
		"Name": m["Name"] + "Experiment",
		"Input": items(m["Experiment"]),
		"Output": no_items(),
		"Ticks": experiment_ticks,
	} for m in milestones if m["Experiments"]],
}]})
