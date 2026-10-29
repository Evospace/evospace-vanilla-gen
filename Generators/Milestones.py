from Common import *

milestones = [
	{
		"Name": "Copper",
		"Label": "Smelting",
		"Position": [1, 0],
		"Tree": [
			["MineralsScan", ""],
			["Smelting", "MineralsScan"],
			["Metalwork", "Smelting"],
			["Furnace", "Smelting"],
			["Destroyer", "Furnace"],
			["Lamp", "Smelting"],
			["Sign", "Lamp"],
			["Chest", "MineralsScan"],
			["InventoryUpgrade", "Chest"],
			["Container", "Chest"],
			["SingleTypeStorage", "Container"],
		],
		"Exits": [["Lamp", "Electricity"], ["Metalwork", "Automation"]],
		"Experiment": [],
	},
	{
		"Name": "Electricity",
		"Label": "Electricity",
		"Position": [0, 0],
		"Tree": [
			["Electricity", ""],
			["PowerGeneration", "Electricity"],
			["PowerTransmission", "PowerGeneration"],
			["DistributedComputing", "PowerGeneration"],
			["CopperWire", "DistributedComputing"],
		],
		"Exits": [["CopperWire", "Circuit"]],
		"Experiment": [["CopperParts", 30], ["CopperPlate", 20]],
	},
	{
		"Name": "Automation",
		"Label": "Automatization",
		"Position": [1, 1],
		"Tree": [
			["BasicMachines", ""],
			["Automatization", "BasicMachines"],
			["Loader", "Automatization"],
			["Sorter", "Loader"],
			["ConstructionTool", "Automatization"],
			["DeconstructionTool", "ConstructionTool"],
			["UpgradeTool", "ConstructionTool"],
			["Constructor", "BasicMachines"],
			["AutomaticMining", "BasicMachines"],
			["DrillingRigProductivity", "AutomaticMining"],
			["AutomaticFarm", "AutomaticMining"],
		],
		"Exits": [["Automatization", "Steel"], ["AutomaticFarm", "Pipes"]],
		"Experiment": [["CopperParts", 40], ["IronPlate", 20]],
	},
	{
		"Name": "Pipes",
		"Label": "FluidTransfer",
		"Position": [2, 1],
		"Tree": [
			["FluidTransfer", ""],
			["Pump", "FluidTransfer"],
			["AtmosphericCondenser", "Pump"],
			["Valve", "FluidTransfer"],
			["Steampack", "Valve"],
			["HighCapacitySteampack", "Steampack"],
			["HighPressureSteampack", "Steampack"],
			["HeatTransferring", "FluidTransfer"],
			["KineticHeater", "HeatTransferring"],
			["FluidFurnace", "HeatTransferring"],
		],
		"Exits": [["Pump", "Steam"]],
		"Experiment": [["CopperPlate", 40], ["BuildingMaterial", 20]],
	},
	{
		"Name": "Circuit",
		"Label": "Circuit",
		"Position": [0, 1],
		"Tree": [
			["CircuitBoard", ""],
			["Triod", "CircuitBoard"],
			["Circuit", "Triod"],
			["Circuit2", "Circuit"],
			["LogicNetworking", "Circuit"],
			["LogicDevices", "LogicNetworking"],
			["AdvancedSign", "LogicDevices"],
			["Spotlight", "LogicNetworking"],
			["Flashlight", "Spotlight"],
		],
		"Exits": [["Circuit", "Transistor"]],
		"Experiment": [["CopperWire", 50], ["CopperParts", 20]],
	},
	{
		"Name": "Steel",
		"Label": "SteelProduction",
		"Position": [1, 2],
		"Tree": [
			["Oven", ""],
			["SteelProduction", "Oven"],
			["AdvancedSmelting", "SteelProduction"],
			["ElectricFurnace", "AdvancedSmelting"],
			["BasicFrame", "SteelProduction"],
			["Railway", "BasicFrame"],
			["RailSignals", "Railway"],
		],
		"Exits": [["AdvancedSmelting", "Aluminium"], ["SteelProduction", "Steam"]],
		"Experiment": [["IronDust", 100], ["CopperParts", 50]],
	},
	{
		"Name": "Steam",
		"Label": "SteamEngine",
		"Position": [2, 2],
		"Tree": [
			["Boiler", ""],
			["SteamEngine", "Boiler"],
			["Flywheel", "SteamEngine"],
			["Generator", "SteamEngine"],
			["SteamTurbine", "Generator"],
			["ElectricEngine", "Generator"],
			["BasicCoil", "ElectricEngine"],
			["WindTurbine", "BasicCoil"],
			["ElectricalSwitch", "Generator"],
			["Diode", "ElectricalSwitch"],
			["SmallSolarPanel", "Diode"],
			["SolarPanel", "SmallSolarPanel"],
			["Dynamo", "SteamTurbine"],
			["RegenerativeFurnace", "Boiler"],
			["SheetRolling", "RegenerativeFurnace"],
		],
		"Exits": [["ElectricEngine", "Chemistry"]],
		"Experiment": [["SteelParts", 50], ["SteelPipe", 20]],
	},
	{
		"Name": "Transistor",
		"Label": "Processor",
		"Position": [0, 2],
		"Tree": [
			["Resistor", ""],
			["Resistor2", "Resistor"],
			["AdvancedCircuit", "Resistor"],
			["NightVision", "AdvancedCircuit"],
			["CircuitBoard2", "AdvancedCircuit"],
			["Transistor", "AdvancedCircuit"],
			["Transistor2", "Transistor"],
			["Assembler", "Transistor"],
			["Processor", "Transistor"],
			["Capacitor", "Processor"],
			["Capacitor2", "Capacitor"],
			["InterchangeableParts", "Assembler"],
			["BeltDrive", "InterchangeableParts"],
		],
		"Exits": [["Processor", "Silicon"]],
		"Experiment": [["Circuit", 100], ["CopperWire", 100]],
	},
	{
		"Name": "Aluminium",
		"Label": "AluminiumProduction",
		"Position": [1, 3],
		"Tree": [
			["Electrolyzer", ""],
			["AluminiumReduction", "Electrolyzer"],
			["AluminiumProduction", "AluminiumReduction"],
			["ReinforcedFrame", "AluminiumProduction"],
			["Boat", "ReinforcedFrame"],
			["OffroadVehicle", "ReinforcedFrame"],
			["Jetpack", "AluminiumProduction"],
			["OreWasher", "Electrolyzer"],
			["Separator", "OreWasher"],
			["Sifter", "Separator"],
		],
		"Exits": [["AluminiumProduction", "StainlessSteel"]],
		"Experiment": [["BauxiteDust", 100], ["SteelParts", 50]],
	},
	{
		"Name": "Chemistry",
		"Label": "IndustrialChemReactor",
		"Position": [2, 3],
		"Tree": [
			["IndustrialChemReactor", ""],
			["Catalyst", "IndustrialChemReactor"],
			["Catalyst2", "Catalyst"],
			["Polyethylene", "Catalyst"],
			["ChemicalBath", "IndustrialChemReactor"],
			["Sulfur", "ChemicalBath"],
			["SulfuricAcid", "Sulfur"],
			["Battery", "SulfuricAcid"],
			["BatteryBox", "Battery"],
			["Fermentation", "IndustrialChemReactor"],
			["CentrifugalPump", "Fermentation"],
			["WaterTubeBoiler", "IndustrialChemReactor"],
			["MagnesiteRefractories", "WaterTubeBoiler"],
		],
		"Exits": [["Catalyst", "Oil"]],
		"Experiment": [["Sulfur", 100], ["SteelElectricEngine", 10]],
	},
	{
		"Name": "Silicon",
		"Label": "QuantumCircuit",
		"Position": [0, 3],
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
			["ThreePhaseCurrent", "Processor2"],
			["BallBearings", "Processor2"],
			["AssemblyLine", "BallBearings"],
			["DieCasting", "DeepStorage"],
		],
		"Exits": [["QuantumProcessor", "QuantumBrain"]],
		"Experiment": [["Processor", 50], ["AdvancedCircuit", 100]],
	},
	{
		"Name": "StainlessSteel",
		"Label": "StainlessSteelProduction",
		"Position": [1, 4],
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
		],
		"Exits": [["IndustrialSmelting", "Titanium"]],
		"Experiment": [["ChromiumDust", 100], ["AluminiumParts", 50]],
	},
	{
		"Name": "Oil",
		"Label": "FuelChemistry",
		"Position": [2, 4],
		"Tree": [
			["PyrolysisUnit", ""],
			["PreciseTemperaturePyrolysis", "PyrolysisUnit"],
			["FuelChemistry", "PreciseTemperaturePyrolysis"],
			["FuelChemistry2", "FuelChemistry"],
			["FuelChemistry3", "FuelChemistry2"],
			["FractionatingColumn", "FuelChemistry"],
			["CombustionEngine", "FuelChemistry"],
			["Pumpjack", "PyrolysisUnit"],
			["PumpjackProductivity", "Pumpjack"],
			["InductionMelting", "PyrolysisUnit"],
			["Passivation", "FractionatingColumn"],
			["SuperheatedSteam", "FuelChemistry2"],
			["ElectricalSteel", "CombustionEngine"],
		],
		"Exits": [["PreciseTemperaturePyrolysis", "Composite"]],
		"Experiment": [["Coal", 200], ["SteelPipe", 50]],
	},
	{
		"Name": "QuantumBrain",
		"Label": "QuantumBrain",
		"Position": [0, 4],
		"Tree": [
			["BrainMatrix", ""],
			["QuantumBrain", "BrainMatrix"],
			["QuantumBrain2", "QuantumBrain"],
			["AntigravityUnit", "QuantumBrain"],
			["DopedSiliconWafer", "BrainMatrix"],
			["Processor3", "DopedSiliconWafer"],
			["Transistor4", "DopedSiliconWafer"],
			["DecisionResonator3", "BrainMatrix"],
			["DecisionResonator4", "DecisionResonator3"],
			["SeleniumPhotocell", "Transistor4"],
			["CementedCarbide", "BrainMatrix"],
			["SpotWelding", "CementedCarbide"],
			["Hydraulics", "AntigravityUnit"],
		],
		"Exits": [],
		"Experiment": [["QuantumProcessor", 20], ["QuantumCircuit", 50]],
	},
	{
		"Name": "Titanium",
		"Label": "TitaniumProduction",
		"Position": [1, 5],
		"Tree": [
			["NitricAcid", ""],
			["KrollProcess", "NitricAcid"],
			["TitaniumProduction", "KrollProcess"],
			["FastSifting", "TitaniumProduction"],
			["PowerCoil", "TitaniumProduction"],
			["BigMonitor", "TitaniumProduction"],
			["PlatinumSolution", "NitricAcid"],
			["CircuitBoard3", "PlatinumSolution"],
			["CrudeTantalum", "NitricAcid"],
			["Capacitor4", "CrudeTantalum"],
			["Resistor4", "CrudeTantalum"],
		],
		"Exits": [["TitaniumProduction", "Fusion"], ["FastSifting", "Nuclear"]],
		"Experiment": [["TitaniumOxideDust", 100], ["ModularFrame", 20]],
	},
	{
		"Name": "Composite",
		"Label": "CompositePlate",
		"Position": [2, 5],
		"Tree": [
			["CarbonFiber", ""],
			["CarbonFiberSheet", "CarbonFiber"],
			["CompositePlate", "CarbonFiberSheet"],
			["PlatinumReflector", "CompositePlate"],
			["HugeMonitor", "CompositePlate"],
			["CatalyticCracking", "CarbonFiber"],
			["FilamentWinding", "CatalyticCracking"],
			["Anodizing", "CarbonFiberSheet"],
			["AutoclaveMolding", "Anodizing"],
			["NumericalControl", "CompositePlate"],
			["LaserCutting", "NumericalControl"],
			["IndustrialRobots", "HugeMonitor"],
			["MachineVision", "IndustrialRobots"],
			["SiliconSolarCell", "PlatinumReflector"],
			["ThinFilmCells", "SiliconSolarCell"],
		],
		"Exits": [],
		"Experiment": [["PolyethyleneSheet", 100], ["Coke", 100]],
	},
	{
		"Name": "Nuclear",
		"Label": "FissionReactor",
		"Position": [0, 5],
		"Tree": [
			["UraniumCell", ""],
			["FissionReactor", "UraniumCell"],
			["ControlCell", "FissionReactor"],
			["ReflectorCell", "ControlCell"],
			["AdvancedReflection", "ReflectorCell"],
			["ThoriumReaction", "AdvancedReflection"],
			["PlutoniumReaction", "ThoriumReaction"],
			["PlutoniumReaction2", "PlutoniumReaction"],
			["Riteg", "ThoriumReaction"],
			["IndustrialBoiler", "FissionReactor"],
			["IndustrialSteamTurbine", "IndustrialBoiler"],
			["IndustrialGenerator", "IndustrialSteamTurbine"],
			["Superalloys", "IndustrialBoiler"],
			["SupercriticalSteam", "Superalloys"],
			["Turbocharging", "IndustrialGenerator"],
			["PowerElectronics", "Turbocharging"],
			["VacuumArcRemelting", "FissionReactor"],
			["PlasmaSpraying", "VacuumArcRemelting"],
		],
		"Exits": [],
		"Experiment": [["UraniumDust", 200], ["TitaniumParts", 50]],
	},
	{
		"Name": "Fusion",
		"Label": "FusionReaction",
		"Position": [1, 6],
		"Tree": [
			["FusionReactor", ""],
			["Rocket", "FusionReactor"],
			["FusionReaction", "FusionReactor"],
			["CompositePlate2", "FusionReaction"],
			["NeutroniumProduction", "FusionReaction"],
			["NeutroniumProduction2", "NeutroniumProduction"],
			["UltimateCatalyst", "NeutroniumProduction"],
			["FuelChemistry4", "UltimateCatalyst"],
			["Portal", "UltimateCatalyst"],
			["LevitationMelting", "NeutroniumProduction"],
			["DegenerateMatter", "NeutroniumProduction"],
			["Magnetohydrodynamics", "FusionReaction"],
			["Superconductivity", "FusionReactor"],
			["MagneticLevitation", "Rocket"],
			["MolecularAssembly", "UltimateCatalyst"],
			["NeutroniumLining", "NeutroniumProduction2"],
			["QuantumDots", "CompositePlate2"],
		],
		"Exits": [],
		"Experiment": [["TitaniumPlate", 100], ["ModularFrame", 50]],
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
	if m["Label"] not in research_by_name:
		raise Exception(f"Milestones: {m['Name']} takes its label from an unknown research {m['Label']}")

	for item, count in m["Experiment"]:
		if item not in item_names:
			raise Exception(f"Milestones: experiment of {m['Name']} names an unknown item {item}")

entries = {m["Name"]: [] for m in milestones}
for m in milestones:
	for research, target in m["Exits"]:
		if research not in m["Researches"]:
			raise Exception(f"Milestones: exit {research} of {m['Name']} is not one of its researches")
		if target not in milestone_by_name:
			raise Exception(f"Milestones: exit of {m['Name']} leads to an unknown milestone {target}")
		d = direction(m["Name"], target)
		if abs(milestone_by_name[target]["Position"][0] - m["Position"][0]) > 1 or abs(milestone_by_name[target]["Position"][1] - m["Position"][1]) > 1 or d == (0, 0):
			raise Exception(f"Milestones: {m['Name']} and {target} are not neighbours on the grid")
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

objects = []
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
		"Experiment": m["Experiment"],
	})

write_file("Generated/Researches/milestones.json", {"Objects": objects})
