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

        for i in range(
            research["Levels"][0] if "Levels" in research else 0,
            research["Levels"][1] + 1 if "Levels" in research else 1,
        ):
            new = []
            for j in unl:
                new.append([j[0], j[1].replace("%Material%", tier_material[i])])

            research["Unlocks"].append(new)

    CostSub = research["CostSub"] if "CostSub" in research else 0
    CostMul = research["CostMul"] if "CostMul" in research else 1

    offset = research["CostLevelOffset"] if "CostLevelOffset" in research else 0

    research["DataPoints"] = []
    for i in range(
        research["Levels"][0] if "Levels" in research else 0,
        research["Levels"][1] + 1 if "Levels" in research else 1,
    ):
        research["DataPoints"].append(
            {"Items": res_cost(i - CostSub + offset, CostMul)}
        )

    researches.append(research)


append_levels(
    {
        "class": static_research,
        "name": "InitialScan",
        "label_parts": [["InitialScan", "researches"]],
        "CompleteByDefault": True,
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "MineralsScan",
        "label_parts": [["MineralsScan", "researches"]],
        "RequiredResearches": ["InitialScan"],
        "Unlocks": [
            ["Hand", tier_material[0] + "Furnace"],
            ["Constructor", tier_material[0] + "Furnace"],
            ["Hand", "SandSurface"],
            ["Hand", "GravelSurface"],
        ],
        "Collect": {"Items": [{"name": "Dirt", "Count": 10}]},
        "Position": [0, 1],
        "Chapter": "Production",
        "CompleteByDefault": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdditionalStorage",
        "label_parts": [["AdditionalStorage", "researches"]],
        "RequiredResearches": ["MineralsScan"],
        "Unlocks": [["Hand", "%Material%Chest"], ["Constructor", "%Material%Chest"]],
        "Position": [-1, 1],
        "Levels": [0, 7],
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "SingleTypeStorage",
        "label_parts": [["SingleTypeStorage", "researches"]],
        "RequiredResearches": ["AdditionalStorage"],
        "Position": [-2, 1],
        "Levels": [1, 7],
        "Chapter": "Production",
        "Unlocks": [
            ["Hand", "%Material%ItemRack"],
            ["Constructor", "%Material%ItemRack"],
        ],
    }
)
append_levels(
    {
        "class": "StaticResearchBonusInventory",
        "name": "InventoryUpgrade",
        "label_parts": [["InventoryUpgrade", "researches"]],
        "Chapter": "Production",
        "RequiredResearches": ["AdditionalStorage"],
        "Unlocks": [],
        "Position": [-2, 2],
        "Levels": [0, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Electricity",
        "label_parts": [["Electricity", "researches"]],
        "RequiredResearches": ["InitialScan"],
        "Unlocks": [
            ["Hand", tier_material[1] + "Connector"],
            ["Constructor", tier_material[1] + "Connector"],
        ],
        "Collect": {"Items": [{"name": "Sand", "Count": 10}]},
        "Position": [0, -1],
        "Chapter": "Production",
        "CompleteByDefault": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "ElectricFurnace",
        "label_parts": [["ElectricFurnace", "machines"]],
        "Levels": [2, 7],
        "RequiredResearches": ["Electricity"],
        "Position": [-1, -2],
        "Chapter": "Production",
        "Unlocks": [
            ["Hand", "%Material%ElectricFurnace"],
            ["Constructor", "%Material%ElectricFurnace"],
        ],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "ElectricalSwitch",
        "label_parts": [["ElectricalSwitch", "machines"]],
        "RequiredResearches": ["Electricity"],
        "Unlocks": [
            ["Hand", tier_material[2] + "ElectricalSwitch"],
            ["Constructor", tier_material[2] + "ElectricalSwitch"],
        ],
        "Position": [0, -2],
        "Levels": [2, 2],
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Diode",
        "label_parts": [["Diode", "machines"]],
        "Position": [0, -3],
        "RequiredResearches": ["Electricity"],
        "Levels": [2, 7],
        "Chapter": "Production",
        "Unlocks": [["Hand", "%Material%Diode"], ["Constructor", "%Material%Diode"]],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "PowerGeneration",
        "label_parts": [["PowerGeneration", "researches"]],
        "RequiredResearches": ["Electricity"],
        "Levels": [1, 1],
        "Unlocks": [
            ["Hand", "%Material%CompactGenerator"],
            ["Constructor", "%Material%CompactGenerator"],
        ],
        "Chapter": "Production",
        "Position": [1, -1],
        "CompleteByDefault": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Electrolysis",
        "label_parts": [["Electrolysis", "researches"]],
        "RequiredResearches": ["SteelProduction"],
        "Levels": [2, 7],
        "Unlocks": [
            ["Hand", "%Material%Electrolyzer"],
            ["Constructor", "%Material%Electrolyzer"],
        ],
        "Chapter": "Production",
        "Position": [4, -1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "SteelProduction",
        "label_parts": [["SteelProduction", "researches"]],
        "RequiredResearches": ["Drying"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%BlastFurnace"],
            ["Constructor", "%Material%BlastFurnace"],
        ],
        "AlsoUnlocks": [
            ["Hand", "SteelParts"],
            ["Hand", "SteelPlate"],
            ["Hand", "SteelPipe"],
        ],
        "Chapter": "Production",
        "Position": [3, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdvancedSmelting",
        "label_parts": [["AdvancedSmelting", "researches"]],
        "RequiredResearches": ["SteelProduction"],
        "Position": [4, 0],
        "Levels": [2, 7],
        "Unlocks": [
            ["Hand", "%Material%ArcSmelter"],
            ["Constructor", "%Material%ArcSmelter"],
        ],
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "SolarPanel",
        "label_parts": [["SolarPanel", "machines"]],
        "Position": [5, 0],
        "RequiredResearches": ["AluminiumProduction"],
        "Levels": [3, 7],
        "Unlocks": [
            ["Hand", "%Material%SolarPanel"],
            ["Constructor", "%Material%SolarPanel"],
        ],
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AluminiumProduction",
        "label_parts": [["AluminiumProduction", "researches"]],
        "RequiredResearches": ["AdvancedSmelting", "Electrolysis"],
        "Unlocks": [
            ["Hand", tier_material[3] + "Parts"],
            ["Hand", tier_material[3] + "Plate"],
            ["Hand", tier_material[3] + "Pipe"],
            ["Constructor", tier_material[3] + "Pipe"],
        ],
        "Chapter": "Production",
        "Position": [5, -1],
        "Levels": [3, 3],
        "CostLevelOffset": -1,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "MassivePowerGeneration",
        "label_parts": [["MassivePowerGeneration", "researches"]],
        "RequiredResearches": ["PowerGeneration"],
        "Unlocks": [
            ["Hand", "%Material%Generator"],
            ["Constructor", "%Material%Generator"],
            ["Hand", "%Material%Boiler"],
            ["Constructor", "%Material%Boiler"],
            ["Hand", "%Material%SteamTurbine"],
            ["Constructor", "%Material%SteamTurbine"],
        ],
        "Levels": [2, 7],
        "Chapter": "Production",
        "Position": [1, -2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "GasTurbine",
        "label_parts": [["GasTurbine", "machines"]],
        "Position": [1, -3],
        "RequiredResearches": ["MassivePowerGeneration"],
        "Levels": [4, 7],
        "Chapter": "Production",
        "Unlocks": [
            ["Hand", "%Material%GasTurbine"],
            ["Constructor", "%Material%GasTurbine"],
        ],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Smelting",
        "label_parts": [["Smelting", "researches"]],
        "RequiredResearches": ["MineralsScan"],
        "Unlocks": [
            ["Hand", "%Material%Smelter"],
            ["Constructor", "%Material%Smelter"],
        ],
        "Levels": [0, 2],
        "Position": [0, 2],
        "Chapter": "Production",
        "CompleteByDefault": True,
    }
)
append_equipment([-1, 3], append_levels, researches)
append_levels(
    {
        "class": static_research,
        "name": "Metalwork",
        "label_parts": [["Metalwork", "researches"]],
        "RequiredResearches": ["Smelting"],
        "Unlocks": [
            ["Hand", "CopperParts"],
            ["Hand", "CopperPlate"],
            ["Hand", "CopperPipe"],
        ],
        "Collect": {"Items": [{"name": "CopperOre", "Count": 10}]},
        "Position": [1, 2],
        "Levels": [1, 1],
        "Chapter": "Production",
        "CompleteByDefault": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Valve",
        "label_parts": [["Vent", "machines"]],
        "RequiredResearches": ["Metalwork"],
        "Unlocks": [
            ["Hand", tier_material[1] + "Vent"],
            ["Constructor", tier_material[1] + "Vent"],
        ],
        "Position": [0, 3],
        "Levels": [1, 1],
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "BasicMachines",
        "label_parts": [["BasicMachines", "researches"]],
        "RequiredResearches": ["Metalwork"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%Macerator"],
            ["Constructor", "%Material%Macerator"],
            ["Hand", "%Material%AutomaticHammer"],
            ["Constructor", "%Material%AutomaticHammer"],
        ],
        "Chapter": "Production",
        "Position": [1, 3],
        "CostMul": 0.25,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Flywheel",
        "label_parts": [["Flywheel", "machines"]],
        "RequiredResearches": ["BasicMachines"],
        "Unlocks": [
            ["Hand", tier_material[2] + "Flywheel"],
            ["Constructor", tier_material[2] + "Flywheel"],
        ],
        "Levels": [2, 2],
        "Chapter": "Production",
        "Position": [0, 4],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Cutting",
        "label_parts": [["Cutting", "researches"]],
        "RequiredResearches": ["BasicMachines"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%CuttingMachine"],
            ["Constructor", "%Material%CuttingMachine"],
        ],
        "Chapter": "Production",
        "Position": [2, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "SolidDump",
        "label_parts": [["SolidDump", "machines"]],
        "Position": [4, 1],
        "Levels": [2, 2],
        "Chapter": "Production",
        "RequiredResearches": ["Furnace"],
        "Unlocks": [
            ["Hand", tier_material[2] + "SolidDump"],
            ["Constructor", tier_material[2] + "SolidDump"],
        ],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Pump",
        "label_parts": [["Pump", "machines"]],
        "RequiredResearches": ["Automatization"],
        "Levels": [1, 7],
        "Unlocks": [["Hand", "%Material%Pump"], ["Constructor", "%Material%Pump"]],
        "Chapter": "Production",
        "Position": [3, 2],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Container",
        "label_parts": [["Container", "machines"]],
        "RequiredResearches": ["Pump"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%Container"],
            ["Constructor", "%Material%Container"],
        ],
        "Chapter": "Production",
        "Position": [4, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FluidFurnace",
        "label_parts": [["FluidFurnace", "machines"]],
        "RequiredResearches": ["Furnace"],
        "Unlocks": [
            ["Hand", "%Material%FluidFurnace"],
            ["Constructor", "%Material%FluidFurnace"],
        ],
        "Levels": [1, 7],
        "Chapter": "Production",
        "Position": [3, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FluidDumping",
        "label_parts": [["FluidDumping", "researches"]],
        "RequiredResearches": ["Container"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%FluidDump"],
            ["Constructor", "%Material%FluidDump"],
        ],
        "Chapter": "Production",
        "Position": [5, 2],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "GasDump",
        "label_parts": [["GasDump", "machines"]],
        "Position": [5, 1],
        "Levels": [2, 2],
        "Chapter": "Production",
        "RequiredResearches": ["Container"],
        "Unlocks": [
            ["Hand", tier_material[2] + "GasDump"],
            ["Constructor", tier_material[2] + "GasDump"],
        ],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Automatization",
        "label_parts": [["Automatization", "researches"]],
        "RequiredResearches": ["BasicMachines"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%RobotArm"],
            ["Constructor", "%Material%RobotArm"],
            ["Hand", "%Material%Conveyor"],
            ["Constructor", "%Material%Conveyor"],
            ["Hand", "%Material%Splitter"],
            ["Constructor", "%Material%Splitter"],
        ],
        "Chapter": "Production",
        "Position": [2, 3],
        "CostMul": 0.25,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Filtering",
        "label_parts": [["Filtering", "researches"]],
        "RequiredResearches": ["Automatization"],
        "Unlocks": [
            ["Hand", "%Material%FilteringRobotArm"],
            ["Constructor", "%Material%FilteringRobotArm"],
            ["Hand", "%Material%Sorter"],
            ["Constructor", "%Material%Sorter"],
        ],
        "Levels": [1, 7],
        "Chapter": "Production",
        "Position": [3, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FilteringPump",
        "label_parts": [["FilteringPump", "machines"]],
        "RequiredResearches": ["Pump"],
        "Unlocks": [
            ["Hand", "%Material%FilteringPump"],
            ["Constructor", "%Material%FilteringPump"],
        ],
        "Levels": [1, 7],
        "Chapter": "Production",
        "Position": [4, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AutomaticMining",
        "label_parts": [["AutomaticMining", "researches"]],
        "RequiredResearches": ["Automatization"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%DrillingRig"],
            ["Constructor", "%Material%DrillingRig"],
        ],
        "Position": [2, 4],
        "Chapter": "Production",
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Pumpjack",
        "label_parts": [["Pumpjack", "machines"]],
        "Position": [2, 5],
        "RequiredResearches": ["AutomaticMining"],
        "Unlocks": [
            ["Hand", "%Material%Pumpjack"],
            ["Constructor", "%Material%Pumpjack"],
        ],
        "Levels": [3, 7],
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AutomaticFarm",
        "label_parts": [["AutomaticFarm", "machines"]],
        "RequiredResearches": ["Automatization"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%AutomaticFarm"],
            ["Constructor", "%Material%AutomaticFarm"],
        ],
        "Chapter": "Production",
        "Position": [3, 4],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "HeatTransferring",
        "label_parts": [["HeatTransferring", "researches"]],
        "RequiredResearches": ["InitialScan"],
        "Unlocks": [
            ["Hand", "%Material%HeatPipe"],
            ["Constructor", "%Material%HeatPipe"],
        ],
        "Position": [-1, -1],
        "Levels": [1, 1],
        "Chapter": "Production",
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Radiator",
        "label_parts": [["Radiator", "machines"]],
        "RequiredResearches": ["HeatTransferring"],
        "Levels": [3, 7],
        "Unlocks": [
            ["Hand", "%Material%Radiator"],
            ["Constructor", "%Material%Radiator"],
        ],
        "Position": [-2, -1],
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AtmosphericCondenser",
        "label_parts": [["AtmosphericCondenser", "machines"]],
        "RequiredResearches": ["InitialScan"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%AtmosphericCondenser"],
            ["Constructor", "%Material%AtmosphericCondenser"],
        ],
        "Chapter": "Production",
        "Position": [-2, 0],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "StirlingEngine",
        "label_parts": [["StirlingEngine", "machines"]],
        "RequiredResearches": ["MineralsScan"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%StirlingEngine"],
            ["Constructor", "%Material%StirlingEngine"],
        ],
        "Chapter": "Production",
        "Position": [1, 1],
        "CompleteByDefault": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Furnace",
        "label_parts": [["Furnace", "machines"]],
        "RequiredResearches": ["StirlingEngine"],
        "Levels": [1, 7],
        "Unlocks": [
            ["Hand", "%Material%Furnace"],
            ["Constructor", "%Material%Furnace"],
        ],
        "Chapter": "Production",
        "Position": [2, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Drying",
        "label_parts": [["Drying", "researches"]],
        "RequiredResearches": [
            "Furnace",
        ],
        "Levels": [1, 7],
        "Unlocks": [["Hand", "%Material%Oven"], ["Constructor", "%Material%Oven"]],
        "Position": [2, 0],
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DistributedComputing",
        "label_parts": [["DistributedComputing", "researches"]],
        "RequiredResearches": ["PowerGeneration"],
        "Unlocks": [
            ["Hand", "%Material%Computer"],
            ["Constructor", "%Material%Computer"],
        ],
        "Levels": [1, 7],
        "Chapter": "Production",
        "Position": [2, -1],
        "CompleteByDefault": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "CopperWire",
        "label_parts": [["CopperWire", "parts"]],
        "RequiredResearches": ["DistributedComputing"],
        "Levels": [1, 1],
        "Unlocks": [["Hand", "CopperWire"], ["Assembler", "CopperWire"]],
        "Chapter": "Production",
        "Position": [2, -2],
        "CompleteByDefault": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "CircuitBoard",
        "label_parts": [["CircuitBoard", "parts"]],
        "RequiredResearches": ["CopperWire"],
        "Levels": [1, 1],
        "Unlocks": [["Hand", "CircuitBoard"]],
        "Chapter": "Production",
        "Position": [2, -3],
        "CostMul": 0.25,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Circuit",
        "label_parts": [["Circuit", "parts"]],
        "RequiredResearches": ["CircuitBoard"],
        "Unlocks": [["Hand", "Circuit"], ["Assembler", "Circuit"]],
        "Levels": [1, 1],
        "Chapter": "Production",
        "Position": [2, -4],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "LogicCircuit",
        "label_parts": [["LogicCircuit", "machines"]],
        "RequiredResearches": ["Circuit"],
        "Unlocks": [
            ["Hand", "SteelLogicCircuit"],
            ["Constructor", "SteelLogicCircuit"],
            ["Hand", "SteelLogicController"],
            ["Constructor", "SteelLogicController"],
            ["Hand", "SteelLogicInterface"],
            ["Constructor", "SteelLogicInterface"],
            ["Hand", "SteelLogicDisplay"],
            ["Constructor", "SteelLogicDisplay"],
            ["Hand", "SteelLogicWire"],
            ["Constructor", "SteelLogicWire"],
        ],
        "Levels": [1, 1],
        "Chapter": "Production",
        "Position": [3, -3],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdvancedCircuit",
        "label_parts": [["AdvancedCircuit", "parts"]],
        "RequiredResearches": ["Circuit"],
        "Levels": [2, 2],
        "Unlocks": [["Hand", "AdvancedCircuit"], ["Assembler", "AdvancedCircuit"]],
        "Chapter": "Production",
        "Position": [3, -4],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "GoldWire",
        "label_parts": [["GoldWire", "parts"]],
        "RequiredResearches": ["AdvancedCircuit", "OreWasher"],
        "Levels": [2, 2],
        "Unlocks": [["Hand", "GoldWire"], ["Assembler", "GoldWire"]],
        "Chapter": "Production",
        "Position": [3, -5],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdvancedCircuitBoard",
        "label_parts": [["AdvancedCircuitBoard", "parts"]],
        "RequiredResearches": ["GoldWire", "PyrolysisUnit"],
        "Levels": [2, 2],
        "Unlocks": [
            ["Hand", "AdvancedCircuitBoard"],
            ["Assembler", "AdvancedCircuitBoard"],
        ],
        "Chapter": "Production",
        "Position": [3, -6],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Processor",
        "label_parts": [["Processor", "parts"]],
        "RequiredResearches": ["AdvancedCircuitBoard"],
        "Unlocks": [
            ["Hand", "Processor"],
            ["Assembler", "Processor"],
            ["Assembler", "SiliconWafer"],
            ["Assembler", "Processor2"],
        ],
        "Chapter": "Production",
        "Position": [3, -7],
        "Levels": [3, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "QuantumCore",
        "label_parts": [["QuantumCore", "parts"]],
        "RequiredResearches": ["Processor"],
        "Levels": [4, 4],
        "Unlocks": [["Hand", "QuantumCore"], ["Assembler", "QuantumCore"]],
        "Chapter": "Production",
        "Position": [3, -8],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "QuantumCircuit",
        "label_parts": [["QuantumCircuit", "parts"]],
        "RequiredResearches": ["QuantumCore"],
        "Levels": [4, 4],
        "Unlocks": [["Hand", "QuantumCircuit"], ["Assembler", "QuantumCircuit"]],
        "Chapter": "Production",
        "Position": [3, -9],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "QuantumProcessor",
        "label_parts": [["QuantumProcessor", "parts"]],
        "RequiredResearches": ["QuantumCircuit"],
        "Levels": [5, 5],
        "Unlocks": [["Hand", "QuantumProcessor"], ["Assembler", "QuantumProcessor"]],
        "Chapter": "Production",
        "Position": [4, -10],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "QuantumBrain",
        "label_parts": [["QuantumBrain", "parts"]],
        "RequiredResearches": ["QuantumProcessor"],
        "Levels": [6, 6],
        "Unlocks": [["Hand", "QuantumBrain"], ["Assembler", "QuantumBrain"]],
        "Chapter": "Production",
        "Position": [4, -11],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "QuantumComputer",
        "label_parts": [["QuantumComputer", "machines"]],
        "RequiredResearches": ["QuantumCircuit"],
        "Unlocks": [
            ["Hand", "%Material%QuantumComputer"],
            ["Constructor", "%Material%QuantumComputer"],
        ],
        "Levels": [5, 7],
        "Chapter": "Production",
        "Position": [4, -9],
        "CostSub": 1,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "MetalConstructions",
        "label_parts": [["MetalConstructions", "researches"]],
        "RequiredResearches": ["Metalwork"],
        "Unlocks": [
            ["Hand", "%Material%Corner"],
            ["Constructor", "%Material%Corner"],
            ["Hand", "%Material%Casing"],
            ["Constructor", "%Material%Casing"],
            ["Hand", "%Material%Beam"],
            ["Constructor", "%Material%Beam"],
        ],
        "Levels": [1, 7],
        "Chapter": "Decorations",
        "Position": [4, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Scaffold",
        "label_parts": [["Scaffold", "researches"]],
        "Chapter": "Decorations",
        "RequiredResearches": ["MetalConstructions"],
        "Unlocks": [
            ["Hand", "%Material%Scaffold"],
            ["Constructor", "%Material%Scaffold"],
        ],
        "Levels": [1, 7],
        "Position": [3, 4],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Chemistry",
        "label_parts": [["Chemistry", "researches"]],
        "Chapter": "Production",
        "RequiredResearches": ["ElectricEngine"],
        "Unlocks": [
            ["Hand", "%Material%ChemReactor"],
            ["Constructor", "%Material%ChemReactor"],
        ],
        "Levels": [2, 7],
        "Position": [5, -2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FilteringUnit",
        "label_parts": [["FilteringUnit", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["Chemistry"],
        "Unlocks": [
            ["Hand", "%Material%FilteringUnit"],
            ["Constructor", "%Material%FilteringUnit"],
        ],
        "Levels": [3, 7],
        "Position": [5, -3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Sifter",
        "label_parts": [["Sifter", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["Chemistry"],
        "Unlocks": [["Hand", "%Material%Sifter"], ["Constructor", "%Material%Sifter"]],
        "Levels": [3, 7],
        "Position": [6, -3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Separator",
        "label_parts": [["Separator", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["ElectricEngine"],
        "Levels": [2, 7],
        "Unlocks": [
            ["Hand", "%Material%Separator"],
            ["Constructor", "%Material%Separator"],
        ],
        "Position": [4, -3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "ElectricEngine",
        "label_parts": [["ElectricEngine", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["Electrolysis"],
        "Levels": [2, 7],
        "Unlocks": [
            ["Hand", "%Material%ElectricEngine"],
            ["Constructor", "%Material%ElectricEngine"],
        ],
        "Position": [4, -2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "OreWasher",
        "label_parts": [["OreWasher", "machines"]],
        "Levels": [2, 7],
        "Chapter": "Production",
        "RequiredResearches": ["Separator"],
        "Unlocks": [
            ["Hand", "%Material%OreWasher"],
            ["Constructor", "%Material%OreWasher"],
        ],
        "Position": [4, -4],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Mixer",
        "label_parts": [["Mixer", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["OreWasher"],
        "Levels": [2, 7],
        "Unlocks": [["Hand", "%Material%Mixer"], ["Constructor", "%Material%Mixer"]],
        "Position": [4, -5],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "ChemicalBath",
        "label_parts": [["ChemicalBath", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["FilteringUnit"],
        "Levels": [3, 7],
        "Unlocks": [
            ["Hand", "%Material%ChemicalBath"],
            ["Constructor", "%Material%ChemicalBath"],
        ],
        "Position": [5, -4],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "StainlessSteelProduction",
        "label_parts": [["StainlessSteelProduction", "researches"]],
        "RequiredResearches": ["Chemistry", "AluminiumProduction"],
        "Unlocks": [
            ["Hand", tier_material[4] + "Parts"],
            ["Hand", tier_material[4] + "Plate"],
            ["Hand", tier_material[4] + "Pipe"],
            ["Constructor", tier_material[4] + "Pipe"],
        ],
        "Chapter": "Production",
        "Position": [6, -2],
        "Levels": [4, 4],
        "CostLevelOffset": -1,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdvancedSeparation",
        "label_parts": [["AdvancedSeparation", "researches"]],
        "Chapter": "Production",
        "RequiredResearches": ["AluminiumProduction"],
        "Position": [6, -1],
        "Levels": [3, 7],
        "Unlocks": [
            ["Hand", "%Material%IndustrialSeparator"],
            ["Constructor", "%Material%IndustrialSeparator"],
        ],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "SmallBattery",
        "label_parts": [["SmallBattery", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["AdvancedSeparation"],
        "Position": [6, 0],
        "Levels": [3, 7],
        "Unlocks": [
            ["Hand", "%Material%SmallBattery"],
            ["Constructor", "%Material%SmallBattery"],
        ],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "TitaniumProduction",
        "label_parts": [["TitaniumProduction", "researches"]],
        "Chapter": "Production",
        "RequiredResearches": ["IndustrialSmelting"],
        "Unlocks": [
            ["Hand", tier_material[5] + "Parts"],
            ["Hand", tier_material[5] + "Plate"],
            ["Hand", tier_material[5] + "Pipe"],
            ["Constructor", tier_material[5] + "Pipe"],
        ],
        "Position": [7, -4],
        "Levels": [4, 4],
        "CostLevelOffset": -1,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "IndustrialBoiler",
        "label_parts": [["IndustrialBoiler", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["TitaniumProduction"],
        "Unlocks": [
            ["Hand", "%Material%IndustrialBoiler"],
            ["Connector", "%Material%IndustrialBoiler"],
        ],
        "Position": [6, -4],
        "Levels": [5, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "IndustrialSteamTurbine",
        "label_parts": [["IndustrialSteamTurbine", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["IndustrialBoiler"],
        "Unlocks": [
            ["Hand", "%Material%IndustrialSteamTurbine"],
            ["Connector", "%Material%IndustrialSteamTurbine"],
        ],
        "Position": [6, -5],
        "Levels": [5, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Freezer",
        "label_parts": [["Freezer", "machines"]],
        "RequiredResearches": ["TitaniumProduction"],
        "Unlocks": [
            ["Hand", "%Material%Freezer"],
            ["Constructor", "%Material%Freezer"],
        ],
        "Chapter": "Production",
        "Position": [8, -4],
        "Levels": [5, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "HardMetalProduction",
        "label_parts": [["HardMetalProduction", "researches"]],
        "RequiredResearches": ["Freezer"],
        "Unlocks": [
            ["Hand", tier_material[6] + "Parts"],
            ["Hand", tier_material[6] + "Plate"],
            ["Hand", tier_material[6] + "Pipe"],
            ["Constructor", tier_material[6] + "Pipe"],
        ],
        "Chapter": "Production",
        "Position": [9, -4],
        "Levels": [5, 5],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FusionReactor",
        "label_parts": [["FusionReactor", "machines"]],
        "RequiredResearches": ["HardMetalProduction"],
        "Unlocks": [
            ["Hand", "%Material%FusionReactor"],
            ["Constructor", "%Material%FusionReactor"],
        ],
        "Chapter": "Production",
        "Position": [10, -4],
        "Levels": [6, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "NeutroniumProduction",
        "label_parts": [["NeutroniumProduction", "researches"]],
        "RequiredResearches": ["FusionReactor"],
        "Unlocks": [
            ["Hand", tier_material[7] + "Parts"],
            ["Hand", tier_material[7] + "Plate"],
            ["Hand", tier_material[7] + "Pipe"],
            ["Constructor", tier_material[7] + "Pipe"],
        ],
        "Chapter": "Production",
        "Position": [11, -4],
        "Levels": [6, 6],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Portal",
        "label_parts": [["Portal", "machines"]],
        "RequiredResearches": ["NeutroniumProduction"],
        "Unlocks": [["Hand", "%Material%Portal"], ["Constructor", "%Material%Portal"]],
        "Chapter": "Production",
        "Position": [12, -4],
        "Levels": [7, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FissionReactor",
        "label_parts": [["FissionReactor", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["TitaniumProduction"],
        "Levels": [5, 7],
        "Unlocks": [
            ["Hand", "%Material%FissionReactor"],
            ["Constructor", "%Material%FissionReactor"],
        ],
        "Position": [7, -6],
    }
)
append_nuclear([7, -7], append_levels, researches)
append_levels(
    {
        "class": static_research,
        "name": "IndustrialSmelting",
        "label_parts": [["IndustrialSmelting", "researches"]],
        "Chapter": "Production",
        "RequiredResearches": ["StainlessSteelProduction"],
        "Levels": [4, 7],
        "Unlocks": [
            ["Hand", "%Material%IndustrialSmelter"],
            ["Constructor", "%Material%IndustrialSmelter"],
        ],
        "Position": [7, -2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Fermentation",
        "label_parts": [["Fermentation", "researches"]],
        "Levels": [4, 7],
        "Chapter": "Production",
        "RequiredResearches": ["IndustrialSmelting"],
        "Position": [7, -3],
        "Unlocks": [
            ["Hand", "%Material%Fermenter"],
            ["Constructor", "%Material%Fermenter"],
        ],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "BatteryBox",
        "label_parts": [["BatteryBox", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["IndustrialSmelting"],
        "Position": [8, -2],
        "Levels": [4, 7],
        "Unlocks": [
            ["Hand", "%Material%BatteryBox"],
            ["Constructor", "%Material%BatteryBox"],
        ],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "InductionCoil",
        "label_parts": [["InductionCoil", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["IndustrialSmelting"],
        "Levels": [4, 7],
        "Unlocks": [
            ["Hand", "%Material%InductionCoil"],
            ["Constructor", "%Material%InductionCoil"],
        ],
        "Position": [8, -3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "IndustrialElectricEngine",
        "label_parts": [["IndustrialElectricEngine", "machines"]],
        "Chapter": "Production",
        "RequiredResearches": ["InductionCoil"],
        "Levels": [4, 7],
        "Unlocks": [
            ["Hand", "%Material%IndustrialElectricEngine"],
            ["Constructor", "%Material%IndustrialElectricEngine"],
        ],
        "Position": [9, -3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Terminal",
        "label_parts": [["Terminal", "machines"]],
        "Levels": [4, 4],
        "Position": [7, -1],
        "Chapter": "Production",
        "RequiredResearches": ["StainlessSteelProduction"],
        "Unlocks": [
            ["Hand", tier_material[4] + "Terminal"],
            ["Constructor", tier_material[4] + "Terminal"],
        ],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FlatTerminal",
        "label_parts": [["FlatTerminal", "machines"]],
        "Levels": [4, 4],
        "Position": [8, -1],
        "Chapter": "Production",
        "RequiredResearches": ["Terminal"],
        "Unlocks": [
            ["Hand", tier_material[4] + "FlatTerminal"],
            ["Constructor", tier_material[4] + "FlatTerminal"],
        ],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Constructor",
        "label_parts": [["Constructor", "machines"]],
        "Position": [1, 5],
        "RequiredResearches": ["Assembler"],
        "Unlocks": [
            ["Hand", "%Material%Constructor"],
            ["Constructor", "%Material%Constructor"],
        ],
        "Levels": [2, 7],
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Assembler",
        "label_parts": [["Assembler", "machines"]],
        "RequiredResearches": ["Automatization"],
        "Unlocks": [
            ["Hand", "%Material%Assembler"],
            ["Constructor", "%Material%Assembler"],
        ],
        "Levels": [1, 7],
        "Position": [1, 4],
        "Chapter": "Production",
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Deconstructor",
        "label_parts": [["Deconstructor", "machines"]],
        "Position": [0, 5],
        "RequiredResearches": ["Constructor"],
        "Unlocks": [
            ["Hand", "%Material%Deconstructor"],
            ["Constructor", "%Material%Deconstructor"],
        ],
        "Levels": [2, 7],
        "Chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "BigTerminal",
        "label_parts": [["BigTerminal", "machines"]],
        "RequiredResearches": ["Terminal"],
        "Unlocks": [
            ["Hand", tier_material[5] + "BigTerminal"],
            ["Constructor", tier_material[5] + "BigTerminal"],
        ],
        "Levels": [4, 4],
        "Chapter": "Production",
        "Position": [7, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "BigFlatTerminal",
        "label_parts": [["BigFlatTerminal", "machines"]],
        "RequiredResearches": ["BigTerminal"],
        "Unlocks": [
            ["Hand", tier_material[5] + "BigFlatTerminal"],
            ["Constructor", tier_material[5] + "BigFlatTerminal"],
        ],
        "Chapter": "Production",
        "Levels": [4, 4],
        "Position": [8, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "HugeTerminal",
        "label_parts": [["HugeTerminal", "machines"]],
        "RequiredResearches": ["BigTerminal"],
        "Unlocks": [
            ["Hand", tier_material[6] + "HugeTerminal"],
            ["Constructor", tier_material[6] + "HugeTerminal"],
        ],
        "Chapter": "Production",
        "Levels": [5, 5],
        "Position": [7, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "HugeFlatTerminal",
        "label_parts": [["HugeFlatTerminal", "machines"]],
        "RequiredResearches": ["HugeTerminal"],
        "Unlocks": [
            ["Hand", tier_material[6] + "HugeFlatTerminal"],
            ["Constructor", tier_material[6] + "HugeFlatTerminal"],
        ],
        "Chapter": "Production",
        "Levels": [5, 5],
        "Position": [8, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "PyrolysisUnit",
        "label_parts": [["PyrolysisUnit", "machines"]],
        "RequiredResearches": ["Mixer"],
        "Unlocks": [
            ["Hand", "%Material%PyrolysisUnit"],
            ["Constructor", "%Material%PyrolysisUnit"],
        ],
        "Levels": [3, 7],
        "Chapter": "Production",
        "Position": [4, -6],
    }
)
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

append_levels(
    {
        "class": static_research,
        "name": "DecorativeWood",
        "label_parts": [["DecorativeWood", "researches"]],
        "Unlocks": [
            ["Hand", "WoodenPlanks"],
            ["Hand", "WoodenStairs"],
            ["Hand", "Bed"],
            ["Hand", "Door"],
        ],
        "Chapter": "Decorations",
        "Position": [0, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeWood2",
        "label_parts": [["DecorativeWood", "researches"], [level_labels[1], "common"]],
        "RequiredResearches": ["DecorativeWood"],
        "Unlocks": [
            ["Hand", "Chair"],
            ["Hand", "Fence"],
            ["Hand", "Ladder"],
            ["Hand", "Rack"],
            ["Hand", "Table"],
        ],
        "Chapter": "Decorations",
        "Position": [0, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Fence",
        "label_parts": [["Fence", "misc"]],
        "RequiredResearches": ["DecorativeWood2"],
        "Unlocks": [["Hand", "SteelFence"]],
        "Chapter": "Decorations",
        "Position": [-1, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Fence1",
        "label_parts": [["Fence", "misc"], [level_labels[1], "common"]],
        "RequiredResearches": ["Fence"],
        "Unlocks": [["Hand", "StainlessSteelFence"]],
        "Chapter": "Decorations",
        "Position": [-2, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeWood4",
        "label_parts": [["DecorativeWood", "researches"], [level_labels[3], "common"]],
        "RequiredResearches": ["DecorativeWood2"],
        "Unlocks": [["Hand", "CopperChair"]],
        "Chapter": "Decorations",
        "Position": [1, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeWood3",
        "label_parts": [["DecorativeWood", "researches"], [level_labels[2], "common"]],
        "RequiredResearches": ["DecorativeWood2", "AdvancedSmelting"],
        "Unlocks": [["Hand", "Window"]],
        "Chapter": "Decorations",
        "Position": [0, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativePlastic",
        "label_parts": [["DecorativePlastic", "researches"]],
        "RequiredResearches": ["Chemistry", "PyrolysisUnit", "DecorativeWood3"],
        "Unlocks": [["Hand", "PlasticWindow"]],
        "Chapter": "Decorations",
        "Position": [-1, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "PlasticBlock",
        "label_parts": [["PlasticBlock", "misc"]],
        "RequiredResearches": ["DecorativePlastic"],
        "Unlocks": [["Hand", "PlasticBlock"], ["Press", "PlasticBlock"]],
        "Chapter": "Decorations",
        "Position": [-2, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "BasicPlatform",
        "label_parts": [["BasicPlatform", "misc"]],
        "CompleteByDefault": True,
        "Chapter": "Decorations",
        "Unlocks": [["Hand", "BasicPlatform"], ["Press", "BasicPlatform"]],
        "Position": [1, -1],
        "RequiredResearches": [],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeStone",
        "label_parts": [["DecorativeStone", "researches"]],
        "RequiredResearches": ["BasicPlatform"],
        "Unlocks": [["Hand", "StoneTiles"], ["CuttingMachine", "StoneTiles"]],
        "Chapter": "Decorations",
        "Position": [1, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeStone2",
        "label_parts": [["DecorativeStone", "researches"], [level_labels[1], "common"]],
        "RequiredResearches": ["DecorativeStone"],
        "Unlocks": [
            ["Hand", "DarkTiles"],
            ["Hand", "RedTiles"],
            ["CuttingMachine", "DarkTiles"],
            ["CuttingMachine", "RedTiles"],
        ],
        "Chapter": "Decorations",
        "Position": [2, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "GlassBlock",
        "label_parts": [["GlassBlock", "misc"]],
        "RequiredResearches": [],
        "Unlocks": [["Hand", "GlassBlock"], ["Press", "GlassBlock"]],
        "Chapter": "Decorations",
        "Position": [2, -1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeStone3",
        "label_parts": [["DecorativeStone", "researches"], [level_labels[2], "common"]],
        "RequiredResearches": ["DecorativeStone2"],
        "Unlocks": [
            ["Hand", "DarkBricks"],
            ["Hand", "RedBricks"],
            ["Hand", "Bricks"],
            ["CuttingMachine", "DarkBricks"],
            ["CuttingMachine", "RedBricks"],
            ["CuttingMachine", "Bricks"],
        ],
        "Chapter": "Decorations",
        "Position": [2, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeStone4",
        "label_parts": [["DecorativeStone", "researches"], [level_labels[3], "common"]],
        "RequiredResearches": ["DecorativeStone3"],
        "Unlocks": [["Hand", "Stairs"]],
        "Chapter": "Decorations",
        "Position": [2, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeConcrete",
        "label_parts": [["DecorativeConcrete", "researches"]],
        "RequiredResearches": ["Mixer"],
        "Unlocks": [["Hand", "ConcreteTiles"], ["CuttingMachine", "ConcreteTiles"]],
        "Chapter": "Decorations",
        "Position": [3, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeConcrete2",
        "label_parts": [
            ["DecorativeConcrete", "researches"],
            [level_labels[1], "common"],
        ],
        "RequiredResearches": ["DecorativeConcrete"],
        "Unlocks": [
            ["Hand", "ConcreteSmallTiles"],
            ["CuttingMachine", "ConcreteSmallTiles"],
        ],
        "Chapter": "Decorations",
        "Position": [3, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeConcrete3",
        "label_parts": [
            ["DecorativeConcrete", "researches"],
            [level_labels[2], "common"],
        ],
        "RequiredResearches": ["DecorativeConcrete2"],
        "Unlocks": [["Hand", "ConcreteBricks"], ["CuttingMachine", "ConcreteBricks"]],
        "Chapter": "Decorations",
        "Position": [3, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeConcrete4",
        "label_parts": [
            ["DecorativeConcrete", "researches"],
            [level_labels[3], "common"],
        ],
        "RequiredResearches": ["DecorativeConcrete3"],
        "Unlocks": [["Hand", "DangerBlock"]],
        "Chapter": "Decorations",
        "Position": [3, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeReinforcedConcrete",
        "label_parts": [["ReinforcedConcrete", "researches"]],
        "RequiredResearches": ["DecorativeConcrete"],
        "Unlocks": [
            ["Hand", "ReinforcedConcreteTiles"],
            ["CuttingMachine", "ReinforcedConcreteTiles"],
        ],
        "Chapter": "Decorations",
        "Position": [4, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeReinforcedConcrete2",
        "label_parts": [
            ["ReinforcedConcrete", "researches"],
            [level_labels[1], "common"],
        ],
        "RequiredResearches": ["DecorativeReinforcedConcrete"],
        "Unlocks": [
            ["Hand", "ReinforcedConcreteSmallTiles"],
            ["CuttingMachine", "ReinforcedConcreteSmallTiles"],
        ],
        "Chapter": "Decorations",
        "Position": [4, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeReinforcedConcrete3",
        "label_parts": [
            ["ReinforcedConcrete", "researches"],
            [level_labels[2], "common"],
        ],
        "RequiredResearches": ["DecorativeReinforcedConcrete2"],
        "Unlocks": [
            ["Hand", "ReinforcedConcreteBricks"],
            ["CuttingMachine", "ReinforcedConcreteBricks"],
        ],
        "Chapter": "Decorations",
        "Position": [4, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorationClay",
        "label_parts": [["DecorationClay", "researches"]],
        "RequiredResearches": ["Drying"],
        "Unlocks": [["Hand", "TerracottaTiles"], ["CuttingMachine", "TerracottaTiles"]],
        "Chapter": "Decorations",
        "Position": [5, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorationClay2",
        "label_parts": [["DecorationClay", "researches"], [level_labels[1], "common"]],
        "RequiredResearches": ["DecorationClay"],
        "Unlocks": [
            ["Hand", "TerracottaBricks"],
            ["CuttingMachine", "TerracottaBricks"],
        ],
        "Chapter": "Decorations",
        "Position": [5, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Press",
        "label_parts": [["Press", "machines"]],
        "RequiredResearches": [],
        "Levels": [2, 7],
        "Unlocks": [["Hand", "%Material%Press"], ["Constructor", "%Material%Press"]],
        "Position": [2, 3],
        "Chapter": "Decorations",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "PaintTool",
        "label_parts": [["PaintTool", "parts"]],
        "RequiredResearches": [],
        "Levels": [1, 1],
        "Unlocks": [["Hand", "CopperPaintTool"], ["Constructor", "CopperPaintTool"]],
        "Position": [1, 2],
        "Chapter": "Decorations",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Lamp",
        "label_parts": [["Lamp", "machines"]],
        "RequiredResearches": [],
        "Levels": [1, 7],
        "Unlocks": [["Hand", "%Material%Lamp"], ["Constructor", "%Material%Lamp"]],
        "Position": [2, 4],
        "Chapter": "Decorations",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Column",
        "label_parts": [["Column", "misc"]],
        "RequiredResearches": [],
        "Levels": [1, 1],
        "Unlocks": [
            ["Hand", "Column"],
            ["Hand", "FluetedColumn"],
            ["Press", "Column"],
            ["Press", "FluetedColumn"],
        ],
        "Position": [1, 4],
        "Chapter": "Decorations",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Sign",
        "label_parts": [["Sign", "machines"]],
        "RequiredResearches": ["MineralsScan"],
        "Unlocks": [["Hand", "%Material%Sign"], ["Constructor", "%Material%Sign"]],
        "Levels": [0, 7],
        "Chapter": "Decorations",
        "Position": [0, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdvancedSign",
        "label_parts": [["AdvancedSign", "machines"]],
        "RequiredResearches": ["Sign"],
        "Unlocks": [
            ["Hand", "%Material%AdvancedSign"],
            ["Constructor", "%Material%AdvancedSign"],
        ],
        "Levels": [2, 7],
        "Chapter": "Decorations",
        "Position": [1, 3],
    }
)

data = {"Objects": researches}

write_file("Generated/Researches/basic.json", data)
write_file("Loc/source/researches.json", csv)
