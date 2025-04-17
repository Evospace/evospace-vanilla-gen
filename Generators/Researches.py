from Common import *
from Materials import *
import copy
from NuclearResearches import *
from EquipmentResearches import *
from PartsResearchHelper import *

researches = []

tier_researches = [
	"Error",
	"Error",
	"SteelProduction",
	"AluminiumProduction",
	"StainlessSteelProduction",
	"TitaniumProduction",
	"CompositePlate",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
]

csv = []

def append_levels(research_base):
	mini, maxi = 0, 1
	if "Levels" in research_base:
		mini, maxi = research_base["Levels"][0], research_base["Levels"][1] + 1

	for i in range(mini, maxi):
		this_level = i - mini
		research = copy.deepcopy(research_base)

		research.setdefault("RequiredResearch", [])

		if i != mini:
			research.update({
				"IsUpgrade": True,
				"MainResearch": False,
				"CompleteByDefault": False,
				"Name": research["Name"] + str(this_level),
				"RequiredResearch": [research_base["Name"] + str(this_level - 1)] if i != mini + 1 else [research_base["Name"]],
			})
			research["RequiredResearch"].append(tier_researches[i])

		if "RequiredResearchArr" in research and len(research["RequiredResearchArr"]) > this_level:
			research["RequiredResearch"].extend(research["RequiredResearchArr"][this_level])

		if research.get("MainResearchArr", [False]*maxi)[this_level]:
			research["MainResearch"] = True

		if "Unlocks" in research:
			research["Unlocks"] = [
				[j[0], j[1].replace("%Material%", tier_material[i])]
				for j in research["Unlocks"]
			]

		if "UnlockFirst" in research and this_level == 0:
			research["Unlocks"].extend([j[0], j[1].replace("%Material%", tier_material[i])] for j in research["UnlockFirst"])

		cost_mul = research.get("CostMul", 1)
		if isinstance(cost_mul, list):
			cost_mul = cost_mul[this_level]
		elif "CostMuls" in research:
			cost_mul = research["CostMuls"][this_level]

		cost = research.get("CostExact", tiers_base_cost[i] * cost_mul)

		research.update({
			"Level": this_level,
			"Levels": [i, i],
			"DataPoints": {"Items": [{"Name": "Computations", "Count": cost}]}
		})

		researches.append(research)

		

