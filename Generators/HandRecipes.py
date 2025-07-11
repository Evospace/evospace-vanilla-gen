from Common import *
from MachinesList import *
from MiscGen import *
import copy

objects_array = []

recipes_hand = []

recipes_press = []

def append_recipe_hand(recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]
	
	dec_recipe = copy.deepcopy(recipe)

	recipes_hand.append(recipe)
	
	output = copy.deepcopy(dec_recipe["Input"])
	
	dec_recipe["Ticks"] = 60
	dec_recipe["ResourceInput"] = { "Name": "Kinetic", "Count": 100 }
	recipes_press.append(dec_recipe)	

recipes_hand.append({
	"Name": "SandSurface",
	"Input":{
		"Items":[
			{
				"Name": "GravelSurface",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "SandSurface",
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
				"Name": "StoneSurface",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "GravelSurface",
				"Count": 1
			}
		]
	},
	"Ticks": 20,
})

recipes_hand.append({
	"Name": "Steampack",
	"Input":{
		"Items":[
			{
				"Name": "CopperParts",
				"Count": 6
			},
			{
				"Name": "CopperPlate",
				"Count": 2
			},
			{
				"Name": "CopperPipe",
				"Count": 4
			},
			{
				"Name": "Circuit",
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Steampack",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "AdvancedSteampack",
	"Input":{
		"Items":[
			{
				"Name": "StainlessSteelParts",
				"Count": 30
			},
			{
				"Name": "StainlessSteelPlate",
				"Count": 10
			},
			{
				"Name": "CopperPipe",
				"Count": 30
			},
			{
				"Name": "Processor",
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedSteampack",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "HighCapacitySteampack",
	"Input":{
		"Items":[
			{
				"Name": "SteelParts",
				"Count": 30
			},
			{
				"Name": "SteelPlate",
				"Count": 10
			},
			{
				"Name": "CopperPipe",
				"Count": 5
			},
			{
				"Name": "Circuit",
				"Count": 15
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "HighCapacitySteampack",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "HighPressureSteampack",
	"Input":{
		"Items":[
			{
				"Name": "SteelParts",
				"Count": 6
			},
			{
				"Name": "SteelPlate",
				"Count": 2
			},
			{
				"Name": "CopperPipe",
				"Count": 30
			},
			{
				"Name": "Circuit",
				"Count": 15
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "HighPressureSteampack",
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
				"Name": "AluminiumParts",
				"Count": 10
			},
			{
				"Name": "AluminiumPlate",
				"Count": 3
			},
			{
				"Name": "AluminiumPipe",
				"Count": 6
			},
			{
				"Name": "AdvancedCircuit",
				"Count": 10
			},
			{
				"Name": "AluminiumElectricEngine",
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Jetpack",
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
				"Name": "StainlessSteelParts",
				"Count": 10
			},
			{
				"Name": "StainlessSteelPlate",
				"Count": 3
			},
			{
				"Name": "StainlessSteelPipe",
				"Count": 6
			},
			{
				"Name": "Processor",
				"Count": 10
			},
			{
				"Name": "StainlessSteelElectricEngine",
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedJetpack",
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
				"Name": "CompositeParts",
				"Count": 20
			},
			{
				"Name": "CompositePlate",
				"Count": 2
			},
			{
				"Name": "CompositePipe",
				"Count": 6
			},
			{
				"Name": "QuantumProcessor",
				"Count": 10
			},
			{
				"Name": "Catalyst",
				"Count": 4
			},
			{
				"Name": "CompositeElectricEngine",
				"Count": 8
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AntigravityUnit",
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
				"Name": "SteelPipe",
				"Count": 1
			},
			{
				"Name": "SteelLamp",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Flashlight",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

for r in recipes_hand:
	r["Locked"] = True

objects_array.append({ "Class": r_dict,
	"Name": "Hand" + r_dict,
	"Recipes": recipes_hand
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/misc_hand.json", data);