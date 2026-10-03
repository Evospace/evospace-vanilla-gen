from Common import *
from MachinesList import *

objects_array = []
images = []

wooden_misc = [
	{
		"Name": "Rack",
		"Cost": 3,
	},{
		"Name": "Ladder",
		"Cost": 3,
	},{
		"Name": "Door",
		"Cost": 3,
		"Positions": [[0,0,0], [0,0,1]],
		"BlockLogic": "DoorBlockLogic",
	},{
		"Name": "Window",
		"Cost": 3,
		"Positions": [[0,0,0], [0,0,1]]
	}
]

simple_single = [
	{
		"Name": "CeramicRoof",
		"Cost": 3,
	},{
		"Name": "ConcreteRamp",
		"Cost": 3,
	},{
		"Name": "ConcreteRamp2",
		"Cost": 3,
		"Label": ["TwoWorldsFormat", "common", ["ConcreteRamp", "misc"], ["II", "common"]],
	},{
		"Name": "ConcreteRamp3",
		"Cost": 3,
		"Label": ["TwoWorldsFormat", "common", ["ConcreteRamp", "misc"], ["III", "common"]],
	},{
		"Name": "ConcreteBeam",
		"Cost": 3,
	},{
		"Name": "ConcreteBeam2",
		"Cost": 3,
		"Label": ["TwoWorldsFormat", "common", ["ConcreteBeam", "misc"], ["II", "common"]],
	},{
		"Name": "CopperChair",
		"Cost": 3,
	},{
		"Name": "FireCup",
		"Cost": 3,
	},{
		"Name": "PlasticWindow",
		"Cost": 3,
		"Positions": [[0,0,0], [0,0,1]]
	},{
		"Name": "RoadCone",
		"Cost": 3,
	},{
		"Name": "WarningBarrier",
		"Cost": 3,
	},{
        "Name": "Spotlight",
        "BlockLogic": "SpotlightBlockLogic",
        "LogicImports": [
            "SpotlightAimX",
            "SpotlightAimY",
            "SpotlightColorR",
            "SpotlightColorG",
            "SpotlightColorB",
        ],
	},{
        "Name": "Led",
        "Tier": 2,
        "BlockLogic": "LedBlockLogic",
        "LogicImports": [
            "LedActive",
            "LedColorR",
            "LedColorG",
            "LedColorB",
        ],
        "Category": "Network",
	},{
        "Name": "LandingPad",
        "BlockLogic": "LandingPadBlockLogic",
        "Positions": [[x, y, 0] for x in range(-2, 3) for y in range(-2, 3)],
	}
]

