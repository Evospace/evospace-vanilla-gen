from Common import *
from MachinesList import *

objects_array = []

cvs = []

wooden_misc = [
    {"name": "Chair"},
    {"name": "Table", "Positions": [[0, 0, 0], [-1, 0, 0]]},
    {"name": "Rack"},
    {
        "name": "Bed",
        "Positions": [[0, 0, 0], [-1, 0, 0]],
        "BlockLogic": "BedBlockLogic",
    },
    {"name": "Ladder"},
    {
        "name": "Door",
        "Positions": [[0, 0, 0], [0, 0, 1]],
        "BlockLogic": "Door",
    },
    {"name": "Window", "Positions": [[0, 0, 0], [0, 0, 1]]},
]

simple_single = [
    {
        "name": "CeramicRoof",
    },
    {
        "name": "Stairs",
    },
    {
        "name": "WoodenStairs",
    },
    {
        "name": "CopperChair",
    },
    {
        "name": "FireCup",
    },
    {"name": "PlasticWindow", "Positions": [[0, 0, 0], [0, 0, 1]]},
    {"name": "SteelFence", "BlockLogic": "FenceBlockLogic", "Tier": 1},
    {"name": "StainlessSteelFence", "BlockLogic": "FenceBlockLogic", "Tier": 2},
    {
        "name": "Fence",
        "BlockLogic": "FenceBlockLogic",
    },
]

# ,{
# 		"name": "Campfire",
# 		"Tier": 0
# 	}
# 	{
# 		"name": "CeramicPlate",
# 		"Tier": 0
# 	},{
# 		"name": "Candle",
# 		"Tier": 0
# 	},{
# 		"name": "CeramicCup",
# 		"Tier": 0
# 	},{
# 		"name": "CeramicPot",
# 		"Tier": 0
# 	}

simple_deco = [
    {"name": "Firefly"},
    {"name": "Flies"},
    {"name": "Birds"},
    {"name": "DesertSound"},
    {"name": "SwampSound"},
    {"name": "Butterfly"},
    {"name": "Leafes"},
    {"name": "Bugs"},
]

simple_blocks = [
    {"name": "WoodenPlanks", "Label": "Wooden Planks", "Tier": 0},
    {"name": "AdminBlocks", "Label": "Admin Blocks", "Tier": 0},
    {"name": "StoneTiles", "Label": "Stone Tiles", "Tier": 0},
    {"name": "RedTiles", "Label": "Red Tiles", "Tier": 0},
    {"name": "DarkTiles", "Label": "Dark Tiles", "Tier": 0},
    {"name": "Terracotta", "Label": "Terracotta", "Tier": 0},
    {"name": "TerracottaTiles", "Label": "Terracotta Tiles", "Tier": 0},
    {"name": "Bricks", "Label": "Bricks", "Tier": 0},
    {"name": "RedBricks", "Label": "Red Bricks", "Tier": 0},
    {"name": "DarkBricks", "Label": "Black Bricks", "Tier": 0},
    {"name": "TerracottaBricks", "Label": "Terracotta Bricks", "Tier": 0},
    {"name": "Concrete", "Label": "Concrete", "Tier": 2},
    {"name": "ConcreteBricks", "Label": "Concrete Bricks", "Tier": 2},
    {"name": "ConcreteTiles", "Label": "Concrete Tiles", "Tier": 2},
    {"name": "ConcreteSmallTiles", "Label": "Concrete Small Tiles", "Tier": 2},
    {"name": "ReinforcedConcrete", "Label": "Reinforced Concrete", "Tier": 2},
    {
        "name": "ReinforcedConcreteTiles",
        "Label": "Reinforced Concrete Tiles",
        "Tier": 2,
    },
    {
        "name": "ReinforcedConcreteSmallTiles",
        "Label": "Reinforced Concrete Small Tiles",
        "Tier": 2,
    },
    {
        "name": "ReinforcedConcreteBricks",
        "Label": "Reinforced Concrete Bricks",
        "Tier": 2,
    },
    {"name": "DangerBlock", "Label": "Danger Block", "Tier": 2},
    {"name": "RustyCopperCasing", "Label": "Rusty Copper Casing", "Tier": 1},
    {"name": "RustyIronCasing", "Label": "Rusty Iron Casing", "Tier": 2},
    {"name": "BasicPlatform", "Label": "Basic Platform", "Tier": 0},
    {"name": "PlasticBlock", "Label": "Plastic Block", "Tier": 0},
    {"name": "GlassBlock", "Label": "Glass Block", "Tier": 0},
    {"name": "PaintWhite", "Label": "Paint White", "Tier": 0},
    {"name": "PaintGray", "Label": "Paint Gray", "Tier": 0},
    {"name": "PaintBlack", "Label": "Paint Black", "Tier": 0},
    {"name": "PaintGreen", "Label": "Paint Green", "Tier": 0},
    {"name": "PaintRed", "Label": "Paint Red", "Tier": 0},
    {"name": "PaintBlue", "Label": "Paint Blue", "Tier": 0},
    {"name": "PaintCopper", "Label": "Paint Copper", "Tier": 0},
    {"name": "PaintSteel", "Label": "Paint Steel", "Tier": 0},
    {"name": "PaintStainlessSteel", "Label": "Paint StainlessSteel", "Tier": 0},
    {"name": "PaintTitanium", "Label": "Paint Titanium", "Tier": 0},
    {"name": "PaintHardMetal", "Label": "Paint Hard Metal", "Tier": 0},
    {"name": "PaintGold", "Label": "Paint Gold", "Tier": 0},
    {"name": "PaintYellow", "Label": "Paint Yellow", "Tier": 0},
    {"name": "PaintMagenta", "Label": "Paint Magenta", "Tier": 0},
    {"name": "PaintCyan", "Label": "Paint Cyan", "Tier": 0},
]

