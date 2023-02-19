from Common import *
from Materials import *
import copy
from NuclearResearches import *
from EquipmentResearches import *

researches = []

csv = []


def append_levels(research):
    if "unlocks" in research:
        unl = copy.deepcopy(research["unlocks"])
        research["unlocks"] = []

        for i in range(
            research["levels"][0] if "levels" in research else 0,
            research["levels"][1] + 1 if "levels" in research else 1,
        ):
            new = []
            for j in unl:
                new.append([j[0], j[1].replace("%Material%", tier_material[i])])

            research["unlocks"].append(new)

    CostSub = research["CostSub"] if "CostSub" in research else 0
    CostMul = research["CostMul"] if "CostMul" in research else 1

    offset = research["CostLevelOffset"] if "CostLevelOffset" in research else 0

    research["data_points"] = []
    for i in range(
        research["levels"][0] if "levels" in research else 0,
        research["levels"][1] + 1 if "levels" in research else 1,
    ):
        research["data_points"].append(
            {"items": res_cost(i - CostSub + offset, CostMul)}
        )

    researches.append(research)


append_levels(
    {
        "class": static_research,
        "name": "InitialScan",
        "label_parts": [["InitialScan", "researches"]],
        "complete_by_default": True,
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "MineralsScan",
        "label_parts": [["MineralsScan", "researches"]],
        "required": ["InitialScan"],
        "unlocks": [
            ["Hand", tier_material[0] + "Furnace"],
            ["Constructor", tier_material[0] + "Furnace"],
            ["Hand", "SandSurface"],
            ["Hand", "GravelSurface"],
        ],
        "collect": {"items": [{"name": "Dirt", "count": 10}]},
        "position": [0, 1],
        "chapter": "Production",
        "complete_by_default": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdditionalStorage",
        "label_parts": [["AdditionalStorage", "researches"]],
        "required": ["MineralsScan"],
        "unlocks": [["Hand", "%Material%Chest"], ["Constructor", "%Material%Chest"]],
        "position": [-1, 1],
        "levels": [0, 7],
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "SingleTypeStorage",
        "label_parts": [["SingleTypeStorage", "researches"]],
        "required": ["AdditionalStorage"],
        "position": [-2, 1],
        "levels": [1, 7],
        "chapter": "Production",
        "unlocks": [
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
        "chapter": "Production",
        "required": ["AdditionalStorage"],
        "unlocks": [],
        "position": [-2, 2],
        "levels": [0, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Electricity",
        "label_parts": [["Electricity", "researches"]],
        "required": ["InitialScan"],
        "unlocks": [
            ["Hand", tier_material[1] + "Connector"],
            ["Constructor", tier_material[1] + "Connector"],
        ],
        "collect": {"items": [{"name": "Sand", "count": 10}]},
        "position": [0, -1],
        "chapter": "Production",
        "complete_by_default": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "ElectricFurnace",
        "label_parts": [["ElectricFurnace", "machines"]],
        "levels": [2, 7],
        "required": ["Electricity"],
        "position": [-1, -2],
        "chapter": "Production",
        "unlocks": [
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
        "required": ["Electricity"],
        "unlocks": [
            ["Hand", tier_material[2] + "ElectricalSwitch"],
            ["Constructor", tier_material[2] + "ElectricalSwitch"],
        ],
        "position": [0, -2],
        "levels": [2, 2],
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Diode",
        "label_parts": [["Diode", "machines"]],
        "position": [0, -3],
        "required": ["Electricity"],
        "levels": [2, 7],
        "chapter": "Production",
        "unlocks": [["Hand", "%Material%Diode"], ["Constructor", "%Material%Diode"]],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "PowerGeneration",
        "label_parts": [["PowerGeneration", "researches"]],
        "required": ["Electricity"],
        "levels": [1, 1],
        "unlocks": [
            ["Hand", "%Material%CompactGenerator"],
            ["Constructor", "%Material%CompactGenerator"],
        ],
        "chapter": "Production",
        "position": [1, -1],
        "complete_by_default": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Electrolysis",
        "label_parts": [["Electrolysis", "researches"]],
        "required": ["SteelProduction"],
        "levels": [2, 7],
        "unlocks": [
            ["Hand", "%Material%Electrolyzer"],
            ["Constructor", "%Material%Electrolyzer"],
        ],
        "chapter": "Production",
        "position": [4, -1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "SteelProduction",
        "label_parts": [["SteelProduction", "researches"]],
        "required": ["Drying"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%BlastFurnace"],
            ["Constructor", "%Material%BlastFurnace"],
        ],
        "also_unlocks": [
            ["Hand", "SteelParts"],
            ["Hand", "SteelPlate"],
            ["Hand", "SteelPipe"],
        ],
        "chapter": "Production",
        "position": [3, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdvancedSmelting",
        "label_parts": [["AdvancedSmelting", "researches"]],
        "required": ["SteelProduction"],
        "position": [4, 0],
        "levels": [2, 7],
        "unlocks": [
            ["Hand", "%Material%ArcSmelter"],
            ["Constructor", "%Material%ArcSmelter"],
        ],
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "SolarPanel",
        "label_parts": [["SolarPanel", "machines"]],
        "position": [5, 0],
        "required": ["AluminiumProduction"],
        "levels": [3, 7],
        "unlocks": [
            ["Hand", "%Material%SolarPanel"],
            ["Constructor", "%Material%SolarPanel"],
        ],
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AluminiumProduction",
        "label_parts": [["AluminiumProduction", "researches"]],
        "required": ["AdvancedSmelting", "Electrolysis"],
        "unlocks": [
            ["Hand", tier_material[3] + "Parts"],
            ["Hand", tier_material[3] + "Plate"],
            ["Hand", tier_material[3] + "Pipe"],
            ["Constructor", tier_material[3] + "Pipe"],
        ],
        "chapter": "Production",
        "position": [5, -1],
        "levels": [3, 3],
        "CostLevelOffset": -1,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "MassivePowerGeneration",
        "label_parts": [["MassivePowerGeneration", "researches"]],
        "required": ["PowerGeneration"],
        "unlocks": [
            ["Hand", "%Material%Generator"],
            ["Constructor", "%Material%Generator"],
            ["Hand", "%Material%Boiler"],
            ["Constructor", "%Material%Boiler"],
            ["Hand", "%Material%SteamTurbine"],
            ["Constructor", "%Material%SteamTurbine"],
        ],
        "levels": [2, 7],
        "chapter": "Production",
        "position": [1, -2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "GasTurbine",
        "label_parts": [["GasTurbine", "machines"]],
        "position": [1, -3],
        "required": ["MassivePowerGeneration"],
        "levels": [4, 7],
        "chapter": "Production",
        "unlocks": [
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
        "required": ["MineralsScan"],
        "unlocks": [
            ["Hand", "%Material%Smelter"],
            ["Constructor", "%Material%Smelter"],
        ],
        "levels": [0, 2],
        "position": [0, 2],
        "chapter": "Production",
        "complete_by_default": True,
    }
)
append_equipment([-1, 3], append_levels, researches)
append_levels(
    {
        "class": static_research,
        "name": "Metalwork",
        "label_parts": [["Metalwork", "researches"]],
        "required": ["Smelting"],
        "unlocks": [
            ["Hand", "CopperParts"],
            ["Hand", "CopperPlate"],
            ["Hand", "CopperPipe"],
        ],
        "collect": {"items": [{"name": "CopperOre", "count": 10}]},
        "position": [1, 2],
        "levels": [1, 1],
        "chapter": "Production",
        "complete_by_default": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Valve",
        "label_parts": [["Vent", "machines"]],
        "required": ["Metalwork"],
        "unlocks": [
            ["Hand", tier_material[1] + "Vent"],
            ["Constructor", tier_material[1] + "Vent"],
        ],
        "position": [0, 3],
        "levels": [1, 1],
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "BasicMachines",
        "label_parts": [["BasicMachines", "researches"]],
        "required": ["Metalwork"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%Macerator"],
            ["Constructor", "%Material%Macerator"],
            ["Hand", "%Material%AutomaticHammer"],
            ["Constructor", "%Material%AutomaticHammer"],
        ],
        "chapter": "Production",
        "position": [1, 3],
        "CostMul": 0.25,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Flywheel",
        "label_parts": [["Flywheel", "machines"]],
        "required": ["BasicMachines"],
        "unlocks": [
            ["Hand", tier_material[2] + "Flywheel"],
            ["Constructor", tier_material[2] + "Flywheel"],
        ],
        "levels": [2, 2],
        "chapter": "Production",
        "position": [0, 4],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Cutting",
        "label_parts": [["Cutting", "researches"]],
        "required": ["BasicMachines"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%CuttingMachine"],
            ["Constructor", "%Material%CuttingMachine"],
        ],
        "chapter": "Production",
        "position": [2, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "SolidDump",
        "label_parts": [["SolidDump", "machines"]],
        "position": [4, 1],
        "levels": [2, 2],
        "chapter": "Production",
        "required": ["Furnace"],
        "unlocks": [
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
        "required": ["Automatization"],
        "levels": [1, 7],
        "unlocks": [["Hand", "%Material%Pump"], ["Constructor", "%Material%Pump"]],
        "chapter": "Production",
        "position": [3, 2],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Container",
        "label_parts": [["Container", "machines"]],
        "required": ["Pump"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%Container"],
            ["Constructor", "%Material%Container"],
        ],
        "chapter": "Production",
        "position": [4, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FluidFurnace",
        "label_parts": [["FluidFurnace", "machines"]],
        "required": ["Furnace"],
        "unlocks": [
            ["Hand", "%Material%FluidFurnace"],
            ["Constructor", "%Material%FluidFurnace"],
        ],
        "levels": [1, 7],
        "chapter": "Production",
        "position": [3, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FluidDumping",
        "label_parts": [["FluidDumping", "researches"]],
        "required": ["Container"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%FluidDump"],
            ["Constructor", "%Material%FluidDump"],
        ],
        "chapter": "Production",
        "position": [5, 2],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "GasDump",
        "label_parts": [["GasDump", "machines"]],
        "position": [5, 1],
        "levels": [2, 2],
        "chapter": "Production",
        "required": ["Container"],
        "unlocks": [
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
        "required": ["BasicMachines"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%RobotArm"],
            ["Constructor", "%Material%RobotArm"],
            ["Hand", "%Material%Conveyor"],
            ["Constructor", "%Material%Conveyor"],
            ["Hand", "%Material%Splitter"],
            ["Constructor", "%Material%Splitter"],
        ],
        "chapter": "Production",
        "position": [2, 3],
        "CostMul": 0.25,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Filtering",
        "label_parts": [["Filtering", "researches"]],
        "required": ["Automatization"],
        "unlocks": [
            ["Hand", "%Material%FilteringRobotArm"],
            ["Constructor", "%Material%FilteringRobotArm"],
            ["Hand", "%Material%Sorter"],
            ["Constructor", "%Material%Sorter"],
        ],
        "levels": [1, 7],
        "chapter": "Production",
        "position": [3, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FilteringPump",
        "label_parts": [["FilteringPump", "machines"]],
        "required": ["Pump"],
        "unlocks": [
            ["Hand", "%Material%FilteringPump"],
            ["Constructor", "%Material%FilteringPump"],
        ],
        "levels": [1, 7],
        "chapter": "Production",
        "position": [4, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AutomaticMining",
        "label_parts": [["AutomaticMining", "researches"]],
        "required": ["Automatization"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%DrillingRig"],
            ["Constructor", "%Material%DrillingRig"],
        ],
        "position": [2, 4],
        "chapter": "Production",
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Pumpjack",
        "label_parts": [["Pumpjack", "machines"]],
        "position": [2, 5],
        "required": ["AutomaticMining"],
        "unlocks": [
            ["Hand", "%Material%Pumpjack"],
            ["Constructor", "%Material%Pumpjack"],
        ],
        "levels": [3, 7],
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AutomaticFarm",
        "label_parts": [["AutomaticFarm", "machines"]],
        "required": ["Automatization"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%AutomaticFarm"],
            ["Constructor", "%Material%AutomaticFarm"],
        ],
        "chapter": "Production",
        "position": [3, 4],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "HeatTransferring",
        "label_parts": [["HeatTransferring", "researches"]],
        "required": ["InitialScan"],
        "unlocks": [
            ["Hand", "%Material%HeatPipe"],
            ["Constructor", "%Material%HeatPipe"],
        ],
        "position": [-1, -1],
        "levels": [1, 1],
        "chapter": "Production",
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Radiator",
        "label_parts": [["Radiator", "machines"]],
        "required": ["HeatTransferring"],
        "levels": [3, 7],
        "unlocks": [
            ["Hand", "%Material%Radiator"],
            ["Constructor", "%Material%Radiator"],
        ],
        "position": [-2, -1],
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AtmosphericCondenser",
        "label_parts": [["AtmosphericCondenser", "machines"]],
        "required": ["InitialScan"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%AtmosphericCondenser"],
            ["Constructor", "%Material%AtmosphericCondenser"],
        ],
        "chapter": "Production",
        "position": [-2, 0],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "StirlingEngine",
        "label_parts": [["StirlingEngine", "machines"]],
        "required": ["MineralsScan"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%StirlingEngine"],
            ["Constructor", "%Material%StirlingEngine"],
        ],
        "chapter": "Production",
        "position": [1, 1],
        "complete_by_default": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Furnace",
        "label_parts": [["Furnace", "machines"]],
        "required": ["StirlingEngine"],
        "levels": [1, 7],
        "unlocks": [
            ["Hand", "%Material%Furnace"],
            ["Constructor", "%Material%Furnace"],
        ],
        "chapter": "Production",
        "position": [2, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Drying",
        "label_parts": [["Drying", "researches"]],
        "required": [
            "Furnace",
        ],
        "levels": [1, 7],
        "unlocks": [["Hand", "%Material%Oven"], ["Constructor", "%Material%Oven"]],
        "position": [2, 0],
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DistributedComputing",
        "label_parts": [["DistributedComputing", "researches"]],
        "required": ["PowerGeneration"],
        "unlocks": [
            ["Hand", "%Material%Computer"],
            ["Constructor", "%Material%Computer"],
        ],
        "levels": [1, 7],
        "chapter": "Production",
        "position": [2, -1],
        "complete_by_default": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "CopperWire",
        "label_parts": [["CopperWire", "parts"]],
        "required": ["DistributedComputing"],
        "levels": [1, 1],
        "unlocks": [["Hand", "CopperWire"], ["Assembler", "CopperWire"]],
        "chapter": "Production",
        "position": [2, -2],
        "complete_by_default": True,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "CircuitBoard",
        "label_parts": [["CircuitBoard", "parts"]],
        "required": ["CopperWire"],
        "levels": [1, 1],
        "unlocks": [["Hand", "CircuitBoard"]],
        "chapter": "Production",
        "position": [2, -3],
        "CostMul": 0.25,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Circuit",
        "label_parts": [["Circuit", "parts"]],
        "required": ["CircuitBoard"],
        "unlocks": [["Hand", "Circuit"], ["Assembler", "Circuit"]],
        "levels": [1, 1],
        "chapter": "Production",
        "position": [2, -4],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "LogicCircuit",
        "label_parts": [["LogicCircuit", "machines"]],
        "required": ["Circuit"],
        "unlocks": [
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
        "levels": [1, 1],
        "chapter": "Production",
        "position": [3, -3],
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdvancedCircuit",
        "label_parts": [["AdvancedCircuit", "parts"]],
        "required": ["Circuit"],
        "levels": [2, 2],
        "unlocks": [["Hand", "AdvancedCircuit"], ["Assembler", "AdvancedCircuit"]],
        "chapter": "Production",
        "position": [3, -4],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "GoldWire",
        "label_parts": [["GoldWire", "parts"]],
        "required": ["AdvancedCircuit", "OreWasher"],
        "levels": [2, 2],
        "unlocks": [["Hand", "GoldWire"], ["Assembler", "GoldWire"]],
        "chapter": "Production",
        "position": [3, -5],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdvancedCircuitBoard",
        "label_parts": [["AdvancedCircuitBoard", "parts"]],
        "required": ["GoldWire", "PyrolysisUnit"],
        "levels": [2, 2],
        "unlocks": [
            ["Hand", "AdvancedCircuitBoard"],
            ["Assembler", "AdvancedCircuitBoard"],
        ],
        "chapter": "Production",
        "position": [3, -6],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Processor",
        "label_parts": [["Processor", "parts"]],
        "required": ["AdvancedCircuitBoard"],
        "unlocks": [
            ["Hand", "Processor"],
            ["Assembler", "Processor"],
            ["Assembler", "SiliconWafer"],
            ["Assembler", "Processor2"],
        ],
        "chapter": "Production",
        "position": [3, -7],
        "levels": [3, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "QuantumCore",
        "label_parts": [["QuantumCore", "parts"]],
        "required": ["Processor"],
        "levels": [4, 4],
        "unlocks": [["Hand", "QuantumCore"], ["Assembler", "QuantumCore"]],
        "chapter": "Production",
        "position": [3, -8],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "QuantumCircuit",
        "label_parts": [["QuantumCircuit", "parts"]],
        "required": ["QuantumCore"],
        "levels": [4, 4],
        "unlocks": [["Hand", "QuantumCircuit"], ["Assembler", "QuantumCircuit"]],
        "chapter": "Production",
        "position": [3, -9],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "QuantumProcessor",
        "label_parts": [["QuantumProcessor", "parts"]],
        "required": ["QuantumCircuit"],
        "levels": [5, 5],
        "unlocks": [["Hand", "QuantumProcessor"], ["Assembler", "QuantumProcessor"]],
        "chapter": "Production",
        "position": [4, -10],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "QuantumBrain",
        "label_parts": [["QuantumBrain", "parts"]],
        "required": ["QuantumProcessor"],
        "levels": [6, 6],
        "unlocks": [["Hand", "QuantumBrain"], ["Assembler", "QuantumBrain"]],
        "chapter": "Production",
        "position": [4, -11],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "QuantumComputer",
        "label_parts": [["QuantumComputer", "machines"]],
        "required": ["QuantumCircuit"],
        "unlocks": [
            ["Hand", "%Material%QuantumComputer"],
            ["Constructor", "%Material%QuantumComputer"],
        ],
        "levels": [5, 7],
        "chapter": "Production",
        "position": [4, -9],
        "CostSub": 1,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "MetalConstructions",
        "label_parts": [["MetalConstructions", "researches"]],
        "required": ["Metalwork"],
        "unlocks": [
            ["Hand", "%Material%Corner"],
            ["Constructor", "%Material%Corner"],
            ["Hand", "%Material%Casing"],
            ["Constructor", "%Material%Casing"],
            ["Hand", "%Material%Beam"],
            ["Constructor", "%Material%Beam"],
        ],
        "levels": [1, 7],
        "chapter": "Decorations",
        "position": [4, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Scaffold",
        "label_parts": [["Scaffold", "researches"]],
        "chapter": "Decorations",
        "required": ["MetalConstructions"],
        "unlocks": [
            ["Hand", "%Material%Scaffold"],
            ["Constructor", "%Material%Scaffold"],
        ],
        "levels": [1, 7],
        "position": [3, 4],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Chemistry",
        "label_parts": [["Chemistry", "researches"]],
        "chapter": "Production",
        "required": ["ElectricEngine"],
        "unlocks": [
            ["Hand", "%Material%ChemReactor"],
            ["Constructor", "%Material%ChemReactor"],
        ],
        "levels": [2, 7],
        "position": [5, -2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FilteringUnit",
        "label_parts": [["FilteringUnit", "machines"]],
        "chapter": "Production",
        "required": ["Chemistry"],
        "unlocks": [
            ["Hand", "%Material%FilteringUnit"],
            ["Constructor", "%Material%FilteringUnit"],
        ],
        "levels": [3, 7],
        "position": [5, -3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Sifter",
        "label_parts": [["Sifter", "machines"]],
        "chapter": "Production",
        "required": ["Chemistry"],
        "unlocks": [["Hand", "%Material%Sifter"], ["Constructor", "%Material%Sifter"]],
        "levels": [3, 7],
        "position": [6, -3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Separator",
        "label_parts": [["Separator", "machines"]],
        "chapter": "Production",
        "required": ["ElectricEngine"],
        "levels": [2, 7],
        "unlocks": [
            ["Hand", "%Material%Separator"],
            ["Constructor", "%Material%Separator"],
        ],
        "position": [4, -3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "ElectricEngine",
        "label_parts": [["ElectricEngine", "machines"]],
        "chapter": "Production",
        "required": ["Electrolysis"],
        "levels": [2, 7],
        "unlocks": [
            ["Hand", "%Material%ElectricEngine"],
            ["Constructor", "%Material%ElectricEngine"],
        ],
        "position": [4, -2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "OreWasher",
        "label_parts": [["OreWasher", "machines"]],
        "levels": [2, 7],
        "chapter": "Production",
        "required": ["Separator"],
        "unlocks": [
            ["Hand", "%Material%OreWasher"],
            ["Constructor", "%Material%OreWasher"],
        ],
        "position": [4, -4],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Mixer",
        "label_parts": [["Mixer", "machines"]],
        "chapter": "Production",
        "required": ["OreWasher"],
        "levels": [2, 7],
        "unlocks": [["Hand", "%Material%Mixer"], ["Constructor", "%Material%Mixer"]],
        "position": [4, -5],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "ChemicalBath",
        "label_parts": [["ChemicalBath", "machines"]],
        "chapter": "Production",
        "required": ["FilteringUnit"],
        "levels": [3, 7],
        "unlocks": [
            ["Hand", "%Material%ChemicalBath"],
            ["Constructor", "%Material%ChemicalBath"],
        ],
        "position": [5, -4],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "StainlessSteelProduction",
        "label_parts": [["StainlessSteelProduction", "researches"]],
        "required": ["Chemistry", "AluminiumProduction"],
        "unlocks": [
            ["Hand", tier_material[4] + "Parts"],
            ["Hand", tier_material[4] + "Plate"],
            ["Hand", tier_material[4] + "Pipe"],
            ["Constructor", tier_material[4] + "Pipe"],
        ],
        "chapter": "Production",
        "position": [6, -2],
        "levels": [4, 4],
        "CostLevelOffset": -1,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdvancedSeparation",
        "label_parts": [["AdvancedSeparation", "researches"]],
        "chapter": "Production",
        "required": ["AluminiumProduction"],
        "position": [6, -1],
        "levels": [3, 7],
        "unlocks": [
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
        "chapter": "Production",
        "required": ["AdvancedSeparation"],
        "position": [6, 0],
        "levels": [3, 7],
        "unlocks": [
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
        "chapter": "Production",
        "required": ["IndustrialSmelting"],
        "unlocks": [
            ["Hand", tier_material[5] + "Parts"],
            ["Hand", tier_material[5] + "Plate"],
            ["Hand", tier_material[5] + "Pipe"],
            ["Constructor", tier_material[5] + "Pipe"],
        ],
        "position": [7, -4],
        "levels": [4, 4],
        "CostLevelOffset": -1,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "IndustrialBoiler",
        "label_parts": [["IndustrialBoiler", "machines"]],
        "chapter": "Production",
        "required": ["TitaniumProduction"],
        "unlocks": [
            ["Hand", "%Material%IndustrialBoiler"],
            ["Connector", "%Material%IndustrialBoiler"],
        ],
        "position": [6, -4],
        "levels": [5, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "IndustrialSteamTurbine",
        "label_parts": [["IndustrialSteamTurbine", "machines"]],
        "chapter": "Production",
        "required": ["IndustrialBoiler"],
        "unlocks": [
            ["Hand", "%Material%IndustrialSteamTurbine"],
            ["Connector", "%Material%IndustrialSteamTurbine"],
        ],
        "position": [6, -5],
        "levels": [5, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Freezer",
        "label_parts": [["Freezer", "machines"]],
        "required": ["TitaniumProduction"],
        "unlocks": [
            ["Hand", "%Material%Freezer"],
            ["Constructor", "%Material%Freezer"],
        ],
        "chapter": "Production",
        "position": [8, -4],
        "levels": [5, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "HardMetalProduction",
        "label_parts": [["HardMetalProduction", "researches"]],
        "required": ["Freezer"],
        "unlocks": [
            ["Hand", tier_material[6] + "Parts"],
            ["Hand", tier_material[6] + "Plate"],
            ["Hand", tier_material[6] + "Pipe"],
            ["Constructor", tier_material[6] + "Pipe"],
        ],
        "chapter": "Production",
        "position": [9, -4],
        "levels": [5, 5],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FusionReactor",
        "label_parts": [["FusionReactor", "machines"]],
        "required": ["HardMetalProduction"],
        "unlocks": [
            ["Hand", "%Material%FusionReactor"],
            ["Constructor", "%Material%FusionReactor"],
        ],
        "chapter": "Production",
        "position": [10, -4],
        "levels": [6, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "NeutroniumProduction",
        "label_parts": [["NeutroniumProduction", "researches"]],
        "required": ["FusionReactor"],
        "unlocks": [
            ["Hand", tier_material[7] + "Parts"],
            ["Hand", tier_material[7] + "Plate"],
            ["Hand", tier_material[7] + "Pipe"],
            ["Constructor", tier_material[7] + "Pipe"],
        ],
        "chapter": "Production",
        "position": [11, -4],
        "levels": [6, 6],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Portal",
        "label_parts": [["Portal", "machines"]],
        "required": ["NeutroniumProduction"],
        "unlocks": [["Hand", "%Material%Portal"], ["Constructor", "%Material%Portal"]],
        "chapter": "Production",
        "position": [12, -4],
        "levels": [7, 7],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "FissionReactor",
        "label_parts": [["FissionReactor", "machines"]],
        "chapter": "Production",
        "required": ["TitaniumProduction"],
        "levels": [5, 7],
        "unlocks": [
            ["Hand", "%Material%FissionReactor"],
            ["Constructor", "%Material%FissionReactor"],
        ],
        "position": [7, -6],
    }
)
append_nuclear([7, -7], append_levels, researches)
append_levels(
    {
        "class": static_research,
        "name": "IndustrialSmelting",
        "label_parts": [["IndustrialSmelting", "researches"]],
        "chapter": "Production",
        "required": ["StainlessSteelProduction"],
        "levels": [4, 7],
        "unlocks": [
            ["Hand", "%Material%IndustrialSmelter"],
            ["Constructor", "%Material%IndustrialSmelter"],
        ],
        "position": [7, -2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Fermentation",
        "label_parts": [["Fermentation", "researches"]],
        "levels": [4, 7],
        "chapter": "Production",
        "required": ["IndustrialSmelting"],
        "position": [7, -3],
        "unlocks": [
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
        "chapter": "Production",
        "required": ["IndustrialSmelting"],
        "position": [8, -2],
        "levels": [4, 7],
        "unlocks": [
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
        "chapter": "Production",
        "required": ["IndustrialSmelting"],
        "levels": [4, 7],
        "unlocks": [
            ["Hand", "%Material%InductionCoil"],
            ["Constructor", "%Material%InductionCoil"],
        ],
        "position": [8, -3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "IndustrialElectricEngine",
        "label_parts": [["IndustrialElectricEngine", "machines"]],
        "chapter": "Production",
        "required": ["InductionCoil"],
        "levels": [4, 7],
        "unlocks": [
            ["Hand", "%Material%IndustrialElectricEngine"],
            ["Constructor", "%Material%IndustrialElectricEngine"],
        ],
        "position": [9, -3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Terminal",
        "label_parts": [["Terminal", "machines"]],
        "levels": [4, 4],
        "position": [7, -1],
        "chapter": "Production",
        "required": ["StainlessSteelProduction"],
        "unlocks": [
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
        "levels": [4, 4],
        "position": [8, -1],
        "chapter": "Production",
        "required": ["Terminal"],
        "unlocks": [
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
        "position": [1, 5],
        "required": ["Assembler"],
        "unlocks": [
            ["Hand", "%Material%Constructor"],
            ["Constructor", "%Material%Constructor"],
        ],
        "levels": [2, 7],
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Assembler",
        "label_parts": [["Assembler", "machines"]],
        "required": ["Automatization"],
        "unlocks": [
            ["Hand", "%Material%Assembler"],
            ["Constructor", "%Material%Assembler"],
        ],
        "levels": [1, 7],
        "position": [1, 4],
        "chapter": "Production",
        "CostMul": 0.5,
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Deconstructor",
        "label_parts": [["Deconstructor", "machines"]],
        "position": [0, 5],
        "required": ["Constructor"],
        "unlocks": [
            ["Hand", "%Material%Deconstructor"],
            ["Constructor", "%Material%Deconstructor"],
        ],
        "levels": [2, 7],
        "chapter": "Production",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "BigTerminal",
        "label_parts": [["BigTerminal", "machines"]],
        "required": ["Terminal"],
        "unlocks": [
            ["Hand", tier_material[5] + "BigTerminal"],
            ["Constructor", tier_material[5] + "BigTerminal"],
        ],
        "levels": [4, 4],
        "chapter": "Production",
        "position": [7, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "BigFlatTerminal",
        "label_parts": [["BigFlatTerminal", "machines"]],
        "required": ["BigTerminal"],
        "unlocks": [
            ["Hand", tier_material[5] + "BigFlatTerminal"],
            ["Constructor", tier_material[5] + "BigFlatTerminal"],
        ],
        "chapter": "Production",
        "levels": [4, 4],
        "position": [8, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "HugeTerminal",
        "label_parts": [["HugeTerminal", "machines"]],
        "required": ["BigTerminal"],
        "unlocks": [
            ["Hand", tier_material[6] + "HugeTerminal"],
            ["Constructor", tier_material[6] + "HugeTerminal"],
        ],
        "chapter": "Production",
        "levels": [5, 5],
        "position": [7, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "HugeFlatTerminal",
        "label_parts": [["HugeFlatTerminal", "machines"]],
        "required": ["HugeTerminal"],
        "unlocks": [
            ["Hand", tier_material[6] + "HugeFlatTerminal"],
            ["Constructor", tier_material[6] + "HugeFlatTerminal"],
        ],
        "chapter": "Production",
        "levels": [5, 5],
        "position": [8, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "PyrolysisUnit",
        "label_parts": [["PyrolysisUnit", "machines"]],
        "required": ["Mixer"],
        "unlocks": [
            ["Hand", "%Material%PyrolysisUnit"],
            ["Constructor", "%Material%PyrolysisUnit"],
        ],
        "levels": [3, 7],
        "chapter": "Production",
        "position": [4, -6],
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
        "unlocks": [
            ["Hand", "WoodenPlanks"],
            ["Hand", "WoodenStairs"],
            ["Hand", "Bed"],
            ["Hand", "Door"],
        ],
        "chapter": "Decorations",
        "position": [0, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeWood2",
        "label_parts": [["DecorativeWood", "researches"], [level_labels[1], "common"]],
        "required": ["DecorativeWood"],
        "unlocks": [
            ["Hand", "Chair"],
            ["Hand", "Fence"],
            ["Hand", "Ladder"],
            ["Hand", "Rack"],
            ["Hand", "Table"],
        ],
        "chapter": "Decorations",
        "position": [0, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Fence",
        "label_parts": [["Fence", "misc"]],
        "required": ["DecorativeWood2"],
        "unlocks": [["Hand", "SteelFence"]],
        "chapter": "Decorations",
        "position": [-1, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Fence1",
        "label_parts": [["Fence", "misc"], [level_labels[1], "common"]],
        "required": ["Fence"],
        "unlocks": [["Hand", "StainlessSteelFence"]],
        "chapter": "Decorations",
        "position": [-2, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeWood4",
        "label_parts": [["DecorativeWood", "researches"], [level_labels[3], "common"]],
        "required": ["DecorativeWood2"],
        "unlocks": [["Hand", "CopperChair"]],
        "chapter": "Decorations",
        "position": [1, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeWood3",
        "label_parts": [["DecorativeWood", "researches"], [level_labels[2], "common"]],
        "required": ["DecorativeWood2", "AdvancedSmelting"],
        "unlocks": [["Hand", "Window"]],
        "chapter": "Decorations",
        "position": [0, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativePlastic",
        "label_parts": [["DecorativePlastic", "researches"]],
        "required": ["Chemistry", "PyrolysisUnit", "DecorativeWood3"],
        "unlocks": [["Hand", "PlasticWindow"]],
        "chapter": "Decorations",
        "position": [-1, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "PlasticBlock",
        "label_parts": [["PlasticBlock", "misc"]],
        "required": ["DecorativePlastic"],
        "unlocks": [["Hand", "PlasticBlock"], ["Press", "PlasticBlock"]],
        "chapter": "Decorations",
        "position": [-2, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "BasicPlatform",
        "label_parts": [["BasicPlatform", "misc"]],
        "complete_by_default": True,
        "chapter": "Decorations",
        "unlocks": [["Hand", "BasicPlatform"], ["Press", "BasicPlatform"]],
        "position": [1, -1],
        "required": [],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeStone",
        "label_parts": [["DecorativeStone", "researches"]],
        "required": ["BasicPlatform"],
        "unlocks": [["Hand", "StoneTiles"], ["CuttingMachine", "StoneTiles"]],
        "chapter": "Decorations",
        "position": [1, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeStone2",
        "label_parts": [["DecorativeStone", "researches"], [level_labels[1], "common"]],
        "required": ["DecorativeStone"],
        "unlocks": [
            ["Hand", "DarkTiles"],
            ["Hand", "RedTiles"],
            ["CuttingMachine", "DarkTiles"],
            ["CuttingMachine", "RedTiles"],
        ],
        "chapter": "Decorations",
        "position": [2, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "GlassBlock",
        "label_parts": [["GlassBlock", "misc"]],
        "required": [],
        "unlocks": [["Hand", "GlassBlock"], ["Press", "GlassBlock"]],
        "chapter": "Decorations",
        "position": [2, -1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeStone3",
        "label_parts": [["DecorativeStone", "researches"], [level_labels[2], "common"]],
        "required": ["DecorativeStone2"],
        "unlocks": [
            ["Hand", "DarkBricks"],
            ["Hand", "RedBricks"],
            ["Hand", "Bricks"],
            ["CuttingMachine", "DarkBricks"],
            ["CuttingMachine", "RedBricks"],
            ["CuttingMachine", "Bricks"],
        ],
        "chapter": "Decorations",
        "position": [2, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeStone4",
        "label_parts": [["DecorativeStone", "researches"], [level_labels[3], "common"]],
        "required": ["DecorativeStone3"],
        "unlocks": [["Hand", "Stairs"]],
        "chapter": "Decorations",
        "position": [2, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeConcrete",
        "label_parts": [["DecorativeConcrete", "researches"]],
        "required": ["Mixer"],
        "unlocks": [["Hand", "ConcreteTiles"], ["CuttingMachine", "ConcreteTiles"]],
        "chapter": "Decorations",
        "position": [3, 0],
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
        "required": ["DecorativeConcrete"],
        "unlocks": [
            ["Hand", "ConcreteSmallTiles"],
            ["CuttingMachine", "ConcreteSmallTiles"],
        ],
        "chapter": "Decorations",
        "position": [3, 1],
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
        "required": ["DecorativeConcrete2"],
        "unlocks": [["Hand", "ConcreteBricks"], ["CuttingMachine", "ConcreteBricks"]],
        "chapter": "Decorations",
        "position": [3, 2],
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
        "required": ["DecorativeConcrete3"],
        "unlocks": [["Hand", "DangerBlock"]],
        "chapter": "Decorations",
        "position": [3, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorativeReinforcedConcrete",
        "label_parts": [["ReinforcedConcrete", "researches"]],
        "required": ["DecorativeConcrete"],
        "unlocks": [
            ["Hand", "ReinforcedConcreteTiles"],
            ["CuttingMachine", "ReinforcedConcreteTiles"],
        ],
        "chapter": "Decorations",
        "position": [4, 0],
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
        "required": ["DecorativeReinforcedConcrete"],
        "unlocks": [
            ["Hand", "ReinforcedConcreteSmallTiles"],
            ["CuttingMachine", "ReinforcedConcreteSmallTiles"],
        ],
        "chapter": "Decorations",
        "position": [4, 1],
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
        "required": ["DecorativeReinforcedConcrete2"],
        "unlocks": [
            ["Hand", "ReinforcedConcreteBricks"],
            ["CuttingMachine", "ReinforcedConcreteBricks"],
        ],
        "chapter": "Decorations",
        "position": [4, 2],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorationClay",
        "label_parts": [["DecorationClay", "researches"]],
        "required": ["Drying"],
        "unlocks": [["Hand", "TerracottaTiles"], ["CuttingMachine", "TerracottaTiles"]],
        "chapter": "Decorations",
        "position": [5, 0],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "DecorationClay2",
        "label_parts": [["DecorationClay", "researches"], [level_labels[1], "common"]],
        "required": ["DecorationClay"],
        "unlocks": [
            ["Hand", "TerracottaBricks"],
            ["CuttingMachine", "TerracottaBricks"],
        ],
        "chapter": "Decorations",
        "position": [5, 1],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Press",
        "label_parts": [["Press", "machines"]],
        "required": [],
        "levels": [2, 7],
        "unlocks": [["Hand", "%Material%Press"], ["Constructor", "%Material%Press"]],
        "position": [2, 3],
        "chapter": "Decorations",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "PaintTool",
        "label_parts": [["PaintTool", "parts"]],
        "required": [],
        "levels": [1, 1],
        "unlocks": [["Hand", "CopperPaintTool"], ["Constructor", "CopperPaintTool"]],
        "position": [1, 2],
        "chapter": "Decorations",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Lamp",
        "label_parts": [["Lamp", "machines"]],
        "required": [],
        "levels": [1, 7],
        "unlocks": [["Hand", "%Material%Lamp"], ["Constructor", "%Material%Lamp"]],
        "position": [2, 4],
        "chapter": "Decorations",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Column",
        "label_parts": [["Column", "misc"]],
        "required": [],
        "levels": [1, 1],
        "unlocks": [
            ["Hand", "Column"],
            ["Hand", "FluetedColumn"],
            ["Press", "Column"],
            ["Press", "FluetedColumn"],
        ],
        "position": [1, 4],
        "chapter": "Decorations",
    }
)
append_levels(
    {
        "class": static_research,
        "name": "Sign",
        "label_parts": [["Sign", "machines"]],
        "required": ["MineralsScan"],
        "unlocks": [["Hand", "%Material%Sign"], ["Constructor", "%Material%Sign"]],
        "levels": [0, 7],
        "chapter": "Decorations",
        "position": [0, 3],
    }
)
append_levels(
    {
        "class": static_research,
        "name": "AdvancedSign",
        "label_parts": [["AdvancedSign", "machines"]],
        "required": ["Sign"],
        "unlocks": [
            ["Hand", "%Material%AdvancedSign"],
            ["Constructor", "%Material%AdvancedSign"],
        ],
        "levels": [2, 7],
        "chapter": "Decorations",
        "position": [1, 3],
    }
)

data = {"Objects": researches}

write_file("Generated/Researches/basic.json", data)
write_file("Loc/source/researches.json", csv)
