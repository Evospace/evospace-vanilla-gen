## -*- coding: utf-8 -*-

from Common import *
from Materials import *

# Crafter block logics: list in each machine below (no implicit defaults in MachinesGen).
CRAFTING_LOGIC_EXPORTS = ["Working", "Progress", "InputInventory", "OutputInventory"]
CRAFTING_LOGIC_IMPORTS = ["Working"]

machines = [
	{
		"Name": "Macerator",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "AutoCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["KineticInput", "PowerInput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"RequiredResearch":["Fermentation"],
		"Description": ["ElectricInput", "PowerInput"],
	},{
		"Name": "Separator",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["KineticInput", "PowerInput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["KineticInput", "PowerInput"],
	},{
		"Name": "Boiler",
		"StartTier": 2,
		"EndTier": 7,
		"CommonTextKeys":[
			"Autocrafter"
		],
		"BlockLogic":"SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["HeatInput", "FluidInput", "FluidOutput", "PowerOutput"],
		"CustomData":{
			"StorageCapacity": 30000,
			"StorageDrain": 0,
		},
	},{
		"Name": "Pipe",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "ConductorBlockLogic",
		"LogicExports": ["Storage"],
		"Description": ["FluidConductor"],
		"PathFinding": True,
        "NoActorRenderable": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
        "Category": "Network",
	},{
		"Name": "HeatPipe",
		"StartTier": 1,
		"EndTier": 1,
		"BlockLogic": "HeatContainerBlockLogic",
		"Description": ["HeatConductor", "HeatStorage"],
		"PathFinding": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
        "Category": "Network",
	},{
		"Name": "PlasmaPipe",
		"StartTier": 4,
		"EndTier": 4,
		"BlockLogic": "HeatContainerBlockLogic",
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
		"LogicExports": ["Storage"],
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
		"LogicExports": ["Storage"],
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
		"LogicExports": ["Storage"],
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
		"LogicImports": ["Working"],
	},{
		"Name": "ElectricalSwitch",
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic": "ElectricitySwitchBlockLogic",
		"Description": ["ElectricConductor"],
		"LogicImports": ["Working"],
	},{
		"Name": "OreWasher",
		"Positions": [[0,0,0],[0,1,0],[-1,0,0],[-1,1,0],[-2,0,0],[-2,1,0],[0,0,1],[0,1,1],[-1,0,1],[-1,1,1],[-2,0,1],[-2,1,1]],
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["KineticInput", "PowerInput"],
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
		"LogicExports": ["Storage"],
		"Description": ["FluidConductor", "FluidStorage"],
	},{
		"Name": "StirlingEngine",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["HeatInput", "KineticOutput","PowerOutput"],
	},{
		"Name": "SteamEngine",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["FluidInput", "KineticOutput", "PowerOutput"],
	},{
		"Name": "CombustionEngine",
		"BlockLogic": "AutoCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["HeatInput", "PowerInput"],
	},{
		"Name": "Generator",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		 
	},{
		"Name": "CompactGenerator",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
	},{
		"Name": "ElectricEngine",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
        "Selector": "Blocks/ElectricEngineBP.ElectricEngineBP_C",
		"Description": ["ElectricInput", "KineticOutput", "PowerOutput"],
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
		"LogicImports": ["Working"],
	},{
		"Name": "Pump",
		"StartTier": 1,
		"EndTier": 7,
		"CustomData":{
			"ItemPortion": 1000
		},
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
		"Description": ["FluidInput", "FluidOutput"],
		"LogicImports": ["Working"],
	},{
		"Name": "Smelter",
		"StartTier": 0,
		"EndTier": 2,
		"BlockLogic":"AutoCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["FluidInput", "KineticOutput","PowerOutput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["FluidInput", "KineticOutput", "PowerOutput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["HeatOutput", "PowerOutput"],
	},{
		"Name": "DroneStation",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,0,2],[-1,0,2],[0,1,2],[-1,1,2]],
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"DroneStationBlockLogic",
		"Description": ["ElectricInput", "PowerInput"],
	},{
		"Name": "ArcSmelter",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,0,2],[-1,0,2],[0,1,2],[-1,1,2]],
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["ElectricInput", "PowerInput"],
	},{
		"Name": "ChemicalBath",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"BlockCreation":"""
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.new( 0, 0, 0 ))
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		""",
		"Description": ["KineticInput", "PowerInput"],
	},{
		"Name": "Sifter",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["KineticInput", "PowerInput"],
	},{
		"Name": "IndustrialChemReactor",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 7,
		"BlockLogic":"SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["ElectricInput"],
	},{
		"Name": "Furnace",
		"StartTier": 0,
		"EndTier": 7,
		"BlockLogic":"AutoCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["HeatOutput", "PowerOutput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["SpeedBonus", "HeatInput", "PowerInput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["SpeedBonus"],
	},{
		"Name": "FluidFurnace",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "AutoCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["FluidInput", "HeatOutput", "PowerOutput"],
	},{
		"Name": "ElectricFurnace",
		"StartTier": 2,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["ElectricInput", "HeatOutput", "PowerOutput"],
	},{
		"Name": "BatteryBox",
		"StartTier": 3,
		"EndTier": 7,
        "BlockLogic": "ElectricityContainerBlockLogic",
		"LogicExports": ["Storage"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["ElectricInput", "PowerInput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["ElectricInput"],
	},{
		"Name": "Mixer",
		"StartTier": 2,
		"EndTier": 7,
		"Positions": [[0,0,0],[-1,0,0],[0,0,1],[-1,0,1]],
		"BlockLogic":"SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["KineticInput", "PowerInput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["FluidOutput"],
	},{
		"Name": "Monitor",
		"StartTier": 4,
		"EndTier": 4,
		"BlockLogic": "MonitorBlockLogic",
		"Actor": "Blocks/MonitorBP.MonitorBP_C",
	},{
		"Name": "BigMonitor",
		"StartTier": 5,
		"EndTier": 5,
		"Image": "Monitor",
		"Positions": [[0,0,0],[0,-1,0],[0,0,1],[0,-1,1]],
		"BlockLogic": "MonitorBlockLogic",
		"Actor": "Blocks/BigMonitorBP.BigMonitorBP_C",
	},{
		"Name": "HugeMonitor",
		"StartTier": 6,
		"EndTier": 6,
		"Image": "Monitor",
		"Positions": [[0,0,0],[0,-1,0],[0,-2,0],[0,0,1],[0,-1,1],[0,-2,1],[0,0,2],[0,-1,2],[0,-2,2]],
		"BlockLogic": "MonitorBlockLogic",
		"Actor": "Blocks/HugeMonitorBP.HugeMonitorBP_C",
	},{
		"Name": "RailStation",
		"StartTier": 3,
		"EndTier": 7,
		"Positions": [[0,0,0],[-1,0,0],[-2,0,0],[-3,0,0]],
		"BlockLogic": "RailStationBlockLogic",
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["FluidInput", "FluidOutput","PowerOutput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["ElectricOutput", "PowerOutput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["ElectricOutput", "PowerOutput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
		"Description": ["HeatInput", "PowerInput"],
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
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
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
        "BlockLogic":"SelectCrafter",
		"LogicExports": CRAFTING_LOGIC_EXPORTS,
		"LogicImports": CRAFTING_LOGIC_IMPORTS,
    },{
		"Name": "Rails",
		"StartTier": 2,
		"EndTier": 2,		
        "BlockLogic":"CableBundleBlockLogic",
		"LogicExports": ["Storage"],
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
		"Name": "LogicSensor",
		"StartTier": 2,
		"EndTier": 2,
        "BlockLogic": "LogicSensorBlockLogic",
		"Description": []
	},{
		"Name": "LogicWire",
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic": "DataConductorBlockLogic",
		"LogicExports": ["Storage"],
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