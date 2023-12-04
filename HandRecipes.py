from Common import *
from MachinesList import *
from MiscGen import *
import copy

objects_array = []

recipes_hand = []

recipes_press = []

def append_recipe_hand_press(recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]
	
	dec_recipe = copy.deepcopy(recipe)

	recipes_hand.append(recipe)
	
	output = copy.deepcopy(dec_recipe["Input"])
	
	dec_recipe["Ticks"] = 60
	dec_recipe["ResourceInput"] = { "Name": "Kinetic" + static_item, "Count": 100 }
	recipes_press.append(dec_recipe)	

recipes_hand.append({
	"Name": "ClayBlock",
	"Input":{
		"Items":[
			{
				"Name": "Clay" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ClayBlock" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"Bricks",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Bricks" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"RedBricks",
	"Input":{
		"Items":[
			{
				"Name": "RedStoneSurface" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "RedBricks" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"DarkBricks",
	"Input":{
		"Items":[
			{
				"Name": "DarkStoneSurface" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DarkBricks" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "SandSurface",
	"Input":{
		"Items":[
			{
				"Name": "GravelSurface" + static_item,
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "SandSurface" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "GravelSurface",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface" + static_item,
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "GravelSurface" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks": 20,
})

recipes_hand.append({
	"Name":"StoneTiles",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "StoneTiles" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"DarkTiles",
	"Input":{
		"Items":[
			{
				"Name": "DarkStoneSurface" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DarkTiles" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"RedTiles",
	"Input":{
		"Items":[
			{
				"Name": "RedStoneSurface" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "RedTiles" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"TerracottaTiles",
	"Input":{
		"Items":[
			{
				"Name": "Terracotta" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "TerracottaTiles" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"TerracottaBricks",
	"Input":{
		"Items":[
			{
				"Name": "TerracottaTiles" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "TerracottaBricks" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"CircuitBoard",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "CircuitBoard" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"GoldWire",
	"Input":{
		"Items":[
			{
				"Name": "GoldIngot" + static_item,
				"Count": 1
			},	
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "GoldWire" + static_item,
				"Count": 2
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"CopperWire",
	"Input":{
		"Items":[
			{
				"Name": "CopperIngot" + static_item,
				"Count": 1
			},	
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperWire" + static_item,
				"Count": 2
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"Circuit",
	"Input":{
		"Items":[
			{
				"Name": "CopperWire" + static_item,
				"Count": 6
			},	
			{
				"Name": "CircuitBoard" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Circuit" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"AdvancedCircuit",
	"Input":{
		"Items":[
			{
				"Name": "Silicon" + static_item,
				"Count": 1
			},	
			{
				"Name": "Circuit" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedCircuit" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"Processor",
	"Input":{
		"Items":[
			{
				"Name": "SiliconWafer" + static_item,
				"Count": 1
			},	
			{
				"Name": "AdvancedCircuit" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Processor" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"QuantumCircuit",
	"Input":{
		"Items":[
			{
				"Name": "QuantumCore" + static_item,
				"Count": 2
			},	
			{
				"Name": "Processor" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumCircuit" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"QuantumProcessor",
	"Input":{
		"Items":[
			{
				"Name": "QuantumCircuit" + static_item,
				"Count": 2
			},	
			{
				"Name": "Processor" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumProcessor" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "WoodenChest",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 6
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "WoodenChest" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

append_recipe_hand_press({
	"Name": "WoodenPlanks",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "WoodenPlanks" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Steampack",
	"Input":{
		"Items":[
			{
				"Name": "CopperParts" + static_item,
				"Count": 6
			},
			{
				"Name": "CopperPlate" + static_item,
				"Count": 2
			},
			{
				"Name": "CopperPipe" + static_item,
				"Count": 4
			},
			{
				"Name": "Circuit" + static_item,
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Steampack" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Jetpack",
	"Input":{
		"Items":[
			{
				"Name": "AluminiumParts" + static_item,
				"Count": 10
			},
			{
				"Name": "AluminiumPlate" + static_item,
				"Count": 3
			},
			{
				"Name": "AluminiumPipe" + static_item,
				"Count": 6
			},
			{
				"Name": "AdvancedCircuit" + static_item,
				"Count": 10
			},
			{
				"Name": "AluminiumElectricEngine" + static_item,
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Jetpack" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Torch",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 1
			},
			{
				"Name": "Organics" + static_item,
				"Count": 10
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Torch" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "AdvancedJetpack",
	"Input":{
		"Items":[
			{
				"Name": "StainlessSteelParts" + static_item,
				"Count": 10
			},
			{
				"Name": "StainlessSteelPlate" + static_item,
				"Count": 3
			},
			{
				"Name": "StainlessSteelPipe" + static_item,
				"Count": 6
			},
			{
				"Name": "Processor" + static_item,
				"Count": 10
			},
			{
				"Name": "StainlessSteelEngine" + static_item,
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedJetpack" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Scanner",
	"Input":{
		"Items":[
			{
				"Name": "SteelPlate" + static_item,
				"Count": 1
			},
			{
				"Name": "AdvancedCircuit" + static_item,
				"Count": 2
			},
			{
				"Name": "CopperConnector" + static_item,
				"Count": 5
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Scanner" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "AntigravityUnit",
	"Input":{
		"Items":[
			{
				"Name": "HardMetalParts" + static_item,
				"Count": 20
			},
			{
				"Name": "HardMetalPlate" + static_item,
				"Count": 2
			},
			{
				"Name": "HardMetalPipe" + static_item,
				"Count": 6
			},
			{
				"Name": "QuantumProcessor" + static_item,
				"Count": 10
			},
			{
				"Name": "Catalyst" + static_item,
				"Count": 4
			},
			{
				"Name": "HardMetalElectricEngine" + static_item,
				"Count": 8
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AntigravityUnit" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Plank",
	"Input":{
		"Items":[
			{
				"Name": "Log" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 2
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Chair",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 4
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Chair" + static_item,
				"Count": 1
			}
		]
	}, 
	"Ticks" : 20 
})

recipes_hand.append({
	"Name": "CopperChair",
	"Input":{
		"Items":[
			{
				"Name": "Chair" + static_item,
				"Count": 1
			},
			{
				"Name": "CopperPlate" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperChair" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Ladder",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 4
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Ladder" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Door",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 8
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Door" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Window",
	"Input":{
		"Items":[
			{
				"Name": "Glass" + static_item,
				"Count": 2
			},
			{
				"Name": "Plank" + static_item,
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Window" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "PlasticWindow",
	"Input":{
		"Items":[
			{
				"Name": "Glass" + static_item,
				"Count": 2
			},
			{
				"Name": "Plastic" + static_item,
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "PlasticWindow" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Table",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 6
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Table" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Bed",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 8
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Bed" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Rack",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 4
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Rack" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "WoodenStairs",
	"Input":{
		"Items":[
			{
				"Name": "WoodenPlanks" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "WoodenStairs" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Stairs",
	"Input":{
		"Items":[
			{
				"Name": "Bricks" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Stairs" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Fence",
	"Input":{
		"Items":[
			{
				"Name": "Plank" + static_item,
				"Count": 3
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Fence" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "SteelFence",
	"Input":{
		"Items":[
			{
				"Name": "SteelParts" + static_item,
				"Count": 3
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "SteelFence" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "StainlessSteelFence",
	"Input":{
		"Items":[
			{
				"Name": "StainlessSteelParts" + static_item,
				"Count": 3
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "StainlessSteelFence" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Flashlight",
	"Input":{
		"Items":[
			{
				"Name": "SteelPipe" + static_item,
				"Count": 1
			},
			{
				"Name": "SteelLamp" + static_item,
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Flashlight" + static_item,
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "ConcreteTiles",
	"Input":{
		"Items":[
			{
				"Name": "Concrete" + static_item,
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteTiles" + static_item,
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})
recipes_hand.append({
	"Name": "ConcreteSmallTiles",
	"Input":{
		"Items":[
			{
				"Name": "Concrete" + static_item,
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteSmallTiles" + static_item,
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})
recipes_hand.append({
	"Name": "ConcreteBricks",
	"Input":{
		"Items":[
			{
				"Name": "Concrete" + static_item,
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteBricks" + static_item,
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})
recipes_hand.append({
	"Name": "ReinforcedConcreteTiles",
	"Input":{
		"Items":[
			{
				"Name": "ReinforcedConcrete" + static_item,
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteTiles" + static_item,
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})
recipes_hand.append({
	"Name": "ReinforcedConcreteSmallTiles",
	"Input":{
		"Items":[
			{
				"Name": "ReinforcedConcrete" + static_item,
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteSmallTiles" + static_item,
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})
recipes_hand.append({
	"Name": "ReinforcedConcreteBricks",
	"Input":{
		"Items":[
			{
				"Name": "ReinforcedConcrete" + static_item,
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteBricks" + static_item,
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})

for r in recipes_hand:
	r["Locked"] = True

objects_array.append({ "Class": base_recipe,
	"Name": "Hand" + base_recipe,
	"Recipes": recipes_hand
})

objects_array.append({ "Class": base_recipe,
	"Name": "Press" + base_recipe,
	"Recipes": recipes_press
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/misc_hand.json", data);