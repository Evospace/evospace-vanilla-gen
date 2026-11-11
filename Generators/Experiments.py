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

experiments = [
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
		"Runs": 0,
		"Pack": [],
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
		"Runs": 25,
		"Pack": [["Triod", 1], ["CopperPipe", 2], ["CopperConveyor", 1]],
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
		"Runs": 25,
		"Pack": [["CopperPump", 1], ["SteelPipe", 3]],
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
			["PowerPole", "ElectricalSwitch"],
			["Lamp", "ElectricalSwitch"],
			["Diode", "Lamp"],
			["Spotlight", "Lamp"],
			["Flashlight", "Spotlight"],
			["SteelLoader", "ElectricEngine"],
		],
		"Exits": [["AdvancedSmelting", "SteelPortal"]],
		"Runs": 25,
		"Pack": [["SteelBoiler", 1], ["SteelSteamEngine", 1]],
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
		"Runs": 25,
		"Pack": [["Circuit", 4], ["CopperWire", 4]],
	},
	{
		"Name": "SatelliteAntenna",
		"Label": "SatelliteAntenna",
		"Position": [0, 4],
		"Build": "SatelliteAntenna",
		"Tree": [],
		"Exits": [["", "Silicon"]],
		"Runs": 1,
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
			["ReinforcedConcrete", "AluminiumProduction"],
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
		"Runs": 30,
		"Pack": [["SteelElectrolyzer", 1], ["SteelSeparator", 1]],
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
			["PowerTower", "BatteryBox"],
			["Fermentation", "ChemicalBath"],
			["PlasticBlock", "Polyethylene"],
			["IndustrialChemReactor", "Catalyst"],
		],
		"Exits": [],
		"Runs": 25,
		"Pack": [["Cell", 1], ["SteelPump", 1]],
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
		"Runs": 50,
		"Pack": [["Processor", 1], ["AdvancedCircuit", 2]],
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
			["StainlessSteelSeparator", 4, ["Pump", "AtmosphericCondenser", "Electrolyzer"]],
			["StainlessSteelElectricFurnace", 4, ["KineticHeater", "Boiler", "SteamTurbine", "SteamEngine"]],
			["StainlessSteelProduction", 4, ["PowerGeneration", "Flywheel", "ElectricEngine", "WindTurbine", "Generator"]],
		],
		"Exits": [["IndustrialSmelting", "StainlessSteelPortal"], ["StainlessSteelProduction", "Oil"]],
		"Runs": 50,
		"Pack": [["ReinforcedFrame", 1], ["AluminiumPipe", 8], ["AluminiumFoil", 12]],
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
			["PyrolysisUnit", 4, ["IndustrialChemReactor", "Fermentation", "ChemicalBath"]],
		],
		"Exits": [["Pumpjack", "PumpjackProductivity"]],
		"Runs": 100,
		"Pack": [["BasicFrame", 2], ["AluminiumPipe", 6], ["StainlessSteelPipe", 2]],
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
		"Runs": 12,
		"Pack": [["QuantumProcessor", 2], ["QuantumCircuit", 5]],
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
		"Runs": 15,
		"Pack": [["ModularFrame", 1], ["AdvancedCoil", 4], ["SiliconMonocrystal", 3]],
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
		"Runs": 15,
		"Pack": [["QuantumCircuit", 1], ["TitaniumPipe", 5], ["Cell", 9]],
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
		"Runs": 6,
		"Pack": [["UraniumCell", 1], ["ReflectorCell", 1], ["ControlCell", 1]],
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
			["CompositeOreWasher", 6, ["MetalBlocks", "Lamp", "SingleTypeStorage", "Destroyer", "Sign", "AdvancedSign", "Chest", "Container", "DeepStorage"], [0, 1]],
			["CompositeAutomaticHammer", 6, ["Pump", "AtmosphericCondenser", "FractionatingColumn", "IndustrialChemReactor", "Fermentation", "PyrolysisUnit", "Electrolyzer", "ChemicalBath"], [0, 1]],
			["CompositePyrolysisUnit", 6, ["ElectricFurnace", "SteelProduction", "AdvancedSmelting", "FluidFurnace", "Furnace", "Oven", "IndustrialSmelting"]],
			["CompositeChemicalBath", 6, ["KineticHeater", "Boiler", "SteamTurbine", "SteamEngine"], [0, 1]],
			["CompositeBoiler", 6, ["IndustrialBoiler", "IndustrialSteamTurbine", "FissionReactor", "Riteg"]],
			["CompositeSteamEngine", 6, ["PowerGeneration", "Flywheel", "IndustrialGenerator", "CombustionEngine", "ElectricEngine", "WindTurbine", "Generator"]],
			["PlatinumReflector", 6, ["Diode", "DistributedComputing", "BatteryBox", "SmallSolarPanel", "SolarPanel"]],
		],
		"Exits": [["PlatinumReflector", "CompositePortal"]],
		"Runs": 30,
		"Pack": [["PowerCoil", 4], ["ReinforcedFrame", 2], ["PlatinumWire", 2]],
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
		"Runs": 20,
		"Pack": [["QuantumBrain", 1], ["PowerCoil", 1], ["PlatinumReflector", 2]],
	},
	{
		"Name": "Infinite",
		"Label": "InventoryUpgrade7",
		"Position": [1, 14],
		"Tier": 8,
		"Tree": [
			["InventoryUpgrade7", ""],
		],
		"Exits": [],
		"Runs": 0,
		"Pack": [],
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
experiments += [{
	"Name": name,
	"Label": "PortalTier" + str(tier),
	"Position": position,
	"Build": "Portal",
	"Stages": stages,
	"Tree": [],
	"Exits": [["", target]],
	"Runs": 1,
} for name, tier, position, stages, target in portal_cards]

modifier_by_name = {o["Name"]: o for o in get_generated_files()["Generated/Mixed/modifiers.json"]["Objects"]}
productivity_bonus = 5
productivity_cards = [
	("DrillingRigProductivity", [2, 0], [[120, pack] for pack in mass_packs]),
	("PumpjackProductivity", [3, 6], [[30, pipe_packs[3]]] * 4 + [[120, pack] for pack in pipe_packs[4:]]),
]
experiments += [{
	"Name": name,
	"Modifier": name,
	"BonusValue": productivity_bonus,
	"Position": position,
	"Tree": [],
	"Exits": [],
	"Runs": 0,
	"Pack": [],
	"Levels": levels,
	"Step": levels[-1][0],
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
	pa, pb = experiment_by_name[a]["Position"], experiment_by_name[b]["Position"]
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

	def corridor(exit_name):
		d = axis((sign(sum(v[0] for v in exit_dirs[exit_name])), sign(sum(v[1] for v in exit_dirs[exit_name]))))
		for d in [d] if d != (0, 0) else sorted({axis(v) for v in exit_dirs[exit_name]}):
			cell = (pos[exit_name][0] + d[0], pos[exit_name][1] + d[1]) if exit_name in pos else (-1, -1)
			while inside(cell):
				reserved.add(cell)
				cell = (cell[0] + d[0], cell[1] + d[1])

	if head in exit_dirs:
		corridor(head)
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
		corridor(exit_name)

	order = [head]
	for name in order:
		order.extend(sorted(children[name], key=lambda c: -size[c]))

	todo = [name for name in order if name not in pos]
	links = {frozenset((pos[name], pos[parent[name]])) for name in pos if parent[name]}
	waiting = {name: sum(1 for c in children[name] if c not in pos) for name in children}

	def candidates(name):
		at = pos[parent[name]]
		found = []
		for group, bonus in ((steps, 100), (diagonals, 0)):
			for s in group:
				cell = add(at, s)
				if not free(cell) or (bonus == 0 and frozenset(((at[0], cell[1]), (cell[0], at[1]))) in links):
					continue
				outward = distance(cell, head_cell) - distance(at, head_cell)
				found.append((bonus + (2 * room(cell) if size[name] > 1 else -room(cell)) + 1.5 * outward - 0.5 * abs(cell[0] - centre), cell))
		return [cell for _, cell in sorted(found, key=lambda f: -f[0])]

	around = lambda cell: [add(cell, s) for s in steps + diagonals]

	def starved(cell):
		for near_cell in [cell] + around(cell):
			name = taken.get(near_cell)
			if waiting.get(name) and sum(1 for c in around(near_cell) if free(c)) < waiting[name]:
				return True
		return False

	rank = {name: k for k, name in enumerate(order)}
	budget = [200000]
	def place(left):
		if not left:
			return True
		_, _, name, cells = min((len(cells), rank[name], name, cells) for name in left if parent[name] in pos for cells in [candidates(name)])
		up = parent[name]
		left.discard(name)
		for cell in cells:
			budget[0] -= 1
			if budget[0] < 0:
				break
			put(name, cell)
			link = frozenset((cell, pos[up]))
			links.add(link)
			waiting[up] -= 1
			if not starved(cell) and place(left):
				return True
			waiting[up] += 1
			links.discard(link)
			del pos[name], taken[cell]
		left.add(name)
		return False

	if not place(set(todo)):
		raise Exception(f"Experiments: {m['Name']} has no layout where every card stands next to its parent: {len(todo)} cards for {sum(1 for x in range(columns) for y in range(rows) if free((x, y)))} free cells, {'search ran out' if budget[0] < 0 else 'every order tried'}")
	return pos

research_objects = objects_of(get_generated_files()["Generated/Researches/basic.json"])
research_by_name = {r["Name"]: r for r in research_objects}
item_names = {o["Name"] for data in get_generated_files().values() for o in objects_of(data) if o.get("Class", "").startswith("StaticItem")}
experiment_by_name = {m["Name"]: m for m in experiments}
stage_dicts = {o["Name"]: o for data in get_generated_files().values() for o in objects_of(data) if o.get("Class") == r_dict and o.get("Recipes")}
laboratory = next(machine for machine in machines if machine.get("BlockLogic") == "ResearchLaboratoryBlockLogic")

def version_card(series, tier):
	for version in research_by_name[series].get("Versions", []):
		if research_by_name[version["Technology"]]["Levels"][0] == tier:
			return version["Technology"]
	raise Exception(f"Experiments: {series} has no version of tier {tier}")

for m in experiments:
	for group in m.get("Versions", []):
		up, tier, series = group[:3]
		cards = [card for _, _, card in sorted((research_by_name[card]["Complexity"], i, card) for i, card in enumerate(version_card(s, tier) for s in series))]
		m["Tree"] += [[card, cards[k - 1] if k else up] for k, card in enumerate(cards)]
		if len(group) > 3:
			m.setdefault("Chunks", {})[cards[0]] = group[3]

owner = {}
positions = {}
for m in experiments:
	position = tuple(m["Position"])
	if position in positions:
		raise Exception(f"Experiments: {m['Name']} and {positions[position]} share the cell {position}")
	positions[position] = m["Name"]

	built = "Build" in m
	leveled = "Levels" in m
	heads = [name for name, up in m["Tree"] if not up]
	if len(heads) != (0 if built or leveled else 1):
		raise Exception(f"Experiments: {m['Name']} needs {'no head, it is built' if built else 'no head, it is leveled' if leveled else 'exactly one head'}, has {heads}")
	m["Head"] = heads[0] if heads else ""
	m["Researches"] = [name for name, _ in m["Tree"]]
	if built:
		stages = stage_dicts.get(m["Build"] + "Stage" + r_dict)
		if m["Build"] not in item_names or not stages:
			raise Exception(f"Experiments: {m['Name']} is built as {m['Build']}, which has no item or no stages")
		if m["Runs"] != 1:
			raise Exception(f"Experiments: {m['Name']} is passed by one build, not {m['Runs']}")
		recipes = stages["Recipes"]
		chosen = [recipes[k] for k in m["Stages"]] if "Stages" in m else recipes
		bill = {}
		for stage in chosen:
			for need in stage["Input"]["Items"]:
				bill[need["Name"]] = bill.get(need["Name"], 0) + need["Count"]
		m["Pack"] = [[name, count] for name, count in bill.items()]
		m["Stage"] = chosen[-1]["Name"]
	for name, up in m["Tree"]:
		if name not in research_by_name:
			raise Exception(f"Experiments: {m['Name']} names an unknown research {name}")
		if up and up not in m["Researches"]:
			raise Exception(f"Experiments: {name} in {m['Name']} hangs on {up}, which is not in the experiment")
		if name in owner:
			raise Exception(f"Experiments: {name} is in both {owner[name]} and {m['Name']}")
		owner[name] = m["Name"]
		research_by_name[name]["Complexity"] *= m.get("CostMulOf", {}).get(name, m.get("CostMul", 1))
	for name in m.get("CostMulOf", {}):
		if name not in m["Researches"]:
			raise Exception(f"Experiments: CostMulOf of {m['Name']} names {name}, which is not in the experiment")
	if not leveled and m["Label"] not in research_by_name:
		raise Exception(f"Experiments: {m['Name']} takes its label from an unknown research {m['Label']}")

	levels = m.get("Levels", [])
	for item, count in m["Pack"] + [entry for _, pack in levels for entry in pack]:
		if item not in item_names:
			raise Exception(f"Experiments: experiment of {m['Name']} names an unknown item {item}")
		if not isinstance(count, int) or count < 1:
			raise Exception(f"Experiments: experiment of {m['Name']} takes {count} of {item}, a pack holds whole items")
	if (m["Runs"] > 0) != bool(m["Pack"]):
		raise Exception(f"Experiments: {m['Name']} has {m['Runs']} experiments of {m['Pack']}")
	if leveled:
		if m["Runs"] or built or m["Tree"] or m.get("Modifier") not in modifier_by_name or m.get("BonusValue", 0) < 1 or m.get("Step", 0) < 1:
			raise Exception(f"Experiments: leveled {m['Name']} needs a modifier, a bonus per level and a step of runs past its levels, and no runs, stages or researches of its own")
		if not levels or any(not isinstance(count, int) or count < 1 or not pack for count, pack in levels):
			raise Exception(f"Experiments: a level of {m['Name']} takes no experiments or an empty pack")

unplaced = [r["Name"] for r in research_objects if r["Class"] == "StaticResearchTechnology" and r["Name"] not in owner]
if unplaced:
	raise Exception(f"Experiments: machine versions on no experiment: {unplaced}")

entries = {m["Name"]: [] for m in experiments}
for m in experiments:
	for research, target in m["Exits"]:
		if research not in m["Researches"] and (research or m["Tree"]):
			raise Exception(f"Experiments: exit {research} of {m['Name']} is not one of its researches")
		if target not in experiment_by_name:
			raise Exception(f"Experiments: exit of {m['Name']} leads to an unknown experiment {target}")
		entries[target].append((m["Name"], research))

roots = [m["Name"] for m in experiments if not entries[m["Name"]]]
if len(roots) != 1:
	raise Exception(f"Experiments: the map needs one root, has {roots}")

boxes = {}
box_of = {}
chunk_heads = set()
for m in experiments:
	parent = {name: up for name, up in m["Tree"]}
	chunks = {name: tuple(d) for name, d in m.get("Chunks", {}).items()}
	for name in chunks:
		if not parent.get(name):
			raise Exception(f"Experiments: chunk {name} of {m['Name']} is not a research hanging in it")
	chunk_heads.update(chunks)

	def top(name):
		while name != m["Head"] and name not in chunks:
			name = parent[name]
		return name

	key_of = lambda head: m["Name"] if head == m["Head"] else m["Name"] + ":" + head
	for head in [m["Head"]] + list(chunks):
		boxes[key_of(head)] = {"Experiment": m["Name"], "Head": head, "Exits": [], "Tree": [[name, "" if name == head else up] for name, up in m["Tree"] if top(name) == head]}
	for name, _ in m["Tree"]:
		box_of[name] = key_of(top(name))
	for head, d in chunks.items():
		boxes[key_of(head)]["Entry"] = (box_of[parent[head]], parent[head], d)
		boxes[box_of[parent[head]]]["Exits"].append((parent[head], d))

def exit_box(experiment, research):
	return box_of[research] if research else experiment

for m in experiments:
	for research, target in m["Exits"]:
		boxes[exit_box(m["Name"], research)]["Exits"].append((research, direction(m["Name"], target)))
	if entries[m["Name"]]:
		source, research = entries[m["Name"]][0]
		boxes[m["Name"]]["Entry"] = (exit_box(source, research), research, axis(direction(source, m["Name"])))

cell_of = {}
origin_x = {}
card_of = {}
paths = {m["Name"]: [] for m in experiments}
node_at = {}
card_at = set()
line_at = set()

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
	carded = key in experiment_by_name
	rows = experiment_by_name[key].get("Rows", tree_rows) if carded else tree_rows
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
		x0 = experiment_by_name[key]["Position"][0] * column_pitch
	anchor_local = add(head_local, scale(e, -reach))
	reserved = through([anchor_local, head_local]) + [(x, head_local[1]) for x in range(cell_columns) if (x - head_local[0]) * e[0] < 0]
	if carded:
		back = add(anchor_local, (e[0], 1)) if e[0] and any(axis(d) == (-e[0], 0) for _, d in box["Exits"]) else None
		reserved += [cell for cell in (add(anchor_local, (dx, dy)) for dx in (-1, 0, 1) for dy in (-1, 0, 1)) if cell != back]
	local_layout = lambda extra: layout({"Name": key, "Tree": box["Tree"], "Head": box["Head"]}, cell_columns, rows, head_local, exit_dirs, reserved + extra) if box["Tree"] else {}
	local = local_layout([])
	above = [(head_local[0], y) for y in range(head_local[1])] if entry and e[0] and not carded else []

	for k in range(1000):
		if k == 1 and above:
			local = local_layout(above)
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
		sides = [through([nodes[research], (gap + d[0], nodes[research][1])]) for research, d in ((research, axis(d)) for research, d in box["Exits"]) if d[0] and research in nodes for gap in [x0 + cell_columns + gap_columns // 2 if d[0] > 0 else x0 - gap_columns // 2 - 1]]
		if fits(set(nodes.values()), cards, line) and not any(cell in node_at or cell in card_at or cell in line_at for side in sides for cell in side):
			break
	else:
		raise Exception(f"Experiments: no room for {key}")

	cell_of.update(nodes)
	origin_x[key] = x0
	if carded:
		card_of[key] = anchor
	if points:
		paths[box["Experiment"]].append(points)
	node_at.update({cell: key for cell in nodes.values()})
	card_at.update(cards)
	line_at.update(line)
	for next_key, next_box in boxes.items():
		if next_box.get("Entry", (None,))[0] == key and next_key not in queue and next_key not in done:
			queue.append(next_key)

if len(done) != len(boxes):
	raise Exception(f"Experiments: not reachable from {roots[0]}: {[key for key in boxes if key not in done]}")

crossing = []
for m in experiments:
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
diagonal = sum(1 for m in experiments for name, up in m["Tree"] if up and abs(cell_of[name][0] - cell_of[up][0]) == 1 and abs(cell_of[name][1] - cell_of[up][1]) == 1)
print(f"Experiments: {len(experiments)} experiments, {sum(len(m['Researches']) for m in experiments)} researches on the grid, {len(outside)} outside, {diagonal} diagonal links")
print(f"Experiments: lines into experiments {sum(n for n, _ in lengths)} cells, longest {lengths[:3]}, crossing {crossing}")

own_lines = sum(1 for m in experiments for name, up in m["Tree"] if up in (research_by_name[name].get("RequiredResearch") or []))
for m in experiments:
	for name, up in m["Tree"]:
		research_by_name[name]["RequiredResearch"] = [up] if up else []
print(f"Experiments: a research opens by its line, {own_lines} of {sum(len(m['Tree']) - 1 for m in experiments)} lines are its own requirement")

experiment_tier = {}
for name in (key for key in done if key in experiment_by_name):
	m = experiment_by_name[name]
	own = sorted(research_by_name[r]["Tier"] for r in m["Researches"])
	experiment_tier[name] = max(own[len(own) // 2:len(own) // 2 + 1] + [m.get("Tier", 0)] + [experiment_tier.get(source, 0) for source, _ in entries[name]])

def price(m, name, floor):
	research = research_by_name[name]
	tier = experiment_tier[m["Name"]]
	cost = max(floor, research["Complexity"])
	research["Tier"] = tier
	research["Complexity"] = cost
	for child, up in m["Tree"]:
		if up == name:
			price(m, child, cost)

for m in experiments:
	if m["Head"]:
		price(m, m["Head"], 0)
	for name in m["Researches"]:
		research_by_name[name]["Complexity"] = round(research_by_name[name]["Complexity"] * tier_cost_mul.get(experiment_tier[m["Name"]], 1))
print(f"Experiments: tiers {experiment_tier}")

objects = []
for m in experiments:
	built = "Build" in m
	objects.append({
		"Class": "StaticExperiment",
		"Name": m["Name"],
		"Label": modifier_by_name[m["Modifier"]]["Label"] if "Modifier" in m else [m["Title"], "researches"] if "Title" in m else research_by_name[m["Label"]]["Label"],
		"Tier": experiment_tier[m["Name"]],
		"Position": m["Position"],
		"Head": m["Head"],
		"Researches": m["Researches"],
		"Layout": [[name, cell_of[name][0], cell_of[name][1], "" if name in chunk_heads else up] for name, up in m["Tree"]],
		"Card": list(card_of[m["Name"]]),
		"Paths": [[list(p) for p in points] for points in paths[m["Name"]]],
		"Exits": m["Exits"],
		"Runs": m["Runs"],
		"Pack": m["Pack"],
		"Recipe": [m["Build"] + "Stage" + r_dict, m["Stage"]] if built else [laboratory["Name"] + r_dict, m["Name"] + "Experiment"] if m["Runs"] else [],
	})
	if "Label" in m:
		objects[-1]["Icon"] = m["Label"]
	if "Image" in m:
		objects[-1]["Image"] = m["Image"]
	if "Levels" in m:
		modifier = modifier_by_name[m["Modifier"]]
		objects[-1].update({
			"Image": modifier["Image"],
			"Modifier": m["Modifier"],
			"BonusValue": m["BonusValue"],
			"Step": m["Step"],
			"Levels": [{
				"Runs": count,
				"Pack": pack,
				"Recipe": [laboratory["Name"] + r_dict, m["Name"] + "Experiment" + str(level + 1)],
			} for level, (count, pack) in enumerate(m["Levels"])],
		})
		del objects[-1]["Head"]
	if built:
		objects[-1]["Build"] = m["Build"]
		del objects[-1]["Head"]

write_file("Generated/Researches/experiments.json", {"Objects": objects})

write_file("Generated/Recipes/laboratory.json", {"Objects": [{
	"Class": r_dict,
	"Name": laboratory["Name"] + r_dict,
	"StartTier": 0,
	"UsedIn": [{"Item": tier_material[laboratory["StartTier"]] + laboratory["Name"], "Tier": laboratory["StartTier"]}],
	"Recipes": [{
		"Name": m["Name"] + "Experiment",
		"Input": items(m["Pack"]),
		"Output": no_items(),
		"Ticks": experiment_ticks,
	} for m in experiments if m["Runs"] and "Build" not in m] + [{
		"Name": m["Name"] + "Experiment" + str(level + 1),
		"Input": items(pack),
		"Output": no_items(),
		"Ticks": experiment_ticks,
	} for m in experiments for level, (count, pack) in enumerate(m.get("Levels", []))],
}]})
