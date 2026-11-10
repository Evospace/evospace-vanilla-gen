from Common import *
from Materials import *
from MachinesList import machines

tier_cost_mul = {1: 0.88, 2: 0.44, 3: 0.32, 4: 1.32, 5: 0.35, 6: 0.52, 7: 0.21, 8: 0.63}

experiment_ticks = 600

mass_packs = [
	[["CopperWire", 8], ["CopperPlate", 4]],
	[["CopperWire", 8], ["SteelPlate", 4]],
	[["CopperWire", 10], ["BasicFrame", 1], ["AluminiumPlate", 1]],
	[["CopperWire", 20], ["BasicFrame", 1], ["AluminiumPlate", 2], ["Processor", 1]],
	[["CopperWire", 20], ["BasicFrame", 1], ["AluminiumPlate", 2], ["Processor", 2]],
	[["CopperWire", 20], ["ReinforcedFrame", 1], ["Processor", 2]],
	[["CopperWire", 40], ["ReinforcedFrame", 1], ["Processor", 3]],
]
pipe_packs = [[["AluminiumPipe" if item == "AluminiumPlate" else item, count] for item, count in pack] for pack in mass_packs]

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
			["PowerGeneration", "Metalwork"],
			["Furnace", "PowerGeneration"],
			["Destroyer", "Furnace"],
			["Oven", "Furnace"],
			["ResearchLaboratory", "Oven"],
			["DistributedComputing", "PowerGeneration"],
			["CopperWire", "PowerGeneration"],
			["PowerTransmission", "CopperWire"],
			["CircuitBoard", "CopperWire"],
			["WireCover", "CircuitBoard"],
			["Triod", "CircuitBoard"],
			["Circuit", "Triod"],
			["Radio", "Circuit"],
			["CopperLamp", "Triod"],
			["GlassBlock", "Circuit"],
			["Constructor", "Circuit"],
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
			["FluidTransfer", "Splitter"],
			["Pump", "FluidTransfer"],
			["AutomaticFarm", "Pump"],
			["AtmosphericCondenser", "Pump"],
			["DecorativePaint", "Pump"],
			["Valve", "FluidTransfer"],
			["Steampack", "Valve"],
			["HeatTransferring", "FluidTransfer"],
			["KineticHeater", "HeatTransferring"],
			["FluidFurnace", "HeatTransferring"],
		],
		"Exits": [["Constructor", "Transistor"], ["ResearchLaboratory", "CopperPortal"], ["AutomaticFarm", "DrillingRigProductivity"]],
		"Experiments": 0,
		"Experiment": [],
	},
	{
		"Name": "Steel",
		"Label": "SteelProduction",
		"Position": [1, 2],
		"Tree": [
			["SteelProduction", ""],
			["SteelAutomaticHammer", "SteelProduction"],
			["SteelMacerator", "SteelAutomaticHammer"],
			["Separator", "SteelMacerator"],
			["OreWasher", "Separator"],
			["Mixer", "OreWasher"],
			["FuelBriquette", "Mixer"],
			["SteelConstructor", "SteelAutomaticHammer"],
			["BasicFrame", "SteelConstructor"],
			["SteelItemRack", "SteelConstructor"],
			["SteelChest", "SteelItemRack"],
			["SteelContainer", "SteelChest"],
			["InventoryUpgrade2", "SteelChest"],
			["SteelDestroyer", "SteelItemRack"],
			["SteelConveyor", "SteelProduction"],
			["SteelSplitter", "SteelConveyor"],
			["Sorter", "SteelSplitter"],
			["SteelRobotArm", "SteelConveyor"],
			["SteelDrillingRig", "SteelRobotArm"],
			["SteelAutomaticFarm", "SteelDrillingRig"],
			["Railway", "BasicFrame"],
			["RailSignals", "Railway"],
			["Concrete", "BasicFrame"],
			["ConcreteBricks", "ConcreteTiles"],
			["ConcreteTiles", "Concrete"],
			["ConcreteSmallTiles", "ConcreteTiles"],
			["Roadwork", "Concrete"],
			["MetalDoors", "BasicFrame"],
			["Designable2", "MetalDoors"],
			["SteelBlock", "Designable2"],
			["SteelSign", "SteelBlock"],
			["LogicNetworking", "SteelConstructor"],
			["Led", "LogicNetworking"],
			["AdvancedSign", "Led"],
			["Speaker", "Led"],
			["SteelButton", "LogicNetworking"],
			["SteelToggleButton", "SteelButton"],
			["SteelPressurePlate", "SteelToggleButton"],
			["LogicTransceiver", "LogicNetworking"],
			["HighCapacitySteampack", "SteelRobotArm"],
			["HighPressureSteampack", "HighCapacitySteampack"],
		],
		"Rows": 7,
		"Exits": [["SteelProduction", "Steam"]],
		"Experiments": 25,
		"Experiment": [["Triod", 1], ["CopperPipe", 2], ["CopperConveyor", 1]],
	},
	{
		"Name": "Steam",
		"Label": "SteamEngine",
		"Title": "SteamPower",
		"Position": [2, 2],
		"Tree": [
			["Boiler", ""],
			["SteamEngine", "Boiler"],
			["Flywheel", "SteamEngine"],
			["DecorativeWood2", "Flywheel"],
			["SteelCompactGenerator", "SteamEngine"],
			["SteelComputer", "SteelCompactGenerator"],
			["SteelFurnace", "Boiler"],
			["SteelOven", "SteelFurnace"],
			["SteelSmelter", "SteelFurnace"],
			["SteelBlastFurnace", "SteelSmelter"],
			["SteelFluidFurnace", "Boiler"],
			["SteelKineticHeater", "SteelFluidFurnace"],
			["SteelPump", "SteelFluidFurnace"],
			["SteelAtmosphericCondenser", "SteelPump"],
		],
		"Exits": [["SteelCompactGenerator", "Electricity"]],
		"Experiments": 25,
		"Experiment": [["CopperPump", 1], ["SteelPipe", 3]],
	},
	{
		"Name": "Electricity",
		"Label": "Generator",
		"Title": "Electricity",
		"Image": "T_LightBulb",
		"Position": [2, 3],
		"Tree": [
			["BasicCoil", ""],
			["ElectricEngine", "BasicCoil"],
			["WindTurbine", "ElectricEngine"],
			["Electrolyzer", "BasicCoil"],
			["AdvancedSmelting", "Electrolyzer"],
			["ElectricFurnace", "AdvancedSmelting"],
			["ElectricalSwitch", "BasicCoil"],
			["Lamp", "ElectricalSwitch"],
			["Diode", "Lamp"],
			["Spotlight", "Lamp"],
			["Flashlight", "Spotlight"],
			["SteelLoader", "ElectricEngine"],
		],
		"Exits": [["AdvancedSmelting", "SteelPortal"]],
		"Experiments": 25,
		"Experiment": [["SteelBoiler", 1], ["SteelSteamEngine", 1]],
	},
	{
		"Name": "Transistor",
		"Label": "Processor",
		"Title": "Microelectronics",
		"Image": "T_Microelectronics",
		"Position": [0, 2],
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
		],
		"Versions": [
			["Transistor", 3, ["Diode", "DistributedComputing"]],
		],
		"Exits": [["SatelliteAntenna", "SatelliteAntenna"]],
		"Experiments": 25,
		"Experiment": [["Circuit", 4], ["CopperWire", 4]],
	},
	{
		"Name": "SatelliteAntenna",
		"Label": "SatelliteAntenna",
		"Position": [0, 4],
		"Build": "SatelliteAntenna",
		"Tree": [],
		"Exits": [["", "Silicon"]],
		"Experiments": 1,
	},
	{
		"Name": "Aluminium",
		"Label": "AluminiumProduction",
		"Position": [1, 4],
		"Tree": [
			["AluminiumReduction", ""],
			["AluminiumProduction", "AluminiumReduction"],
			["ReinforcedFrame", "AluminiumProduction"],
			["Boat", "AluminiumElectricEngine"],
			["OffroadVehicle", "Boat"],
			["Jetpack", "Boat"],
			["Sifter", "AluminiumSeparator"],
			["ReinforcedConcrete", "ReinforcedFrame"],
			["ReinforcedConcreteTiles", "ReinforcedConcrete"],
			["ReinforcedConcreteSmallTiles", "ReinforcedConcreteTiles"],
			["ReinforcedConcreteBricks", "ReinforcedConcreteTiles"],
			["DangerBlock", "ReinforcedConcrete"],
			["DecorativeWood3", "DangerBlock"],
			["Designable3", "DecorativeWood3"],
			["DecorativeWood4", "Designable3"],
			["InventoryUpgrade3", "AluminiumChest"],
			["SteamTurbine", "ReinforcedFrame"],
			["Generator", "AluminiumWindTurbine"],
			["SmallSolarPanel", "Generator"],
			["SolarPanel", "SmallSolarPanel"],
		],
		"Rows": 10,
		"Versions": [
			["AluminiumReduction", 3, ["AutomaticHammer", "Macerator", "Constructor", "Separator", "OreWasher", "Mixer"], [-1, 0]],
			["AluminiumMacerator", 3, ["Automatization", "Conveyor", "Splitter", "Loader", "Sorter"]],
			["AluminiumConveyor", 3, ["AutomaticFarm", "AutomaticMining"]],
			["AluminiumSeparator", 3, ["Pump", "AtmosphericCondenser", "Electrolyzer"]],
			["AluminiumProduction", 3, ["PowerGeneration", "Flywheel", "ElectricEngine", "WindTurbine"]],
			["AluminiumProduction", 3, ["MetalBlocks", "Lamp", "SingleTypeStorage", "Destroyer", "Sign", "AdvancedSign", "Chest", "Container"]],
			["AluminiumMixer", 3, ["Furnace", "FluidFurnace", "ElectricFurnace", "AdvancedSmelting", "SteelProduction", "Oven"]],
			["AluminiumElectricFurnace", 3, ["KineticHeater", "Boiler", "SteamEngine"]],
		],
		"Exits": [["AluminiumProduction", "AluminiumPortal"], ["ReinforcedFrame", "Chemistry"]],
		"Experiments": 30,
		"Experiment": [["SteelElectrolyzer", 1], ["SteelSeparator", 1]],
	},
	{
		"Name": "Chemistry",
		"Label": "ChemicalBath",
		"Position": [3, 4],
		"Tree": [
			["ChemicalBath", ""],
			["Catalyst", "ChemicalBath"],
			["Catalyst2", "SulfuricAcid"],
			["Polyethylene", "IndustrialChemReactor"],
			["Sulfur", "ChemicalBath"],
			["SulfuricAcid", "IndustrialChemReactor"],
			["Battery", "SulfuricAcid"],
			["BatteryBox", "Battery"],
			["Fermentation", "ChemicalBath"],
			["PlasticBlock", "Polyethylene"],
			["IndustrialChemReactor", "Catalyst"],
		],
		"Exits": [],
		"Experiments": 25,
		"Experiment": [["Cell", 1], ["SteelPump", 1]],
	},
	{
		"Name": "Silicon",
		"Label": "QuantumCircuit",
		"Position": [0, 6],
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
		"Versions": [
			["SiliconWafer", 4, ["Diode", "DistributedComputing", "BatteryBox", "SmallSolarPanel", "SolarPanel"]],
		],
		"Exits": [["QuantumProcessor", "QuantumBrain"]],
		"Experiments": 50,
		"Experiment": [["Processor", 1], ["AdvancedCircuit", 2]],
	},
	{
		"Name": "StainlessSteel",
		"Label": "StainlessSteelProduction",
		"Position": [1, 6],
		"Tree": [
			["AdvancedAlloys", ""],
			["StainlessSteelProduction", "AdvancedAlloys"],
			["IndustrialSmelting", "StainlessSteelProduction"],
			["IndustrialSteelProduction", "IndustrialSmelting"],
			["ModularFrame", "StainlessSteelProduction"],
			["Monitor", "ModularFrame"],
			["AdvancedNightVision", "Monitor"],
			["AdvancedCoil", "ModularFrame"],
			["AdvancedJetpack", "AdvancedCoil"],
			["AdvancedSteampack", "AdvancedJetpack"],
			["InventoryUpgrade4", "StainlessSteelChest"],
		],
		"Rows": 6,
		"Versions": [
			["AdvancedAlloys", 4, ["AutomaticHammer", "Macerator", "Constructor", "Mixer", "Assembler"], [-1, 0]],
			["StainlessSteelMacerator", 4, ["Sifter", "Separator", "OreWasher"]],
			["StainlessSteelMixer", 4, ["Automatization", "Conveyor", "Splitter", "Loader", "Sorter"]],
			["StainlessSteelConveyor", 4, ["AutomaticFarm", "AutomaticMining"]],
			["StainlessSteelProduction", 4, ["MetalBlocks", "Lamp", "SingleTypeStorage", "Destroyer", "Sign", "AdvancedSign", "Chest", "Container"]],
			["StainlessSteelAssembler", 4, ["ElectricFurnace", "SteelProduction", "FluidFurnace", "AdvancedSmelting", "Furnace", "Oven"]],
		],
		"Exits": [["IndustrialSmelting", "StainlessSteelPortal"], ["StainlessSteelProduction", "Oil"]],
		"Experiments": 50,
		"Experiment": [["ReinforcedFrame", 1], ["AluminiumPipe", 8], ["AluminiumFoil", 12]],
	},
	{
		"Name": "Oil",
		"Label": "FuelChemistry",
		"Position": [2, 6],
		"Tree": [
			["PyrolysisUnit", ""],
			["PreciseTemperaturePyrolysis", "PyrolysisUnit"],
			["FuelChemistry", "PreciseTemperaturePyrolysis"],
			["FuelChemistry2", "FuelChemistry"],
			["FuelChemistry3", "FuelChemistry2"],
			["FractionatingColumn", "FuelChemistry"],
			["CombustionEngine", "FuelChemistry"],
			["Pumpjack", "PyrolysisUnit"],
			["DecorativePlastic", "PyrolysisUnit"],
		],
		"Versions": [
			["PyrolysisUnit", 4, ["Pump", "AtmosphericCondenser", "IndustrialChemReactor", "Fermentation", "Electrolyzer", "ChemicalBath"]],
			["FuelChemistry2", 4, ["KineticHeater", "Boiler", "SteamTurbine", "SteamEngine"]],
			["CombustionEngine", 4, ["PowerGeneration", "Flywheel", "ElectricEngine", "WindTurbine", "Generator"]],
		],
		"Exits": [["Pumpjack", "PumpjackProductivity"]],
		"Experiments": 100,
		"Experiment": [["BasicFrame", 2], ["AluminiumPipe", 6], ["StainlessSteelPipe", 2]],
	},
	{
		"Name": "QuantumBrain",
		"Label": "QuantumBrain",
		"Position": [0, 8],
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
		"Experiments": 12,
		"Experiment": [["QuantumProcessor", 2], ["QuantumCircuit", 5]],
	},
	{
		"Name": "Titanium",
		"Label": "TitaniumProduction",
		"Position": [1, 8],
		"CostMul": 2,
		"Tree": [
			["NitricAcid", ""],
			["KrollProcess", "NitricAcid"],
			["NitroBriquette", "KrollProcess"],
			["TitaniumProduction", "KrollProcess"],
			["FastSifting", "KrollProcess"],
			["PowerCoil", "TitaniumProduction"],
			["BigMonitor", "PowerCoil"],
			["PlatinumSolution", "NitricAcid"],
			["CircuitBoard3", "PlatinumSolution"],
			["CrudeTantalum", "NitricAcid"],
			["Capacitor4", "CrudeTantalum"],
			["Resistor4", "CrudeTantalum"],
		],
		"Versions": [
			["NitricAcid", 5, ["AutomaticHammer", "Macerator", "Constructor", "Mixer", "Assembler"], [-1, 0]],
			["TitaniumMixer", 5, ["Sifter", "Separator", "OreWasher"]],
			["TitaniumMacerator", 5, ["Automatization", "Conveyor", "Splitter", "Loader", "Sorter"]],
			["TitaniumConveyor", 5, ["AutomaticFarm", "Pumpjack", "AutomaticMining"]],
			["TitaniumAssembler", 5, ["MetalBlocks", "Lamp", "SingleTypeStorage", "Destroyer", "Sign", "AdvancedSign", "Chest", "Container", "DeepStorage"]],
		],
		"Exits": [["TitaniumProduction", "TitaniumPortal"], ["FastSifting", "Nuclear"]],
		"Experiments": 15,
		"Experiment": [["ModularFrame", 1], ["AdvancedCoil", 4], ["SiliconMonocrystal", 3]],
	},
	{
		"Name": "Nuclear",
		"Label": "FissionReactor",
		"Position": [2, 8],
		"CostMul": 2,
		"CostMulOf": {name: 4 for name in ["UraniumCell", "FissionReactor", "ControlCell", "ReflectorCell", "ReactionThrottling", "AdvancedReflection", "AdvancedReflection2"]},
		"Tree": [
			["UraniumCell", ""],
			["FissionReactor", "UraniumCell"],
			["ControlCell", "FissionReactor"],
			["ReflectorCell", "ControlCell"],
			["AdvancedReflection", "ReflectorCell"],
			["IndustrialBoiler", "FissionReactor"],
			["IndustrialSteamTurbine", "IndustrialBoiler"],
			["IndustrialGenerator", "IndustrialSteamTurbine"],
			["ReactionThrottling", "ControlCell"],
			["AdvancedReflection2", "AdvancedReflection"],
		],
		"Versions": [
			["UraniumCell", 5, ["Pump", "AtmosphericCondenser", "FractionatingColumn", "IndustrialChemReactor", "Fermentation", "PyrolysisUnit", "Electrolyzer", "ChemicalBath"], [1, 0]],
			["TitaniumAtmosphericCondenser", 5, ["KineticHeater", "Boiler", "SteamTurbine", "SteamEngine"]],
			["TitaniumChemicalBath", 5, ["PowerGeneration", "Flywheel", "CombustionEngine", "ElectricEngine", "WindTurbine", "Generator"], [0, 1]],
			["TitaniumElectricEngine", 5, ["Diode", "DistributedComputing", "BatteryBox", "SmallSolarPanel", "SolarPanel"]],
			["TitaniumKineticAccumulator", 5, ["ElectricFurnace", "SteelProduction", "AdvancedSmelting", "FluidFurnace", "Furnace", "Oven", "IndustrialSmelting"]],
		],
		"Exits": [["AdvancedReflection", "Breeder"]],
		"Experiments": 15,
		"Experiment": [["QuantumCircuit", 1], ["TitaniumPipe", 5], ["Cell", 9]],
	},
	{
		"Name": "Breeder",
		"Label": "ThoriumReaction",
		"Title": "Breeder",
		"Position": [2, 9],
		"CostMul": 2,
		"CostMulOf": {name: 4 for name in ["ThoriumReaction", "PlutoniumReaction", "PlutoniumReaction2"]},
		"Tree": [
			["ThoriumReaction", ""],
			["PlutoniumReaction", "ThoriumReaction"],
			["PlutoniumReaction2", "PlutoniumReaction"],
			["Riteg", "PlutoniumReaction2"],
		],
		"Exits": [],
		"Experiments": 6,
		"Experiment": [["UraniumCell", 1], ["ReflectorCell", 1], ["ControlCell", 1]],
	},
	{
		"Name": "Composite",
		"Label": "CompositePlate",
		"Position": [1, 10],
		"Tree": [
			["CarbonFiber", ""],
			["CarbonFiberSheet", "CarbonFiber"],
			["CompositePlate", "CarbonFiberSheet"],
			["PlatinumReflector", "CompositePlate"],
			["HugeMonitor", "CompositePlate"],
			["InventoryUpgrade5", "CompositeChest"],
		],
		"Versions": [
			["CarbonFiber", 6, ["AutomaticHammer", "Macerator", "Constructor", "Mixer", "Assembler"], [1, 0]],
			["CompositeMixer", 6, ["Sifter", "Separator", "OreWasher"]],
			["CompositeMacerator", 6, ["Automatization", "Conveyor", "Splitter", "Loader", "Sorter"]],
			["CompositeLoader", 6, ["AutomaticFarm", "Pumpjack", "AutomaticMining"]],
			["CompositeOreWasher", 6, ["MetalBlocks", "Lamp", "SingleTypeStorage", "Destroyer", "Sign", "AdvancedSign", "Chest", "Container", "DeepStorage"]],
			["CompositeAutomaticHammer", 6, ["Pump", "AtmosphericCondenser", "FractionatingColumn", "IndustrialChemReactor", "Fermentation", "PyrolysisUnit", "Electrolyzer", "ChemicalBath"], [0, 1]],
			["CompositePyrolysisUnit", 6, ["ElectricFurnace", "SteelProduction", "AdvancedSmelting", "FluidFurnace", "Furnace", "Oven", "IndustrialSmelting"]],
			["CompositeChemicalBath", 6, ["KineticHeater", "Boiler", "SteamTurbine", "SteamEngine"], [0, 1]],
			["CompositeBoiler", 6, ["IndustrialBoiler", "IndustrialSteamTurbine", "FissionReactor", "Riteg"]],
			["CompositeSteamEngine", 6, ["PowerGeneration", "Flywheel", "IndustrialGenerator", "CombustionEngine", "ElectricEngine", "WindTurbine", "Generator"]],
			["PlatinumReflector", 6, ["Diode", "DistributedComputing", "BatteryBox", "SmallSolarPanel", "SolarPanel"]],
		],
		"Exits": [["PlatinumReflector", "CompositePortal"]],
		"Experiments": 30,
		"Experiment": [["PowerCoil", 4], ["ReinforcedFrame", 2], ["PlatinumWire", 2]],
	},
	{
		"Name": "Fusion",
		"Label": "FusionReaction",
		"Position": [1, 12],
		"Tree": [
			["FusionReactor", ""],
			["Rocket", "FusionReactor"],
			["FusionReaction", "Rocket"],
			["CompositePlate2", "FusionReaction"],
			["NeutroniumProduction", "FusionReaction"],
			["NeutroniumProduction2", "UltimateCatalyst"],
			["UltimateCatalyst", "NeutroniumProduction"],
			["FuelChemistry4", "UltimateCatalyst"],
			["InventoryUpgrade6", "NeutroniumChest"],
		],
		"Versions": [
			["FusionReactor", 7, ["AutomaticHammer", "Macerator", "Constructor", "Mixer", "Assembler"], [-1, 0]],
			["NeutroniumMixer", 7, ["Sifter", "Separator", "OreWasher"]],
			["NeutroniumMacerator", 7, ["Automatization", "Conveyor", "Splitter", "Loader", "Sorter"]],
			["NeutroniumLoader", 7, ["AutomaticFarm", "Pumpjack", "AutomaticMining"]],
			["NeutroniumOreWasher", 7, ["MetalBlocks", "Lamp", "SingleTypeStorage", "Destroyer", "Sign", "AdvancedSign", "Chest", "Container", "DeepStorage"]],
			["NeutroniumAutomaticHammer", 7, ["Pump", "AtmosphericCondenser", "FractionatingColumn", "IndustrialChemReactor", "Fermentation", "PyrolysisUnit", "Electrolyzer", "ChemicalBath"], [0, 1]],
			["NeutroniumPyrolysisUnit", 7, ["ElectricFurnace", "SteelProduction", "AdvancedSmelting", "FluidFurnace", "Furnace", "Oven", "IndustrialSmelting"]],
			["NeutroniumChemicalBath", 7, ["KineticHeater", "Boiler", "SteamTurbine", "SteamEngine"], [0, 1]],
			["NeutroniumBoiler", 7, ["IndustrialBoiler", "IndustrialSteamTurbine", "FusionReactor", "FissionReactor", "Riteg"]],
			["NeutroniumSteamEngine", 7, ["PowerGeneration", "Flywheel", "IndustrialGenerator", "CombustionEngine", "ElectricEngine", "WindTurbine", "Generator"]],
			["NeutroniumSteamTurbine", 7, ["Diode", "BatteryBox", "SmallSolarPanel", "SolarPanel"]],
		],
		"Exits": [["UltimateCatalyst", "NeutroniumPortal"]],
		"Experiments": 20,
		"Experiment": [["QuantumBrain", 1], ["PowerCoil", 1], ["PlatinumReflector", 2]],
	},
	{
		"Name": "Infinite",
		"Label": "DrillingRigProductivity8",
		"Position": [1, 14],
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

portal_cards = [
	("CopperPortal", 1, [1, 1], [0, 1], "Steel"),
	("SteelPortal", 2, [2, 4], [2], "Aluminium"),
	("AluminiumPortal", 3, [1, 5], [3], "StainlessSteel"),
	("StainlessSteelPortal", 4, [1, 7], [4], "Titanium"),
	("TitaniumPortal", 5, [1, 9], [5], "Composite"),
	("CompositePortal", 6, [1, 11], [6], "Fusion"),
	("NeutroniumPortal", 7, [1, 13], [7, 8], "Infinite"),
]
milestones += [{
	"Name": name,
	"Label": "PortalTier" + str(tier),
	"Position": position,
	"Build": "Portal",
	"Stages": stages,
	"Tree": [],
	"Exits": [["", target]],
	"Experiments": 1,
} for name, tier, position, stages, target in portal_cards]

productivity_cards = [
	("DrillingRigProductivity", [2, 0], [[120, pack] for pack in mass_packs]),
	("PumpjackProductivity", [3, 6], [[30, pipe_packs[3]]] * 4 + [[120, pack] for pack in pipe_packs[4:]]),
]
milestones += [{
	"Name": name,
	"Label": name,
	"Position": position,
	"Tree": [[name, ""]],
	"Exits": [],
	"Experiments": 0,
	"Experiment": [],
	"Levels": levels,
} for name, position, levels in productivity_cards]

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
		for d in [d] if d != (0, 0) else sorted({axis(v) for v in exit_dirs[exit_name]}):
			cell = (pos[exit_name][0] + d[0], pos[exit_name][1] + d[1]) if exit_name in pos else (-1, -1)
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
laboratory = next(machine for machine in machines if machine.get("BlockLogic") == "ResearchLaboratoryBlockLogic")

def version_card(series, tier):
	for version in research_by_name[series].get("Versions", []):
		if research_by_name[version["Technology"]]["Levels"][0] == tier:
			return version["Technology"]
	raise Exception(f"Milestones: {series} has no version of tier {tier}")

for m in milestones:
	for group in m.get("Versions", []):
		up, tier, series = group[:3]
		cards = [card for _, _, card in sorted((research_by_name[card]["Complexity"], i, card) for i, card in enumerate(version_card(s, tier) for s in series))]
		m["Tree"] += [[card, cards[k - 1 - (k - 1) % 2] if k else up] for k, card in enumerate(cards)]
		if len(group) > 3:
			m.setdefault("Chunks", {})[cards[0]] = group[3]

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
		recipes = stages["Recipes"]
		chosen = [recipes[k] for k in m["Stages"]] if "Stages" in m else recipes
		bill = {}
		for stage in chosen:
			for need in stage["Input"]["Items"]:
				bill[need["Name"]] = bill.get(need["Name"], 0) + need["Count"]
		m["Experiment"] = [[name, count] for name, count in bill.items()]
		m["Stage"] = chosen[-1]["Name"]
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

	levels = m.get("Levels", [])
	for item, count in m["Experiment"] + [entry for _, pack in levels for entry in pack]:
		if item not in item_names:
			raise Exception(f"Milestones: experiment of {m['Name']} names an unknown item {item}")
		if not isinstance(count, int) or count < 1:
			raise Exception(f"Milestones: experiment of {m['Name']} takes {count} of {item}, a pack holds whole items")
	if (m["Experiments"] > 0) != bool(m["Experiment"]):
		raise Exception(f"Milestones: {m['Name']} has {m['Experiments']} experiments of {m['Experiment']}")
	if levels:
		head = research_by_name[m["Head"]]
		if m["Experiments"] or built or not head.get("Infinite") or head.get("MaxLevel") != len(levels):
			raise Exception(f"Milestones: {m['Name']} has {len(levels)} levels, its head {m['Head']} takes {head.get('MaxLevel')} and nothing else pays for it")
		if any(not isinstance(count, int) or count < 1 or not pack for count, pack in levels):
			raise Exception(f"Milestones: a level of {m['Name']} takes no experiments or an empty pack")

unplaced = [r["Name"] for r in research_objects if r["Class"] == "StaticResearchTechnology" and r["Name"] not in owner]
if unplaced:
	raise Exception(f"Milestones: machine versions on no milestone: {unplaced}")

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
		back = add(anchor_local, (e[0], 1)) if e[0] and any(axis(d) == (-e[0], 0) for _, d in box["Exits"]) else None
		reserved += [cell for cell in (add(anchor_local, (dx, dy)) for dx in (-1, 0, 1) for dy in (-1, 0, 1)) if cell != back]
	local_layout = lambda extra: layout({"Name": key, "Tree": box["Tree"], "Head": box["Head"]}, cell_columns, rows, head_local, exit_dirs, reserved + extra) if box["Tree"] else ({}, [])
	local, missed = local_layout([])
	above = [(head_local[0], y) for y in range(head_local[1])] if entry and e[0] and not carded else []

	for k in range(1000):
		if k == 1 and above:
			local, missed = local_layout(above)
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
	long_links += [f"{key}:{n}" for n in missed]

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
		"Recipe": [m["Build"] + "Stage" + r_dict, m["Stage"]] if built else [laboratory["Name"] + r_dict, m["Name"] + "Experiment"] if m["Experiments"] else [],
	})
	if "Image" in m:
		objects[-1]["Image"] = m["Image"]
	if "Levels" in m:
		objects[-1]["Levels"] = [{
			"Experiments": count,
			"Experiment": pack,
			"Recipe": [laboratory["Name"] + r_dict, m["Name"] + "Experiment" + str(level + 1)],
		} for level, (count, pack) in enumerate(m["Levels"])]
	if built:
		objects[-1]["Build"] = m["Build"]
		del objects[-1]["Head"]

write_file("Generated/Researches/milestones.json", {"Objects": objects})

write_file("Generated/Recipes/laboratory.json", {"Objects": [{
	"Class": r_dict,
	"Name": laboratory["Name"] + r_dict,
	"StartTier": 0,
	"UsedIn": [{"Item": tier_material[laboratory["StartTier"]] + laboratory["Name"], "Tier": laboratory["StartTier"]}],
	"Recipes": [{
		"Name": m["Name"] + "Experiment",
		"Input": items(m["Experiment"]),
		"Output": no_items(),
		"Ticks": experiment_ticks,
	} for m in milestones if m["Experiments"] and "Build" not in m] + [{
		"Name": m["Name"] + "Experiment" + str(level + 1),
		"Input": items(pack),
		"Output": no_items(),
		"Ticks": experiment_ticks,
	} for m in milestones for level, (count, pack) in enumerate(m.get("Levels", []))],
}]})
