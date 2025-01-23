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
	"HardMetalProduction",
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
	"Unlocks": [["Hand" + base_recipe, tier_material[0] + "Furnace"],["Hand" + base_recipe, "SandSurface"],["Hand" + base_recipe, "GravelSurface"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdditionalStorage",
	"LabelParts": [["AdditionalStorage", "researches"]],
	"RequiredResearch": ["MineralsScan"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Chest"] ],
	"Levels":[0,7],
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SingleTypeStorage",
	"LabelParts": [["SingleTypeStorage", "researches"]],
	"RequiredResearch": ["AdditionalStorage" ],
	
	"Levels":[1,7],
	
	"Unlocks": [["Hand" + base_recipe, "%Material%ItemRack"] ],
})
append_levels({
	"Class": "StaticResearchBonusInventory",
	"Name": "InventoryUpgrade",
	"LabelParts": [["InventoryUpgrade", "researches"]],
	"RequiredResearchArr": [["AdditionalStorage"],["AdditionalStorage1"],["AdditionalStorage2"],["AdditionalStorage3"],["AdditionalStorage4"],["AdditionalStorage5"],["AdditionalStorage6"],[],[],[],[],[],[],[]],
	"Unlocks": [],
	"Levels": [0,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Electricity",
	"LabelParts": [["Electricity", "researches"]],
	"RequiredResearch": ["MineralScan"+static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[1] + "Connector"],["Hand" + base_recipe, tier_material[1] + "HandGenerator"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricFurnace",
	"LabelParts": [["ElectricFurnace", "machines"]],
	"Levels": [2,7],
	"RequiredResearch": ["CopperWire"],
	"Unlocks": [["Hand" + base_recipe, "%Material%ElectricFurnace"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricalSwitch",
	"LabelParts": [["ElectricalSwitch", "machines"]],
	"RequiredResearch": ["CopperWire"],
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "ElectricalSwitch"]],
	"Levels": [2,2],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Diode",
	"LabelParts": [["Diode", "machines"]],
	
	"RequiredResearch": ["ElectricalSwitch"],
	"Levels": [2,7],
	
	"Unlocks": [["Hand" + base_recipe, "%Material%Diode"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PowerGeneration",
	"LabelParts": [["PowerGeneration", "researches"]],
	"RequiredResearch": ["Electricity"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CompactGenerator"] ],
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Electrolysis",
	"LabelParts": [["Electrolysis", "researches"]],
	"RequiredResearch": ["SteelProduction"], 
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Electrolyzer"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SteelProduction",
	"LabelParts": [["SteelProduction", "researches"]],
	"RequiredResearch": ["Drying"+static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BlastFurnace"] ],
	"AlsoUnlocks": get_parts_unlocks(tier_material[2]),
	"MainResearch": True,
	"CostMul": 5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSmelting",
	"LabelParts": [["AdvancedSmelting", "researches"]],
	"RequiredResearch": ["SteelProduction"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ArcSmelter"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SolarPanel",
	"LabelParts": [["SolarPanel", "machines"]],
	"RequiredResearch": ["SiliconWafer"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%SolarPanel"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AluminiumProduction",
	"LabelParts": [["AluminiumProduction", "researches"]],
	"RequiredResearch": ["AdvancedSmelting", "Electrolysis"],
	"Unlocks": get_parts_unlocks(tier_material[3]),
	"Levels": [3,3],
	"CostLevelOffset": -1,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GasTurbine",
	"LabelParts": [["GasTurbine", "machines"]],
	"RequiredResearch": ["MassivePowerGeneration"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%GasTurbine"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Smelting",
	"LabelParts": [["Smelting", "researches"]],
	"RequiredResearch": ["MineralsScan"+static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Smelter"]],
	"Levels": [0,2],
	"CompleteByDefault": True,
	"MainResearch": True
})
append_equipment([-1,3], append_levels, researches)
append_levels({
	"Class": "StaticResearch",
	"Name": "Metalwork",
	"LabelParts": [["Metalwork", "researches"]],
	"RequiredResearch": ["Smelting"+static_research],
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
	"Unlocks": [["Hand" + base_recipe, tier_material[1] + "Vent"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BasicMachines",
	"LabelParts": [["BasicMachines", "researches"]],
	"RequiredResearch": ["Metalwork"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Macerator"],
	["Hand" + base_recipe, "%Material%AutomaticHammer"]],
	"CostMul":0.25,
	"MainResearch": True,
	"Description": [["BasicMachinesDescription", "ui"]]
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Flywheel",
	"LabelParts": [["Flywheel", "machines"]],
	"RequiredResearch": ["BasicMachines"],
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "Flywheel"]],
	"Levels": [2,2],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Destroyer",
	"LabelParts": [["Destroyer", "machines"]],
	"Levels": [1,7],
	"RequiredResearch": ["Furnace"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Destroyer"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Pump",
	"LabelParts": [["Pump", "machines"]],
	"RequiredResearch": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Pump"] ],
	"CostMul":0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Container",
	"LabelParts": [["Container", "machines"]],
	"RequiredResearch": ["Pump"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Container"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FluidFurnace",
	"LabelParts": [["FluidFurnace", "machines"]],
	"RequiredResearch": ["Furnace"],
	"Unlocks": [["Hand" + base_recipe, "%Material%FluidFurnace"] ],
	"Levels": [1,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Automatization",
	"LabelParts": [["Automatization", "researches"]],
	"RequiredResearch": ["BasicMachines"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%RobotArm"],
	["Hand" + base_recipe, "%Material%Conveyor"],
	["Hand" + base_recipe, "%Material%Splitter"]],
	"CostMul":0.25,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OverflowPump",
	"LabelParts": [["OverflowPump", "machines"]],
	"RequiredResearch": ["Pump"],
	"Unlocks": [["Hand" + base_recipe, "%Material%OverflowPump"]],
	"Levels": [1,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AutomaticMining",
	"LabelParts": [["AutomaticMining", "researches"]],
	"RequiredResearch": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%DrillingRig"] ],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Cutting",
	"LabelParts": [["Cutting", "researches"]],
	"RequiredResearch": ["BasicMachines"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CuttingMachine"] ],
	"MainResearch": True,
	"CostMul":0.25,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Pumpjack",
	"LabelParts": [["Pumpjack", "machines"]],
	"RequiredResearch": ["AutomaticMining"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Pumpjack"] ],
	"Levels": [3,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AutomaticFarm",
	"LabelParts": [["AutomaticFarm", "machines"]],
	"RequiredResearch": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%AutomaticFarm"] ],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HeatTransferring",
	"LabelParts": [["HeatTransferring", "researches"]],
	"RequiredResearch": ["Smelting"],
	"Unlocks": [["Hand" + base_recipe, "%Material%HeatPipe"] ],
	"Levels":[1,1],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "KineticHeater",
	"LabelParts": [["KineticHeater", "machines"]],
	"RequiredResearch": ["HeatTransferring"],
	"Unlocks": [["Hand" + base_recipe, "%Material%KineticHeater"] ],
	"Levels":[1,7],
	"CostMul":1,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Radiator",
	"LabelParts": [["Radiator", "machines"]],
	"RequiredResearch": ["HeatTransferring"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Radiator"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AtmosphericCondenser",
	"LabelParts": [["AtmosphericCondenser", "machines"]],
	"RequiredResearch": ["AutomaticFarm"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%AtmosphericCondenser"] ],
	"CostMul":0.5,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "StirlingEngine",
	"LabelParts": [["StirlingEngine", "machines"]],
	"RequiredResearch": ["MineralsScan"+static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%StirlingEngine"] ],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Drying",
	"LabelParts": [["Drying", "researches"]],
	"RequiredResearch": ["Furnace",],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Oven"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DistributedComputing",
	"LabelParts": [["DistributedComputing", "researches"]],
	"RequiredResearchArr": [["PowerGeneration"], ["AdvancedCircuit"], ["Processor"], ["QuantumCircuit"], ["QuantumProcessor"], ["QuantumBrain"]],
	"Unlocks": [["Hand" + base_recipe, "%Material%Computer"] ],
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
	"Unlocks": [["Hand" + base_recipe, "CopperWire"],["Assembler" + base_recipe, "CopperWire"]],
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
	"Unlocks": [["Hand" + base_recipe, "CircuitBoard"]],
	"CostMul":0.25,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Circuit",
	"LabelParts": [["Circuit", "parts"]],
	"RequiredResearch": ["CircuitBoard"],
	"Unlocks": [["Hand" + base_recipe, "Circuit"],["Assembler" + base_recipe, "Circuit"]],
	"Levels": [1,1],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Furnace",
	"LabelParts": [["Furnace", "machines"]],
	"RequiredResearch": ["StirlingEngine"],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Furnace"] ],
	"MainResearchArr": [True,True,True,True,True,True,True],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "MassivePowerGeneration",
	"LabelParts": [["MassivePowerGeneration", "researches"]],
	"RequiredResearch": ["PowerGeneration" ],
	"Unlocks": [["Hand" + base_recipe, "%Material%Generator"] ,
	["Hand" + base_recipe, "%Material%Boiler"] ,
	["Hand" + base_recipe, "%Material%SteamTurbine"] ],
	"Levels": [2,7],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "LogicCircuit",
	"LabelParts": [["LogicCircuit", "machines"]],
	"RequiredResearch": ["Circuit"],
	"Unlocks": [["Hand" + base_recipe, "SteelLogicCircuit"] ,
	["Hand" + base_recipe, "SteelLogicController"] ,
	["Hand" + base_recipe, "SteelLogicInterface"] ,
	["Hand" + base_recipe, "SteelLogicDisplay"] ,
	["Hand" + base_recipe, "SteelLogicWire"] ],
	"Levels": [2,2],
	"CostMul": 1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedCircuit",
	"LabelParts": [["AdvancedCircuit", "parts"]],
	"RequiredResearch": ["Separator", "Circuit"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + base_recipe, "AdvancedCircuit"],["Assembler" + base_recipe, "AdvancedCircuit"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GoldWire",
	"LabelParts": [["GoldWire", "parts"]],
	"RequiredResearch": ["AdvancedCircuit", "OreWasher"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + base_recipe, "GoldWire"],["Assembler" + base_recipe, "GoldWire"]],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedCircuitBoard",
	"LabelParts": [["AdvancedCircuitBoard", "parts"]],
	"RequiredResearch": ["GoldWire", "PyrolysisUnit"],
	"Levels": [3,3],
	"Unlocks": [["Hand" + base_recipe, "AdvancedCircuitBoard"],["Assembler" + base_recipe, "AdvancedCircuitBoard"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SiliconWafer",
	"LabelParts": [["SiliconWafer", "parts"]],
	"RequiredResearch": ["AdvancedCircuit"],
	"Unlocks": [["Assembler" + base_recipe, "SiliconWafer"]],
	"Levels": [3,3],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Processor",
	"LabelParts": [["Processor", "parts"]],
	"RequiredResearch": ["SiliconWafer", "AdvancedCircuitBoard"],
	"Unlocks": [["Hand" + base_recipe, "Processor"],["Assembler" + base_recipe, "Processor"],["Assembler" + base_recipe, "Processor2"]],
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
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "Sulfur"]],
	"MainResearch": True,
	"CostMul": 0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SulfuricAcid",
	"LabelParts": [["SulfuricAcidSynthesis", "researches"]],
	"RequiredResearch": ["Sulfur"],
	"Levels": [4,4],
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "SulfuricAcid"]],
	"MainResearch": True,
	"CostMul": 0.75,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "NitricAcid",
	"LabelParts": [["NitricAcid", "parts"]],
	"RequiredResearch": ["IndustrialChemReactor"],
	"Levels": [4,4],
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "NitricAcid"]],
	"CostMul": 0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "RareEarthElement",
	"LabelParts": [["RareEarthElement", "parts"]],
	"RequiredResearch": ["ChemicalBath", "SulfuricAcid"],
	"Levels": [4,4],
	"Unlocks": [["ChemicalBath" + base_recipe, "RareEarthElement"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumCore",
	"LabelParts": [["QuantumCore", "parts"]],
	"RequiredResearch": ["Processor", "RareEarthElement"],
	"Levels": [4,4],
	"Unlocks": [["Hand" + base_recipe, "QuantumCore"],["Assembler" + base_recipe, "QuantumCore"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumCircuit",
	"LabelParts": [["QuantumCircuit", "parts"]],
	"RequiredResearch": ["QuantumCore"],
	"Levels": [4,4],
	"Unlocks": [["Hand" + base_recipe, "QuantumCircuit"],["Assembler" + base_recipe, "QuantumCircuit"]],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumProcessor",
	"LabelParts": [["QuantumProcessor", "parts"]],
	"RequiredResearch": ["QuantumCircuit"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + base_recipe, "QuantumProcessor"],["Assembler" + base_recipe, "QuantumProcessor"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumBrain",
	"LabelParts": [["QuantumBrain", "parts"]],
	"RequiredResearch": ["QuantumProcessor"],
	"Levels": [6,6],
	"Unlocks": [["Hand" + base_recipe, "QuantumBrain"],["Assembler" + base_recipe, "QuantumBrain"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "MetalConstructions",
	"LabelParts": [["MetalConstructions", "researches"]],
	"RequiredResearch": ["Metalwork"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Corner"] ,
	["Hand" + base_recipe, "%Material%Casing"] ,
	["Hand" + base_recipe, "%Material%Beam"] ],
	"Levels": [1,7],
	"Chapter":"Decorations"+static_chapter,
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Scaffold",
	"LabelParts": [["Scaffold", "researches"]],
	"RequiredResearch": ["MetalConstructions"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Scaffold"] ],
	"Levels": [1,7],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Chemistry",
	"LabelParts": [["Chemistry", "researches"]],
	"RequiredResearch": ["ElectricEngine"],
	"Unlocks": [["Hand" + base_recipe, "%Material%ChemReactor"] ],
	"Levels": [2,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialChemReactor",
	"LabelParts": [["IndustrialChemReactor", "machines"]],
	"RequiredResearch": ["Chemistry"],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialChemReactor"] ],
	"Levels": [3,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Catalyst",
	"LabelParts": [["Catalyst", "parts"]],
	"RequiredResearch": ["IndustrialChemReactor"],
	"Unlocks": [["Hand" + base_recipe, "Catalyst"],["Assembler" + base_recipe, "Catalyst"]],
	"Levels": [2,2],
	"MainResearch": True,
	"CostMul":5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FuelChemistry",
	"LabelParts": [["FuelChemistry", "researches"]],
	"RequiredResearch": ["Catalyst"],
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "Superfuel"], ["IndustrialChemReactor" + base_recipe, "RocketFuel"]],
	"Levels": [3,3],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FuelChemistry2",
	"LabelParts": [["FuelChemistry2", "researches"]],
	"RequiredResearch": ["FuelChemistry"],
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "RocketFuel2"], ["IndustrialChemReactor" + base_recipe, "Superfuel2"]],
	"Levels": [3,3],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sifter",
	"LabelParts": [["Sifter", "machines"]],
	"RequiredResearch": ["Chemistry"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Sifter"] ],
	"Levels": [3,7],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Separator",
	"LabelParts": [["Separator", "machines"]],
	"RequiredResearch": ["ElectricEngine"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Separator"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricEngine",
	"LabelParts": [["ElectricEngine", "machines"]],
	"RequiredResearch": ["Electrolysis"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ElectricEngine"] ],
	"MainResearchArr": [True, True, False, False, False, False, False],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BiElectricEngine",
	"LabelParts": [["BiElectricEngine", "machines"]],
	"RequiredResearch": ["ElectricEngine"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BiElectricEngine"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OreWasher",
	"LabelParts": [["OreWasher", "machines"]],
	"Levels": [2,7],
	"RequiredResearch": ["Separator"],
	"Unlocks": [["Hand" + base_recipe, "%Material%OreWasher"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Mixer",
	"LabelParts": [["Mixer", "machines"]],
	"RequiredResearch": ["OreWasher"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Mixer"] ],
	"MainResearch": True,
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ChemicalBath",
	"LabelParts": [["ChemicalBath", "machines"]],
	"RequiredResearch": ["IndustrialChemReactor"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ChemicalBath"] ],
	"MainResearch": True,
	"CostMul":5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OilCrackingTower",
	"LabelParts": [["OilCrackingTower", "machines"]],
	"RequiredResearch": ["FuelChemistry"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%OilCrackingTower"] ],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CombustionEngine",
	"LabelParts": [["CombustionEngine", "machines"]],
	"RequiredResearch": ["Catalyst"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CombustionEngine"] ],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "StainlessSteelProduction",
	"LabelParts": [["StainlessSteelProduction", "researches"]],
	"RequiredResearch": ["Chemistry", "AluminiumProduction", "AdvancedSeparation"],
	"Unlocks": get_parts_unlocks(tier_material[4]),
	"AlsoUnlocks": [["Hand" + base_recipe, "Cell"]],
	"Levels": [4,4],
	"CostLevelOffset": -1,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSeparation",
	"LabelParts": [["AdvancedSeparation", "researches"]],
	"RequiredResearch": ["AluminiumProduction", "ElectricEngine1"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSeparator"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SmallBattery",
	"LabelParts": [["SmallBattery", "machines"]],
	"RequiredResearch": ["AluminiumProduction"],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%SmallBattery"] ],
	"MainResearch": True,
	"CostMul":1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BatteryBox",
	"LabelParts": [["BatteryBox", "machines"]],
	"RequiredResearch": ["SmallBattery"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BatteryBox"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "TitaniumProduction",
	"LabelParts": [["TitaniumProduction", "researches"]],
	"RequiredResearch": ["IndustrialSmelting"],
	"Unlocks": get_parts_unlocks(tier_material[5]),
	"Levels": [5,5],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialBoiler",
	"LabelParts": [["IndustrialBoiler", "machines"]],
	"RequiredResearch": ["TitaniumProduction"],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialBoiler"],["Connector" + base_recipe, "%Material%IndustrialBoiler"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialSteamTurbine",
	"LabelParts": [["IndustrialSteamTurbine", "machines"]],
	"RequiredResearch": ["IndustrialBoiler"],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSteamTurbine"],["Connector" + base_recipe, "%Material%IndustrialSteamTurbine"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialGenerator",
	"LabelParts": [["IndustrialGenerator", "machines"]],
	"RequiredResearch": ["IndustrialSteamTurbine"],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialGenerator"],["Connector" + base_recipe, "%Material%IndustrialGenerator"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Freezer",
	"LabelParts": [["Freezer", "machines"]],
	"RequiredResearch": ["TitaniumProduction"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Freezer"] ],
	"Levels": [5,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HardMetalProduction",
	"LabelParts": [["HardMetalProduction", "researches"]],
	"RequiredResearch": ["Freezer"],
	"Unlocks": get_parts_unlocks(tier_material[6]),
	"Levels": [5,5],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FusionReactor",
	"LabelParts": [["FusionReactor", "machines"]],
	"RequiredResearch": ["HardMetalProduction"],
	"Unlocks": [["Hand" + base_recipe, "%Material%FusionReactor"] ],
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
	"Unlocks": [["Hand" + base_recipe, "UltimateCatalyst"],["Assembler" + base_recipe, "UltimateCatalyst"]],
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	 "Class": "StaticResearch",
	 "Name": "Portal",
	 "LabelParts": [["Portal", "machines"]],
	 "RequiredResearch": ["UltimateCatalyst", "QuantumBrain"],
	 "Unlocks": [["Hand" + base_recipe, "%Material%Portal"] ],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%FissionReactor"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "UraniumCell",
	"LabelParts": [["UraniumCell", "parts"]],
	"RequiredResearch": ["TitaniumProduction"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + base_recipe, "UraniumCell"],["Assembler" + base_recipe, "UraniumCell"]],
})
append_nuclear([7,-7], append_levels, researches)
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialSmelting",
	"LabelParts": [["IndustrialSmelting", "researches"]],
	"RequiredResearch": ["StainlessSteelProduction"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSmelter"] ],
	"MainResearch": True,
	"CostMul":5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fermentation",
	"LabelParts": [["Fermentation", "researches"]],
	"Levels": [3,7],
	"RequiredResearch": ["Chemistry"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Fermenter"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "InductionCoil",
	"LabelParts": [["InductionCoil", "machines"]],
	"RequiredResearch": ["IndustrialSmelting"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%InductionCoil"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialElectricEngine",
	"LabelParts": [["IndustrialElectricEngine", "machines"]],
	"RequiredResearch": ["InductionCoil"],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialElectricEngine"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Terminal",
	"LabelParts": [["Terminal", "machines"]],
	"Levels": [4,4],
	"RequiredResearch": ["StainlessSteelProduction"],
	"Unlocks": [["Hand" + base_recipe, tier_material[4] + "Terminal"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FlatTerminal",
	"LabelParts": [["FlatTerminal", "machines"]],
	"Levels": [4,4],
	"RequiredResearch": ["Terminal"],
	"Unlocks": [["Hand" + base_recipe, tier_material[4] + "FlatTerminal"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Constructor",
	"LabelParts": [["Constructor", "machines"]],
	"RequiredResearch": ["Assembler"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Constructor"] ],
	"Levels": [2, 7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Assembler",
	"LabelParts": [["Assembler", "machines"]],
	"RequiredResearch": ["Automatization"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Assembler"] ],
	"Levels": [1,7],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BigTerminal",
	"LabelParts": [["BigTerminal", "machines"]],
	"RequiredResearch": ["Terminal"],
	"Unlocks": [["Hand" + base_recipe, tier_material[5] + "BigTerminal"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BigFlatTerminal",
	"LabelParts": [["BigFlatTerminal", "machines"]],
	"RequiredResearch": ["BigTerminal"],
	"Unlocks": [["Hand" + base_recipe, tier_material[5] + "BigFlatTerminal"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HugeTerminal",
	"LabelParts": [["HugeTerminal", "machines"]],
	"RequiredResearch": ["BigTerminal"],
	"Unlocks": [["Hand" + base_recipe, tier_material[6] + "HugeTerminal"]],
	"Levels": [5,5],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HugeFlatTerminal",
	"LabelParts": [["HugeFlatTerminal", "machines"]],
	"RequiredResearch": ["HugeTerminal"],
	"Unlocks": [["Hand" + base_recipe, tier_material[6] + "HugeFlatTerminal"]],
	"Levels": [5,5],
}) 
append_levels({
	"Class": "StaticResearch",
	"Name": "PyrolysisUnit",
	"LabelParts": [["PyrolysisUnit", "machines"]],
	"RequiredResearch": ["Mixer"],
	"Unlocks": [["Hand" + base_recipe, "%Material%PyrolysisUnit"] ],
	"Levels": [3,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PreciseTemperaturePyrolysis",
	"LabelParts": [["PreciseTemperaturePyrolysis", "researches"]],
	"RequiredResearch": ["PyrolysisUnit"],
	"Unlocks": [["PyrolysisUnit" + base_recipe, "RawOil"]],
	"Levels": [4,4]
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SteamPyrolysis",
	"LabelParts": [["SteamPyrolysis", "researches"]],
	"RequiredResearch": ["PreciseTemperaturePyrolysis"],
	"Unlocks": [["PyrolysisUnit" + base_recipe, "RawOilSteam"],["PyrolysisUnit" + base_recipe, "HeavyOilSteam"],["PyrolysisUnit" + base_recipe, "GasolineSteam"],["PyrolysisUnit" + base_recipe, "MethaneSteam"]],
	"Levels": [5,5]
})
	
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood",
	"RequiredResearch": ["Cutting"],
	"LabelParts": [["DecorativeWood", "researches"]],
	"Unlocks": [["Hand" + base_recipe, "WoodenPlanks"],["Hand" + base_recipe, "WoodenStairs"],["Hand" + base_recipe, "Bed"],["Hand" + base_recipe, "Door"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood2",
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[1], "common"]],
	"RequiredResearch": ["DecorativeWood"],
	"Unlocks": [["Hand" + base_recipe, "Chair"],["Hand" + base_recipe, "Fence"],["Hand" + base_recipe, "Ladder"],["Hand" + base_recipe, "Rack"],["Hand" + base_recipe, "Table"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fence",
	"LabelParts": [["Fence", "misc"]],
	"RequiredResearch": ["DecorativeWood2"],
	"Unlocks": [["Hand" + base_recipe, "SteelFence"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fence1",
	"LabelParts": [["Fence", "misc"], [level_labels[1], "common"]],
	"RequiredResearch": ["Fence"],
	"Unlocks": [["Hand" + base_recipe, "StainlessSteelFence"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood4",
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[3], "common"]],
	"RequiredResearch": ["DecorativeWood2"],
	"Unlocks": [["Hand" + base_recipe, "CopperChair"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood3",
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[2], "common"]],
	"RequiredResearch": ["DecorativeWood2", "AdvancedSmelting"],
	"Unlocks": [["Hand" + base_recipe, "Window"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativePlastic",
	"LabelParts": [["DecorativePlastic", "researches"]],
	"RequiredResearch": ["Chemistry", "PyrolysisUnit", "DecorativeWood3"],
	"Unlocks": [["Hand" + base_recipe, "PlasticWindow"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PlasticBlock",
	"LabelParts": [["PlasticBlock", "misc"]],
	"RequiredResearch": ["DecorativePlastic"], 
	"Unlocks": [["Hand" + base_recipe, "PlasticBlock"],["Press" + base_recipe, "PlasticBlock"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BasicPlatform",
	"LabelParts": [["BasicPlatform", "misc"]],
	"CompleteByDefault": True,
	"Unlocks": [["Hand" + base_recipe, "BasicPlatform"], ["Press" + base_recipe, "BasicPlatform"]],
	"RequiredResearch": []
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone",
	"LabelParts": [["DecorativeStone", "researches"]],
	"RequiredResearch": ["Press"+static_research], 
	"Unlocks": [["Hand" + base_recipe, "StoneTiles"], ["CuttingMachine" + base_recipe, "StoneTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone2",
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[1], "common"]],
	"RequiredResearch": ["DecorativeStone"], 
	"Unlocks": [["Hand" + base_recipe, "DarkTiles"],["Hand" + base_recipe, "RedTiles"],["CuttingMachine" + base_recipe, "DarkTiles"],["CuttingMachine" + base_recipe, "RedTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GlassBlock",
	"LabelParts": [["GlassBlock", "misc"]],
	"RequiredResearch": ["Press"+static_research], 
	"Unlocks": [["Hand" + base_recipe, "GlassBlock"],["Press" + base_recipe, "GlassBlock"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone3",
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[2], "common"]],

	"RequiredResearch": ["DecorativeStone2"], 
	"Unlocks": [["Hand" + base_recipe, "DarkBricks"],["Hand" + base_recipe, "RedBricks"],["Hand" + base_recipe, "Bricks"],["CuttingMachine" + base_recipe, "DarkBricks"],["CuttingMachine" + base_recipe, "RedBricks"],["CuttingMachine" + base_recipe, "Bricks"]],
	
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone4",
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[3], "common"]],
	"RequiredResearch": ["DecorativeStone3"], 
	"Unlocks": [["Hand" + base_recipe, "Stairs"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeConcrete",
	"LabelParts": [["DecorativeConcrete", "researches"]],
	"RequiredResearch": ["Mixer"], 
	"Unlocks": [["Hand" + base_recipe, "ConcreteTiles"], ["CuttingMachine" + base_recipe, "ConcreteTiles"],
			 ["Hand" + base_recipe, "ConcreteBeam"], ["Press" + base_recipe, "ConcreteBeam"]],
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
		"Unlocks": [[crafter + base_recipe, item], [crafter2 + base_recipe, item]],
		"Levels": [3, 3],
	})
     
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete",
	"LabelParts": [["ReinforcedConcrete", "researches"]],
	"RequiredResearch": ["DecorativeConcrete"], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteTiles"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete2",
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[1], "common"]],

	"RequiredResearch": ["DecorativeReinforcedConcrete"], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteSmallTiles"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteSmallTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete3",
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[2], "common"]],
	"RequiredResearch": ["DecorativeReinforcedConcrete2"], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteBricks"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteBricks"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorationClay",
	"LabelParts": [["DecorationClay", "researches"]],
	"RequiredResearch": ["Drying"], 
	"Unlocks": [["Hand" + base_recipe, "TerracottaTiles"], ["CuttingMachine" + base_recipe, "TerracottaTiles"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorationClay2",
	"LabelParts": [["DecorationClay", "researches"], [level_labels[1], "common"]],
	"RequiredResearch": ["DecorationClay"], 
	"Unlocks": [["Hand" + base_recipe, "TerracottaBricks"], ["CuttingMachine" + base_recipe, "TerracottaBricks"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Press",
	"LabelParts": [["Press", "machines"]],
	"RequiredResearch": ["SteelProduction"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Press"] ],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%Lamp"] ],
	"CostMul": 0.1,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Column",
	"LabelParts": [["Column", "misc"]],
	"RequiredResearch": ["DecorativeStone"],
	"Levels": [1,1],
	"Unlocks": [["Hand" + base_recipe, "Column"],["Hand" + base_recipe, "FluetedColumn"],["Press" + base_recipe, "Column"],["Press" + base_recipe, "FluetedColumn"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sign",
	"LabelParts": [["Sign", "machines"]],
	"RequiredResearch": ["Press"],
	"Unlocks": [["Hand" + base_recipe, "%Material%Sign"] ],
	"Levels": [0,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSign",
	"LabelParts": [["AdvancedSign", "machines"]],
	"RequiredResearch": ["Sign"],
	"Unlocks": [["Hand" + base_recipe, "%Material%AdvancedSign"] ],
	"Levels": [2,7]
})
	
data = {
	"Objects": researches
}

csv.append(["InventoryUpgrade", "Inventory Upgrade"])
csv.append(["PlutoniumReaction", "Plutonium Reaction"])
csv.append(["ThoriumReaction", "Thorium Reaction"])
csv.append(["Drying", "Drying"])	
csv.append(["PowerGeneration", "Power Generation"])
csv.append(["Automatization", "Automatization"])
csv.append(["AdditionalStorage", "Additional Storage"])
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
csv.append(["MassivePowerGeneration", "Massive Power Generation"])
csv.append(["AdvancedSmelting", "Advanced Smelting"])
csv.append(["IndustrialSmelting", "Industrial Smelting"])
csv.append(["Fermentation", "Fermentation"])
csv.append(["AdvancedSeparation", "Advanced Separation"])
csv.append(["NeutroniumProduction", "Neutronium Production"])
csv.append(["AluminiumProduction", "Aluminium Production"])
csv.append(["StainlessSteelProduction", "Stainless Steel Production"])
csv.append(["TitaniumProduction", "Titanium Production"])
csv.append(["HardMetalProduction", "Hard Metal Production"])
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

write_file("Generated/Researches/basic.json", data)
write_file("Loc/source/researches.json", csv)