simple_blocks = [
	{
		"Name": "WoodenPlanks",
		"Cost": 2,
		"Label": "Wooden Planks",
		"Tier": 0
	},{
		"Name": "AdminBlocks",
		"Label": "Admin Blocks",
		"Tier": 0
	},{
		"Name": "StoneTiles",
		"Cost": 2,
		"Label": "Stone Tiles",
		"Tier": 0
	},{
		"Name": "RedTiles",
		"Cost": 2,
		"Label": "Red Tiles",
		"Tier": 0
	},{
		"Name": "DarkTiles",
		"Cost": 2,
		"Label": "Dark Tiles",
		"Tier": 0
	},{
		"Name": "Terracotta",
		"Cost": 2,
		"Label": "Terracotta",
		"Tier": 0
	},{
		"Name": "TerracottaTiles",
		"Cost": 2,
		"Label": "Terracotta Tiles",
		"Tier": 0
	},{
		"Name": "Bricks",
		"Cost": 2,
		"Label": "Bricks",
		"Tier": 0
	},{
		"Name": "RedBricks",
		"Cost": 2,
		"Label": "Red Bricks",
		"Tier": 0
	},{
		"Name": "DarkBricks",
		"Cost": 2,
		"Label": "Black Bricks",
		"Tier": 0
	},{
		"Name": "TerracottaBricks",
		"Cost": 2,
		"Label": "Terracotta Bricks",
		"Tier": 0
	},{
		"Name": "Concrete",
		"Cost": 4,
		"Label": "Concrete",
		"Tier": 2
	},{
		"Name": "ConcreteBricks",
		"Cost": 4,
		"Label": "Concrete Bricks",
		"Tier": 2
	},{
		"Name": "ConcreteTiles",
		"Cost": 4,
		"Label": "Concrete Tiles",
		"Tier": 2
	},{
		"Name": "ConcreteSmallTiles",
		"Cost": 4,
		"Label": "Concrete Small Tiles",
		"Tier": 2
	},{
		"Name": "ReinforcedConcrete",
		"Cost": 8,
		"Label": "Reinforced Concrete",
		"Tier": 2
	},{
		"Name": "ReinforcedConcreteTiles",
		"Cost": 8,
		"Label": "Reinforced Concrete Tiles",
		"Tier": 2
	},{
		"Name": "ReinforcedConcreteSmallTiles",
		"Cost": 8,
		"Label": "Reinforced Concrete Small Tiles",
		"Tier": 2
	},{
		"Name": "ReinforcedConcreteBricks",
		"Cost": 8,
		"Label": "Reinforced Concrete Bricks",
		"Tier": 2
	},{
		"Name":"DangerBlock",
		"Cost": 8,
		"Label":"Danger Block",
		"Tier": 2
	},{
		"Name":"BasicPlatform",
		"Cost": 1,
		"Label":"Basic Platform",
		"Tier": 0
	},{
		"Name":"PlasticBlock",
		"Cost": 4,
		"Label":"Plastic Block",
		"Tier": 0
	},{
		"Name":"GlassBlock",
		"Cost": 2,
		"Label":"Glass Block",
		"Tier": 0,
		"Transparent": True
	},{
		"Name":"PaintWhite",
		"Cost": 2,
		"Label":"Paint White",
		"Tier": 0
	},{
		"Name":"PaintGray",
		"Cost": 2,
		"Label":"Paint Gray",
		"Tier": 0
	},{
		"Name":"PaintBlack",
		"Cost": 2,
		"Label":"Paint Black",
		"Tier": 0
	},{
		"Name":"PaintGreen",
		"Cost": 2,
		"Label":"Paint Green",
		"Tier": 0
	},{
		"Name":"PaintRed",
		"Cost": 2,
		"Label":"Paint Red",
		"Tier": 0
	},{
		"Name":"PaintBlue",
		"Cost": 2,
		"Label":"Paint Blue",
		"Tier": 0
	},{
		"Name":"PaintCopper",
		"Cost": 2,
		"Label":"Paint Copper",
		"Tier": 0
	},{
		"Name":"PaintSteel",
		"Cost": 2,
		"Label":"Paint Steel",
		"Tier": 0
	},{
		"Name":"PaintStainlessSteel",
		"Cost": 2,
		"Label":"Paint StainlessSteel",
		"Tier": 0
	},{
		"Name":"PaintTitanium",
		"Cost": 2,
		"Label":"Paint Titanium",
		"Tier": 0
	},{
		"Name":"PaintHardMetal",
		"Cost": 2,
		"Label":"Paint Hard Metal",
		"Tier": 0
	},{
		"Name":"PaintGold",
		"Cost": 2,
		"Label":"Paint Gold",
		"Tier": 0
	},{
		"Name":"PaintYellow",
		"Cost": 2,
		"Label":"Paint Yellow",
		"Tier": 0
	},{
		"Name":"PaintMagenta",
		"Cost": 2,
		"Label":"Paint Magenta",
		"Tier": 0
	},{
		"Name":"PaintCyan",
		"Cost": 2,
		"Label":"Paint Cyan",
		"Tier": 0
	}
]

static_mesh_block = [
]

