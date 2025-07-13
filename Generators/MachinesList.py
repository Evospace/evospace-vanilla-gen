## -*- coding: utf-8 -*-

from Common import *
from Materials import *

machines = [
	{
		"Name": "Macerator",
		"Label": "Macerator",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "AutoCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 20,
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
		"StartTier": 3,
		"EndTier": 7,
		"Positions": [[0,0,0],[0,0,1]],
		"BlockLogic":"SelectCrafter",
		"RequiredResearch":["Fermentation"],
		"Description": ["ElectricInput", "PowerInput"],
        "PowerInput": 20,
	},{
		"Name": "Separator",
		"Label": "Separator",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 80,
	},{
		"Name": "Beam",
		"Label": "Beam",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "BlockLogic",
		"Description": ["BuildingBlock"],
	},{
		"Name": "Spawner",
		"Label": "Spawner",
		"StartTier": 1,
		"EndTier": 1,
		"BlockLogic": "BedBlockLogic",
	},{
		"Name": "Corner",
		"Label": "Corner",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "SimpleInstancedBlockLogic",
		"Description": ["BuildingBlock"]
	},{
		"Name": "AutomaticHammer",
		"Label": "Automatic Hammer",
		"Positions": [[0,0,0],[0,0,1]],
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 30,
	},{
		"Name": "Boiler",
		"Label": "Boiler",
		"StartTier": 2,
		"EndTier": 7,
		"CommonTextKeys":[
			"Autocrafter"
		],
		"BlockLogic":"SelectCrafter",
		"Description": ["HeatInput", "FluidInput", "FluidOutput", "PowerOutput"],
		"CustomData":{
			"StorageCapacity": 30000,
			"StorageDrain": 0,
		},
		"PowerOutput": 200,
	},{
		"Name": "Pipe",
		"Label": "Pipe",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "ConductorBlockLogic",
		"Description": ["FluidConductor"],
		"PathFinding": True,
        "NoActorRenderable": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
        "Category": "Network",
	},{
		"Name": "HeatPipe",
		"Label": "Heat Pipe",
		"StartTier": 1,
		"EndTier": 1,
		"BlockLogic": "HeatConductorBlockLogic",
		"Description": ["HeatConductor", "HeatStorage"],
		"PathFinding": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
        "Category": "Network",
	},{
		"Name": "PlasmaPipe",
		"Label": "Plasma Pipe",
		"StartTier": 4,
		"EndTier": 4,
		"BlockLogic": "PlasmaConductorBlockLogic",
		"Description": ["HeatConductor", "HeatStorage"],
		"PathFinding": True,
        "ExactName": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
        "Category": "Network",
	},{
		"Name": "Flywheel",
		"Label": "Flywheel",
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic": "KineticConductorBlockLogic",
		"Description": ["KineticConductor", "KineticStorage"],
		"PathFinding": True,
        "Category": "Network",
	},{
		"Name": "Scaffold",
		"Label": "Scaffold",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "SimpleInstancedBlockLogic",
		"Description": ["BuildingBlock"],
	},{
		"Name": "Sign",
		"Label": "Sign",
		"StartTier": 0,
		"EndTier": 7,
		"BlockLogic": "SignBlockLogic",
	},{
		"Name": "AdvancedSign",
		"Label": "Advanced Sign",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SignBlockLogic",
	},{
		"Name": "CopperConnector",
		"Label": "Copper Cable",
		"StartTier": 0,
		"EndTier": 0,
		"BlockLogic": "ConductorBlockLogic",
        "Description": ["ElectricConductor"],
		"PathFinding": True,
        "ExactName": True,
        "NoActorRenderable": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
        "Category": "Network",
        "ReplaceTag": "Cable",
	},{
		"Name": "Chest",
		"Label": "Chest",
		"StartTier": 0,
		"EndTier": 7,
        "Description": ["ItemInput", "ItemStorage"],
	},{
		"Name": "ItemRack",
		"Label": "Item Rack",
		"Positions": [[0,0,0],[-1,0,0],[0,0,1],[-1,0,1]],
		"StartTier": 1,
		"EndTier": 7,
        "Description": ["ItemInput", "ItemStorage"],
	},{
		"Name": "Vent",
		"Label": "Valve",
		"StartTier": 1,
		"EndTier": 1,
		"CommonTextKeys":[
			"Valve"
		],
		"BlockLogic": "FluidSwitchBlockLogic",
		"Description": ["FluidConductor"],
	},{
		"Name": "ElectricalSwitch",
		"Label": "Switch",
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic": "ElectricitySwitchBlockLogic",
		"Description": ["ElectricConductor"],
	},{
		"Name": "OreWasher",
		"Label": "Ore Washer",
		"Positions": [[0,0,0],[0,1,0],[-1,0,0],[-1,1,0],[-2,0,0],[-2,1,0],[0,0,1],[0,1,1],[-1,0,1],[-1,1,1],[-2,0,1],[-2,1,1]],
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 20,
	},{
		"Name": "Conveyor",
		"Label": "Conveyor",
		"StartTier": 1,
		"EndTier": 7,
		"CommonTextKeys":[
			"Conveyor",
			"Transporter"
		],
		"Selector": "Blocks/ArrowConvBP.ArrowConvBP_C",
		"PathFinding": True,
        "ReplaceTag": "Conveyor",
	},{
		"Name": "Splitter",
		"Label": "Splitter",
		"StartTier": 1,
		"EndTier": 7,
		"Description": ["Splitter"],
        "ReplaceTag": "Conveyor",
	},{
		"Name": "Sorter",
		"Label": "Sorter",
		"StartTier": 2,
		"EndTier": 7,
		"Description": ["Splitter", "Sorter"],
        "ReplaceTag": "Conveyor",
	},{
		"Name": "Container",
		"Label": "Container",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "FluidContainerBlockLogic",
		"Description": ["FluidConductor", "FluidStorage"],
	},{
		"Name": "StirlingEngine",
		"Label": "Stirling Engine",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["HeatInput", "KineticOutput","PowerOutput"],
		"PowerOutput": 50,
	},{
		"Name": "SteamEngine",
		"Label": "Steam Engine",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["FluidInput", "KineticOutput", "PowerOutput"],
		"PowerOutput": 200,
	},{
		"Name": "CombustionEngine",
		"Label": "Combustion Engine",
		"BlockLogic": "AutoCrafter",
		"StartTier": 4,
		"EndTier": 7,
        "Description": ["FluidInput", "KineticOutput", "PowerOutput"],
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,2,0],[-1,2,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,2,1],[-1,2,1]],
	},{
		"Name": "FractionatingColumn",
		"Label": "Fractionating Column",
		"StartTier": 4,
		"EndTier": 7,
		"Description": ["ElectricInput", "PowerInput", "FluidInput", "FluidOutput"],
		"BlockLogic": "SelectCrafter",
		"Positions": [
            [0,0,0],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[1,1,0],[-1,-1,0],[1,-1,0],[-1,1,0],
            [0,0,1],[1,0,1],[-1,0,1],[0,1,1],[0,-1,1],[1,1,1],[-1,-1,1],[1,-1,1],[-1,1,1],
            
			[0,0,2],[1,0,2],[-1,0,2],[0,1,2],[0,-1,2],[1,1,2],[-1,-1,2],[1,-1,2],[-1,1,2],
            [0,0,3],[1,0,3],[-1,0,3],[0,1,3],[0,-1,3],[1,1,3],[-1,-1,3],[1,-1,3],[-1,1,3],
            
			[0,0,4],[1,0,4],[-1,0,4],[0,1,4],[0,-1,4],[1,1,4],[-1,-1,4],[1,-1,4],[-1,1,4],
            [0,0,5],[1,0,5],[-1,0,5],[0,1,5],[0,-1,5],[1,1,5],[-1,-1,5],[1,-1,5],[-1,1,5]
        ]
	},{
		"Name": "PyrolysisUnit",
		"Label": "Pyrolysis Unit",
		"Positions": [[0,0,0],[0,0,1],[0,1,0],[0,2,0]],
		"StartTier": 4,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["HeatInput", "PowerInput"],
        "PowerInput": 50,
	},{
        "Name": "HandGenerator",
        "Label": "Hand Generator",
        "StartTier": 1,
        "EndTier": 1,
        "Description": ["KineticOutput", "PowerOutput"],
        "PowerOutput": 9,
        "Positions": [
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 2],
        ],
    },{
		"Name": "Generator",
		"Label": "Generator",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		"PowerOutput": 200 * 5 * 2,
	},{
		"Name": "IndustrialGenerator",
		"Label": "Industrial Generator",
		"Positions": [
            [0, 0, 0], [0, 2, 0], [1, 2, 0], [-1, 2, 0], [0, 3, 0], [1, 3, 0], [-1, 3, 0],
			[0, 1, 0], [1, 1, 0], [-1, 1, 0],
			[0, 2, 1], [1, 2, 1], [-1, 2, 1], [0, 3, 1], [1, 3, 1], [-1, 3, 1],
			[0, 1, 1], [1, 1, 1], [-1, 1, 1],
			[0, 2, 2], [1, 2, 2], [-1, 2, 2], [0, 3, 2], [1, 3, 2], [-1, 3, 2],
			[0, 1, 2], [1, 1, 2], [-1, 1, 2],
			[-1, 0, 0], [1, 0, 0], [-1, 0, 1], [0, 0, 1], [1, 0, 1],
			[-1, 0, 2], [0, 0, 2], [1, 0, 2]],
		"StartTier": 5,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		"PowerOutput": 240*20,
		 
	},{
		"Name": "CompactGenerator",
		"Label": "Compact Generator",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		"PowerOutput": 50,
	},{
		"Name": "ElectricEngine",
		"Label": "Electric Engine",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
        "Selector": "Blocks/ElectricEngineBP.ElectricEngineBP_C",
		"Description": ["ElectricInput", "KineticOutput", "PowerOutput"],
		"PowerOutput": 100,
        "DefaultRotation": [-1, 0, 0, 0]
	},{
		"Name": "Loader",
		"Label": "Loader",
		"StartTier": 1,
		"EndTier": 7,
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
	},{
		"Name": "RobotArm",
		"Label": "Robot Arm",
		"StartTier": 1,
		"EndTier": 7,
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
	},{
		"Name": "Pump",
		"Label": "Pump",
		"StartTier": 1,
		"EndTier": 7,
		"CustomData":{
			"ItemPortion": 1000
		},
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
		"Description": ["FluidInput", "FluidOutput"],
	},{
		"Name": "OverflowPump",
		"Label": "Overflow Pump",
		"StartTier": 1,
		"EndTier": 7,
		"CustomData":{
			"ItemPortion": 1000
		},
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
		"Description": ["FluidInput", "FluidOutput"],
	},{
		"Name": "Smelter",
		"Label": "Smelter",
		"StartTier": 0,
		"EndTier": 2,
		"BlockLogic":"AutoCrafter",
		"Description": ["HeatInput"],
		"CustomData":{
			"Capacity":32
		}
	},{
		"Name": "SteamTurbine",
		"Label": "Steam Turbine",
		"Positions": [[0,0,0],[-1,0,0],[-2,0,0],[0,-1,0],[-1,-1,0],[-2,-1,0],[0,0,1],[-1,0,1],[-2,0,1],[0,-1,1],[-1,-1,1],[-2,-1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["FluidInput", "KineticOutput","PowerOutput"],
		"PowerOutput": 200 * 5 * 2,
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
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["FluidInput", "KineticOutput", "PowerOutput"],
		"PowerOutput": fission_output(),
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
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"Description": ["HeatOutput", "PowerOutput"],
		"PowerOutput": 500,
	},{
		"Name": "DroneStation",
		"Label": "Drone Station",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,0,2],[-1,0,2],[0,1,2],[-1,1,2]],
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"DroneStationBlockLogic",
		"Description": ["ElectricInput", "PowerInput"],
        "PowerInput": 50,
	},{
		"Name": "ArcSmelter",
		"Label": "Arc Smelter",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,0,2],[-1,0,2],[0,1,2],[-1,1,2]],
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["ElectricInput", "PowerInput"],
        "PowerInput": 100,
	},{
		"Name": "ChemicalBath",
		"Label": "Chemical Bath",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.new( 0, 0, 0 ))
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		""",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 100,
	},{
		"Name": "Sifter",
		"Label": "Sifter",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 50,
	},{
		"Name": "IndustrialChemReactor",
		"Label": "Chemical Reactor",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"Description": ["ElectricInput"],
	},{
		"Name": "Furnace",
		"Label": "Furnace",
		"StartTier": 0,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
        "Selector": "019/FurnaceSelector.FurnaceSelector_C",
		"Description": ["HeatOutput", "PowerOutput"],
        "PowerOutput": 50,
	},{
		"Name": "Oven",
		"Label": "Oven",
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],
			[0,1,0],[-2,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],
			[0,1,1],[-1,1,1],[-2,1,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],
			[0,-1,2],[-1,-1,2],[-2,-1,2],
		],
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["SpeedBonus", "HeatInput", "PowerInput"],
        "PowerInput": 100,
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
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["SpeedBonus"],
	},{
		"Name": "FluidFurnace",
		"Label": "Fluid Furnace",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "AutoCrafter",
		"BlockCreation":"""
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.up, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		""",
		"Description": ["FluidInput", "HeatOutput", "PowerOutput"],
        "PowerOutput": 200,
	},{
		"Name": "ElectricFurnace",
		"Label": "Electric Furnace",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.up, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		""",
		"Description": ["ElectricInput", "HeatOutput", "PowerOutput"],
		"PowerOutput": 250,
	},{
		"Name": "BatteryBox",
		"Label": "Battery Box",
		"StartTier": 3,
		"EndTier": 7,
        "BlockLogic": "BatteryContainerBlockLogic",
		"Description": ["ElectricConductor", "ElectricStorage"]
	},{
		 "Name": "Portal",
		 "Label": "Portal",
         "Description": ["PowerInput"],
		 "StartTier": 7,
		 "EndTier": 7,
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
	},
	{
		"Name": "DrillingRig",
		"Label": "Drilling Rig",
        "BlockLogic": "DrillingRig",
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],
			[0,1,0],[-1,1,0],[-2,1,0],
			[0,-1,0],[-1,-1,0],[-2,-1,0],
			
			[0,0,1],[-1,0,1],[-2,0,1],
			[0,1,1],[-1,1,1],[-2,1,1],
			[0,-1,1],[-1,-1,1],[-2,-1,1],
			
			[0,0,2],[-1,0,2],[-2,0,2],
			[0,1,2],[-1,1,2],[-2,1,2],
			
			[-1,0,3],
			[-1,1,3],
			
			[-1,0,4],
			[-1,1,4],
		],
		"StartTier": 1,
		"EndTier": 7,
		"Description": ["KineticInput", "ItemOutput"],
        "ItemLogic": "/Game/Equipped/DrillBP.DrillBP_C",
	},{
		"Name": "Assembler",
		"Label": "Assembler",
		"StartTier": 3,
		"EndTier": 7,
		"Positions": [
			[0,0,0],[-1,0,0],[-2,0,0],
			[0,0,1],[-1,0,1],[-2,0,1],
			
			[0,-1,0],[-1,-1,0],[-2,-1,0],
			[0,-1,1],[-1,-1,1],[-2,-1,1],
            
			[0,-2,0],[-1,-2,0],[-2,-2,0],
			[0,-2,1],[-1,-2,1],[-2,-2,1],
		],
		"Description": ["ElectricInput", "PowerInput"],
        "PowerInput": 160,
	},{
		"Name": "Constructor",
		"Label": "Constructor",
		"StartTier": 1,
		"EndTier": 7,
		"Positions": [
			[0,0,0],[-1,0,0],
			[0,0,1],[-1,0,1],
			
			[0,-1,0],[-1,-1,0],
			[0,-1,1],[-1,-1,1],
		],
		"BlockLogic":"SelectCrafter",
		"Description": ["ElectricInput", "PowerInput"],
        "PowerInput": 40,
	},{
		"Name": "Destroyer",
		"Label": "Destroyer",
		"Positions": [
			[0,0,0],[0,1,0],[0,2,0],
            [1,0,0],[1,1,0],[1,2,0],
            
			[0,0,1],[0,1,1],[0,2,1],
            [1,0,1],[1,1,1],[1,2,1],
		],
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic":"DumpCrafterBlockLogic",
		"Description": ["FluidInput"],
	},{
		"Name": "Lamp",
		"Label": "Lamp",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "LampBlockLogic",
	},{
		"Name": "AdminElectricGenerator",
		"Label": "Creative Electric Generator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["ElectricOutput"],
	},{
		"Name": "AdminItemGenerator",
		"Label": "Creative Item Generator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["ItemOutput"],
	},{
		"Name": "AdminKineticGenerator",
		"Label": "Creative Kinetic Generator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["KineticOutput"],
	},{
		"Name": "AdminHeatGenerator",
		"Label": "Creative Heat Generator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["HeatOutput"],
	},{
		"Name": "AdminFluidGenerator",
		"Label": "Creative Fluid Generator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["FluidOutput"],
	},{
		"Name": "AdminExterminator",
		"Label": "Creative Exterminator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["KineticInput", "HeatInput", "FluidInput", "ItemInput", "KineticInput"],
	},{
		"Name": "Electrolyzer",
		"Label": "Electrolyzer",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"Description": ["ElectricInput"],
	},{
		"Name": "Mixer",
		"Label": "Mixer",
		"StartTier": 2,
		"EndTier": 7,
		"Positions": [[0,0,0],[-1,0,0],[0,0,1],[-1,0,1]],
		"BlockLogic":"SelectCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 15,
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
		"EndTier": 7,
		"BlockLogic":"FarmBlockLogic",
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
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"Description": ["FluidOutput"],
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
		"Name": "RailStation",
		"Label": "Rail Station",
		"StartTier": 3,
		"EndTier": 7,
		"Positions": [[0,0,0],[-1,0,0],[-2,0,0],[-3,0,0]],
		"BlockLogic": "RailStationBlockLogic",
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
		"EndTier": 6,
		"BlockLogic":"ComputerBlockLogic",
		"Description": ["ElectricInput"],
	},{
		"Name": "Diode",
		"Label": "Diode",
		"StartTier": 2,
		"EndTier": 7,
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
	#	"EndTier": 7,
	#	"CommonTextKeys":[
	#		"Container"
	#	],
	#	"RequiredResearch":["LiquidsScan"+static_research],
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
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"CustomData":{
			"LoadIndependent": True,
			"StorageCapacity": 10000000,
			"StorageDrain": 80,
		},
		"Description": ["HeatOutput", "PowerOutput"],
	},{
		"Name": "FusionReactor",
		"Label": "Fusion Reactor",
        "Description": ["PowerInput"],
		"StartTier": 6,
		"EndTier": 7,
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
	},{
		"Name": "IndustrialBoiler",
		"Label": "Industrial Boiler",
		"StartTier": 5,
		"EndTier": 7,
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
		"BlockLogic":"SelectCrafter",
		"Description": ["FluidInput", "FluidOutput","PowerOutput"],
		"PowerOutput": fission_output(),
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
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"Description": ["ElectricOutput", "PowerOutput"],
		"PowerOutput": 800
	},
	{
		"Name": "SmallSolarPanel",
		"Label": "Small Solar Panel",
		"Positions": [
			[0,0,0],
			[0,-1,0],
			[0,0,1],
			[0,-1,1],
		],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"Description": ["ElectricOutput", "PowerOutput"],
		"PowerOutput": 80
	},
	{
		"Name": "Pumpjack",
		"Label": "Pumpjack",
        "BlockLogic":"Pumpjack",
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
		"StartTier": 4,
		"EndTier": 7,	
		"Description": ["KineticInput", "FluidOutput"],		
	},{
		"Name": "IndustrialSmelter",
		"Label": "Industrial Smelter",
		"StartTier": 4,
		"EndTier": 7,
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
		"Description": ["HeatInput", "PowerInput"],
        "PowerInput": 1000,
	},{
		"Name": "CreativeController",
		"Label": "Creative Controller",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["DataInput", "DataOutput"],
	},{
		"Name": "TeslaTower",
		"Label": "TeslaTower",
		"StartTier": 5,
		"EndTier": 7,		
        "BlockLogic":"SelectCrafter",
        "Positions": [
			[0,0,0],[1,0,0],[0,1,0],[1,1,0],
            [0,0,1],[1,0,1],[0,1,1],[1,1,1],
            [0,0,2],[1,0,2],[0,1,2],[1,1,2],
            [0,0,3],[1,0,3],[0,1,3],[1,1,3],
            [0,0,4],[1,0,4],[0,1,4],[1,1,4],
		]
	},{
        "Name": "KineticHeater",
        "Label": "Kinetic Heater",
        "StartTier": 1,
        "EndTier": 7,
        "Description": ["KineticInput", "HeatOutput", "PowerOutput"],
        "PowerOutput": 20,
        "BlockLogic":"SelectCrafter",
        "BlockCreation":"""
		local a = self:CreateAccessor(Class.find("KineticInputAccessor"))
		a:SetSidePos(Vec3i.left, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.right, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		""",
    },{
		"Name": "CableBundle",
		"Label": "Cable Bundle",
		"StartTier": 1,
		"EndTier": 1,		
        "BlockLogic":"CableBundleBlockLogic",
		"Description": ["ElectricConductor"],
        "CustomData":{
			"SplineMesh": "/Game/CoreContent/Rail2",
		}
	},{
		"Name": "Rails",
		"Label": "Rails",
		"StartTier": 2,
		"EndTier": 2,		
        "BlockLogic":"CableBundleBlockLogic",
		"Description": ["ElectricConductor"],
        "CustomData":{
			"SplineMesh": "/Game/CoreContent/Rail2",
		}
	}
]