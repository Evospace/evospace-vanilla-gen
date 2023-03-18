from Common import *

objects_array = []

csv = []

mapgen_objects = [
    {
        "name": "Sand",
        "color": [142 / 255.0, 119 / 255.0, 71 / 255.0],
        "side": [158 / 255.0, 123 / 255.0, 100 / 255.0],
        "Item": [200 / 255.0, 200 / 255.0, 50 / 255.0],
        "drops": "Sand",
        "hardness": 1,
    },
    {
        "name": "Sandstone",
        "color": [223 / 255.0, 221 / 255.0, 192 / 255.0],
        "side": [158 / 255.0, 123 / 255.0, 100 / 255.0],
        "Item": [200 / 255.0, 200 / 255.0, 50 / 255.0],
        "drops": "Sand",
        "hardness": 1,
    },
    {
        "name": "Stone",
        "color": [111 / 255.0, 106 / 255.0, 85 / 255.0],
        "side": [111 / 255.0, 106 / 255.0, 85 / 255.0],
        "Item": [128 / 255.0, 128 / 255.0, 128 / 255.0],
        "drops": "Stone",
        "hardness": 2,
    },
    {
        "name": "DesertSand",
        "color": [175 / 255.0, 148 / 255.0, 87 / 255.0],
        "side": [180 / 255.0, 133 / 255.0, 109 / 255.0],
        "Item": [200 / 255.0, 200 / 255.0, 50 / 255.0],
        "drops": "Sand",
        "hardness": 1,
    },
    {
        "name": "Grass",
        "color": [85 / 255.0 / 5, 100 / 255.0 / 5, 29 / 255.0 / 5],
        "side": [134 / 255.0 / 5, 102 / 255.0 / 5, 64 / 255.0 / 5],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "drops": "Dirt",
        "hardness": 1,
    },
    {
        "name": "BogFog",
        "color": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "side": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "drops": "Dirt",
        "hardness": 1,
    },
    {
        "name": "LavaSmoke",
        "color": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "side": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "Item": [128 / 255.0, 128 / 255.0, 128 / 255.0],
        "drops": "Basalt",
        "hardness": 2,
    },
    {
        "name": "Lava",
        "color": [104 / 255.0, 104 / 255.0, 104 / 255.0],
        "side": [104 / 255.0, 104 / 255.0, 104 / 255.0],
        "Item": [127 / 255.0, 127 / 255.0, 127 / 255.0],
        "drops": "Basalt",
        "hardness": 5,
    },
    {
        "name": "Basalt",
        "color": [105 / 255.0, 105 / 255.0, 105 / 255.0],
        "side": [105 / 255.0, 105 / 255.0, 105 / 255.0],
        "Item": [128 / 255.0, 128 / 255.0, 128 / 255.0],
        "drops": "Basalt",
        "hardness": 2,
    },
    {
        "name": "Bog",
        "color": [109 / 255.0 / 5, 108 / 255.0 / 5, 20 / 255.0 / 5],
        "side": [134 / 255.0 / 5, 102 / 255.0 / 5, 64 / 255.0 / 5],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "drops": "Dirt",
        "hardness": 1,
    },
    {
        "name": "PineForest",
        "color": [87 / 255.0, 66 / 255.0, 38 / 255.0],
        "side": [87 / 255.0, 66 / 255.0, 38 / 255.0],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "drops": "Dirt",
        "hardness": 1,
    },
    {
        "name": "CoralBubbleEmitter",
        "color": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "side": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "Item": [128 / 255.0, 128 / 255.0, 128 / 255.0],
        "drops": "Dirt",
        "hardness": 2,
    },
    {
        "name": "Dirt",
        "color": [134 / 255.0, 102 / 255.0, 64 / 255.0],
        "side": [134 / 255.0, 102 / 255.0, 64 / 255.0],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "drops": "Dirt",
        "hardness": 1,
    },
    {
        "name": "Gravel",
        "color": [141 / 255.0, 118 / 255.0, 70 / 255.0],
        "side": [141 / 255.0, 118 / 255.0, 70 / 255.0],
        "Item": [200 / 255.0, 200 / 255.0, 50 / 255.0],
        "drops": "Gravel",
        "hardness": 1,
    },
    {
        "name": "DryGrass",
        "color": [85 / 255.0, 50 / 255.0, 29 / 255.0],
        "side": [134 / 255.0, 102 / 255.0, 65 / 255.0],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "drops": "Dirt",
        "hardness": 1,
    },
    {
        "name": "Limestone",
        "color": [161 / 255.0, 156 / 255.0, 135 / 255.0],
        "side": [161 / 255.0, 156 / 255.0, 135 / 255.0],
        "Item": [161 / 255.0, 156 / 255.0, 135 / 255.0],
        "drops": "Gravel",
        "hardness": 1.5,
    },
    {
        "name": "RedStone",
        "color": [91 / 255.0, 56 / 255.0, 35 / 255.0],
        "side": [91 / 255.0, 56 / 255.0, 35 / 255.0],
        "Item": [91 / 255.0, 56 / 255.0, 35 / 255.0],
        "drops": "RedStone",
        "hardness": 2,
    },
    {
        "name": "DarkStone",
        "color": [12 / 255.0, 8 / 255.0, 12 / 255.0],
        "side": [12 / 255.0, 8 / 255.0, 12 / 255.0],
        "Item": [12 / 255.0, 8 / 255.0, 12 / 255.0],
        "drops": "DarkStone",
        "hardness": 2,
    },
    {
        "name": "Snow",
        "color": [253 / 255.0, 252 / 255.0, 254 / 255.0],
        "side": [133 / 255.0, 101 / 255.0, 64 / 255.0],
        "Item": [255 / 255.0, 255 / 255.0, 255 / 255.0],
        "drops": "Snow",
        "hardness": 1,
    },
    {
        "name": "Granite",
        "color": [111 / 255.0, 106 / 255.0, 85 / 255.0],
        "side": [111 / 255.0, 106 / 255.0, 85 / 255.0],
        "Item": [128 / 255.0, 128 / 255.0, 128 / 255.0],
        "drops": "Granite",
        "hardness": 4,
    },
    {
        "name": "Peat",
        "color": [109 / 255.0 / 7, 108 / 255.0 / 7, 20 / 255.0 / 7],
        "side": [134 / 255.0 / 7, 102 / 255.0 / 7, 64 / 255.0 / 7],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "drops": "Peat",
        "hardness": 1,
    },
]