equipped = [
	{
		"Name": "Flashlight",
		"ItemLogic": "/Script/Evospace.FlashlightItemLogic",
		"EquipmentSlot": "Light"
	},{
		"Name": "Steampack",
		"ItemLogic": "/Game/Equipped/SteampackBP.SteampackBP_C",
		"EquipmentSlot": "Jetpack"
	},{
		"Name": "HighPressureSteampack",
		"ItemLogic": "/Game/Equipped/HighPresSteampackBP.HighPresSteampackBP_C",
		"EquipmentSlot": "Jetpack"
	},{
		"Name": "HighCapacitySteampack",
		"ItemLogic": "/Game/Equipped/HighCapSteampackBP.HighCapSteampackBP_C",
		"EquipmentSlot": "Jetpack"
	},{
		"Name": "AdvancedSteampack",
		"ItemLogic": "/Game/Equipped/AdvancedSteampackBP.AdvancedSteampackBP_C",
		"EquipmentSlot": "Jetpack"
	},{
		"Name": "Jetpack",
		"ItemLogic": "/Game/Equipped/JetpackBP.JetpackBP_C",
		"EquipmentSlot": "Jetpack"
	},{
		"Name": "AdvancedJetpack",
		"ItemLogic": "/Game/Equipped/AdvancedJetpackBP.AdvancedJetpackBP_C",
		"EquipmentSlot": "Jetpack"
	},{
		"Name": "AntigravityUnit",
		"ItemLogic": "/Game/Equipped/AntigravityUnitBP.AntigravityUnitBP_C",
		"EquipmentSlot": "Jetpack"
	},{
		"Name": "NightVision",
		"ItemLogic": "/Game/Equipped/NightVisionBP.NightVisionBP_C",
		"EquipmentSlot": "Light"
	},{
		"Name": "AdvancedNightVision",
		"ItemLogic": "/Game/Equipped/AdvancedNightVisionBP.AdvancedNightVisionBP_C",
		"EquipmentSlot": "Light"
	}
]

for one in wooden_misc:
    item = { "Class": "StaticItem",
		"Name": one["Name"],
		"Image": "T_" + one["Name"],
		"Block": one["Name"],
		"StackSize": 32,
		"Label":[one["Name"],"misc"],
		"ItemLogic": building_single_logic,
		"Category": "Decoration",
	}

    objects_array.append(item)
	
    block = {
		"Name": one["Name"],
		"Item" : one["Name"],
		"Actor" : "Blocks/" + one["Name"] + "BP." + one["Name"] + "BP_C",
		"BlockLogic": "BlockLogic" if "BlockLogic" not in one else one["BlockLogic"],
		"Class": "StaticBlock",
		"Minable": decor_minable(one["Cost"]),
	}
	
    if "Positions" in one:
        block["Positions"] = one["Positions"]
		
    objects_array.append(block)

for one in simple_single:
    objects_array.append({ "Class": "StaticItem",
		"Name": one["Name"],
		"Image": "T_" + one["Name"],
		"ItemLogic": building_single_logic,
		"Block": one["Name"],
		"StackSize": 32,
		"Label": one.get("Label", [one["Name"], "misc"]),
		"Tier": one["Tier"] if "Tier" in one else 0,
		"Category": one["Category"] if "Category" in one else "Decoration",
	})

    block = {
		"Class": "StaticBlock",
		"Name": one["Name"],
		"Item" : one["Name"],
		"Actor" : "Blocks/" + one["Name"] + "BP." + one["Name"] + "BP_C",
		"BlockLogic": "BlockLogic" if "BlockLogic" not in one else one["BlockLogic"],
		"Minable": decor_minable(one["Cost"]) if "Cost" in one else {"Result": one["Name"]},
	}
	
    if "Positions" in one:
        block["Positions"] = one["Positions"]

    if "LogicExports" in one:
        block["ExportOptions"] = one["LogicExports"]
    if "LogicImports" in one:
        block["ImportOptions"] = one["LogicImports"]
		
    objects_array.append(block)
	
for one in simple_blocks:
    objects_array.append({ "Class": "StaticItem",
		"Name": one["Name"],
		"Image": "T_" + one["Name"],
		"ItemLogic": building_cube_logic,
		"Block": one["Name"] + static_block,
		"StackSize": 999,
		"Label":[one["Name"],"misc"],
		"Category": "Block",
		"DescriptionParts": [["BuildingBlock", "common"]],
	})
	
for one in simple_blocks:
    objects_array.append({ "Class": tesselator_cube,
		"Name": one["Name"] + tesselator,
		"Material" : "/Game/Materials/" + one["Name"],
		"Transparent": one["Transparent"] if "Transparent" in one else False
	})

