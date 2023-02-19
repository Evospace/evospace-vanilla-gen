from MachinesList import *
from Common import *

objects_array = []

cvs = []

ore_types = [
    {
        # https://en.wikipedia.org/wiki/List_of_copper_ores
        "name": "Copper",
        "Byproducts": [
            "GoldDust",  # wash
            ["CopperOreDust", "MalachiteCrystal", "MalachiteCluster"],  # sifter
        ],
        "color": [1, 0.1, 0],
        "Hardness": 1.5,
        "drops": "CopperOre",
        "Remain": 1000,
    },
    {
        # https://www.tf.uni-kiel.de/matwis/amat/iss/kap_a/advanced/aa_2_1.html
        # https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D0%BA%D0%B5%D0%BB%D1%8C#%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5
        "name": "Iron",
        "Byproducts": [
            "ChromiumOxideDust",  # wash
            ["IronOreDust", "CinnabarCrystal", "CinnabarCluster"],  # sifter
        ],
        "color": [111 / 255.0, 106 / 255.0, 81 / 255.0],
        "Hardness": 2,
        "drops": "IronOre",
        "Remain": 1000,
    },
    {
        "name": "Uranium",
        "Byproducts": [
            "Uranium235Dust",  # wash
            ["ThoriumDust", "UraniniteCrystal", "UraniniteCluster"],  # sifter
        ],
        "ByproductChanse": [20],
        "color": [0, 1, 0],
        "Hardness": 2,
        "tier": 5,
        "drops": "UraniumOre",
        "Remain": 1000,
    },
    {
        # https://en.wikipedia.org/wiki/Cassiterite
        "name": "Aluminium",
        "Byproducts": [
            "TitaniumOxideDust",  # wash
            ["AluminiumOreDust", "RutileCrystal", "Emerald"],  # sifter
        ],
        "color": [0.5, 0.5, 1],
        "Hardness": 2,
        "drops": "AluminiumOre",
        "Oxide": True,
        "Remain": 1000,
    },
    {
        "name": "Coal",
        "color": [0.06, 0.06, 0.06],
        "side": [0.06, 0.06, 0.06],
        "Item": [0.06, 0.06, 0.06],
        "drops": "Coal",
        "tier": 0,
        "Hardness": 1,
        "NotOre": True,
        "Remain": 1000,
    },
    {
        "name": "Clay",
        "color": [202 / 255.0, 115 / 255.0, 43 / 255.0],
        "side": [202 / 255.0, 115 / 255.0, 43 / 255.0],
        "Item": [202 / 255.0, 115 / 255.0, 43 / 255.0],
        "drops": "Clay",
        "tier": 0,
        "Hardness": 1,
        "NotOre": True,
        "Byproducts": ["RareEarthElement"],
    },
]

images = []

