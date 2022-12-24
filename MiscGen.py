from Common import *
from MachinesList import *

objects_array = []

cvs = []

wooden_misc = [
    {"Name": "Chair"},
    {"Name": "Table", "Positions": [[0, 0, 0], [-1, 0, 0]]},
    {"Name": "Rack"},
    {
        "Name": "Bed",
        "Positions": [[0, 0, 0], [-1, 0, 0]],
        "BlockLogic": "BedBlockLogic",
    },
    {"Name": "Ladder"},
    {
        "Name": "Door",
        "Positions": [[0, 0, 0], [0, 0, 1]],
        "BlockLogic": "DoorBlockLogic",
    },
    {"Name": "Window", "Positions": [[0, 0, 0], [0, 0, 1]]},
]

simple_single = [
    {
        "Name": "CeramicRoof",
    },
    {
        "Name": "Stairs",
    },
    {
        "Name": "WoodenStairs",
    },
    {
        "Name": "CopperChair",
    },
    {
        "Name": "FireCup",
    },
    {"Name": "PlasticWindow", "Positions": [[0, 0, 0], [0, 0, 1]]},
    {"Name": "SteelFence", "BlockLogic": "FenceBlockLogic", "Tier": 1},
    {"Name": "StainlessSteelFence", "BlockLogic": "FenceBlockLogic", "Tier": 2},
    {
        "Name": "Fence",
        "BlockLogic": "FenceBlockLogic",
    },
]

# ,{
# 		"Name": "Campfire",
# 		"Tier": 0
# 	}
# 	{
# 		"Name": "CeramicPlate",
# 		"Tier": 0
# 	},{
# 		"Name": "Candle",
# 		"Tier": 0
# 	},{
# 		"Name": "CeramicCup",
# 		"Tier": 0
# 	},{
# 		"Name": "CeramicPot",
# 		"Tier": 0
# 	}

simple_deco = [
    {"Name": "Firefly"},
    {"Name": "Flies"},
    {"Name": "Birds"},
    {"Name": "DesertSound"},
    {"Name": "SwampSound"},
    {"Name": "Butterfly"},
    {"Name": "Leafes"},
    {"Name": "Bugs"},
]

simple_blocks = [
    {"Name": "WoodenPlanks", "Label": "Wooden Planks", "Tier": 0},
    {"Name": "AdminBlocks", "Label": "Admin Blocks", "Tier": 0},
    {"Name": "StoneTiles", "Label": "Stone Tiles", "Tier": 0},
    {"Name": "RedTiles", "Label": "Red Tiles", "Tier": 0},
    {"Name": "DarkTiles", "Label": "Dark Tiles", "Tier": 0},
    {"Name": "Terracotta", "Label": "Terracotta", "Tier": 0},
    {"Name": "TerracottaTiles", "Label": "Terracotta Tiles", "Tier": 0},
    {"Name": "Bricks", "Label": "Bricks", "Tier": 0},
    {"Name": "RedBricks", "Label": "Red Bricks", "Tier": 0},
    {"Name": "DarkBricks", "Label": "Black Bricks", "Tier": 0},
    {"Name": "TerracottaBricks", "Label": "Terracotta Bricks", "Tier": 0},
    {"Name": "Concrete", "Label": "Concrete", "Tier": 2},
    {"Name": "ConcreteBricks", "Label": "Concrete Bricks", "Tier": 2},
    {"Name": "ConcreteTiles", "Label": "Concrete Tiles", "Tier": 2},
    {"Name": "ConcreteSmallTiles", "Label": "Concrete Small Tiles", "Tier": 2},
    {"Name": "ReinforcedConcrete", "Label": "Reinforced Concrete", "Tier": 2},
    {
        "Name": "ReinforcedConcreteTiles",
        "Label": "Reinforced Concrete Tiles",
        "Tier": 2,
    },
    {
        "Name": "ReinforcedConcreteSmallTiles",
        "Label": "Reinforced Concrete Small Tiles",
        "Tier": 2,
    },
    {
        "Name": "ReinforcedConcreteBricks",
        "Label": "Reinforced Concrete Bricks",
        "Tier": 2,
    },
    {"Name": "DangerBlock", "Label": "Danger Block", "Tier": 2},
    {"Name": "RustyCopperCasing", "Label": "Rusty Copper Casing", "Tier": 1},
    {"Name": "RustyIronCasing", "Label": "Rusty Iron Casing", "Tier": 2},
    {"Name": "BasicPlatform", "Label": "Basic Platform", "Tier": 0},
    {"Name": "PlasticBlock", "Label": "Plastic Block", "Tier": 0},
    {"Name": "GlassBlock", "Label": "Glass Block", "Tier": 0},
    {"Name": "PaintWhite", "Label": "Paint White", "Tier": 0},
    {"Name": "PaintGray", "Label": "Paint Gray", "Tier": 0},
    {"Name": "PaintBlack", "Label": "Paint Black", "Tier": 0},
    {"Name": "PaintGreen", "Label": "Paint Green", "Tier": 0},
    {"Name": "PaintRed", "Label": "Paint Red", "Tier": 0},
    {"Name": "PaintBlue", "Label": "Paint Blue", "Tier": 0},
    {"Name": "PaintCopper", "Label": "Paint Copper", "Tier": 0},
    {"Name": "PaintSteel", "Label": "Paint Steel", "Tier": 0},
    {"Name": "PaintStainlessSteel", "Label": "Paint StainlessSteel", "Tier": 0},
    {"Name": "PaintTitanium", "Label": "Paint Titanium", "Tier": 0},
    {"Name": "PaintHardMetal", "Label": "Paint Hard Metal", "Tier": 0},
    {"Name": "PaintGold", "Label": "Paint Gold", "Tier": 0},
    {"Name": "PaintYellow", "Label": "Paint Yellow", "Tier": 0},
    {"Name": "PaintMagenta", "Label": "Paint Magenta", "Tier": 0},
    {"Name": "PaintCyan", "Label": "Paint Cyan", "Tier": 0},
]

