from Common import *
from MachinesList import *

objects_array = []

cvs = []

wooden_misc = [
    {"name": "Chair"},
    {"name": "Table", "sub_blocks": [[0, 0, 0], [-1, 0, 0]]},
    {"name": "Rack"},
    {
        "name": "Bed",
        "sub_blocks": [[0, 0, 0], [-1, 0, 0]],
        "BlockLogic": "BedBlockLogic",
    },
    {"name": "Ladder"},
    {
        "name": "Door",
        "sub_blocks": [[0, 0, 0], [0, 0, 1]],
        "BlockLogic": "Door",
    },
    {"name": "Window", "sub_blocks": [[0, 0, 0], [0, 0, 1]]},
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
    {"name": "PlasticWindow", "sub_blocks": [[0, 0, 0], [0, 0, 1]]},
    {"name": "SteelFence", "BlockLogic": "FenceBlockLogic", "tier": 1},
    {"name": "StainlessSteelFence", "BlockLogic": "FenceBlockLogic", "tier": 2},
    {
        "name": "Fence",
        "BlockLogic": "FenceBlockLogic",
    },
]

# ,{
# 		"name": "Campfire",
# 		"tier": 0
# 	}
# 	{
# 		"name": "CeramicPlate",
# 		"tier": 0
# 	},{
# 		"name": "Candle",
# 		"tier": 0
# 	},{
# 		"name": "CeramicCup",
# 		"tier": 0
# 	},{
# 		"name": "CeramicPot",
# 		"tier": 0
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
    {"name": "WoodenPlanks", "Label": "Wooden Planks", "tier": 0},
    {"name": "AdminBlocks", "Label": "Admin Blocks", "tier": 0},
    {"name": "StoneTiles", "Label": "Stone Tiles", "tier": 0},
    {"name": "RedTiles", "Label": "Red Tiles", "tier": 0},
    {"name": "DarkTiles", "Label": "Dark Tiles", "tier": 0},
    {"name": "Terracotta", "Label": "Terracotta", "tier": 0},
    {"name": "TerracottaTiles", "Label": "Terracotta Tiles", "tier": 0},
    {"name": "Bricks", "Label": "Bricks", "tier": 0},
    {"name": "RedBricks", "Label": "Red Bricks", "tier": 0},
    {"name": "DarkBricks", "Label": "Black Bricks", "tier": 0},
    {"name": "TerracottaBricks", "Label": "Terracotta Bricks", "tier": 0},
    {"name": "Concrete", "Label": "Concrete", "tier": 2},
    {"name": "ConcreteBricks", "Label": "Concrete Bricks", "tier": 2},
    {"name": "ConcreteTiles", "Label": "Concrete Tiles", "tier": 2},
    {"name": "ConcreteSmallTiles", "Label": "Concrete Small Tiles", "tier": 2},
    {"name": "ReinforcedConcrete", "Label": "Reinforced Concrete", "tier": 2},
    {
        "name": "ReinforcedConcreteTiles",
        "Label": "Reinforced Concrete Tiles",
        "tier": 2,
    },
    {
        "name": "ReinforcedConcreteSmallTiles",
        "Label": "Reinforced Concrete Small Tiles",
        "tier": 2,
    },
    {
        "name": "ReinforcedConcreteBricks",
        "Label": "Reinforced Concrete Bricks",
        "tier": 2,
    },
    {"name": "DangerBlock", "Label": "Danger Block", "tier": 2},
    {"name": "RustyCopperCasing", "Label": "Rusty Copper Casing", "tier": 1},
    {"name": "RustyIronCasing", "Label": "Rusty Iron Casing", "tier": 2},
    {"name": "BasicPlatform", "Label": "Basic Platform", "tier": 0},
    {"name": "PlasticBlock", "Label": "Plastic Block", "tier": 0},
    {"name": "GlassBlock", "Label": "Glass Block", "tier": 0},
    {"name": "PaintWhite", "Label": "Paint White", "tier": 0},
    {"name": "PaintGray", "Label": "Paint Gray", "tier": 0},
    {"name": "PaintBlack", "Label": "Paint Black", "tier": 0},
    {"name": "PaintGreen", "Label": "Paint Green", "tier": 0},
    {"name": "PaintRed", "Label": "Paint Red", "tier": 0},
    {"name": "PaintBlue", "Label": "Paint Blue", "tier": 0},
    {"name": "PaintCopper", "Label": "Paint Copper", "tier": 0},
    {"name": "PaintSteel", "Label": "Paint Steel", "tier": 0},
    {"name": "PaintStainlessSteel", "Label": "Paint StainlessSteel", "tier": 0},
    {"name": "PaintTitanium", "Label": "Paint Titanium", "tier": 0},
    {"name": "PaintHardMetal", "Label": "Paint Hard Metal", "tier": 0},
    {"name": "PaintGold", "Label": "Paint Gold", "tier": 0},
    {"name": "PaintYellow", "Label": "Paint Yellow", "tier": 0},
    {"name": "PaintMagenta", "Label": "Paint Magenta", "tier": 0},
    {"name": "PaintCyan", "Label": "Paint Cyan", "tier": 0},
]