static_mesh_block = [{"name": "Column"}, {"name": "FluetedColumn"}]

equipped = [
    {"name": "Torch", "item_logic": "Equipped/TorchBP.TorchBP_C"},
    {"name": "Flashlight", "item_logic": "Equipped/FlashlightBP.FlashlightBP_C"},
    {"name": "NightVision", "item_logic": "Equipped/NightVisionBP.NightVisionBP_C"},
    {
        "name": "AdvancedNightVision",
        "item_logic": "Equipped/AdvancedNightVisionBP.AdvancedNightVisionBP_C",
    },
    {"name": "Steampack", "item_logic": "Equipped/SteampackBP.SteampackBP_C"},
    {"name": "Jetpack", "item_logic": "Equipped/JetpackBP.JetpackBP_C"},
    {
        "name": "AdvancedJetpack",
        "item_logic": "Equipped/AdvancedJetpackBP.AdvancedJetpackBP_C",
    },
    {
        "name": "AntigravityUnit",
        "item_logic": "Equipped/AntigravityUnitBP.AntigravityUnitBP_C",
    },
    {"name": "Scanner", "item_logic": "Equipped/ScannerBP.ScannerBP_C"},
]

for one in wooden_misc:
    cvs.append([one["name"], "Wooden " + CamelToSpaces(one["name"])])

    item = {
        "class": static_item,
        "name": one["name"],
        "image": "T_" + one["name"],
        "logic_json": {"Block": one["name"]},
        "max_count": 32,
        "tag": "Decoration",
        "label_parts": [[one["name"], "misc"]],
        "item_logic": building_single_logic,
    }

    objects_array.append(item)

    block = {
        "name": one["name"],
        "Item": one["name"],
        "Actor": "/Game/Blocks/" + one["name"] + "BP." + one["name"] + "BP_C",
        "BlockLogic": "BlockLogic" if "BlockLogic" not in one else one["BlockLogic"],
        "class": static_block,
    }

    if "Positions" in one:
        block["Positions"] = one["Positions"]

    objects_array.append(block)

