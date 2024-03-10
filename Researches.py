from Common import *
from Materials import *
import copy
from NuclearResearches import *
from EquipmentResearches import *
from PartsResearchHelper import *

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
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "MineralsScan" + static_research,
	"LabelParts": [["MineralsScan", "researches"]],

	"RequiredResearches": ["InitialScan" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[0] + "Furnace"],["Constructor" + base_recipe, tier_material[0] + "Furnace"],["Hand" + base_recipe, "SandSurface"],["Hand" + base_recipe, "GravelSurface"]],
	"Collect": { "Items": [
		{
			"Name": "Dirt" + static_item,
			"Count": 10
		}
	] },
	"Position": [0,1],
	"Chapter": "Production"+static_chapter,
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "AdditionalStorage" + static_research,
	"LabelParts": [["AdditionalStorage", "researches"]],
	"RequiredResearches": ["MineralsScan" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Chest"],["Constructor" + base_recipe, "%Material%Chest"]],
	"Position": [-1,1],
	"Levels":[0,7],
	"Chapter":"Production"+static_chapter,
	"CompleteByDefault": True,
})
append_levels({
	"Class": static_research,
	"Name": "SingleTypeStorage" + static_research,
	"LabelParts": [["SingleTypeStorage", "researches"]],
	"RequiredResearches": ["AdditionalStorage" + static_research ],
	"Position": [-2,1],
	"Levels":[1,7],
	"Chapter":"Production"+static_chapter,
	"Unlocks": [["Hand" + base_recipe, "%Material%ItemRack"],["Constructor" + base_recipe, "%Material%ItemRack"]],
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
	"Unlocks": [["Hand" + base_recipe, tier_material[1] + "Connector"], ["Constructor" + base_recipe, tier_material[1] + "Connector"],["Hand" + base_recipe, tier_material[1] + "HandGenerator"],["Constructor" + base_recipe, tier_material[1] + "HandGenerator"]],
	"Position": [0,-1],
	"Chapter": "Production"+static_chapter,
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "ElectricFurnace" + static_research,
	"LabelParts": [["ElectricFurnace", "machines"]],
	"Levels": [2,7],
	"RequiredResearches": ["Electricity" + static_research],
	"Position": [-1,-2],
	"Chapter": "Production"+static_chapter,
	"Unlocks": [["Hand" + base_recipe, "%Material%ElectricFurnace"],["Constructor" + base_recipe, "%Material%ElectricFurnace"]],
})
append_levels({
	"Class": static_research,
	"Name": "ElectricalSwitch" + static_research,
	"LabelParts": [["ElectricalSwitch", "machines"]],
	"RequiredResearches": ["Electricity" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "ElectricalSwitch"],["Constructor" + base_recipe, tier_material[2] + "ElectricalSwitch"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%Diode"],["Constructor" + base_recipe, "%Material%Diode"]],
})
append_levels({
	"Class": static_research,
	"Name": "PowerGeneration" + static_research,
	"LabelParts": [["PowerGeneration", "researches"]],
	"RequiredResearches": ["Electricity" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CompactGenerator"],["Constructor" + base_recipe, "%Material%CompactGenerator"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%Electrolyzer"],["Constructor" + base_recipe, "%Material%Electrolyzer"]],
	"Chapter": "Production" + static_chapter,
	"Position": [4,-1]
})
append_levels({
	"Class": static_research,
	"Name": "SteelProduction" + static_research,
	"LabelParts": [["SteelProduction", "researches"]],
	"RequiredResearches": ["Drying"+static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BlastFurnace"],["Constructor" + base_recipe, "%Material%BlastFurnace"]],
	"AlsoUnlocks": get_parts_unlocks(tier_material[2]),
	"Chapter":"Production"+static_chapter,
	"Position": [3, 0],
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedSmelting" + static_research,
	"LabelParts": [["AdvancedSmelting", "researches"]],
	"RequiredResearches": ["SteelProduction" + static_research],
	"Position": [4, 0],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ArcSmelter"],["Constructor" + base_recipe, "%Material%ArcSmelter"]],
	"Chapter":"Production"+static_chapter,
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "SolarPanel" + static_research,
	"LabelParts": [["SolarPanel", "machines"]],
	"Position": [5, 0],
	"RequiredResearches": ["AluminiumProduction" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%SolarPanel"],["Constructor" + base_recipe, "%Material%SolarPanel"]],
	"Chapter":"Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "AluminiumProduction" + static_research,
	"LabelParts": [["AluminiumProduction", "researches"]],
	"RequiredResearches": ["AdvancedSmelting" + static_research, "Electrolysis" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[3]),
	"Chapter": "Production" + static_chapter,
	"Position": [5,-1],
	"Levels": [3,3],
	"CostLevelOffset": -1,
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "MassivePowerGeneration" + static_research,
	"LabelParts": [["MassivePowerGeneration", "researches"]],
	"RequiredResearches": ["PowerGeneration" + static_research ],
	"Unlocks": [["Hand" + base_recipe, "%Material%Generator"],["Constructor" + base_recipe, "%Material%Generator"],
	["Hand" + base_recipe, "%Material%Boiler"],["Constructor" + base_recipe, "%Material%Boiler"],
	["Hand" + base_recipe, "%Material%SteamTurbine"],["Constructor" + base_recipe, "%Material%SteamTurbine"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%GasTurbine"],["Constructor" + base_recipe, "%Material%GasTurbine"]],
})
append_levels({
	"Class": static_research,
	"Name": "Smelting" + static_research,
	"LabelParts": [["Smelting", "researches"]],
	"RequiredResearches": ["MineralsScan"+static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Smelter"], ["Constructor" + base_recipe, "%Material%Smelter"]],
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
	"Unlocks": get_parts_unlocks(tier_material[1]),
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
	"Unlocks": [["Hand" + base_recipe, tier_material[1] + "Vent"],["Constructor" + base_recipe, tier_material[1] + "Vent"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%Macerator"],["Constructor" + base_recipe, "%Material%Macerator"],
	["Hand" + base_recipe, "%Material%AutomaticHammer"],["Constructor" + base_recipe, "%Material%AutomaticHammer"]],
	"Chapter":"Production"+static_chapter,
	"Position": [1, 3],
	"CostMul":0.25
})
append_levels({
	"Class": static_research,
	"Name": "Flywheel" + static_research,
	"LabelParts": [["Flywheel", "machines"]],
	"RequiredResearches": ["BasicMachines" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "Flywheel"],["Constructor" + base_recipe, tier_material[2] + "Flywheel"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%CuttingMachine"],["Constructor" + base_recipe, "%Material%CuttingMachine"]],
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
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "SolidDump"],["Constructor" + base_recipe, tier_material[2] + "SolidDump"]],
})
append_levels({
	"Class": static_research,
	"Name": "Pump" + static_research,
	"LabelParts": [["Pump", "machines"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Pump"],["Constructor" + base_recipe, "%Material%Pump"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%Container"],["Constructor" + base_recipe, "%Material%Container"]],
	"Chapter":"Production"+static_chapter,
	"Position": [4, 2],
})
append_levels({
	"Class": static_research,
	"Name": "FluidFurnace" + static_research,
	"LabelParts": [["FluidFurnace", "machines"]],
	"RequiredResearches": ["Furnace" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%FluidFurnace"],["Constructor" + base_recipe, "%Material%FluidFurnace"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%FluidDump"],["Constructor" + base_recipe, "%Material%FluidDump"]],
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
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "GasDump"],["Constructor" + base_recipe, tier_material[2] + "GasDump"]],
})
append_levels({
	"Class": static_research,
	"Name": "Automatization" + static_research,
	"LabelParts": [["Automatization", "researches"]],
	"RequiredResearches": ["BasicMachines" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%RobotArm"],["Constructor" + base_recipe, "%Material%RobotArm"],
	["Hand" + base_recipe, "%Material%Conveyor"],["Constructor" + base_recipe, "%Material%Conveyor"],
	["Hand" + base_recipe, "%Material%Splitter"],["Constructor" + base_recipe, "%Material%Splitter"]],
	"Chapter":"Production"+static_chapter,
	"Position": [2, 3],
	"CostMul":0.25
})
append_levels({
	"Class": static_research,
	"Name": "Filtering" + static_research,
	"LabelParts": [["Filtering", "researches"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%FilteringRobotArm"],["Constructor" + base_recipe, "%Material%FilteringRobotArm"],
	["Hand" + base_recipe, "%Material%Sorter"],["Constructor" + base_recipe, "%Material%Sorter"]],
	"Levels": [1,7],
	"Chapter": "Production"+static_chapter,
	"Position": [3, 3],
})
append_levels({
	"Class": static_research,
	"Name": "FilteringPump" + static_research,
	"LabelParts": [["FilteringPump", "machines"]],
	"RequiredResearches": ["Pump" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%FilteringPump"],["Constructor" + base_recipe, "%Material%FilteringPump"]],
	"Levels": [1,7],
	"Chapter": "Production"+static_chapter,
	"Position": [4, 3],
})
append_levels({
	"Class": static_research,
	"Name": "OverflowPump" + static_research,
	"LabelParts": [["OverflowPump", "machines"]],
	"RequiredResearches": ["FilteringPump" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%OverflowPump"],["Constructor" + base_recipe, "%Material%OverflowPump"]],
	"Levels": [1,7],
	"Chapter": "Production"+static_chapter,
	"Position": [4, 4],
})
append_levels({
	"Class": static_research,
	"Name": "AutomaticMining" + static_research,
	"LabelParts": [["AutomaticMining", "researches"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%DrillingRig"],["Constructor" + base_recipe, "%Material%DrillingRig"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%Pumpjack"],["Constructor" + base_recipe, "%Material%Pumpjack"]],
	"Levels": [3,7],
	"Chapter":"Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "AutomaticFarm" + static_research,
	"LabelParts": [["AutomaticFarm", "machines"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%AutomaticFarm"],["Constructor" + base_recipe, "%Material%AutomaticFarm"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,4],
	"CostMul":0.5
})
append_levels({
	"Class": static_research,
	"Name": "HeatTransferring" + static_research,
	"LabelParts": [["HeatTransferring", "researches"]],
	"RequiredResearches": ["InitialScan" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%HeatPipe"],["Constructor" + base_recipe, "%Material%HeatPipe"]],
	"Position": [-1,-1],
	"Levels":[1,1],
	"Chapter":"Production"+static_chapter,
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "KineticHeater" + static_research,
	"LabelParts": [["KineticHeater", "machines"]],
	"RequiredResearches": ["HeatTransferring" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%KineticHeater"],["Constructor" + base_recipe, "%Material%KineticHeater"]],
	"Position": [-2,0],
	"Levels":[1,7],
	"Chapter":"Production"+static_chapter,
	"CostMul":1,
})
append_levels({
	"Class": static_research,
	"Name": "Radiator" + static_research,
	"LabelParts": [["Radiator", "machines"]],
	"RequiredResearches": ["HeatTransferring" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Radiator"],["Constructor" + base_recipe, "%Material%Radiator"]],
	"Position": [-2,-1],
	"Chapter":"Production"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "AtmosphericCondenser" + static_research,
	"LabelParts": [["AtmosphericCondenser", "machines"]],
	"RequiredResearches": ["InitialScan" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%AtmosphericCondenser"],["Constructor" + base_recipe, "%Material%AtmosphericCondenser"]],
	"Chapter":"Production"+static_chapter,
	"Position": [-1,0],
	"CostMul":0.5,
})
append_levels({
	"Class": static_research,
	"Name": "StirlingEngine" + static_research,
	"LabelParts": [["StirlingEngine", "machines"]],
	"RequiredResearches": ["MineralsScan"+static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%StirlingEngine"],["Constructor" + base_recipe, "%Material%StirlingEngine"]],
	"Chapter":"Production"+static_chapter,
	"Position": [1,1],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "Furnace" + static_research,
	"LabelParts": [["Furnace", "machines"]],
	"RequiredResearches": ["StirlingEngine" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Furnace"],["Constructor" + base_recipe, "%Material%Furnace"]],
	"Chapter":"Production"+static_chapter,
	"Position": [2, 1],
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "Drying" + static_research,
	"LabelParts": [["Drying", "researches"]],
	"RequiredResearches": ["Furnace" + static_research,],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Oven"],["Constructor" + base_recipe, "%Material%Oven"]],
	"Position": [2,0],
	"Chapter":"Production"+static_chapter,
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "DistributedComputing" + static_research,
	"LabelParts": [["DistributedComputing", "researches"]],
	"RequiredResearches": ["PowerGeneration" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Computer"],["Constructor" + base_recipe, "%Material%Computer"]],
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
	"Unlocks": [["Hand" + base_recipe, "CopperWire"],["Assembler" + base_recipe, "CopperWire"]],
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
	"Unlocks": [["Hand" + base_recipe, "CircuitBoard"]],
	"Chapter":"Production"+static_chapter,
	"Position": [2,-3],
	"CostMul":0.25,
})
append_levels({
	"Class": static_research,
	"Name": "Circuit" + static_research,
	"LabelParts": [["Circuit", "parts"]],
	"RequiredResearches": ["CircuitBoard" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Circuit"],["Assembler" + base_recipe, "Circuit"]],
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
	"Unlocks": [["Hand" + base_recipe, "SteelLogicCircuit"],["Constructor" + base_recipe, "SteelLogicCircuit"],
	["Hand" + base_recipe, "SteelLogicController"],["Constructor" + base_recipe, "SteelLogicController"],
	["Hand" + base_recipe, "SteelLogicInterface"],["Constructor" + base_recipe, "SteelLogicInterface"],
	["Hand" + base_recipe, "SteelLogicDisplay"],["Constructor" + base_recipe, "SteelLogicDisplay"],
	["Hand" + base_recipe, "SteelLogicWire"],["Constructor" + base_recipe, "SteelLogicWire"]],
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
	"Unlocks": [["Hand" + base_recipe, "AdvancedCircuit"],["Assembler" + base_recipe, "AdvancedCircuit"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-4],
})
append_levels({
	"Class": static_research,
	"Name": "GoldWire" + static_research,
	"LabelParts": [["GoldWire", "parts"]],
	"RequiredResearches": ["AdvancedCircuit" + static_research, "OreWasher" + static_research],
	"Levels": [2,2],
	"Unlocks": [["Hand" + base_recipe, "GoldWire"],["Assembler" + base_recipe, "GoldWire"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-5],
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedCircuitBoard" + static_research,
	"LabelParts": [["AdvancedCircuitBoard", "parts"]],
	"RequiredResearches": ["GoldWire" + static_research, "PyrolysisUnit" + static_research],
	"Levels": [2,2],
	"Unlocks": [["Hand" + base_recipe, "AdvancedCircuitBoard"],["Assembler" + base_recipe, "AdvancedCircuitBoard"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-6],
})
append_levels({
	"Class": static_research,
	"Name": "Processor" + static_research,
	"LabelParts": [["Processor", "parts"]],
	"RequiredResearches": ["AdvancedCircuitBoard" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Processor"],["Assembler" + base_recipe, "Processor"],["Assembler" + base_recipe, "SiliconWafer"],["Assembler" + base_recipe, "Processor2"]],
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
	"Unlocks": [["Hand" + base_recipe, "QuantumCore"],["Assembler" + base_recipe, "QuantumCore"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-8],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumCircuit" + static_research,
	"LabelParts": [["QuantumCircuit", "parts"]],
	"RequiredResearches": ["QuantumCore" + static_research],
	"Levels": [4,4],
	"Unlocks": [["Hand" + base_recipe, "QuantumCircuit"],["Assembler" + base_recipe, "QuantumCircuit"]],
	"Chapter":"Production"+static_chapter,
	"Position": [3,-9],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumProcessor" + static_research,
	"LabelParts": [["QuantumProcessor", "parts"]],
	"RequiredResearches": ["QuantumCircuit" + static_research],
	"Levels": [5,5],
	"Unlocks": [["Hand" + base_recipe, "QuantumProcessor"],["Assembler" + base_recipe, "QuantumProcessor"]],
	"Chapter":"Production"+static_chapter,
	"Position": [4,-10],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumBrain" + static_research,
	"LabelParts": [["QuantumBrain", "parts"]],
	"RequiredResearches": ["QuantumProcessor" + static_research],
	"Levels": [6,6],
	"Unlocks": [["Hand" + base_recipe, "QuantumBrain"],["Assembler" + base_recipe, "QuantumBrain"]],
	"Chapter":"Production"+static_chapter,
	"Position": [4,-11],
})
append_levels({
	"Class": static_research,
	"Name": "QuantumComputer" + static_research,
	"LabelParts": [["QuantumComputer", "machines"]],
	"RequiredResearches": ["QuantumCircuit" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%QuantumComputer"],["Constructor" + base_recipe, "%Material%QuantumComputer"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%Corner"],["Constructor" + base_recipe, "%Material%Corner"],
	["Hand" + base_recipe, "%Material%Casing"],["Constructor" + base_recipe,"%Material%Casing"],
	["Hand" + base_recipe, "%Material%Beam"],["Constructor" + base_recipe, "%Material%Beam"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%Scaffold"],["Constructor" + base_recipe, "%Material%Scaffold"]],
	"Levels": [1,7],
	"Position": [3, 4],
})
append_levels({
	"Class": static_research,
	"Name": "Chemistry" + static_research,
	"LabelParts": [["Chemistry", "researches"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["ElectricEngine" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%ChemReactor"],["Constructor" + base_recipe, "%Material%ChemReactor"]],
	"Levels": [2,7],
	"Position": [5,-2],
})
append_levels({
	"Class": static_research,
	"Name": "Catalyst" + static_research,
	"LabelParts": [["Catalyst", "parts"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Chemistry" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Catalyst"],["Assembler" + base_recipe, "Catalyst"]],
	"Levels": [2,2],
	"Position": [5,-3],
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialChemReactor" + static_research,
	"LabelParts": [["IndustrialChemReactor", "machines"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Catalyst" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialChemReactor"],["Constructor" + base_recipe, "%Material%IndustrialChemReactor"]],
	"Levels": [3,7],
	"Position": [5,-6],
})
append_levels({
	"Class": static_research,
	"Name": "FuelChemistry" + static_research,
	"LabelParts": [["FuelChemistry", "researches"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["IndustrialChemReactor" + static_research],
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "Superfuel"], ["IndustrialChemReactor" + base_recipe, "RocketFuel"]],
	"Levels": [3,3],
	"Position": [6,-7],
})
append_levels({
	"Class": static_research,
	"Name": "FuelChemistry2" + static_research,
	"LabelParts": [["FuelChemistry2", "researches"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["FuelChemistry" + static_research],
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "RocketFuel2"], ["IndustrialChemReactor" + base_recipe, "Superfuel2"]],
	"Levels": [3,3],
	"Position": [6,-8],
})
append_levels({
	"Class": static_research,
	"Name": "Sifter" + static_research,
	"LabelParts": [["Sifter", "machines"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Chemistry" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Sifter"],["Constructor" + base_recipe, "%Material%Sifter"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%Separator"],["Constructor" + base_recipe, "%Material%Separator"]],
	"Position": [4,-3],
})
append_levels({
	"Class": static_research,
	"Name": "ElectricEngine" + static_research,
	"LabelParts": [["ElectricEngine", "machines"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Electrolysis" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ElectricEngine"],["Constructor" + base_recipe, "%Material%ElectricEngine"]],
	"Position": [4,-2],
})
append_levels({
	"Class": static_research,
	"Name": "BiElectricEngine" + static_research,
	"LabelParts": [["BiElectricEngine", "machines"]],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["ElectricEngine" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BiElectricEngine"],["Constructor" + base_recipe, "%Material%BiElectricEngine"]],
	"Position": [3,-2],
})
append_levels({
	"Class": static_research,
	"Name": "OreWasher" + static_research,
	"LabelParts": [["OreWasher", "machines"]],
	"Levels": [2,7],
	"Chapter":"Production"+static_chapter,
	"RequiredResearches": ["Separator" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%OreWasher"],["Constructor" + base_recipe, "%Material%OreWasher"]],
	"Position": [4,-4],
})
append_levels({
	"Class": static_research,
	"Name": "Mixer" + static_research,
	"LabelParts": [["Mixer", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["OreWasher" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Mixer"],["Constructor" + base_recipe, "%Material%Mixer"]],
	"Position": [4,-5],
})
append_levels({
	"Class": static_research,
	"Name": "ChemicalBath" + static_research,
	"LabelParts": [["ChemicalBath", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialChemReactor" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ChemicalBath"],["Constructor" + base_recipe, "%Material%ChemicalBath"]],
	"Position": [5,-7],
})
append_levels({
	"Class": static_research,
	"Name": "OilCrackingTower" + static_research,
	"LabelParts": [["OilCrackingTower", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["FuelChemistry" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%OilCrackingTower"],["Constructor" + base_recipe, "%Material%OilCrackingTower"]],
	"Position": [5,-8],
})
append_levels({
	"Class": static_research,
	"Name": "CombustionEngine" + static_research,
	"LabelParts": [["CombustionEngine", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialChemReactor" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CombustionEngine"],["Constructor" + base_recipe, "%Material%CombustionEngine"]],
	"Position": [4,-7],
})
append_levels({
	"Class": static_research,
	"Name": "StainlessSteelProduction" + static_research,
	"LabelParts": [["StainlessSteelProduction", "researches"]],
	"RequiredResearches": ["Chemistry" + static_research, "AluminiumProduction" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[4]),
	"AlsoUnlocks": [["Hand" + base_recipe, "Cell"]],
	"Chapter": "Production" + static_chapter,
	"Position": [6,-2],
	"Levels": [4,4],
	"CostLevelOffset": -1,
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "AdvancedSeparation" + static_research,
	"LabelParts": [["AdvancedSeparation", "researches"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["AluminiumProduction" + static_research],
	"Position": [6,-1],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSeparator"],["Constructor" + base_recipe, "%Material%IndustrialSeparator"]],
})
append_levels({
	"Class": static_research,
	"Name": "SmallBattery" + static_research,
	"LabelParts": [["SmallBattery", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["AdvancedSeparation" + static_research],
	"Position": [6,0],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%SmallBattery"],["Constructor" + base_recipe, "%Material%SmallBattery"]],
})
append_levels({
	"Class": static_research,
	"Name": "TitaniumProduction" + static_research,
	"LabelParts": [["TitaniumProduction", "researches"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialSmelting" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[5]),
	"Position": [7,-4],
	"Levels": [4,4],
	"CostLevelOffset": -1,
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialBoiler" + static_research,
	"LabelParts": [["IndustrialBoiler", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["TitaniumProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialBoiler"],["Connector" + base_recipe, "%Material%IndustrialBoiler"]],
	"Position": [6,-4],
	"Levels": [5,7],
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialSteamTurbine" + static_research,
	"LabelParts": [["IndustrialSteamTurbine", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialBoiler" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSteamTurbine"],["Connector" + base_recipe, "%Material%IndustrialSteamTurbine"]],
	"Position": [6,-5],
	"Levels": [5,7],
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialGenerator" + static_research,
	"LabelParts": [["IndustrialGenerator", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialSteamTurbine" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialGenerator"],["Connector" + base_recipe, "%Material%IndustrialGenerator"]],
	"Position": [6,-6],
	"Levels": [5,7],
})
append_levels({
	"Class": static_research,
	"Name": "Freezer" + static_research,
	"LabelParts": [["Freezer", "machines"]],
	"RequiredResearches": ["TitaniumProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Freezer"],["Constructor" + base_recipe, "%Material%Freezer"]],
	"Chapter": "Production"+static_chapter,
	"Position": [8,-4],
	"Levels": [5,7],
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "HardMetalProduction" + static_research,
	"LabelParts": [["HardMetalProduction", "researches"]],
	"RequiredResearches": ["Freezer" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[6]),
	"Chapter": "Production" + static_chapter,
	"Position": [9,-4],
	"Levels": [5,5],
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "FusionReactor" + static_research,
	"LabelParts": [["FusionReactor", "machines"]],
	"RequiredResearches": ["HardMetalProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%FusionReactor"],["Constructor" + base_recipe, "%Material%FusionReactor"]],
	"Chapter":"Production"+static_chapter,
	"Position": [10,-4],
	"Levels": [6,7],
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "NeutroniumProduction" + static_research,
	"LabelParts": [["NeutroniumProduction", "researches"]],
	"RequiredResearches": ["FusionReactor" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[7]),
	"Chapter": "Production" + static_chapter,
	"Position": [11,-5],
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "UltimateCatalyst" + static_research,
	"LabelParts": [["UltimateCatalyst", "parts"]],
	"RequiredResearches": ["NeutroniumProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "UltimateCatalyst"],["Assembler" + base_recipe, "UltimateCatalyst"]],
	"Chapter": "Production" + static_chapter,
	"Position": [11,-4],
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	 "Class": static_research,
	 "Name": "Portal" + static_research,
	 "LabelParts": [["Portal", "machines"]],
	 "RequiredResearches": ["UltimateCatalyst" + static_research],
	 "Unlocks": [["Hand" + base_recipe, "%Material%Portal"],["Constructor" + base_recipe, "%Material%Portal"]],
	 "Chapter": "Production" + static_chapter,
	 "Position": [12,-4],
	 "Levels": [7,7],
	 "MainResearch": True,
 })
append_levels({
	"Class": static_research,
	"Name": "FissionReactor" + static_research,
	"LabelParts": [["FissionReactor", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["UraniumCell" + static_research],
	"Levels": [5,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%FissionReactor"],["Constructor" + base_recipe, "%Material%FissionReactor"]],
	"Position": [7,-6],
})
append_levels({
	"Class": static_research,
	"Name": "UraniumCell" + static_research,
	"LabelParts": [["UraniumCell", "parts"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["TitaniumProduction" + static_research],
	"Levels": [5,5],
	"Unlocks": [["Hand" + base_recipe, "UraniumCell"],["Assembler" + base_recipe, "UraniumCell"]],
	"Position": [7,-5],
})
append_nuclear([7,-7], append_levels, researches)
append_levels({
	"Class": static_research,
	"Name": "IndustrialSmelting" + static_research,
	"LabelParts": [["IndustrialSmelting", "researches"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["StainlessSteelProduction" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSmelter"],["Constructor" + base_recipe, "%Material%IndustrialSmelter"]],
	"Position": [7,-2],
	"MainResearch": True,
})
append_levels({
	"Class": static_research,
	"Name": "Fermentation" + static_research,
	"LabelParts": [["Fermentation", "researches"]],
	"Levels": [4,7],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialSmelting" + static_research],
	"Position": [7,-3],
	"Unlocks": [["Hand" + base_recipe, "%Material%Fermenter"],["Constructor" + base_recipe, "%Material%Fermenter"]],
})
append_levels({
	"Class": static_research,
	"Name": "BatteryBox" + static_research,
	"LabelParts": [["BatteryBox", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialSmelting" + static_research],
	"Position": [8,-2],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BatteryBox"],["Constructor" + base_recipe, "%Material%BatteryBox"]],
})
append_levels({
	"Class": static_research,
	"Name": "InductionCoil" + static_research,
	"LabelParts": [["InductionCoil", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["IndustrialSmelting" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%InductionCoil"],["Constructor" + base_recipe, "%Material%InductionCoil"]],
	"Position": [8,-3],
})
append_levels({
	"Class": static_research,
	"Name": "IndustrialElectricEngine" + static_research,
	"LabelParts": [["IndustrialElectricEngine", "machines"]],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["InductionCoil" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialElectricEngine"],["Constructor" + base_recipe, "%Material%IndustrialElectricEngine"]],
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
	"Unlocks": [["Hand" + base_recipe, tier_material[4] + "Terminal"],["Constructor" + base_recipe, tier_material[4] + "Terminal"]],
})
append_levels({
	"Class": static_research,
	"Name": "FlatTerminal" + static_research,
	"LabelParts": [["FlatTerminal", "machines"]],
	"Levels": [4,4],
	"Position": [8,-1],
	"Chapter": "Production" + static_chapter,
	"RequiredResearches": ["Terminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[4] + "FlatTerminal"],["Constructor" + base_recipe, tier_material[4] + "FlatTerminal"]],
})
append_levels({
	"Class": static_research,
	"Name": "Constructor" + static_research,
	"LabelParts": [["Constructor", "machines"]],
	"Position": [1,5],
	"RequiredResearches": ["Assembler" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Constructor"],["Constructor" + base_recipe, "%Material%Constructor"]],
	"Levels": [2, 7],
	"Chapter": "Production" + static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "Assembler" + static_research,
	"LabelParts": [["Assembler", "machines"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Assembler"],["Constructor" + base_recipe, "%Material%Assembler"]],
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
	"Unlocks": [["Hand" + base_recipe, "%Material%Deconstructor"],["Constructor" + base_recipe, "%Material%Deconstructor"]],
	"Levels": [2,7],
	"Chapter": "Production" + static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "BigTerminal" + static_research,
	"LabelParts": [["BigTerminal", "machines"]],
	"RequiredResearches": ["Terminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[5] + "BigTerminal"],["Constructor" + base_recipe, tier_material[5] + "BigTerminal"]],
	"Levels": [4,4],
	"Chapter": "Production" + static_chapter,
	"Position": [7,0],
})
append_levels({
	"Class": static_research,
	"Name": "BigFlatTerminal" + static_research,
	"LabelParts": [["BigFlatTerminal", "machines"]],
	"RequiredResearches": ["BigTerminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[5] + "BigFlatTerminal"],["Constructor" + base_recipe, tier_material[5] + "BigFlatTerminal"]],
	"Chapter": "Production" + static_chapter,
	"Levels": [4,4],
	"Position": [8,0],
})
append_levels({
	"Class": static_research,
	"Name": "HugeTerminal" + static_research,
	"LabelParts": [["HugeTerminal", "machines"]],
	"RequiredResearches": ["BigTerminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[6] + "HugeTerminal"],["Constructor" + base_recipe, tier_material[6] + "HugeTerminal"]],
	"Chapter": "Production" + static_chapter,
	"Levels": [5,5],
	"Position": [7,1],
})
append_levels({
	"Class": static_research,
	"Name": "HugeFlatTerminal" + static_research,
	"LabelParts": [["HugeFlatTerminal", "machines"]],
	"RequiredResearches": ["HugeTerminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[6] + "HugeFlatTerminal"],["Constructor" + base_recipe, tier_material[6] + "HugeFlatTerminal"]],
	"Chapter": "Production" + static_chapter,
	"Levels": [5,5],
	"Position": [8,1],
}) 
append_levels({
	"Class": static_research,
	"Name": "PyrolysisUnit" + static_research,
	"LabelParts": [["PyrolysisUnit", "machines"]],
	"RequiredResearches": ["Mixer" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%PyrolysisUnit"],["Constructor" + base_recipe, "%Material%PyrolysisUnit"]],
	"Levels": [3,7],
	"Chapter": "Production" + static_chapter,
	"Position": [4,-6],
})
	
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood" + static_research,
	"LabelParts": [["DecorativeWood", "researches"]],
	"Unlocks": [["Hand" + base_recipe, "WoodenPlanks"],["Hand" + base_recipe, "WoodenStairs"],["Hand" + base_recipe, "Bed"],["Hand" + base_recipe, "Door"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [0,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood2" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[1], "common"]],
	"RequiredResearches": ["DecorativeWood" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Chair"],["Hand" + base_recipe, "Fence"],["Hand" + base_recipe, "Ladder"],["Hand" + base_recipe, "Rack"],["Hand" + base_recipe, "Table"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [0,1],
})
append_levels({
	"Class": static_research,
	"Name": "Fence" + static_research,
	"LabelParts": [["Fence", "misc"]],
	"RequiredResearches": ["DecorativeWood2" + static_research],
	"Unlocks": [["Hand" + base_recipe, "SteelFence"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [-1,1],
})
append_levels({
	"Class": static_research,
	"Name": "Fence1" + static_research,
	"LabelParts": [["Fence", "misc"], [level_labels[1], "common"]],
	"RequiredResearches": ["Fence" + static_research],
	"Unlocks": [["Hand" + base_recipe, "StainlessSteelFence"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [-2,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood4" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[3], "common"]],
	"RequiredResearches": ["DecorativeWood2" + static_research],
	"Unlocks": [["Hand" + base_recipe, "CopperChair"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [1,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeWood3" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[2], "common"]],
	"RequiredResearches": ["DecorativeWood2" + static_research, "AdvancedSmelting" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Window"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [0,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativePlastic" + static_research,
	"LabelParts": [["DecorativePlastic", "researches"]],
	"RequiredResearches": ["Chemistry" + static_research, "PyrolysisUnit" + static_research, "DecorativeWood3" + static_research],

	"Unlocks": [["Hand" + base_recipe, "PlasticWindow"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [-1,2],
})
append_levels({
	"Class": static_research,
	"Name": "PlasticBlock" + static_research,
	"LabelParts": [["PlasticBlock", "misc"]],
	"RequiredResearches": ["DecorativePlastic" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "PlasticBlock"],["Press" + base_recipe, "PlasticBlock"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [-2,2],
})
append_levels({
	"Class": static_research,
	"Name": "BasicPlatform" + static_research,
	"LabelParts": [["BasicPlatform", "misc"]],
	"CompleteByDefault": True,
	"Chapter": "Decorations"+static_chapter,
	"Unlocks": [["Hand" + base_recipe, "BasicPlatform"], ["Press" + base_recipe, "BasicPlatform"]],
	"Position": [1,-1],
	"RequiredResearches": []
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone" + static_research,
	"LabelParts": [["DecorativeStone", "researches"]],
	"RequiredResearches": ["BasicPlatform"+static_research], 
	"Unlocks": [["Hand" + base_recipe, "StoneTiles"], ["CuttingMachine" + base_recipe, "StoneTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [1,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone2" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorativeStone" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "DarkTiles"],["Hand" + base_recipe, "RedTiles"],["CuttingMachine" + base_recipe, "DarkTiles"],["CuttingMachine" + base_recipe, "RedTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [2,0],
})
append_levels({
	"Class": static_research,
	"Name": "GlassBlock" + static_research,
	"LabelParts": [["GlassBlock", "misc"]],

	"RequiredResearches": [], 
	"Unlocks": [["Hand" + base_recipe, "GlassBlock"],["Press" + base_recipe, "GlassBlock"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [2,-1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone3" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[2], "common"]],

	"RequiredResearches": ["DecorativeStone2" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "DarkBricks"],["Hand" + base_recipe, "RedBricks"],["Hand" + base_recipe, "Bricks"],["CuttingMachine" + base_recipe, "DarkBricks"],["CuttingMachine" + base_recipe, "RedBricks"],["CuttingMachine" + base_recipe, "Bricks"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [2,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeStone4" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[3], "common"]],

	"RequiredResearches": ["DecorativeStone3" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "Stairs"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [2,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete" + static_research,
	"LabelParts": [["DecorativeConcrete", "researches"]],
	"RequiredResearches": ["Mixer" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ConcreteTiles"], ["CuttingMachine" + base_recipe, "ConcreteTiles"],
			 ["Hand" + base_recipe, "ConcreteBeam"], ["Press" + base_recipe, "ConcreteBeam"]],
	"Chapter": "Decorations" + static_chapter,
	"Levels": [1, 2],
	"Position": [3,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete2" + static_research,
	"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorativeConcrete" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ConcreteSmallTiles"], ["CuttingMachine" + base_recipe, "ConcreteSmallTiles"],
			 ["Hand" + base_recipe, "ConcreteBeam2"], ["Press" + base_recipe, "ConcreteBeam2"],
			 ["Hand" + base_recipe, "ConcreteRamp3"], ["Press" + base_recipe, "ConcreteRamp3"]],
	"Chapter": "Decorations" + static_chapter,
	"Levels": [1, 3],
	"Position": [3,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete3" + static_research,
	"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[2], "common"]],

	"RequiredResearches": ["DecorativeConcrete2" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ConcreteBricks"], ["CuttingMachine" + base_recipe, "ConcreteBricks"],
			 ["Hand" + base_recipe, "ConcreteRamp"], ["Press" + base_recipe, "ConcreteRamp"],
			 ["Hand" + base_recipe, "ConcreteRamp2"], ["Press" + base_recipe, "ConcreteRamp2"]],
	"Chapter": "Decorations" + static_chapter,
	"Levels": [2, 4],
	"Position": [3,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeConcrete4" + static_research,
	"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[3], "common"]],

	"RequiredResearches": ["DecorativeConcrete3" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "DangerBlock"]],
	"Chapter": "Decorations" + static_chapter,
	"Levels": [3, 3],
	"Position": [3,3],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeReinforcedConcrete" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"]],

	"RequiredResearches": ["DecorativeConcrete" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteTiles"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [4,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeReinforcedConcrete2" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorativeReinforcedConcrete" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteSmallTiles"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteSmallTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [4,1],
})
append_levels({
	"Class": static_research,
	"Name": "DecorativeReinforcedConcrete3" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[2], "common"]],

	"RequiredResearches": ["DecorativeReinforcedConcrete2" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteBricks"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteBricks"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [4,2],
})
append_levels({
	"Class": static_research,
	"Name": "DecorationClay" + static_research,
	"LabelParts": [["DecorationClay", "researches"]],

	"RequiredResearches": ["Drying" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "TerracottaTiles"], ["CuttingMachine" + base_recipe, "TerracottaTiles"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [5,0],
})
append_levels({
	"Class": static_research,
	"Name": "DecorationClay2" + static_research,
	"LabelParts": [["DecorationClay", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorationClay" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "TerracottaBricks"], ["CuttingMachine" + base_recipe, "TerracottaBricks"]],
	"Chapter": "Decorations" + static_chapter,
	"Position": [5,1],
})
append_levels({
	"Class": static_research,
	"Name": "Press" + static_research,
	"LabelParts": [["Press", "machines"]],
	"RequiredResearches": [],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Press"],["Constructor" + base_recipe, "%Material%Press"]],
	"Position": [2, 3],
	"Chapter": "Decorations"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "PaintTool" + static_research,
	"LabelParts": [["PaintTool", "parts"]],
	"RequiredResearches": [],
	"Levels": [1,1],
	"Unlocks": [["Hand" + base_recipe, "CopperPaintTool"],["Constructor" + base_recipe, "CopperPaintTool"]],
	"Position": [1, 2],
	"Chapter": "Decorations"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "Lamp" + static_research,
	"LabelParts": [["Lamp", "machines"]],
	"RequiredResearches": [],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Lamp"],["Constructor" + base_recipe, "%Material%Lamp"]],
	"Position": [2, 4],
	"Chapter": "Decorations"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "Column" + static_research,
	"LabelParts": [["Column", "misc"]],
	"RequiredResearches": [],
	"Levels": [1,1],
	"Unlocks": [["Hand" + base_recipe, "Column"],["Hand" + base_recipe, "FluetedColumn"],["Press" + base_recipe, "Column"],["Press" + base_recipe, "FluetedColumn"]],
	"Position": [1, 4],
	"Chapter": "Decorations"+static_chapter,
})
append_levels({
	"Class": static_research,
	"Name": "Sign" + static_research,
	"LabelParts": [["Sign", "machines"]],
	"RequiredResearches": ["MineralsScan" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Sign"],["Constructor" + base_recipe, "%Material%Sign"]],
	"Levels": [0,7],
	"Chapter": "Decorations"+static_chapter,
	"Position": [0,3],

})
append_levels({
	"Class": static_research,
	"Name": "AdvancedSign" + static_research,
	"LabelParts": [["AdvancedSign", "machines"]],
	"RequiredResearches": ["Sign" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%AdvancedSign"],["Constructor" + base_recipe, "%Material%AdvancedSign"]],
	"Levels": [2,7],
	"Chapter": "Decorations"+static_chapter,
	"Position": [1,3],
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
csv.append(["FuelChemistry", "Fuel Chemistry"])
csv.append(["FuelChemistry2", "Fuel Chemistry II"])

write_file("Generated/Researches/basic.json", data);
write_file("Loc/source/researches.json", csv)
