from Common import *
from Materials import *
import copy
from NuclearResearches import *
from EquipmentResearches import *
from PartsResearchHelper import *

researches = []

tier_researches = [
	"MineralScan",
	"MineralScan",
	"SteelProduction",
	"AluminiumProduction",
	"StainlessSteelProduction",
	"TitaniumProduction",
	"CompositeMaterials",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
]

csv = []

def append_levels(research_base):
	mini = research_base["Levels"][0] if "Levels" in research_base else 0
	maxi = research_base["Levels"][1] + 1 if "Levels" in research_base else 1
	for i in range(mini, maxi):
		thisLevel = i - mini
		research = copy.deepcopy(research_base)

		if "RequiredResearch" not in research:
			research["RequiredResearch"] = []

		if i != mini:
			research["IsUpgrade"] = True
			research["MainResearch"] = False
			research["CompleteByDefault"] = False
			research["Name"] = research["Name"] + str(thisLevel)
			if i != mini + 1:
				research["RequiredResearch"] = [research_base["Name"] + str(thisLevel - 1)]
			else:
				research["RequiredResearch"] = [research_base["Name"]]

			research["RequiredResearch"].append(tier_researches[i])

		if "RequiredResearchArr" in research:
			if len(research["RequiredResearchArr"]) > thisLevel:
				research["RequiredResearch"].extend(research["RequiredResearchArr"][thisLevel])

		if "MainResearchArr" in research and research["MainResearchArr"][thisLevel] == True:
			research["MainResearch"] = True

		if "Unlocks" in research:
			unl = copy.deepcopy(research["Unlocks"])
			research["Unlocks"] = []
			
			new = []
			for j in unl:
				new.append([j[0], j[1].replace("%Material%", tier_material[i])])                
			research["Unlocks"] = new
		
		CostMul = research["CostMul"] if "CostMul" in research else 1
		CostMul = research["CostMuls"][thisLevel] if "CostMuls" in research else CostMul

		research["Level"] = thisLevel
		research["Levels"] = [i,i]
		research["DataPoints"] = {"Items" : [{
			"Name": "Computations",
			"Count": tiers_base_cost[i] * CostMul
			}]
		}
    
		researches.append(research)

