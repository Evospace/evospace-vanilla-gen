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
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        local input = crafter.resource_input_inventory
        input.item = StaticItem.find("Kinetic")
        input.input = 20
        input.capacity = 20
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.down
        acc.pos = Vec3i.back
        acc.inventory = input
		end
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "CuttingMachine",
		"Label": "Cutting Machine",
		"StartTier": 1,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        local input = crafter.resource_input_inventory
        input.item = StaticItem.find("Kinetic")
        input.input = 20
        input.capacity = 20
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.back
        acc.pos = Vec3i.zero
        acc.inventory = input
		end
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
		"StartTier": 3,
		"EndTier": 10,
		"Positions": [[0,0,0],[0,0,1]],
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        local input = crafter.resource_input_inventory
        input.item = StaticItem.find("Electricity")
        input.input = 20
        input.capacity = 20
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.back
        acc.pos = Vec3i.zero
        acc.inventory = input
		end
		""",
		"RequiredResearches":["Fermentation"+static_research],
		"Description": ["ElectricInput"],
	},{
		"Name": "ChemReactor",
		"Label": "Chemical Reactor",
		"StartTier": 2,
		"EndTier": 10,		
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        local input = crafter.resource_input_inventory
        input.item = StaticItem.find("Electricity")
        input.input = 20
        input.capacity = 20
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.back
        acc.pos = Vec3i.zero
        acc.inventory = input
		end
		""",
		"Description": ["ElectricInput"],
	},{
		"Name": "Separator",
		"Label": "Separator",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":"""
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        local input = crafter.resource_input_inventory
        input.item = StaticItem.find("Kinetic")
        input.input = 20
        input.capacity = 20
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.back
        acc.pos = Vec3i.zero
        acc.inventory = input
		end
		""",
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
		"BlockCreation":"""
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        
        local input = crafter.resource_input_inventory
        input.item = StaticItem.find("Kinetic")
        input.input = 20
        input.capacity = 20
        
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.back
        acc.pos = Vec3i.zero
        acc.inventory = input
		end
		""",
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
		"BlockCreation":"""
		return function(self)
		local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.back, Vec3i.zero)
        local b = self:new_resource_accessor("Output")
        b:SetSidePos(Vec3i.up, Vec3i.zero)
        local res = self:get_resource_component()
		a:bind_input(res)
        b:bind_output(res)
        res.input = 20
        res.output = 20
        res.input_item = StaticItem.find("Heat")
        res.output_item = StaticItem.find("Steam")
        
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos()
		a:Bind(self:GetInputContainer())
		end
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
		"BlockLogic": "ElectricConductorBlockLogic",
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
		"BlockLogic": "ElectricSwitchBlockLogic",
		"Description": ["ElectricConductor"],
	},{
		"Name": "OreWasher",
		"Label": "Ore Washer",
		"Positions": [[0,0,0],[0,1,0],[-1,0,0],[-1,1,0],[-2,0,0],[-2,1,0],[0,0,1],[0,1,1],[-1,0,1],[-1,1,1],[-2,0,1],[-2,1,1]],
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic":"AutoCrafter",
		"BlockCreation":""" -----------
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.new(0,1,0))
        local res = self:get_resource_component()
		a:Bind(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.back, Vec3i.zero)
        local res = self:get_resource_component()
		a:Bind(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		end
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
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        local input = crafter.resource_input_inventory
        input.item = StaticItem.find("Kinetic")
        input.input = 20
        input.capacity = 20
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.back
        acc.pos = Vec3i.zero
        acc.inventory = input
		end
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
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
		return function(self)
-------
		local a = self:CreateAccessor(Class.find("HeatInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("KineticOutputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		end
		""",
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
		"BlockCreation":"""
		return function(self)
		local a = self:new_resource_accessor("Output")
		a:SetSidePos(Vec3i.right, Vec3i.new(-1,0,0))
        local res = self:get_resource_component()
		a:bind_output(res)
        res.output = 20
        res.output_item = StaticItem.find("Kinetic")
		end
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
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.back, Vec3i.new( -1, 0, 0 ))
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Electricity")
		end
		""",
	},{
		"Name": "PyrolysisUnit",
		"Label": "Pyrolysis Unit",
		"Positions": [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,2,0]],
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        local input = crafter.resource_input_inventory
        input.item = StaticItem.find("Heat")
        input.input = 20
        input.capacity = 20
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.down
        acc.pos = Vec3i.zero
        acc.inventory = input
		end
		""",
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
		"BlockCreation":"""
		return function(self)		
        local crafter = AbstractCrafter.cast(self)
        local inv = crafter.resource_input_inventory
        inv.item = StaticItem.find("Kinetic")
        inv.input = 20
        inv.capacity = 20
        
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.back
        acc.pos = Vec3i.new( -1, 1, 0 )
        acc.inventory = inv
        
        inv = crafter.resource_output_inventory
        inv.item = StaticItem.find("Electricity")
        inv.output = 20
        
    	acc = ResourceAccessor.new(crafter, "Output")
        crafter:reg(acc)
        acc.side = Vec3i.front
        acc.pos = Vec3i.zero
        acc.inventory = inv
		end
		""",
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
		"BlockCreation":"""
		return function(self)
		local res = self:get_resource_component()
        res.input = 20
        res.output = 20
        res.input_item = StaticItem.find("Kinetic")
        res.output_item = StaticItem.find("Electricity")
		local a = self:new_resource_accessor("KineticInputAccessor")
		a:SetSidePos(Vec3i.right, Vec3i.new( 0, -2, 0 ))
		a:bind_input(res)
		local a = self:new_resource_accessor("ElectricOutputAccessor")
		a:SetSidePos(Vec3i.left, Vec3i.new( 0, 1, 0 ))		
		a:bind_output(res)
		end
		""",
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		"PowerOutput": 243*20,
		 
	},{
		"Name": "CompactGenerator",
		"Label": "Compact Generator",
		"StartTier": 1,
		"EndTier": 7,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
		return function(self)
		local res = self:get_resource_component()
        res.input = 20
        res.output = 20
        res.input_item = StaticItem.find("Kinetic")
        res.output_item = StaticItem.find("Electricity")
		local a = self:get_resource_component("Input")
		a:SetSidePos(Vec3i.front, Vec3i.zero)
		a:bind_input(res)
		local a = self:get_resource_component("Output")
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:bind_output(res)
		end
		""",
		"Description": ["KineticInput", "ElectricOutput", "PowerOutput"],
		"PowerOutput": 18,
	},{
		"Name": "ElectricEngine",
		"Label": "Electric Engine",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SelectCrafterInstanced",
        "Selector": "Blocks/ElectricEngineBP.ElectricEngineBP_C",
		"BlockCreation":"""
        return function(self)
        local crafter = AbstractCrafter.cast(self)
        
        local inv = crafter.resource_input_inventory
        inv.item = StaticItem.find("Electricity")
        inv.input = 20
        inv.capacity = 20
        
        local acc = ResourceAccessor.new(crafter, "Input1")
        crafter:reg(acc)
        acc.side = Vec3i.back
        acc.pos = Vec3i.zero
        acc.inventory = inv
        
        local acc = ResourceAccessor.new(crafter, "Input2")
        crafter:reg(acc)
        acc.side = Vec3i.down
        acc.pos = Vec3i.zero
        acc.inventory = inv
        
        local inv = crafter.resource_output_inventory
        inv.item = StaticItem.find("Kinetic")
        inv.output = 20
        inv.capacity = 20
        
    	local acc = ResourceAccessor.new(crafter, "Output")
        crafter:reg(acc)
        acc.side = Vec3i.front
        acc.pos = Vec3i.zero
        acc.inventory = inv
        end
		""",
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
        return function(self)
		
		local a = self:CreateAccessor(Class.find("KineticOutputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("KineticOutputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.zero)
		a:Bind(self:GetInputContainer())
        end
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
		return function(self)
		
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
		end
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
		"Name": "FilteringRobotArm",
		"Label": "Filtering Robot Arm",
		"StartTier": 1,
		"EndTier": 10,
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
		"Description": ["Sorter"],
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
		"Name": "FilteringPump",
		"Label": "Filtering Pump",
		"StartTier": 1,
		"EndTier": 10,
		"CustomData":{
			"ItemPortion": 1000
		},
		"Selector": "Blocks/ArrowBP.ArrowBP_C",
		"Description": ["Sorter", "FluidInput", "FluidOutput"],
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
		"BlockCreation":"""
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        local input = crafter.resource_input_inventory
        input.item = StaticItem.find("Heat")
        input.input = 20
        input.capacity = 20
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.down
        acc.pos = Vec3i.zero
        acc.inventory = input
		end
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
		return function(self)	
        local crafter = AbstractCrafter.cast(self)
        
        local inv = crafter.resource_output_inventory
        inv.item = StaticItem.find("Kinetic")
        inv.output = 40
        
    	acc = ResourceAccessor.new(crafter, "Output")
        crafter:reg(acc)
        acc.side = Vec3i.front
        acc.pos = Vec3i.zero
        acc.inventory = inv
        
        local inv = crafter.resource_input_inventory
        inv.item = StaticItem.find("Steam")
        inv.input = 40
        
    	acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.up
        acc.pos = Vec3i.new(0, 0, 1)
        acc.inventory = inv
        end
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
		return function(self)
		
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(0, 0, 0))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("KineticOutputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.new(-5, -1, 0))
		a:Bind(self:GetOutputContainer())
		end
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
		"BlockCreation":"""
		return function(self)
		
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.up, Vec3i.new( -2, 0, 1 ))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.new( -1, -1, 1 ))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("KineticOutputAccessor"))
		a:SetSidePos(Vec3i.right, Vec3i.new( -3, -1, 0 ))
		a:Bind(self:GetOutputContainer())
		end
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
		return function(self)
		
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.new( 0, 0, 0 ))
		a:Bind(self:GetOutputContainer())
		a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.up, Vec3i.new( 0, 0, 1 ))
		a:Bind(self:GetOutputContainer())
		end
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
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.back, Vec3i.new( -1, 1, 0 ))
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Electricity")
		end
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
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.new( 0, 0, 0 ))
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		end
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
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.zero)
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		end
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "IndustrialChemReactor",
		"Label": "Industrial Chemical Reactor",
		"Positions": [[0,0,0],[-1,0,0],[0,1,0],[-1,1,0],[0,0,1],[-1,0,1],[0,1,1],[-1,1,1]],
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.new( 0, 0, 0 ))
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Electricity")
		end
		""",
		"Description": ["ElectricInput"],
	},{
		"Name": "Furnace",
		"Label": "Furnace",
		"StartTier": 0,
		"EndTier": 10,
		"BlockLogic":"Furnace",
        "Selector": "019/FurnaceSelector.FurnaceSelector_C",
		"BlockCreation":"""
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        
        local output = crafter.resource_output_inventory
        output.item = StaticItem.find("Heat")
        output.output = 20
        output.capacity = 200
        
        local acc = ResourceAccessor.new(crafter, "Output")
        crafter:reg(acc)
        acc.side, acc.pos = Vec3i.up, Vec3i.zero
        acc.inventory = output
        acc.channel = "Heat"
        acc.is_output = true
		end
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
		return function(self)
		
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.up, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		end
		""",
		"Description": ["FluidInput", "HeatOutput"],
	},{
		"Name": "ElectricFurnace",
		"Label": "Electric Furnace",
		"StartTier": 2,
		"EndTier": 10,
		"BlockLogic": "SelectCrafter",
		"BlockCreation":"""
		return function(self)
		
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.up, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		end
		""",
		"Description": ["ElectricInput", "HeatOutput", "PowerOutput"],
		"PowerOutput": 40,
	},{
		"Name": "BatteryBox",
		"Label": "Battery Box",
		"StartTier": 4,
		"EndTier": 10,
        "BlockLogic": "BatteryContainerBlockLogic",
		"Description": ["ElectricConductor", "ElectricStorage"]
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
		return function(self)
		
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
		end
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
		return function(self)
		local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.zero)
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Electricity")
		end
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
		return function(self)
		local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.zero)
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Electricity")
		end
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
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.zero)
        local res = self:get_resource_component()
		a:Bind(res)
        res.input = 20
        res.input_item = StaticItem.find("Electricity")
		end
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
		return function(self)
		local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.front, Vec3i.zero)
        local res = self:get_resource_component()
		a:bind_input(res)
        res.input = 20
        res.input_item = StaticItem.find("Electricity")
		end
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
		return function(self)
		
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		end
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
		return function(self)
		
		local a = self:CreateAccessor(Class.find("ElectricInputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		end
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
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.back, Vec3i.new(-1,0,0))
        local res = self:get_resource_component()
		a:Bind(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		end
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
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.back, Vec3i.new(-1,0,0))
        local res = self:get_resource_component()
		a:Bind(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		end
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
		return function(self)
		
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(0,0,0))
		a:Bind(self:GetInputContainer())
		end
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
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        
        local inv = crafter.resource_input_inventory
        inv.item = StaticItem.find("Kinetic")
        inv.input = 20
        inv.capacity = 20
        
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.right
        acc.pos = Vec3i.new(-1,-2,0)
        acc.inventory = inv
        
        inv = crafter.resource_output_inventory
        inv.item = StaticItem.find("Electricity")
        inv.output = 20
        
    	acc = ResourceAccessor.new(crafter, "Output")
        crafter:reg(acc)
        acc.side = Vec3i.front
        acc.pos = Vec3i.zero
        acc.inventory = inv
        
		
		local a = self:CreateAccessor(Class.find("FluidOutputAccessor"))
		a:SetSidePos(Vec3i.front, Vec3i.new(0,0,0))
		a:Bind(self:GetOutputContainer())
		local a = self:CreateAccessor(Class.find("KineticInputAccessor"))
		a:SetSidePos(Vec3i.right, Vec3i.new(-1,-2,0))
		a:Bind(self:GetInputContainer())
		end
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
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.back, Vec3i.new(-1,1,0))
        local res = self:get_resource_component()
		a:Bind(res)
        res.input = 20
        res.input_item = StaticItem.find("Kinetic")
		end
		""",
		"Description": ["KineticInput"],
	},{
		"Name": "Radiator",
		"Label": "Radiator",
		"StartTier": 3,
		"EndTier": 10,
		"BlockLogic":"SelectCrafter",
		"BlockCreation":"""
		return function(self)
        local a = self:new_resource_accessor("Input")
		a:SetSidePos(Vec3i.down, Vec3i.zero)
        local res = self:get_resource_component()
		a:Bind(res)
        res.input = 20
        res.input_item = StaticItem.find("Heat")
		end
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
	#	"RequiredResearches":["LiquidsScan"+static_research],
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
		return function(self)
		
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
		end
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
		return function(self)
		
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
		end
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
		return function(self)
		
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
		end
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
	#	"RequiredResearches":["HeatTransferring"+static_research],
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
	#	"RequiredResearches":["HeatTransferring"+static_research],
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
		return function(self)
		
		local a = self:CreateAccessor(Class.find("FluidInputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.new(-1,0,2))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.new(0,0,2))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.new(-2,0,2))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.new(-1,1,2))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatInputAccessor"))
		a:SetSidePos(Vec3i.down, Vec3i.new(-1,-1,2))
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("FluidOutputAccessor"))
		a:SetSidePos(Vec3i.back, Vec3i.new(-2,0,0))
		a:Bind(self:GetOutputContainer())
		end
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
		return function(self)
        local crafter = AbstractCrafter.cast(self)
        local inv = crafter.resource_input_inventory
        inv.item = StaticItem.find("Heat")
        inv.input = 20
        local acc = ResourceAccessor.new(crafter, "Input")
        crafter:reg(acc)
        acc.side = Vec3i.front
        acc.pos = Vec3i.zero
        acc.inventory = inv
		end
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
		return function(self)
		
		local a = self:CreateAccessor(Class.find("KineticInputAccessor"))
		a:SetSidePos(Vec3i.left, Vec3i.zero)
		a:Bind(self:GetInputContainer())
		local a = self:CreateAccessor(Class.find("HeatOutputAccessor"))
		a:SetSidePos(Vec3i.right, Vec3i.zero)
		a:Bind(self:GetOutputContainer())
		end
		""",
    },{
		"Name": "CableBundle",
		"Label": "Cable Bundle",
		"StartTier": 1,
		"EndTier": 1,		
        "BlockLogic":"CableBundleBlockLogic",
		"Description": ["ElectricConductor"],
        "CustomData":{
			"SplineMesh": "CoreContent/Rail2",
		}
	},{
		"Name": "Rails",
		"Label": "Rails",
		"StartTier": 2,
		"EndTier": 2,		
        "BlockLogic":"CableBundleBlockLogic",
		"Description": ["ElectricConductor"],
        "CustomData":{
			"SplineMesh": "CoreContent/Rail2",
		}
	}
]