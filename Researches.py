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
	"Name": "InitialScan" + static_research,
	"LabelParts": [["InitialScan", "researches"]],
	"CompleteByDefault": True,
	"Chapter": "Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "MineralsScan" + static_research,
	"LabelParts": [["MineralsScan", "researches"]],

	"RequiredResearches": ["InitialScan" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[0] + "Furnace"],["Constructor" + recipe_dictionary, tier_material[0] + "Furnace"],["Hand" + recipe_dictionary, "SandSurface"],["Hand" + recipe_dictionary, "GravelSurface"]],
	"Collect": { "Items": [
		{
			"Name": "Dirt" + static_item,
			"Count": 10
		}
	] },
	"Position": [0,1],
	"Chapter": "Production"+static_chapter,
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "AdditionalStorage" + static_research,
	"LabelParts": [["AdditionalStorage", "researches"]],
	"RequiredResearches": ["MineralsScan" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Chest"],["Constructor" + recipe_dictionary, "%Material%Chest"]],
	"Position": [-1,1],
	"Levels":[0,7],
	"Chapter":"Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "SingleTypeStorage" + static_research,
	"LabelParts": [["SingleTypeStorage", "researches"]],
	"RequiredResearches": ["AdditionalStorage" + static_research ],
	"Position": [-2,1],
	"Levels":[1,7],
	"Chapter":"Production"+static_chapter,
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%ItemRack"],["Constructor" + recipe_dictionary, "%Material%ItemRack"]],
})
append_levels({
	"Class": "StaticResearchBonusInventory",
	"Name": "InventoryUpgrade" + static_research,
	"LabelParts": [["InventoryUpgrade", "researches"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["AdditionalStorage" + static_research],
	"Unlocks": [],
	"Position": [-2,2],
	"Levels": [0,7],
})
append_levels({
	"Class": static_research,
	"Name": "Electricity" + static_research,
	"LabelParts": [["Electricity", "researches"]],
	"RequiredResearches": ["InitialScan"+static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[1] + "Connector"], ["Constructor" + recipe_dictionary, tier_material[1] + "Connector"]],
	"Collect": { "Items": [
		{
			"Name": "Sand" + static_item,
			"Count": 10
		}
	] },
	"Position": [0,-1],
	"Chapter": "Production"+static_chapter,
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "ElectricFurnace" + static_research,
	"LabelParts": [["ElectricFurnace", "machines"]],
	"Levels": [2,7],
	"RequiredResearches": ["Electricity" + static_research],
	"Position": [-1,-2],
	"Chapter": "Production"+static_chapter,
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%ElectricFurnace"],["Constructor" + recipe_dictionary, "%Material%ElectricFurnace"]],
})
append_levels({
	"Class": static_research,
	"Name": "ElectricalSwitch" + static_research,
	"LabelParts": [["ElectricalSwitch", "machines"]],
	"RequiredResearches": ["Electricity" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[2] + "ElectricalSwitch"],["Constructor" + recipe_dictionary, tier_material[2] + "ElectricalSwitch"]],
	"Position": [0,-2],
	"Levels": [2,2],
	"Chapter": "Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "Diode" + static_research,
	"LabelParts": [["Diode", "machines"]],
	"Position": [0,-3],
	"RequiredResearches": ["Electricity" + static_research],
	"Levels": [2,7],
	"Chapter": "Production"+static_chapter,
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Diode"],["Constructor" + recipe_dictionary, "%Material%Diode"]],
})
append_levels({
	"Class": static_research,
	"Name": "PowerGeneration" + static_research,
	"LabelParts": [["PowerGeneration", "researches"]],
	"RequiredResearches": ["Electricity" + static_research],
	"Levels": [1,1],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%CompactGenerator"],["Constructor" + recipe_dictionary, "%Material%CompactGenerator"]],
	"Chapter":"Production"+static_chapter,
	"Position": [1,-1],
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "Electrolysis" + static_research,
	"LabelParts": [["Electrolysis", "researches"]],
	"RequiredResearches": ["SteelProduction" + static_research], 
	"Levels": [2,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Electrolyzer"],["Constructor" + recipe_dictionary, "%Material%Electrolyzer"]],
	"Chapter": "Production" + static_chapter,
	"Position": [4,-1]
})
append_levels({
	"Class": static_research,
	"Name": "SteelProduction" + static_research,
	"LabelParts": [["SteelProduction", "researches"]],
	"RequiredResearches": ["Drying"+static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%BlastFurnace"],["Constructor" + recipe_dictionary, "%Material%BlastFurnace"]],
	"AlsoUnlocks": [["Hand" + recipe_dictionary, "SteelParts"],["Hand" + recipe_dictionary, "SteelPlate"],["Hand" + recipe_dictionary, "SteelPipe"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3, 0],
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedSmelting" + static_research,
	"LabelParts": [["AdvancedSmelting", "researches"]],
	"RequiredResearches": ["SteelProduction" + static_research],
	"Position": [4, 0],
	"Levels": [2,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%ArcSmelter"],["Constructor" + recipe_dictionary, "%Material%ArcSmelter"]],
	"Chapter":"Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "SolarPanel" + static_research,
	"LabelParts": [["SolarPanel", "machines"]],
	"Position": [5, 0],
	"RequiredResearches": ["AluminiumProduction" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%SolarPanel"],["Constructor" + recipe_dictionary, "%Material%SolarPanel"]],
	"Chapter":"Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "AluminiumProduction" + static_research,
	"LabelParts": [["AluminiumProduction", "researches"]],
	"RequiredResearches": ["AdvancedSmelting" + static_research, "Electrolysis" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[3] + "Parts"],
	["Hand" + recipe_dictionary, tier_material[3] + "Plate"],
	["Hand" + recipe_dictionary, tier_material[3] + "Pipe"],["Constructor" + recipe_dictionary, tier_material[3] + "Pipe"]],
	"Chapter": "Production" + static_chapter,
	"Position": [5,-1],
	"Levels": [3,3],
	"CostLevelOffset": -1,
})
append_levels({
	"Class": static_research,
	"Name": "MassivePowerGeneration" + static_research,
	"LabelParts": [["MassivePowerGeneration", "researches"]],
	"RequiredResearches": ["PowerGeneration" + static_research ],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Generator"],["Constructor" + recipe_dictionary, "%Material%Generator"],
	["Hand" + recipe_dictionary, "%Material%Boiler"],["Constructor" + recipe_dictionary, "%Material%Boiler"],
	["Hand" + recipe_dictionary, "%Material%SteamTurbine"],["Constructor" + recipe_dictionary, "%Material%SteamTurbine"]],
	"Levels": [2,7],
	"Chapter":"Production"+static_chapter,
	"Position": [1,-2],
})
append_levels({
	"Class": static_research,
	"Name": "GasTurbine" + static_research,
	"LabelParts": [["GasTurbine", "machines"]],
	"Position": [1,-3],
	"RequiredResearches": ["MassivePowerGeneration" + static_research],
	"Levels": [4,7],
	"Chapter":"Production"+static_chapter,
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%GasTurbine"],["Constructor" + recipe_dictionary, "%Material%GasTurbine"]],
})
append_levels({
	"Class": static_research,
	"Name": "Smelting" + static_research,
	"LabelParts": [["Smelting", "researches"]],
	"RequiredResearches": ["MineralsScan"+static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Smelter"], ["Constructor" + recipe_dictionary, "%Material%Smelter"]],
	"Levels": [0,2],
	"Position": [0,2],
	"Chapter": "Production"+static_chapter,
	"CompleteByDefault": True,
})
append_equipment([-1,3], append_levels, researches)
append_levels({
	"Class": static_research,
	"Name": "Metalwork" + static_research,
	"LabelParts": [["Metalwork", "researches"]],
	"RequiredResearches": ["Smelting"+static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "CopperParts"],["Hand" + recipe_dictionary, "CopperPlate"],["Hand" + recipe_dictionary, "CopperPipe"]],
	"Collect": { "Items": [
		{
			"Name": "CopperOre" + static_item,
			"Count": 10
		}
	] },
	"Position": [1,2],
	"Levels": [1,1],
	"Chapter": "Production"+static_chapter,
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "Valve" + static_research,
	"LabelParts": [["Vent", "machines"]],
	"RequiredResearches": ["Metalwork" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[1] + "Vent"],["Constructor" + recipe_dictionary, tier_material[1] + "Vent"]],
	"Position": [0,3],
	"Levels": [1,1],
	"Chapter": "Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "BasicMachines" + static_research,
	"LabelParts": [["BasicMachines", "researches"]],
	"RequiredResearches": ["Metalwork" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Macerator"],["Constructor" + recipe_dictionary, "%Material%Macerator"],
	["Hand" + recipe_dictionary, "%Material%AutomaticHammer"],["Constructor" + recipe_dictionary, "%Material%AutomaticHammer"]],
	"Chapter":"Production"+static_chapter,
	"Position": [1, 3],
	"CostMul":0.25
})
append_levels({
	"Class": static_research,
	"Name": "Flywheel" + static_research,
	"LabelParts": [["Flywheel", "machines"]],
	"RequiredResearches": ["BasicMachines" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[2] + "Flywheel"],["Constructor" + recipe_dictionary, tier_material[2] + "Flywheel"]],
	"Levels": [2,2],
	"Chapter":"Production"+static_chapter,
	"Position": [0,4],
})
append_levels({
	"Class": static_research,
	"Name": "Cutting" + static_research,
	"LabelParts": [["Cutting", "researches"]],

	"RequiredResearches": ["BasicMachines" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%CuttingMachine"],["Constructor" + recipe_dictionary, "%Material%CuttingMachine"]],
	"Chapter":"Production"+static_chapter,
	"Position": [2, 2],
})
append_levels({
	"Class": static_research,
	"Name": "SolidDump" + static_research,
	"LabelParts": [["SolidDump", "machines"]],
	"Position": [4, 1],
	"Levels": [2,2],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Furnace" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[2] + "SolidDump"],["Constructor" + recipe_dictionary, tier_material[2] + "SolidDump"]],
})
append_levels({
	"Class": static_research,
	"Name": "Pump" + static_research,
	"LabelParts": [["Pump", "machines"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Pump"],["Constructor" + recipe_dictionary, "%Material%Pump"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3, 2],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "Container" + static_research,
	"LabelParts": [["Container", "machines"]],
	"RequiredResearches": ["Pump" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Container"],["Constructor" + recipe_dictionary, "%Material%Container"]],
	"Chapter":"Production"+static_chapter,
	"Position": [4, 2],
})
append_levels({
	"Class": static_research,
	"Name": "FluidFurnace" + static_research,
	"LabelParts": [["FluidFurnace", "machines"]],
	"RequiredResearches": ["Furnace" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%FluidFurnace"],["Constructor" + recipe_dictionary, "%Material%FluidFurnace"]],
	"Levels": [1,7],
	"Chapter":"Production"+static_chapter,
	"Position": [3, 1],
})
append_levels({
	"Class": static_research,
	"Name": "FluidDumping" + static_research,
	"LabelParts": [["FluidDumping", "researches"]],
	"RequiredResearches": ["Container" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%FluidDump"],["Constructor" + recipe_dictionary, "%Material%FluidDump"]],
	"Chapter":"Production"+static_chapter,
	"Position": [5, 2],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "GasDump" + static_research,
	"LabelParts": [["GasDump", "machines"]],
	"Position": [5, 1],
	"Levels": [2,2],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Container" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[2] + "GasDump"],["Constructor" + recipe_dictionary, tier_material[2] + "GasDump"]],
})
append_levels({
	"Class": static_research,
	"Name": "Automatization" + static_research,
	"LabelParts": [["Automatization", "researches"]],
	"RequiredResearches": ["BasicMachines" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%RobotArm"],["Constructor" + recipe_dictionary, "%Material%RobotArm"],
	["Hand" + recipe_dictionary, "%Material%Conveyor"],["Constructor" + recipe_dictionary, "%Material%Conveyor"],
	["Hand" + recipe_dictionary, "%Material%Splitter"],["Constructor" + recipe_dictionary, "%Material%Splitter"]],
	"Chapter":"Production"+static_chapter,
	"Position": [2, 3],
	"CostMul":0.25
})
append_levels({
	"Class": static_research,
	"Name": "Filtering" + static_research,
	"LabelParts": [["Filtering", "researches"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%FilteringRobotArm"],["Constructor" + recipe_dictionary, "%Material%FilteringRobotArm"],
	["Hand" + recipe_dictionary, "%Material%Sorter"],["Constructor" + recipe_dictionary, "%Material%Sorter"]],
	"Levels": [1,7],
	"Chapter": "Production"+static_chapter,
	"Position": [3, 3],
})
append_levels({
	"Class": static_research,
	"Name": "FilteringPump" + static_research,
	"LabelParts": [["FilteringPump", "machines"]],
	"RequiredResearches": ["Pump" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%FilteringPump"],["Constructor" + recipe_dictionary, "%Material%FilteringPump"]],
	"Levels": [1,7],
	"Chapter": "Production"+static_chapter,
	"Position": [4, 3],
})
append_levels({
	"Class": static_research,
	"Name": "AutomaticMining" + static_research,
	"LabelParts": [["AutomaticMining", "researches"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%DrillingRig"],["Constructor" + recipe_dictionary, "%Material%DrillingRig"]],
	"Position": [2, 4],
	"Chapter":"Production"+static_chapter,
	"CostMul":0.5
})
append_levels({
	"Class": static_research,
	"Name": "Pumpjack" + static_research,
	"LabelParts": [["Pumpjack", "machines"]],
	"Position": [2, 5],
	"RequiredResearches": ["AutomaticMining" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Pumpjack"],["Constructor" + recipe_dictionary, "%Material%Pumpjack"]],
	"Levels": [3,7],
	"Chapter":"Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "AutomaticFarm" + static_research,
	"LabelParts": [["AutomaticFarm", "machines"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%AutomaticFarm"],["Constructor" + recipe_dictionary, "%Material%AutomaticFarm"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,4],
	"CostMul":0.5
})
append_levels({
	"Class": static_research,
	"Name": "HeatTransferring" + static_research,
	"LabelParts": [["HeatTransferring", "researches"]],
	"RequiredResearches": ["InitialScan" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%HeatPipe"],["Constructor" + recipe_dictionary, "%Material%HeatPipe"]],
	"Position": [-1,-1],
	"Levels":[1,1],
	"Chapter":"Production"+static_chapter,
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "Radiator" + static_research,
	"LabelParts": [["Radiator", "machines"]],
	"RequiredResearches": ["HeatTransferring" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Radiator"],["Constructor" + recipe_dictionary, "%Material%Radiator"]],
	"Position": [-2,-1],
	"Chapter":"Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "AtmosphericCondenser" + static_research,
	"LabelParts": [["AtmosphericCondenser", "machines"]],
	"RequiredResearches": ["InitialScan" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%AtmosphericCondenser"],["Constructor" + recipe_dictionary, "%Material%AtmosphericCondenser"]],
	"Chapter":"Production"+static_chapter,
	"Position": [-2,0],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "StirlingEngine" + static_research,
	"LabelParts": [["StirlingEngine", "machines"]],
	"RequiredResearches": ["MineralsScan"+static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%StirlingEngine"],["Constructor" + recipe_dictionary, "%Material%StirlingEngine"]],
	"Chapter":"Production"+static_chapter,
	"Position": [1,1],
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "Furnace" + static_research,
	"LabelParts": [["Furnace", "machines"]],
	"RequiredResearches": ["StirlingEngine" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Furnace"],["Constructor" + recipe_dictionary, "%Material%Furnace"]],
	"Chapter":"Production"+static_chapter,
	"Position": [2, 1],
})
append_levels({
	"Class": static_research,
	"Name": "Drying" + static_research,
	"LabelParts": [["Drying", "researches"]],
	"RequiredResearches": ["Furnace" + static_research,],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Oven"],["Constructor" + recipe_dictionary, "%Material%Oven"]],
	"Position": [2,0],
	"Chapter":"Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "DistributedComputing" + static_research,
	"LabelParts": [["DistributedComputing", "researches"]],
	"RequiredResearches": ["PowerGeneration" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Computer"],["Constructor" + recipe_dictionary, "%Material%Computer"]],
	"Levels": [1,7],
	"Chapter":"Production"+static_chapter,
	"Position": [2,-1],
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "CopperWire" + static_research,
	"LabelParts": [["CopperWire", "parts"]],
	"RequiredResearches": ["DistributedComputing" + static_research],
	"Levels": [1,1],
	"Unlocks": [["Hand" + recipe_dictionary, "CopperWire"],["Assembler" + recipe_dictionary, "CopperWire"]],
	"Chapter":"Production"+static_chapter,
	"Position": [2,-2],
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "CircuitBoard" + static_research,
	"LabelParts": [["CircuitBoard", "parts"]],
	"RequiredResearches": ["CopperWire" + static_research],
	"Levels": [1,1],
	"Unlocks": [["Hand" + recipe_dictionary, "CircuitBoard"]],
	"Chapter":"Production"+static_chapter,
	"Position": [2,-3],
	"CostMul":0.25,
})
append_levels({
	"Class": static_research,
	"Name": "Circuit" + static_research,
	"LabelParts": [["Circuit", "parts"]],
	"RequiredResearches": ["CircuitBoard" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "Circuit"],["Assembler" + recipe_dictionary, "Circuit"]],
	"Levels": [1,1],
	"Chapter":"Production"+static_chapter,
	"Position": [2,-4],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "LogicCircuit" + static_research,
	"LabelParts": [["LogicCircuit", "machines"]],
	"RequiredResearches": ["Circuit" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "SteelLogicCircuit"],["Constructor" + recipe_dictionary, "SteelLogicCircuit"],
	["Hand" + recipe_dictionary, "SteelLogicController"],["Constructor" + recipe_dictionary, "SteelLogicController"],
	["Hand" + recipe_dictionary, "SteelLogicInterface"],["Constructor" + recipe_dictionary, "SteelLogicInterface"],
	["Hand" + recipe_dictionary, "SteelLogicDisplay"],["Constructor" + recipe_dictionary, "SteelLogicDisplay"],
	["Hand" + recipe_dictionary, "SteelLogicWire"],["Constructor" + recipe_dictionary, "SteelLogicWire"]],
	"Levels": [1,1],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-3],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedCircuit" + static_research,
	"LabelParts": [["AdvancedCircuit", "parts"]],
	"RequiredResearches": ["Circuit" + static_research],
	"Levels": [2,2],
	"Unlocks": [["Hand" + recipe_dictionary, "AdvancedCircuit"],["Assembler" + recipe_dictionary, "AdvancedCircuit"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-4],
})
append_levels({
	"Class": static_research,
	"Name": "GoldWire" + static_research,
	"LabelParts": [["GoldWire", "parts"]],
	"RequiredResearches": ["AdvancedCircuit" + static_research, "OreWasher" + static_research],
	"Levels": [2,2],
	"Unlocks": [["Hand" + recipe_dictionary, "GoldWire"],["Assembler" + recipe_dictionary, "GoldWire"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-5],
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedCircuitBoard" + static_research,
	"LabelParts": [["AdvancedCircuitBoard", "parts"]],
	"RequiredResearches": ["GoldWire" + static_research, "PyrolysisUnit" + static_research],
	"Levels": [2,2],
	"Unlocks": [["Hand" + recipe_dictionary, "AdvancedCircuitBoard"],["Assembler" + recipe_dictionary, "AdvancedCircuitBoard"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-6],
})
append_levels({
	"Class": static_research,
	"Name": "Processor" + static_research,
	"LabelParts": [["Processor", "parts"]],
	"RequiredResearches": ["AdvancedCircuitBoard" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "Processor"],["Assembler" + recipe_dictionary, "Processor"],["Assembler" + recipe_dictionary, "SiliconWafer"],["Assembler" + recipe_dictionary, "Processor2"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-7],
	"Levels": [3,3],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumCore" + static_research,
	"LabelParts": [["QuantumCore", "parts"]],
	"RequiredResearches": ["Processor" + static_research],
	"Levels": [4,4],
	"Unlocks": [["Hand" + recipe_dictionary, "QuantumCore"],["Assembler" + recipe_dictionary, "QuantumCore"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-8],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumCircuit" + static_research,
	"LabelParts": [["QuantumCircuit", "parts"]],
	"RequiredResearches": ["QuantumCore" + static_research],
	"Levels": [4,4],
	"Unlocks": [["Hand" + recipe_dictionary, "QuantumCircuit"],["Assembler" + recipe_dictionary, "QuantumCircuit"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-9],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumProcessor" + static_research,
	"LabelParts": [["QuantumProcessor", "parts"]],
	"RequiredResearches": ["QuantumCircuit" + static_research],
	"Levels": [5,5],
	"Unlocks": [["Hand" + recipe_dictionary, "QuantumProcessor"],["Assembler" + recipe_dictionary, "QuantumProcessor"]],
	"Chapter":"Production"+static_chapter,
	"Position": [4,-10],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumBrain" + static_research,
	"LabelParts": [["QuantumBrain", "parts"]],
	"RequiredResearches": ["QuantumProcessor" + static_research],
	"Levels": [6,6],
	"Unlocks": [["Hand" + recipe_dictionary, "QuantumBrain"],["Assembler" + recipe_dictionary, "QuantumBrain"]],
	"Chapter":"Production"+static_chapter,
	"Position": [4,-11],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumComputer" + static_research,
	"LabelParts": [["QuantumComputer", "machines"]],
	"RequiredResearches": ["QuantumCircuit" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%QuantumComputer"],["Constructor" + recipe_dictionary, "%Material%QuantumComputer"]],
	"Levels": [5,7],
	"Chapter":"Production"+static_chapter,
	"Position": [4,-9],
	"CostSub": 1,
})
append_levels({
	"Class": static_research,
	"Name": "MetalConstructions" + static_research,
	"LabelParts": [["MetalConstructions", "researches"]],
	"RequiredResearches": ["Metalwork" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Corner"],["Constructor" + recipe_dictionary, "%Material%Corner"],
	["Hand" + recipe_dictionary, "%Material%Casing"],["Constructor" + recipe_dictionary,"%Material%Casing"],
	["Hand" + recipe_dictionary, "%Material%Beam"],["Constructor" + recipe_dictionary, "%Material%Beam"]],
	"Levels": [1,7],
	"Chapter":"Decorations"+static_chapter,
	"Position": [4,3],
})
append_levels({
	"Class": static_research,
	"Name": "Scaffold" + static_research,
	"LabelParts": [["Scaffold", "researches"]],
	"Chapter": "Decorations"+static_chapter,
	"RequiredResearches": ["MetalConstructions" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Scaffold"],["Constructor" + recipe_dictionary, "%Material%Scaffold"]],
	"Levels": [1,7],
	"Position": [3, 4],
})
append_levels({
	"Class": static_research,
	"Name": "Chemistry" + static_research,
	"LabelParts": [["Chemistry", "researches"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["ElectricEngine" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%ChemReactor"],["Constructor" + recipe_dictionary, "%Material%ChemReactor"]],
	"Levels": [2,7],
	"Position": [5,-2],
})
append_levels({
	"Class": static_research,
	"Name": "FilteringUnit" + static_research,
	"LabelParts": [["FilteringUnit", "machines"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Chemistry" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%FilteringUnit"],["Constructor" + recipe_dictionary, "%Material%FilteringUnit"]],
	"Levels": [3,7],
	"Position": [5,-3],
})
append_levels({
	"Class": static_research,
	"Name": "Sifter" + static_research,
	"LabelParts": [["Sifter", "machines"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Chemistry" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Sifter"],["Constructor" + recipe_dictionary, "%Material%Sifter"]],
	"Levels": [3,7],
	"Position": [6,-3],
})
append_levels({
	"Class": static_research,
	"Name": "Separator" + static_research,
	"LabelParts": [["Separator", "machines"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["ElectricEngine" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Separator"],["Constructor" + recipe_dictionary, "%Material%Separator"]],
	"Position": [4,-3],
})
append_levels({
	"Class": static_research,
	"Name": "ElectricEngine" + static_research,
	"LabelParts": [["ElectricEngine", "machines"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Electrolysis" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%ElectricEngine"],["Constructor" + recipe_dictionary, "%Material%ElectricEngine"]],
	"Position": [4,-2],
})
append_levels({
	"Class": static_research,
	"Name": "OreWasher" + static_research,
	"LabelParts": [["OreWasher", "machines"]],
	"Levels": [2,7],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Separator" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%OreWasher"],["Constructor" + recipe_dictionary, "%Material%OreWasher"]],
	"Position": [4,-4],
})
append_levels({
	"Class": static_research,
	"Name": "Mixer" + static_research,
	"LabelParts": [["Mixer", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["OreWasher" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Mixer"],["Constructor" + recipe_dictionary, "%Material%Mixer"]],
	"Position": [4,-5],
})
append_levels({
	"Class": static_research,
	"Name": "ChemicalBath" + static_research,
	"LabelParts": [["ChemicalBath", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["FilteringUnit" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%ChemicalBath"],["Constructor" + recipe_dictionary, "%Material%ChemicalBath"]],
	"Position": [5,-4],
})
append_levels({
	"Class": static_research,
	"Name": "StainlessSteelProduction" + static_research,
	"LabelParts": [["StainlessSteelProduction", "researches"]],
	"RequiredResearches": ["Chemistry" + static_research, "AluminiumProduction" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[4] + "Parts"],
	["Hand" + recipe_dictionary, tier_material[4] + "Plate"],
	["Hand" + recipe_dictionary, tier_material[4] + "Pipe"],["Constructor" + recipe_dictionary, tier_material[4] + "Pipe"]],
	"Chapter": "Production" + static_chapter,
	"Position": [6,-2],
	"Levels": [4,4],
	"CostLevelOffset": -1,
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedSeparation" + static_research,
	"LabelParts": [["AdvancedSeparation", "researches"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["AluminiumProduction" + static_research],
	"Position": [6,-1],
	"Levels": [3,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%IndustrialSeparator"],["Constructor" + recipe_dictionary, "%Material%IndustrialSeparator"]],
})
append_levels({
	"Class": static_research,
	"Name": "SmallBattery" + static_research,
	"LabelParts": [["SmallBattery", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["AdvancedSeparation" + static_research],
	"Position": [6,0],
	"Levels": [3,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%SmallBattery"],["Constructor" + recipe_dictionary, "%Material%SmallBattery"]],
})
append_levels({
	"Class": static_research,
	"Name": "TitaniumProduction" + static_research,
	"LabelParts": [["TitaniumProduction", "researches"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialSmelting" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[5] + "Parts"],
	["Hand" + recipe_dictionary, tier_material[5] + "Plate"],
	["Hand" + recipe_dictionary, tier_material[5] + "Pipe"],["Constructor" + recipe_dictionary, tier_material[5] + "Pipe"]],
	"Position": [7,-4],
	"Levels": [4,4],
	"CostLevelOffset": -1,
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialBoiler" + static_research,
	"LabelParts": [["IndustrialBoiler", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["TitaniumProduction" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%IndustrialBoiler"],["Connector" + recipe_dictionary, "%Material%IndustrialBoiler"]],
	"Position": [6,-4],
	"Levels": [5,7],
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialSteamTurbine" + static_research,
	"LabelParts": [["IndustrialSteamTurbine", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialBoiler" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%IndustrialSteamTurbine"],["Connector" + recipe_dictionary, "%Material%IndustrialSteamTurbine"]],
	"Position": [6,-5],
	"Levels": [5,7],
})
append_levels({
	"Class": static_research,
	"Name": "Freezer" + static_research,
	"LabelParts": [["Freezer", "machines"]],
	"RequiredResearches": ["TitaniumProduction" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Freezer"],["Constructor" + recipe_dictionary, "%Material%Freezer"]],
	"Chapter": "Production"+static_chapter,
	"Position": [8,-4],
	"Levels": [5,7],
})
append_levels({
	"Class": static_research,
	"Name": "HardMetalProduction" + static_research,
	"LabelParts": [["HardMetalProduction", "researches"]],
	"RequiredResearches": ["Freezer" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[6] + "Parts"],
	["Hand" + recipe_dictionary, tier_material[6] + "Plate"],
	["Hand" + recipe_dictionary, tier_material[6] + "Pipe"],["Constructor" + recipe_dictionary, tier_material[6] + "Pipe"]],
	"Chapter": "Production" + static_chapter,
	"Position": [9,-4],
	"Levels": [5,5],
})
append_levels({
	"Class": static_research,
	"Name": "FusionReactor" + static_research,
	"LabelParts": [["FusionReactor", "machines"]],
	"RequiredResearches": ["HardMetalProduction" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%FusionReactor"],["Constructor" + recipe_dictionary, "%Material%FusionReactor"]],
	"Chapter":"Production"+static_chapter,
	"Position": [10,-4],
	"Levels": [6,7],
})
append_levels({
	"Class": static_research,
	"Name": "NeutroniumProduction" + static_research,
	"LabelParts": [["NeutroniumProduction", "researches"]],
	"RequiredResearches": ["FusionReactor" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[7] + "Parts"],
	["Hand" + recipe_dictionary, tier_material[7] + "Plate"],
	["Hand" + recipe_dictionary, tier_material[7] + "Pipe"],["Constructor" + recipe_dictionary, tier_material[7] + "Pipe"]],
	"Chapter": "Production" + static_chapter,
	"Position": [11,-4],
	"Levels": [6,6],
})
append_levels({
	 "Class": static_research,
	 "Name": "Portal" + static_research,
	 "LabelParts": [["Portal", "machines"]],
	 "RequiredResearches": ["NeutroniumProduction" + static_research],
	 "Unlocks": [["Hand" + recipe_dictionary, "%Material%Portal"],["Constructor" + recipe_dictionary, "%Material%Portal"]],
	 "Chapter": "Production" + static_chapter,
	 "Position": [12,-4],
	 "Levels": [7,7],
 })
append_levels({
	"Class": static_research,
	"Name": "FissionReactor" + static_research,
	"LabelParts": [["FissionReactor", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["TitaniumProduction" + static_research],
	"Levels": [5,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%FissionReactor"],["Constructor" + recipe_dictionary, "%Material%FissionReactor"]],
	"Position": [7,-6],
})
append_nuclear([7,-7], append_levels, researches)
append_levels({
	"Class": static_research,
	"Name": "IndustrialSmelting" + static_research,
	"LabelParts": [["IndustrialSmelting", "researches"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["StainlessSteelProduction" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%IndustrialSmelter"],["Constructor" + recipe_dictionary, "%Material%IndustrialSmelter"]],
	"Position": [7,-2],
})
append_levels({
	"Class": static_research,
	"Name": "Fermentation" + static_research,
	"LabelParts": [["Fermentation", "researches"]],
	"Levels": [4,7],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialSmelting" + static_research],
	"Position": [7,-3],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Fermenter"],["Constructor" + recipe_dictionary, "%Material%Fermenter"]],
})
append_levels({
	"Class": static_research,
	"Name": "BatteryBox" + static_research,
	"LabelParts": [["BatteryBox", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialSmelting" + static_research],
	"Position": [8,-2],
	"Levels": [4,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%BatteryBox"],["Constructor" + recipe_dictionary, "%Material%BatteryBox"]],
})
append_levels({
	"Class": static_research,
	"Name": "InductionCoil" + static_research,
	"LabelParts": [["InductionCoil", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialSmelting" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%InductionCoil"],["Constructor" + recipe_dictionary, "%Material%InductionCoil"]],
	"Position": [8,-3],
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialElectricEngine" + static_research,
	"LabelParts": [["IndustrialElectricEngine", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["InductionCoil" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%IndustrialElectricEngine"],["Constructor" + recipe_dictionary, "%Material%IndustrialElectricEngine"]],
	"Position": [9,-3],
})
append_levels({
	"Class": static_research,
	"Name": "Terminal" + static_research,
	"LabelParts": [["Terminal", "machines"]],
	"Levels": [4,4],
	"Position": [7,-1],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["StainlessSteelProduction" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[4] + "Terminal"],["Constructor" + recipe_dictionary, tier_material[4] + "Terminal"]],
})
append_levels({
	"Class": static_research,
	"Name": "FlatTerminal" + static_research,
	"LabelParts": [["FlatTerminal", "machines"]],
	"Levels": [4,4],
	"Position": [8,-1],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["Terminal" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[4] + "FlatTerminal"],["Constructor" + recipe_dictionary, tier_material[4] + "FlatTerminal"]],
})
append_levels({
	"Class": static_research,
	"Name": "Constructor" + static_research,
	"LabelParts": [["Constructor", "machines"]],
	"Position": [1,5],
	"RequiredResearches": ["Assembler" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Constructor"],["Constructor" + recipe_dictionary, "%Material%Constructor"]],
	"Levels": [2, 7],
	"Chapter": "Production" + static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "Assembler" + static_research,
	"LabelParts": [["Assembler", "machines"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Assembler"],["Constructor" + recipe_dictionary, "%Material%Assembler"]],
	"Levels": [1,7],
	"Position": [1, 4],
	"Chapter": "Production" + static_chapter,
	"CostMul":0.5
})
append_levels({
	"Class": static_research,
	"Name": "Deconstructor" + static_research,
	"LabelParts": [["Deconstructor", "machines"]],
	"Position": [0, 5],
	"RequiredResearches": ["Constructor" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Deconstructor"],["Constructor" + recipe_dictionary, "%Material%Deconstructor"]],
	"Levels": [2,7],
	"Chapter": "Production" + static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "BigTerminal" + static_research,
	"LabelParts": [["BigTerminal", "machines"]],
	"RequiredResearches": ["Terminal" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[5] + "BigTerminal"],["Constructor" + recipe_dictionary, tier_material[5] + "BigTerminal"]],
	"Levels": [4,4],
	"Chapter": "Production" + static_chapter,
	"Position": [7,0],
})
append_levels({
	"Class": static_research,
	"Name": "BigFlatTerminal" + static_research,
	"LabelParts": [["BigFlatTerminal", "machines"]],
	"RequiredResearches": ["BigTerminal" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[5] + "BigFlatTerminal"],["Constructor" + recipe_dictionary, tier_material[5] + "BigFlatTerminal"]],
	"Chapter": "Production" + static_chapter,
	"Levels": [4,4],
	"Position": [8,0],
})
append_levels({
	"Class": static_research,
	"Name": "HugeTerminal" + static_research,
	"LabelParts": [["HugeTerminal", "machines"]],
	"RequiredResearches": ["BigTerminal" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[6] + "HugeTerminal"],["Constructor" + recipe_dictionary, tier_material[6] + "HugeTerminal"]],
	"Chapter": "Production" + static_chapter,
	"Levels": [5,5],
	"Position": [7,1],
})
append_levels({
	"Class": static_research,
	"Name": "HugeFlatTerminal" + static_research,
	"LabelParts": [["HugeFlatTerminal", "machines"]],
	"RequiredResearches": ["HugeTerminal" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, tier_material[6] + "HugeFlatTerminal"],["Constructor" + recipe_dictionary, tier_material[6] + "HugeFlatTerminal"]],
	"Chapter": "Production" + static_chapter,
	"Levels": [5,5],
	"Position": [8,1],
}) 
append_levels({
	"Class": static_research,
	"Name": "PyrolysisUnit" + static_research,
	"LabelParts": [["PyrolysisUnit", "machines"]],
	"RequiredResearches": ["Mixer" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%PyrolysisUnit"],["Constructor" + recipe_dictionary, "%Material%PyrolysisUnit"]],
	"Levels": [3,7],
	"Chapter": "Production" + static_chapter,
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
	"Name": "DecorativeWood" + static_research,
	"LabelParts": [["DecorativeWood", "researches"]],
	"Unlocks": [["Hand" + recipe_dictionary, "WoodenPlanks"],["Hand" + recipe_dictionary, "WoodenStairs"],["Hand" + recipe_dictionary, "Bed"],["Hand" + recipe_dictionary, "Door"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [0,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood2" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[1], "common"]],
	"RequiredResearches": ["DecorativeWood" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "Chair"],["Hand" + recipe_dictionary, "Fence"],["Hand" + recipe_dictionary, "Ladder"],["Hand" + recipe_dictionary, "Rack"],["Hand" + recipe_dictionary, "Table"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [0,1],
})
append_levels({
	"Class": static_research,
	"Name": "Fence" + static_research,
	"LabelParts": [["Fence", "misc"]],
	"RequiredResearches": ["DecorativeWood2" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "SteelFence"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [-1,1],
})
append_levels({
	"Class": static_research,
	"Name": "Fence1" + static_research,
	"LabelParts": [["Fence", "misc"], [level_labels[1], "common"]],
	"RequiredResearches": ["Fence" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "StainlessSteelFence"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [-2,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood4" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[3], "common"]],
	"RequiredResearches": ["DecorativeWood2" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "CopperChair"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [1,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood3" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[2], "common"]],
	"RequiredResearches": ["DecorativeWood2" + static_research, "AdvancedSmelting" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "Window"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [0,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativePlastic" + static_research,
	"LabelParts": [["DecorativePlastic", "researches"]],
	"RequiredResearches": ["Chemistry" + static_research, "PyrolysisUnit" + static_research, "DecorativeWood3" + static_research],

	"Unlocks": [["Hand" + recipe_dictionary, "PlasticWindow"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [-1,2],
})
append_levels({
	"Class": static_research,
	"Name": "PlasticBlock" + static_research,
	"LabelParts": [["PlasticBlock", "misc"]],
	"RequiredResearches": ["DecorativePlastic" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "PlasticBlock"],["Press" + recipe_dictionary, "PlasticBlock"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [-2,2],
})
append_levels({
	"Class": static_research,
	"Name": "BasicPlatform" + static_research,
	"LabelParts": [["BasicPlatform", "misc"]],
	"CompleteByDefault": True,
	"Chapter": "Decorations"+static_chapter,
	"Unlocks": [["Hand" + recipe_dictionary, "BasicPlatform"], ["Press" + recipe_dictionary, "BasicPlatform"]],
	"Position": [1,-1],
	"RequiredResearches": []
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone" + static_research,
	"LabelParts": [["DecorativeStone", "researches"]],
	"RequiredResearches": ["BasicPlatform"+static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "StoneTiles"], ["CuttingMachine" + recipe_dictionary, "StoneTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [1,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone2" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorativeStone" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "DarkTiles"],["Hand" + recipe_dictionary, "RedTiles"],["CuttingMachine" + recipe_dictionary, "DarkTiles"],["CuttingMachine" + recipe_dictionary, "RedTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [2,0],
})
append_levels({
	"Class": static_research,
	"Name": "GlassBlock" + static_research,
	"LabelParts": [["GlassBlock", "misc"]],

	"RequiredResearches": [], 
	"Unlocks": [["Hand" + recipe_dictionary, "GlassBlock"],["Press" + recipe_dictionary, "GlassBlock"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [2,-1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone3" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[2], "common"]],

	"RequiredResearches": ["DecorativeStone2" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "DarkBricks"],["Hand" + recipe_dictionary, "RedBricks"],["Hand" + recipe_dictionary, "Bricks"],["CuttingMachine" + recipe_dictionary, "DarkBricks"],["CuttingMachine" + recipe_dictionary, "RedBricks"],["CuttingMachine" + recipe_dictionary, "Bricks"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [2,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone4" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[3], "common"]],

	"RequiredResearches": ["DecorativeStone3" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "Stairs"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [2,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete" + static_research,
	"LabelParts": [["DecorativeConcrete", "researches"]],
	"RequiredResearches": ["Mixer" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "ConcreteTiles"], ["CuttingMachine" + recipe_dictionary, "ConcreteTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [3,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete2" + static_research,
	"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorativeConcrete" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "ConcreteSmallTiles"], ["CuttingMachine" + recipe_dictionary, "ConcreteSmallTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [3,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete3" + static_research,
	"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[2], "common"]],

	"RequiredResearches": ["DecorativeConcrete2" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "ConcreteBricks"], ["CuttingMachine" + recipe_dictionary, "ConcreteBricks"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [3,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete4" + static_research,
	"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[3], "common"]],

	"RequiredResearches": ["DecorativeConcrete3" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "DangerBlock"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [3,3],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeReinforcedConcrete" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"]],

	"RequiredResearches": ["DecorativeConcrete" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "ReinforcedConcreteTiles"], ["CuttingMachine" + recipe_dictionary, "ReinforcedConcreteTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [4,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeReinforcedConcrete2" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorativeReinforcedConcrete" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "ReinforcedConcreteSmallTiles"], ["CuttingMachine" + recipe_dictionary, "ReinforcedConcreteSmallTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [4,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeReinforcedConcrete3" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[2], "common"]],

	"RequiredResearches": ["DecorativeReinforcedConcrete2" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "ReinforcedConcreteBricks"], ["CuttingMachine" + recipe_dictionary, "ReinforcedConcreteBricks"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [4,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorationClay" + static_research,
	"LabelParts": [["DecorationClay", "researches"]],

	"RequiredResearches": ["Drying" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "TerracottaTiles"], ["CuttingMachine" + recipe_dictionary, "TerracottaTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [5,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorationClay2" + static_research,
	"LabelParts": [["DecorationClay", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorationClay" + static_research], 
	"Unlocks": [["Hand" + recipe_dictionary, "TerracottaBricks"], ["CuttingMachine" + recipe_dictionary, "TerracottaBricks"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [5,1],
})
append_levels({
	"Class": static_research,
	"Name": "Press" + static_research,
	"LabelParts": [["Press", "machines"]],
	"RequiredResearches": [],
	"Levels": [2,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Press"],["Constructor" + recipe_dictionary, "%Material%Press"]],
	"Position": [2, 3],
	"Chapter": "Decorations"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "PaintTool" + static_research,
	"LabelParts": [["PaintTool", "parts"]],
	"RequiredResearches": [],
	"Levels": [1,1],
	"Unlocks": [["Hand" + recipe_dictionary, "CopperPaintTool"],["Constructor" + recipe_dictionary, "CopperPaintTool"]],
	"Position": [1, 2],
	"Chapter": "Decorations"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "Lamp" + static_research,
	"LabelParts": [["Lamp", "machines"]],
	"RequiredResearches": [],
	"Levels": [1,7],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Lamp"],["Constructor" + recipe_dictionary, "%Material%Lamp"]],
	"Position": [2, 4],
	"Chapter": "Decorations"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "Column" + static_research,
	"LabelParts": [["Column", "misc"]],
	"RequiredResearches": [],
	"Levels": [1,1],
	"Unlocks": [["Hand" + recipe_dictionary, "Column"],["Hand" + recipe_dictionary, "FluetedColumn"],["Press" + recipe_dictionary, "Column"],["Press" + recipe_dictionary, "FluetedColumn"]],
	"Position": [1, 4],
	"Chapter": "Decorations"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "Sign" + static_research,
	"LabelParts": [["Sign", "machines"]],
	"RequiredResearches": ["MineralsScan" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%Sign"],["Constructor" + recipe_dictionary, "%Material%Sign"]],
	"Levels": [0,7],
	"Chapter": "Decorations"+static_chapter,
	"Position": [0,3],

})
append_levels({
	"Class": static_research,
	"Name": "AdvancedSign" + static_research,
	"LabelParts": [["AdvancedSign", "machines"]],
	"RequiredResearches": ["Sign" + static_research],
	"Unlocks": [["Hand" + recipe_dictionary, "%Material%AdvancedSign"],["Constructor" + recipe_dictionary, "%Material%AdvancedSign"]],
	"Levels": [2,7],
	"Chapter": "Decorations"+static_chapter,
	"Position": [1,3],
})
	
data = {
	"Objects": researches
}

write_file("Generated/Researches/basic.json", data);
write_file("Loc/source/researches.json", csv)