append_levels({
	"Class": "StaticResearch",
	"Name": "MineralsScan",
	"LabelParts": [["MineralsScan", "researches"]],
	"RequiredResearch": [],
	"Unlocks": [["Hand" + r_dict, tier_material[0] + "Furnace"],["Hand" + r_dict, "SandSurface"],["Hand" + r_dict, "GravelSurface"]],
	"CompleteByDefault": True,
	"MainResearch": True,
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
	"RequiredResearch": ["MineralScan"],
	"Unlocks": [["Hand" + r_dict, "CopperConnector"],["Hand" + r_dict, "CopperHandGenerator"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricFurnace",
	"LabelParts": [["ElectricFurnace", "machines"]],
	"Levels": [2,7],
	"RequiredResearch": ["CopperWire"],
	"Unlocks": [["Hand" + r_dict, "%Material%ElectricFurnace"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricalSwitch",
	"LabelParts": [["ElectricalSwitch", "machines"]],
	"RequiredResearch": ["CopperWire"],
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
	"Unlocks": [["Hand" + r_dict, "%Material%CompactGenerator"] ],
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SteelProduction",
	"LabelParts": [["SteelProduction", "researches"]],
	"RequiredResearch": ["Oven"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%BlastFurnace"] ] + get_parts_unlocks(tier_material[2]),
	"MainResearch": True,
	"CostMul": 5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSmelting",
	"LabelParts": [["AdvancedSmelting", "researches"]],
	"RequiredResearch": ["SteelProduction"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%ArcSmelter"] ],
	"MainResearch": True,
	"CostMul": 4
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
	"Name": "Electrolysis",
	"LabelParts": [["Electrolysis", "researches"]],
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
	"RequiredResearch": ["Electrolysis"], 
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
	"Unlocks": get_parts_unlocks(tier_material[3]),
	"Levels": [3,3],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GasTurbine",
	"LabelParts": [["GasTurbine", "machines"]],
	"RequiredResearch": ["Error"],
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
	"RequiredResearch": ["BasicMachines"],
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
	"Unlocks": [["Hand" + r_dict, "%Material%RobotArm"],
	["Hand" + r_dict, "%Material%Conveyor"],
	["Hand" + r_dict, "%Material%Splitter"]],
	"CostMul":0.25,
	"MainResearch": True,
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
	"Name": "Cutting",
	"LabelParts": [["Cutting", "researches"]],
	"RequiredResearch": ["BasicMachines"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%CuttingMachine"] ],
	"MainResearch": True,
	"CostMul":0.25,
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
	"Name": "StirlingEngine",
	"LabelParts": [["StirlingEngine", "machines"]],
	"RequiredResearch": ["MineralsScan"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%StirlingEngine"] ],
	"CompleteByDefault": True,
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
	"CostMul":0.25,
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
	"Name": "Furnace",
	"LabelParts": [["Furnace", "machines"]],
	"RequiredResearch": ["StirlingEngine"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Furnace"] ],
	"MainResearchArr": [True,True,True,True,True,True,True],
	"CostMul": 2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Boiler",
	"LabelParts": [["Boiler", "machines"]],
	"RequiredResearch": ["PowerGeneration"],
	"Unlocks": [["Hand" + r_dict, "%Material%Boiler"]],
	"Levels": [2,7],
	"MainResearch": True
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
	"Name": "AdvancedCircuit",
	"LabelParts": [["AdvancedCircuit", "parts"]],
	"RequiredResearch": ["Separator", "Circuit"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + r_dict, "AdvancedCircuit"],[assembler_r_dict, "AdvancedCircuit"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GoldWire",
	"LabelParts": [["GoldWire", "parts"]],
	"RequiredResearch": ["AdvancedCircuit", "OreWasher"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + r_dict, "GoldWire"],[assembler_r_dict, "GoldWire"]],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedCircuitBoard",
	"LabelParts": [["AdvancedCircuitBoard", "parts"]],
	"RequiredResearch": ["GoldWire", "PyrolysisUnit"],
	"Levels": [3,3],
	"Unlocks": [["Hand" + r_dict, "AdvancedCircuitBoard"],[assembler_r_dict, "AdvancedCircuitBoard"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SiliconWafer",
	"LabelParts": [["SiliconWafer", "parts"]],
	"RequiredResearch": ["AdvancedCircuit"],
	"Unlocks": [[assembler_r_dict, "SiliconWafer"]],
	"Levels": [3,3],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Processor",
	"LabelParts": [["Processor", "parts"]],
	"RequiredResearch": ["SiliconWafer", "AdvancedCircuitBoard"],
	"Unlocks": [["Hand" + r_dict, "Processor"],[assembler_r_dict, "Processor"],[assembler_r_dict, "Processor2"]],
	"Levels": [3,3],
	"MainResearch": True,
	"CostMul":2.5,
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
	"Name": "Battery",
	"LabelParts": [["Battery", "parts"]],
	"RequiredResearch": ["SulfuricAcid"],
	"Levels": [4,4],
	"Unlocks": [[assembler_r_dict, "Battery"],["Hand" + r_dict, "Battery"]],
	"MainResearch": True,
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
	"Unlocks": [["IndustrialChemReactor" + r_dict, "NitricAcid"]],
	"CostMul": 0.2,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "LithiumPlate",
	"LabelParts": [["LithiumPlate", "parts"]],
	"RequiredResearch": ["NitricAcid"],
	"Levels": [5,5],
	"Unlocks": [["IndustrialChemReactor" + r_dict, "LithiumPlate"]],
	"CostMul": 0.3,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "LithiumBattery",
	"LabelParts": [["LithiumBattery", "researches"]],
	"RequiredResearch": ["LithiumPlate"],
	"Levels": [5,5],
	"Unlocks": [[assembler_r_dict, "LithiumBattery"]],
	"CostMul": 0.75,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "RareEarthSludge",
	"LabelParts": [["RareEarthSludge", "parts"]],
	"RequiredResearch": ["SulfuricAcid"],
	"Levels": [4,4],
	"Unlocks": [["IndustrialChemReactor" + r_dict, "RareEarthSludge"]],
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
	"Name": "QuantumProcessor",
	"LabelParts": [["QuantumProcessor", "parts"]],
	"RequiredResearch": ["QuantumCircuit"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + r_dict, "QuantumProcessor"],[assembler_r_dict, "QuantumProcessor"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumBrain",
	"LabelParts": [["QuantumBrain", "parts"]],
	"RequiredResearch": ["QuantumProcessor"],
	"Levels": [6,6],
	"Unlocks": [["Hand" + r_dict, "QuantumBrain"],[assembler_r_dict, "QuantumBrain"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "MetalConstructions",
	"LabelParts": [["MetalConstructions", "researches"]],
	"RequiredResearch": ["Metalwork"],
	"Unlocks": [["Hand" + r_dict, "%Material%Corner"] ,
	["Hand" + r_dict, "%Material%Casing"] ,
	["Hand" + r_dict, "%Material%Beam"] ],
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
	"Name": "Chemistry",
	"LabelParts": [["Chemistry", "researches"]],
	"RequiredResearch": ["ElectricEngine"],
	"Unlocks": [["Hand" + r_dict, "%Material%ChemReactor"] ],
	"Levels": [2,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialChemReactor",
	"LabelParts": [["IndustrialChemReactor", "machines"]],
	"RequiredResearch": ["Chemistry"],
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
	"RequiredResearch": ["Chemistry"],
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
	"CostMul": 2
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
	"RequiredResearch": ["OreWasher"],
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
	"RequiredResearch": ["Chemistry", "AluminiumProduction", "Separator"],
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
	"Name": "CompositeMaterials",
	"LabelParts": [["CompositeMaterials", "parts"]],
	"RequiredResearch": ["TitaniumProduction", "LithiumPlate", "CarbonFiberSheet"],
	"Levels": [6,6],
	"Unlocks": [[assembler_r_dict, "CompositePlate"]],
	"MainResearch": True,
	"CostMul": 2.25
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FusionReactor",
	"LabelParts": [["FusionReactor", "machines"]],
	"RequiredResearch": ["CompositeMaterials"],
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
	"RequiredResearch": ["Chemistry"],
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
	"Name": "SteamPyrolysis",
	"LabelParts": [["SteamPyrolysis", "researches"]],
	"RequiredResearch": ["PreciseTemperaturePyrolysis"],
	"Unlocks": [["PyrolysisUnit" + r_dict, "RawOilSteam"],["PyrolysisUnit" + r_dict, "HeavyOilSteam"],["PyrolysisUnit" + r_dict, "GasolineSteam"],["PyrolysisUnit" + r_dict, "MethaneSteam"]],
	"Levels": [5,5]
})
	
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood",
	"RequiredResearch": ["Cutting"],
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
	"RequiredResearch": ["Chemistry", "PyrolysisUnit", "DecorativeWood3"],
	"Unlocks": [["Hand" + r_dict, "PlasticWindow"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PlasticBlock",
	"LabelParts": [["PlasticBlock", "misc"]],
	"RequiredResearch": ["DecorativePlastic"], 
	"Unlocks": [["Hand" + r_dict, "PlasticBlock"],["Press" + r_dict, "PlasticBlock"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BasicPlatform",
	"LabelParts": [["BasicPlatform", "misc"]],
	"CompleteByDefault": True,
	"Unlocks": [["Hand" + r_dict, "BasicPlatform"], ["Press" + r_dict, "BasicPlatform"]],
	"RequiredResearch": ["MineralsScan"]
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone",
	"LabelParts": [["DecorativeStone", "researches"]],
	"RequiredResearch": ["Press"], 
	"Unlocks": [["Hand" + r_dict, "StoneTiles"], ["CuttingMachine" + r_dict, "StoneTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone2",
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[1], "common"]],
	"RequiredResearch": ["DecorativeStone"], 
	"Unlocks": [["Hand" + r_dict, "DarkTiles"],["Hand" + r_dict, "RedTiles"],["CuttingMachine" + r_dict, "DarkTiles"],["CuttingMachine" + r_dict, "RedTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GlassBlock",
	"LabelParts": [["GlassBlock", "misc"]],
	"RequiredResearch": ["Press"], 
	"Unlocks": [["Hand" + r_dict, "GlassBlock"],["Press" + r_dict, "GlassBlock"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone3",
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[2], "common"]],

	"RequiredResearch": ["DecorativeStone2"], 
	"Unlocks": [["Hand" + r_dict, "DarkBricks"],["Hand" + r_dict, "RedBricks"],["Hand" + r_dict, "Bricks"],["CuttingMachine" + r_dict, "DarkBricks"],["CuttingMachine" + r_dict, "RedBricks"],["CuttingMachine" + r_dict, "Bricks"]],
	
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone4",
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[3], "common"]],
	"RequiredResearch": ["DecorativeStone3"], 
	"Unlocks": [["Hand" + r_dict, "Stairs"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeConcrete",
	"LabelParts": [["DecorativeConcrete", "researches"]],
	"RequiredResearch": ["Mixer"], 
	"Unlocks": [["Hand" + r_dict, "ConcreteTiles"], ["CuttingMachine" + r_dict, "ConcreteTiles"],
			 ["Hand" + r_dict, "ConcreteBeam"], ["Press" + r_dict, "ConcreteBeam"]],
	"Levels": [1, 2],
})

for index, crafter, item, crafter2 in [
		(1, "Hand", "ConcreteSmallTiles", "CuttingMachine"), 
		(2, "Hand", "ConcreteBeam2", "Press"),
        (3, "Hand", "ConcreteRamp3", "Press"),
        (4, "Hand", "ConcreteRamp", "Press"),
        (5, "Hand", "ConcreteRamp2", "Press"),
        (6, "Hand", "DangerBlock", "Press")
	]:
	append_levels({
		"Class": "StaticResearch",
		"Name": "DecorativeConcrete" + item,
		"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[index], "common"]],
		"RequiredResearch": ["DecorativeConcrete"], 
		"Unlocks": [[crafter + r_dict, item], [crafter2 + r_dict, item]],
		"Levels": [3, 3],
	})
     
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete",
	"LabelParts": [["ReinforcedConcrete", "researches"]],
	"RequiredResearch": ["DecorativeConcrete"], 
	"Unlocks": [["Hand" + r_dict, "ReinforcedConcreteTiles"], ["CuttingMachine" + r_dict, "ReinforcedConcreteTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete2",
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[1], "common"]],

	"RequiredResearch": ["DecorativeReinforcedConcrete"], 
	"Unlocks": [["Hand" + r_dict, "ReinforcedConcreteSmallTiles"], ["CuttingMachine" + r_dict, "ReinforcedConcreteSmallTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete3",
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[2], "common"]],
	"RequiredResearch": ["DecorativeReinforcedConcrete2"], 
	"Unlocks": [["Hand" + r_dict, "ReinforcedConcreteBricks"], ["CuttingMachine" + r_dict, "ReinforcedConcreteBricks"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorationClay",
	"LabelParts": [["DecorationClay", "researches"]],
	"RequiredResearch": ["Oven"], 
	"Unlocks": [["Hand" + r_dict, "TerracottaTiles"], ["CuttingMachine" + r_dict, "TerracottaTiles"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorationClay2",
	"LabelParts": [["DecorationClay", "researches"], [level_labels[1], "common"]],
	"RequiredResearch": ["DecorationClay"], 
	"Unlocks": [["Hand" + r_dict, "TerracottaBricks"], ["CuttingMachine" + r_dict, "TerracottaBricks"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Press",
	"LabelParts": [["Press", "machines"]],
	"RequiredResearch": ["SteelProduction"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + r_dict, "%Material%Press"] ],
})
append_levels({
	"Class": "StaticResearchToolUnlock",
	"Name": "PaintTool",
	"LabelParts": [["PaintTool", "parts"]],
	"RequiredResearch": ["Press"],
	"Levels": [1,1],
	"Unlocks": [],
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
	"Name": "Column",
	"LabelParts": [["Column", "misc"]],
	"RequiredResearch": ["DecorativeStone"],
	"Levels": [1,1],
	"Unlocks": [["Hand" + r_dict, "Column"],["Hand" + r_dict, "FluetedColumn"],["Press" + r_dict, "Column"],["Press" + r_dict, "FluetedColumn"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sign",
	"LabelParts": [["Sign", "machines"]],
	"RequiredResearch": ["Press"],
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
csv.append(["Electrolysis", "Electrolysis"])
csv.append(["Sign", "Sign"])
csv.append(["Cutting", "Cutting"])
csv.append(["SteelProduction", "Steel Production"])
csv.append(["AutomaticMining", "Automatic Mining"])
csv.append(["MetalConstructions", "Metal Constructions"])	
csv.append(["Chemistry", "Chemistry"])
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
csv.append(["DecorativeWood", "Decorative Wood"])
csv.append(["DecorativePlastic", "Decorative Plastic"])
csv.append(["DecorativeStone", "Decorative Stone"])
csv.append(["DecorativeConcrete", "Decorative Concrete"])
csv.append(["DecorationClay", "Decoration Clay"])
csv.append(["ReinforcedConcrete", "Decorative Reinforced Concrete"])
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

write_file("Generated/Researches/basic.json", data)
write_file("Loc/source/researches.json", csv)
