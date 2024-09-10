from Common import *
from Materials import *
import copy
from NuclearResearches import *
from EquipmentResearches import *
from PartsResearchHelper import *

researches = []

tier_researches = [
	"InitialScan",
	"InitialScan",
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
		if i != mini:
			research["IsUpgrade"] = True
			research["MainResearch"] = False
			research["CompleteByDefault"] = False
			research["Name"] = research["Name"] + str(thisLevel)
			if i != mini + 1:
				research["RequiredResearches"] = [research_base["Name"] + str(thisLevel - 1)]
			else:
				research["RequiredResearches"] = [research_base["Name"]]

			research["RequiredResearches"].append(tier_researches[i])

		if "Unlocks" in research:
			unl = copy.deepcopy(research["Unlocks"])
			research["Unlocks"] = []
			
			new = []
			for j in unl:
				new.append([j[0], j[1].replace("%Material%", tier_material[i])])                
			research["Unlocks"].append(new)
		
		CostSub = research["CostSub"] if "CostSub" in research else 0
		CostMul = research["CostMul"] if "CostMul" in research else 1
		offset = research["CostLevelOffset"] if "CostLevelOffset" in research else 0

		research["Levels"] = [i,i]
		research["DataPoints"] = {"Items" : res_cost(i - CostSub + offset, CostMul)}
    
		researches.append(research)

append_levels({
	"Class": "StaticResearchToolUnlock",
	"Name": "InitialScan" + static_research,
	"LabelParts": [["InitialScan", "researches"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "MineralsScan" + static_research,
	"LabelParts": [["MineralsScan", "researches"]],
	"RequiredResearches": ["InitialScan" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[0] + "Furnace"],["Constructor" + base_recipe, tier_material[0] + "Furnace"],["Hand" + base_recipe, "SandSurface"],["Hand" + base_recipe, "GravelSurface"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdditionalStorage" + static_research,
	"LabelParts": [["AdditionalStorage", "researches"]],
	"RequiredResearches": ["MineralsScan" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Chest"],["Constructor" + base_recipe, "%Material%Chest"]],
	"Levels":[0,7],
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SingleTypeStorage" + static_research,
	"LabelParts": [["SingleTypeStorage", "researches"]],
	"RequiredResearches": ["AdditionalStorage" + static_research ],
	
	"Levels":[1,7],
	
	"Unlocks": [["Hand" + base_recipe, "%Material%ItemRack"],["Constructor" + base_recipe, "%Material%ItemRack"]],
})
append_levels({
	"Class": "StaticResearchBonusInventory",
	"Name": "InventoryUpgrade" + static_research,
	"LabelParts": [["InventoryUpgrade", "researches"]],
	"RequiredResearches": ["AdditionalStorage" + static_research],
	"Unlocks": [],
	"Levels": [0,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Electricity" + static_research,
	"LabelParts": [["Electricity", "researches"]],
	"RequiredResearches": ["InitialScan"+static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[1] + "Connector"], ["Constructor" + base_recipe, tier_material[1] + "Connector"],["Hand" + base_recipe, tier_material[1] + "HandGenerator"],["Constructor" + base_recipe, tier_material[1] + "HandGenerator"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricFurnace" + static_research,
	"LabelParts": [["ElectricFurnace", "machines"]],
	"Levels": [2,7],
	"RequiredResearches": ["CopperWire" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%ElectricFurnace"],["Constructor" + base_recipe, "%Material%ElectricFurnace"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricalSwitch" + static_research,
	"LabelParts": [["ElectricalSwitch", "machines"]],
	"RequiredResearches": ["CopperWire" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "ElectricalSwitch"],["Constructor" + base_recipe, tier_material[2] + "ElectricalSwitch"]],
	"Levels": [2,2],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Diode" + static_research,
	"LabelParts": [["Diode", "machines"]],
	
	"RequiredResearches": ["ElectricalSwitch" + static_research],
	"Levels": [2,7],
	
	"Unlocks": [["Hand" + base_recipe, "%Material%Diode"],["Constructor" + base_recipe, "%Material%Diode"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PowerGeneration" + static_research,
	"LabelParts": [["PowerGeneration", "researches"]],
	"RequiredResearches": ["Electricity" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CompactGenerator"],["Constructor" + base_recipe, "%Material%CompactGenerator"]],
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Electrolysis" + static_research,
	"LabelParts": [["Electrolysis", "researches"]],
	"RequiredResearches": ["SteelProduction" + static_research], 
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Electrolyzer"],["Constructor" + base_recipe, "%Material%Electrolyzer"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SteelProduction" + static_research,
	"LabelParts": [["SteelProduction", "researches"]],
	"RequiredResearches": ["Drying"+static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BlastFurnace"],["Constructor" + base_recipe, "%Material%BlastFurnace"]],
	"AlsoUnlocks": get_parts_unlocks(tier_material[2]),
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSmelting" + static_research,
	"LabelParts": [["AdvancedSmelting", "researches"]],
	"RequiredResearches": ["SteelProduction" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ArcSmelter"],["Constructor" + base_recipe, "%Material%ArcSmelter"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SolarPanel" + static_research,
	"LabelParts": [["SolarPanel", "machines"]],
	"RequiredResearches": ["SiliconWafer" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%SolarPanel"],["Constructor" + base_recipe, "%Material%SolarPanel"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AluminiumProduction" + static_research,
	"LabelParts": [["AluminiumProduction", "researches"]],
	"RequiredResearches": ["AdvancedSmelting" + static_research, "Electrolysis" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[3]),
	"Levels": [3,3],
	"CostLevelOffset": -1,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "MassivePowerGeneration" + static_research,
	"LabelParts": [["MassivePowerGeneration", "researches"]],
	"RequiredResearches": ["PowerGeneration" + static_research ],
	"Unlocks": [["Hand" + base_recipe, "%Material%Generator"],["Constructor" + base_recipe, "%Material%Generator"],
	["Hand" + base_recipe, "%Material%Boiler"],["Constructor" + base_recipe, "%Material%Boiler"],
	["Hand" + base_recipe, "%Material%SteamTurbine"],["Constructor" + base_recipe, "%Material%SteamTurbine"]],
	"Levels": [2,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GasTurbine" + static_research,
	"LabelParts": [["GasTurbine", "machines"]],
	"RequiredResearches": ["MassivePowerGeneration" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%GasTurbine"],["Constructor" + base_recipe, "%Material%GasTurbine"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Smelting" + static_research,
	"LabelParts": [["Smelting", "researches"]],
	"RequiredResearches": ["MineralsScan"+static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Smelter"], ["Constructor" + base_recipe, "%Material%Smelter"]],
	"Levels": [0,2],
	"CompleteByDefault": True,
})
append_equipment([-1,3], append_levels, researches)
append_levels({
	"Class": "StaticResearch",
	"Name": "Metalwork" + static_research,
	"LabelParts": [["Metalwork", "researches"]],
	"RequiredResearches": ["Smelting"+static_research],
	"Unlocks": get_parts_unlocks(tier_material[1]),
	"Levels": [1,1],
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Valve" + static_research,
	"LabelParts": [["Vent", "machines"]],
	"RequiredResearches": ["Metalwork" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[1] + "Vent"],["Constructor" + base_recipe, tier_material[1] + "Vent"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BasicMachines" + static_research,
	"LabelParts": [["BasicMachines", "researches"]],
	"RequiredResearches": ["Metalwork" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Macerator"],["Constructor" + base_recipe, "%Material%Macerator"],
	["Hand" + base_recipe, "%Material%AutomaticHammer"],["Constructor" + base_recipe, "%Material%AutomaticHammer"]],
	"CostMul":0.25
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Flywheel" + static_research,
	"LabelParts": [["Flywheel", "machines"]],
	"RequiredResearches": ["BasicMachines" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "Flywheel"],["Constructor" + base_recipe, tier_material[2] + "Flywheel"]],
	"Levels": [2,2],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Cutting" + static_research,
	"LabelParts": [["Cutting", "researches"]],
	"RequiredResearches": ["BasicMachines" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CuttingMachine"],["Constructor" + base_recipe, "%Material%CuttingMachine"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SolidDump" + static_research,
	"LabelParts": [["SolidDump", "machines"]],
	"Levels": [2,2],
	"RequiredResearches": ["Furnace" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "SolidDump"],["Constructor" + base_recipe, tier_material[2] + "SolidDump"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Pump" + static_research,
	"LabelParts": [["Pump", "machines"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Pump"],["Constructor" + base_recipe, "%Material%Pump"]],
	"CostMul":0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Container" + static_research,
	"LabelParts": [["Container", "machines"]],
	"RequiredResearches": ["Pump" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Container"],["Constructor" + base_recipe, "%Material%Container"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FluidFurnace" + static_research,
	"LabelParts": [["FluidFurnace", "machines"]],
	"RequiredResearches": ["Furnace" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%FluidFurnace"],["Constructor" + base_recipe, "%Material%FluidFurnace"]],
	"Levels": [1,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FluidDumping" + static_research,
	"LabelParts": [["FluidDumping", "researches"]],
	"RequiredResearches": ["Container" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%FluidDump"],["Constructor" + base_recipe, "%Material%FluidDump"]],
	"CostMul":0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GasDump" + static_research,
	"LabelParts": [["GasDump", "machines"]],
	"Levels": [2,2],
	"RequiredResearches": ["Container" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "GasDump"],["Constructor" + base_recipe, tier_material[2] + "GasDump"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Automatization" + static_research,
	"LabelParts": [["Automatization", "researches"]],
	"RequiredResearches": ["BasicMachines" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%RobotArm"],["Constructor" + base_recipe, "%Material%RobotArm"],
	["Hand" + base_recipe, "%Material%Conveyor"],["Constructor" + base_recipe, "%Material%Conveyor"],
	["Hand" + base_recipe, "%Material%Splitter"],["Constructor" + base_recipe, "%Material%Splitter"]],
	"CostMul":0.25
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Filtering" + static_research,
	"LabelParts": [["Filtering", "researches"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%FilteringRobotArm"],["Constructor" + base_recipe, "%Material%FilteringRobotArm"],
	["Hand" + base_recipe, "%Material%Sorter"],["Constructor" + base_recipe, "%Material%Sorter"]],
	"Levels": [1,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FilteringPump" + static_research,
	"LabelParts": [["FilteringPump", "machines"]],
	"RequiredResearches": ["Pump" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%FilteringPump"],["Constructor" + base_recipe, "%Material%FilteringPump"]],
	"Levels": [1,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OverflowPump" + static_research,
	"LabelParts": [["OverflowPump", "machines"]],
	"RequiredResearches": ["FilteringPump" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%OverflowPump"],["Constructor" + base_recipe, "%Material%OverflowPump"]],
	"Levels": [1,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AutomaticMining" + static_research,
	"LabelParts": [["AutomaticMining", "researches"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%DrillingRig"],["Constructor" + base_recipe, "%Material%DrillingRig"]],
	"CostMul":0.5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Pumpjack" + static_research,
	"LabelParts": [["Pumpjack", "machines"]],
	"RequiredResearches": ["AutomaticMining" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Pumpjack"],["Constructor" + base_recipe, "%Material%Pumpjack"]],
	"Levels": [3,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AutomaticFarm" + static_research,
	"LabelParts": [["AutomaticFarm", "machines"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%AutomaticFarm"],["Constructor" + base_recipe, "%Material%AutomaticFarm"]],
	"CostMul":0.5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HeatTransferring" + static_research,
	"LabelParts": [["HeatTransferring", "researches"]],
	"RequiredResearches": ["InitialScan" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%HeatPipe"],["Constructor" + base_recipe, "%Material%HeatPipe"]],
	"Levels":[1,1],
	"CostMul":0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "KineticHeater" + static_research,
	"LabelParts": [["KineticHeater", "machines"]],
	"RequiredResearches": ["HeatTransferring" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%KineticHeater"],["Constructor" + base_recipe, "%Material%KineticHeater"]],
	"Levels":[1,7],
	"CostMul":1,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Radiator" + static_research,
	"LabelParts": [["Radiator", "machines"]],
	"RequiredResearches": ["HeatTransferring" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Radiator"],["Constructor" + base_recipe, "%Material%Radiator"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AtmosphericCondenser" + static_research,
	"LabelParts": [["AtmosphericCondenser", "machines"]],
	"RequiredResearches": ["InitialScan" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%AtmosphericCondenser"],["Constructor" + base_recipe, "%Material%AtmosphericCondenser"]],
	"CostMul":0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "StirlingEngine" + static_research,
	"LabelParts": [["StirlingEngine", "machines"]],
	"RequiredResearches": ["MineralsScan"+static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%StirlingEngine"],["Constructor" + base_recipe, "%Material%StirlingEngine"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Furnace" + static_research,
	"LabelParts": [["Furnace", "machines"]],
	"RequiredResearches": ["StirlingEngine" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Furnace"],["Constructor" + base_recipe, "%Material%Furnace"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Drying" + static_research,
	"LabelParts": [["Drying", "researches"]],
	"RequiredResearches": ["Furnace" + static_research,],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Oven"],["Constructor" + base_recipe, "%Material%Oven"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DistributedComputing" + static_research,
	"LabelParts": [["DistributedComputing", "researches"]],
	"RequiredResearches": ["PowerGeneration" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Computer"],["Constructor" + base_recipe, "%Material%Computer"]],
	"Levels": [1,7],
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CopperWire" + static_research,
	"LabelParts": [["CopperWire", "parts"]],
	"RequiredResearches": ["DistributedComputing" + static_research],
	"Levels": [1,1],
	"Unlocks": [["Hand" + base_recipe, "CopperWire"],["Assembler" + base_recipe, "CopperWire"]],
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CircuitBoard" + static_research,
	"LabelParts": [["CircuitBoard", "parts"]],
	"RequiredResearches": ["CopperWire" + static_research],
	"Levels": [1,1],
	"Unlocks": [["Hand" + base_recipe, "CircuitBoard"]],
	"CostMul":0.25,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Circuit" + static_research,
	"LabelParts": [["Circuit", "parts"]],
	"RequiredResearches": ["CircuitBoard" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Circuit"],["Assembler" + base_recipe, "Circuit"]],
	"Levels": [1,1],
	"CostMul":0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "LogicCircuit" + static_research,
	"LabelParts": [["LogicCircuit", "machines"]],
	"RequiredResearches": ["Circuit" + static_research],
	"Unlocks": [["Hand" + base_recipe, "SteelLogicCircuit"],["Constructor" + base_recipe, "SteelLogicCircuit"],
	["Hand" + base_recipe, "SteelLogicController"],["Constructor" + base_recipe, "SteelLogicController"],
	["Hand" + base_recipe, "SteelLogicInterface"],["Constructor" + base_recipe, "SteelLogicInterface"],
	["Hand" + base_recipe, "SteelLogicDisplay"],["Constructor" + base_recipe, "SteelLogicDisplay"],
	["Hand" + base_recipe, "SteelLogicWire"],["Constructor" + base_recipe, "SteelLogicWire"]],
	"Levels": [1,1],
	"CostMul":0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedCircuit" + static_research,
	"LabelParts": [["AdvancedCircuit", "parts"]],
	"RequiredResearches": ["Circuit" + static_research],
	"Levels": [2,2],
	"Unlocks": [["Hand" + base_recipe, "AdvancedCircuit"],["Assembler" + base_recipe, "AdvancedCircuit"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GoldWire" + static_research,
	"LabelParts": [["GoldWire", "parts"]],
	"RequiredResearches": ["AdvancedCircuit" + static_research, "OreWasher" + static_research],
	"Levels": [2,2],
	"Unlocks": [["Hand" + base_recipe, "GoldWire"],["Assembler" + base_recipe, "GoldWire"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedCircuitBoard" + static_research,
	"LabelParts": [["AdvancedCircuitBoard", "parts"]],
	"RequiredResearches": ["GoldWire" + static_research, "PyrolysisUnit" + static_research],
	"Levels": [2,2],
	"Unlocks": [["Hand" + base_recipe, "AdvancedCircuitBoard"],["Assembler" + base_recipe, "AdvancedCircuitBoard"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SiliconWafer" + static_research,
	"LabelParts": [["SiliconWafer", "parts"]],
	"RequiredResearches": ["Assembler" + static_research],
	"Unlocks": [["Assembler" + base_recipe, "SiliconWafer"]],
	"Levels": [3,3],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Processor" + static_research,
	"LabelParts": [["Processor", "parts"]],
	"RequiredResearches": ["SiliconWafer" + static_research, "AdvancedCircuit" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Processor"],["Assembler" + base_recipe, "Processor"],["Assembler" + base_recipe, "Processor2"]],
	"Levels": [3,3],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumCore" + static_research,
	"LabelParts": [["QuantumCore", "parts"]],
	"RequiredResearches": ["Processor" + static_research],
	"Levels": [4,4],
	"Unlocks": [["Hand" + base_recipe, "QuantumCore"],["Assembler" + base_recipe, "QuantumCore"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumCircuit" + static_research,
	"LabelParts": [["QuantumCircuit", "parts"]],
	"RequiredResearches": ["QuantumCore" + static_research],
	"Levels": [4,4],
	"Unlocks": [["Hand" + base_recipe, "QuantumCircuit"],["Assembler" + base_recipe, "QuantumCircuit"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumProcessor" + static_research,
	"LabelParts": [["QuantumProcessor", "parts"]],
	"RequiredResearches": ["QuantumCircuit" + static_research],
	"Levels": [5,5],
	"Unlocks": [["Hand" + base_recipe, "QuantumProcessor"],["Assembler" + base_recipe, "QuantumProcessor"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumBrain" + static_research,
	"LabelParts": [["QuantumBrain", "parts"]],
	"RequiredResearches": ["QuantumProcessor" + static_research],
	"Levels": [6,6],
	"Unlocks": [["Hand" + base_recipe, "QuantumBrain"],["Assembler" + base_recipe, "QuantumBrain"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumComputer" + static_research,
	"LabelParts": [["QuantumComputer", "machines"]],
	"RequiredResearches": ["QuantumCircuit" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%QuantumComputer"],["Constructor" + base_recipe, "%Material%QuantumComputer"]],
	"Levels": [5,7],
	"CostSub": 1,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "MetalConstructions" + static_research,
	"LabelParts": [["MetalConstructions", "researches"]],
	"RequiredResearches": ["Metalwork" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Corner"],["Constructor" + base_recipe, "%Material%Corner"],
	["Hand" + base_recipe, "%Material%Casing"],["Constructor" + base_recipe,"%Material%Casing"],
	["Hand" + base_recipe, "%Material%Beam"],["Constructor" + base_recipe, "%Material%Beam"]],
	"Levels": [1,7],
	"Chapter":"Decorations"+static_chapter,
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Scaffold" + static_research,
	"LabelParts": [["Scaffold", "researches"]],
	"RequiredResearches": ["MetalConstructions" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Scaffold"],["Constructor" + base_recipe, "%Material%Scaffold"]],
	"Levels": [1,7],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Chemistry" + static_research,
	"LabelParts": [["Chemistry", "researches"]],
	"RequiredResearches": ["ElectricEngine" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%ChemReactor"],["Constructor" + base_recipe, "%Material%ChemReactor"]],
	"Levels": [2,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Catalyst" + static_research,
	"LabelParts": [["Catalyst", "parts"]],
	"RequiredResearches": ["Chemistry" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Catalyst"],["Assembler" + base_recipe, "Catalyst"]],
	"Levels": [2,2],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialChemReactor" + static_research,
	"LabelParts": [["IndustrialChemReactor", "machines"]],
	"RequiredResearches": ["Catalyst" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialChemReactor"],["Constructor" + base_recipe, "%Material%IndustrialChemReactor"]],
	"Levels": [3,7],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FuelChemistry" + static_research,
	"LabelParts": [["FuelChemistry", "researches"]],
	"RequiredResearches": ["IndustrialChemReactor" + static_research],
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "Superfuel"], ["IndustrialChemReactor" + base_recipe, "RocketFuel"]],
	"Levels": [3,3],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FuelChemistry2" + static_research,
	"LabelParts": [["FuelChemistry2", "researches"]],
	"RequiredResearches": ["FuelChemistry" + static_research],
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "RocketFuel2"], ["IndustrialChemReactor" + base_recipe, "Superfuel2"]],
	"Levels": [3,3],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sifter" + static_research,
	"LabelParts": [["Sifter", "machines"]],
	"RequiredResearches": ["Chemistry" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Sifter"],["Constructor" + base_recipe, "%Material%Sifter"]],
	"Levels": [3,7],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Separator" + static_research,
	"LabelParts": [["Separator", "machines"]],
	"RequiredResearches": ["ElectricEngine" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Separator"],["Constructor" + base_recipe, "%Material%Separator"]],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricEngine" + static_research,
	"LabelParts": [["ElectricEngine", "machines"]],
	"RequiredResearches": ["Electrolysis" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ElectricEngine"],["Constructor" + base_recipe, "%Material%ElectricEngine"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BiElectricEngine" + static_research,
	"LabelParts": [["BiElectricEngine", "machines"]],
	"RequiredResearches": ["ElectricEngine" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BiElectricEngine"],["Constructor" + base_recipe, "%Material%BiElectricEngine"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OreWasher" + static_research,
	"LabelParts": [["OreWasher", "machines"]],
	"Levels": [2,7],
	"RequiredResearches": ["Separator" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%OreWasher"],["Constructor" + base_recipe, "%Material%OreWasher"]],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Mixer" + static_research,
	"LabelParts": [["Mixer", "machines"]],
	"RequiredResearches": ["OreWasher" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Mixer"],["Constructor" + base_recipe, "%Material%Mixer"]],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ChemicalBath" + static_research,
	"LabelParts": [["ChemicalBath", "machines"]],
	"RequiredResearches": ["IndustrialChemReactor" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ChemicalBath"],["Constructor" + base_recipe, "%Material%ChemicalBath"]],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OilCrackingTower" + static_research,
	"LabelParts": [["OilCrackingTower", "machines"]],
	"RequiredResearches": ["FuelChemistry" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%OilCrackingTower"],["Constructor" + base_recipe, "%Material%OilCrackingTower"]],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CombustionEngine" + static_research,
	"LabelParts": [["CombustionEngine", "machines"]],
	"RequiredResearches": ["IndustrialChemReactor" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CombustionEngine"],["Constructor" + base_recipe, "%Material%CombustionEngine"]],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "StainlessSteelProduction" + static_research,
	"LabelParts": [["StainlessSteelProduction", "researches"]],
	"RequiredResearches": ["Chemistry" + static_research, "AluminiumProduction" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[4]),
	"AlsoUnlocks": [["Hand" + base_recipe, "Cell"]],
	"Levels": [4,4],
	"CostLevelOffset": -1,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSeparation" + static_research,
	"LabelParts": [["AdvancedSeparation", "researches"]],
	"RequiredResearches": ["AluminiumProduction" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSeparator"],["Constructor" + base_recipe, "%Material%IndustrialSeparator"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SmallBattery" + static_research,
	"LabelParts": [["SmallBattery", "machines"]],
	"RequiredResearches": ["AdvancedSeparation" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%SmallBattery"],["Constructor" + base_recipe, "%Material%SmallBattery"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BatteryBox" + static_research,
	"LabelParts": [["BatteryBox", "machines"]],
	"RequiredResearches": ["SmallBattery" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BatteryBox"],["Constructor" + base_recipe, "%Material%BatteryBox"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "TitaniumProduction" + static_research,
	"LabelParts": [["TitaniumProduction", "researches"]],
	"RequiredResearches": ["IndustrialSmelting" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[5]),
	"Levels": [4,4],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialBoiler" + static_research,
	"LabelParts": [["IndustrialBoiler", "machines"]],
	"RequiredResearches": ["TitaniumProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialBoiler"],["Connector" + base_recipe, "%Material%IndustrialBoiler"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialSteamTurbine" + static_research,
	"LabelParts": [["IndustrialSteamTurbine", "machines"]],
	"RequiredResearches": ["IndustrialBoiler" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSteamTurbine"],["Connector" + base_recipe, "%Material%IndustrialSteamTurbine"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialGenerator" + static_research,
	"LabelParts": [["IndustrialGenerator", "machines"]],
	"RequiredResearches": ["IndustrialSteamTurbine" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialGenerator"],["Connector" + base_recipe, "%Material%IndustrialGenerator"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Freezer" + static_research,
	"LabelParts": [["Freezer", "machines"]],
	"RequiredResearches": ["TitaniumProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Freezer"],["Constructor" + base_recipe, "%Material%Freezer"]],
	"Levels": [5,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HardMetalProduction" + static_research,
	"LabelParts": [["HardMetalProduction", "researches"]],
	"RequiredResearches": ["Freezer" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[6]),
	"Levels": [5,5],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FusionReactor" + static_research,
	"LabelParts": [["FusionReactor", "machines"]],
	"RequiredResearches": ["HardMetalProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%FusionReactor"],["Constructor" + base_recipe, "%Material%FusionReactor"]],
	"Levels": [6,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "NeutroniumProduction" + static_research,
	"LabelParts": [["NeutroniumProduction", "researches"]],
	"RequiredResearches": ["FusionReactor" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[7]),
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "UltimateCatalyst" + static_research,
	"LabelParts": [["UltimateCatalyst", "parts"]],
	"RequiredResearches": ["NeutroniumProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "UltimateCatalyst"],["Assembler" + base_recipe, "UltimateCatalyst"]],
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	 "Class": "StaticResearch",
	 "Name": "Portal" + static_research,
	 "LabelParts": [["Portal", "machines"]],
	 "RequiredResearches": ["UltimateCatalyst" + static_research],
	 "Unlocks": [["Hand" + base_recipe, "%Material%Portal"],["Constructor" + base_recipe, "%Material%Portal"]],
	 "Levels": [7,7],
	 "MainResearch": True,
 })
append_levels({
	"Class": "StaticResearch",
	"Name": "FissionReactor" + static_research,
	"LabelParts": [["FissionReactor", "machines"]],
	"RequiredResearches": ["UraniumCell" + static_research],
	"Levels": [5,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%FissionReactor"],["Constructor" + base_recipe, "%Material%FissionReactor"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "UraniumCell" + static_research,
	"LabelParts": [["UraniumCell", "parts"]],
	"RequiredResearches": ["TitaniumProduction" + static_research],
	"Levels": [5,5],
	"Unlocks": [["Hand" + base_recipe, "UraniumCell"],["Assembler" + base_recipe, "UraniumCell"]],
})
append_nuclear([7,-7], append_levels, researches)
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialSmelting" + static_research,
	"LabelParts": [["IndustrialSmelting", "researches"]],
	"RequiredResearches": ["StainlessSteelProduction" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSmelter"],["Constructor" + base_recipe, "%Material%IndustrialSmelter"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fermentation" + static_research,
	"LabelParts": [["Fermentation", "researches"]],
	"Levels": [3,7],
	"RequiredResearches": ["Chemistry" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Fermenter"],["Constructor" + base_recipe, "%Material%Fermenter"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "InductionCoil" + static_research,
	"LabelParts": [["InductionCoil", "machines"]],
	"RequiredResearches": ["IndustrialSmelting" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%InductionCoil"],["Constructor" + base_recipe, "%Material%InductionCoil"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialElectricEngine" + static_research,
	"LabelParts": [["IndustrialElectricEngine", "machines"]],
	"RequiredResearches": ["InductionCoil" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialElectricEngine"],["Constructor" + base_recipe, "%Material%IndustrialElectricEngine"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Terminal" + static_research,
	"LabelParts": [["Terminal", "machines"]],
	"Levels": [4,4],
	"RequiredResearches": ["StainlessSteelProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[4] + "Terminal"],["Constructor" + base_recipe, tier_material[4] + "Terminal"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FlatTerminal" + static_research,
	"LabelParts": [["FlatTerminal", "machines"]],
	"Levels": [4,4],
	"RequiredResearches": ["Terminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[4] + "FlatTerminal"],["Constructor" + base_recipe, tier_material[4] + "FlatTerminal"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Constructor" + static_research,
	"LabelParts": [["Constructor", "machines"]],
	"RequiredResearches": ["Assembler" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Constructor"],["Constructor" + base_recipe, "%Material%Constructor"]],
	"Levels": [2, 7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Assembler" + static_research,
	"LabelParts": [["Assembler", "machines"]],
	"RequiredResearches": ["Automatization" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Assembler"],["Constructor" + base_recipe, "%Material%Assembler"]],
	"Levels": [1,7],
	"CostMul":0.5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Deconstructor" + static_research,
	"LabelParts": [["Deconstructor", "machines"]],
	"RequiredResearches": ["Constructor" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Deconstructor"],["Constructor" + base_recipe, "%Material%Deconstructor"]],
	"Levels": [2,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BigTerminal" + static_research,
	"LabelParts": [["BigTerminal", "machines"]],
	"RequiredResearches": ["Terminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[5] + "BigTerminal"],["Constructor" + base_recipe, tier_material[5] + "BigTerminal"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BigFlatTerminal" + static_research,
	"LabelParts": [["BigFlatTerminal", "machines"]],
	"RequiredResearches": ["BigTerminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[5] + "BigFlatTerminal"],["Constructor" + base_recipe, tier_material[5] + "BigFlatTerminal"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HugeTerminal" + static_research,
	"LabelParts": [["HugeTerminal", "machines"]],
	"RequiredResearches": ["BigTerminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[6] + "HugeTerminal"],["Constructor" + base_recipe, tier_material[6] + "HugeTerminal"]],
	"Levels": [5,5],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HugeFlatTerminal" + static_research,
	"LabelParts": [["HugeFlatTerminal", "machines"]],
	"RequiredResearches": ["HugeTerminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[6] + "HugeFlatTerminal"],["Constructor" + base_recipe, tier_material[6] + "HugeFlatTerminal"]],
	"Levels": [5,5],
}) 
append_levels({
	"Class": "StaticResearch",
	"Name": "PyrolysisUnit" + static_research,
	"LabelParts": [["PyrolysisUnit", "machines"]],
	"RequiredResearches": ["Mixer" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%PyrolysisUnit"],["Constructor" + base_recipe, "%Material%PyrolysisUnit"]],
	"Levels": [3,7],
})
	
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood" + static_research,
	"RequiredResearches": ["Cutting" + static_research],
	"LabelParts": [["DecorativeWood", "researches"]],
	"Unlocks": [["Hand" + base_recipe, "WoodenPlanks"],["Hand" + base_recipe, "WoodenStairs"],["Hand" + base_recipe, "Bed"],["Hand" + base_recipe, "Door"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood2" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[1], "common"]],
	"RequiredResearches": ["DecorativeWood" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Chair"],["Hand" + base_recipe, "Fence"],["Hand" + base_recipe, "Ladder"],["Hand" + base_recipe, "Rack"],["Hand" + base_recipe, "Table"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fence" + static_research,
	"LabelParts": [["Fence", "misc"]],
	"RequiredResearches": ["DecorativeWood2" + static_research],
	"Unlocks": [["Hand" + base_recipe, "SteelFence"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fence1" + static_research,
	"LabelParts": [["Fence", "misc"], [level_labels[1], "common"]],
	"RequiredResearches": ["Fence" + static_research],
	"Unlocks": [["Hand" + base_recipe, "StainlessSteelFence"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood4" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[3], "common"]],
	"RequiredResearches": ["DecorativeWood2" + static_research],
	"Unlocks": [["Hand" + base_recipe, "CopperChair"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood3" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[2], "common"]],
	"RequiredResearches": ["DecorativeWood2" + static_research, "AdvancedSmelting" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Window"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativePlastic" + static_research,
	"LabelParts": [["DecorativePlastic", "researches"]],
	"RequiredResearches": ["Chemistry" + static_research, "PyrolysisUnit" + static_research, "DecorativeWood3" + static_research],
	"Unlocks": [["Hand" + base_recipe, "PlasticWindow"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PlasticBlock" + static_research,
	"LabelParts": [["PlasticBlock", "misc"]],
	"RequiredResearches": ["DecorativePlastic" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "PlasticBlock"],["Press" + base_recipe, "PlasticBlock"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BasicPlatform" + static_research,
	"LabelParts": [["BasicPlatform", "misc"]],
	"CompleteByDefault": True,
	"Unlocks": [["Hand" + base_recipe, "BasicPlatform"], ["Press" + base_recipe, "BasicPlatform"]],
	"RequiredResearches": []
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone" + static_research,
	"LabelParts": [["DecorativeStone", "researches"]],
	"RequiredResearches": ["Press"+static_research], 
	"Unlocks": [["Hand" + base_recipe, "StoneTiles"], ["CuttingMachine" + base_recipe, "StoneTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone2" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[1], "common"]],
	"RequiredResearches": ["DecorativeStone" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "DarkTiles"],["Hand" + base_recipe, "RedTiles"],["CuttingMachine" + base_recipe, "DarkTiles"],["CuttingMachine" + base_recipe, "RedTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GlassBlock" + static_research,
	"LabelParts": [["GlassBlock", "misc"]],
	"RequiredResearches": ["Press"+static_research], 
	"Unlocks": [["Hand" + base_recipe, "GlassBlock"],["Press" + base_recipe, "GlassBlock"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone3" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[2], "common"]],

	"RequiredResearches": ["DecorativeStone2" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "DarkBricks"],["Hand" + base_recipe, "RedBricks"],["Hand" + base_recipe, "Bricks"],["CuttingMachine" + base_recipe, "DarkBricks"],["CuttingMachine" + base_recipe, "RedBricks"],["CuttingMachine" + base_recipe, "Bricks"]],
	
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone4" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[3], "common"]],
	"RequiredResearches": ["DecorativeStone3" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "Stairs"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeConcrete" + static_research,
	"LabelParts": [["DecorativeConcrete", "researches"]],
	"RequiredResearches": ["Mixer" + static_research], 
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
		"Name": "DecorativeConcrete" + item + static_research,
		"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[index], "common"]],
		"RequiredResearches": ["DecorativeConcrete" + static_research], 
		"Unlocks": [[crafter + base_recipe, item], [crafter2 + base_recipe, item]],
		"Levels": [3, 3],
	})
     
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"]],
	"RequiredResearches": ["DecorativeConcrete" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteTiles"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete2" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[1], "common"]],

	"RequiredResearches": ["DecorativeReinforcedConcrete" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteSmallTiles"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteSmallTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete3" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[2], "common"]],
	"RequiredResearches": ["DecorativeReinforcedConcrete2" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteBricks"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteBricks"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorationClay" + static_research,
	"LabelParts": [["DecorationClay", "researches"]],
	"RequiredResearches": ["Drying" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "TerracottaTiles"], ["CuttingMachine" + base_recipe, "TerracottaTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorationClay2" + static_research,
	"LabelParts": [["DecorationClay", "researches"], [level_labels[1], "common"]],
	"RequiredResearches": ["DecorationClay" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "TerracottaBricks"], ["CuttingMachine" + base_recipe, "TerracottaBricks"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Press" + static_research,
	"LabelParts": [["Press", "machines"]],
	"RequiredResearches": [],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Press"],["Constructor" + base_recipe, "%Material%Press"]],
})
append_levels({
	"Class": "StaticResearchToolUnlock",
	"Name": "PaintTool" + static_research,
	"LabelParts": [["PaintTool", "parts"]],
	"RequiredResearches": ["Press" + static_research],
	"Levels": [1,1],
	"Unlocks": [],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Lamp" + static_research,
	"LabelParts": [["Lamp", "machines"]],
	"RequiredResearches": [],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Lamp"],["Constructor" + base_recipe, "%Material%Lamp"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Column" + static_research,
	"LabelParts": [["Column", "misc"]],
	"RequiredResearches": ["DecorativeStone" + static_research],
	"Levels": [1,1],
	"Unlocks": [["Hand" + base_recipe, "Column"],["Hand" + base_recipe, "FluetedColumn"],["Press" + base_recipe, "Column"],["Press" + base_recipe, "FluetedColumn"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sign" + static_research,
	"LabelParts": [["Sign", "machines"]],
	"RequiredResearches": ["Press" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Sign"],["Constructor" + base_recipe, "%Material%Sign"]],
	"Levels": [0,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSign" + static_research,
	"LabelParts": [["AdvancedSign", "machines"]],
	"RequiredResearches": ["Sign" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%AdvancedSign"],["Constructor" + base_recipe, "%Material%AdvancedSign"]],
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

write_file("Generated/Researches/basic.json", data)
write_file("Loc/source/researches.json", csv)
