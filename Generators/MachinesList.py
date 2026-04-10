## -*- coding: utf-8 -*-

from Common import *
from Materials import *

machines = [
	{
		"Name": "Macerator",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "AutoCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 20,
	}
	#,{
	#	"Name": "RollerMachine",
	#	
	#	"StartTier": 2,
	#	"EndTier": 4,
	#	"Description": "Unused.",
	#}
	,{
		"Name": "Fermenter",
		"StartTier": 3,
		"EndTier": 7,
		"Positions": [[0,0,0],[0,0,1]],
		"BlockLogic":"SelectCrafter",
		"RequiredResearch":["Fermentation"],
		"Description": ["ElectricInput", "PowerInput"],
        "PowerInput": 20,
	},{
		"Name": "Separator",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 80,
	},{
		"Name": "Spawner",
		"StartTier": 1,
		"EndTier": 1,
		"BlockLogic": "BedBlockLogic",
	},{
		"Name": "AutomaticHammer",
		"Positions": [[0,0,0],[0,0,1]],
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 30,
	},{
		"Name": "Boiler",
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
		"StartTier": 1,
		"EndTier": 1,
		"BlockLogic": "ConductorBlockLogic",
		"Description": ["HeatConductor", "HeatStorage"],
		"PathFinding": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
        "Category": "Network",
	},{
		"Name": "PlasmaPipe",
		"StartTier": 4,
		"EndTier": 4,
		"BlockLogic": "ConductorBlockLogic",
		"Description": ["HeatConductor", "HeatStorage"],
		"PathFinding": True,
        "ExactName": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
        "Category": "Network",
	},{
		"Name": "Flywheel",
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic": "KineticConductorBlockLogic",
		"Description": ["KineticConductor", "KineticStorage"],
		"PathFinding": True,
        "Category": "Network",
	},{
		"Name": "Sign",
		"StartTier": 0,
		"EndTier": 7,
		"BlockLogic": "SignBlockLogic",
	},{
		"Name": "AdvancedSign",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SignBlockLogic",
	},{
		"Name": "CopperConnector",
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
		"StartTier": 0,
		"EndTier": 7,
        "Description": ["ItemInput", "ItemStorage"],
		"LogicExports": ["ChestExportInventory"],
	},{
		"Name": "ItemRack",
		"Positions": [[0,0,0],[-1,0,0],[0,0,1],[-1,0,1]],
		"StartTier": 1,
		"EndTier": 7,
        "Description": ["ItemInput", "ItemStorage"],
	},{
		"Name": "Vent",
		"StartTier": 1,
		"EndTier": 1,
		"CommonTextKeys":[
			"Valve"
		],
		"BlockLogic": "FluidSwitchBlockLogic",
		"Description": ["FluidConductor"],
	},{
		"Name": "ElectricalSwitch",
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic": "ElectricitySwitchBlockLogic",
		"Description": ["ElectricConductor"],
	},{
		"Name": "OreWasher",
		"Positions": [[0,0,0],[0,1,0],[-1,0,0],[-1,1,0],[-2,0,0],[-2,1,0],[0,0,1],[0,1,1],[-1,0,1],[-1,1,1],[-2,0,1],[-2,1,1]],
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 20,
	},{
		"Name": "Conveyor",
		"StartTier": 1,
		"EndTier": 7,
		"CommonTextKeys":[
			"Conveyor",
			"Transporter"
		],
		"Selector": "Blocks/ArrowConvBP.ArrowConvBP_C",
		"PathFinding": True,
        "NoActorRenderable": True,
        "ReplaceTag": "Conveyor",
	},{
		"Name": "Splitter",
		"StartTier": 1,
		"EndTier": 7,
		"Description": ["Splitter"],
        "ReplaceTag": "Conveyor",
	},{
		"Name": "Sorter",
		"StartTier": 2,
		"EndTier": 7,
		"Description": ["Splitter", "Sorter"],
        "ReplaceTag": "Conveyor",
	},{
		"Name": "Container",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "FluidContainerBlockLogic",
		"Description": ["FluidConductor", "FluidStorage"],
	},{
		"Name": "StirlingEngine",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["HeatInput", "KineticOutput","PowerOutput"],
		"PowerOutput": 50,
	},{
		"Name": "SteamEngine",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["FluidInput", "KineticOutput", "PowerOutput"],
		"PowerOutput": 200,
	},{
		"Name": "CombustionEngine",
		"BlockLogic": "AutoCrafter",
		"StartTier": 4,
		"EndTier": 7,
        "Description": ["FluidInput", "KineticOutput", "PowerOutput"],
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,2,0],[-1,2,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,2,1],[-1,2,1]],
	},{
		"Name": "FractionatingColumn",
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
		"Positions": [[0,0,0],[0,0,1],[0,1,0],[0,2,0]],
		"StartTier": 4,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["HeatInput", "PowerInput"],
        "PowerInput": 50,
	},{
		"Name": "Generator",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		"PowerOutput": 200 * 5 * 2,
	},{
		"Name": "IndustrialGenerator",
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
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		"PowerOutput": 50,
	},{
		"Name": "ElectricEngine",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
        "Selector": "Blocks/ElectricEngineBP.ElectricEngineBP_C",
		"Description": ["ElectricInput", "KineticOutput", "PowerOutput"],
		"PowerOutput": 100,
        "DefaultRotation": [-1, 0, 0, 0]
	},{
		"Name": "Loader",
		"StartTier": 1,
		"EndTier": 7,
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
	},{
		"Name": "RobotArm",
		"StartTier": 1,
		"EndTier": 7,
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
	},{
		"Name": "Pump",
		"StartTier": 1,
		"EndTier": 7,
		"CustomData":{
			"ItemPortion": 1000
		},
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
		"Description": ["FluidInput", "FluidOutput"],
	},{
		"Name": "Smelter",
		"StartTier": 0,
		"EndTier": 2,
		"BlockLogic":"AutoCrafter",
		"Description": ["HeatInput", "PowerInput"],
		"CustomData":{
			"Capacity":32
		}
	},{
		"Name": "SteamTurbine",
		"Positions": [[0,0,0],[-1,0,0],[-2,0,0],[0,-1,0],[-1,-1,0],[-2,-1,0],[0,0,1],[-1,0,1],[-2,0,1],[0,-1,1],[-1,-1,1],[-2,-1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["FluidInput", "KineticOutput","PowerOutput"],
		"PowerOutput": 200 * 5 * 2,
	},{
		"Name": "IndustrialSteamTurbine",
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
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,0,2],[-1,0,2],[0,1,2],[-1,1,2]],
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"DroneStationBlockLogic",
		"Description": ["ElectricInput", "PowerInput"],
        "PowerInput": 50,
	},{
		"Name": "ArcSmelter",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,0,2],[-1,0,2],[0,1,2],[-1,1,2]],
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["ElectricInput", "PowerInput"],
        "PowerInput": 100,
	},{
		"Name": "ChemicalBath",
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
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 50,
	},{
		"Name": "IndustrialChemReactor",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"Description": ["ElectricInput"],
	},{
		"Name": "Furnace",
		"StartTier": 0,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"Description": ["HeatOutput", "PowerOutput"],
        "PowerOutput": 50,
	},{
		"Name": "Oven",
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
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "AutoCrafter",
		"Description": ["FluidInput", "HeatOutput", "PowerOutput"],
        "PowerOutput": 200,
	},{
		"Name": "ElectricFurnace",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"Description": ["ElectricInput", "HeatOutput", "PowerOutput"],
		"PowerOutput": 250,
	},{
		"Name": "BatteryBox",
		"StartTier": 3,
		"EndTier": 7,
        "BlockLogic": "ElectricityContainerBlockLogic",
		"Description": ["ElectricConductor", "ElectricStorage"]
	},{
		 "Name": "Portal",
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
        "ItemLogic": "/Game/Equipped/DrillBuildingTool.DrillBuildingTool_C",
	},{
		"Name": "Assembler",
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
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "LampBlockLogic",
	},{
		"Name": "AdminElectricGenerator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["ElectricOutput"],
	},{
		"Name": "AdminItemGenerator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["ItemOutput"],
	},{
		"Name": "AdminKineticGenerator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["KineticOutput"],
	},{
		"Name": "AdminHeatGenerator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["HeatOutput"],
	},{
		"Name": "AdminFluidGenerator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["FluidOutput"],
	},{
		"Name": "AdminExterminator",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["KineticInput", "HeatInput", "FluidInput", "ItemInput", "KineticInput"],
	},{
		"Name": "Electrolyzer",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"Description": ["ElectricInput"],
	},{
		"Name": "Mixer",
		"StartTier": 2,
		"EndTier": 7,
		"Positions": [[0,0,0],[-1,0,0],[0,0,1],[-1,0,1]],
		"BlockLogic":"SelectCrafter",
		"Description": ["KineticInput", "PowerInput"],
        "PowerInput": 15,
	},{
		"Name": "AutomaticFarm",
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
		"BlockLogic":"SelectCrafter",
		"Description": ["FluidInput"],
	},{
		"Name": "AtmosphericCondenser",
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
		"StartTier": 4,
		"EndTier": 4,
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "BigTerminal",
		"StartTier": 5,
		"EndTier": 5,
		"Image": "Terminal",
		"Positions": [[0,0,0],[0,-1,0],[0,0,1],[0,-1,1]],
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "HugeTerminal",
		"StartTier": 6,
		"EndTier": 6,
		"Image": "Terminal",
		"Positions": [[0,0,0],[0,-1,0],[0,-2,0],[0,0,1],[0,-1,1],[0,-2,1],[0,0,2],[0,-1,2],[0,-2,2]],
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "FlatTerminal",
		"StartTier": 4,
		"EndTier": 4,
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "BigFlatTerminal",
		"StartTier": 5,
		"EndTier": 5,
		"Image": "FlatTerminal",
		"Positions": [[0,0,0],[0,-1,0],[0,0,1],[0,-1,1]],
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "RailStation",
		"StartTier": 3,
		"EndTier": 7,
		"Positions": [[0,0,0],[-1,0,0],[-2,0,0],[-3,0,0]],
		"BlockLogic": "RailStationBlockLogic",
	},{
		"Name": "HugeFlatTerminal",
		"StartTier": 6,
		"EndTier": 6,
		"Image": "FlatTerminal",
		"Positions": [[0,0,0],[0,-1,0],[0,-2,0],[0,0,1],[0,-1,1],[0,-2,1],[0,0,2],[0,-1,2],[0,-2,2]],
		"BlockLogic": "MonitorBlockLogic",
	},{
		"Name": "Computer",
		"StartTier": 1,
		"EndTier": 6,
		"BlockLogic":"ComputerBlockLogic",
		"Description": ["ElectricInput"],
	},{
		"Name": "Diode",
		"StartTier": 2,
		"EndTier": 7,
		"Description": ["ElectricInput", "ElectricOutput"],
	},
	#,{
	#	"Name": "Tank",
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
        "Description": ["PowerInput"],
        "BlockLogic":"SelectCrafter",
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
		"ItemLogic": "/Game/Equipped/PumpjackBuildingTool.PumpjackBuildingTool_C",
	},{
		"Name": "Pumpjack_leg",
		"ExactName": True,
		"BlockLogic":"Pumpjack",
		"Actor": "Blocks/PumpjackBP.PumpjackBP_C",
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
		"EndTier": 4,
		"Description": ["KineticInput", "FluidOutput"],
	},{
		"Name": "IndustrialSmelter",
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
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["DataInput", "DataOutput"],
	},{
		"Name": "TeslaTower",
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
        "StartTier": 1,
        "EndTier": 7,
        "Description": ["KineticInput", "HeatOutput", "PowerOutput"],
        "PowerOutput": 20,
        "BlockLogic":"SelectCrafter",
    },{
		"Name": "Rails",
		"StartTier": 2,
		"EndTier": 2,		
        "BlockLogic":"CableBundleBlockLogic",
		"Description": ["ElectricConductor"],
        "CustomData":{
			"SplineMesh": "/Game/CoreContent/Rail2",
		}
	},{
		"Name": "LogicInterface",
		"StartTier": 2,
		"EndTier": 2,
        "BlockLogic": "LogicInterfaceBlockLogic",
		"Description": []
	},{
		"Name": "LogicWire",
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic": "ConductorBlockLogic",
		"Description": ["DataConductor"],
		"PathFinding": True,
        "NoActorRenderable": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
        "Category": "Network",
	},{
		"Name": "StorageCore",
		"StartTier": 2,
		"EndTier": 2,		
        "BlockLogic": "ItemRack",
		"Description": []
	}
]