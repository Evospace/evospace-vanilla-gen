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
        "Recipes": "Macerator",
		"Description": ["KineticInput"],
	},{
		"Name": "CuttingMachine",
		"Label": "Cutting Machine",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
        "Recipes": "CuttingMachine",
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
		"StartTier": 3,
		"EndTier": 10,
		"Positions": [[0,0,0],[0,0,1]],
		"BlockLogic":"SelectCrafter",
		"RequiredResearch":["Fermentation"+static_research],
		"Description": ["ElectricInput"],
	},{
		"Name": "ChemReactor",
		"Label": "Chemical Reactor",
		"StartTier": 2,
		"EndTier": 10,		
		"BlockLogic":"SelectCrafter",
		"Description": ["ElectricInput"],
	},{
		"Name": "Separator",
		"Label": "Separator",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"Description": ["KineticInput"],
	},{
		"Name": "Beam",
		"Label": "Beam",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "BlockLogic",
		"Description": ["BuildingBlock"],
	},{
		"Name": "Corner",
		"Label": "Corner",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "SimpleInstancedBlockLogic",
		"Description": ["BuildingBlock"]
	},{
		"Name": "AutomaticHammer",
		"Label": "Automatic Hammer",
		"Positions": [[0,0,0],[0,0,1]],
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
        "Recipes": "AutomaticHammer",
		"Description": ["KineticInput"],
	},{
		"Name": "Boiler",
		"Label": "Boiler",
		"StartTier": 2,
		"EndTier": 10,
		"CommonTextKeys":[
			"Autocrafter"
		],
		"BlockLogic":"NuclearReactorBlockLogic",
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
		"Description": ["FluidConductor"],
		"PathFinding": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
	},{
		"Name": "HeatPipe",
		"Label": "Heat Pipe",
		"StartTier": 1,
		"EndTier": 1,
		"BlockLogic": "HeatConductorBlockLogic",
		"Description": ["HeatConductor", "HeatStorage"],
		"PathFinding": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
	},{
		"Name": "Flywheel",
		"Label": "Flywheel",
		"StartTier": 2,
		"EndTier": 2,
		"BlockLogic": "KineticConductorBlockLogic",
		"Description": ["KineticConductor", "KineticStorage"],
		"PathFinding": True,
	},{
		"Name": "Scaffold",
		"Label": "Scaffold",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "SimpleInstancedBlockLogic",
		"Description": ["BuildingBlock"],
	},{
		"Name": "Sign",
		"Label": "Sign",
		"StartTier": 0,
		"EndTier": 10,
		"BlockLogic": "SignBlockLogic",
	},{
		"Name": "AdvancedSign",
		"Label": "Advanced Sign",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SignBlockLogic",
	},{
		"Name": "Connector",
		"Label": "Cable",
		"StartTier": 1,
		"EndTier": 1,
		"BlockLogic": "ElectricityConductorBlockLogic",
        "Description": ["ElectricConductor"],
		"PathFinding": True,
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
	},{
		"Name": "Chest",
		"Label": "Chest",
		"StartTier": 0,
		"EndTier": 10,
        "Description": ["ItemInput", "ItemStorage"],
	},{
		"Name": "ItemRack",
		"Label": "Item Rack",
		"Positions": [[0,0,0],[-1,0,0],[0,0,1],[-1,0,1]],
		"StartTier": 1,
		"EndTier": 10,
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
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
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
		"Selector": "Blocks/ArrowConvBP.ArrowConvBP_C",
		"PathFinding": True,
	},{
		"Name": "Splitter",
		"Label": "Splitter",
		"StartTier": 1,
		"EndTier": 10,
		"Description": ["Splitter"],
	},{
		"Name": "Sorter",
		"Label": "Sorter",
		"StartTier": 2,
		"EndTier": 10,
		"Description": ["Splitter", "Sorter"],
	},{
		"Name": "Container",
		"Label": "Container",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "FluidContainerBlockLogic",
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
        local crafter = AbstractCrafter.cast(self)
        
        local inv = ResourceInventory.new(crafter, "InputInv")
        inv.item = StaticItem.find("Kinetic")
        inv.capacity = 20
        crafter.energy_input_inventory = inv
        
        local acc = ResourceAccessor.new(crafter, "Input1")
        acc.side, acc.pos = Vec3i.back, Vec3i.zero
        acc.inventory = inv
        acc.is_input = true
        acc.channel = "Kinetic"
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
	#	
	#	
	#	local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
	#	a:SetSidePos(Vec3i.left, Vec3i.zero)
	#	a:Bind(self:GetInputContainer())
	#	
	#	local a = self:CreateAccessor(Class.find("FluidOutputAccessor"))
	#	a:SetSidePos(Vec3i.right, Vec3i.zero)
	#	a:Bind(self:GetOutputContainer())
	#	""",
	#	 
	#}
	,{
		"Name": "StirlingEngine",
		"Label": "Stirling Engine",
		"StartTier": 1,
		"EndTier": 10,
        "Recipes": "StirlingEngine",
		"BlockLogic": "SelectCrafter",
		"Description": ["HeatInput", "KineticOutput","PowerOutput"],
		"PowerOutput": 10,
	},{
		"Name": "CombustionEngine",
		"Label": "Combustion Engine",
		"BlockLogic": "SelectCrafter",
		"StartTier": 2,
		"EndTier": 10,
		"Description": ["FluidInput", "KineticOutput"],
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""local a = self:new_resource_accessor("Output")
		a:SetSidePos(Vec3i.right, Vec3i.new(-1,0,0))
        local res = self:get_resource_component()
		a:bind_output(res)
        res.output = 20
        res.output_item = StaticItem.find("Kinetic")
		""",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,2,0],[-1,2,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,2,1],[-1,2,1]],
	},{
		"Name": "OilCrackingTower",
		"Label": "Oil Cracking Tower",
		"StartTier": 4,
		"EndTier": 10,
		"Description": ["ElectricInput", "FluidInput", "FluidOutput"],
		"BlockLogic": "SelectCrafter",
		"Positions": [[0,0,0],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[1,1,0],[-1,-1,0],[1,-1,0],[-1,1,0],
                [0,0,1],[1,0,1],[-1,0,1],[0,1,1],[0,-1,1],[1,1,1],[-1,-1,1],[1,-1,1],[-1,1,1],
                [0,0,2],[1,0,2],[-1,0,2],[0,1,2],[0,-1,2],[1,1,2],[-1,-1,2],[1,-1,2],[-1,1,2],
                [0,0,3],[1,0,3],[-1,0,3],[0,1,3],[0,-1,3],[1,1,3],[-1,-1,3],[1,-1,3],[-1,1,3],
                [0,0,4],[1,0,4],[-1,0,4],[0,1,4],[0,-1,4],[1,1,4],[-1,-1,4],[1,-1,4],[-1,1,4],
                [0,0,5],[1,0,5],[-1,0,5],[0,1,5],[0,-1,5],[1,1,5],[-1,-1,5],[1,-1,5],[-1,1,5],
                [0,0,6],[1,0,6],[-1,0,6],[0,1,6],[0,-1,6],[1,1,6],[-1,-1,6],[1,-1,6],[-1,1,6],
                [0,0,7],[1,0,7],[-1,0,7],[0,1,7],[0,-1,7],[1,1,7],[-1,-1,7],[1,-1,7],[-1,1,7]],
        "BlockCreation":"""
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.back, Vec3i.new( -1, 0, 0 ))
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Electricity")
		""",
	},{
		"Name": "PyrolysisUnit",
		"Label": "Pyrolysis Unit",
		"Positions": [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,2,0]],
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"Description": ["HeatInput"],
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
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		"PowerOutput": 243,
		 
	},{
		"Name": "IndustrialGenerator",
		"Label": "Industrial Generator",
		"Positions": [[0,0,0],[1,0,0],[-1,0,0],[0,1,0],[1,1,0],[-1,1,0],[0,-1,0],[1,-1,0],[-1,-1,0],
		[0,0,1],[1,0,1],[-1,0,1],[0,1,1],[1,1,1],[-1,1,1],[0,-1,1],[1,-1,1],[-1,-1,1],
		[0,0,2],[1,0,2],[-1,0,2],[0,1,2],[1,1,2],[-1,1,2],[0,-1,2],[1,-1,2],[-1,-1,2],
        [-1,-2,0],[0,-2,0],[1,-2,0],[-1,-2,1],[0,-2,1],[1,-2,1],[-1,-2,2],[0,-2,2],[1,-2,2]],
		"StartTier": 5,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""local res = self:get_resource_component()
        res.input_item = StaticItem.find("Kinetic")
        res.output_item = StaticItem.find("Electricity")
		local a = self:new_resource_accessor("KineticInputAccessor")
		a:SetSidePos(Vec3i.right, Vec3i.new( 0, -2, 0 ))
		a:bind_input(res)
		local a = self:new_resource_accessor("ElectricOutputAccessor")
		a:SetSidePos(Vec3i.left, Vec3i.new( 0, 1, 0 ))		
		a:bind_output(res)
		""",
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		"PowerOutput": 243*20,
		 
	},{
		"Name": "CompactGenerator",
		"Label": "Compact Generator",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
        "Recipes": "CompactGenerator",
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		"PowerOutput": 18,
	},{
		"Name": "ElectricEngine",
		"Label": "Electric Engine",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
        "Selector": "Blocks/ElectricEngineBP.ElectricEngineBP_C",
		"Description": ["ElectricInput", "KineticOutput", "PowerOutput"],
		"PowerOutput": 55,
        "DefaultRotation": [-1, 0, 0, 0]
	},{
		"Name": "BiElectricEngine",
        "Recipes": "ElectricEngine",
		"Label": "Bi-Directional Electric Engine",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
		local a = self:CreateAccessor(Class.find("KineticOutputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("KineticOutputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.zero)
		a:Bind(self:GetInputContainer())
        """,
		"Description": ["ElectricInput", "KineticOutput", "PowerOutput"],
		"PowerOutput": 55,
        "DefaultRotation": [-1, 0, 0, 0]
	},{
		"Name": "IndustrialElectricEngine",
		"Label": "Industrial Electric Engine",
		"StartTier": 4,
		"EndTier": 10,
		"Positions": [[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,0,1],[1,0,1],[0,1,1],[1,1,1]],
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("KineticOutputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(1,0,0))
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.right, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		""",
		"Description": ["ElectricInput", "KineticOutput", "PowerOutput"],
		"PowerOutput": 55*50,
	},{
		"Name": "RobotArm",
		"Label": "Robot Arm",
		"StartTier": 1,
		"EndTier": 10,
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
	},{
		"Name": "Pump",
		"Label": "Pump",
		"StartTier": 1,
		"EndTier": 10,
		"CustomData":{
			"ItemPortion": 1000
		},
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
		"Description": ["FluidInput", "FluidOutput"],
	},{
		"Name": "OverflowPump",
		"Label": "Overflow Pump",
		"StartTier": 1,
		"EndTier": 10,
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
        "Recipes": "Smelter",
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
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(0, 0, 0))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("KineticOutputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.new(-5, -1, 0))
		a:Bind(self:GetOutputContainer())
		""",
		"Description": ["FluidInput", "KineticOutput","PowerOutput"],
		"PowerOutput": fission_fullpower * 0.9 * 0.9,
	},{
		"Name": "GasTurbine",
		"Label": "Gas Turbine",
		"Positions": [[0,0,0],[-1,0,0],[-2,0,0],[-3,0,0],[0,-1,0],[-1,-1,0],[-2,-1,0],[-3,-1,0],[0,0,1],[-1,0,1],[-2,0,1],[-3,0,1],[0,-1,1],[-1,-1,1],[-2,-1,1],[-3,-1,1]],
		"StartTier": 4,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
        "Recipes": "GasTurbine",
		"BlockCreation":"""
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.up, Vec3i.new( -2, 0, 1 ))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.new( -1, -1, 1 ))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("KineticOutputAccessor"))
		a:SetSidePos(Vec3i.right, Vec3i.new( -3, -1, 0 ))
		a:Bind(self:GetOutputContainer())
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
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.new( 0, 0, 0 ))
		a:Bind(self:GetOutputContainer())
		a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.up, Vec3i.new( 0, 0, 1 ))
		a:Bind(self:GetOutputContainer())
		""",
		"Description": ["HeatOutput", "PowerOutput"],
		"PowerOutput": 500,
	},{
		"Name": "ArcSmelter",
		"Label": "Arc Smelter",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1],[0,0,2],[-1,0,2],[0,1,2],[-1,1,2]],
		"StartTier": 2,
		"EndTier": 10,
        "Recipes": "ArcSmelter",
		"BlockLogic":"AutoCrafter",
		"Description": ["ElectricInput", "PowerInput"],
        "PowerInput": 100,
	},{
		"Name": "ChemicalBath",
		"Label": "Chemical Bath",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 10,
        "Recipes": "ChemicalBath",
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.new( 0, 0, 0 ))
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "Sifter",
		"Label": "Sifter",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
        "Recipes": "Sifter",
		"BlockCreation":"""
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.zero)
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "IndustrialChemReactor",
		"Label": "Industrial Chemical Reactor",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"Description": ["ElectricInput"],
	},{
		"Name": "Furnace",
		"Label": "Furnace",
		"StartTier": 0,
		"EndTier": 10,
		"BlockLogic":"Furnace",
        "Recipes": "Furnace",
        "Selector": "019/FurnaceSelector.FurnaceSelector_C",
		"Description": ["HeatOutput"],
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
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
        "Recipes": "Oven",
		"Description": ["SpeedBonus"]
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
        "Recipes": "BlastFurnace",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"Description": ["SpeedBonus"],
	},{
		"Name": "FluidFurnace",
		"Label": "Fluid Furnace",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic": "AutoCrafter",
		"BlockCreation":"""
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.up, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		""",
		"Description": ["FluidInput", "HeatOutput"],
	},{
		"Name": "ElectricFurnace",
		"Label": "Electric Furnace",
		"StartTier": 2,
		"EndTier": 10,
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
		"PowerOutput": 40,
	},{
		"Name": "BatteryBox",
		"Label": "Battery Box",
		"StartTier": 3,
		"EndTier": 10,
        "BlockLogic": "BatteryContainerBlockLogic",
		"Description": ["ElectricConductor", "ElectricStorage"]
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
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(0,1,1))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.left, Vec3i.new(0,1,1))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(0,-5,1))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.right, Vec3i.new(0,-5,1))
		a:Bind(self:GetInputContainer())
		""",
	},
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
        "Recipes": "Assembler",
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
        "Recipes": "Hand",
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.zero)
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Electricity")
		""",
		"Description": ["ElectricInput"],
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
		"EndTier": 10,
		"BlockLogic":"DumpCrafterBlockLogic",
		"Description": ["FluidInput"],
	},{
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
		"Description": ["ElectricInput"],
	},{
		"Name": "Mixer",
		"Label": "Mixer",
		"StartTier": 2,
		"EndTier": 10,
		"Positions": [[0,0,0],[-1,0,0],[0,0,1],[-1,0,1]],
		"BlockLogic":"SelectCrafter",
		"Description": ["KineticInput"],
	},{
		"Name": "AutomaticFarm",
		"Label": "Automatic Farm",
        "Recipes": "AutomaticFarm",
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
		"Description": ["FluidInput"],
	},{
		"Name": "AtmosphericCondenser",
		"Label": "Atmospheric Condenser",
        "Recipes": "AtmosphericCondenser",
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
		"EndTier": 10,
		"BlockLogic":"ComputerBlockLogic",
		"Description": ["ElectricInput"],
	},{
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
		"Description": ["KineticInput"],
	},{
		"Name": "Radiator",
		"Label": "Radiator",
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.down, Vec3i.zero)
        local res = self:get_resource_component()
		a:Bind(res)
        res.input = 20
        res.input_item = StaticItem.find("Heat")
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
		"EndTier": 10,
		"BlockLogic":"NuclearReactorBlockLogic",
		"BlockCreation":"""
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.left, Vec3i.new(0, 1, 0))
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(0, 1, 0))
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(0, -2, 0))
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.right, Vec3i.new(0, -2, 0))
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.left, Vec3i.new(-3, 1, 0)) 
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.new(-3, 1, 0))
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.new(-3, -2, 0))
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.right, Vec3i.new(-3, -2, 0))
		a:Bind(self:GetOutputContainer())
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
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(0, 1, 0))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.left, Vec3i.new(0, 1, 0))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(0, -3, 0))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.right, Vec3i.new(0, -3, 0))
		a:Bind(self:GetInputContainer())
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
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.up, Vec3i.new(0, -1, 2))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.new(0, -1, 0))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.new(-1, -1, 0))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.new(-2, -1, 0))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.new(-3, -1, 0))
		a:Bind(self:GetInputContainer())
		a = self:CreateAccessor(Class.find("FluidOutputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.new(-3, 0, 0))
		a:Bind(self:GetOutputContainer())
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
		"BlockLogic":"BigSolarPanel",
		"Description": ["ElectricOutput", "PowerOutput"],
		"PowerOutput": 800,
        "CustomData": {
            "Power": 800
		}
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
		"EndTier": 10,
		"BlockLogic":"SolarPanel",
		"Description": ["ElectricOutput", "PowerOutput"],
		"PowerOutput": 80,
        "CustomData": {
            "Power": 80
		}
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
	#	
	#	
	#	local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
	#	a:SetSidePos(Vec3i.left, Vec3i.zero)
	#	a:Bind(self:GetInputContainer())
	#	
	#	local a = self:CreateAccessor(Class.find("FluidOutputAccessor"))
	#	a:SetSidePos(Vec3i.right, Vec3i.zero)
	#	a:Bind(self:GetOutputContainer())
	#	
	#	local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
	#	a:SetSidePos(Vec3i.up, Vec3i.zero)
	#	a:Bind(self:GetOutputContainer())
	#	""",
	#	"RequiredResearch":["HeatTransferring"+static_research],
	#}
	#,{
	#	"Name": "InverseHeatExchanger",
	#	"Label": "Inverse Heat Exchanger",
	#	"StartTier": 1,
	#	"EndTier": 10,
	#	"BlockLogic":"SelectCrafter",
	#	"BlockCreation":"""
	#	
	#	
	#	local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
	#	a:SetSidePos(Vec3i.left, Vec3i.zero)
	#	a:Bind(self:GetInputContainer())
	#	
	#	local a = self:CreateAccessor(Class.find("FluidOutputAccessor"))
	#	a:SetSidePos(Vec3i.right, Vec3i.zero)
	#	a:Bind(self:GetOutputContainer())
	#	
	#	local a = self:CreateAccessor(Class.find("HeatInputAccessor"))
	#	a:SetSidePos(Vec3i.down, Vec3i.zero)
	#	a:Bind(self:GetInputContainer())
	#	""",
	#	"RequiredResearch":["HeatTransferring"+static_research],
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
        local crafter = AbstractCrafter.cast(self)
        
        local inv = ResourceInventory.new(crafter, "InputInv")
        inv.item = StaticItem.find("Heat")
        inv.input = 20
        crafter.energy_input_inventory = inv
        
        local acc = ResourceAccessor.new(crafter, "Input")
        acc.side = Vec3i.front
        acc.pos = Vec3i.zero
        acc.inventory = inv
		""",
		"Description": ["ElectricInput", "HeatOutput"],
	},{
		"Name": "CreativeController",
		"Label": "Creative Controller",
		"StartTier": 7,
		"EndTier": 7,
		"Description": ["DataInput", "DataOutput"],
        "Craftable": False,
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
        "Selector": "Blocks/AllSidesPipeBP.AllSidesPipeBP_C",
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
	},
    {
        "Name": "KineticHeater",
        "Label": "Kinetic Heater",
        "StartTier": 1,
        "EndTier": 10,
        "Description": ["KineticInput", "HeatOutput", "PowerOutput"],
        "PowerOutput": 9,
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