for one in simple_blocks:
    objects_array.append({ "Class": "StaticBlock",
		"Name": one["Name"] + static_block,
		"Item" : one["Name"],
		"Tesselator": one["Name"] + tesselator,
		"BuildingMode": "Plane",
		"Minable": decor_minable(one["Cost"]) if "Cost" in one else {"Result": one["Name"]},
	})
	
for one in static_mesh_block:
    objects_array.append({ "Class": "StaticItem",
		"Name": one["Name"],
		"Image": "T_" + one["Name"],
		"ItemLogic": building_single_logic,
		"Block": one["Name"] + static_block,
		"StackSize": 32,
		"Label":[one["Name"],"misc"],
	})	
    objects_array.append({
		"Class": "StaticBlock",
		"Name": one["Name"] + static_block,
		"Item" : one["Name"],
		"Actor" : "Blocks/" + one["Name"] + "BP." + one["Name"] + "BP_C",
		"BlockLogic": "BlockLogic",
		"Minable": {"Result": one["Name"]},
	})
	
images.append({
		"Base": "T_" + "BasicPlatform",
		"NewName": "T_" + "LandingPad",
		"AddMask": "T_GreenCircle" + additive_ico,
	})
	
images.append({
		"Base": "T_" + "JetpackBase",
		"NewName": "T_" + "Jetpack",
		"MulMask": "T_Material" + "Aluminium",
	})
	
images.append({
		"Base": "T_" + "JetpackBase",
		"NewName": "T_" + "Steampack",
		"MulMask": "T_Material" + "Copper",
	})

images.append({
		"Base": "T_" + "JetpackBase",
		"NewName": "T_" + "HighPressureSteampack",
		"MulMask": "T_Material" + "Steel",
		"AddMask": "T_RedCircle" + additive_ico,
	})

images.append({
		"Base": "T_" + "JetpackBase",
		"NewName": "T_" + "HighCapacitySteampack",
		"MulMask": "T_Material" + "Steel",
		"AddMask": "T_BlueCircle" + additive_ico,
	})

images.append({
		"Base": "T_" + "JetpackBase",
		"NewName": "T_" + "AdvancedSteampack",
		"MulMask": "T_Material" + "StainlessSteel",
		"AddMask": "T_GreenCircle" + additive_ico,
	})
	
for one in equipped:
	equ = { "Class": "StaticItem",
		"Name": one["Name"],
		"Image": "T_" + one["Name"],
		"StackSize": 32,
		"Label":[one["Name"],"misc"],
		"EquipmentItem": True,
		"Category": "Equipment",
	}
	if "ItemLogic" in one:
		equ["ItemLogic"] = one["ItemLogic"]
	if "EquipmentSlot" in one:
		equ["EquipmentSlot"] = one["EquipmentSlot"]

	objects_array.append(equ)

objects_array.append({
	"Class": "StaticItem",
	"Name": "BuiltinFlashlight",
	"Image": "T_BuiltinFlashlight",
	"StackSize": 1,
	"Label": ["BuiltinFlashlight", "misc"],
	"Type": "Abstract",
	"ItemLogic": "/Script/Evospace.FlashlightItemLogic",
	"EquipmentItem": True,
	"EquipmentSlot": "Light",
	"Category": "Equipment",
})

objects_array.append({
	"Class": "StaticItem",
	"Name": "Ghost",
	"Image": "T_ConstructionBlueprint",
	"StackSize": 1,
	"Label": ["Ghost", "misc"],
	"Type": "Abstract",
	"Block": "Ghost",
	"Category": "Block",
})
objects_array.append({
	"Class": "GhostStaticBlock",
	"Name": "Ghost",
	"Item": "Ghost",
	"Minable": {
		"Count": 0,
	},
})

	
data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/misc.json", data)

objects_array = []

objects_array.append({	
		"Class": ico_generator,
		"Name": "Misc" + ico_generator,
		"Images": images
	})
	
data = {
	"Objects": objects_array
}

write_file("Generated/Resources/misc.json", data)