for one in simple_single:
    cvs.append([one["name"], CamelToSpaces(one["name"])])

    objects_array.append(
        {
            "class": static_item,
            "name": one["name"],
            "image": "T_" + one["name"],
            "item_logic": building_single_logic,
            "logic_json": {"Block": one["name"]},
            "max_count": 32,
            "tag": "Decoration",
            "label_parts": [[one["name"], "misc"]],
            "Tier": one["Tier"] if "Tier" in one else 0,
        }
    )

    block = {
        "class": static_block,
        "name": one["name"],
        "Item": one["name"],
        "Actor": "/Game/Blocks/" + one["name"] + "BP." + one["name"] + "BP_C",
        "BlockLogic": "BlockLogic" if "BlockLogic" not in one else one["BlockLogic"],
    }

    if "Positions" in one:
        block["Positions"] = one["Positions"]

    objects_array.append(block)

for one in simple_deco:
    cvs.append([one["name"], CamelToSpaces(one["name"])])

    deco = {
        "class": static_item,
        "name": one["name"],
        "image": "T_" + one["name"],
        "item_logic": building_decoration_logic,
        "logic_json": {"Block": one["name"]},
        "max_count": 32,
        "label_parts": [[one["name"], "misc"]],
        "tag": "Decoration",
    }
    if "item_logic" in one:
        deco["item_logic"] = one["item_logic"]

    objects_array.append(deco)
    objects_array.append(
        {
            "class": static_decoration,
            "name": one["name"],
            "Item": one["name"],
            "Actor": "Decorations/" + one["name"] + "BP." + one["name"] + "BP_C",
            "BlockLogic": "BlockLogic",
        }
    )

for one in simple_blocks:
    cvs.append([one["name"], CamelToSpaces(one["name"])])

    objects_array.append(
        {
            "class": static_item,
            "name": one["name"],
            "image": "T_" + one["name"],
            "item_logic": building_plane_logic,
            "logic_json": {"Block": one["name"], "BuildingMode": "Plane"},
            "max_count": 999,
            "tag": "Decoration",
            "label_parts": [[one["name"], "misc"]],
            "category": "Block",
            "description_parts": [["BuildingBlock", "common"]],
        }
    )
    objects_array.append(
        {
            "class": tesselator_cube,
            "name": one["name"],
            "Material": "Materials/" + one["name"],
        }
    )
    objects_array.append(
        {
            "class": static_block,
            "name": one["name"],
            "Item": one["name"],
            "Tesselator": one["name"],
        }
    )

for one in static_mesh_block:
    cvs.append([one["name"], CamelToSpaces(one["name"])])

    objects_array.append(
        {
            "class": static_item,
            "name": one["name"],
            "image": "T_" + one["name"],
            "item_logic": building_single_logic,
            "logic_json": {"Block": one["name"]},
            "max_count": 32,
            "tag": "Decoration",
            "label_parts": [[one["name"], "misc"]],
        }
    )
    # objects_array.append({ "class": tesselator_static_mesh,
    # 	"name": one["name"]_static_mesh,
    # 	"Mesh": "Models/" + one["name"],
    # })
    objects_array.append(
        {
            "class": static_block,
            "name": one["name"],
            "Item": one["name"],
            "Actor": "/Game/Blocks/" + one["name"] + "BP." + one["name"] + "BP_C",
            "BlockLogic": "BlockLogic",
            # "Tesselator": one["name"]_static_mesh
        }
    )

images = []

images.append(
    {
        "Base": "T_" + "JetpackBase",
        "NewName": "T_" + "Jetpack",
        "MulMask": "T_" + "Aluminium",
    }
)

images.append(
    {
        "Base": "T_" + "JetpackBase",
        "NewName": "T_" + "Steampack",
        "MulMask": "T_" + "Copper",
    }
)

for one in equipped:
    cvs.append([one["name"], CamelToSpaces(one["name"])])

    equ = {
        "class": static_item,
        "name": one["name"],
        "image": "T_" + one["name"],
        "logic_json": {"Block": one["name"]},
        "max_count": 32,
        "tag": "Misc",
        "label_parts": [[one["name"], "misc"]],
    }
    if "item_logic" in one:
        equ["item_logic"] = one["item_logic"]

    objects_array.append(equ)


data = {"Objects": objects_array}

write_file("Generated/Mixed/misc.json", data)

write_file("Loc/source/misc.json", cvs)

objects_array = []

objects_array.append(
    {"class": ico_generator, "name": "Misc" + ico_generator, "Images": images}
)

data = {"Objects": objects_array}

write_file("Generated/Resources/misc.json", data)
