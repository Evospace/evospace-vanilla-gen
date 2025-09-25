from Common import *
from Materials import *
import copy
from NuclearResearches import *
from EquipmentResearches import *
from PartsResearchHelper import *

researches = []

tier_researches = [
	"MineralsScan",
	"Metalwork",
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
			"Complexity": cost
		})

		researches.append(research)

		

append_levels({
	"Class": research_recipe,
	"Name": "MineralsScan",
	"Label": ["MineralsScan", "researches"],
	"RequiredResearch": [],
	"Unlocks": [["Hand" + r_dict, tier_material[0] + "Furnace"],["Hand" + r_dict, "SandSurface"],["Hand" + r_dict, "GravelSurface"],["Hand" + r_dict, "Dirt"],["Hand" + r_dict, "CopperSpawner"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "BasicPlatform",
	"Label": ["BasicPlatform", "parts"],
	"RequiredResearch": ["MineralsScan"],
	"Unlocks": [["Hand" + r_dict, "BasicPlatform"], ["Hand" + r_dict, "BuildingMaterial"]],
	"CompleteByDefault": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "Bricks",
	"Label": ["Bricks", "misc"],
	"RequiredResearch": ["BasicPlatform"],
	"Unlocks": [["Hand" + r_dict, "Bricks"]],
})
for miscBlock in ["WoodenPlanks", "StoneTiles", "RedTiles", "DarkTiles", "Terracotta", "TerracottaTiles", "RedBricks", "DarkBricks", "TerracottaBricks"]:
	append_levels({
		"Class": research_recipe,
		"Name": miscBlock,
		"Label": [miscBlock, "misc"],
		"RequiredResearch": ["Bricks"],
		"Unlocks": [["Hand" + r_dict, miscBlock]],
		"Levels": [1,1]
	})
for miscBlock in ["Concrete", "ConcreteBricks", "ConcreteTiles", "ConcreteSmallTiles"]:
	append_levels({
		"Class": research_recipe,
		"Name": miscBlock,
		"Label": [miscBlock, "misc"],
		"RequiredResearch": ["StoneTiles"],
		"Unlocks": [["Hand" + r_dict, miscBlock]],
		"Levels": [2,2]
	})
for miscBlock in ["ReinforcedConcrete", "ReinforcedConcreteTiles", "ReinforcedConcreteSmallTiles", "ReinforcedConcreteBricks", "DangerBlock"]:
	append_levels({
		"Class": research_recipe,
		"Name": miscBlock,
		"Label": [miscBlock, "misc"],
		"RequiredResearch": ["Concrete"],
		"Unlocks": [["Hand" + r_dict, miscBlock]],
		"Levels": [3,3]
	})
append_levels({
	"Class": research_recipe,
	"Name": "Chest",
	"Label": ["Chest", "machines"],
	"RequiredResearch": ["MineralsScan"],
	"Unlocks": [["Hand" + r_dict, "%Material%Chest"] ],
	"Levels":[0,7],
	"CompleteByDefault": True,
	"CostMul": 3,
})
append_levels({
	"Class": research_recipe,
	"Name": "SingleTypeStorage",
	"Label": ["SingleTypeStorage", "researches"],
	"RequiredResearch": ["Chest" ],
	"MainResearch": True,
	"Levels":[1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%ItemRack"] ],
})
append_levels({
	"Class": "StaticResearchBonusInventory",
	"Name": "InventoryUpgrade",
	"Label": ["InventoryUpgrade", "researches"],
	"RequiredResearchArr": [["Chest"],["Chest1"],["Chest2"],["Chest3"],["Chest4"],["Chest5"],["Chest6"],[],[],[],[],[],[],[]],
	"Unlocks": [],
	"Levels": [0,7],
	"CostMul": 10,
})
append_levels({
	"Class": research_recipe,
	"Name": "Electricity",
	"Label": ["Electricity", "researches"],
	"RequiredResearch": ["MineralsScan"],
	"Unlocks": [["Hand" + r_dict, "CopperConnector"],["Hand" + r_dict, "CopperHandGenerator"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "ElectricFurnace",
	"Label": ["ElectricFurnace", "machines"],
	"Levels": [2,7],
	"RequiredResearch": ["CopperWire", "SteelProduction"],
	"Unlocks": [["Hand" + r_dict, "%Material%ElectricFurnace"] ],
})
append_levels({
	"Class": research_recipe,
	"Name": "ElectricalSwitch",
	"Label": ["ElectricalSwitch", "machines"],
	"RequiredResearch": ["CopperWire","SteelProduction"],
	"Unlocks": [["Hand" + r_dict, tier_material[2] + "ElectricalSwitch"]],
	"Levels": [2,2],
})
append_levels({
	"Class": research_recipe,
	"Name": "Diode",
	"Label": ["Diode", "machines"],
	"RequiredResearch": ["ElectricalSwitch"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Diode"] ],
})
append_levels({
	"Class": research_recipe,
	"Name": "PowerGeneration",
	"Label": ["PowerGeneration", "researches"],
	"RequiredResearch": ["Electricity", "Metalwork"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%CompactGenerator"],["Hand" + r_dict, "%Material%StirlingEngine"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "SteelProduction",
	"Label": ["SteelProduction", "researches"],
	"RequiredResearch": ["Oven"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%BlastFurnace"]],
	"UnlockFirst": get_parts_unlocks(tier_material[2]),
	"MainResearch": True,
	"CostMuls": [5, 2.5, 1.5, 1, 1, 1, 1, 1]
})
append_levels({
	"Class": research_recipe,
	"Name": "AdvancedSmelting",
	"Label": ["AdvancedSmelting", "researches"],
	"RequiredResearch": ["SteelProduction"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%ArcSmelter"] ],
	"MainResearch": True,
	"CostMuls": [4, 2, 1.5, 1, 1, 1, 1, 1, 1]
})
append_levels({
	"Class": research_recipe,
	"Name": "SmallSolarPanel",
	"Label": ["SmallSolarPanel", "machines"],
	"RequiredResearchArr": [["Electrolyzer1"], ["SiliconWafer"], [], [], [], [], [], [], [], [], []],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%SmallSolarPanel"], ["Hand" + r_dict, "%Material%SolarCell"]],
	"CostMul": 2
})
append_levels({
	"Class": research_recipe,
	"Name": "SolarPanel",
	"Label": ["SolarPanel", "machines"],
	"RequiredResearch": ["SmallSolarPanel"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%SolarPanel"] ],
	"CostMul": 8
})
append_levels({
	"Class": research_recipe,
	"Name": "Electrolyzer",
	"Label": ["Electrolyzer", "machines"],
	"RequiredResearch": ["SteelProduction"], 
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Electrolyzer"] ],
	"MainResearch": True,
	"CostMul": 3
})
append_levels({
	"Class": research_recipe,
	"Name": "AluminiumReduction",
	"Label": ["AluminiumReduction", "researches"],
	"RequiredResearch": ["Electrolyzer"], 
	"Levels": [2,2],
	"Unlocks": [["Electrolyzer" + r_dict, "AluminiumOxideDust"], ["Electrolyzer" + r_dict, "AluminiumOreDust"]],
	"MainResearch": True,
	"CostMul": 2.5
})
append_levels({
	"Class": research_recipe,
	"Name": "AluminiumProduction",
	"Label": ["AluminiumProduction", "researches"],
	"RequiredResearch": ["AdvancedSmelting", "AluminiumReduction"],
	"Unlocks": get_parts_unlocks(tier_material[3]) + [["Hand" + r_dict, "AluminiumFoil"],["Assembler" + r_dict, "AluminiumFoil"],["Hand" + r_dict, "Cell"]],
	"Levels": [3,3],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "Smelting",
	"Label": ["Smelting", "researches"],
	"RequiredResearch": ["MineralsScan"],
	"Unlocks": [["Hand" + r_dict, "%Material%Smelter"]],
	"Levels": [0,2],
	"CompleteByDefault": True,
	"MainResearch": True
})
append_equipment([-1,3], append_levels, researches)
append_levels({
	"Class": research_recipe,
	"Name": "Metalwork",
	"Label": ["Metalwork", "researches"],
	"RequiredResearch": ["Smelting"],
	"Unlocks": get_parts_unlocks(tier_material[1]),
	"Levels": [1,1],
	"CompleteByDefault": True,
	"MainResearch": True
})
append_levels({
	"Class": research_recipe,
	"Name": "Valve",
	"Label": ["Vent", "machines"],
	"RequiredResearch": ["Metalwork"],
	"Unlocks": [["Hand" + r_dict, tier_material[1] + "Vent"]],
	"Levels": [1,1],
})
append_levels({
	"Class": research_recipe,
	"Name": "BasicMachines",
	"Label": ["BasicMachines", "researches"],
	"RequiredResearch": ["Metalwork"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Macerator"],
	["Hand" + r_dict, "%Material%AutomaticHammer"]],
	"CostMul":0.25,
	"MainResearch": True,
	"Description": [["BasicMachinesDescription", "ui"]]
})
append_levels({
	"Class": research_recipe,
	"Name": "Flywheel",
	"Label": ["Flywheel", "machines"],
	"RequiredResearch": ["BasicMachines", "SteelProduction"],
	"Unlocks": [["Hand" + r_dict, tier_material[2] + "Flywheel"]],
	"Levels": [2,2],
})
append_levels({
	"Class": research_recipe,
	"Name": "Destroyer",
	"Label": ["Destroyer", "machines"],
	"Levels": [1,7],
	"RequiredResearch": ["Furnace"],
	"Unlocks": [["Hand" + r_dict, "%Material%Destroyer"]],
})
append_levels({
	"Class": research_recipe,
	"Name": "Pump",
	"Label": ["Pump", "machines"],
	"RequiredResearch": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Pump"] ],
	"CostMul":0.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Container",
	"Label": ["Container", "machines"],
	"RequiredResearchArr": [["Chest"],["Chest1"],["Chest2"],["Chest3"],["Chest4"],["Chest5"],["Chest6"],[],[],[],[],[],[],[]],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Container"] ],
	"MainResearch": True,
	"CostMul": 3,
})
append_levels({
	"Class": research_recipe,
	"Name": "FluidFurnace",
	"Label": ["FluidFurnace", "machines"],
	"RequiredResearch": ["Furnace"],
	"Unlocks": [["Hand" + r_dict, "%Material%FluidFurnace"] ],
	"Levels": [1,7],
})
append_levels({
	"Class": research_recipe,
	"Name": "Automatization",
	"Label": ["Automatization", "researches"],
	"RequiredResearch": ["BasicMachines"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%RobotArm"], ["Hand" + r_dict, "%Material%Conveyor"], ["Hand" + r_dict, "%Material%Splitter"]],
	"CostMul":0.25,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "Loader",
	"Label": ["Loader", "machines"],
	"RequiredResearch": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Loader"]],
	"CostMul": 2,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "Sorter",
	"Label": ["Sorter", "machines"],
	"RequiredResearch": ["Automatization1"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Sorter"]],
	"CostMul": 3,
})
append_levels({
	"Class": research_recipe,
	"Name": "OverflowPump",
	"Label": ["OverflowPump", "machines"],
	"RequiredResearch": ["Pump"],
	"Unlocks": [["Hand" + r_dict, "%Material%OverflowPump"]],
	"Levels": [1,7],
})
append_levels({
	"Class": research_recipe,
	"Name": "AutomaticMining",
	"Label": ["AutomaticMining", "researches"],
	"RequiredResearch": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%DrillingRig"] ],
	"CostMuls":[0.5, 0.75, 2.0, 3.0, 4.0, 5.0, 6.0],
	"MainResearch": True
})
append_levels({
	"Class": research_recipe,
	"Name": "Pumpjack",
	"Label": ["Pumpjack", "machines"],
	"RequiredResearch": ["AutomaticMining2"],
	"Unlocks": [["Hand" + r_dict, "%Material%Pumpjack"] ],
	"Levels": [4,7],
})
append_levels({
	"Class": research_recipe,
	"Name": "AutomaticFarm",
	"Label": ["AutomaticFarm", "machines"],
	"RequiredResearchArr": [["Automatization"],["Automatization1"],["Automatization2"],["Automatization3"],["Automatization4"],["Automatization5"],["Automatization6"],],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%AutomaticFarm"] ],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": research_recipe,
	"Name": "HeatTransferring",
	"Label": ["HeatTransferring", "researches"],
	"RequiredResearch": ["Smelting"],
	"Unlocks": [["Hand" + r_dict, "%Material%HeatPipe"] ],
	"Levels":[1,1],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": research_recipe,
	"Name": "KineticHeater",
	"Label": ["KineticHeater", "machines"],
	"RequiredResearch": ["HeatTransferring"],
	"Unlocks": [["Hand" + r_dict, "%Material%KineticHeater"] ],
	"Levels":[1,7],
	"CostMul":1,
})
append_levels({
	"Class": research_recipe,
	"Name": "AtmosphericCondenser",
	"Label": ["AtmosphericCondenser", "machines"],
	"RequiredResearch": ["AutomaticFarm"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%AtmosphericCondenser"] ],
	"CostMul":0.5,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "Oven",
	"Label": ["Oven", "researches"],
	"RequiredResearch": ["Furnace",],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Oven"] ],
	"MainResearch": True,
	"CostMul":3,
})
append_levels({
	"Class": research_recipe,
	"Name": "DistributedComputing",
	"Label": ["DistributedComputing", "researches"],
	"RequiredResearchArr": [["PowerGeneration"], ["AdvancedCircuit"], ["Processor"], ["QuantumCircuit"], ["QuantumProcessor"], ["QuantumBrain"]],
	"Unlocks": [["Hand" + r_dict, "%Material%Computer"] ],
	"Levels": [1,6],
	"CompleteByDefault": True,
	"MainResearchArr": [True,True,True,True,True,True,True],
	
})
append_levels({
	"Class": research_recipe,
	"Name": "CopperWire",
	"Label": ["CopperWire", "parts"],
	"RequiredResearch": ["DistributedComputing"],
	"Levels": [1,1],
	"Unlocks": [["Hand" + r_dict, "CopperWire"],[assembler_r_dict, "CopperWire"]],
	"CompleteByDefault": True,
	"MainResearch": True,
	"CostMul": 0.125
})
append_levels({
	"Class": research_recipe,
	"Name": "CircuitBoard",
	"Label": ["CircuitBoard", "parts"],
	"RequiredResearch": ["CopperWire"],
	"Levels": [1,1],
	"Unlocks": [["Hand" + r_dict, "CircuitBoard"]],
	"CostMul":0.3,
	"MainResearch": True
})
append_levels({
	"Class": research_recipe,
	"Name": "CircuitBoard2",
	"Label": ["TwoWorldsFormat", "common", ["CircuitBoard", "parts"], ["II", "common"]],
	"RequiredResearch": ["CircuitBoard", "Polyethylene"],
	"Levels": [3,3],
	"Unlocks": [[assembler_r_dict, "CircuitBoard2"]],
	"CostMul":1.5
})
append_levels({
	"Class": research_recipe,
	"Name": "CircuitBoard3",
	"Label": ["TwoWorldsFormat", "common", ["CircuitBoard", "parts"], ["III", "common"]],
	"RequiredResearch": ["CircuitBoard2", "CarbonFiber"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "CircuitBoard3"]],
	"CostMul":0.5
})
append_levels({
	"Class": research_recipe,
	"Name": "Triod",
	"Label": ["Triod", "parts"],
	"RequiredResearch": ["CircuitBoard"],
	"Unlocks": [["Hand" + r_dict, "Triod"],[assembler_r_dict, "Triod"]],
	"Levels": [1,1],
	"MainResearch": True
})
append_levels({
	"Class": research_recipe,
	"Name": "Circuit",
	"Label": ["Circuit", "parts"],
	"RequiredResearch": ["Triod"],
	"Unlocks": [["Hand" + r_dict, "Circuit"],[assembler_r_dict, "Circuit"]],
	"Levels": [1,1],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Circuit2",
	"Label": ["TwoWorldsFormat", "common", ["Circuit", "parts"], ["II", "common"]],
	"RequiredResearch": ["Circuit", "Transistor"],
	"Unlocks": [[assembler_r_dict, "Circuit2"]],
	"Levels": [1,1],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Furnace",
	"Label": ["Furnace", "machines"],
	"RequiredResearch": ["PowerGeneration"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Furnace"] ],
	"MainResearchArr": [True,True,True,True,True,True,True],
	"CostMul": 2.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Boiler",
	"Label": ["Boiler", "machines"],
	"RequiredResearch": ["PowerGeneration", "SteelProduction"],
	"Unlocks": [["Hand" + r_dict, "%Material%Boiler"]],
	"Levels": [2,7],
	"MainResearchArr": [True,True,False,False,False,False,False],
})
append_levels({
	"Class": research_recipe,
	"Name": "SteamEngine",
	"Label": ["SteamEngine", "machines"],
	"RequiredResearch": ["Boiler"],
	"Unlocks": [["Hand" + r_dict, "%Material%SteamEngine"]],
	"Levels": [2,7],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Resistor",
	"Label": ["Resistor", "parts"],
	"RequiredResearch": ["Circuit"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + r_dict, "Resistor"],[assembler_r_dict, "Resistor2"]],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Resistor2",
	"Label": ["TwoWorldsFormat", "common", ["Resistor", "parts"], ["II", "common"]],
	"RequiredResearch": ["Resistor", "Polyethylene"],
	"Levels": [3,3],
	"Unlocks": [[assembler_r_dict, "Resistor3"]],
	"CostMul": 1,
})
append_levels({
	"Class": research_recipe,
	"Name": "Resistor3",
	"Label": ["TwoWorldsFormat", "common", ["Resistor", "parts"], ["III", "common"]],
	"RequiredResearch": ["Resistor2", "Polyethylene", "CrudeTantalum"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "Resistor4"]],
	"CostMul": 1,
})
append_levels({
	"Class": research_recipe,
	"Name": "Resistor4",
	"Label": ["TwoWorldsFormat", "common", ["Resistor", "parts"], ["IV", "common"]],
	"RequiredResearch": ["Resistor3"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "Resistor5"]],
	"CostMul": 1,
})
append_levels({
	"Class": research_recipe,
	"Name": "AdvancedCircuit",
	"Label": ["AdvancedCircuit", "parts"],
	"RequiredResearch": ["Separator", "Resistor"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + r_dict, "AdvancedCircuit"],[assembler_r_dict, "AdvancedCircuit"]],
	"CostMul":1.6,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "Transistor",
	"Label": ["Transistor", "parts"],
	"RequiredResearch": ["AdvancedCircuit"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + r_dict, "Transistor"],[assembler_r_dict, "Transistor"]],
	"MainResearch": True,
	"CostMul":3.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Transistor2",
	"Label": ["TwoWorldsFormat", "common", ["Transistor", "parts"], ["II", "common"]],
	"RequiredResearch": ["Transistor", "Polyethylene"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "Transistor2"]],
	"CostMul":6.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Transistor3",
	"Label": ["TwoWorldsFormat", "common", ["Transistor", "parts"], ["III", "common"]],
	"RequiredResearch": ["Transistor2"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "Transistor3"]],
	"CostMul":12.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Transistor4",
	"Label": ["TwoWorldsFormat", "common", ["Transistor", "parts"], ["IV", "common"]],
	"RequiredResearch": ["Transistor3", "DopedSiliconWafer"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "Transistor4"]],
	"CostExact": 4*10**6,
})
append_levels({
	"Class": research_recipe,
	"Name": "AdvancedCircuit2",
	"Label": ["TwoWorldsFormat", "common", ["AdvancedCircuit", "parts"], ["II", "common"]],
	"RequiredResearch": ["Transistor"],
	"Levels": [2,2],
	"Unlocks": [[assembler_r_dict, "AdvancedCircuit2"]],
	"CostMul":2.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "SiliconWafer",
	"Label": ["SiliconWafer", "parts"],
	"RequiredResearch": ["IndustrialSmelting"],
	"Unlocks": [["IndustrialSmelter"+r_dict, "SiliconMonocrystal"],[assembler_r_dict, "SiliconWafer"]],
	"Levels": [4,4],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "DopedSiliconWafer",
	"Label": ["DopedSiliconWafer", "parts"],
	"RequiredResearch": ["SiliconWafer", "PlatinumSolution"],
	"Unlocks": [["IndustrialSmelter"+r_dict, "DopedSiliconMonocrystal"],[assembler_r_dict, "DopedSiliconWafer"]],
	"Levels": [6,6]
})
append_levels({
	"Class": research_recipe,
	"Name": "Processor",
	"Label": ["Processor", "parts"],
	"RequiredResearch": ["AdvancedCircuit"],
	"Unlocks": [["Hand" + r_dict, "Processor"]],
	"Levels": [3,3],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Capacitor",
	"Label": ["Capacitor", "parts"],
	"RequiredResearch": ["Processor"],
	"Levels": [3,3],
	"Unlocks": [["Hand" + r_dict, "Capacitor"]],
	"MainResearch": True,
	"CostMul":1.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Capacitor2",
	"Label": ["TwoWorldsFormat", "common", ["Capacitor", "parts"], ["II", "common"]],
	"RequiredResearch": ["Capacitor"],
	"Levels": [3,3],
	"Unlocks": [[assembler_r_dict, "Capacitor2"]],
	"CostMul":3,
})
append_levels({
	"Class": research_recipe,
	"Name": "Capacitor3",
	"Label": ["TwoWorldsFormat", "common", ["Capacitor", "parts"], ["III", "common"]],
	"RequiredResearch": ["Capacitor2", "Polyethylene"],
	"Levels": [3,3],
	"Unlocks": [[assembler_r_dict, "Capacitor3"]],
	"CostMul":6,
})
append_levels({
	"Class": research_recipe,
	"Name": "Capacitor4",
	"Label": ["TwoWorldsFormat", "common", ["Capacitor", "parts"], ["IV", "common"]],
	"RequiredResearch": ["Capacitor3", "Polyethylene"],
	"Levels": [3,3],
	"Unlocks": [[assembler_r_dict, "Capacitor4"]],
	"CostMul":12,
})
append_levels({
	"Class": research_recipe,
	"Name": "Processor2",
	"Label": ["TwoWorldsFormat", "common", ["Processor", "parts"], ["II", "common"]],
	"RequiredResearch": ["Capacitor"],
	"Unlocks": [[assembler_r_dict, "Processor2"]],
	"Levels": [3,3],
	"MainResearch": True,
	"CostMul":4,
})
append_levels({
	"Class": research_recipe,
	"Name": "Processor3",
	"Label": ["TwoWorldsFormat", "common", ["Processor", "parts"], ["III", "common"]],
	"RequiredResearch": ["Processor2", "DopedSiliconWafer"],
	"Unlocks": [[assembler_r_dict, "Processor3"]],
	"Levels": [3,3],
	"CostExact": 4*10**6,
})
append_levels({
	"Class": research_recipe,
	"Name": "Sulfur",
	"Label": ["SulfurSynthesis", "researches"],
	"RequiredResearch": ["IndustrialChemReactor", "PyrolysisUnit"],
	"Levels": [4,4],
	"Unlocks": [["IndustrialChemReactor" + r_dict, "Sulfur"]],
	"MainResearch": True,
	"CostMul": 0.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "SulfuricAcid",
	"Label": ["SulfuricAcidSynthesis", "researches"],
	"RequiredResearch": ["Sulfur", "Catalyst"],
	"Levels": [4,4],
	"Unlocks": [["IndustrialChemReactor" + r_dict, "SulfuricAcid"]],
	"MainResearch": True,
	"CostMul": 0.75,
})
append_levels({
	"Class": research_recipe,
	"Name": "BasicBattery",
	"Label": ["BasicBattery", "parts"],
	"RequiredResearch": ["Battery", "BatteryBox"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "BasicBattery"],["Hand" + r_dict, "BasicBattery"]],
	"MainResearch": True,
	"CostMul": 0.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "AdvancedBattery",
	"Label": ["AdvancedBattery", "parts"],
	"RequiredResearch": ["BasicBattery"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "AdvancedBattery"],["Hand" + r_dict, "AdvancedBattery"]],
	"CostMul": 4,
})
append_levels({
	"Class": research_recipe,
	"Name": "SuperiorBattery",
	"Label": ["SuperiorBattery", "parts"],
	"RequiredResearch": ["AdvancedBattery"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "SuperiorBattery"],["Hand" + r_dict, "SuperiorBattery"]],
	"CostMul": 8,
})
append_levels({
	"Class": research_recipe,
	"Name": "UltimateBattery",
	"Label": ["UltimateBattery", "parts"],
	"RequiredResearch": ["SuperiorBattery"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "UltimateBattery"],["Hand" + r_dict, "UltimateBattery"]],
	"CostMul": 16,
})
append_levels({
	"Class": research_recipe,
	"Name": "Battery",
	"Label": ["Battery", "parts"],
	"RequiredResearch": ["SulfuricAcid"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "Battery"],["Hand" + r_dict, "Battery"]],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "NitricAcid",
	"Label": ["NitricAcid", "parts"],
	"RequiredResearch": ["IndustrialChemReactor1"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "NitricAcid"]],
	"CostMul": 0.2,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "PlatinumSolution",
	"Label": ["PlatinumSolution", "parts"],
	"RequiredResearch": ["NitricAcid"],
	"Levels": [5,5],
	"Unlocks": [[ic_reactor_r_dict, "PlatinumSolution"],[ic_reactor_r_dict, "AmmoniumChloride"],[ic_reactor_r_dict, "Platinum"]],
	"CostMul": 1.2,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "RareEarthSludge",
	"Label": ["RareEarthSludge", "parts"],
	"RequiredResearch": ["SulfuricAcid"],
	"Levels": [4,4],
	"Unlocks": [["ChemicalBath" + r_dict, "RareEarthSludge"]],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "QuantumCore",
	"Label": ["QuantumCore", "parts"],
	"RequiredResearch": ["Processor", "RareEarthSludge"],
	"Levels": [4,4],
	"Unlocks": [["Hand" + r_dict, "QuantumCore"],[assembler_r_dict, "QuantumCore"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "QuantumCircuit",
	"Label": ["QuantumCircuit", "parts"],
	"RequiredResearch": ["QuantumCore"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + r_dict, "QuantumCircuit"],[assembler_r_dict, "QuantumCircuit"]],
	"MainResearch": True,
	"CostMul": 0.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "QuantumCircuit2",
	"Label": ["TwoWorldsFormat", "common", ["QuantumCircuit", "parts"], ["II", "common"]],
	"RequiredResearch": ["QuantumCircuit"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "QuantumCircuit2"]],
	"MainResearch": False,
	"CostMul": 1,
})
append_levels({
	"Class": research_recipe,
	"Name": "DecisionResonator",
	"Label": ["DecisionResonator", "parts"],
	"RequiredResearch": ["QuantumCircuit"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + r_dict, "DecisionResonator"]],
	"MainResearch": True,
	"CostMul":0.75,
})
append_levels({
	"Class": research_recipe,
	"Name": "DecisionResonator2",
	"Label": ["TwoWorldsFormat", "common", ["DecisionResonator", "parts"], ["II", "common"]],
	"RequiredResearch": ["DecisionResonator"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "DecisionResonator2"]],
	"CostMul":1.0,
})
append_levels({
	"Class": research_recipe,
	"Name": "DecisionResonator3",
	"Label": ["TwoWorldsFormat", "common", ["DecisionResonator", "parts"], ["III", "common"]],
	"RequiredResearch": ["DecisionResonator2"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "DecisionResonator3"]],
	"CostMul":2.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "DecisionResonator4",
	"Label": ["TwoWorldsFormat", "common", ["DecisionResonator", "parts"], ["IV", "common"]],
	"RequiredResearch": ["DecisionResonator3", "DopedSiliconWafer"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "DecisionResonator4"]],
	"CostMul":5.0,
})
append_levels({
	"Class": research_recipe,
	"Name": "QuantumProcessor",
	"Label": ["QuantumProcessor", "parts"],
	"RequiredResearch": ["DecisionResonator"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + r_dict, "QuantumProcessor"],[assembler_r_dict, "QuantumProcessor"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "QuantumProcessor2",
	"Label": ["TwoWorldsFormat", "common", ["QuantumProcessor", "parts"], ["II", "common"]],
	"RequiredResearch": ["QuantumProcessor"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "QuantumProcessor2"]],
	"CostMul":5,
})
append_levels({
	"Class": research_recipe,
	"Name": "BrainMatrix",
	"Label": ["BrainMatrix", "parts"],
	"RequiredResearch": ["QuantumProcessor"],
	"Levels": [6,6],
	"Unlocks": [["Hand" + r_dict, "BrainMatrix"]],
	"MainResearch": True,
	"CostMul":1.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "QuantumBrain",
	"Label": ["QuantumBrain", "parts"],
	"RequiredResearch": ["BrainMatrix"],
	"Levels": [6,6],
	"Unlocks": [["Hand" + r_dict, "QuantumBrain"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "QuantumBrain2",
	"Label": ["TwoWorldsFormat", "common", ["QuantumBrain", "parts"],["II", "common"]],
	"RequiredResearch": ["QuantumBrain", "UltimateCatalyst"],
	"Levels": [6,6],
	"Unlocks": [[assembler_r_dict, "QuantumBrain2"]],
	"MainResearch": True,
	"CostMul":5,
})
append_levels({
	"Class": research_recipe,
	"Name": "MetalConstructions",
	"Label": ["MetalConstructions", "researches"],
	"RequiredResearch": ["Bricks"],
	"Unlocks": [["Hand" + r_dict, "%Material%Corner"],
	["Hand" + r_dict, "%Material%Beam"]],
	"Levels": [1,7],
	"Chapter":"Decorations"+static_chapter,
	
})
append_levels({
	"Class": research_recipe,
	"Name": "Scaffold",
	"Label": ["Scaffold", "researches"],
	"RequiredResearch": ["MetalConstructions"],
	"Unlocks": [["Hand" + r_dict, "%Material%Scaffold"] ],
	"Levels": [1,7],
	
})
append_levels({
	"Class": research_recipe,
	"Name": "IndustrialChemReactor",
	"Label": ["IndustrialChemReactor", "machines"],
	"RequiredResearch": ["ElectricEngine"],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialChemReactor"] ],
	"Levels": [3,7],
	"MainResearchArr": [True, True, False, False, False, False],
})
append_levels({
	"Class": research_recipe,
	"Name": "Catalyst",
	"Label": ["Catalyst", "parts"],
	"RequiredResearch": ["IndustrialChemReactor"],
	"Unlocks": [["Hand" + r_dict, "Catalyst"]],
	"Levels": [3,3],
	"MainResearch": True,
	"CostMul": 1.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "Catalyst2",
	"Label": ["TwoWorldsFormat", "common", ["Catalyst", "parts"],["II", "common"]],
	"RequiredResearch": ["Catalyst"],
	"Unlocks": [[assembler_r_dict, "Catalyst2"]],
	"Levels": [3,3],
	"CostMul": 3,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "FuelChemistry",
	"Label": ["FuelChemistry", "researches"],
	"RequiredResearch": ["Catalyst"],
	"Unlocks": [[ic_reactor_r_dict, "RocketFuel"]],
	"Levels": [3,3],
})
append_levels({
	"Class": research_recipe,
	"Name": "FuelChemistry2",
	"Label": ["TwoWorldsFormat", "common", ["FuelChemistry", "researches"], ["II", "common"]],
	"RequiredResearch": ["FuelChemistry", "NitricAcid"],
	"Unlocks": [[ic_reactor_r_dict, "HighCetaneDiesel"]],
	"Levels": [4,4],
})
append_levels({
	"Class": research_recipe,
	"Name": "FuelChemistry3",
	"Label": ["TwoWorldsFormat", "common", ["FuelChemistry", "researches"], ["III", "common"]],
	"RequiredResearch": ["FuelChemistry2", "IndustrialChemReactor2"],
	"Unlocks": [[ic_reactor_r_dict, "Superfuel"]],
	"Levels": [5,5],
})
append_levels({
	"Class": research_recipe,
	"Name": "FuelChemistry4",
	"Label": ["TwoWorldsFormat", "common", ["FuelChemistry", "researches"], ["IV", "common"]],
	"RequiredResearch": ["FuelChemistry3", "UltimateCatalyst"],
	"Unlocks": [[ic_reactor_r_dict, "RocketFuel2"], [ic_reactor_r_dict, "Superfuel2"]],
	"Levels": [6,6],
})
append_levels({
	"Class": research_recipe,
	"Name": "Sifter",
	"Label": [["Sifter", "machines"]],
	"RequiredResearch": ["ElectricEngine"],
	"Unlocks": [["Hand" + r_dict, "%Material%Sifter"] ],
	"Levels": [3,7],
	
})
append_levels({
	"Class": research_recipe,
	"Name": "Separator",
	"Label": ["Separator", "machines"],
	"RequiredResearch": ["ElectricEngine"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Separator"] ],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "ElectricEngine",
	"Label": ["ElectricEngine", "machines"],
	"RequiredResearch": ["SteelProduction"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%ElectricEngine"] ],
	"MainResearchArr": [True, True, False, False, False, False, False],
	"CostMul": 2,
})
append_levels({
	"Class": research_recipe,
	"Name": "Generator",
	"Label": ["Generator", "machines"],
	"RequiredResearch": ["ElectricEngine1"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Generator"]],
	"MainResearchArr": [True, False, False, False, False, False, False],
	"CostMul": 2.5,
})
append_levels({
	"Class": research_recipe,
	"Name": "SteamTurbine",
	"Label": ["SteamTurbine", "machines"],
	"RequiredResearch": ["Generator", "Boiler1"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%SteamTurbine"] ],
	"MainResearchArr": [True, False, False, False, False, False, False],
	"CostMul": 1.0,
})
append_levels({
	"Class": research_recipe,
	"Name": "OreWasher",
	"Label": ["OreWasher", "machines"],
	"Levels": [2,7],
	"RequiredResearch": ["Separator"],
	"Unlocks": [["Hand" + r_dict, "%Material%OreWasher"] ],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "Mixer",
	"Label": ["Mixer", "machines"],
	"RequiredResearch": ["OreWasher", "Electrolyzer"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Mixer"] ],
	"MainResearch": True,
	
})
append_levels({
	"Class": research_recipe,
	"Name": "ChemicalBath",
	"Label": ["ChemicalBath", "machines"],
	"RequiredResearch": ["IndustrialChemReactor"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%ChemicalBath"] ],
	"MainResearch": True,
	"CostMul":5,
})
append_levels({
	"Class": research_recipe,
	"Name": "FractionatingColumn",
	"Label": ["FractionatingColumn", "machines"],
	"RequiredResearch": ["FuelChemistry"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + r_dict, "%Material%FractionatingColumn"] ],
	
})
append_levels({
	"Class": research_recipe,
	"Name": "CombustionEngine",
	"Label": ["CombustionEngine", "machines"],
	"RequiredResearch": ["Catalyst"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + r_dict, "%Material%CombustionEngine"] ],
	
})
append_levels({
	"Class": research_recipe,
	"Name": "AdvancedAlloys",
	"Label": ["AdvancedAlloys", "researches"],
	"RequiredResearch": ["Mixer", "AluminiumProduction", "Separator"],
	"Unlocks": [["Mixer" + r_dict, "SSCraft"],["Mixer" + r_dict, "SSCraft2"]],
	"Levels": [4,4],
	"MainResearch": True,
	"CostMul": 0.5
})
append_levels({
	"Class": research_recipe,
	"Name": "StainlessSteelProduction",
	"Label": ["StainlessSteelProduction", "researches"],
	"RequiredResearch": ["AdvancedAlloys"],
	"Unlocks": get_parts_unlocks(tier_material[4]) + [],
	"Levels": [4,4],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "BatteryBox",
	"Label": ["BatteryBox", "machines"],
	"RequiredResearch": ["AluminiumProduction"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + r_dict, "%Material%BatteryBox"] ],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "PrimitiveBattery",
	"Label": ["PrimitiveBattery", "parts"],
	"RequiredResearch": ["BatteryBox"],
	"Levels": [3,3],
	"Unlocks": [[h_r_dict, "PrimitiveBattery"]],
	"CostMul": 2,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "CarbonFiber",
	"Label": ["CarbonFiber", "parts"],
	"RequiredResearch": ["PyrolysisUnit", "IndustrialChemReactor1"],
	"Unlocks": [["PyrolysisUnit"+r_dict,"CarbonFiber"], [ic_reactor_r_dict, "CarbonPrecursor"]],
	"Levels": [5,5],
	"MainResearch": True,
	"CostMul": 0.3,
})
append_levels({
	"Class": research_recipe,
	"Name": "CarbonFiberSheet",
	"Label": ["CarbonFiberSheet", "parts"],
	"RequiredResearch": ["CarbonFiber"],
	"Unlocks": [["Hand"+r_dict,"CarbonFiberSheet"]],
	"Levels": [5,5],
	"MainResearch": True,
	"CostMul": 0.6,
})
append_levels({
	"Class": research_recipe,
	"Name": "KrollProcess",
	"Label": ["KrollProcess", "researches"],
	"RequiredResearch": ["IndustrialSmelting", "NitricAcid"],
	"Unlocks": [["IndustrialSmelter"+r_dict,"SpongeToPlate"],["IndustrialChemReactor" + r_dict, "TitaniumSponge"],["IndustrialChemReactor" + r_dict, "TitaniumTetrachloride"]],
	"Levels": [5,5],
	"MainResearch": True,
	"CostMul": 0.5,
	
})
append_levels({
	"Class": research_recipe,
	"Name": "TitaniumProduction",
	"Label": ["TitaniumProduction", "researches"],
	"RequiredResearch": ["KrollProcess"],
	"Unlocks": get_parts_unlocks(tier_material[5]),
	"Levels": [5,5],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "IndustrialBoiler",
	"Label": ["IndustrialBoiler", "machines"],
	"RequiredResearch": ["TitaniumProduction"],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialBoiler"],["Connector" + r_dict, "%Material%IndustrialBoiler"]],
	"Levels": [5,7],
})
append_levels({
	"Class": research_recipe,
	"Name": "IndustrialSteamTurbine",
	"Label": ["IndustrialSteamTurbine", "machines"],
	"RequiredResearch": ["IndustrialBoiler"],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialSteamTurbine"],["Connector" + r_dict, "%Material%IndustrialSteamTurbine"]],
	"Levels": [5,7],
})
append_levels({
	"Class": research_recipe,
	"Name": "IndustrialGenerator",
	"Label": ["IndustrialGenerator", "machines"],
	"RequiredResearch": ["IndustrialSteamTurbine"],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialGenerator"],["Connector" + r_dict, "%Material%IndustrialGenerator"]],
	"Levels": [5,7],
})
append_levels({
	"Class": research_recipe,
	"Name": "Polyethylene",
	"Label": ["PolyethyleneSheet", "parts"],
	"RequiredResearch": ["IndustrialChemReactor"],
	"Levels": [3,3],
	"Unlocks": [[ic_reactor_r_dict, "PolyethyleneSheet"]],
	"MainResearch": True,
	"CostMul": 1.25
})
append_levels({
	"Class": research_recipe,
	"Name": "CrudeTantalum",
	"Label": ["CrudeTantalum", "researches"],
	"RequiredResearch": ["Polyethylene"],
	"Levels": [5,5],
	"Unlocks": [["IndustrialSmelter" + r_dict, "TantalumSludge"], [h_r_dict, "TantalumWire"], [h_r_dict, "TantalumFoil"]],
	"CostMul": 5.5
})
append_levels({
	"Class": research_recipe,
	"Name": "CompositePlate",
	"Label": ["CompositePlate", "parts"],
	"RequiredResearch": ["TitaniumProduction", "CarbonFiberSheet", "Polyethylene"],
	"Levels": [6,6],
	"Unlocks": [[assembler_r_dict, "CompositePlate"]] + get_parts_unlocks(tier_material[6]),
	"MainResearch": True,
	"CostMul": 2.25
})
append_levels({
	"Class": research_recipe,
	"Name": "CompositePlate2",
	"Label": ["TwoWorldsFormat", "common", ["CompositePlate", "parts"], ["II", "common"]],
	"RequiredResearch": ["CompositePlate", "Polyethylene"],
	"Levels": [6,6],
	"Unlocks": [[assembler_r_dict, "CompositePlate2"]],
	"MainResearch": True,
	"CostMul": 5
})
append_levels({
	"Class": research_recipe,
	"Name": "PlatinumReflector",
	"Label": ["PlatinumReflector", "parts"],
	"RequiredResearch": ["PlatinumSolution"],
	"Unlocks": [["Hand" + r_dict, "PlatinumReflector"]],
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "FusionReactor",
	"Label": ["FusionReactor", "machines"],
	"RequiredResearch": ["CompositePlate", "PlatinumReflector"],
	"Unlocks": [["Hand" + r_dict, "%Material%FusionReactor"] ],
	"Levels": [6,7],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "FusionReaction",
	"Label": ["FusionReaction", "researches"],
	"RequiredResearch": ["FusionReactor"],
	"Unlocks": [[ic_reactor_r_dict, "SynthesisCell"], ["FusionReactor" + r_dict, "HotNeutroniumPlate1"], [ic_reactor_r_dict, "NeutroniumPlate"]],
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "NeutroniumProduction",
	"Label": ["NeutroniumProduction", "researches"],
	"RequiredResearch": ["FusionReaction"],
	"Unlocks": get_parts_unlocks(tier_material[7]),
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "UltimateCatalyst",
	"Label": ["UltimateCatalyst", "parts"],
	"RequiredResearch": ["NeutroniumProduction"],
	"Unlocks": [["Hand" + r_dict, "UltimateCatalyst"]],
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "NeutroniumProduction2",
	"Label": ["TwoWorldsFormat", "common", ["NeutroniumProduction", "researches"], ["II", "common"]],
	"RequiredResearch": ["UltimateCatalyst"],
	"Unlocks": [["FusionReactor" + r_dict, "HotNeutroniumPlate2"]],
	"Levels": [6,6],
	"CostMul": 2
})
append_levels({
	 "Class": research_recipe,
	 "Name": "Portal",
	 "Label": ["Portal", "machines"],
	 "RequiredResearch": ["UltimateCatalyst", "QuantumBrain"],
	 "Unlocks": [["Hand" + r_dict, "%Material%Portal"] ],
	 "Levels": [7,7],
	 "MainResearch": True,
	 "CostMul": 2
 })
append_levels({
	"Class": research_recipe,
	"Name": "FissionReactor",
	"Label": ["FissionReactor", "machines"],
	"RequiredResearch": ["UraniumCell"],
	"Levels": [5,7],
	"Unlocks": [["Hand" + r_dict, "%Material%FissionReactor"] ],
})
append_levels({
	"Class": research_recipe,
	"Name": "UraniumCell",
	"Label": ["UraniumCell", "parts"],
	"RequiredResearch": ["TitaniumProduction"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + r_dict, "UraniumCell"]],
})
append_nuclear([7,-7], append_levels, researches)
append_levels({
	"Class": research_recipe,
	"Name": "IndustrialSmelting",
	"Label": ["IndustrialSmelting", "researches"],
	"RequiredResearch": ["StainlessSteelProduction"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + r_dict, "%Material%IndustrialSmelter"] ],
	"MainResearch": True,
	"CostMul": 3,
})
append_levels({
	"Class": research_recipe,
	"Name": "IndustrialSteelProduction",
	"Label": ["IndustrialSteelProduction", "researches"],
	"RequiredResearch": ["IndustrialSmelting"],
	"Levels": [4,4],
	"Unlocks": [["IndustrialSmelter" + r_dict, "Steel"]],
	"CostMul":2,
})
append_levels({
	"Class": research_recipe,
	"Name": "Fermentation",
	"Label": ["Fermentation", "researches"],
	"Levels": [3,7],
	"RequiredResearch": ["ElectricEngine"],
	"Unlocks": [["Hand" + r_dict, "%Material%Fermenter"] ],
})
append_levels({
	"Class": research_recipe,
	"Name": "Terminal",
	"Label": ["Terminal", "machines"],
	"Levels": [4,4],
	"RequiredResearch": ["StainlessSteelProduction"],
	"Unlocks": [["Hand" + r_dict, tier_material[4] + "Terminal"]],
})
append_levels({
	"Class": research_recipe,
	"Name": "FlatTerminal",
	"Label": ["FlatTerminal", "machines"],
	"Levels": [4,4],
	"RequiredResearch": ["Terminal"],
	"Unlocks": [["Hand" + r_dict, tier_material[4] + "FlatTerminal"]],
})
append_levels({
	"Class": research_recipe,
	"Name": "Assembler",
	"Label": ["Assembler", "machines"],
	"RequiredResearch": ["AdvancedCircuit"],
	"Unlocks": [["Hand" + r_dict, "%Material%Assembler"]],
	"Levels": [3,7],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "Constructor",
	"Label": ["Constructor", "machines"],
	"RequiredResearch": ["Automatization"],
	"Unlocks": [["Hand" + r_dict, "%Material%Constructor"]],
	"Levels": [1, 7],
	"CostMul": 0.5,
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "BigTerminal",
	"Label": ["BigTerminal", "machines"],
	"RequiredResearch": ["Terminal"],
	"Unlocks": [["Hand" + r_dict, tier_material[5] + "BigTerminal"]],
	"Levels": [4,4],
})
append_levels({
	"Class": research_recipe,
	"Name": "BigFlatTerminal",
	"Label": ["BigFlatTerminal", "machines"],
	"RequiredResearch": ["BigTerminal"],
	"Unlocks": [["Hand" + r_dict, tier_material[5] + "BigFlatTerminal"]],
	"Levels": [4,4],
})
append_levels({
	"Class": research_recipe,
	"Name": "HugeTerminal",
	"Label": ["HugeTerminal", "machines"],
	"RequiredResearch": ["BigTerminal"],
	"Unlocks": [["Hand" + r_dict, tier_material[6] + "HugeTerminal"]],
	"Levels": [5,5],
})
append_levels({
	"Class": research_recipe,
	"Name": "HugeFlatTerminal",
	"Label": ["HugeFlatTerminal", "machines"],
	"RequiredResearch": ["HugeTerminal"],
	"Unlocks": [["Hand" + r_dict, tier_material[6] + "HugeFlatTerminal"]],
	"Levels": [5,5],
}) 
append_levels({
	"Class": research_recipe,
	"Name": "PyrolysisUnit",
	"Label": ["PyrolysisUnit", "machines"],
	"RequiredResearch": ["Mixer"],
	"Unlocks": [["Hand" + r_dict, "%Material%PyrolysisUnit"] ],
	"Levels": [4,7],
	"MainResearch": True,
})
append_levels({
	"Class": research_recipe,
	"Name": "PreciseTemperaturePyrolysis",
	"Label": ["PreciseTemperaturePyrolysis", "researches"],
	"RequiredResearch": ["PyrolysisUnit"],
	"Unlocks": [["PyrolysisUnit" + r_dict, f"RawOil{i}"] for i in range(len(oil_crack_array(0)))],
	"Levels": [4,4]
})	
append_levels({
	"Class": research_recipe,
	"Name": "DecorativeWood",
	"RequiredResearch": ["Bricks"],
	"Label": ["DecorativeWood", "researches"],
	"Unlocks": [["Hand" + r_dict, "WoodenPlanks"],["Hand" + r_dict, "WoodenStairs"],["Hand" + r_dict, "Bed"],["Hand" + r_dict, "Door"]],
	"Levels": [1,1],
})
append_levels({
	"Class": research_recipe,
	"Name": "DecorativeWood2",
	"Label": ["TwoWorldsFormat", "common", ["DecorativeWood", "researches"], [level_labels[1], "common"]],
	"RequiredResearch": ["DecorativeWood"],
	"Unlocks": [["Hand" + r_dict, "Chair"],["Hand" + r_dict, "Fence"],["Hand" + r_dict, "Ladder"],["Hand" + r_dict, "Rack"],["Hand" + r_dict, "Table"]],
	"Levels": [2,2],
})
append_levels({
	"Class": research_recipe,
	"Name": "Fence",
	"Label": ["Fence", "misc"],
	"RequiredResearch": ["DecorativeWood2"],
	"Unlocks": [["Hand" + r_dict, "SteelFence"]],
	"Levels": [2,2],
})
append_levels({
	"Class": research_recipe,
	"Name": "Fence1",
	"Label": ["TwoWorldsFormat", "common", ["Fence", "misc"], [level_labels[1], "common"]],
	"RequiredResearch": ["Fence"],
	"Unlocks": [["Hand" + r_dict, "StainlessSteelFence"]],
	"Levels": [3,3],
})
append_levels({
	"Class": research_recipe,
	"Name": "DecorativeWood4",
	"Label": ["TwoWorldsFormat", "common", ["DecorativeWood", "researches"], [level_labels[3], "common"]],
	"RequiredResearch": ["DecorativeWood2"],
	"Unlocks": [["Hand" + r_dict, "CopperChair"]],
	"Levels": [3,3],
})
append_levels({
	"Class": research_recipe,
	"Name": "DecorativeWood3",
	"Label": [["DecorativeWood", "researches"], [level_labels[2], "common"]],
	"RequiredResearch": ["DecorativeWood2", "AdvancedSmelting"],
	"Unlocks": [["Hand" + r_dict, "Window"]],
	"Levels": [3,3],
})
append_levels({
	"Class": research_recipe,
	"Name": "DecorativePlastic",
	"Label": ["DecorativePlastic", "researches"],
	"RequiredResearch": ["IndustrialChemReactor", "PyrolysisUnit", "DecorativeWood3"],
	"Unlocks": [["Hand" + r_dict, "PlasticWindow"]],
	"Levels": [4,4],
})
append_levels({
	"Class": research_recipe,
	"Name": "Lamp",
	"Label": ["Lamp", "machines"],
	"RequiredResearch": [],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Lamp"] ],
	"CostMul": 0.1,
})
append_levels({
	"Class": research_recipe,
	"Name": "Flashlight",
	"Label": ["Flashlight", "misc"],
	"RequiredResearch": ["Lamp1"],
	"Unlocks": [["Hand" + r_dict, "Flashlight"]],
	"Levels": [2,2],
})
append_levels({
	"Class": research_recipe,
	"Name": "Sign",
	"Label": ["Sign", "machines"],
	"RequiredResearch": ["Lamp"],
	"Unlocks": [["Hand" + r_dict, "%Material%Sign"] ],
	"Levels": [0,7],
})
append_levels({
	"Class": research_recipe,
	"Name": "AdvancedSign",
	"Label": ["AdvancedSign", "machines"],
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
csv.append(["IndustrialSteelProduction", "Industrial Steel Production"])
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
csv.append(["SulfurSynthesis", "Sulfur Synthesis"])
csv.append(["SulfuricAcidSynthesis", "Sulfuric Acid Synthesis"])
csv.append(["PreciseTemperaturePyrolysis", "Precise Temperature Pyrolysis"])
csv.append(["SteamPyrolysis", "Steam Pyrolysis"])
csv.append(["KrollProcess", "Kroll Process"])
csv.append(["AluminiumReduction", "Aluminium Reduction"])
csv.append(["AdvancedAlloys", "Advanced Alloys"])
csv.append(["LithiumBattery", "Lithium Battery"])
csv.append(["CrudeTantalum", "Crude Tantalum"])
csv.append(["FusionReaction", "Fusion Reaction"])

write_file("Generated/Researches/basic.json", data)
write_file("Loc/source/researches.json", csv)
