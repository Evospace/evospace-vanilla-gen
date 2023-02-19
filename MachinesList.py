## -*- coding: utf-8 -*-

from Common import *
from Materials import *

machines = [
    {
        "name": "Macerator",
        "Label": "Macerator",
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput"],
    },
    {
        "name": "CuttingMachine",
        "Label": "Cutting Machine",
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput"],
    }
    # ,{
    # 	"name": "RollerMachine",
    # 	"Label": "Roller Machine",
    #
    # 	"StartTier": 2,
    # 	"EndTier": 4,
    # 	"Description": "Unused.",
    # }
    ,
    {
        "name": "Fermenter",
        "Label": "Fermenter",
        "StartTier": 4,
        "EndTier": 10,
        "Positions": [[0, 0, 0], [0, 0, 1]],
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()

		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "required": ["Fermentation"],
        "Description": ["ElectricInput"],
    },
    {
        "name": "ChemReactor",
        "Label": "Chemical Reactor",
        "StartTier": 2,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["ElectricInput"],
    },
    {
        "name": "Separator",
        "Label": "Separator",
        "StartTier": 2,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput"],
    },
    {
        "name": "Beam",
        "Label": "Beam",
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "BlockLogic",
        "tag": "Decoration",
        "Description": ["BuildingBlock"],
    },
    {
        "name": "Corner",
        "Label": "Corner",
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "BlockLogic",
        "tag": "Decoration",
        "Description": ["BuildingBlock"],
    },
    {
        "name": "AutomaticHammer",
        "Label": "Automatic Hammer",
        "Positions": [[0, 0, 0], [0, 0, 1]],
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")

		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput"],
    }
    # ,{
    # 	"name": "Lathe",
    # 	"Label": "Lathe",
    #
    # 	"StartTier": 2,
    # 	"EndTier": 7,
    # 	"Description": "Unused.",
    # }
    ,
    {
        "name": "Boiler",
        "Label": "Boiler",
        "StartTier": 2,
        "EndTier": 10,
        "CommonTextKeys": ["Autocrafter"],
        "BlockLogic": "NuclearReactor",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_input = get_class("HeatInputAccessor")
		fluid_input = get_class("FluidInputAccessor")
		fluid_output = get_class("FluidOutputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(fluid_output)
		a:set_side_pos(Vec3i.up(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["HeatInput", "FluidInput", "FluidOutput", "PowerOutput"],
        "CustomData": {
            "StorageCapacity": 30000,
            "StorageDrain": 0,
        },
        "PowerOutput": 100,
    },
    {
        "name": "Pipe",
        "Label": "Pipe",
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "FluidConductor",
        "tag": "Logistics",
        "Description": ["FluidConductor"],
        "PathFinding": True,
    },
    {
        "name": "HeatPipe",
        "Label": "Heat Pipe",
        "StartTier": 1,
        "EndTier": 1,
        "BlockLogic": "HeatConductor",
        "tag": "Logistics",
        "Description": ["HeatConductor", "HeatStorage"],
        "PathFinding": True,
    },
    {
        "name": "Flywheel",
        "Label": "Flywheel",
        "StartTier": 2,
        "EndTier": 2,
        "BlockLogic": "KineticConductor",
        "tag": "Logistics",
        "Description": ["KineticConductor", "KineticStorage"],
        "PathFinding": True,
    },
    {
        "name": "Scaffold",
        "Label": "Scaffold",
        "StartTier": 1,
        "EndTier": 10,
        "tag": "Decoration",
        "BlockLogic": "BlockLogic",
        "Description": ["BuildingBlock"],
    },
    {
        "name": "Sign",
        "Label": "Sign",
        "tag": "Decoration",
        "StartTier": 0,
        "EndTier": 10,
        "BlockLogic": "Sign",
    },
    {
        "name": "AdvancedSign",
        "Label": "Advanced Sign",
        "tag": "Decoration",
        "StartTier": 2,
        "EndTier": 10,
        "BlockLogic": "Sign",
    },
    {
        "name": "Connector",
        "Label": "Cable",
        "StartTier": 1,
        "EndTier": 1,
        "BlockLogic": "ElectricConductor",
        "tag": "Logistics",
        "PathFinding": True,
    },
    {
        "name": "Chest",
        "Label": "Chest",
        "StartTier": 0,
        "EndTier": 10,
        "tag": "Logistics",
    },
    {
        "name": "ItemRack",
        "Label": "Item Rack",
        "Positions": [[0, 0, 0], [-1, 0, 0], [0, 0, 1], [-1, 0, 1]],
        "StartTier": 1,
        "EndTier": 10,
        "tag": "Logistics",
    },
    {
        "name": "Vent",
        "Label": "Valve",
        "StartTier": 1,
        "EndTier": 1,
        "CommonTextKeys": ["Valve"],
        "BlockLogic": "FluidSwitch",
        "tag": "Logistics",
        "Description": ["FluidConductor"],
    },
    {
        "name": "ElectricalSwitch",
        "Label": "Switch",
        "StartTier": 2,
        "EndTier": 2,
        "BlockLogic": "ElectricSwitch",
        "tag": "Logistics",
        "Description": ["ElectricConductor"],
    },
    {
        "name": "OreWasher",
        "Label": "Ore Washer",
        "Positions": [
            [0, 0, 0],
            [0, 1, 0],
            [-1, 0, 0],
            [-1, 1, 0],
            [-2, 0, 0],
            [-2, 1, 0],
            [0, 0, 1],
            [0, 1, 1],
            [-1, 0, 1],
            [-1, 1, 1],
            [-2, 0, 1],
            [-2, 1, 1],
        ],
        "StartTier": 2,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0,1,0))
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput"],
    },
    {
        "name": "Conveyor",
        "Label": "Conveyor",
        "StartTier": 1,
        "EndTier": 10,
        "CommonTextKeys": ["Conveyor", "Transporter"],
        "Selector": "/Game/Blocks/ArrowConvBP.ArrowConvBP_C",
        "tag": "Logistics",
        "PathFinding": True,
    },
    {
        "name": "Splitter",
        "Label": "Splitter",
        "StartTier": 1,
        "EndTier": 10,
        "Description": ["Splitter"],
        "tag": "Logistics",
    },
    {
        "name": "Sorter",
        "Label": "Sorter",
        "StartTier": 2,
        "EndTier": 10,
        "Description": ["Splitter", "Sorter"],
        "tag": "Logistics",
    },
    {
        "name": "Container",
        "Label": "Container",
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "FluidContainer",
        "tag": "Logistics",
        "Description": ["FluidConductor", "FluidStorage"],
    },
    {
        "name": "Press",
        "Label": "Press",
        "StartTier": 2,
        "EndTier": 10,
        "CommonTextKeys": ["Press", "Autocrafter"],
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
    }
    # ,{
    # 	"name": "Compressor",
    # 	"Label": "Compressor",
    # 	"StartTier": 2,
    # 	"EndTier": 10,
    # 	"CommonTextKeys":[
    # 		"Autocrafter"
    # 	],
    # 	"BlockLogic":"SelectCrafter",
    # 	"BlockCreation":"""
    # 	local crafter = current_block_logic()
    #
    # 	local a = crafter:create_accessor(ElectricInputAccessor))
    # 	a:set_side_pos(Vec3i.left(), Vec3i.zero())
    # 	a:bind(crafter:get_input_container())
    #
    # 	local a = crafter:create_accessor(FluidOutputAccessor))
    # 	a:set_side_pos(Vec3i.right(), Vec3i.zero())
    # 	a:bind(crafter:get_output_container())
    # 	""",
    #
    # }
    ,
    {
        "name": "StirlingEngine",
        "Label": "Stirling Engine",
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_input = get_class("HeatInputAccessor")
		kinetic_output = get_class("KineticOutputAccessor")
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(kinetic_output)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		""",
        "Description": ["HeatInput", "KineticOutput", "PowerOutput"],
        "PowerOutput": 10,
    },
    {
        "name": "CombustionEngine",
        "Label": "Combustion Engine",
        "StartTier": 2,
        "EndTier": 10,
        "Description": ["FluidInput", "KineticOutput"],
    },
    {
        "name": "PyrolysisUnit",
        "Label": "Pyrolysis Unit",
        "Positions": [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 2, 0]],
        "StartTier": 3,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_input = get_class("HeatInputAccessor")
		heat_output = get_class("HeatOutputAccessor")
		kinetic_input = get_class("KineticInputAccessor")
		kinetic_output = get_class("KineticOutputAccessor")
		electric_input = get_class("ElectricInputAccessor")
		electric_output = get_class("ElectricOutputAccessor")
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.new( 0, 0, 0 ))
		a:bind(crafter:get_input_container())
		""",
        "Description": ["HeatInput"],
    },
    {
        "name": "Generator",
        "Label": "Generator",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
        ],
        "StartTier": 2,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		electric_output = get_class("ElectricOutputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.new( -1, 1, 0 ))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(electric_output)
		a:set_side_pos(Vec3i.front(), Vec3i.new( 0, 0, 0 ))
		a:bind(crafter:get_output_container())
		""",
        "Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
        "PowerOutput": 243,
    },
    {
        "name": "CompactGenerator",
        "Label": "Compact Generator",
        "StartTier": 1,
        "EndTier": 1,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		electric_output = get_class("ElectricOutputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(electric_output)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		""",
        "Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
        "PowerOutput": 18,
    },
    {
        "name": "ElectricEngine",
        "Label": "Electric Engine",
        "StartTier": 2,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_output = get_class("KineticOutputAccessor")
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(kinetic_output)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.down(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["ElectricInput", "KineticOutput", "PowerOutput"],
        "PowerOutput": 55,
    },
    {
        "name": "IndustrialElectricEngine",
        "Label": "Industrial Electric Engine",
        "StartTier": 4,
        "EndTier": 10,
        "Positions": [
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
            [1, 1, 0],
            [0, 0, 1],
            [1, 0, 1],
            [0, 1, 1],
            [1, 1, 1],
        ],
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_output = get_class("KineticOutputAccessor")
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(kinetic_output)
		a:set_side_pos(Vec3i.front(), Vec3i.new(1,0,0))
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.down(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.right(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["ElectricInput", "KineticOutput", "PowerOutput"],
        "PowerOutput": 55 * 50,
    },
    {
        "name": "RobotArm",
        "Label": "Robot Arm",
        "StartTier": 1,
        "EndTier": 10,
        "Selector": "/Game/Blocks/ArrowBP.ArrowBP_C",
        "tag": "Logistics",
    },
    {
        "name": "FilteringRobotArm",
        "Label": "Filtering Robot Arm",
        "StartTier": 1,
        "EndTier": 10,
        "Selector": "/Game/Blocks/ArrowBP.ArrowBP_C",
        "tag": "Logistics",
        "Description": ["Sorter"],
    },
    {
        "name": "Pump",
        "Label": "Pump",
        "StartTier": 1,
        "EndTier": 10,
        "CustomData": {"ItemPortion": 1000},
        "tag": "Logistics",
        "Selector": "/Game/Blocks/ArrowBP.ArrowBP_C",
        "Description": ["FluidInput", "FluidOutput"],
    },
    {
        "name": "FilteringPump",
        "Label": "Filtering Pump",
        "StartTier": 1,
        "EndTier": 10,
        "CustomData": {"ItemPortion": 1000},
        "tag": "Logistics",
        "Selector": "/Game/Blocks/ArrowBP.ArrowBP_C",
        "Description": ["Sorter", "FluidInput", "FluidOutput"],
    },
    {
        "name": "Smelter",
        "Label": "Smelter",
        "StartTier": 0,
        "EndTier": 2,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_input = get_class("HeatInputAccessor")
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["HeatInput"],
        "CustomData": {"Capacity": 32},
    },
    {
        "name": "SteamTurbine",
        "Label": "Steam Turbine",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
        ],
        "StartTier": 2,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_output = get_class("KineticOutputAccessor")
		fluid_input = get_class("FluidInputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.up(), Vec3i.new(0, 0, 1))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(kinetic_output)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		""",
        "Description": ["FluidInput", "KineticOutput", "PowerOutput"],
        "PowerOutput": 270,
    },
    {
        "name": "IndustrialSteamTurbine",
        "Label": "Industrial Steam Turbine",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [-3, 0, 0],
            [-4, 0, 0],
            [-5, 0, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [-3, -1, 0],
            [-4, -1, 0],
            [-5, -1, 0],
            [0, -2, 0],
            [-1, -2, 0],
            [-2, -2, 0],
            [-3, -2, 0],
            [-4, -2, 0],
            [-5, -2, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [-3, 0, 1],
            [-4, 0, 1],
            [-5, 0, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [-3, -1, 1],
            [-4, -1, 1],
            [-5, -1, 1],
            [0, -2, 1],
            [-1, -2, 1],
            [-2, -2, 1],
            [-3, -2, 1],
            [-4, -2, 1],
            [-5, -2, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [-3, 0, 2],
            [-4, 0, 2],
            [-5, 0, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
            [-3, -1, 2],
            [-4, -1, 2],
            [-5, -1, 2],
            [0, -2, 2],
            [-1, -2, 2],
            [-2, -2, 2],
            [-3, -2, 2],
            [-4, -2, 2],
            [-5, -2, 2],
        ],
        "StartTier": 5,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		fluid_input = get_class("FluidInputAccessor")
		electric_output = get_class("ElectricOutputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0, 0, 0))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(electric_output)
		a:set_side_pos(Vec3i.back(), Vec3i.new(-5, -1, 0))
		a:bind(crafter:get_output_container())
		""",
        "Description": ["FluidInput", "ElectricOutput", "PowerOutput"],
        "PowerOutput": fission_fullpower * 0.9 * 0.9,
    },
    {
        "name": "GasTurbine",
        "Label": "Gas Turbine",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [-3, 0, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [-3, -1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [-3, 0, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [-3, -1, 1],
        ],
        "StartTier": 4,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_input = get_class("HeatInputAccessor")
		heat_output = get_class("HeatOutputAccessor")
		kinetic_input = get_class("KineticInputAccessor")
		kinetic_output = get_class("KineticOutputAccessor")
		electric_input = get_class("ElectricInputAccessor")
		electric_output = get_class("ElectricOutputAccessor")
		fluid_input = get_class("FluidInputAccessor")
		fluid_output = get_class("FluidOutputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.up(), Vec3i.new( -2, 0, 1 ))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.back(), Vec3i.new( -1, -1, 1 ))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(kinetic_output)
		a:set_side_pos(Vec3i.right(), Vec3i.new( -3, -1, 0 ))
		a:bind(crafter:get_output_container())
		""",
        "Description": ["FluidInput", "KineticOutput"],
    },
    {
        "name": "Riteg",
        "Label": "RTG",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [1, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [1, -1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [1, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [1, 1, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [1, -1, 1],
        ],
        "StartTier": 5,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_output = get_class("HeatOutputAccessor")
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.down(), Vec3i.new( 0, 0, 0 ))
		a:bind(crafter:get_output_container())
		
		a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.up(), Vec3i.new( 0, 0, 1 ))
		a:bind(crafter:get_output_container())
		""",
        "Description": ["HeatOutput", "PowerOutput"],
        "PowerOutput": 500,
    },
    {
        "name": "ArcSmelter",
        "Label": "Arc Smelter",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
        ],
        "StartTier": 2,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_input = get_class("HeatInputAccessor")
		heat_output = get_class("HeatOutputAccessor")
		kinetic_input = get_class("KineticInputAccessor")
		kinetic_output = get_class("KineticOutputAccessor")
		electric_input = get_class("ElectricInputAccessor")
		electric_output = get_class("ElectricOutputAccessor")
		fluid_input = get_class("FluidInputAccessor")
		fluid_output = get_class("FluidOutputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.back(), Vec3i.new( -1, 1, 0 ))
		a:bind(crafter:get_input_container())
		""",
        "Description": ["ElectricInput"],
    },
    {
        "name": "ChemicalBath",
        "Label": "Chemical Bath",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
        ],
        "StartTier": 3,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new( 0, 0, 0 ))
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput"],
    },
    {
        "name": "Sifter",
        "Label": "Sifter",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
        ],
        "StartTier": 3,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new( 0, 0, 0 ))
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput"],
    },
    {
        "name": "FilteringUnit",
        "Label": "Filtering Unit",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
        ],
        "StartTier": 3,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new( 0, 0, 0 ))
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput"],
    },
    {
        "name": "Furnace",
        "Label": "Furnace",
        "StartTier": 0,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_output = get_class("HeatOutputAccessor")
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.up(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		""",
        "Description": ["HeatOutput"],
    },
    {
        "name": "Oven",
        "Label": "Oven",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [-2, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [-2, 1, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
            [-2, 1, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
        ],
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "Description": ["SpeedBonus"],
    },
    {
        "name": "BlastFurnace",
        "Label": "Blast Furnace",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [-2, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [-2, 1, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
            [-2, 1, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
            [0, 0, 3],
            [-1, 0, 3],
            [-2, 0, 3],
            [0, 1, 3],
            [-1, 1, 3],
            [-2, 1, 3],
            [0, -1, 3],
            [-1, -1, 3],
            [-2, -1, 3],
        ],
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "Description": ["SpeedBonus"],
    },
    {
        "name": "FluidFurnace",
        "Label": "Fluid Furnace",
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_output = get_class("HeatOutputAccessor")
		fluid_input = get_class("FluidInputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.up(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		""",
        "Description": ["FluidInput", "HeatOutput"],
    },
    {
        "name": "ElectricFurnace",
        "Label": "Electric Furnace",
        "StartTier": 2,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_output = get_class("HeatOutputAccessor")
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.up(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		""",
        "Description": ["ElectricInput", "HeatOutput", "PowerOutput"],
        "PowerOutput": 40,
    },
    {
        "name": "BatteryBox",
        "Label": "Battery Box",
        "StartTier": 4,
        "EndTier": 10,
        "Description": ["ElectricConductor", "ElectricStorage"],
        "CustomData": {
            "BaseCapacity": 1000000,
            "BonusCapacity": 1000000,
        },
    },
    {
        "name": "SmallBattery",
        "Label": "Small Battery",
        "StartTier": 3,
        "EndTier": 10,
        "Description": ["ElectricConductor", "ElectricStorage"],
        "BlockLogic": "BatteryBox",
        "CustomData": {
            "BaseCapacity": 100000,
            "BonusCapacity": 100000,
        },
    },
    {
        "name": "Portal",
        "Label": "Portal",
        "StartTier": 7,
        "EndTier": 10,
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [-3, 0, 0],
            [-4, 0, 0],
            [-5, 0, 0],
            [-6, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [-2, 1, 0],
            [-3, 1, 0],
            [-4, 1, 0],
            [-5, 1, 0],
            [-6, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [-3, -1, 0],
            [-4, -1, 0],
            [-5, -1, 0],
            [-6, -1, 0],
            [0, -2, 0],
            [-1, -2, 0],
            [-2, -2, 0],
            [-3, -2, 0],
            [-4, -2, 0],
            [-5, -2, 0],
            [-6, -2, 0],
            [0, -3, 0],
            [-1, -3, 0],
            [-2, -3, 0],
            [-3, -3, 0],
            [-4, -3, 0],
            [-5, -3, 0],
            [-6, -3, 0],
            [0, -4, 0],
            [-1, -4, 0],
            [-2, -4, 0],
            [-3, -4, 0],
            [-4, -4, 0],
            [-5, -4, 0],
            [-6, -4, 0],
            [0, -5, 0],
            [-1, -5, 0],
            [-2, -5, 0],
            [-3, -5, 0],
            [-4, -5, 0],
            [-5, -5, 0],
            [-6, -5, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [-3, 0, 1],
            [-4, 0, 1],
            [-5, 0, 1],
            [-6, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [-2, 1, 1],
            [-3, 1, 1],
            [-4, 1, 1],
            [-5, 1, 1],
            [-6, 1, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [-3, -1, 1],
            [-4, -1, 1],
            [-5, -1, 1],
            [-6, -1, 1],
            [0, -2, 1],
            [-1, -2, 1],
            [-2, -2, 1],
            [-3, -2, 1],
            [-4, -2, 1],
            [-5, -2, 1],
            [-6, -2, 1],
            [0, -3, 1],
            [-1, -3, 1],
            [-2, -3, 1],
            [-3, -3, 1],
            [-4, -3, 1],
            [-5, -3, 1],
            [-6, -3, 1],
            [0, -4, 1],
            [-1, -4, 1],
            [-2, -4, 1],
            [-3, -4, 1],
            [-4, -4, 1],
            [-5, -4, 1],
            [-6, -4, 1],
            [0, -5, 1],
            [-1, -5, 1],
            [-2, -5, 1],
            [-3, -5, 1],
            [-4, -5, 1],
            [-5, -5, 1],
            [-6, -5, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [-3, 0, 2],
            [-4, 0, 2],
            [-5, 0, 2],
            [-6, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
            [-2, 1, 2],
            [-3, 1, 2],
            [-4, 1, 2],
            [-5, 1, 2],
            [-6, 1, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
            [-3, -1, 2],
            [-4, -1, 2],
            [-5, -1, 2],
            [-6, -1, 2],
            [0, -2, 2],
            [-1, -2, 2],
            [-2, -2, 2],
            [-3, -2, 2],
            [-4, -2, 2],
            [-5, -2, 2],
            [-6, -2, 2],
            [0, -3, 2],
            [-1, -3, 2],
            [-2, -3, 2],
            [-3, -3, 2],
            [-4, -3, 2],
            [-5, -3, 2],
            [-6, -3, 2],
            [0, -4, 2],
            [-1, -4, 2],
            [-2, -4, 2],
            [-3, -4, 2],
            [-4, -4, 2],
            [-5, -4, 2],
            [-6, -4, 2],
            [0, -5, 2],
            [-1, -5, 2],
            [-2, -5, 2],
            [-3, -5, 2],
            [-4, -5, 2],
            [-5, -5, 2],
            [-6, -5, 2],
            [0, 0, 3],
            [-1, 0, 3],
            [-2, 0, 3],
            [-3, 0, 3],
            [-4, 0, 3],
            [-5, 0, 3],
            [-6, 0, 3],
            [0, 1, 3],
            [-1, 1, 3],
            [-2, 1, 3],
            [-3, 1, 3],
            [-4, 1, 3],
            [-5, 1, 3],
            [-6, 1, 3],
            [0, -1, 3],
            [-1, -1, 3],
            [-2, -1, 3],
            [-3, -1, 3],
            [-4, -1, 3],
            [-5, -1, 3],
            [-6, -1, 3],
            [0, -2, 3],
            [-1, -2, 3],
            [-2, -2, 3],
            [-3, -2, 3],
            [-4, -2, 3],
            [-5, -2, 3],
            [-6, -2, 3],
            [0, -3, 3],
            [-1, -3, 3],
            [-2, -3, 3],
            [-3, -3, 3],
            [-4, -3, 3],
            [-5, -3, 3],
            [-6, -3, 3],
            [0, -4, 3],
            [-1, -4, 3],
            [-2, -4, 3],
            [-3, -4, 3],
            [-4, -4, 3],
            [-5, -4, 3],
            [-6, -4, 3],
            [0, -5, 3],
            [-1, -5, 3],
            [-2, -5, 3],
            [-3, -5, 3],
            [-4, -5, 3],
            [-5, -5, 3],
            [-6, -5, 3],
            [0, 0, 3],
            [-1, 0, 3],
            [-2, 0, 3],
            [-3, 0, 3],
            [-4, 0, 3],
            [-5, 0, 3],
            [-6, 0, 4],
            [0, 1, 3],
            [-1, 1, 3],
            [-2, 1, 3],
            [-3, 1, 3],
            [-4, 1, 3],
            [-5, 1, 3],
            [-6, 1, 4],
            [0, -1, 3],
            [-1, -1, 3],
            [-2, -1, 3],
            [-3, -1, 3],
            [-4, -1, 3],
            [-5, -1, 3],
            [-6, -1, 4],
            [0, -2, 3],
            [-1, -2, 3],
            [-2, -2, 3],
            [-3, -2, 3],
            [-4, -2, 3],
            [-5, -2, 3],
            [-6, -2, 4],
            [0, -3, 3],
            [-1, -3, 3],
            [-2, -3, 3],
            [-3, -3, 3],
            [-4, -3, 3],
            [-5, -3, 3],
            [-6, -3, 4],
            [0, -4, 3],
            [-1, -4, 3],
            [-2, -4, 3],
            [-3, -4, 3],
            [-4, -4, 3],
            [-5, -4, 3],
            [-6, -4, 4],
            [0, -5, 3],
            [-1, -5, 3],
            [-2, -5, 3],
            [-3, -5, 3],
            [-4, -5, 3],
            [-5, -5, 3],
            [-6, -5, 4],
        ],
        "BlockCreation": """
		local crafter = current_block_logic()
		
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0,1,1))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.left(), Vec3i.new(0,1,1))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0,-5,1))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.right(), Vec3i.new(0,-5,1))
		a:bind(crafter:get_input_container())
		""",
    },
    # {
    # 	"name": "MoltenSaltBattery",
    # 	"Label": "Molten Salt Battery",
    # 	"StartTier": 5,
    # 	"EndTier": 10,
    # 	"BlockLogic": "HighcapElectricBattery",
    # }
    {
        "name": "DrillingRig",
        "Label": "Drilling Rig",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [-2, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [-2, 1, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
            [-2, 1, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
            [0, 0, 3],
            [-1, 0, 3],
            [-2, 0, 3],
            [0, 1, 3],
            [-1, 1, 3],
            [-2, 1, 3],
            [0, -1, 3],
            [-1, -1, 3],
            [-2, -1, 3],
            [0, 0, 4],
            [-1, 0, 4],
            [-2, 0, 4],
            [0, 1, 4],
            [-1, 1, 4],
            [-2, 1, 4],
            [0, -1, 4],
            [-1, -1, 4],
            [-2, -1, 4],
        ],
        "StartTier": 1,
        "EndTier": 10,
        "Description": ["KineticInput", "ItemOutput"],
    },
    {
        "name": "Assembler",
        "Label": "Assembler",
        "StartTier": 1,
        "EndTier": 10,
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [0, -1, 0],
            [-1, -1, 0],
            [0, -1, 1],
            [-1, -1, 1],
        ],
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["ElectricInput"],
    },
    {
        "name": "Constructor",
        "Label": "Constructor",
        "StartTier": 2,
        "EndTier": 10,
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [0, -1, 0],
            [-1, -1, 0],
            [0, -1, 1],
            [-1, -1, 1],
        ],
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["ElectricInput"],
    },
    {
        "name": "Deconstructor",
        "Label": "Deconstructor",
        "StartTier": 2,
        "EndTier": 10,
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [0, -1, 0],
            [-1, -1, 0],
            [0, -1, 1],
            [-1, -1, 1],
        ],
        "BlockLogic": "DeconstructorCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["ElectricInput"],
    },
    {
        "name": "FluidDump",
        "Label": "Fluid Dump",
        "Positions": [
            [0, 0, 0],
            [0, -1, 0],
            [0, -2, 0],
            [0, 1, 0],
            [0, 2, 0],
            [-1, 0, 0],
            [-1, -1, 0],
            [-1, -2, 0],
            [-1, 1, 0],
            [-1, 2, 0],
            [-2, 0, 0],
            [-2, -1, 0],
            [-2, -2, 0],
            [-2, 1, 0],
            [-2, 2, 0],
            [-3, 0, 0],
            [-3, -1, 0],
            [-3, -2, 0],
            [-3, 1, 0],
            [-3, 2, 0],
            [-4, 0, 0],
            [-4, -1, 0],
            [-4, -2, 0],
            [-4, 1, 0],
            [-4, 2, 0],
        ],
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		fluid_input = get_class("FluidInputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["FluidInput"],
    },
    {
        "name": "GasDump",
        "Label": "Gas Dump",
        "Positions": [[0, 0, 0]],
        "StartTier": 2,
        "EndTier": 2,
        "BlockLogic": "DumpCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()

		fluid_input = get_class("FluidInputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.down(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["FluidInput"],
    },
    {
        "name": "SolidDump",
        "Label": "Solid Dump",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [0, -1, 0],
            [-1, -1, 0],
        ],
        "StartTier": 2,
        "EndTier": 2,
        "BlockLogic": "DumpAny",
        "Description": ["SolidInput"],
    },
    # ,{
    # 	"name": "Liquifier",
    # 	"Label": "Liquifier",
    # 	"StartTier": 2,
    # 	"EndTier": 3,
    # 	"Description": ""
    # }
    {
        "name": "Lamp",
        "Label": "Lamp",
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "Lamp",
    },
    {
        "name": "AdminElectricGenerator",
        "Label": "Creative Electric Generator",
        "StartTier": 7,
        "EndTier": 7,
        "craftable": False,
        "Description": ["ElectricOutput"],
    },
    {
        "name": "AdminItemGenerator",
        "Label": "Creative Item Generator",
        "StartTier": 7,
        "EndTier": 7,
        "craftable": False,
        "Description": ["ItemOutput"],
    },
    {
        "name": "AdminKineticGenerator",
        "Label": "Creative Kinetic Generator",
        "StartTier": 7,
        "EndTier": 7,
        "craftable": False,
        "Description": ["KineticOutput"],
    },
    {
        "name": "AdminHeatGenerator",
        "Label": "Creative Heat Generator",
        "StartTier": 7,
        "EndTier": 7,
        "craftable": False,
        "Description": ["HeatOutput"],
    },
    {
        "name": "AdminFluidGenerator",
        "Label": "Creative Fluid Generator",
        "StartTier": 7,
        "EndTier": 7,
        "craftable": False,
        "Description": ["FluidOutput"],
    },
    {
        "name": "AdminExterminator",
        "Label": "Creative Exterminator",
        "StartTier": 7,
        "EndTier": 7,
        "craftable": False,
        "Description": [
            "KineticInput",
            "HeatInput",
            "FluidInput",
            "ItemInput",
            "KineticInput",
        ],
    },
    {
        "name": "Electrolyzer",
        "Label": "Electrolyzer",
        "StartTier": 2,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["ElectricInput"],
    },
    {
        "name": "Mixer",
        "Label": "Mixer",
        "StartTier": 2,
        "EndTier": 10,
        "Positions": [[0, 0, 0], [-1, 0, 0], [0, 0, 1], [-1, 0, 1]],
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.new(-1,0,0))
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput"],
    },
    {
        "name": "Freezer",
        "Label": "Freezer",
        "StartTier": 5,
        "EndTier": 10,
        "Positions": [[0, 0, 0], [-1, 0, 0], [0, 0, 1], [-1, 0, 1]],
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.left(), Vec3i.new(-1,0,0))
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput", "HeatOutput"],
    },
    {
        "name": "AutomaticFarm",
        "Label": "Automatic Farm",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [-3, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [-2, 1, 0],
            [-3, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [-3, -1, 0],
            [0, -2, 0],
            [-1, -2, 0],
            [-2, -2, 0],
            [-3, -2, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [-3, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [-2, 1, 1],
            [-3, 1, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [-3, -1, 1],
            [0, -2, 1],
            [-1, -2, 1],
            [-2, -2, 1],
            [-3, -2, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [-3, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
            [-2, 1, 2],
            [-3, 1, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
            [-3, -1, 2],
            [0, -2, 2],
            [-1, -2, 2],
            [-2, -2, 2],
            [-3, -2, 2],
        ],
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		fluid_input = get_class("FluidInputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0,0,0))
		a:bind(crafter:get_input_container())
		""",
        "Description": ["FluidInput"],
    },
    {
        "name": "AtmosphericCondenser",
        "Label": "Atmospheric Condenser",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [0, -2, 0],
            [-1, -2, 0],
            [-2, -2, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [0, -2, 1],
            [-1, -2, 1],
            [-2, -2, 1],
        ],
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		local a = crafter:create_accessor(get_class("FluidOutputAccessor"))
		a:set_side_pos(Vec3i.front(), Vec3i.new(0,0,0))
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(get_class("KineticInputAccessor"))
		a:set_side_pos(Vec3i.right(), Vec3i.new(-1,-2,0))
		a:bind(crafter:get_input_container())
		""",
        "Description": ["KineticInput", "FluidOutput"],
    },
    {
        "name": "Terminal",
        "Label": "Terminal",
        "StartTier": 4,
        "EndTier": 4,
        "BlockLogic": "Monitor",
    },
    {
        "name": "BigTerminal",
        "Label": "Big Terminal",
        "StartTier": 5,
        "EndTier": 5,
        "image": "Terminal",
        "Positions": [[0, 0, 0], [0, -1, 0], [0, 0, 1], [0, -1, 1]],
        "BlockLogic": "Monitor",
    },
    {
        "name": "HugeTerminal",
        "Label": "Huge Terminal",
        "StartTier": 6,
        "EndTier": 6,
        "image": "Terminal",
        "Positions": [
            [0, 0, 0],
            [0, -1, 0],
            [0, -2, 0],
            [0, 0, 1],
            [0, -1, 1],
            [0, -2, 1],
            [0, 0, 2],
            [0, -1, 2],
            [0, -2, 2],
        ],
        "BlockLogic": "Monitor",
    },
    {
        "name": "FlatTerminal",
        "Label": "Flat Terminal",
        "StartTier": 4,
        "EndTier": 4,
        "BlockLogic": "Monitor",
    },
    {
        "name": "BigFlatTerminal",
        "Label": "Big Flat Terminal",
        "StartTier": 5,
        "EndTier": 5,
        "image": "FlatTerminal",
        "Positions": [[0, 0, 0], [0, -1, 0], [0, 0, 1], [0, -1, 1]],
        "BlockLogic": "Monitor",
    },
    {
        "name": "HugeFlatTerminal",
        "Label": "Huge Flat Terminal",
        "StartTier": 6,
        "EndTier": 6,
        "image": "FlatTerminal",
        "Positions": [
            [0, 0, 0],
            [0, -1, 0],
            [0, -2, 0],
            [0, 0, 1],
            [0, -1, 1],
            [0, -2, 1],
            [0, 0, 2],
            [0, -1, 2],
            [0, -2, 2],
        ],
        "BlockLogic": "Monitor",
    },
    {
        "name": "Computer",
        "Label": "Computer",
        "StartTier": 1,
        "EndTier": 10,
        "BlockLogic": "Computer",
        "Description": ["ElectricInput"],
    },
    {
        "name": "QuantumComputer",
        "Label": "Quantum Computer",
        "StartTier": 5,
        "EndTier": 10,
        "BlockLogic": "QuantumComputer",
        "Description": ["ElectricInput"],
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [0, -2, 0],
            [-1, -2, 0],
            [-2, -2, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [0, -2, 1],
            [-1, -2, 1],
            [-2, -2, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [0, -2, 2],
            [-1, -2, 2],
            [-2, -2, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
        ],
    },
    {
        "name": "IndustrialSeparator",
        "Label": "Industrial Separator",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [0, 1, 1],
            [-1, 1, 1],
        ],
        "StartTier": 3,
        "EndTier": 10,
        "CommonTextKeys": ["Separator", "Autocrafter"],
        "BlockLogic": "AutoCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		local a = crafter:create_accessor(get_class("KineticInputAccessor"))
		a:set_side_pos(Vec3i.back(), Vec3i.new(-1,1,0))
		a:bind(crafter:get_input_container())
		print('123123')
		""",
        "Description": ["KineticInput"],
    },
    {
        "name": "Radiator",
        "Label": "Radiator",
        "StartTier": 3,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		local a = crafter:create_accessor(get_class("HeatInputAccessor"))
		a:set_side_pos(Vec3i.down(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
        "Description": ["HeatInput"],
    },
    {
        "name": "Diode",
        "Label": "Diode",
        "StartTier": 2,
        "EndTier": 10,
        "Description": ["ElectricInput", "ElectricOutput"],
    },
    # ,{
    # 	"name": "Tank",
    # 	"Label": "Tank",
    # 	"Positions": [
    # 		[0,0,0],[-1,0,0],[-2,0,0],
    # 		[0,1,0],[-1,1,0],[-2,1,0],
    # 		[0,-1,0],[-1,-1,0],[-2,-1,0],
    #
    # 		[0,0,1],[-1,0,1],[-2,0,1],
    # 		[0,1,1],[-1,1,1],[-2,1,1],
    # 		[0,-1,1],[-1,-1,1],[-2,-1,1],
    #
    # 		[0,0,2],[-1,0,2],[-2,0,2],
    # 		[0,1,2],[-1,1,2],[-2,1,2],
    # 		[0,-1,2],[-1,-1,2],[-2,-1,2],
    # 	],
    # 	"StartTier": 1,
    # 	"EndTier": 10,
    # 	"CommonTextKeys":[
    # 		"Container"
    # 	],
    # 	"required":["LiquidsScan"],
    # },
    {
        "name": "FissionReactor",
        "Label": "Fission Reactor",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [-3, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [-2, 1, 0],
            [-3, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [-3, -1, 0],
            [0, -2, 0],
            [-1, -2, 0],
            [-2, -2, 0],
            [-3, -2, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [-3, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [-2, 1, 1],
            [-3, 1, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [-3, -1, 1],
            [0, -2, 1],
            [-1, -2, 1],
            [-2, -2, 1],
            [-3, -2, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [-3, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
            [-2, 1, 2],
            [-3, 1, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
            [-3, -1, 2],
            [0, -2, 2],
            [-1, -2, 2],
            [-2, -2, 2],
            [-3, -2, 2],
            [0, 0, 3],
            [-1, 0, 3],
            [-2, 0, 3],
            [-3, 0, 3],
            [0, 1, 3],
            [-1, 1, 3],
            [-2, 1, 3],
            [-3, 1, 3],
            [0, -1, 3],
            [-1, -1, 3],
            [-2, -1, 3],
            [-3, -1, 3],
            [0, -2, 3],
            [-1, -2, 3],
            [-2, -2, 3],
            [-3, -2, 3],
            [0, 0, 4],
            [-1, 0, 4],
            [-2, 0, 4],
            [-3, 0, 4],
            [0, 1, 4],
            [-1, 1, 4],
            [-2, 1, 4],
            [-3, 1, 4],
            [0, -1, 4],
            [-1, -1, 4],
            [-2, -1, 4],
            [-3, -1, 4],
            [0, -2, 4],
            [-1, -2, 4],
            [-2, -2, 4],
            [-3, -2, 4],
        ],
        "StartTier": 5,
        "EndTier": 10,
        "BlockLogic": "NuclearReactor",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_output = get_class("HeatOutputAccessor")
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.left(), Vec3i.new(0, 1, 0))
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0, 1, 0))
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0, -2, 0))
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.right(), Vec3i.new(0, -2, 0))
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.left(), Vec3i.new(-3, 1, 0)) 
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.back(), Vec3i.new(-3, 1, 0))
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.back(), Vec3i.new(-3, -2, 0))
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.right(), Vec3i.new(-3, -2, 0))
		a:bind(crafter:get_output_container())
		""",
        "CustomData": {
            "LoadIndependent": True,
            "StorageCapacity": 10000000,
            "StorageDrain": 80,
        },
        "Description": ["HeatOutput"],
    },
    {
        "name": "FusionReactor",
        "Label": "Fusion Reactor",
        "StartTier": 6,
        "EndTier": 10,
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [-3, 0, 0],
            [-4, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [-2, 1, 0],
            [-3, 1, 0],
            [-4, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [-3, -1, 0],
            [-4, -1, 0],
            [0, -2, 0],
            [-1, -2, 0],
            [-2, -2, 0],
            [-3, -2, 0],
            [-4, -2, 0],
            [0, -3, 0],
            [-1, -3, 0],
            [-2, -3, 0],
            [-3, -3, 0],
            [-4, -3, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [-3, 0, 1],
            [-4, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [-2, 1, 1],
            [-3, 1, 1],
            [-4, 1, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [-3, -1, 1],
            [-4, -1, 1],
            [0, -2, 1],
            [-1, -2, 1],
            [-2, -2, 1],
            [-3, -2, 1],
            [-4, -2, 1],
            [0, -3, 1],
            [-1, -3, 1],
            [-2, -3, 1],
            [-3, -3, 1],
            [-4, -3, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [-3, 0, 2],
            [-4, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
            [-2, 1, 2],
            [-3, 1, 2],
            [-4, 1, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
            [-3, -1, 2],
            [-4, -1, 2],
            [0, -2, 2],
            [-1, -2, 2],
            [-2, -2, 2],
            [-3, -2, 2],
            [-4, -2, 2],
            [0, -3, 2],
            [-1, -3, 2],
            [-2, -3, 2],
            [-3, -3, 2],
            [-4, -3, 2],
            [0, 0, 3],
            [-1, 0, 3],
            [-2, 0, 3],
            [-3, 0, 3],
            [-4, 0, 3],
            [0, 1, 3],
            [-1, 1, 3],
            [-2, 1, 3],
            [-3, 1, 3],
            [-4, 1, 3],
            [0, -1, 3],
            [-1, -1, 3],
            [-2, -1, 3],
            [-3, -1, 3],
            [-4, -1, 3],
            [0, -2, 3],
            [-1, -2, 3],
            [-2, -2, 3],
            [-3, -2, 3],
            [-4, -2, 3],
            [0, -3, 3],
            [-1, -3, 3],
            [-2, -3, 3],
            [-3, -3, 3],
            [-4, -3, 3],
        ],
        "BlockLogic": "FusionReactor",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0, 1, 0))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.left(), Vec3i.new(0, 1, 0))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0, -3, 0))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.right(), Vec3i.new(0, -3, 0))
		a:bind(crafter:get_input_container())
		""",
    },
    {
        "name": "IndustrialBoiler",
        "Label": "Industrial Boiler",
        "StartTier": 5,
        "EndTier": 10,
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [-3, 0, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [-3, -1, 0],
            [0, -2, 0],
            [-1, -2, 0],
            [-2, -2, 0],
            [-3, -2, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [-3, 0, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [-3, -1, 1],
            [0, -2, 1],
            [-1, -2, 1],
            [-2, -2, 1],
            [-3, -2, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [-3, 0, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
            [-3, -1, 2],
            [0, -2, 2],
            [-1, -2, 2],
            [-2, -2, 2],
            [-3, -2, 2],
        ],
        "BlockLogic": "NuclearReactor",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_input = get_class("HeatInputAccessor")
		heat_output = get_class("HeatOutputAccessor")
		kinetic_input = get_class("KineticInputAccessor")
		kinetic_output = get_class("KineticOutputAccessor")
		electric_input = get_class("ElectricInputAccessor")
		electric_output = get_class("ElectricOutputAccessor")
		fluid_input = get_class("FluidInputAccessor")
		fluid_output = get_class("FluidOutputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0, 0, 0))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.new(0, -1, 0))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.new(-1, -1, 0))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.new(-2, -1, 0))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.new(-3, -1, 0))
		a:bind(crafter:get_input_container())
		
		a = crafter:create_accessor(fluid_output)
		a:set_side_pos(Vec3i.back(), Vec3i.new(-3, 0, 0))
		a:bind(crafter:get_output_container())
		""",
        "Description": ["FluidInput", "FluidOutput", "PowerOutput"],
        "PowerOutput": fission_fullpower * 0.9,
        "CustomData": {"StorageCapacity": 6000000, "StorageDrain": 0},
    },
    {
        "name": "SolarPanel",
        "Label": "Solar Panel",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [1, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [1, -1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [1, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [1, 1, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [1, -1, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [1, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
            [1, 1, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [1, -1, 2],
        ],
        "StartTier": 3,
        "EndTier": 10,
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		

		electric_output = get_class("ElectricOutputAccessor")
		
		local a = crafter:create_accessor(electric_output)
		a:set_side_pos(Vec3i.down(), Vec3i.new(0,0,0))
		a:bind(crafter:get_output_container())
		""",
        "Description": ["ElectricOutput", "PowerOutput"],
        "PowerOutput": 50,
    },
    {
        "name": "Pumpjack",
        "Label": "Pumpjack",
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [-3, 0, 0],
            [-4, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [-2, 1, 0],
            [-3, 1, 0],
            [-4, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [-3, -1, 0],
            [-4, -1, 0],
            [0, 0, 1],
            [-1, 0, 1],
            [-2, 0, 1],
            [-3, 0, 1],
            [-4, 0, 1],
            [0, 1, 1],
            [-1, 1, 1],
            [-2, 1, 1],
            [-3, 1, 1],
            [-4, 1, 1],
            [0, -1, 1],
            [-1, -1, 1],
            [-2, -1, 1],
            [-3, -1, 1],
            [-4, -1, 1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [-3, 0, 2],
            [-4, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
            [-2, 1, 2],
            [-3, 1, 2],
            [-4, 1, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
            [-3, -1, 2],
            [-4, -1, 2],
            [0, 0, 3],
            [-1, 0, 3],
            [-2, 0, 3],
            [-3, 0, 3],
            [-4, 0, 3],
            [0, 1, 3],
            [-1, 1, 3],
            [-2, 1, 3],
            [-3, 1, 3],
            [-4, 1, 3],
            [0, -1, 3],
            [-1, -1, 3],
            [-2, -1, 3],
            [-3, -1, 3],
            [-4, -1, 3],
        ],
        "StartTier": 3,
        "EndTier": 10,
        "Description": ["KineticInput", "FluidOutput"],
    },
    ##,{
    ##	"name": "PneumaticPipe",
    ##	"Label": "Pneumatic Pipe",
    ##	"StartTier": 3,
    ##	"EndTier": 5,
    ##	"CommonTextKeys":[
    ##
    ##	],
    ##
    ##}
    ##,{
    ##	"name": "PneumaticInput",
    ##	"Label": "Pneumatic Input",
    ##	"StartTier": 3,
    ##	"EndTier": 5,
    ##	"CommonTextKeys":[
    ##
    ##	],
    ##
    ##}
    # {
    # 	"name": "DistributionBox",
    # 	"Label": "Distribution Box",
    # 	"StartTier": 2,
    # 	"EndTier": 7,
    # 	"CommonTextKeys":[
    # 		"Chest"
    # 	],
    # },
    # {
    # 	"name": "HeatExchanger",
    # 	"Label": "Heat Exchanger",
    # 	"StartTier": 3,
    # 	"EndTier": 10,
    # 	"BlockLogic":"SelectCrafter",
    # 	"BlockCreation":"""
    # 	local crafter = current_block_logic()
    #
    # 	local a = crafter:create_accessor(FluidInputAccessor))
    # 	a:set_side_pos(Vec3i.left(), Vec3i.zero())
    # 	a:bind(crafter:get_input_container())
    #
    # 	local a = crafter:create_accessor(FluidOutputAccessor))
    # 	a:set_side_pos(Vec3i.right(), Vec3i.zero())
    # 	a:bind(crafter:get_output_container())
    #
    # 	local a = crafter:create_accessor(HeatOutputAccessor))
    # 	a:set_side_pos(Vec3i.up(), Vec3i.zero())
    # 	a:bind(crafter:get_output_container())
    # 	""",
    # 	"required":["HeatTransferring"],
    # }
    # ,{
    # 	"name": "InverseHeatExchanger",
    # 	"Label": "Inverse Heat Exchanger",
    # 	"StartTier": 1,
    # 	"EndTier": 10,
    # 	"BlockLogic":"SelectCrafter",
    # 	"BlockCreation":"""
    # 	local crafter = current_block_logic()
    #
    # 	local a = crafter:create_accessor(FluidInputAccessor))
    # 	a:set_side_pos(Vec3i.left(), Vec3i.zero())
    # 	a:bind(crafter:get_input_container())
    #
    # 	local a = crafter:create_accessor(FluidOutputAccessor))
    # 	a:set_side_pos(Vec3i.right(), Vec3i.zero())
    # 	a:bind(crafter:get_output_container())
    #
    # 	local a = crafter:create_accessor(HeatInputAccessor))
    # 	a:set_side_pos(Vec3i.down(), Vec3i.zero())
    # 	a:bind(crafter:get_input_container())
    # 	""",
    # 	"required":["HeatTransferring"],
    # }
    # ,{
    # 	"name": "IndustrialOven",
    # 	"Label": "Industrial Oven",
    # 	"StartTier": 3,
    # 	"EndTier": 7,
    # 	"CommonTextKeys":[
    # 		"Dryer",
    # 		"CokeOven"
    # 	],
    #
    # 	"Positions": [
    # 		[0,0,0],[-1,0,0],
    # 		[0,1,0],[-1,1,0],
    # 	],
    #
    # }
    {
        "name": "IndustrialSmelter",
        "Label": "Industrial Smelter",
        "StartTier": 4,
        "EndTier": 10,
        "Positions": [
            [0, 0, 0],
            [-1, 0, 0],
            [-2, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [-2, 1, 0],
            [0, -1, 0],
            [-1, -1, 0],
            [-2, -1, 0],
            [-1, 0, 1],  # [0,0,1],[-2,0,1],
            # [0,1,1],[-1,1,1],[-2,1,1],
            # [-1,-1,1],[0,-1,1],[-2,-1,1],
            [0, 0, 2],
            [-1, 0, 2],
            [-2, 0, 2],
            [0, 1, 2],
            [-1, 1, 2],
            [-2, 1, 2],
            [0, -1, 2],
            [-1, -1, 2],
            [-2, -1, 2],
        ],
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		heat_input = get_class("HeatInputAccessor")
		fluid_input = get_class("FluidInputAccessor")
		fluid_output = get_class("FluidOutputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.back(), Vec3i.new(-1,0,2))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.new(0,0,2))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.new(-2,0,2))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.new(-1,1,2))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.new(-1,-1,2))
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(fluid_output)
		a:set_side_pos(Vec3i.back(), Vec3i.new(-2,0,0))
		a:bind(crafter:get_output_container())
		""",
        "Description": ["HeatInput"],
    },
    {
        "name": "InductionCoil",
        "Label": "Induction Coil",
        "StartTier": 4,
        "EndTier": 10,
        "Positions": [
            [0, 0, 0],
            [-2, 0, 0],
            [0, 1, 0],
            [-1, 1, 0],
            [-2, 1, 0],
            [-1, -1, 0],
            [0, -1, 0],
            [-2, -1, 0],
        ],
        "BlockLogic": "SelectCrafter",
        "BlockCreation": """
		local crafter = current_block_logic()
		
		local heat_output = get_class("HeatOutputAccessor")
		local electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_output)
		
		a:set_side_pos(Vec3i.up(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		""",
        "Description": ["ElectricInput", "HeatOutput"],
    },
    {
        "name": "CreativeController",
        "Label": "Creative Controller",
        "StartTier": 7,
        "EndTier": 7,
        "Description": ["DataInput", "DataOutput"],
    },
    {
        "name": "LogicCircuit",
        "Label": "Logic Circuit",
        "StartTier": 2,
        "EndTier": 2,
        "Description": ["DataInput", "DataOutput"],
    },
    {
        "name": "LogicInterface",
        "Label": "Logic Interface",
        "StartTier": 2,
        "EndTier": 2,
        "Description": ["DataOutput"],
    },
    {
        "name": "LogicController",
        "Label": "Logic Controller",
        "StartTier": 2,
        "EndTier": 2,
        "Description": ["DataInput"],
    },
    {
        "name": "LogicDisplay",
        "Label": "Logic Display",
        "StartTier": 2,
        "EndTier": 2,
        "Description": ["DataInput"],
    },
    {
        "name": "LogicWire",
        "Label": "Logic Wire",
        "BlockLogic": "DataConductor",
        "StartTier": 2,
        "EndTier": 2,
        "Description": ["DataConductor"],
    },
    {
        "name": "Button",
        "Label": "Button",
        "StartTier": 2,
        "EndTier": 2,
        "Description": ["DataOutput"],
    },
    {
        "name": "ToggleButton",
        "Label": "Toggle Button",
        "StartTier": 2,
        "EndTier": 2,
        "Description": ["DataOutput"],
    },
]