static_mesh_block = [{"name": "Column"}, {"name": "FluetedColumn"}]

equipped = [
    {"name": "Torch", "logic": "Equipped/TorchBP.TorchBP_C"},
    {"name": "Flashlight", "logic": "Equipped/FlashlightBP.FlashlightBP_C"},
    {"name": "NightVision", "logic": "Equipped/NightVisionBP.NightVisionBP_C"},
    {
        "name": "AdvancedNightVision",
        "logic": "Equipped/AdvancedNightVisionBP.AdvancedNightVisionBP_C",
    },
    {"name": "Steampack", "logic": "Equipped/SteampackBP.SteampackBP_C"},
    {"name": "Jetpack", "logic": "Equipped/JetpackBP.JetpackBP_C"},
    {
        "name": "AdvancedJetpack",
        "logic": "Equipped/AdvancedJetpackBP.AdvancedJetpackBP_C",
    },
    {
        "name": "AntigravityUnit",
        "logic": "Equipped/AntigravityUnitBP.AntigravityUnitBP_C",
    },
    {"name": "Scanner", "logic": "Equipped/ScannerBP.ScannerBP_C"},
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
        "logic": building_single_logic,
    }

    objects_array.append(item)

    block = {
        "name": one["name"],
        "Item": one["name"],
        "Actor": "/Game/Blocks/" + one["name"] + "BP." + one["name"] + "BP_C",
        "BlockLogic": "BlockLogic" if "BlockLogic" not in one else one["BlockLogic"],
        "class": static_block,
    }

    if "sub_blocks" in one:
        block["sub_blocks"] = one["sub_blocks"]

    objects_array.append(block)

for one in simple_single:
    cvs.append([one["name"], CamelToSpaces(one["name"])])

    objects_array.append(
        {
            "class": static_item,
            "name": one["name"],
            "image": "T_" + one["name"],
            "logic": building_single_logic,
            "logic_json": {"Block": one["name"]},
            "max_count": 32,
            "tag": "Decoration",
            "label_parts": [[one["name"], "misc"]],
            "tier": one["tier"] if "tier" in one else 0,
        }
    )

    block = {
        "class": static_block,
        "name": one["name"],
        "Item": one["name"],
        "Actor": "/Game/Blocks/" + one["name"] + "BP." + one["name"] + "BP_C",
        "logic": "BlockLogic" if "BlockLogic" not in one else one["BlockLogic"],
    }

    if "sub_blocks" in one:
        block["sub_blocks"] = one["sub_blocks"]

    objects_array.append(block)

for one in simple_deco:
    cvs.append([one["name"], CamelToSpaces(one["name"])])

    deco = {
        "class": static_item,
        "name": one["name"],
        "image": "T_" + one["name"],
        "logic": building_decoration_logic,
        "logic_json": {"Block": one["name"]},
        "max_count": 32,
        "label_parts": [[one["name"], "misc"]],
        "tag": "Decoration",
    }
    if "logic" in one:
        deco["logic"] = one["logic"]

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
            "logic": building_plane_logic,
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
            "logic": building_single_logic,
            "logic_json": {"Block": one["name"]},
            "max_count": 32,
            "tag": "Decoration",
            "label_parts": [[one["name"], "misc"]],
        }
    )
    # objects_array.append({ "class": tesselator_static_mesh,
    # 	"name": one["name"]_static_mesh,
    # 	"mesh": "Models/" + one["name"],
    # })
    objects_array.append(
        {
            "class": static_block,
            "name": one["name"],
            "Item": one["name"],
            "Actor": "/Game/Blocks/" + one["name"] + "BP." + one["name"] + "BP_C",
            "logic": "BlockLogic",
            # "Tesselator": one["name"]_static_mesh
        }
    )

images = []

images.append(
    {
        "base": "T_" + "JetpackBase",
        "new_name": "T_" + "Jetpack",
        "mul": "T_" + "Aluminium",
    }
)

images.append(
    {
        "base": "T_" + "JetpackBase",
        "new_name": "T_" + "Steampack",
        "mul": "T_" + "Copper",
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
    if "logic" in one:
        equ["logic"] = one["logic"]

    objects_array.append(equ)


data = {"Objects": objects_array}

write_file("Generated/Mixed/misc.json", data)

write_file("Loc/source/misc.json", cvs)

objects_array = []

objects_array.append(
    {"class": ico_generator, "name": "Misc" + ico_generator, "images": images}
)

data = {"Objects": objects_array}

write_file("Generated/Resources/misc.json", data)