append_levels({
	"Class": "StaticResearch",
	"Name": "MineralsScan",
	"LabelParts": [["MineralsScan", "researches"]],
	"RequiredResearch": [],
	"Unlocks": [["Hand" + r_dict, tier_material[0] + "Furnace"],["Hand" + r_dict, "SandSurface"],["Hand" + r_dict, "GravelSurface"],["Hand" + r_dict, "Dirt"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearchDecorationUnlock",
	"Name": "BasicPlatform",
	"LabelParts": [["BasicPlatform", "parts"]],
	"RequiredResearch": ["MineralsScan"],
	"Decoration": "BasicPlatform",
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearchDecorationUnlock",
	"Name": "Bricks",
	"LabelParts": [["Bricks", "misc"]],
	"RequiredResearch": ["BasicPlatform"],
	"Decoration": "Bricks",
})
for miscBlock in ["WoodenPlanks", "StoneTiles", "RedTiles", "DarkTiles", "Terracotta", "TerracottaTiles", "RedBricks", "DarkBricks", "TerracottaBricks"]:
	append_levels({
		"Class": "StaticResearchDecorationUnlock",
		"Name": miscBlock,
		"LabelParts": [[miscBlock, "misc"]],
		"RequiredResearch": ["Bricks"],
		"Decoration": miscBlock,
		"Levels": [1,1]
	})
for miscBlock in ["Concrete", "ConcreteBricks", "ConcreteTiles", "ConcreteSmallTiles"]:
	append_levels({
		"Class": "StaticResearchDecorationUnlock",
		"Name": miscBlock,
		"LabelParts": [[miscBlock, "misc"]],
		"RequiredResearch": ["StoneTiles"],
		"Decoration": miscBlock,
		"Levels": [2,2]
	})
for miscBlock in ["ReinforcedConcrete", "ReinforcedConcreteTiles", "ReinforcedConcreteSmallTiles", "ReinforcedConcreteBricks", "DangerBlock"]:
	append_levels({
		"Class": "StaticResearchDecorationUnlock",
		"Name": miscBlock,
		"LabelParts": [[miscBlock, "misc"]],
		"RequiredResearch": ["Concrete"],
		"Decoration": miscBlock,
		"Levels": [3,3]
	})
append_levels({
	"Class": "StaticResearch",
	"Name": "Chest",
	"LabelParts": [["Chest", "blocks"]],
	"RequiredResearch": ["MineralsScan"],
	"Unlocks": [["Hand" + r_dict, "%Material%Chest"] ],
	"Levels":[0,7],
	"CompleteByDefault": True,
	"CostMul": 3,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SingleTypeStorage",
	"LabelParts": [["SingleTypeStorage", "researches"]],
	"RequiredResearch": ["Chest" ],
	"MainResearch": True,
	"Levels":[1,7],
	
	"Unlocks": [["Hand" + r_dict, "%Material%ItemRack"] ],
})
append_levels({
	"Class": "StaticResearchBonusInventory",
	"Name": "InventoryUpgrade",
	"LabelParts": [["InventoryUpgrade", "researches"]],
	"RequiredResearchArr": [["Chest"],["Chest1"],["Chest2"],["Chest3"],["Chest4"],["Chest5"],["Chest6"],[],[],[],[],[],[],[]],
	"Unlocks": [],
	"Levels": [0,7],
	"CostMul": 10,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Electricity",
	"LabelParts": [["Electricity", "researches"]],
	"RequiredResearch": ["MineralsScan"],
	"Unlocks": [["Hand" + r_dict, "CopperConnector"],["Hand" + r_dict, "CopperHandGenerator"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricFurnace",
	"LabelParts": [["ElectricFurnace", "machines"]],
	"Levels": [2,7],
	"RequiredResearch": ["CopperWire", "SteelProduction"],
	"Unlocks": [["Hand" + r_dict, "%Material%ElectricFurnace"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricalSwitch",
	"LabelParts": [["ElectricalSwitch", "machines"]],
	"RequiredResearch": ["CopperWire","SteelProduction"],
	"Unlocks": [["Hand" + r_dict, tier_material[2] + "ElectricalSwitch"]],
	"Levels": [2,2],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Diode",
	"LabelParts": [["Diode", "machines"]],
	
	"RequiredResearch": ["ElectricalSwitch"],
	"Levels": [2,7],
	
	"Unlocks": [["Hand" + r_dict, "%Material%Diode"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PowerGeneration",
	"LabelParts": [["PowerGeneration", "researches"]],
	"RequiredResearch": ["Electricity"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%CompactGenerator"],["Hand" + r_dict, "%Material%StirlingEngine"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SteelProduction",
	"LabelParts": [["SteelProduction", "researches"]],
	"RequiredResearch": ["Oven"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%BlastFurnace"] ] + get_parts_unlocks(tier_material[2]),
	"MainResearch": True,
	"CostMuls": [5, 2.5, 1.5, 1, 1, 1, 1, 1]
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSmelting",
	"LabelParts": [["AdvancedSmelting", "researches"]],
	"RequiredResearch": ["SteelProduction"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%ArcSmelter"] ],
	"MainResearch": True,
	"CostMuls": [4, 2, 1.5, 1, 1, 1, 1, 1, 1]
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SmallSolarPanel",
	"LabelParts": [["SmallSolarPanel", "machines"]],
	"RequiredResearch": ["SiliconWafer"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%SmallSolarPanel"] ],
	"CostMul": 2
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SolarPanel",
	"LabelParts": [["SolarPanel", "machines"]],
	"RequiredResearch": ["SmallSolarPanel"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%SolarPanel"] ],
	"CostMul": 8
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Electrolyzer",
	"LabelParts": [["Electrolyzer", "researches"]],
	"RequiredResearch": ["SteelProduction"], 
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Electrolyzer"] ],
	"MainResearch": True,
	"CostMul": 3
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AluminiumReduction",
	"LabelParts": [["AluminiumReduction", "researches"]],
	"RequiredResearch": ["Electrolyzer"], 
	"Levels": [2,2],
	"Unlocks": [["Electrolyzer" + r_dict, "AluminiumOxideDust"], ["Electrolyzer" + r_dict, "AluminiumOreDust"]],
	"MainResearch": True,
	"CostMul": 2.5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AluminiumProduction",
	"LabelParts": [["AluminiumProduction", "researches"]],
	"RequiredResearch": ["AdvancedSmelting", "AluminiumReduction"],
	"Unlocks": get_parts_unlocks(tier_material[3]) + [["Hand" + r_dict, "AluminiumFoil"],["Assembler" + r_dict, "AluminiumFoil"]],
	"Levels": [3,3],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GasTurbine",
	"LabelParts": [["GasTurbine", "machines"]],
	"RequiredResearch": ["StainlessSteelProduction"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + r_dict, "%Material%GasTurbine"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Smelting",
	"LabelParts": [["Smelting", "researches"]],
	"RequiredResearch": ["MineralsScan"],
	"Unlocks": [["Hand" + r_dict, "%Material%Smelter"]],
	"Levels": [0,2],
	"CompleteByDefault": True,
	"MainResearch": True
})
append_equipment([-1,3], append_levels, researches)
append_levels({
	"Class": "StaticResearch",
	"Name": "Metalwork",
	"LabelParts": [["Metalwork", "researches"]],
	"RequiredResearch": ["Smelting"],
	"Unlocks": get_parts_unlocks(tier_material[1]),
	"Levels": [1,1],
	"CompleteByDefault": True,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Valve",
	"LabelParts": [["Vent", "machines"]],
	"RequiredResearch": ["Metalwork"],
	"Unlocks": [["Hand" + r_dict, tier_material[1] + "Vent"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BasicMachines",
	"LabelParts": [["BasicMachines", "researches"]],
	"RequiredResearch": ["Metalwork"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Macerator"],
	["Hand" + r_dict, "%Material%AutomaticHammer"]],
	"CostMul":0.25,
	"MainResearch": True,
	"Description": [["BasicMachinesDescription", "ui"]]
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Flywheel",
	"LabelParts": [["Flywheel", "machines"]],
	"RequiredResearch": ["BasicMachines", "SteelProduction"],
	"Unlocks": [["Hand" + r_dict, tier_material[2] + "Flywheel"]],
	"Levels": [2,2],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Destroyer",
	"LabelParts": [["Destroyer", "machines"]],
	"Levels": [1,7],
	"RequiredResearch": ["Furnace"],
	"Unlocks": [["Hand" + r_dict, "%Material%Destroyer"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Pump",
	"LabelParts": [["Pump", "machines"]],
	"RequiredResearch": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Pump"] ],
	"CostMul":0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Container",
	"LabelParts": [["Container", "machines"]],
	"RequiredResearchArr": [["Chest"],["Chest1"],["Chest2"],["Chest3"],["Chest4"],["Chest5"],["Chest6"],[],[],[],[],[],[],[]],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Container"] ],
	"MainResearch": True,
	"CostMul": 3,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FluidFurnace",
	"LabelParts": [["FluidFurnace", "machines"]],
	"RequiredResearch": ["Furnace"],
	"Unlocks": [["Hand" + r_dict, "%Material%FluidFurnace"] ],
	"Levels": [1,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Automatization",
	"LabelParts": [["Automatization", "researches"]],
	"RequiredResearch": ["BasicMachines"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%RobotArm"], ["Hand" + r_dict, "%Material%Conveyor"], ["Hand" + r_dict, "%Material%Splitter"]],
	"CostMul":0.25,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sorter",
	"LabelParts": [["Sorter", "machines"]],
	"RequiredResearch": ["Automatization1"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Sorter"]],
	"CostMul": 3,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OverflowPump",
	"LabelParts": [["OverflowPump", "machines"]],
	"RequiredResearch": ["Pump"],
	"Unlocks": [["Hand" + r_dict, "%Material%OverflowPump"]],
	"Levels": [1,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AutomaticMining",
	"LabelParts": [["AutomaticMining", "researches"]],
	"RequiredResearch": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%DrillingRig"] ],
	"CostMuls":[0.5, 0.75, 2.0, 3.0, 4.0, 5.0, 6.0],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Pumpjack",
	"LabelParts": [["Pumpjack", "machines"]],
	"RequiredResearch": ["AutomaticMining"],
	"Unlocks": [["Hand" + r_dict, "%Material%Pumpjack"] ],
	"Levels": [3,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AutomaticFarm",
	"LabelParts": [["AutomaticFarm", "machines"]],
	"RequiredResearch": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%AutomaticFarm"] ],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HeatTransferring",
	"LabelParts": [["HeatTransferring", "researches"]],
	"RequiredResearch": ["Smelting"],
	"Unlocks": [["Hand" + r_dict, "%Material%HeatPipe"] ],
	"Levels":[1,1],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "KineticHeater",
	"LabelParts": [["KineticHeater", "machines"]],
	"RequiredResearch": ["HeatTransferring"],
	"Unlocks": [["Hand" + r_dict, "%Material%KineticHeater"] ],
	"Levels":[1,7],
	"CostMul":1,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Radiator",
	"LabelParts": [["Radiator", "machines"]],
	"RequiredResearch": ["HeatTransferring"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Radiator"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AtmosphericCondenser",
	"LabelParts": [["AtmosphericCondenser", "machines"]],
	"RequiredResearch": ["AutomaticFarm"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%AtmosphericCondenser"] ],
	"CostMul":0.5,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Oven",
	"LabelParts": [["Oven", "researches"]],
	"RequiredResearch": ["Furnace",],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Oven"] ],
	"MainResearch": True,
	"CostMul":3,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DistributedComputing",
	"LabelParts": [["DistributedComputing", "researches"]],
	"RequiredResearchArr": [["PowerGeneration"], ["AdvancedCircuit"], ["Processor"], ["QuantumCircuit"], ["QuantumProcessor"], ["QuantumBrain"]],
	"Unlocks": [["Hand" + r_dict, "%Material%Computer"] ],
	"Levels": [1,7],
	"CompleteByDefault": True,
	"MainResearchArr": [True,True,True,True,True,True,True],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CopperWire",
	"LabelParts": [["CopperWire", "parts"]],
	"RequiredResearch": ["DistributedComputing"],
	"Levels": [1,1],
	"Unlocks": [["Hand" + r_dict, "CopperWire"],[assembler_r_dict, "CopperWire"]],
	"CompleteByDefault": True,
	"MainResearch": True,
	"CostMul": 0.125
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CircuitBoard",
	"LabelParts": [["CircuitBoard", "parts"]],
	"RequiredResearch": ["CopperWire"],
	"Levels": [1,1],
	"Unlocks": [["Hand" + r_dict, "CircuitBoard"]],
	"CostMul":0.3,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Triod",
	"LabelParts": [["Triod", "parts"]],
	"RequiredResearch": ["CircuitBoard"],
	"Unlocks": [["Hand" + r_dict, "Triod"],[assembler_r_dict, "Triod"]],
	"Levels": [1,1],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Circuit",
	"LabelParts": [["Circuit", "parts"]],
	"RequiredResearch": ["Triod"],
	"Unlocks": [["Hand" + r_dict, "Circuit"],[assembler_r_dict, "Circuit"]],
	"Levels": [1,1],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Circuit2",
	"LabelParts": [["Circuit", "parts"], ["II", "common"]],
	"RequiredResearch": ["Circuit", "Transistor"],
	"Unlocks": [[assembler_r_dict, "Circuit2"]],
	"Levels": [1,1],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Furnace",
	"LabelParts": [["Furnace", "machines"]],
	"RequiredResearch": ["PowerGeneration"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Furnace"] ],
	"MainResearchArr": [True,True,True,True,True,True,True],
	"CostMul": 2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Boiler",
	"LabelParts": [["Boiler", "machines"]],
	"RequiredResearch": ["PowerGeneration", "SteelProduction"],
	"Unlocks": [["Hand" + r_dict, "%Material%Boiler"]],
	"Levels": [2,7],
	"MainResearchArr": [True,True,False,False,False,False,False],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SteamEngine",
	"LabelParts": [["SteamEngine", "machines"]],
	"RequiredResearch": ["Boiler"],
	"Unlocks": [["Hand" + r_dict, "%Material%SteamEngine"]],
	"Levels": [2,7],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "LogicCircuit",
	"LabelParts": [["LogicCircuit", "machines"]],
	"RequiredResearch": ["Circuit"],
	"Unlocks": [["Hand" + r_dict, "SteelLogicCircuit"] ,
	["Hand" + r_dict, "SteelLogicController"] ,
	["Hand" + r_dict, "SteelLogicInterface"] ,
	["Hand" + r_dict, "SteelLogicDisplay"] ,
	["Hand" + r_dict, "SteelLogicWire"] ],
	"Levels": [2,2],
	"CostMul": 1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Resistor",
	"LabelParts": [["Resistor", "parts"]],
	"RequiredResearch": ["Circuit"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + r_dict, "Resistor"],[assembler_r_dict, "Resistor2"]],
	"MainResearch": True,
	"CostMul":1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Resistor2",
	"LabelParts": [["Resistor", "parts"], ["II", "common"]],
	"RequiredResearch": ["Resistor", "Polyethylene"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "Resistor3"]],
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Resistor3",
	"LabelParts": [["Resistor", "parts"], ["III", "common"]],
	"RequiredResearch": ["Resistor2", "Tetrafluoroethylene", "CrudeNiobium"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "Resistor4"]],
	"CostMul":4.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Resistor4",
	"LabelParts": [["Resistor", "parts"], ["IV", "common"]],
	"RequiredResearch": ["Resistor3", "TantalumDust"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "Resistor5"]],
	"CostMul":8.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedCircuit",
	"LabelParts": [["AdvancedCircuit", "parts"]],
	"RequiredResearch": ["Separator", "Resistor"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + r_dict, "AdvancedCircuit"],[assembler_r_dict, "AdvancedCircuit"]],
	"CostMul":1.6,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Transistor",
	"LabelParts": [["Transistor", "parts"]],
	"RequiredResearch": ["AdvancedCircuit"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + r_dict, "Transistor"],[assembler_r_dict, "Transistor"]],
	"MainResearch": True,
	"CostMul":3.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Transistor2",
	"LabelParts": [["Transistor", "parts"], ["II", "common"]],
	"RequiredResearch": ["Transistor", "Polyethylene"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "Transistor2"]],
	"CostMul":6.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Transistor3",
	"LabelParts": [["Transistor", "parts"], ["III", "common"]],
	"RequiredResearch": ["Transistor2"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "Transistor3"]],
	"CostMul":12.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Transistor4",
	"LabelParts": [["Transistor", "parts"], ["IV", "common"]],
	"RequiredResearch": ["Transistor3", "DopedSiliconWafer"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "Transistor4"]],
	"CostExact": 4*10**6,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedCircuit2",
	"LabelParts": [["AdvancedCircuit", "parts"], ["II", "common"]],
	"RequiredResearch": ["Transistor"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "AdvancedCircuit2"]],
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SiliconWafer",
	"LabelParts": [["SiliconWafer", "parts"]],
	"RequiredResearch": ["AdvancedCircuit"],
	"Unlocks": [["IndustrialSmelter"+r_dict, "SiliconMonocrystal"],[assembler_r_dict, "SiliconWafer"]],
	"Levels": [3,3],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DopedSiliconWafer",
	"LabelParts": [["DopedSiliconWafer", "parts"]],
	"RequiredResearch": ["SiliconWafer", "PlatinumRhodiumSolution"],
	"Unlocks": [["IndustrialSmelter"+r_dict, "DopedSiliconMonocrystal"],[assembler_r_dict, "DopedSiliconWafer"]],
	"Levels": [6,6]
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Processor",
	"LabelParts": [["Processor", "parts"]],
	"RequiredResearch": ["SiliconWafer"],
	"Unlocks": [["Hand" + r_dict, "Processor"]],
	"Levels": [3,3],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Capacitor",
	"LabelParts": [["Capacitor", "parts"]],
	"RequiredResearch": ["Processor"],
	"Levels": [3,3],
	"Unlocks": [["Hand" + r_dict, "Capacitor"]],
	"MainResearch": True,
	"CostMul":1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Capacitor2",
	"LabelParts": [["Capacitor", "parts"], ["II", "common"]],
	"RequiredResearch": ["Capacitor"],
	"Levels": [3,3],
	"Unlocks": [[assembler_r_dict, "Capacitor2"]],
	"CostMul":3,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Capacitor3",
	"LabelParts": [["Capacitor", "parts"], ["III", "common"]],
	"RequiredResearch": ["Capacitor2", "Polyethylene", "TantalumDust"],
	"Levels": [3,3],
	"Unlocks": [[assembler_r_dict, "Capacitor3"]],
	"CostMul":6,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Capacitor4",
	"LabelParts": [["Capacitor", "parts"], ["IV", "common"]],
	"RequiredResearch": ["Capacitor3", "Tetrafluoroethylene"],
	"Levels": [3,3],
	"Unlocks": [[assembler_r_dict, "Capacitor4"]],
	"CostMul":12,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Processor2",
	"LabelParts": [["Processor", "parts"], ["II", "common"]],
	"RequiredResearch": ["Capacitor"],
	"Unlocks": [[assembler_r_dict, "Processor2"]],
	"Levels": [3,3],
	"MainResearch": True,
	"CostMul":4,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Processor3",
	"LabelParts": [["Processor", "parts"], ["III", "common"]],
	"RequiredResearch": ["Processor2", "DopedSiliconWafer"],
	"Unlocks": [[assembler_r_dict, "Processor3"]],
	"Levels": [3,3],
	"CostExact": 4*10**6,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sulfur",
	"LabelParts": [["SulfurSynthesis", "researches"]],
	"RequiredResearch": ["IndustrialChemReactor", "PyrolysisUnit"],
	"Levels": [4,4],
	"Unlocks": [["IndustrialChemReactor" + r_dict, "Sulfur"]],
	"MainResearch": True,
	"CostMul": 0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SulfuricAcid",
	"LabelParts": [["SulfuricAcidSynthesis", "researches"]],
	"RequiredResearch": ["Sulfur", "Catalyst"],
	"Levels": [4,4],
	"Unlocks": [["IndustrialChemReactor" + r_dict, "SulfuricAcid"]],
	"MainResearch": True,
	"CostMul": 0.75,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BasicBattery",
	"LabelParts": [["BasicBattery", "parts"]],
	"RequiredResearch": ["Battery", "BatteryBox"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "BasicBattery"],["Hand" + r_dict, "BasicBattery"]],
	"MainResearch": True,
	"CostMul": 0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedBattery",
	"LabelParts": [["AdvancedBattery", "parts"]],
	"RequiredResearch": ["BasicBattery"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "AdvancedBattery"],["Hand" + r_dict, "AdvancedBattery"]],
	"CostMul": 4,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SuperiorBattery",
	"LabelParts": [["SuperiorBattery", "parts"]],
	"RequiredResearch": ["AdvancedBattery"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "SuperiorBattery"],["Hand" + r_dict, "SuperiorBattery"]],
	"CostMul": 8,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "UltimateBattery",
	"LabelParts": [["UltimateBattery", "parts"]],
	"RequiredResearch": ["SuperiorBattery"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "UltimateBattery"],["Hand" + r_dict, "UltimateBattery"]],
	"CostMul": 16,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Battery",
	"LabelParts": [["Battery", "parts"]],
	"RequiredResearch": ["SulfuricAcid"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "Battery"],["Hand" + r_dict, "Battery"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "NitricAcid",
	"LabelParts": [["NitricAcid", "parts"]],
	"RequiredResearch": ["IndustrialChemReactor1"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "NitricAcid"]],
	"CostMul": 0.2,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HydrochloricAcid",
	"LabelParts": [["HydrochloricAcid", "parts"]],
	"RequiredResearch": ["NitricAcid"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "HydrochloricAcid"]],
	"CostMul": 0.4,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AquaRegia",
	"LabelParts": [["AquaRegia", "parts"]],
	"RequiredResearch": ["HydrochloricAcid"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "AquaRegia"]],
	"CostMul": 0.8,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PlatinumRhodiumSolution",
	"LabelParts": [["PlatinumRhodiumSolution", "parts"]],
	"RequiredResearch": ["AquaRegia"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "PlatinumRhodiumSolution"],[ic_reactor_r_dict, "AmmoniumChloride"],[ic_reactor_r_dict, "RhodiumSolution"]],
	"CostMul": 1.2,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "RhodiumDust",
	"LabelParts": [["RhodiumDust", "parts"]],
	"RequiredResearch": ["AdvancedCatalyst"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "RhodiumDust"], [ic_reactor_r_dict,"MesitylOxide"], 
			 [ic_reactor_r_dict, "MethylIsobutylKetone"], [assembler_r_dict, "RhodiumFoil"]],
	"CostMul": 3.0,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "RhodiumReflector",
	"LabelParts": [["RhodiumReflector", "parts"]],
	"RequiredResearch": ["RhodiumDust"],
	"Levels": [5,5],
	"Unlocks": [[h_r_dict, "RhodiumReflector"], [assembler_r_dict, "RhodiumReflector"]],
	"CostMul": 6,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "RareEarthSludge",
	"LabelParts": [["RareEarthSludge", "parts"]],
	"RequiredResearch": ["SulfuricAcid"],
	"Levels": [4,4],
	"Unlocks": [["ChemicalBath" + r_dict, "RareEarthSludge"]],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumCore",
	"LabelParts": [["QuantumCore", "parts"]],
	"RequiredResearch": ["Processor", "RareEarthSludge"],
	"Levels": [4,4],
	"Unlocks": [["Hand" + r_dict, "QuantumCore"],[assembler_r_dict, "QuantumCore"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumCircuit",
	"LabelParts": [["QuantumCircuit", "parts"]],
	"RequiredResearch": ["QuantumCore"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + r_dict, "QuantumCircuit"],[assembler_r_dict, "QuantumCircuit"]],
	"MainResearch": True,
	"CostMul": 0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecisionResonator",
	"LabelParts": [["DecisionResonator", "parts"]],
	"RequiredResearch": ["QuantumCircuit"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + r_dict, "DecisionResonator"]],
	"MainResearch": True,
	"CostMul":0.75,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecisionResonator2",
	"LabelParts": [["DecisionResonator", "parts"], ["II", "common"]],
	"RequiredResearch": ["DecisionResonator"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "DecisionResonator2"]],
	"CostMul":1.0,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecisionResonator3",
	"LabelParts": [["DecisionResonator", "parts"], ["III", "common"]],
	"RequiredResearch": ["DecisionResonator2"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "DecisionResonator3"]],
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecisionResonator4",
	"LabelParts": [["DecisionResonator", "parts"], ["IV", "common"]],
	"RequiredResearch": ["DecisionResonator3", "DopedSiliconWafer"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "DecisionResonator4"]],
	"CostMul":5.0,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumProcessor",
	"LabelParts": [["QuantumProcessor", "parts"]],
	"RequiredResearch": ["DecisionResonator"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + r_dict, "QuantumProcessor"],[assembler_r_dict, "QuantumProcessor"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BrainMatrix",
	"LabelParts": [["BrainMatrix", "parts"]],
	"RequiredResearch": ["QuantumProcessor"],
	"Levels": [6,6],
	"Unlocks": [["Hand" + r_dict, "BrainMatrix"]],
	"MainResearch": True,
	"CostMul":1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumBrain",
	"LabelParts": [["QuantumBrain", "parts"]],
	"RequiredResearch": ["BrainMatrix"],
	"Levels": [6,6],
	"Unlocks": [["Hand" + r_dict, "QuantumBrain"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumBrain2",
	"LabelParts": [["QuantumBrain", "parts"],["II", "common"]],
	"RequiredResearch": ["QuantumBrain", "UltimateCatalyst"],
	"Levels": [6,6],
	"Unlocks": [[assembler_r_dict, "QuantumBrain2"]],
	"MainResearch": True,
	"CostMul":5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "MetalConstructions",
	"LabelParts": [["MetalConstructions", "researches"]],
	"RequiredResearch": ["Bricks"],
	"Unlocks": [["Hand" + r_dict, "%Material%Corner"],
	["Hand" + r_dict, "%Material%Beam"]],
	"Levels": [1,7],
	"Chapter":"Decorations"+static_chapter,
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Scaffold",
	"LabelParts": [["Scaffold", "researches"]],
	"RequiredResearch": ["MetalConstructions"],
	"Unlocks": [["Hand" + r_dict, "%Material%Scaffold"] ],
	"Levels": [1,7],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialChemReactor",
	"LabelParts": [["IndustrialChemReactor", "machines"]],
	"RequiredResearch": ["ElectricEngine"],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialChemReactor"] ],
	"Levels": [3,7],
	"MainResearchArr": [True, True, False, False, False, False],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Catalyst",
	"LabelParts": [["Catalyst", "parts"]],
	"RequiredResearch": ["IndustrialChemReactor"],
	"Unlocks": [["Hand" + r_dict, "Catalyst"],[assembler_r_dict, "Catalyst"]],
	"Levels": [4,4],
	"MainResearch": True,
	"CostMul":1,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Catalyst2",
	"LabelParts": [["Catalyst", "parts"],["II", "common"]],
	"RequiredResearch": ["Catalyst"],
	"Unlocks": [[assembler_r_dict, "Catalyst2"]],
	"Levels": [4,4],
	"CostMul":1.5,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedCatalyst",
	"LabelParts": [["AdvancedCatalyst", "parts"]],
	"RequiredResearch": ["Catalyst2", "PlatinumRhodiumSolution"],
	"Unlocks": [[assembler_r_dict, "AdvancedCatalyst"]],
	"Levels": [6,6],
	"CostMul": 1.75,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FuelChemistry",
	"LabelParts": [["FuelChemistry", "researches"]],
	"RequiredResearch": ["Catalyst"],
	"Unlocks": [["IndustrialChemReactor" + r_dict, "Superfuel"], ["IndustrialChemReactor" + r_dict, "RocketFuel"]],
	"Levels": [3,3],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FuelChemistry2",
	"LabelParts": [["FuelChemistry2", "researches"]],
	"RequiredResearch": ["FuelChemistry"],
	"Unlocks": [["IndustrialChemReactor" + r_dict, "RocketFuel2"], ["IndustrialChemReactor" + r_dict, "Superfuel2"]],
	"Levels": [3,3],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sifter",
	"LabelParts": [["Sifter", "machines"]],
	"RequiredResearch": ["ElectricEngine"],
	"Unlocks": [["Hand" + r_dict, "%Material%Sifter"] ],
	"Levels": [3,7],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Separator",
	"LabelParts": [["Separator", "machines"]],
	"RequiredResearch": ["ElectricEngine"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Separator"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricEngine",
	"LabelParts": [["ElectricEngine", "machines"]],
	"RequiredResearch": ["SteelProduction"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%ElectricEngine"] ],
	"MainResearchArr": [True, True, False, False, False, False, False],
	"CostMul": 2,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Generator",
	"LabelParts": [["Generator", "machines"]],
	"RequiredResearch": ["ElectricEngine1"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Generator"]],
	"UnlockFirst": [["Hand" + r_dict, "SCable"]],
	"MainResearchArr": [True, False, False, False, False, False, False],
	"CostMul": 2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GoldCable",
	"LabelParts": [["GoldCable", "parts"]],
	"RequiredResearch": ["Generator"],
	"Levels": [3,3],
	"Unlocks": [[h_r_dict, "GCable"]],
	"MainResearch": True,
	"CostMul": 4,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AluminiumCable",
	"LabelParts": [["GoldCable", "parts"]],
	"RequiredResearch": ["GoldCable"],
	"Levels": [3,3],
	"Unlocks": [[h_r_dict, "ACable"]],
	"MainResearch": True,
	"CostMul": 8,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SteamTurbine",
	"LabelParts": [["SteamTurbine", "machines"]],
	"RequiredResearch": ["Generator", "Boiler1"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%SteamTurbine"] ],
	"MainResearchArr": [True, False, False, False, False, False, False],
	"CostMul": 1.0,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Transformer",
	"LabelParts": [["TransformerLVMV", "machines"]],
	"RequiredResearch": ["Generator"],
	"Levels": [3,3],
	"Unlocks": [["Hand" + r_dict, "TransformerLVMV"]],
	"MainResearchArr": [True, False, False, False, False, False, False],
	"CostMul": 1.5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BiElectricEngine",
	"LabelParts": [["BiElectricEngine", "machines"]],
	"RequiredResearch": ["ElectricEngine"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%BiElectricEngine"] ],
	"CostMul": 4
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OreWasher",
	"LabelParts": [["OreWasher", "machines"]],
	"Levels": [2,7],
	"RequiredResearch": ["Separator"],
	"Unlocks": [["Hand" + r_dict, "%Material%OreWasher"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Mixer",
	"LabelParts": [["Mixer", "machines"]],
	"RequiredResearch": ["OreWasher", "Electrolyzer"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Mixer"] ],
	"MainResearch": True,
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ChemicalBath",
	"LabelParts": [["ChemicalBath", "machines"]],
	"RequiredResearch": ["IndustrialChemReactor"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%ChemicalBath"] ],
	"MainResearch": True,
	"CostMul":5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OilCrackingTower",
	"LabelParts": [["OilCrackingTower", "machines"]],
	"RequiredResearch": ["FuelChemistry"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + r_dict, "%Material%OilCrackingTower"] ],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CombustionEngine",
	"LabelParts": [["CombustionEngine", "machines"]],
	"RequiredResearch": ["Catalyst"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%CombustionEngine"] ],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedAlloys",
	"LabelParts": [["AdvancedAlloys", "researches"]],
	"RequiredResearch": ["Mixer", "AluminiumProduction", "Separator"],
	"Unlocks": [["Mixer" + r_dict, "SSCraft"],["Mixer" + r_dict, "SSCraft2"]],
	"Levels": [4,4],
	"MainResearch": True,
	"CostMul": 0.5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "StainlessSteelProduction",
	"LabelParts": [["StainlessSteelProduction", "researches"]],
	"RequiredResearch": ["AdvancedAlloys"],
	"Unlocks": get_parts_unlocks(tier_material[4]) + [["Hand" + r_dict, "Cell"]],
	"Levels": [4,4],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BatteryBox",
	"LabelParts": [["BatteryBox", "machines"]],
	"RequiredResearch": ["AluminiumProduction"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%BatteryBox"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PrimitiveBattery",
	"LabelParts": [["PrimitiveBattery", "parts"]],
	"RequiredResearch": ["BatteryBox"],
	"Levels": [3,3],
	"Unlocks": [[assembler_r_dict, "PrimitiveBattery"],["Hand" + r_dict, "PrimitiveBattery"]],
	"CostMul": 2,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CarbonFiber",
	"LabelParts": [["CarbonFiber", "parts"]],
	"RequiredResearch": ["PyrolysisUnit", "IndustrialChemReactor1"],
	"Unlocks": [["PyrolysisUnit"+r_dict,"CarbonFiber"]],
	"Levels": [5,5],
	"MainResearch": True,
	"CostMul": 0.3,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CarbonFiberSheet",
	"LabelParts": [["CarbonFiberSheet", "parts"]],
	"RequiredResearch": ["CarbonFiber"],
	"Unlocks": [["Hand"+r_dict,"CarbonFiberSheet"]],
	"Levels": [5,5],
	"MainResearch": True,
	"CostMul": 0.6,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "KrollProcess",
	"LabelParts": [["KrollProcess", "researches"]],
	"RequiredResearch": ["IndustrialSmelting"],
	"Unlocks": [["IndustrialSmelter"+r_dict,"SpongeToPlate"],["IndustrialChemReactor" + r_dict, "TitaniumSponge"],["IndustrialChemReactor" + r_dict, "TitaniumTetrachloride"]],
	"Levels": [5,5],
	"MainResearch": True,
	"CostMul": 0.5,
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "TitaniumProduction",
	"LabelParts": [["TitaniumProduction", "researches"]],
	"RequiredResearch": ["KrollProcess"],
	"Unlocks": get_parts_unlocks(tier_material[5]),
	"Levels": [5,5],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialBoiler",
	"LabelParts": [["IndustrialBoiler", "machines"]],
	"RequiredResearch": ["TitaniumProduction"],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialBoiler"],["Connector" + r_dict, "%Material%IndustrialBoiler"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialSteamTurbine",
	"LabelParts": [["IndustrialSteamTurbine", "machines"]],
	"RequiredResearch": ["IndustrialBoiler"],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialSteamTurbine"],["Connector" + r_dict, "%Material%IndustrialSteamTurbine"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialGenerator",
	"LabelParts": [["IndustrialGenerator", "machines"]],
	"RequiredResearch": ["IndustrialSteamTurbine"],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialGenerator"],["Connector" + r_dict, "%Material%IndustrialGenerator"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Polyethylene",
	"LabelParts": [["PolyethyleneSheet", "parts"]],
	"RequiredResearch": ["IndustrialChemReactor"],
	"Levels": [4,4],
	"Unlocks": [[ic_reactor_r_dict, "PolyethyleneSheet"]],
	"MainResearch": True,
	"CostMul": 1.25
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Tetrafluoroethylene",
	"LabelParts": [["Tetrafluoroethylene", "parts"]],
	"RequiredResearch": ["Polyethylene"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "PolytetrafluoroethyleneSheet"], ["PyrolysisUnit"+r_dict, "Tetrafluoroethylene"], [ic_reactor_r_dict, "Chlorodifluoromethane"], [ic_reactor_r_dict, "Chloroform"]],
	"MainResearch": True,
	"CostMul": 2.25
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CrudeNiobium",
	"LabelParts": [["CrudeNiobium", "researches"]],
	"RequiredResearch": ["Tetrafluoroethylene"],
	"Levels": [5,5],
	"Unlocks": [["IndustrialSmelter" + r_dict, "TantalumSludge"], [h_r_dict, "NiobiumWire"]],
	"CostMul": 5.5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "NiobiumDust",
	"LabelParts": [["NiobiumDust", "parts"]],
	"RequiredResearch": ["CrudeNiobium"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "TantalumSludge2"], [assembler_r_dict, "NiobiumWire2"]],
	"CostMul": 7
})
append_levels({
	"Class": "StaticResearch",
	"Name": "TantalumDust",
	"LabelParts": [["TantalumDust", "parts"]],
	"RequiredResearch": ["NiobiumDust"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "TantalumSolution"], [assembler_r_dict, "TantalumWire2"], [assembler_r_dict, "TantalumFoil"],
			 [h_r_dict, "TantalumWire"], [h_r_dict, "TantalumFoil"]],
	"CostMul": 9
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Tetrafluoroethylene2",
	"LabelParts": [["Tetrafluoroethylene", "parts"], ["II", "common"]],
	"RequiredResearch": ["Tetrafluoroethylene"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "Chlorodifluoromethane2"]],
	"MainResearch": True,
	"CostMul": 8
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CompositePlate",
	"LabelParts": [["CompositePlate", "parts"]],
	"RequiredResearch": ["TitaniumProduction", "CarbonFiberSheet", "Tetrafluoroethylene"],
	"Levels": [6,6],
	"Unlocks": [[assembler_r_dict, "CompositePlate"]],
	"MainResearch": True,
	"CostMul": 2.25
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CompositePlate2",
	"LabelParts": [["CompositePlate", "parts"], ["II", "common"]],
	"RequiredResearch": ["CompositePlate", "Polythetrafluoroethylene"],
	"Levels": [6,6],
	"Unlocks": [[assembler_r_dict, "CompositePlate2"]],
	"MainResearch": True,
	"CostMul": 5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FusionReactor",
	"LabelParts": [["FusionReactor", "machines"]],
	"RequiredResearch": ["CompositePlate", "RhodiumReflector"],
	"Unlocks": [["Hand" + r_dict, "%Material%FusionReactor"] ],
	"Levels": [6,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "NeutroniumProduction",
	"LabelParts": [["NeutroniumProduction", "researches"]],
	"RequiredResearch": ["FusionReactor"],
	"Unlocks": get_parts_unlocks(tier_material[7]),
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "UltimateCatalyst",
	"LabelParts": [["UltimateCatalyst", "parts"]],
	"RequiredResearch": ["NeutroniumProduction"],
	"Unlocks": [["Hand" + r_dict, "UltimateCatalyst"],[assembler_r_dict, "UltimateCatalyst"]],
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	 "Class": "StaticResearch",
	 "Name": "Portal",
	 "LabelParts": [["Portal", "machines"]],
	 "RequiredResearch": ["UltimateCatalyst", "QuantumBrain"],
	 "Unlocks": [["Hand" + r_dict, "%Material%Portal"] ],
	 "Levels": [7,7],
	 "MainResearch": True,
	 "CostMul": 5
 })
append_levels({
	"Class": "StaticResearch",
	"Name": "FissionReactor",
	"LabelParts": [["FissionReactor", "machines"]],
	"RequiredResearch": ["UraniumCell"],
	"Levels": [5,7],
	"Unlocks": [["Hand" + r_dict, "%Material%FissionReactor"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "UraniumCell",
	"LabelParts": [["UraniumCell", "parts"]],
	"RequiredResearch": ["TitaniumProduction"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + r_dict, "UraniumCell"],[assembler_r_dict, "UraniumCell"]],
})
append_nuclear([7,-7], append_levels, researches)
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialSmelting",
	"LabelParts": [["IndustrialSmelting", "researches"]],
	"RequiredResearch": ["StainlessSteelProduction"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialSmelter"] ],
	"MainResearch": True,
	"CostMul":5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fermentation",
	"LabelParts": [["Fermentation", "researches"]],
	"Levels": [3,7],
	"RequiredResearch": ["ElectricEngine"],
	"Unlocks": [["Hand" + r_dict, "%Material%Fermenter"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "InductionCoil",
	"LabelParts": [["InductionCoil", "machines"]],
	"RequiredResearch": ["IndustrialSmelting"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + r_dict, "%Material%InductionCoil"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialElectricEngine",
	"LabelParts": [["IndustrialElectricEngine", "machines"]],
	"RequiredResearch": ["InductionCoil"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialElectricEngine"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Terminal",
	"LabelParts": [["Terminal", "machines"]],
	"Levels": [4,4],
	"RequiredResearch": ["StainlessSteelProduction"],
	"Unlocks": [["Hand" + r_dict, tier_material[4] + "Terminal"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FlatTerminal",
	"LabelParts": [["FlatTerminal", "machines"]],
	"Levels": [4,4],
	"RequiredResearch": ["Terminal"],
	"Unlocks": [["Hand" + r_dict, tier_material[4] + "FlatTerminal"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Assembler",
	"LabelParts": [["Assembler", "machines"]],
	"RequiredResearch": ["AdvancedCircuit"],
	"Unlocks": [["Hand" + r_dict, "%Material%Assembler"]],
	"Levels": [3,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Constructor",
	"LabelParts": [["Constructor", "machines"]],
	"RequiredResearch": ["Automatization"],
	"Unlocks": [["Hand" + r_dict, "%Material%Constructor"]],
	"Levels": [1, 7],
	"CostMul": 0.5,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BigTerminal",
	"LabelParts": [["BigTerminal", "machines"]],
	"RequiredResearch": ["Terminal"],
	"Unlocks": [["Hand" + r_dict, tier_material[5] + "BigTerminal"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BigFlatTerminal",
	"LabelParts": [["BigFlatTerminal", "machines"]],
	"RequiredResearch": ["BigTerminal"],
	"Unlocks": [["Hand" + r_dict, tier_material[5] + "BigFlatTerminal"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HugeTerminal",
	"LabelParts": [["HugeTerminal", "machines"]],
	"RequiredResearch": ["BigTerminal"],
	"Unlocks": [["Hand" + r_dict, tier_material[6] + "HugeTerminal"]],
	"Levels": [5,5],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HugeFlatTerminal",
	"LabelParts": [["HugeFlatTerminal", "machines"]],
	"RequiredResearch": ["HugeTerminal"],
	"Unlocks": [["Hand" + r_dict, tier_material[6] + "HugeFlatTerminal"]],
	"Levels": [5,5],
}) 
append_levels({
	"Class": "StaticResearch",
	"Name": "PyrolysisUnit",
	"LabelParts": [["PyrolysisUnit", "machines"]],
	"RequiredResearch": ["Mixer"],
	"Unlocks": [["Hand" + r_dict, "%Material%PyrolysisUnit"] ],
	"Levels": [3,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PreciseTemperaturePyrolysis",
	"LabelParts": [["PreciseTemperaturePyrolysis", "researches"]],
	"RequiredResearch": ["PyrolysisUnit"],
	"Unlocks": [["PyrolysisUnit" + r_dict, "RawOil"]],
	"Levels": [4,4]
})	
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood",
	"RequiredResearch": ["Bricks"],
	"LabelParts": [["DecorativeWood", "researches"]],
	"Unlocks": [["Hand" + r_dict, "WoodenPlanks"],["Hand" + r_dict, "WoodenStairs"],["Hand" + r_dict, "Bed"],["Hand" + r_dict, "Door"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood2",
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[1], "common"]],
	"RequiredResearch": ["DecorativeWood"],
	"Unlocks": [["Hand" + r_dict, "Chair"],["Hand" + r_dict, "Fence"],["Hand" + r_dict, "Ladder"],["Hand" + r_dict, "Rack"],["Hand" + r_dict, "Table"]],
	"Levels": [2,2],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fence",
	"LabelParts": [["Fence", "misc"]],
	"RequiredResearch": ["DecorativeWood2"],
	"Unlocks": [["Hand" + r_dict, "SteelFence"]],
	"Levels": [2,2],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fence1",
	"LabelParts": [["Fence", "misc"], [level_labels[1], "common"]],
	"RequiredResearch": ["Fence"],
	"Unlocks": [["Hand" + r_dict, "StainlessSteelFence"]],
	"Levels": [3,3],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood4",
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[3], "common"]],
	"RequiredResearch": ["DecorativeWood2"],
	"Unlocks": [["Hand" + r_dict, "CopperChair"]],
	"Levels": [3,3],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood3",
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[2], "common"]],
	"RequiredResearch": ["DecorativeWood2", "AdvancedSmelting"],
	"Unlocks": [["Hand" + r_dict, "Window"]],
	"Levels": [3,3],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativePlastic",
	"LabelParts": [["DecorativePlastic", "researches"]],
	"RequiredResearch": ["IndustrialChemReactor", "PyrolysisUnit", "DecorativeWood3"],
	"Unlocks": [["Hand" + r_dict, "PlasticWindow"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Lamp",
	"LabelParts": [["Lamp", "machines"]],
	"RequiredResearch": [],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Lamp"] ],
	"CostMul": 0.1,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sign",
	"LabelParts": [["Sign", "machines"]],
	"RequiredResearch": ["Lamp"],
	"Unlocks": [["Hand" + r_dict, "%Material%Sign"] ],
	"Levels": [0,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSign",
	"LabelParts": [["AdvancedSign", "machines"]],
	"RequiredResearch": ["Sign"],
	"Unlocks": [["Hand" + r_dict, "%Material%AdvancedSign"] ],
	"Levels": [2,7]
})
	
data = {
	"Objects": researches
}

csv.append(["InventoryUpgrade", "Inventory Upgrade"])
csv.append(["PlutoniumReaction", "Plutonium Reaction"])
csv.append(["ThoriumReaction", "Thorium Reaction"])
csv.append(["PowerGeneration", "Power Generation"])
csv.append(["Automatization", "Automatization"])
csv.append(["HeatTransferring", "Heat Transferring"])
csv.append(["BasicMachines", "Basic Machines"])
csv.append(["Container", "Fluid Storage"])
csv.append(["SingleTypeStorage", "Single Type Storage"])
csv.append(["DistributedComputing", "Distributed Computing"])
csv.append(["Sign", "Sign"])
csv.append(["SteelProduction", "Steel Production"])
csv.append(["AutomaticMining", "Automatic Mining"])
csv.append(["MetalConstructions", "Metal Constructions"])	
csv.append(["AdvancedSmelting", "Advanced Smelting"])
csv.append(["IndustrialSmelting", "Industrial Smelting"])
csv.append(["Fermentation", "Fermentation"])
csv.append(["NeutroniumProduction", "Neutronium Production"])
csv.append(["AluminiumProduction", "Aluminium Production"])
csv.append(["StainlessSteelProduction", "Stainless Steel Production"])
csv.append(["TitaniumProduction", "Titanium Production"])
csv.append(["MineralsScan", "Minerals Scan"])
csv.append(["Electricity", "Electricity"])
csv.append(["Smelting", "Smelting"])
csv.append(["Metalwork", "Metalwork"])
csv.append(["AdvancedReflection", "Advanced Reflection"])
csv.append(["ReactionThrottling", "Reaction Throttling"])
csv.append(["FuelChemistry", "Fuel Chemistry"])
csv.append(["FuelChemistry2", "Fuel Chemistry II"])
csv.append(["SulfurSynthesis", "Sulfur Synthesis"])
csv.append(["SulfuricAcidSynthesis", "Sulfuric Acid Synthesis"])
csv.append(["PreciseTemperaturePyrolysis", "Precise Temperature Pyrolysis"])
csv.append(["SteamPyrolysis", "Steam Pyrolysis"])
csv.append(["KrollProcess", "Kroll Process"])
csv.append(["AluminiumReduction", "Aluminium Reduction"])
csv.append(["AdvancedAlloys", "Advanced Alloys"])
csv.append(["LithiumBattery", "Lithium Battery"])
csv.append(["CrudeNiobium", "Crude Niobium"])

write_file("Generated/Researches/basic.json", data)
write_file("Loc/source/researches.json", csv)