static_mesh_block = [{"Name": "Column"}, {"Name": "FluetedColumn"}]

equipped = [
    {"Name": "Torch", "ItemLogic": "Equipped/TorchBP.TorchBP_C"},
    {"Name": "Flashlight", "ItemLogic": "Equipped/FlashlightBP.FlashlightBP_C"},
    {"Name": "NightVision", "ItemLogic": "Equipped/NightVisionBP.NightVisionBP_C"},
    {
        "Name": "AdvancedNightVision",
        "ItemLogic": "Equipped/AdvancedNightVisionBP.AdvancedNightVisionBP_C",
    },
    {"Name": "Steampack", "ItemLogic": "Equipped/SteampackBP.SteampackBP_C"},
    {"Name": "Jetpack", "ItemLogic": "Equipped/JetpackBP.JetpackBP_C"},
    {
        "Name": "AdvancedJetpack",
        "ItemLogic": "Equipped/AdvancedJetpackBP.AdvancedJetpackBP_C",
    },
    {
        "Name": "AntigravityUnit",
        "ItemLogic": "Equipped/AntigravityUnitBP.AntigravityUnitBP_C",
    },
    {"Name": "Scanner", "ItemLogic": "Equipped/ScannerBP.ScannerBP_C"},
]

for one in wooden_misc:
    cvs.append([one["Name"], "Wooden " + CamelToSpaces(one["Name"])])

    item = {
        "Class": static_item,
        "Name": one["Name"],
        "Image": "T_" + one["Name"],
        "LogicJson": {"Block": one["Name"]},
        "MaxCount": 32,
        "Tag": "Decoration",
        "LabelParts": [[one["Name"], "misc"]],
        "ItemLogic": building_single_logic,
    }

    objects_array.append(item)

    block = {
        "Name": one["Name"],
        "Item": one["Name"],
        "Actor": "/Game/Blocks/" + one["Name"] + "BP." + one["Name"] + "BP_C",
        "BlockLogic": "BlockLogic" if "BlockLogic" not in one else one["BlockLogic"],
        "Class": static_block,
    }

    if "Positions" in one:
        block["Positions"] = one["Positions"]

    objects_array.append(block)

