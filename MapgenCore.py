from Common import *

objects_array = []

csv = []

mapgen_objects = [
    {
        "name": "Sand",
        "Color": [142 / 255.0, 119 / 255.0, 71 / 255.0],
        "Side": [158 / 255.0, 123 / 255.0, 100 / 255.0],
        "Item": [200 / 255.0, 200 / 255.0, 50 / 255.0],
        "Drops": "Sand",
        "Hardness": 1,
    },
    {
        "name": "Sandstone",
        "Color": [223 / 255.0, 221 / 255.0, 192 / 255.0],
        "Side": [158 / 255.0, 123 / 255.0, 100 / 255.0],
        "Item": [200 / 255.0, 200 / 255.0, 50 / 255.0],
        "Drops": "Sand",
        "Hardness": 1,
    },
    {
        "name": "Stone",
        "Color": [111 / 255.0, 106 / 255.0, 85 / 255.0],
        "Side": [111 / 255.0, 106 / 255.0, 85 / 255.0],
        "Item": [128 / 255.0, 128 / 255.0, 128 / 255.0],
        "Drops": "Stone",
        "Hardness": 2,
    },
    {
        "name": "DesertSand",
        "Color": [175 / 255.0, 148 / 255.0, 87 / 255.0],
        "Side": [180 / 255.0, 133 / 255.0, 109 / 255.0],
        "Item": [200 / 255.0, 200 / 255.0, 50 / 255.0],
        "Drops": "Sand",
        "Hardness": 1,
    },
    {
        "name": "Grass",
        "Color": [85 / 255.0 / 5, 100 / 255.0 / 5, 29 / 255.0 / 5],
        "Side": [134 / 255.0 / 5, 102 / 255.0 / 5, 64 / 255.0 / 5],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "Drops": "Dirt",
        "Hardness": 1,
    },
    {
        "name": "BogFog",
        "Color": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "Side": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "Drops": "Dirt",
        "Hardness": 1,
    },
    {
        "name": "LavaSmoke",
        "Color": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "Side": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "Item": [128 / 255.0, 128 / 255.0, 128 / 255.0],
        "Drops": "Basalt",
        "Hardness": 2,
    },
    {
        "name": "Lava",
        "Color": [104 / 255.0, 104 / 255.0, 104 / 255.0],
        "Side": [104 / 255.0, 104 / 255.0, 104 / 255.0],
        "Item": [127 / 255.0, 127 / 255.0, 127 / 255.0],
        "Drops": "Basalt",
        "Hardness": 5,
    },
    {
        "name": "Basalt",
        "Color": [105 / 255.0, 105 / 255.0, 105 / 255.0],
        "Side": [105 / 255.0, 105 / 255.0, 105 / 255.0],
        "Item": [128 / 255.0, 128 / 255.0, 128 / 255.0],
        "Drops": "Basalt",
        "Hardness": 2,
    },
    {
        "name": "Bog",
        "Color": [109 / 255.0 / 5, 108 / 255.0 / 5, 20 / 255.0 / 5],
        "Side": [134 / 255.0 / 5, 102 / 255.0 / 5, 64 / 255.0 / 5],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "Drops": "Dirt",
        "Hardness": 1,
    },
    {
        "name": "PineForest",
        "Color": [87 / 255.0, 66 / 255.0, 38 / 255.0],
        "Side": [87 / 255.0, 66 / 255.0, 38 / 255.0],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "Drops": "Dirt",
        "Hardness": 1,
    },
    {
        "name": "CoralBubbleEmitter",
        "Color": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "Side": [255 / 255.0, 0 / 255.0, 0 / 255.0],
        "Item": [128 / 255.0, 128 / 255.0, 128 / 255.0],
        "Drops": "Dirt",
        "Hardness": 2,
    },
    {
        "name": "Dirt",
        "Color": [134 / 255.0, 102 / 255.0, 64 / 255.0],
        "Side": [134 / 255.0, 102 / 255.0, 64 / 255.0],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "Drops": "Dirt",
        "Hardness": 1,
    },
    {
        "name": "Gravel",
        "Color": [141 / 255.0, 118 / 255.0, 70 / 255.0],
        "Side": [141 / 255.0, 118 / 255.0, 70 / 255.0],
        "Item": [200 / 255.0, 200 / 255.0, 50 / 255.0],
        "Drops": "Gravel",
        "Hardness": 1,
    },
    {
        "name": "DryGrass",
        "Color": [85 / 255.0, 50 / 255.0, 29 / 255.0],
        "Side": [134 / 255.0, 102 / 255.0, 65 / 255.0],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "Drops": "Dirt",
        "Hardness": 1,
    },
    {
        "name": "Limestone",
        "Color": [161 / 255.0, 156 / 255.0, 135 / 255.0],
        "Side": [161 / 255.0, 156 / 255.0, 135 / 255.0],
        "Item": [161 / 255.0, 156 / 255.0, 135 / 255.0],
        "Drops": "Gravel",
        "Hardness": 1.5,
    },
    {
        "name": "RedStone",
        "Color": [91 / 255.0, 56 / 255.0, 35 / 255.0],
        "Side": [91 / 255.0, 56 / 255.0, 35 / 255.0],
        "Item": [91 / 255.0, 56 / 255.0, 35 / 255.0],
        "Drops": "RedStone",
        "Hardness": 2,
    },
    {
        "name": "DarkStone",
        "Color": [12 / 255.0, 8 / 255.0, 12 / 255.0],
        "Side": [12 / 255.0, 8 / 255.0, 12 / 255.0],
        "Item": [12 / 255.0, 8 / 255.0, 12 / 255.0],
        "Drops": "DarkStone",
        "Hardness": 2,
    },
    {
        "name": "Snow",
        "Color": [253 / 255.0, 252 / 255.0, 254 / 255.0],
        "Side": [133 / 255.0, 101 / 255.0, 64 / 255.0],
        "Item": [255 / 255.0, 255 / 255.0, 255 / 255.0],
        "Drops": "Snow",
        "Hardness": 1,
    },
    {
        "name": "Granite",
        "Color": [111 / 255.0, 106 / 255.0, 85 / 255.0],
        "Side": [111 / 255.0, 106 / 255.0, 85 / 255.0],
        "Item": [128 / 255.0, 128 / 255.0, 128 / 255.0],
        "Drops": "Granite",
        "Hardness": 4,
    },
    {
        "name": "Peat",
        "Color": [109 / 255.0 / 7, 108 / 255.0 / 7, 20 / 255.0 / 7],
        "Side": [134 / 255.0 / 7, 102 / 255.0 / 7, 64 / 255.0 / 7],
        "Item": [102 / 255.0, 51 / 255.0, 0 / 255.0],
        "Drops": "Peat",
        "Hardness": 1,
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
            "item_logic": building_brush_slot_logic,
            "Mesh": "Models/piece",
            "Materials": ["Materials/" + object["Drops"]],
            "Color": object["Item"],
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
            "Material": "Materials/Triplanar/" + object["name"] + "Material",
        }
    )
    objects_array.append(
        {
            "class": static_surface,
            "name": object["name"] + "Surface",
            "Tesselator": object["name"] + "Surface",
            "Item": object["name"] + "Surface",
            "ColorSide": object["Side"],
            "color_top": object["Color"],
            "is_surface": True,
        }
    )
    pickaxe_recipes.append(
        {
            "name": object["name"] + "SurfaceBreaking",
            "Ticks": object["Hardness"] * 20,
            "Input": {"Items": [{"name": object["name"] + "Surface", "Count": 1}]},
            "Output": {"Items": [{"name": object["Drops"] + "Surface", "Count": 1}]},
        }
    )

data = {"Objects": objects_array}

write_file("Generated/Mixed/mapgen_core.json", data)

objects_array = []

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Multitool" + recipe_dictionary,
        "Recipes": pickaxe_recipes,
    }
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/mapgen_core.json", data)

write_file("Loc/source/mapgen_core.json", csv)
