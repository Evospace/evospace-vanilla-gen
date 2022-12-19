## -*- coding: utf-8 -*-

from Common import *
from Materials import *

machines = [
	{
		"Name": "Macerator",
		"Label": "Macerator",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "AutoCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "CuttingMachine",
		"Label": "Cutting Machine",
		
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput"],
	}
	#,{
	#	"Name": "RollerMachine",
	#	"Label": "Roller Machine",
	#	
	#	"StartTier": 2,
	#	"EndTier": 4,
	#	"Description": "Unused.",
	#}
	,{
		"Name": "Fermenter",
		"Label": "Fermenter",
		"StartTier": 4,
		"EndTier": 10,
		"Positions": [[0,0,0],[0,0,1]],
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()

		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"RequiredResearches":["Fermentation"],
		"Description": ["ElectricInput"],
	},{
		"Name": "ChemReactor",
		"Label": "Chemical Reactor",
		"StartTier": 2,
		"EndTier": 10,		
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["ElectricInput"],
	},{
		"Name": "Separator",
		"Label": "Separator",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "Beam",
		"Label": "Beam",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "BlockLogic",
		"Tag":"Decoration",
		"Description": ["BuildingBlock"],
	},{
		"Name": "Corner",
		"Label": "Corner",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "BlockLogic",
		"Tag":"Decoration",
		"Description": ["BuildingBlock"],
	},{
		"Name": "AutomaticHammer",
		"Label": "Automatic Hammer",
		"Positions": [[0,0,0],[0,0,1]],
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")

		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput"],
	}
	#,{
	#	"Name": "Lathe",
	#	"Label": "Lathe",
	#	
	#	"StartTier": 2,
	#	"EndTier": 7,
	#	"Description": "Unused.",
	#}
	,{
		"Name": "Boiler",
		"Label": "Boiler",
		"StartTier": 2,
		"EndTier": 10,
		"CommonTextKeys":[
			"Autocrafter"
		],
		"BlockLogic":"NuclearReactorBlockLogic",
		"BlockCreation":"""
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
		"CustomData":{
			"StorageCapacity": 30000,
			"StorageDrain": 0,
		},
		"PowerOutput": 100,
	},{
		"Name": "Pipe",
		"Label": "Pipe",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "FluidConductorBlockLogic",
		"Tag": "Logistics",
		"Description": ["FluidConductor"],
		"PathFinding": True,
	},{
		"Name": "HeatPipe",
		"Label": "Heat Pipe",
		"StartTier": 1,
		"EndTier": 1,
		"BlockLogic": "HeatConductorBlockLogic",
		"Tag": "Logistics",
		"Description": ["HeatConductor", "HeatStorage"],
		"PathFinding": True,
	},{
		"Name": "Flywheel",
		"Label": "Flywheel",
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic": "KineticConductorBlockLogic",
		"Tag": "Logistics",
		"Description": ["KineticConductor", "KineticStorage"],
		"PathFinding": True,
	},{
		"Name": "Scaffold",
		"Label": "Scaffold",
		"StartTier": 1,
		"EndTier": 10,
		"Tag": "Decoration",
		"BlockLogic": "BlockLogic",
		"Description": ["BuildingBlock"],
	},{
		"Name": "Sign",
		"Label": "Sign",
		"Tag":"Decoration",
		"StartTier": 0,
		"EndTier": 10,
		"BlockLogic": "SignBlockLogic",
	},{
		"Name": "AdvancedSign",
		"Label": "Advanced Sign",
		"Tag":"Decoration",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SignBlockLogic",
	},{
		"Name": "Connector",
		"Label": "Cable",
		"StartTier": 1,
		"EndTier": 1,
		"BlockLogic": "ElectricConductorBlockLogic",
		"Tag": "Logistics",
		"PathFinding": True,
	},{
		"Name": "Chest",
		"Label": "Chest",
		"StartTier": 0,
		"EndTier": 10,
		"Tag": "Logistics",
	},{
		"Name": "ItemRack",
		"Label": "Item Rack",
		"Positions": [[0,0,0],[-1,0,0],[0,0,1],[-1,0,1]],
		"StartTier": 1,
		"EndTier": 10,
		"Tag": "Logistics",
	},{
		"Name": "Vent",
		"Label": "Valve",
		"StartTier": 1,
		"EndTier": 1,
		"CommonTextKeys":[
			"Valve"
		],
		"BlockLogic": "FluidSwitchBlockLogic",
		"Tag": "Logistics",
		"Description": ["FluidConductor"],
	},{
		"Name": "ElectricalSwitch",
		"Label": "Switch",
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic": "ElectricSwitchBlockLogic",
		"Tag": "Logistics",
		"Description": ["ElectricConductor"],
	},{
		"Name": "OreWasher",
		"Label": "Ore Washer",
		"Positions": [[0,0,0],[0,1,0],[-1,0,0],[-1,1,0],[-2,0,0],[-2,1,0],[0,0,1],[0,1,1],[-1,0,1],[-1,1,1],[-2,0,1],[-2,1,1]],
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0,1,0))
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "Conveyor",
		"Label": "Conveyor",
		"StartTier": 1,
		"EndTier": 10,
		"CommonTextKeys":[
			"Conveyor",
			"Transporter"
		],
		"Selector": "/Game/Blocks/ArrowConvBP.ArrowConvBP_C",
		"Tag": "Logistics",
		"PathFinding": True,
	},{
		"Name": "Splitter",
		"Label": "Splitter",
		"StartTier": 1,
		"EndTier": 10,
		"Description": ["Splitter"],
		"Tag": "Logistics",
	},{
		"Name": "Sorter",
		"Label": "Sorter",
		"StartTier": 2,
		"EndTier": 10,
		"Description": ["Splitter", "Sorter"],
		"Tag": "Logistics",
	},{
		"Name": "Container",
		"Label": "Container",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "FluidContainerBlockLogic",
		"Tag": "Logistics",
		"Description": ["FluidConductor", "FluidStorage"],
	},{
		"Name": "Press",
		"Label": "Press",
		"StartTier": 2,
		"EndTier": 10,
		"CommonTextKeys":[
			"Press",
			"Autocrafter"
		],
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
	}
	#,{
	#	"Name": "Compressor",
	#	"Label": "Compressor",
	#	"StartTier": 2,
	#	"EndTier": 10,
	#	"CommonTextKeys":[
	#		"Autocrafter"
	#	],
	#	"BlockLogic":"SelectCrafter",
	#	"BlockCreation":"""
	#	local crafter = current_block_logic()
	#	
	#	local a = crafter:create_accessor(ElectricInputAccessor))
	#	a:set_side_pos(Vec3i.left(), Vec3i.zero())
	#	a:bind(crafter:get_input_container())
	#	
	#	local a = crafter:create_accessor(FluidOutputAccessor))
	#	a:set_side_pos(Vec3i.right(), Vec3i.zero())
	#	a:bind(crafter:get_output_container())
	#	""",
	#	 
	#}
	,{
		"Name": "StirlingEngine",
		"Label": "Stirling Engine",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
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
		"Description": ["HeatInput", "KineticOutput","PowerOutput"],
		"PowerOutput": 10,
	},{
		"Name": "CombustionEngine",
		"Label": "Combustion Engine",
		"StartTier": 2,
		"EndTier": 10,
		"Description": ["FluidInput", "KineticOutput"],
	},{
		"Name": "PyrolysisUnit",
		"Label": "Pyrolysis Unit",
		"Positions": [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,2,0]],
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
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
	},{
		"Name": "Generator",
		"Label": "Generator",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
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
		 
	},{
		"Name": "CompactGenerator",
		"Label": "Compact Generator",
		"StartTier": 1,
		"EndTier": 1,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
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
	},{
		"Name": "ElectricEngine",
		"Label": "Electric Engine",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
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
	},{
		"Name": "IndustrialElectricEngine",
		"Label": "Industrial Electric Engine",
		"StartTier": 4,
		"EndTier": 10,
		"Positions": [[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,0,1],[1,0,1],[0,1,1],[1,1,1]],
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
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
		"PowerOutput": 55*50,
	},{
		"Name": "RobotArm",
		"Label": "Robot Arm",
		"StartTier": 1,
		"EndTier": 10,
		"Selector": "/Game/Blocks/ArrowBP.ArrowBP_C",
		"Tag": "Logistics", 
	},{
		"Name": "FilteringRobotArm",
		"Label": "Filtering Robot Arm",
		"StartTier": 1,
		"EndTier": 10,
		"Selector": "/Game/Blocks/ArrowBP.ArrowBP_C",
		"Tag": "Logistics",
		"Description": ["Sorter"],
	},{
		"Name": "Pump",
		"Label": "Pump",
		"StartTier": 1,
		"EndTier": 10,
		"CustomData":{
			"ItemPortion": 1000
		},
		"Tag": "Logistics",
		"Selector": "/Game/Blocks/ArrowBP.ArrowBP_C",
		"Description": ["FluidInput", "FluidOutput"],
	},{
		"Name": "FilteringPump",
		"Label": "Filtering Pump",
		"StartTier": 1,
		"EndTier": 10,
		"CustomData":{
			"ItemPortion": 1000
		},
		"Tag": "Logistics",
		"Selector": "/Game/Blocks/ArrowBP.ArrowBP_C",
		"Description": ["Sorter", "FluidInput", "FluidOutput"],
	},{
		"Name": "Smelter",
		"Label": "Smelter",
		"StartTier": 0,
		"EndTier": 2,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		heat_input = get_class("HeatInputAccessor")
		
		local a = crafter:create_accessor(heat_input)
		a:set_side_pos(Vec3i.down(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["HeatInput"],
		"CustomData":{
			"Capacity":32
		}
	},{
		"Name": "SteamTurbine",
		"Label": "Steam Turbine",
		"Positions": [[0,0,0],[-1,0,0],[-2,0,0],[0,-1,0],[-1,-1,0],[-2,-1,0],[0,0,1],[-1,0,1],[-2,0,1],[0,-1,1],[-1,-1,1],[-2,-1,1]],
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
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
		"Description": ["FluidInput", "KineticOutput","PowerOutput"],
		"PowerOutput": 270,
	},{
		"Name": "IndustrialSteamTurbine",
		"Label": "Industrial Steam Turbine",
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],   [-3,0,0], [-4,0,0], [-5,0,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],[-3,-1,0],[-4,-1,0],[-5,-1,0],
			[0,-2,0],[-1,-2,0],[-2,-2,0],[-3,-2,0],[-4,-2,0],[-5,-2,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],   [-3,0,1], [-4,0,1], [-5,0,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],[-3,-1,1],[-4,-1,1],[-5,-1,1],
			[0,-2,1],[-1,-2,1],[-2,-2,1],[-3,-2,1],[-4,-2,1],[-5,-2,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],   [-3,0,2], [-4,0,2], [-5,0,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],[-3,-1,2],[-4,-1,2],[-5,-1,2],
			[0,-2,2],[-1,-2,2],[-2,-2,2],[-3,-2,2],[-4,-2,2],[-5,-2,2],
		],
		"StartTier": 5,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
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
		"Description": ["FluidInput", "ElectricOutput","PowerOutput"],
		"PowerOutput": fission_fullpower * 0.9 * 0.9,
	},{
		"Name": "GasTurbine",
		"Label": "Gas Turbine",
		"Positions": [[0,0,0],[-1,0,0],[-2,0,0],[-3,0,0],[0,-1,0],[-1,-1,0],[-2,-1,0],[-3,-1,0],[0,0,1],[-1,0,1],[-2,0,1],[-3,0,1],[0,-1,1],[-1,-1,1],[-2,-1,1],[-3,-1,1]],
		"StartTier": 4,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
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
	},{
		"Name": "Riteg",
		"Label": "RTG",
		"Positions": [
		    [0,0,0],[-1,0,0],[1,0,0],
			[0,1,0],[-1,1,0],[1,1,0],
			[0,-1,0],[-1,-1,0],[1,-1,0],
			
			[0,0,1],[-1,0,1],[1,0,1],
			[0,1,1],[-1,1,1],[1,1,1],
			[0,-1,1],[-1,-1,1],[1,-1,1],
		],
		"StartTier": 5,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
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
	},{
		"Name": "ArcSmelter",
		"Label": "Arc Smelter",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,0,2],[-1,0,2],[0,1,2],[-1,1,2]],
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
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
	},{
		"Name": "ChemicalBath",
		"Label": "Chemical Bath",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new( 0, 0, 0 ))
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "Sifter",
		"Label": "Sifter",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new( 0, 0, 0 ))
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "FilteringUnit",
		"Label": "Filtering Unit",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new( 0, 0, 0 ))
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "Furnace",
		"Label": "Furnace",
		"StartTier": 0,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		heat_output = get_class("HeatOutputAccessor")
		
		local a = crafter:create_accessor(heat_output)
		a:set_side_pos(Vec3i.up(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		""",
		"Description": ["HeatOutput"],
	},{
		"Name": "Oven",
		"Label": "Oven",
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],
			[0,1,1],[-1,1,1],[-2,1,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],
		],
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"Description": ["SpeedBonus"],
	},{
		"Name": "BlastFurnace",
		"Label": "Blast Furnace",
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],
			[0,1,1],[-1,1,1],[-2,1,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],
			
			[0,0,3],[-1,0,3],[-2,0,3],
			[0,1,3],[-1,1,3],[-2,1,3],
			[0,-1,3],[-1,-1,3],[-2,-1,3],
		],
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"Description": ["SpeedBonus"],
	},{
		"Name": "FluidFurnace",
		"Label": "Fluid Furnace",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "AutoCrafter",
		"BlockCreation":"""
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
	},{
		"Name": "ElectricFurnace",
		"Label": "Electric Furnace",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
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
	},{
		"Name": "BatteryBox",
		"Label": "Battery Box",
		"StartTier": 4,
		"EndTier": 10,
		"Description": ["ElectricConductor", "ElectricStorage"],
		"CustomData": {
			"BaseCapacity": 1000000,
			"BonusCapacity": 1000000,
		},
	},{
		 "Name": "SmallBattery",
		 "Label": "Small Battery",
		 "StartTier": 3,
		 "EndTier": 10,
		 "Description": ["ElectricConductor", "ElectricStorage"],
		 "BlockLogic": "BatteryBoxBlockLogic",
		 "CustomData": {
			 "BaseCapacity": 100000,
			 "BonusCapacity": 100000,
		 },
	},{
		 "Name": "Portal",
		 "Label": "Portal",
		 "StartTier": 7,
		 "EndTier": 10,
		 "Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],[-3,0,0],[-4,0,0],[-5,0,0],[-6,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],[-3,1,0],[-4,1,0],[-5,1,0],[-6,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],[-3,-1,0],[-4,-1,0],[-5,-1,0],[-6,-1,0],
			[0,-2,0],[-1,-2,0],[-2,-2,0],[-3,-2,0],[-4,-2,0],[-5,-2,0],[-6,-2,0],
			[0,-3,0],[-1,-3,0],[-2,-3,0],[-3,-3,0],[-4,-3,0],[-5,-3,0],[-6,-3,0],
			[0,-4,0],[-1,-4,0],[-2,-4,0],[-3,-4,0],[-4,-4,0],[-5,-4,0],[-6,-4,0],
			[0,-5,0],[-1,-5,0],[-2,-5,0],[-3,-5,0],[-4,-5,0],[-5,-5,0],[-6,-5,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],[-3,0,1],[-4,0,1],[-5,0,1],[-6,0,1],
			[0,1,1],[-1,1,1],[-2,1,1],[-3,1,1],[-4,1,1],[-5,1,1],[-6,1,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],[-3,-1,1],[-4,-1,1],[-5,-1,1],[-6,-1,1],
			[0,-2,1],[-1,-2,1],[-2,-2,1],[-3,-2,1],[-4,-2,1],[-5,-2,1],[-6,-2,1],
			[0,-3,1],[-1,-3,1],[-2,-3,1],[-3,-3,1],[-4,-3,1],[-5,-3,1],[-6,-3,1],
			[0,-4,1],[-1,-4,1],[-2,-4,1],[-3,-4,1],[-4,-4,1],[-5,-4,1],[-6,-4,1],
			[0,-5,1],[-1,-5,1],[-2,-5,1],[-3,-5,1],[-4,-5,1],[-5,-5,1],[-6,-5,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],[-3,0,2],[-4,0,2],[-5,0,2],[-6,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],[-3,1,2],[-4,1,2],[-5,1,2],[-6,1,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],[-3,-1,2],[-4,-1,2],[-5,-1,2],[-6,-1,2],
			[0,-2,2],[-1,-2,2],[-2,-2,2],[-3,-2,2],[-4,-2,2],[-5,-2,2],[-6,-2,2],
			[0,-3,2],[-1,-3,2],[-2,-3,2],[-3,-3,2],[-4,-3,2],[-5,-3,2],[-6,-3,2],
			[0,-4,2],[-1,-4,2],[-2,-4,2],[-3,-4,2],[-4,-4,2],[-5,-4,2],[-6,-4,2],
			[0,-5,2],[-1,-5,2],[-2,-5,2],[-3,-5,2],[-4,-5,2],[-5,-5,2],[-6,-5,2],
			
			[0,0,3],[-1,0,3],[-2,0,3],[-3,0,3],[-4,0,3],[-5,0,3],[-6,0,3],
			[0,1,3],[-1,1,3],[-2,1,3],[-3,1,3],[-4,1,3],[-5,1,3],[-6,1,3],
			[0,-1,3],[-1,-1,3],[-2,-1,3],[-3,-1,3],[-4,-1,3],[-5,-1,3],[-6,-1,3],
			[0,-2,3],[-1,-2,3],[-2,-2,3],[-3,-2,3],[-4,-2,3],[-5,-2,3],[-6,-2,3],
			[0,-3,3],[-1,-3,3],[-2,-3,3],[-3,-3,3],[-4,-3,3],[-5,-3,3],[-6,-3,3],
			[0,-4,3],[-1,-4,3],[-2,-4,3],[-3,-4,3],[-4,-4,3],[-5,-4,3],[-6,-4,3],
			[0,-5,3],[-1,-5,3],[-2,-5,3],[-3,-5,3],[-4,-5,3],[-5,-5,3],[-6,-5,3],
			
			[0,0,3],[-1,0,3],[-2,0,3],[-3,0,3],[-4,0,3],[-5,0,3],[-6,0,4],
			[0,1,3],[-1,1,3],[-2,1,3],[-3,1,3],[-4,1,3],[-5,1,3],[-6,1,4],
			[0,-1,3],[-1,-1,3],[-2,-1,3],[-3,-1,3],[-4,-1,3],[-5,-1,3],[-6,-1,4],
			[0,-2,3],[-1,-2,3],[-2,-2,3],[-3,-2,3],[-4,-2,3],[-5,-2,3],[-6,-2,4],
			[0,-3,3],[-1,-3,3],[-2,-3,3],[-3,-3,3],[-4,-3,3],[-5,-3,3],[-6,-3,4],
			[0,-4,3],[-1,-4,3],[-2,-4,3],[-3,-4,3],[-4,-4,3],[-5,-4,3],[-6,-4,4],
			[0,-5,3],[-1,-5,3],[-2,-5,3],[-3,-5,3],[-4,-5,3],[-5,-5,3],[-6,-5,4]
		],
		"BlockCreation":"""
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
	#{
	#	"Name": "MoltenSaltBattery",
	#	"Label": "Molten Salt Battery",
	#	"StartTier": 5,
	#	"EndTier": 10,
	#	"BlockLogic": "HighcapElectricBatteryBlockLogic",
	#}
	{
		"Name": "DrillingRig",
		"Label": "Drilling Rig",
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],
			[0,1,1],[-1,1,1],[-2,1,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],
			
			[0,0,3],[-1,0,3],[-2,0,3],
			[0,1,3],[-1,1,3],[-2,1,3],
			[0,-1,3],[-1,-1,3],[-2,-1,3],
			
			[0,0,4],[-1,0,4],[-2,0,4],
			[0,1,4],[-1,1,4],[-2,1,4],
			[0,-1,4],[-1,-1,4],[-2,-1,4],
		],
		"StartTier": 1,
		"EndTier": 10,
		"Description": ["KineticInput", "ItemOutput"],
	},{
		"Name": "Assembler",
		"Label": "Assembler",
		"StartTier": 1,
		"EndTier": 10,
		"Positions": [
			[0,0,0],[-1,0,0],
			[0,0,1],[-1,0,1],
			
			[0,-1,0],[-1,-1,0],
			[0,-1,1],[-1,-1,1],
		],
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
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
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["ElectricInput"],
	},{
		"Name": "Constructor",
		"Label": "Constructor",
		"StartTier": 2,
		"EndTier": 10,
		"Positions": [
			[0,0,0],[-1,0,0],
			[0,0,1],[-1,0,1],
			
			[0,-1,0],[-1,-1,0],
			[0,-1,1],[-1,-1,1],
		],
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
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
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["ElectricInput"],
	},{
		"Name": "Deconstructor",
		"Label": "Deconstructor",
		"StartTier": 2,
		"EndTier": 10,
		"Positions": [
			[0,0,0],[-1,0,0],
			[0,0,1],[-1,0,1],
			
			[0,-1,0],[-1,-1,0],
			[0,-1,1],[-1,-1,1],
		],
		"BlockLogic":"DeconstructorCrafterBlockLogic",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["ElectricInput"],
	},
	{
		"Name": "FluidDump",
		"Label": "Fluid Dump",
		"Positions": [
			[0,0,0],[0,-1,0],[0,-2,0],[0,1,0],[0,2,0],
			[-1,0,0],[-1,-1,0],[-1,-2,0],[-1,1,0],[-1,2,0],
			[-2,0,0],[-2,-1,0],[-2,-2,0],[-2,1,0],[-2,2,0],
			[-3,0,0],[-3,-1,0],[-3,-2,0],[-3,1,0],[-3,2,0],
			[-4,0,0],[-4,-1,0],[-4,-2,0],[-4,1,0],[-4,2,0],
		],
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		fluid_input = get_class("FluidInputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["FluidInput"],
	},{
		"Name": "GasDump",
		"Label": "Gas Dump",
		"Positions": [
			[0,0,0]
		],
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic":"DumpCrafterBlockLogic",
		"BlockCreation":"""
		local crafter = current_block_logic()

		fluid_input = get_class("FluidInputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.down(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["FluidInput"],
	},{
		"Name": "SolidDump",
		"Label": "Solid Dump",
		"Positions": [
			[0,0,0],[-1,0,0],
			[0,-1,0],[-1,-1,0],
		],
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic":"DumpAnyBlockLogic",
		"Description": ["SolidInput"],
	},
	#,{
	#	"Name": "Liquifier",
	#	"Label": "Liquifier",
	#	"StartTier": 2,
	#	"EndTier": 3,
	#	"Description": ""
	#}
	{
		"Name": "Lamp",
		"Label": "Lamp",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "LampBlockLogic",
	},{
		"Name": "AdminElectricGenerator",
		"Label": "Creative Electric Generator",
		"StartTier": 7,
		"EndTier": 7,
		"Craftable": False,
		"Description": ["ElectricOutput"],
	},{
		"Name": "AdminItemGenerator",
		"Label": "Creative Item Generator",
		"StartTier": 7,
		"EndTier": 7,
		"Craftable": False,
		"Description": ["ItemOutput"],
	},{
		"Name": "AdminKineticGenerator",
		"Label": "Creative Kinetic Generator",
		"StartTier": 7,
		"EndTier": 7,
		"Craftable": False,
		"Description": ["KineticOutput"],
	},{
		"Name": "AdminHeatGenerator",
		"Label": "Creative Heat Generator",
		"StartTier": 7,
		"EndTier": 7,
		"Craftable": False,
		"Description": ["HeatOutput"],
	},{
		"Name": "AdminFluidGenerator",
		"Label": "Creative Fluid Generator",
		"StartTier": 7,
		"EndTier": 7,
		"Craftable": False,
		"Description": ["FluidOutput"],
	},{
		"Name": "AdminExterminator",
		"Label": "Creative Exterminator",
		"StartTier": 7,
		"EndTier": 7,
		"Craftable": False,
		"Description": ["KineticInput", "HeatInput", "FluidInput", "ItemInput", "KineticInput"],
	},{
		"Name": "Electrolyzer",
		"Label": "Electrolyzer",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		electric_input = get_class("ElectricInputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.back(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["ElectricInput"],
	},{
		"Name": "Mixer",
		"Label": "Mixer",
		"StartTier": 2,
		"EndTier": 10,
		"Positions": [[0,0,0],[-1,0,0],[0,0,1],[-1,0,1]],
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.back(), Vec3i.new(-1,0,0))
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "Freezer",
		"Label": "Freezer",
		"StartTier": 5,
		"EndTier": 10,
		"Positions": [[0,0,0],[-1,0,0],[0,0,1],[-1,0,1]],
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		kinetic_input = get_class("KineticInputAccessor")
		
		local a = crafter:create_accessor(kinetic_input)
		a:set_side_pos(Vec3i.left(), Vec3i.new(-1,0,0))
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput", "HeatOutput"],
	},{
		"Name": "AutomaticFarm",
		"Label": "Automatic Farm",
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],[-3,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],[-3,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],[-3,-1,0],
			[0,-2,0],[-1,-2,0],[-2,-2,0],[-3,-2,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],[-3,0,1],
			[0,1,1],[-1,1,1],[-2,1,1],[-3,1,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],[-3,-1,1],
			[0,-2,1],[-1,-2,1],[-2,-2,1],[-3,-2,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],[-3,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],[-3,1,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],[-3,-1,2],
			[0,-2,2],[-1,-2,2],[-2,-2,2],[-3,-2,2],
		],
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		fluid_input = get_class("FluidInputAccessor")
		
		local a = crafter:create_accessor(fluid_input)
		a:set_side_pos(Vec3i.front(), Vec3i.new(0,0,0))
		a:bind(crafter:get_input_container())
		""",
		"Description": ["FluidInput"],
	},{
		"Name": "AtmosphericCondenser",
		"Label": "Atmospheric Condenser",
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],
			[0,-2,0],[-1,-2,0],[-2,-2,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],
			[0,-2,1],[-1,-2,1],[-2,-2,1],
		],
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		local a = crafter:create_accessor(get_class("FluidOutputAccessor"))
		a:set_side_pos(Vec3i.front(), Vec3i.new(0,0,0))
		a:bind(crafter:get_output_container())
		
		local a = crafter:create_accessor(get_class("KineticInputAccessor"))
		a:set_side_pos(Vec3i.right(), Vec3i.new(-1,-2,0))
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput", "FluidOutput"],
	},{
		"Name": "Terminal",
		"Label": "Terminal",
		"StartTier": 4,
		"EndTier": 4,
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "BigTerminal",
		"Label": "Big Terminal",
		"StartTier": 5,
		"EndTier": 5,
		"Image": "Terminal",
		"Positions": [[0,0,0],[0,-1,0],[0,0,1],[0,-1,1]],
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "HugeTerminal",
		"Label": "Huge Terminal",
		"StartTier": 6,
		"EndTier": 6,
		"Image": "Terminal",
		"Positions": [[0,0,0],[0,-1,0],[0,-2,0],[0,0,1],[0,-1,1],[0,-2,1],[0,0,2],[0,-1,2],[0,-2,2]],
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "FlatTerminal",
		"Label": "Flat Terminal",
		"StartTier": 4,
		"EndTier": 4,
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "BigFlatTerminal",
		"Label": "Big Flat Terminal",
		"StartTier": 5,
		"EndTier": 5,
		"Image": "FlatTerminal",
		"Positions": [[0,0,0],[0,-1,0],[0,0,1],[0,-1,1]],
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "HugeFlatTerminal",
		"Label": "Huge Flat Terminal",
		"StartTier": 6,
		"EndTier": 6,
		"Image": "FlatTerminal",
		"Positions": [[0,0,0],[0,-1,0],[0,-2,0],[0,0,1],[0,-1,1],[0,-2,1],[0,0,2],[0,-1,2],[0,-2,2]],
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "Computer",
		"Label": "Computer",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"ComputerBlockLogic",
		"Description": ["ElectricInput"],
	},{
		"Name": "QuantumComputer",
		"Label": "Quantum Computer",
		"StartTier": 5,
		"EndTier": 10,
		"BlockLogic":"QuantumComputerBlockLogic",
		"Description": ["ElectricInput"],
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],
			[0,-2,0],[-1,-2,0],[-2,-2,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],
			[0,-2,1],[-1,-2,1],[-2,-2,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],
			[0,-2,2],[-1,-2,2],[-2,-2,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],
		]
	}
	,{
		"Name": "IndustrialSeparator",
		"Label": "Industrial Separator",
		"Positions": [[0,0,0],[-1,0,0],[0,-1,0],[-1,-1,0],[0,1,0],[-1,1,0], [0,0,1],[-1,0,1],[0,-1,1],[-1,-1,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 10,
		"CommonTextKeys":[
			"Separator",
			"Autocrafter"
		],
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		local a = crafter:create_accessor(get_class("KineticInputAccessor"))
		a:set_side_pos(Vec3i.back(), Vec3i.new(-1,1,0))
		a:bind(crafter:get_input_container())
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "Radiator",
		"Label": "Radiator",
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		local a = crafter:create_accessor(get_class("HeatInputAccessor"))
		a:set_side_pos(Vec3i.down(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		""",
		"Description": ["HeatInput"],
	},{
		"Name": "Diode",
		"Label": "Diode",
		"StartTier": 2,
		"EndTier": 10,
		"Description": ["ElectricInput", "ElectricOutput"],
	},
	#,{
	#	"Name": "Tank",
	#	"Label": "Tank",
	#	"Positions": [
	#		[0,0,0],[-1,0,0],[-2,0,0],
	#		[0,1,0],[-1,1,0],[-2,1,0],
	#		[0,-1,0],[-1,-1,0],[-2,-1,0],
	#		
	#		[0,0,1],[-1,0,1],[-2,0,1],
	#		[0,1,1],[-1,1,1],[-2,1,1],
	#		[0,-1,1],[-1,-1,1],[-2,-1,1],
	#		
	#		[0,0,2],[-1,0,2],[-2,0,2],
	#		[0,1,2],[-1,1,2],[-2,1,2],
	#		[0,-1,2],[-1,-1,2],[-2,-1,2],
	#	],
	#	"StartTier": 1,
	#	"EndTier": 10,
	#	"CommonTextKeys":[
	#		"Container"
	#	],
	#	"RequiredResearches":["LiquidsScan"],
	#},
	{
		"Name": "FissionReactor",
		"Label": "Fission Reactor",
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],[-3,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],[-3,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],[-3,-1,0],
			[0,-2,0],[-1,-2,0],[-2,-2,0],[-3,-2,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],[-3,0,1],
			[0,1,1],[-1,1,1],[-2,1,1],[-3,1,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],[-3,-1,1],
			[0,-2,1],[-1,-2,1],[-2,-2,1],[-3,-2,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],[-3,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],[-3,1,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],[-3,-1,2],
			[0,-2,2],[-1,-2,2],[-2,-2,2],[-3,-2,2],
			
			[0,0,3],[-1,0,3],[-2,0,3],[-3,0,3],
			[0,1,3],[-1,1,3],[-2,1,3],[-3,1,3],
			[0,-1,3],[-1,-1,3],[-2,-1,3],[-3,-1,3],
			[0,-2,3],[-1,-2,3],[-2,-2,3],[-3,-2,3],
			
			[0,0,4],[-1,0,4],[-2,0,4],[-3,0,4],
			[0,1,4],[-1,1,4],[-2,1,4],[-3,1,4],
			[0,-1,4],[-1,-1,4],[-2,-1,4],[-3,-1,4],
			[0,-2,4],[-1,-2,4],[-2,-2,4],[-3,-2,4],
		],
		"StartTier": 5,
		"EndTier": 10,
		"BlockLogic":"NuclearReactorBlockLogic",
		"BlockCreation":"""
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
		"CustomData":{
			"LoadIndependent": True,
			"StorageCapacity": 10000000,
			"StorageDrain": 80,
		},
		"Description": ["HeatOutput"],
	},{
		"Name": "FusionReactor",
		"Label": "Fusion Reactor",
		"StartTier": 6,
		"EndTier": 10,
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],[-3,0,0],[-4,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],[-3,1,0],[-4,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],[-3,-1,0],[-4,-1,0],
			[0,-2,0],[-1,-2,0],[-2,-2,0],[-3,-2,0],[-4,-2,0],
			[0,-3,0],[-1,-3,0],[-2,-3,0],[-3,-3,0],[-4,-3,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],[-3,0,1],[-4,0,1],
			[0,1,1],[-1,1,1],[-2,1,1],[-3,1,1],[-4,1,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],[-3,-1,1],[-4,-1,1],
			[0,-2,1],[-1,-2,1],[-2,-2,1],[-3,-2,1],[-4,-2,1],
			[0,-3,1],[-1,-3,1],[-2,-3,1],[-3,-3,1],[-4,-3,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],[-3,0,2],[-4,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],[-3,1,2],[-4,1,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],[-3,-1,2],[-4,-1,2],
			[0,-2,2],[-1,-2,2],[-2,-2,2],[-3,-2,2],[-4,-2,2],
			[0,-3,2],[-1,-3,2],[-2,-3,2],[-3,-3,2],[-4,-3,2],
			
			[0,0,3],[-1,0,3],[-2,0,3],[-3,0,3],[-4,0,3],
			[0,1,3],[-1,1,3],[-2,1,3],[-3,1,3],[-4,1,3],
			[0,-1,3],[-1,-1,3],[-2,-1,3],[-3,-1,3],[-4,-1,3],
			[0,-2,3],[-1,-2,3],[-2,-2,3],[-3,-2,3],[-4,-2,3],
			[0,-3,3],[-1,-3,3],[-2,-3,3],[-3,-3,3],[-4,-3,3],
		],
		"BlockLogic":"FusionReactorBlockLogic",
		"BlockCreation":"""
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
	},{
		"Name": "IndustrialBoiler",
		"Label": "Industrial Boiler",
		"StartTier": 5,
		"EndTier": 10,
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],   [-3,0,0], 
			[0,-1,0],[-1,-1,0],[-2,-1,0],[-3,-1,0],
			[0,-2,0],[-1,-2,0],[-2,-2,0],[-3,-2,0],
															 
			[0,0,1],[-1,0,1],[-2,0,1],   [-3,0,1], 
			[0,-1,1],[-1,-1,1],[-2,-1,1],[-3,-1,1],
			[0,-2,1],[-1,-2,1],[-2,-2,1],[-3,-2,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],   [-3,0,2], 
			[0,-1,2],[-1,-1,2],[-2,-1,2],[-3,-1,2],
			[0,-2,2],[-1,-2,2],[-2,-2,2],[-3,-2,2],
		],
		"BlockLogic":"NuclearReactorBlockLogic",
		"BlockCreation":"""
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
		"Description": ["FluidInput", "FluidOutput","PowerOutput"],
		"PowerOutput": fission_fullpower * 0.9,
		"CustomData":{
			"StorageCapacity": 6000000,
			"StorageDrain": 0
		}
	},
	{
		"Name": "SolarPanel",
		"Label": "Solar Panel",
		"Positions": [
			[0,0,0],[-1,0,0],[1,0,0],
			[0,1,0],[-1,1,0],[1,1,0],
			[0,-1,0],[-1,-1,0],[1,-1,0],
			
			[0,0,1],[-1,0,1],[1,0,1],
			[0,1,1],[-1,1,1],[1,1,1],
			[0,-1,1],[-1,-1,1],[1,-1,1],
			
			[0,0,2],[-1,0,2],[1,0,2],
			[0,1,2],[-1,1,2],[1,1,2],
			[0,-1,2],[-1,-1,2],[1,-1,2],
		],
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
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
		"Name": "Pumpjack",
		"Label": "Pumpjack",
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],[-3,0,0],[-4,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],[-3,1,0],[-4,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],[-3,-1,0],[-4,-1,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],[-3,0,1],[-4,0,1],
			[0,1,1],[-1,1,1],[-2,1,1],[-3,1,1],[-4,1,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],[-3,-1,1],[-4,-1,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],[-3,0,2],[-4,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],[-3,1,2],[-4,1,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],[-3,-1,2],[-4,-1,2],
			
			[0,0,3],[-1,0,3],[-2,0,3],[-3,0,3],[-4,0,3],
			[0,1,3],[-1,1,3],[-2,1,3],[-3,1,3],[-4,1,3],
			[0,-1,3],[-1,-1,3],[-2,-1,3],[-3,-1,3],[-4,-1,3],
		],
		"StartTier": 3,
		"EndTier": 10,	
		"Description": ["KineticInput", "FluidOutput"],		
	},
	##,{
	##	"Name": "PneumaticPipe",
	##	"Label": "Pneumatic Pipe",
	##	"StartTier": 3,
	##	"EndTier": 5,
	##	"CommonTextKeys":[
	##		
	##	],
    ##
	##}
	##,{
	##	"Name": "PneumaticInput",
	##	"Label": "Pneumatic Input",
	##	"StartTier": 3,
	##	"EndTier": 5,
	##	"CommonTextKeys":[
	##		
	##	],
	##	
	##}
	#{
	#	"Name": "DistributionBox",
	#	"Label": "Distribution Box",
	#	"StartTier": 2,
	#	"EndTier": 7,
	#	"CommonTextKeys":[
	#		"Chest"
	#	],
	#},
	#{
	#	"Name": "HeatExchanger",
	#	"Label": "Heat Exchanger",
	#	"StartTier": 3,
	#	"EndTier": 10,
	#	"BlockLogic":"SelectCrafter",
	#	"BlockCreation":"""
	#	local crafter = current_block_logic()
	#	
	#	local a = crafter:create_accessor(FluidInputAccessor))
	#	a:set_side_pos(Vec3i.left(), Vec3i.zero())
	#	a:bind(crafter:get_input_container())
	#	
	#	local a = crafter:create_accessor(FluidOutputAccessor))
	#	a:set_side_pos(Vec3i.right(), Vec3i.zero())
	#	a:bind(crafter:get_output_container())
	#	
	#	local a = crafter:create_accessor(HeatOutputAccessor))
	#	a:set_side_pos(Vec3i.up(), Vec3i.zero())
	#	a:bind(crafter:get_output_container())
	#	""",
	#	"RequiredResearches":["HeatTransferring"],
	#}
	#,{
	#	"Name": "InverseHeatExchanger",
	#	"Label": "Inverse Heat Exchanger",
	#	"StartTier": 1,
	#	"EndTier": 10,
	#	"BlockLogic":"SelectCrafter",
	#	"BlockCreation":"""
	#	local crafter = current_block_logic()
	#	
	#	local a = crafter:create_accessor(FluidInputAccessor))
	#	a:set_side_pos(Vec3i.left(), Vec3i.zero())
	#	a:bind(crafter:get_input_container())
	#	
	#	local a = crafter:create_accessor(FluidOutputAccessor))
	#	a:set_side_pos(Vec3i.right(), Vec3i.zero())
	#	a:bind(crafter:get_output_container())
	#	
	#	local a = crafter:create_accessor(HeatInputAccessor))
	#	a:set_side_pos(Vec3i.down(), Vec3i.zero())
	#	a:bind(crafter:get_input_container())
	#	""",
	#	"RequiredResearches":["HeatTransferring"],
	#}
	#,{
	#	"Name": "IndustrialOven",
	#	"Label": "Industrial Oven",
	#	"StartTier": 3,
	#	"EndTier": 7,
	#	"CommonTextKeys":[
	#		"Dryer",
	#		"CokeOven"
	#	],
	#	
	#	"Positions": [
	#		[0,0,0],[-1,0,0],
	#		[0,1,0],[-1,1,0],
	#	],
	#	
	#}
	{
		"Name": "IndustrialSmelter",
		"Label": "Industrial Smelter",
		"StartTier": 4,
		"EndTier": 10,
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],
			
			[-1,0,1],#[0,0,1],[-2,0,1],
			#[0,1,1],[-1,1,1],[-2,1,1],
			#[-1,-1,1],[0,-1,1],[-2,-1,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],
		],
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
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
	},{
		"Name": "InductionCoil",
		"Label": "Induction Coil",
		"StartTier": 4,
		"EndTier": 10,
		"Positions": [
			[0,0,0],[-2,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],
			[-1,-1,0],[0,-1,0],[-2,-1,0],
		],
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		local crafter = current_block_logic()
		
		local heat_input = get_class("HeatInputAccessor")
		local heat_output = get_class("HeatOutputAccessor")
		local kinetic_input = get_class("KineticInputAccessor")
		local kinetic_output = get_class("KineticOutputAccessor")
		local electric_input = get_class("ElectricInputAccessor")
		local electric_output = get_class("ElectricOutputAccessor")
		local fluid_input = get_class("FluidInputAccessor")
		local fluid_output = get_class("FluidOutputAccessor")
		
		local a = crafter:create_accessor(electric_input)
		a:set_side_pos(Vec3i.front(), Vec3i.zero())
		a:bind(crafter:get_input_container())
		
		local a = crafter:create_accessor(heat_output)
		
		a:set_side_pos(Vec3i.up(), Vec3i.zero())
		a:bind(crafter:get_output_container())
		""",
		"Description": ["ElectricInput", "HeatOutput"],
	},{
		"Name": "CreativeController",
		"Label": "Creative Controller",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["DataInput", "DataOutput"],
	},{
		"Name": "LogicCircuit",
		"Label": "Logic Circuit",
		"StartTier": 2,
		"EndTier": 2,
		"Description": ["DataInput", "DataOutput"],
	},{
		"Name": "LogicInterface",
		"Label": "Logic Interface",
		"StartTier": 2,
		"EndTier": 2,
		"Description": ["DataOutput"],
	},{
		"Name": "LogicController",
		"Label": "Logic Controller",
		"StartTier": 2,
		"EndTier": 2,
		"Description": ["DataInput"],
	},{
		"Name": "LogicDisplay",
		"Label": "Logic Display",
		"StartTier": 2,
		"EndTier": 2,
		"Description": ["DataInput"],
	},{
		"Name": "LogicWire",
		"Label": "Logic Wire",
		"BlockLogic":"DataConductorBlockLogic",
		"StartTier": 2,
		"EndTier": 2,
		"Description": ["DataConductor"],
	},{
		"Name": "Button",
		"Label": "Button",
		"StartTier": 2,
		"EndTier": 2,		
		"Description": ["DataOutput"],
	},{
		"Name": "ToggleButton",
		"Label": "Toggle Button",
		"StartTier": 2,
		"EndTier": 2,		
		"Description": ["DataOutput"],
	}
]