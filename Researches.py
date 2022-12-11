from Common import *
from Materials import *
import copy
from NuclearResearches import *
from EquipmentResearches import *

researches = []

csv = []

def append_levels(research):
	if "Unlocks" in research:
		unl = copy.deepcopy(research["Unlocks"])
		research["Unlocks"] = []
		
		for i in range(research["Levels"][0] if "Levels" in research else 0, research["Levels"][1] + 1 if "Levels" in research else 1):
			new = []
			for j in unl:
				new.append([j[0], j[1].replace("%Material%", tier_material[i])])				
							
			research["Unlocks"].append(new)
	
	CostSub = research["CostSub"] if "CostSub" in research else 0
	CostMul = research["CostMul"] if "CostMul" in research else 1

	offset = research["CostLevelOffset"] if "CostLevelOffset" in research else 0
	
	research["DataPoints"] = []
	for i in range(research["Levels"][0] if "Levels" in research else 0, research["Levels"][1] + 1 if "Levels" in research else 1):
		research["DataPoints"].append({"Items" : res_cost(i - CostSub + offset, CostMul)})
	
	researches.append(research)

append_levels({
	"Class": static_research,
	"Name": "InitialScan",
	"LabelParts": [["InitialScan", "researches"]],
	"CompleteByDefault": True,
	"Chapter": "Production",
})
append_levels({
	"Class": static_research,
	"Name": "MineralsScan",
	"LabelParts": [["MineralsScan", "researches"]],

	"RequiredResearches": ["InitialScan"],
	"Unlocks": [["Hand", tier_material[0] + "Furnace"],["Constructor", tier_material[0] + "Furnace"],["Hand", "SandSurface"],["Hand", "GravelSurface"]],
	"Collect": { "Items": [
		{
			"Name": "Dirt",
			"Count": 10
		}
	] },
	"Position": [0,1],
	"Chapter": "Production",
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "AdditionalStorage",
	"LabelParts": [["AdditionalStorage", "researches"]],
	"RequiredResearches": ["MineralsScan"],
	"Unlocks": [["Hand", "%Material%Chest"],["Constructor", "%Material%Chest"]],
	"Position": [-1,1],
	"Levels":[0,7],
	"Chapter":"Production",
})
append_levels({
	"Class": static_research,
	"Name": "SingleTypeStorage",
	"LabelParts": [["SingleTypeStorage", "researches"]],
	"RequiredResearches": ["AdditionalStorage" ],
	"Position": [-2,1],
	"Levels":[1,7],
	"Chapter":"Production",
	"Unlocks": [["Hand", "%Material%ItemRack"],["Constructor", "%Material%ItemRack"]],
})
append_levels({
	"Class": "StaticResearchBonusInventory",
	"Name": "InventoryUpgrade",
	"LabelParts": [["InventoryUpgrade", "researches"]],
	"Chapter": "Production",
	"RequiredResearches": ["AdditionalStorage"],
	"Unlocks": [],
	"Position": [-2,2],
	"Levels": [0,7],
})
append_levels({
	"Class": static_research,
	"Name": "Electricity",
	"LabelParts": [["Electricity", "researches"]],
	"RequiredResearches": ["InitialScan"],
	"Unlocks": [["Hand", tier_material[1] + "Connector"], ["Constructor", tier_material[1] + "Connector"]],
	"Collect": { "Items": [
		{
			"Name": "Sand",
			"Count": 10
		}
	] },
	"Position": [0,-1],
	"Chapter": "Production",
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "ElectricFurnace",
	"LabelParts": [["ElectricFurnace", "machines"]],
	"Levels": [2,7],
	"RequiredResearches": ["Electricity"],
	"Position": [-1,-2],
	"Chapter": "Production",
	"Unlocks": [["Hand", "%Material%ElectricFurnace"],["Constructor", "%Material%ElectricFurnace"]],
})
append_levels({
	"Class": static_research,
	"Name": "ElectricalSwitch",
	"LabelParts": [["ElectricalSwitch", "machines"]],
	"RequiredResearches": ["Electricity"],
	"Unlocks": [["Hand", tier_material[2] + "ElectricalSwitch"],["Constructor", tier_material[2] + "ElectricalSwitch"]],
	"Position": [0,-2],
	"Levels": [2,2],
	"Chapter": "Production",
})
append_levels({
	"Class": static_research,
	"Name": "Diode",
	"LabelParts": [["Diode", "machines"]],
	"Position": [0,-3],
	"RequiredResearches": ["Electricity"],
	"Levels": [2,7],
	"Chapter": "Production",
	"Unlocks": [["Hand", "%Material%Diode"],["Constructor", "%Material%Diode"]],
})
append_levels({
	"Class": static_research,
	"Name": "PowerGeneration",
	"LabelParts": [["PowerGeneration", "researches"]],
	"RequiredResearches": ["Electricity"],
	"Levels": [1,1],
	"Unlocks": [["Hand", "%Material%CompactGenerator"],["Constructor", "%Material%CompactGenerator"]],
	"Chapter":"Production",
	"Position": [1,-1],
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "Electrolysis",
	"LabelParts": [["Electrolysis", "researches"]],
	"RequiredResearches": ["SteelProduction"], 
	"Levels": [2,7],
	"Unlocks": [["Hand", "%Material%Electrolyzer"],["Constructor", "%Material%Electrolyzer"]],
	"Chapter": "Production",
	"Position": [4,-1]
})
append_levels({
	"Class": static_research,
	"Name": "SteelProduction",
	"LabelParts": [["SteelProduction", "researches"]],
	"RequiredResearches": ["Drying"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%BlastFurnace"],["Constructor", "%Material%BlastFurnace"]],
	"AlsoUnlocks": [["Hand", "SteelParts"],["Hand", "SteelPlate"],["Hand", "SteelPipe"]],
	"Chapter":"Production",
	"Position": [3, 0],
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedSmelting",
	"LabelParts": [["AdvancedSmelting", "researches"]],
	"RequiredResearches": ["SteelProduction"],
	"Position": [4, 0],
	"Levels": [2,7],
	"Unlocks": [["Hand", "%Material%ArcSmelter"],["Constructor", "%Material%ArcSmelter"]],
	"Chapter":"Production",
})
append_levels({
	"Class": static_research,
	"Name": "SolarPanel",
	"LabelParts": [["SolarPanel", "machines"]],
	"Position": [5, 0],
	"RequiredResearches": ["AluminiumProduction"],
	"Levels": [3,7],
	"Unlocks": [["Hand", "%Material%SolarPanel"],["Constructor", "%Material%SolarPanel"]],
	"Chapter":"Production",
})
append_levels({
	"Class": static_research,
	"Name": "AluminiumProduction",
	"LabelParts": [["AluminiumProduction", "researches"]],
	"RequiredResearches": ["AdvancedSmelting", "Electrolysis"],
	"Unlocks": [["Hand", tier_material[3] + "Parts"],
	["Hand", tier_material[3] + "Plate"],
	["Hand", tier_material[3] + "Pipe"],["Constructor", tier_material[3] + "Pipe"]],
	"Chapter": "Production",
	"Position": [5,-1],
	"Levels": [3,3],
	"CostLevelOffset": -1,
})
append_levels({
	"Class": static_research,
	"Name": "MassivePowerGeneration",
	"LabelParts": [["MassivePowerGeneration", "researches"]],
	"RequiredResearches": ["PowerGeneration" ],
	"Unlocks": [["Hand", "%Material%Generator"],["Constructor", "%Material%Generator"],
	["Hand", "%Material%Boiler"],["Constructor", "%Material%Boiler"],
	["Hand", "%Material%SteamTurbine"],["Constructor", "%Material%SteamTurbine"]],
	"Levels": [2,7],
	"Chapter":"Production",
	"Position": [1,-2],
})
append_levels({
	"Class": static_research,
	"Name": "GasTurbine",
	"LabelParts": [["GasTurbine", "machines"]],
	"Position": [1,-3],
	"RequiredResearches": ["MassivePowerGeneration"],
	"Levels": [4,7],
	"Chapter":"Production",
	"Unlocks": [["Hand", "%Material%GasTurbine"],["Constructor", "%Material%GasTurbine"]],
})
append_levels({
	"Class": static_research,
	"Name": "Smelting",
	"LabelParts": [["Smelting", "researches"]],
	"RequiredResearches": ["MineralsScan"],
	"Unlocks": [["Hand", "%Material%Smelter"], ["Constructor", "%Material%Smelter"]],
	"Levels": [0,2],
	"Position": [0,2],
	"Chapter": "Production",
	"CompleteByDefault": True,
})
append_equipment([-1,3], append_levels, researches)
append_levels({
	"Class": static_research,
	"Name": "Metalwork",
	"LabelParts": [["Metalwork", "researches"]],
	"RequiredResearches": ["Smelting"],
	"Unlocks": [["Hand", "CopperParts"],["Hand", "CopperPlate"],["Hand", "CopperPipe"]],
	"Collect": { "Items": [
		{
			"Name": "CopperOre",
			"Count": 10
		}
	] },
	"Position": [1,2],
	"Levels": [1,1],
	"Chapter": "Production",
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "Valve",
	"LabelParts": [["Vent", "machines"]],
	"RequiredResearches": ["Metalwork"],
	"Unlocks": [["Hand", tier_material[1] + "Vent"],["Constructor", tier_material[1] + "Vent"]],
	"Position": [0,3],
	"Levels": [1,1],
	"Chapter": "Production",
})
append_levels({
	"Class": static_research,
	"Name": "BasicMachines",
	"LabelParts": [["BasicMachines", "researches"]],
	"RequiredResearches": ["Metalwork"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%Macerator"],["Constructor", "%Material%Macerator"],
	["Hand", "%Material%AutomaticHammer"],["Constructor", "%Material%AutomaticHammer"]],
	"Chapter":"Production",
	"Position": [1, 3],
	"CostMul":0.25
})
append_levels({
	"Class": static_research,
	"Name": "Flywheel",
	"LabelParts": [["Flywheel", "machines"]],
	"RequiredResearches": ["BasicMachines"],
	"Unlocks": [["Hand", tier_material[2] + "Flywheel"],["Constructor", tier_material[2] + "Flywheel"]],
	"Levels": [2,2],
	"Chapter":"Production",
	"Position": [0,4],
})
append_levels({
	"Class": static_research,
	"Name": "Cutting",
	"LabelParts": [["Cutting", "researches"]],

	"RequiredResearches": ["BasicMachines"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%CuttingMachine"],["Constructor", "%Material%CuttingMachine"]],
	"Chapter":"Production",
	"Position": [2, 2],
})
append_levels({
	"Class": static_research,
	"Name": "SolidDump",
	"LabelParts": [["SolidDump", "machines"]],
	"Position": [4, 1],
	"Levels": [2,2],
	"Chapter":"Production",
	"RequiredResearches": ["Furnace"],
	"Unlocks": [["Hand", tier_material[2] + "SolidDump"],["Constructor", tier_material[2] + "SolidDump"]],
})
append_levels({
	"Class": static_research,
	"Name": "Pump",
	"LabelParts": [["Pump", "machines"]],
	"RequiredResearches": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%Pump"],["Constructor", "%Material%Pump"]],
	"Chapter":"Production",
	"Position": [3, 2],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "Container",
	"LabelParts": [["Container", "machines"]],
	"RequiredResearches": ["Pump"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%Container"],["Constructor", "%Material%Container"]],
	"Chapter":"Production",
	"Position": [4, 2],
})
append_levels({
	"Class": static_research,
	"Name": "FluidFurnace",
	"LabelParts": [["FluidFurnace", "machines"]],
	"RequiredResearches": ["Furnace"],
	"Unlocks": [["Hand", "%Material%FluidFurnace"],["Constructor", "%Material%FluidFurnace"]],
	"Levels": [1,7],
	"Chapter":"Production",
	"Position": [3, 1],
})
append_levels({
	"Class": static_research,
	"Name": "FluidDumping",
	"LabelParts": [["FluidDumping", "researches"]],
	"RequiredResearches": ["Container"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%FluidDump"],["Constructor", "%Material%FluidDump"]],
	"Chapter":"Production",
	"Position": [5, 2],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "GasDump",
	"LabelParts": [["GasDump", "machines"]],
	"Position": [5, 1],
	"Levels": [2,2],
	"Chapter":"Production",
	"RequiredResearches": ["Container"],
	"Unlocks": [["Hand", tier_material[2] + "GasDump"],["Constructor", tier_material[2] + "GasDump"]],
})
append_levels({
	"Class": static_research,
	"Name": "Automatization",
	"LabelParts": [["Automatization", "researches"]],
	"RequiredResearches": ["BasicMachines"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%RobotArm"],["Constructor", "%Material%RobotArm"],
	["Hand", "%Material%Conveyor"],["Constructor", "%Material%Conveyor"],
	["Hand", "%Material%Splitter"],["Constructor", "%Material%Splitter"]],
	"Chapter":"Production",
	"Position": [2, 3],
	"CostMul":0.25
})
append_levels({
	"Class": static_research,
	"Name": "Filtering",
	"LabelParts": [["Filtering", "researches"]],
	"RequiredResearches": ["Automatization"],
	"Unlocks": [["Hand", "%Material%FilteringRobotArm"],["Constructor", "%Material%FilteringRobotArm"],
	["Hand", "%Material%Sorter"],["Constructor", "%Material%Sorter"]],
	"Levels": [1,7],
	"Chapter": "Production",
	"Position": [3, 3],
})
append_levels({
	"Class": static_research,
	"Name": "FilteringPump",
	"LabelParts": [["FilteringPump", "machines"]],
	"RequiredResearches": ["Pump"],
	"Unlocks": [["Hand", "%Material%FilteringPump"],["Constructor", "%Material%FilteringPump"]],
	"Levels": [1,7],
	"Chapter": "Production",
	"Position": [4, 3],
})
append_levels({
	"Class": static_research,
	"Name": "AutomaticMining",
	"LabelParts": [["AutomaticMining", "researches"]],
	"RequiredResearches": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%DrillingRig"],["Constructor", "%Material%DrillingRig"]],
	"Position": [2, 4],
	"Chapter":"Production",
	"CostMul":0.5
})
append_levels({
	"Class": static_research,
	"Name": "Pumpjack",
	"LabelParts": [["Pumpjack", "machines"]],
	"Position": [2, 5],
	"RequiredResearches": ["AutomaticMining"],
	"Unlocks": [["Hand", "%Material%Pumpjack"],["Constructor", "%Material%Pumpjack"]],
	"Levels": [3,7],
	"Chapter":"Production",
})
append_levels({
	"Class": static_research,
	"Name": "AutomaticFarm",
	"LabelParts": [["AutomaticFarm", "machines"]],
	"RequiredResearches": ["Automatization"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%AutomaticFarm"],["Constructor", "%Material%AutomaticFarm"]],
	"Chapter":"Production",
	"Position": [3,4],
	"CostMul":0.5
})
append_levels({
	"Class": static_research,
	"Name": "HeatTransferring",
	"LabelParts": [["HeatTransferring", "researches"]],
	"RequiredResearches": ["InitialScan"],
	"Unlocks": [["Hand", "%Material%HeatPipe"],["Constructor", "%Material%HeatPipe"]],
	"Position": [-1,-1],
	"Levels":[1,1],
	"Chapter":"Production",
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "Radiator",
	"LabelParts": [["Radiator", "machines"]],
	"RequiredResearches": ["HeatTransferring"],
	"Levels": [3,7],
	"Unlocks": [["Hand", "%Material%Radiator"],["Constructor", "%Material%Radiator"]],
	"Position": [-2,-1],
	"Chapter":"Production",
})
append_levels({
	"Class": static_research,
	"Name": "AtmosphericCondenser",
	"LabelParts": [["AtmosphericCondenser", "machines"]],
	"RequiredResearches": ["InitialScan"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%AtmosphericCondenser"],["Constructor", "%Material%AtmosphericCondenser"]],
	"Chapter":"Production",
	"Position": [-2,0],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "StirlingEngine",
	"LabelParts": [["StirlingEngine", "machines"]],
	"RequiredResearches": ["MineralsScan"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%StirlingEngine"],["Constructor", "%Material%StirlingEngine"]],
	"Chapter":"Production",
	"Position": [1,1],
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "Furnace",
	"LabelParts": [["Furnace", "machines"]],
	"RequiredResearches": ["StirlingEngine"],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%Furnace"],["Constructor", "%Material%Furnace"]],
	"Chapter":"Production",
	"Position": [2, 1],
})
append_levels({
	"Class": static_research,
	"Name": "Drying",
	"LabelParts": [["Drying", "researches"]],
	"RequiredResearches": ["Furnace",],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%Oven"],["Constructor", "%Material%Oven"]],
	"Position": [2,0],
	"Chapter":"Production",
})
append_levels({
	"Class": static_research,
	"Name": "DistributedComputing",
	"LabelParts": [["DistributedComputing", "researches"]],
	"RequiredResearches": ["PowerGeneration"],
	"Unlocks": [["Hand", "%Material%Computer"],["Constructor", "%Material%Computer"]],
	"Levels": [1,7],
	"Chapter":"Production",
	"Position": [2,-1],
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "CopperWire",
	"LabelParts": [["CopperWire", "parts"]],
	"RequiredResearches": ["DistributedComputing"],
	"Levels": [1,1],
	"Unlocks": [["Hand", "CopperWire"],["Assembler", "CopperWire"]],
	"Chapter":"Production",
	"Position": [2,-2],
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "CircuitBoard",
	"LabelParts": [["CircuitBoard", "parts"]],
	"RequiredResearches": ["CopperWire"],
	"Levels": [1,1],
	"Unlocks": [["Hand", "CircuitBoard"]],
	"Chapter":"Production",
	"Position": [2,-3],
	"CostMul":0.25,
})
append_levels({
	"Class": static_research,
	"Name": "Circuit",
	"LabelParts": [["Circuit", "parts"]],
	"RequiredResearches": ["CircuitBoard"],
	"Unlocks": [["Hand", "Circuit"],["Assembler", "Circuit"]],
	"Levels": [1,1],
	"Chapter":"Production",
	"Position": [2,-4],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "LogicCircuit",
	"LabelParts": [["LogicCircuit", "machines"]],
	"RequiredResearches": ["Circuit"],
	"Unlocks": [["Hand", "SteelLogicCircuit"],["Constructor", "SteelLogicCircuit"],
	["Hand", "SteelLogicController"],["Constructor", "SteelLogicController"],
	["Hand", "SteelLogicInterface"],["Constructor", "SteelLogicInterface"],
	["Hand", "SteelLogicDisplay"],["Constructor", "SteelLogicDisplay"],
	["Hand", "SteelLogicWire"],["Constructor", "SteelLogicWire"]],
	"Levels": [1,1],
	"Chapter":"Production",
	"Position": [3,-3],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedCircuit",
	"LabelParts": [["AdvancedCircuit", "parts"]],
	"RequiredResearches": ["Circuit"],
	"Levels": [2,2],
	"Unlocks": [["Hand", "AdvancedCircuit"],["Assembler", "AdvancedCircuit"]],
	"Chapter":"Production",
	"Position": [3,-4],
})
append_levels({
	"Class": static_research,
	"Name": "GoldWire",
	"LabelParts": [["GoldWire", "parts"]],
	"RequiredResearches": ["AdvancedCircuit", "OreWasher"],
	"Levels": [2,2],
	"Unlocks": [["Hand", "GoldWire"],["Assembler", "GoldWire"]],
	"Chapter":"Production",
	"Position": [3,-5],
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedCircuitBoard",
	"LabelParts": [["AdvancedCircuitBoard", "parts"]],
	"RequiredResearches": ["GoldWire", "PyrolysisUnit"],
	"Levels": [2,2],
	"Unlocks": [["Hand", "AdvancedCircuitBoard"],["Assembler", "AdvancedCircuitBoard"]],
	"Chapter":"Production",
	"Position": [3,-6],
})
append_levels({
	"Class": static_research,
	"Name": "Processor",
	"LabelParts": [["Processor", "parts"]],
	"RequiredResearches": ["AdvancedCircuitBoard"],
	"Unlocks": [["Hand", "Processor"],["Assembler", "Processor"],["Assembler", "SiliconWafer"],["Assembler", "Processor2"]],
	"Chapter":"Production",
	"Position": [3,-7],
	"Levels": [3,3],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumCore",
	"LabelParts": [["QuantumCore", "parts"]],
	"RequiredResearches": ["Processor"],
	"Levels": [4,4],
	"Unlocks": [["Hand", "QuantumCore"],["Assembler", "QuantumCore"]],
	"Chapter":"Production",
	"Position": [3,-8],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumCircuit",
	"LabelParts": [["QuantumCircuit", "parts"]],
	"RequiredResearches": ["QuantumCore"],
	"Levels": [4,4],
	"Unlocks": [["Hand", "QuantumCircuit"],["Assembler", "QuantumCircuit"]],
	"Chapter":"Production",
	"Position": [3,-9],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumProcessor",
	"LabelParts": [["QuantumProcessor", "parts"]],
	"RequiredResearches": ["QuantumCircuit"],
	"Levels": [5,5],
	"Unlocks": [["Hand", "QuantumProcessor"],["Assembler", "QuantumProcessor"]],
	"Chapter":"Production",
	"Position": [4,-10],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumBrain",
	"LabelParts": [["QuantumBrain", "parts"]],
	"RequiredResearches": ["QuantumProcessor"],
	"Levels": [6,6],
	"Unlocks": [["Hand", "QuantumBrain"],["Assembler", "QuantumBrain"]],
	"Chapter":"Production",
	"Position": [4,-11],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumComputer",
	"LabelParts": [["QuantumComputer", "machines"]],
	"RequiredResearches": ["QuantumCircuit"],
	"Unlocks": [["Hand", "%Material%QuantumComputer"],["Constructor", "%Material%QuantumComputer"]],
	"Levels": [5,7],
	"Chapter":"Production",
	"Position": [4,-9],
	"CostSub": 1,
})
append_levels({
	"Class": static_research,
	"Name": "MetalConstructions",
	"LabelParts": [["MetalConstructions", "researches"]],
	"RequiredResearches": ["Metalwork"],
	"Unlocks": [["Hand", "%Material%Corner"],["Constructor", "%Material%Corner"],
	["Hand", "%Material%Casing"],["Constructor","%Material%Casing"],
	["Hand", "%Material%Beam"],["Constructor", "%Material%Beam"]],
	"Levels": [1,7],
	"Chapter":"Decorations",
	"Position": [4,3],
})
append_levels({
	"Class": static_research,
	"Name": "Scaffold",
	"LabelParts": [["Scaffold", "researches"]],
	"Chapter": "Decorations",
	"RequiredResearches": ["MetalConstructions"],
	"Unlocks": [["Hand", "%Material%Scaffold"],["Constructor", "%Material%Scaffold"]],
	"Levels": [1,7],
	"Position": [3, 4],
})
append_levels({
	"Class": static_research,
	"Name": "Chemistry",
	"LabelParts": [["Chemistry", "researches"]],
	"Chapter":"Production",
	"RequiredResearches": ["ElectricEngine"],
	"Unlocks": [["Hand", "%Material%ChemReactor"],["Constructor", "%Material%ChemReactor"]],
	"Levels": [2,7],
	"Position": [5,-2],
})
append_levels({
	"Class": static_research,
	"Name": "FilteringUnit",
	"LabelParts": [["FilteringUnit", "machines"]],
	"Chapter":"Production",
	"RequiredResearches": ["Chemistry"],
	"Unlocks": [["Hand", "%Material%FilteringUnit"],["Constructor", "%Material%FilteringUnit"]],
	"Levels": [3,7],
	"Position": [5,-3],
})
append_levels({
	"Class": static_research,
	"Name": "Sifter",
	"LabelParts": [["Sifter", "machines"]],
	"Chapter":"Production",
	"RequiredResearches": ["Chemistry"],
	"Unlocks": [["Hand", "%Material%Sifter"],["Constructor", "%Material%Sifter"]],
	"Levels": [3,7],
	"Position": [6,-3],
})
append_levels({
	"Class": static_research,
	"Name": "Separator",
	"LabelParts": [["Separator", "machines"]],
	"Chapter":"Production",
	"RequiredResearches": ["ElectricEngine"],
	"Levels": [2,7],
	"Unlocks": [["Hand", "%Material%Separator"],["Constructor", "%Material%Separator"]],
	"Position": [4,-3],
})
append_levels({
	"Class": static_research,
	"Name": "ElectricEngine",
	"LabelParts": [["ElectricEngine", "machines"]],
	"Chapter":"Production",
	"RequiredResearches": ["Electrolysis"],
	"Levels": [2,7],
	"Unlocks": [["Hand", "%Material%ElectricEngine"],["Constructor", "%Material%ElectricEngine"]],
	"Position": [4,-2],
})
append_levels({
	"Class": static_research,
	"Name": "OreWasher",
	"LabelParts": [["OreWasher", "machines"]],
	"Levels": [2,7],
	"Chapter":"Production",
	"RequiredResearches": ["Separator"],
	"Unlocks": [["Hand", "%Material%OreWasher"],["Constructor", "%Material%OreWasher"]],
	"Position": [4,-4],
})
append_levels({
	"Class": static_research,
	"Name": "Mixer",
	"LabelParts": [["Mixer", "machines"]],
	"Chapter": "Production",
	"RequiredResearches": ["OreWasher"],
	"Levels": [2,7],
	"Unlocks": [["Hand", "%Material%Mixer"],["Constructor", "%Material%Mixer"]],
	"Position": [4,-5],
})
append_levels({
	"Class": static_research,
	"Name": "ChemicalBath",
	"LabelParts": [["ChemicalBath", "machines"]],
	"Chapter": "Production",
	"RequiredResearches": ["FilteringUnit"],
	"Levels": [3,7],
	"Unlocks": [["Hand", "%Material%ChemicalBath"],["Constructor", "%Material%ChemicalBath"]],
	"Position": [5,-4],
})
append_levels({
	"Class": static_research,
	"Name": "StainlessSteelProduction",
	"LabelParts": [["StainlessSteelProduction", "researches"]],
	"RequiredResearches": ["Chemistry", "AluminiumProduction"],
	"Unlocks": [["Hand", tier_material[4] + "Parts"],
	["Hand", tier_material[4] + "Plate"],
	["Hand", tier_material[4] + "Pipe"],["Constructor", tier_material[4] + "Pipe"]],
	"Chapter": "Production",
	"Position": [6,-2],
	"Levels": [4,4],
	"CostLevelOffset": -1,
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedSeparation",
	"LabelParts": [["AdvancedSeparation", "researches"]],
	"Chapter": "Production",
	"RequiredResearches": ["AluminiumProduction"],
	"Position": [6,-1],
	"Levels": [3,7],
	"Unlocks": [["Hand", "%Material%IndustrialSeparator"],["Constructor", "%Material%IndustrialSeparator"]],
})
append_levels({
	"Class": static_research,
	"Name": "SmallBattery",
	"LabelParts": [["SmallBattery", "machines"]],
	"Chapter": "Production",
	"RequiredResearches": ["AdvancedSeparation"],
	"Position": [6,0],
	"Levels": [3,7],
	"Unlocks": [["Hand", "%Material%SmallBattery"],["Constructor", "%Material%SmallBattery"]],
})
append_levels({
	"Class": static_research,
	"Name": "TitaniumProduction",
	"LabelParts": [["TitaniumProduction", "researches"]],
	"Chapter": "Production",
	"RequiredResearches": ["IndustrialSmelting"],
	"Unlocks": [["Hand", tier_material[5] + "Parts"],
	["Hand", tier_material[5] + "Plate"],
	["Hand", tier_material[5] + "Pipe"],["Constructor", tier_material[5] + "Pipe"]],
	"Position": [7,-4],
	"Levels": [4,4],
	"CostLevelOffset": -1,
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialBoiler",
	"LabelParts": [["IndustrialBoiler", "machines"]],
	"Chapter": "Production",
	"RequiredResearches": ["TitaniumProduction"],
	"Unlocks": [["Hand", "%Material%IndustrialBoiler"],["Connector", "%Material%IndustrialBoiler"]],
	"Position": [6,-4],
	"Levels": [5,7],
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialSteamTurbine",
	"LabelParts": [["IndustrialSteamTurbine", "machines"]],
	"Chapter": "Production",
	"RequiredResearches": ["IndustrialBoiler"],
	"Unlocks": [["Hand", "%Material%IndustrialSteamTurbine"],["Connector", "%Material%IndustrialSteamTurbine"]],
	"Position": [6,-5],
	"Levels": [5,7],
})
append_levels({
	"Class": static_research,
	"Name": "Freezer",
	"LabelParts": [["Freezer", "machines"]],
	"RequiredResearches": ["TitaniumProduction"],
	"Unlocks": [["Hand", "%Material%Freezer"],["Constructor", "%Material%Freezer"]],
	"Chapter": "Production",
	"Position": [8,-4],
	"Levels": [5,7],
})
append_levels({
	"Class": static_research,
	"Name": "HardMetalProduction",
	"LabelParts": [["HardMetalProduction", "researches"]],
	"RequiredResearches": ["Freezer"],
	"Unlocks": [["Hand", tier_material[6] + "Parts"],
	["Hand", tier_material[6] + "Plate"],
	["Hand", tier_material[6] + "Pipe"],["Constructor", tier_material[6] + "Pipe"]],
	"Chapter": "Production",
	"Position": [9,-4],
	"Levels": [5,5],
})
append_levels({
	"Class": static_research,
	"Name": "FusionReactor",
	"LabelParts": [["FusionReactor", "machines"]],
	"RequiredResearches": ["HardMetalProduction"],
	"Unlocks": [["Hand", "%Material%FusionReactor"],["Constructor", "%Material%FusionReactor"]],
	"Chapter":"Production",
	"Position": [10,-4],
	"Levels": [6,7],
})
append_levels({
	"Class": static_research,
	"Name": "NeutroniumProduction",
	"LabelParts": [["NeutroniumProduction", "researches"]],
	"RequiredResearches": ["FusionReactor"],
	"Unlocks": [["Hand", tier_material[7] + "Parts"],
	["Hand", tier_material[7] + "Plate"],
	["Hand", tier_material[7] + "Pipe"],["Constructor", tier_material[7] + "Pipe"]],
	"Chapter": "Production",
	"Position": [11,-4],
	"Levels": [6,6],
})
append_levels({
	 "Class": static_research,
	 "Name": "Portal",
	 "LabelParts": [["Portal", "machines"]],
	 "RequiredResearches": ["NeutroniumProduction"],
	 "Unlocks": [["Hand", "%Material%Portal"],["Constructor", "%Material%Portal"]],
	 "Chapter": "Production",
	 "Position": [12,-4],
	 "Levels": [7,7],
 })
append_levels({
	"Class": static_research,
	"Name": "FissionReactor",
	"LabelParts": [["FissionReactor", "machines"]],
	"Chapter": "Production",
	"RequiredResearches": ["TitaniumProduction"],
	"Levels": [5,7],
	"Unlocks": [["Hand", "%Material%FissionReactor"],["Constructor", "%Material%FissionReactor"]],
	"Position": [7,-6],
})
append_nuclear([7,-7], append_levels, researches)
append_levels({
	"Class": static_research,
	"Name": "IndustrialSmelting",
	"LabelParts": [["IndustrialSmelting", "researches"]],
	"Chapter": "Production",
	"RequiredResearches": ["StainlessSteelProduction"],
	"Levels": [4,7],
	"Unlocks": [["Hand", "%Material%IndustrialSmelter"],["Constructor", "%Material%IndustrialSmelter"]],
	"Position": [7,-2],
})
append_levels({
	"Class": static_research,
	"Name": "Fermentation",
	"LabelParts": [["Fermentation", "researches"]],
	"Levels": [4,7],
	"Chapter": "Production",
	"RequiredResearches": ["IndustrialSmelting"],
	"Position": [7,-3],
	"Unlocks": [["Hand", "%Material%Fermenter"],["Constructor", "%Material%Fermenter"]],
})
append_levels({
	"Class": static_research,
	"Name": "BatteryBox",
	"LabelParts": [["BatteryBox", "machines"]],
	"Chapter": "Production",
	"RequiredResearches": ["IndustrialSmelting"],
	"Position": [8,-2],
	"Levels": [4,7],
	"Unlocks": [["Hand", "%Material%BatteryBox"],["Constructor", "%Material%BatteryBox"]],
})
append_levels({
	"Class": static_research,
	"Name": "InductionCoil",
	"LabelParts": [["InductionCoil", "machines"]],
	"Chapter": "Production",
	"RequiredResearches": ["IndustrialSmelting"],
	"Levels": [4,7],
	"Unlocks": [["Hand", "%Material%InductionCoil"],["Constructor", "%Material%InductionCoil"]],
	"Position": [8,-3],
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialElectricEngine",
	"LabelParts": [["IndustrialElectricEngine", "machines"]],
	"Chapter": "Production",
	"RequiredResearches": ["InductionCoil"],
	"Levels": [4,7],
	"Unlocks": [["Hand", "%Material%IndustrialElectricEngine"],["Constructor", "%Material%IndustrialElectricEngine"]],
	"Position": [9,-3],
})
append_levels({
	"Class": static_research,
	"Name": "Terminal",
	"LabelParts": [["Terminal", "machines"]],
	"Levels": [4,4],
	"Position": [7,-1],
	"Chapter": "Production",
	"RequiredResearches": ["StainlessSteelProduction"],
	"Unlocks": [["Hand", tier_material[4] + "Terminal"],["Constructor", tier_material[4] + "Terminal"]],
})
append_levels({
	"Class": static_research,
	"Name": "FlatTerminal",
	"LabelParts": [["FlatTerminal", "machines"]],
	"Levels": [4,4],
	"Position": [8,-1],
	"Chapter": "Production",
	"RequiredResearches": ["Terminal"],
	"Unlocks": [["Hand", tier_material[4] + "FlatTerminal"],["Constructor", tier_material[4] + "FlatTerminal"]],
})
append_levels({
	"Class": static_research,
	"Name": "Constructor",
	"LabelParts": [["Constructor", "machines"]],
	"Position": [1,5],
	"RequiredResearches": ["Assembler"],
	"Unlocks": [["Hand", "%Material%Constructor"],["Constructor", "%Material%Constructor"]],
	"Levels": [2, 7],
	"Chapter": "Production",
})
append_levels({
	"Class": static_research,
	"Name": "Assembler",
	"LabelParts": [["Assembler", "machines"]],
	"RequiredResearches": ["Automatization"],
	"Unlocks": [["Hand", "%Material%Assembler"],["Constructor", "%Material%Assembler"]],
	"Levels": [1,7],
	"Position": [1, 4],
	"Chapter": "Production",
	"CostMul":0.5
})
append_levels({
	"Class": static_research,
	"Name": "Deconstructor",
	"LabelParts": [["Deconstructor", "machines"]],
	"Position": [0, 5],
	"RequiredResearches": ["Constructor"],
	"Unlocks": [["Hand", "%Material%Deconstructor"],["Constructor", "%Material%Deconstructor"]],
	"Levels": [2,7],
	"Chapter": "Production",
})
append_levels({
	"Class": static_research,
	"Name": "BigTerminal",
	"LabelParts": [["BigTerminal", "machines"]],
	"RequiredResearches": ["Terminal"],
	"Unlocks": [["Hand", tier_material[5] + "BigTerminal"],["Constructor", tier_material[5] + "BigTerminal"]],
	"Levels": [4,4],
	"Chapter": "Production",
	"Position": [7,0],
})
append_levels({
	"Class": static_research,
	"Name": "BigFlatTerminal",
	"LabelParts": [["BigFlatTerminal", "machines"]],
	"RequiredResearches": ["BigTerminal"],
	"Unlocks": [["Hand", tier_material[5] + "BigFlatTerminal"],["Constructor", tier_material[5] + "BigFlatTerminal"]],
	"Chapter": "Production",
	"Levels": [4,4],
	"Position": [8,0],
})
append_levels({
	"Class": static_research,
	"Name": "HugeTerminal",
	"LabelParts": [["HugeTerminal", "machines"]],
	"RequiredResearches": ["BigTerminal"],
	"Unlocks": [["Hand", tier_material[6] + "HugeTerminal"],["Constructor", tier_material[6] + "HugeTerminal"]],
	"Chapter": "Production",
	"Levels": [5,5],
	"Position": [7,1],
})
append_levels({
	"Class": static_research,
	"Name": "HugeFlatTerminal",
	"LabelParts": [["HugeFlatTerminal", "machines"]],
	"RequiredResearches": ["HugeTerminal"],
	"Unlocks": [["Hand", tier_material[6] + "HugeFlatTerminal"],["Constructor", tier_material[6] + "HugeFlatTerminal"]],
	"Chapter": "Production",
	"Levels": [5,5],
	"Position": [8,1],
}) 
append_levels({
	"Class": static_research,
	"Name": "PyrolysisUnit",
	"LabelParts": [["PyrolysisUnit", "machines"]],
	"RequiredResearches": ["Mixer"],
	"Unlocks": [["Hand", "%Material%PyrolysisUnit"],["Constructor", "%Material%PyrolysisUnit"]],
	"Levels": [3,7],
	"Chapter": "Production",
	"Position": [4,-6],
})
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
csv.append(["FluidDumping", "Fluid Dumping"])
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
csv.append(["InitialScan", "Initial Scan"])
csv.append(["MineralsScan", "Minerals Scan"])
csv.append(["Electricity", "Electricity"])
csv.append(["Smelting", "Smelting"])
csv.append(["Metalwork", "Metalwork"])
csv.append(["Filtering", "Filtering"])
csv.append(["DecorativeWood", "Decorative Wood"])
csv.append(["DecorativePlastic", "Decorative Plastic"])
csv.append(["DecorativeStone", "Decorative Stone"])
csv.append(["DecorativeConcrete", "Decorative Concrete"])
csv.append(["DecorationClay", "Decoration Clay"])
csv.append(["ReinforcedConcrete", "Decorative Reinforced Concrete"])
csv.append(["AdvancedReflection", "Advanced Reflection"])
csv.append(["ReactionThrottling", "Reaction Throttling"])
	
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood",
	"LabelParts": [["DecorativeWood", "researches"]],
	"Unlocks": [["Hand", "WoodenPlanks"],["Hand", "WoodenStairs"],["Hand", "Bed"],["Hand", "Door"]],
	"Chapter": "Decorations",
	"Position": [0,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood2",
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[1], "common"]],
	"RequiredResearches": ["DecorativeWood"],
	"Unlocks": [["Hand", "Chair"],["Hand", "Fence"],["Hand", "Ladder"],["Hand", "Rack"],["Hand", "Table"]],
	"Chapter": "Decorations",
	"Position": [0,1],
})
append_levels({
	"Class": static_research,
	"Name": "Fence",
	"LabelParts": [["Fence", "misc"]],
	"RequiredResearches": ["DecorativeWood2"],
	"Unlocks": [["Hand", "SteelFence"]],
	"Chapter": "Decorations",
	"Position": [-1,1],
})
append_levels({
	"Class": static_research,
	"Name": "Fence1",
	"LabelParts": [["Fence", "misc"], [level_labels[1], "common"]],
	"RequiredResearches": ["Fence"],
	"Unlocks": [["Hand", "StainlessSteelFence"]],
	"Chapter": "Decorations",
	"Position": [-2,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood4",
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[3], "common"]],
	"RequiredResearches": ["DecorativeWood2"],
	"Unlocks": [["Hand", "CopperChair"]],
	"Chapter": "Decorations",
	"Position": [1,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood3",
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[2], "common"]],
	"RequiredResearches": ["DecorativeWood2", "AdvancedSmelting"],
	"Unlocks": [["Hand", "Window"]],
	"Chapter": "Decorations",
	"Position": [0,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativePlastic",
	"LabelParts": [["DecorativePlastic", "researches"]],
	"RequiredResearches": ["Chemistry", "PyrolysisUnit", "DecorativeWood3"],

	"Unlocks": [["Hand", "PlasticWindow"]],
	"Chapter": "Decorations",
	"Position": [-1,2],
})
append_levels({
	"Class": static_research,
	"Name": "PlasticBlock",
	"LabelParts": [["PlasticBlock", "misc"]],
	"RequiredResearches": ["DecorativePlastic"], 
	"Unlocks": [["Hand", "PlasticBlock"],["Press", "PlasticBlock"]],
	"Chapter": "Decorations",
	"Position": [-2,2],
})
append_levels({
	"Class": static_research,
	"Name": "BasicPlatform",
	"LabelParts": [["BasicPlatform", "misc"]],
	"CompleteByDefault": True,
	"Chapter": "Decorations",
	"Unlocks": [["Hand", "BasicPlatform"], ["Press", "BasicPlatform"]],
	"Position": [1,-1],
	"RequiredResearches": []
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone",
	"LabelParts": [["DecorativeStone", "researches"]],
	"RequiredResearches": ["BasicPlatform"], 
	"Unlocks": [["Hand", "StoneTiles"], ["CuttingMachine", "StoneTiles"]],
	"Chapter": "Decorations",
	"Position": [1,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone2",
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorativeStone"], 
	"Unlocks": [["Hand", "DarkTiles"],["Hand", "RedTiles"],["CuttingMachine", "DarkTiles"],["CuttingMachine", "RedTiles"]],
	"Chapter": "Decorations",
	"Position": [2,0],
})
append_levels({
	"Class": static_research,
	"Name": "GlassBlock",
	"LabelParts": [["GlassBlock", "misc"]],

	"RequiredResearches": [], 
	"Unlocks": [["Hand", "GlassBlock"],["Press", "GlassBlock"]],
	"Chapter": "Decorations",
	"Position": [2,-1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone3",
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[2], "common"]],

	"RequiredResearches": ["DecorativeStone2"], 
	"Unlocks": [["Hand", "DarkBricks"],["Hand", "RedBricks"],["Hand", "Bricks"],["CuttingMachine", "DarkBricks"],["CuttingMachine", "RedBricks"],["CuttingMachine", "Bricks"]],
	"Chapter": "Decorations",
	"Position": [2,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone4",
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[3], "common"]],

	"RequiredResearches": ["DecorativeStone3"], 
	"Unlocks": [["Hand", "Stairs"]],
	"Chapter": "Decorations",
	"Position": [2,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete",
	"LabelParts": [["DecorativeConcrete", "researches"]],
	"RequiredResearches": ["Mixer"], 
	"Unlocks": [["Hand", "ConcreteTiles"], ["CuttingMachine", "ConcreteTiles"]],
	"Chapter": "Decorations",
	"Position": [3,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete2",
	"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorativeConcrete"], 
	"Unlocks": [["Hand", "ConcreteSmallTiles"], ["CuttingMachine", "ConcreteSmallTiles"]],
	"Chapter": "Decorations",
	"Position": [3,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete3",
	"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[2], "common"]],

	"RequiredResearches": ["DecorativeConcrete2"], 
	"Unlocks": [["Hand", "ConcreteBricks"], ["CuttingMachine", "ConcreteBricks"]],
	"Chapter": "Decorations",
	"Position": [3,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete4",
	"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[3], "common"]],

	"RequiredResearches": ["DecorativeConcrete3"], 
	"Unlocks": [["Hand", "DangerBlock"]],
	"Chapter": "Decorations",
	"Position": [3,3],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeReinforcedConcrete",
	"LabelParts": [["ReinforcedConcrete", "researches"]],

	"RequiredResearches": ["DecorativeConcrete"], 
	"Unlocks": [["Hand", "ReinforcedConcreteTiles"], ["CuttingMachine", "ReinforcedConcreteTiles"]],
	"Chapter": "Decorations",
	"Position": [4,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeReinforcedConcrete2",
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorativeReinforcedConcrete"], 
	"Unlocks": [["Hand", "ReinforcedConcreteSmallTiles"], ["CuttingMachine", "ReinforcedConcreteSmallTiles"]],
	"Chapter": "Decorations",
	"Position": [4,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeReinforcedConcrete3",
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[2], "common"]],

	"RequiredResearches": ["DecorativeReinforcedConcrete2"], 
	"Unlocks": [["Hand", "ReinforcedConcreteBricks"], ["CuttingMachine", "ReinforcedConcreteBricks"]],
	"Chapter": "Decorations",
	"Position": [4,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorationClay",
	"LabelParts": [["DecorationClay", "researches"]],

	"RequiredResearches": ["Drying"], 
	"Unlocks": [["Hand", "TerracottaTiles"], ["CuttingMachine", "TerracottaTiles"]],
	"Chapter": "Decorations",
	"Position": [5,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorationClay2",
	"LabelParts": [["DecorationClay", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorationClay"], 
	"Unlocks": [["Hand", "TerracottaBricks"], ["CuttingMachine", "TerracottaBricks"]],
	"Chapter": "Decorations",
	"Position": [5,1],
})
append_levels({
	"Class": static_research,
	"Name": "Press",
	"LabelParts": [["Press", "machines"]],
	"RequiredResearches": [],
	"Levels": [2,7],
	"Unlocks": [["Hand", "%Material%Press"],["Constructor", "%Material%Press"]],
	"Position": [2, 3],
	"Chapter": "Decorations",
})
append_levels({
	"Class": static_research,
	"Name": "PaintTool",
	"LabelParts": [["PaintTool", "parts"]],
	"RequiredResearches": [],
	"Levels": [1,1],
	"Unlocks": [["Hand", "CopperPaintTool"],["Constructor", "CopperPaintTool"]],
	"Position": [1, 2],
	"Chapter": "Decorations",
})
append_levels({
	"Class": static_research,
	"Name": "Lamp",
	"LabelParts": [["Lamp", "machines"]],
	"RequiredResearches": [],
	"Levels": [1,7],
	"Unlocks": [["Hand", "%Material%Lamp"],["Constructor", "%Material%Lamp"]],
	"Position": [2, 4],
	"Chapter": "Decorations",
})
append_levels({
	"Class": static_research,
	"Name": "Column",
	"LabelParts": [["Column", "misc"]],
	"RequiredResearches": [],
	"Levels": [1,1],
	"Unlocks": [["Hand", "Column"],["Hand", "FluetedColumn"],["Press", "Column"],["Press", "FluetedColumn"]],
	"Position": [1, 4],
	"Chapter": "Decorations",
})
append_levels({
	"Class": static_research,
	"Name": "Sign",
	"LabelParts": [["Sign", "machines"]],
	"RequiredResearches": ["MineralsScan"],
	"Unlocks": [["Hand", "%Material%Sign"],["Constructor", "%Material%Sign"]],
	"Levels": [0,7],
	"Chapter": "Decorations",
	"Position": [0,3],

})
append_levels({
	"Class": static_research,
	"Name": "AdvancedSign",
	"LabelParts": [["AdvancedSign", "machines"]],
	"RequiredResearches": ["Sign"],
	"Unlocks": [["Hand", "%Material%AdvancedSign"],["Constructor", "%Material%AdvancedSign"]],
	"Levels": [2,7],
	"Chapter": "Decorations",
	"Position": [1,3],
})
	
data = {
	"Objects": researches
}

write_file("Generated/Researches/basic.json", data);
write_file("Loc/source/researches.json", csv)