for one in simple_single:
    cvs.append([one["Name"], CamelToSpaces(one["Name"])])

    objects_array.append(
        {
            "Class": static_item,
            "Name": one["Name"],
            "Image": "T_" + one["Name"],
            "ItemLogic": building_single_logic,
            "LogicJson": {"Block": one["Name"]},
            "MaxCount": 32,
            "Tag": "Decoration",
            "LabelParts": [[one["Name"], "misc"]],
            "Tier": one["Tier"] if "Tier" in one else 0,
        }
    )

    block = {
        "Class": static_block,
        "Name": one["Name"],
        "Item": one["Name"],
        "Actor": "/Game/Blocks/" + one["Name"] + "BP." + one["Name"] + "BP_C",
        "BlockLogic": "BlockLogic" if "BlockLogic" not in one else one["BlockLogic"],
    }

    if "Positions" in one:
        block["Positions"] = one["Positions"]

    objects_array.append(block)

for one in simple_deco:
    cvs.append([one["Name"], CamelToSpaces(one["Name"])])

    deco = {
        "Class": static_item,
        "Name": one["Name"],
        "Image": "T_" + one["Name"],
        "ItemLogic": building_decoration_logic,
        "LogicJson": {"Block": one["Name"]},
        "MaxCount": 32,
        "LabelParts": [[one["Name"], "misc"]],
        "Tag": "Decoration",
    }
    if "ItemLogic" in one:
        deco["ItemLogic"] = one["ItemLogic"]

    objects_array.append(deco)
    objects_array.append(
        {
            "Class": static_decoration,
            "Name": one["Name"],
            "Item": one["Name"],
            "Actor": "Decorations/" + one["Name"] + "BP." + one["Name"] + "BP_C",
            "BlockLogic": "BlockLogic",
        }
    )

for one in simple_blocks:
    cvs.append([one["Name"], CamelToSpaces(one["Name"])])

    objects_array.append(
        {
            "Class": static_item,
            "Name": one["Name"],
            "Image": "T_" + one["Name"],
            "ItemLogic": building_plane_logic,
            "LogicJson": {"Block": one["Name"], "BuildingMode": "Plane"},
            "MaxCount": 999,
            "Tag": "Decoration",
            "LabelParts": [[one["Name"], "misc"]],
            "Category": "Block",
            "DescriptionParts": [["BuildingBlock", "common"]],
        }
    )
    objects_array.append(
        {
            "Class": tesselator_cube,
            "Name": one["Name"],
            "Material": "Materials/" + one["Name"],
        }
    )
    objects_array.append(
        {
            "Class": static_block,
            "Name": one["Name"],
            "Item": one["Name"],
            "Tesselator": one["Name"],
        }
    )

for one in static_mesh_block:
    cvs.append([one["Name"], CamelToSpaces(one["Name"])])

    objects_array.append(
        {
            "Class": static_item,
            "Name": one["Name"],
            "Image": "T_" + one["Name"],
            "ItemLogic": building_single_logic,
            "LogicJson": {"Block": one["Name"]},
            "MaxCount": 32,
            "Tag": "Decoration",
            "LabelParts": [[one["Name"], "misc"]],
        }
    )
    # objects_array.append({ "Class": tesselator_static_mesh,
    # 	"Name": one["Name"]_static_mesh,
    # 	"Mesh": "Models/" + one["Name"],
    # })
    objects_array.append(
        {
            "Class": static_block,
            "Name": one["Name"],
            "Item": one["Name"],
            "Actor": "/Game/Blocks/" + one["Name"] + "BP." + one["Name"] + "BP_C",
            "BlockLogic": "BlockLogic",
            # "Tesselator": one["Name"]_static_mesh
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
    cvs.append([one["Name"], CamelToSpaces(one["Name"])])

    equ = {
        "Class": static_item,
        "Name": one["Name"],
        "Image": "T_" + one["Name"],
        "LogicJson": {"Block": one["Name"]},
        "MaxCount": 32,
        "Tag": "Misc",
        "LabelParts": [[one["Name"], "misc"]],
    }
    if "ItemLogic" in one:
        equ["ItemLogic"] = one["ItemLogic"]

    objects_array.append(equ)


data = {"Objects": objects_array}

write_file("Generated/Mixed/misc.json", data)

write_file("Loc/source/misc.json", cvs)

objects_array = []

objects_array.append(
    {"Class": ico_generator, "Name": "Misc" + ico_generator, "Images": images}
)

data = {"Objects": objects_array}

write_file("Generated/Resources/misc.json", data)