for ore_type in ore_types:
    item_name = ore_type["name"] + "Ore"
    named_mat = named_material(ore_type["name"])

    cvs.append([ore_type["name"] + "Ore", ore_type["name"] + " Ore"])

    item = {
        "class": static_item,
        "name": item_name,
        "mesh": "Models/Ore",
        "image": "T_" + ore_type["name"] + "Ore",
        "max_count": 32,
        "category": "Ore",
        "label_parts": [[ore_type["name"] + "Ore", "ores"]],
        "CommonTextKeys": [],
        "Materials": ["Materials/" + ore_type["name"] + "ImpureOreGravel"],
    }

    if "SmeltLevel" in named_mat:
        item["CommonTextKeys"].append("SmeltLevel" + str(named_mat["SmeltLevel"]))

    objects_array.append(item)
    objects_array.append(
        {
            "class": "TesselatorMarching",
            "name": ore_type["name"] + "Ore",
            "Material": "Materials/Triplanar/" + ore_type["name"] + "OreMaterial",
        }
    )
    objects_array.append(
        {
            "class": static_surface,
            "name": ore_type["name"] + "Ore",
            "Tesselator": ore_type["name"] + "Ore",
            "Item": item_name,
            "ColorSide": ore_type["color"],
            "color_top": ore_type["color"],
            "is_surface": True,
        }
    )
    images.append(
        {
            "base": "T_" + "Ore",
            "new_name": "T_" + ore_type["name"] + "Ore",
            "mul": "T_" + ore_type["name"],
        }
    )

    if "NotOre" not in ore_type:
        # impur gravel
        cvs.append(
            [
                ore_type["name"] + "ImpureOreGravel",
                ore_type["name"] + " Impure Ore Gravel",
            ]
        )
        item = {
            "class": static_item,
            "name": ore_type["name"] + "ImpureOreGravel",
            "Label": ore_type["name"] + " Impure Ore Gravel",
            "mesh": "Models/Gravel",
            "image": "T_" + ore_type["name"] + "ImpureOreGravel",
            "max_count": 32,
            "Materials": ["Materials/" + ore_type["name"] + "ImpureOreGravel"],
            "category": "Ore",
            "label_parts": [[ore_type["name"] + "ImpureOreGravel", "ores"]],
            "CommonTextKeys": [],
        }

        if "SmeltLevel" in named_mat:
            item["CommonTextKeys"].append("SmeltLevel" + str(named_mat["SmeltLevel"]))

        if "mesh" in named_mat:
            item["mesh"] = named_mat["mesh"]

        objects_array.append(item)

        # gravel
        cvs.append([ore_type["name"] + "OreGravel", ore_type["name"] + " Ore Gravel"])
        item = {
            "class": static_item,
            "name": ore_type["name"] + "OreGravel",
            "Label": ore_type["name"] + " Ore Gravel",
            "mesh": "Models/Gravel",
            "image": "T_" + ore_type["name"] + "OreGravel",
            "max_count": 32,
            "Materials": ["Materials/" + ore_type["name"] + "OreGravel"],
            "category": "Ore",
            "label_parts": [[ore_type["name"] + "OreGravel", "ores"]],
            "CommonTextKeys": [],
        }

        if "SmeltLevel" in named_mat:
            item["CommonTextKeys"].append("SmeltLevel" + str(named_mat["SmeltLevel"]))

        objects_array.append(item)

        # impure dust
        cvs.append(
            [ore_type["name"] + "OreDust", ore_type["name"] + " Impure Ore Dust"]
        )
        item = {
            "class": static_item,
            "name": ore_type["name"] + "OreDust",
            "Label": ore_type["name"] + " Impure Ore Dust",
            "mesh": "Models/Dust",
            "image": "T_" + ore_type["name"] + "OreDust",
            "max_count": 32,
            "Materials": ["Materials/ImpureOreDust"],
            "category": "Ore",
            "label_parts": [[ore_type["name"] + "OreDust", "ores"]],
            "CommonTextKeys": [],
            "Materials": ["Materials/" + ore_type["name"] + "OreGravel"],
        }

        if "SmeltLevel" in named_mat:
            item["CommonTextKeys"].append("SmeltLevel" + str(named_mat["SmeltLevel"]))

        objects_array.append(item)

        images.append(
            {
                "base": "T_" + "Gravel",
                "new_name": "T_" + ore_type["name"] + "OreGravel",
                "mul": "T_" + ore_type["name"],
                "add": "T_" + "Gravel" + additive_ico,
            }
        )

        images.append(
            {
                "base": "T_" + "Gravel",
                "new_name": "T_" + ore_type["name"] + "ImpureOreGravel",
                "mul": "T_" + ore_type["name"],
                "add": ["T_" + "impure_gravel_add", "T_" + "Gravel" + additive_ico],
            }
        )

        images.append(
            {
                "base": "T_" + "Dust",
                "new_name": "T_" + ore_type["name"] + "OreDust",
                "mul": "T_" + ore_type["name"],
                "add": "T_" + "impure_dust_add",
            }
        )

data = {"Objects": objects_array}

filename = "Generated/Mixed/ores.json"

write_file(filename, data)

objects_array = []

objects_array.append(
    {"class": ico_generator, "name": "Ores" + ico_generator, "images": images}
)

data = {"Objects": objects_array}

write_file("Generated/Resources/ores.json", data)

write_file("Loc/source/ores.json", cvs)
