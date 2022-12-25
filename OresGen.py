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
        "Color": [1, 0.1, 0],
        "Hardness": 1.5,
        "Drops": "CopperOre",
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
        "Color": [111 / 255.0, 106 / 255.0, 81 / 255.0],
        "Hardness": 2,
        "Drops": "IronOre",
        "Remain": 1000,
    },
    {
        "name": "Uranium",
        "Byproducts": [
            "Uranium235Dust",  # wash
            ["ThoriumDust", "UraniniteCrystal", "UraniniteCluster"],  # sifter
        ],
        "ByproductChanse": [20],
        "Color": [0, 1, 0],
        "Hardness": 2,
        "Tier": 5,
        "Drops": "UraniumOre",
        "Remain": 1000,
    },
    {
        # https://en.wikipedia.org/wiki/Cassiterite
        "name": "Aluminium",
        "Byproducts": [
            "TitaniumOxideDust",  # wash
            ["AluminiumOreDust", "RutileCrystal", "Emerald"],  # sifter
        ],
        "Color": [0.5, 0.5, 1],
        "Hardness": 2,
        "Drops": "AluminiumOre",
        "Oxide": True,
        "Remain": 1000,
    },
    {
        "name": "Coal",
        "Color": [0.06, 0.06, 0.06],
        "Side": [0.06, 0.06, 0.06],
        "Item": [0.06, 0.06, 0.06],
        "Drops": "Coal",
        "Tier": 0,
        "Hardness": 1,
        "NotOre": True,
        "Remain": 1000,
    },
    {
        "name": "Clay",
        "Color": [202 / 255.0, 115 / 255.0, 43 / 255.0],
        "Side": [202 / 255.0, 115 / 255.0, 43 / 255.0],
        "Item": [202 / 255.0, 115 / 255.0, 43 / 255.0],
        "Drops": "Clay",
        "Tier": 0,
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
        "Mesh": "Models/Ore",
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
            "ColorSide": ore_type["Color"],
            "color_top": ore_type["Color"],
            "is_surface": True,
        }
    )
    images.append(
        {
            "Base": "T_" + "Ore",
            "NewName": "T_" + ore_type["name"] + "Ore",
            "MulMask": "T_" + ore_type["name"],
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
            "Mesh": "Models/Gravel",
            "image": "T_" + ore_type["name"] + "ImpureOreGravel",
            "max_count": 32,
            "Materials": ["Materials/" + ore_type["name"] + "ImpureOreGravel"],
            "category": "Ore",
            "label_parts": [[ore_type["name"] + "ImpureOreGravel", "ores"]],
            "CommonTextKeys": [],
        }

        if "SmeltLevel" in named_mat:
            item["CommonTextKeys"].append("SmeltLevel" + str(named_mat["SmeltLevel"]))

        if "Mesh" in named_mat:
            item["Mesh"] = named_mat["Mesh"]

        objects_array.append(item)

        # gravel
        cvs.append([ore_type["name"] + "OreGravel", ore_type["name"] + " Ore Gravel"])
        item = {
            "class": static_item,
            "name": ore_type["name"] + "OreGravel",
            "Label": ore_type["name"] + " Ore Gravel",
            "Mesh": "Models/Gravel",
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
            "Mesh": "Models/Dust",
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
                "Base": "T_" + "Gravel",
                "NewName": "T_" + ore_type["name"] + "OreGravel",
                "MulMask": "T_" + ore_type["name"],
                "AddMask": "T_" + "Gravel" + additive_ico,
            }
        )

        images.append(
            {
                "Base": "T_" + "Gravel",
                "NewName": "T_" + ore_type["name"] + "ImpureOreGravel",
                "MulMask": "T_" + ore_type["name"],
                "AddMask": ["T_" + "impure_gravel_add", "T_" + "Gravel" + additive_ico],
            }
        )

        images.append(
            {
                "Base": "T_" + "Dust",
                "NewName": "T_" + ore_type["name"] + "OreDust",
                "MulMask": "T_" + ore_type["name"],
                "AddMask": "T_" + "impure_dust_add",
            }
        )

data = {"Objects": objects_array}

filename = "Generated/Mixed/ores.json"

write_file(filename, data)

objects_array = []

objects_array.append(
    {"class": ico_generator, "name": "Ores" + ico_generator, "Images": images}
)

data = {"Objects": objects_array}

write_file("Generated/Resources/ores.json", data)

write_file("Loc/source/ores.json", cvs)