pickaxe_recipes = []

for object in mapgen_objects:
    csv.append([object["name"] + "Surface", CamelToSpaces(object["name"])])

    objects_array.append(
        {
            "class": static_item,
            "name": object["name"] + "Surface",
            "image": "T_" + object["name"],
            "logic": building_brush_slot_logic,
            "mesh": "Models/piece",
            "materials": ["Materials/" + object["drops"]],
            "color": object["Item"],
            "logic_json": {"Block": object["name"] + "Surface"},
            "max_count": 64,
            "label_parts": [[object["name"] + "Surface", "mapgen_core"]],
            "tag": "Misc",
        }
    )
    objects_array.append(
        {
            "class": "TesselatorMarching",
            "name": object["name"] + "Surface",
            "material": "Materials/Triplanar/" + object["name"] + "Material",
        }
    )
    objects_array.append(
        {
            "class": static_surface,
            "name": object["name"] + "Surface",
            "tesselator": object["name"] + "Surface",
            "Item": object["name"] + "Surface",
            "color_side": object["side"],
            "color_top": object["color"],
            "is_surface": True,
        }
    )
    pickaxe_recipes.append(
        {
            "name": object["name"] + "SurfaceBreaking",
            "ticks": object["hardness"] * 20,
            "input": {"items": [{"name": object["name"] + "Surface", "count": 1}]},
            "output": {"items": [{"name": object["drops"] + "Surface", "count": 1}]},
        }
    )

data = {"Objects": objects_array}

write_file("Generated/Mixed/mapgen_core.json", data)

objects_array = []

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Multitool",
        "recipes": pickaxe_recipes,
    }
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/mapgen_core.json", data)

write_file("Loc/source/mapgen_core.json", csv)
