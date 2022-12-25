from MachinesList import *
from PartsList import *
from Common import *
import copy

objects_array = []

researches = []

images = []
recipes_cutter = []
recipes_hammer = []
recipes_macerator = []
recipes_hand = []
recipes_assembler = []
recipes_furnace = []
recipes_press = []
recipes_wrench = []
recipes_smelt = []
recipes_liq_dump = []
recipes_gas_dump = []
recipes_gasfurn = []

recipes_gasturb = []

cvs = []


def append_gas_burning(recipe):
    gas2 = copy.deepcopy(recipe)
    gas2["Input"]["Items"].append(
        {"name": "Oxygen", "Count": gas2["Input"]["Items"][0]["Count"]}
    )
    gas2["Output"]["Items"][0]["Count"] = gas2["Output"]["Items"][0]["Count"] * 2
    gas2["Output"]["Items"] = [gas2["Output"]["Items"][0]]
    recipes_gasturb.append(gas2)

    recipes_gasturb.append(recipe)


# tiered parts
for part in parts:
    for tier in tiers_numlist:
        material = tier_material[tier]
        if part["StartTier"] <= tier and part["EndTier"] >= tier:
            cvs.append(
                [material + part["name"], CamelToSpaces(material) + " " + part["Label"]]
            )
            level = tier - part["StartTier"]
            item = {
                "class": static_item,
                "name": material + part["name"],
                "label_parts": [[material + part["name"], "parts"]],
                "image": "T_" + material + part["name"],
                "max_count": part["Stack"],
                "logic_json": {"Block": material + part["name"]},
                "tag": "Misc",
                "Materials": ["Materials/" + material],
                "category": "Parts",
            }
            if "item_logic" in part:
                item["item_logic"] = part["item_logic"]

            if "Mesh" in part:
                item["Mesh"] = part["Mesh"]

            if "Materials" in part:
                dict = copy.deepcopy(part["Materials"])
                for i in range(0, len(dict)):
                    if dict[i].find("%Material%") != -1:
                        dict[i] = dict[i].replace("%Material%", tier_material[tier])
                item["Materials"] = dict

            if "tag" in part:
                item["tag"] = part["tag"]

            objects_array.append(item)

            images.append(
                {
                    "NewName": "T_" + material + part["name"],
                    "Base": "T_" + part["name"],
                    "MulMask": "T_" + material,
                    "AddMask": "T_" + part["name"] + additive_ico,
                }
            )

            if "Volume" in part:
                recipes_macerator.append(
                    {
                        "name": material + part["name"],
                        "Input": {
                            "Items": [
                                {"name": material + part["name"], "Count": 1},
                            ]
                        },
                        "ResourceInput": {
                            "name": "Kinetic",
                            "Count": 10 * 1.5**level,
                        },
                        "Output": {
                            "Items": [
                                {"name": material + "Dust", "Count": part["Volume"]}
                            ]
                        },
                        "Ticks": 80 * part["Volume"] * 1.5**level,
                    }
                )
            recipes_wrench.append(simple_in_out_recipe(material + part["name"]))

            if (
                part["name"] == "Casing"
                and part["StartTier"] <= tier
                and part["EndTier"] >= tier
            ):
                recipes_hand.append(
                    {
                        "name": material + "Casing",
                        "Input": {"Items": [{"name": material + "Plate", "Count": 3}]},
                        "Output": {
                            "Items": [{"name": material + "Casing", "Count": 1}]
                        },
                        "Ticks": 40,
                    }
                )
                objects_array.append(
                    {
                        "class": tesselator_cube,
                        "name": material + "Casing" + tesselator,
                        "Material": "Materials/" + material + "Casing",
                    }
                )
                objects_array.append(
                    {
                        "class": static_block,
                        "name": material + "Casing",
                        "Item": material + "Casing",
                        "Tesselator": material + "Casing" + tesselator,
                    }
                )

            if part["name"] == "Plate":
                recipes_hammer.append(
                    {
                        "name": material + "Plate",
                        "Input": {
                            "Items": [
                                {
                                    "name": material
                                    + ("Ingot" if material != "Stone" else "Surface"),
                                    "Count": 1,
                                },
                            ]
                        },
                        "ResourceInput": {
                            "name": "Kinetic",
                            "Count": 10 * 1.5**level,
                        },
                        "Output": {"Items": [{"name": material + "Plate", "Count": 1}]},
                        "Ticks": 80 * 1.5**level,
                    }
                )
                recipes_hand.append(
                    {
                        "name": material + "Plate",
                        "Input": {
                            "Items": [
                                {
                                    "name": material
                                    + ("Ingot" if material != "Stone" else "Surface"),
                                    "Count": 1,
                                }
                            ]
                        },
                        "Output": {"Items": [{"name": material + "Plate", "Count": 1}]},
                        "Ticks": 20,
                    }
                )

            if part["name"] == "Parts":
                recipes_hand.append(
                    {  # parts recipe
                        "name": material + "Parts",
                        "Input": {"Items": [{"name": material + "Plate", "Count": 1}]},
                        "Output": {"Items": [{"name": material + "Parts", "Count": 1}]},
                        "Ticks": 20,
                    }
                )
                recipes_cutter.append(
                    {
                        "name": material + "Parts",
                        "Input": {
                            "Items": [
                                {"name": material + "Plate", "Count": 1},
                            ]
                        },
                        "ResourceInput": {
                            "name": "Kinetic",
                            "Count": 10 * 1.5**level,
                        },
                        "Output": {"Items": [{"name": material + "Parts", "Count": 1}]},
                        "Ticks": 80 * 1.5**level,
                    }
                )

# ingots, dusts, fluids, gems, blocks
for material in materials:

    # abstract
    if "IsAbstract" in material:
        cvs.append([material["name"], material["Label"]])
        item = {
            "class": static_item,
            "name": material["name"],
            "image": "T_" + material["name"],
            "max_count": 1,
            "tag": "Misc",
            "label_parts": [[material["name"], "parts"]],
        }

        if "Unit" in material:
            item["Unit"] = material["Unit"]

        if "UnitMul" in material:
            item["UnitMul"] = material["UnitMul"]

        if "category" in material:
            item["category"] = material["category"]

        if "tag" in material:
            item["tag"] = material["tag"]

        if "Description" in material:
            item["description_parts"] = material["Description"]

        objects_array.append(item)

    # exact
    if "IsExact" in material:
        cvs.append([material["name"], material["Label"]])
        item = {
            "class": static_item,
            "name": material["name"],
            "image": "T_" + material["name"],
            "max_count": 32 if material["name"] != "Signal" else 214748364,
            "label_parts": [[material["name"], "parts"]],
            "tag": "Misc",
        }

        if "Craftable" in material:
            item["Craftable"] = False

        if "category" in material:
            item["category"] = material["category"]

        if "Description" in material:
            item["description_parts"] = material["Description"]

        if "tag" in material:
            item["tag"] = material["tag"]

        if "Unit" in material:
            item["Unit"] = material["Unit"]

        if "Stack" in material:
            item["max_count"] = material["Stack"]

        if "Mesh" in material:
            item["Mesh"] = material["Mesh"]
            item["Materials"] = ["Materials/" + material["name"]]

        if "Materials" in material:
            item["Materials"] = material["Materials"]

        if "Burnable" in material:
            recipes_furnace.append(
                {
                    "name": material["name"],
                    "Input": {"Items": [{"name": material["name"], "Count": 1}]},
                    "Output": {
                        "Items": [
                            # {
                            # 	"name": "AshDust",
                            # 	"Count": material["Burnable"]["TotalAsh"],
                            # }
                        ],
                    },
                    "ResourceOutput": {
                        "name": "Heat",
                        "Count": material["Burnable"]["HeatPerTick"],
                    },
                    "Ticks": material["Burnable"]["BurnTime"],
                }
            )
            item["description_parts"] = [
                [
                    "burnable",
                    "common",
                    material["Burnable"]["BurnTime"]
                    * material["Burnable"]["HeatPerTick"],
                ],
                ["power_output", "common", material["Burnable"]["HeatPerTick"] * 20],
            ]

        objects_array.append(item)

    # ingot
    if "IsIngot" in material:
        cvs.append([material["name"] + "Ingot", material["Label"] + " Ingot"])
        item = {
            "class": static_item,
            "name": material["name"] + "Ingot",
            "image": "T_" + material["name"] + "Ingot",
            "max_count": 32,
            "Mesh": "Models/Ingot",
            "Materials": ["Materials/" + material["name"]],
            "label_parts": [[material["name"] + "Ingot", "parts"]],
            "tag": "Misc",
            "category": "Ingot",
        }

        if "category" in material:
            item["category"] = material["category"]

        if "tag" in material:
            item["tag"] = material["tag"]

        objects_array.append(item)

        images.append(
            {
                "NewName": "T_" + material["name"] + "Ingot",
                "Base": "T_" + "Ingot",
                "MulMask": "T_" + material["name"],
                "AddMask": "T_" + "Ingot" + additive_ico,
            }
        )

        if "SmeltLevel" in material and material["SmeltLevel"] <= 0:
            recipes_smelt.append(
                {
                    "name": material["name"] + "Ingot",
                    "Input": {
                        "Items": [{"name": material["name"] + "Dust", "Count": 1}],
                    },
                    "ResourceInput": {
                        "name": "Heat",
                        "Count": 10,
                    },
                    "Output": {
                        "Items": [{"name": material["name"] + "Ingot", "Count": 1}]
                    },
                    "Ticks": 200,
                }
            )

        recipes_macerator.append(
            {
                "name": material["name"] + "Ingot",
                "Input": {
                    "Items": [
                        {"name": material["name"] + "Ingot", "Count": 1},
                    ]
                },
                "ResourceInput": {"name": "Kinetic", "Count": 15},
                "Output": {"Items": [{"name": material["name"] + "Dust", "Count": 1}]},
                "Ticks": 120,
            }
        )

    if "IsBlock" in material:
        cvs.append([material["name"] + "Block", material["Label"] + " Block"])
        item = {
            "class": static_item,
            "name": material["name"] + "Block",
            "image": "T_" + material["name"] + "Block",
            "max_count": 999,
            # "Mesh": "Models/Ingot",
            "Materials": ["Materials/" + material["name"]],
            "label_parts": [[material["name"] + "Block", "parts"]],
            "tag": "Decoration",
            "category": "Block",
            "item_logic": building_cube_logic,
            "logic_json": {"Block": material["name"] + "Block"},
        }

        if "category" in material:
            item["category"] = material["category"]

        if "tag" in material:
            item["tag"] = material["tag"]

        objects_array.append(item)

        images.append(
            {
                "NewName": "T_" + material["name"] + "Block",
                "Base": "T_" + "Block",
                "MulMask": "T_" + material["name"],
                "AddMask": "T_" + "Block" + additive_ico,
            }
        )
        objects_array.append(
            {
                "class": tesselator_cube,
                "name": material["name"] + "Block" + tesselator,
                "Material": "Materials/" + material["name"],
            }
        )
        objects_array.append(
            {
                "class": static_block,
                "name": material["name"] + "Block",
                "Item": material["name"] + "Block",
                "Tesselator": material["name"] + "Block" + tesselator,
            }
        )

        recipes_press.append(
            {
                "name": material["name"] + "Block",
                "Input": {
                    "Items": [{"name": material["name"] + "Dust", "Count": 4}],
                },
                "ResourceInput": {
                    "name": "Kinetic",
                    "Count": 10,
                },
                "Output": {"Items": [{"name": material["name"] + "Block", "Count": 1}]},
                "Ticks": 200,
            }
        )

        recipes_wrench.append(
            {
                "name": material["name"] + "Block" + "Wrenching",
                "Ticks": 20,
                "Input": {"Items": [{"name": material["name"] + "Block", "Count": 1}]},
                "Output": {"Items": [{"name": material["name"] + "Block", "Count": 1}]},
            }
        )

    # fluid
    if "IsFluid" in material:
        cvs.append([material["name"], material["Label"]])
        item = {
            "class": static_item,
            "name": material["name"] + "",
            "image": "T_" + material["name"] + "",
            "max_count": 1,
            "category": "",
            "tag": "Misc",
            "label_parts": [[material["name"], "parts"]],
            "UnitMul": 1.0 / 1000.0,
            "category": "Fluid",
            "description_parts": [["Fluid", "common"], ["ByPipes", "common"]],
            "Solid": False,
        }

        if "category" in material:
            item["category"] = material["category"]

        if "tag" in material:
            item["tag"] = material["tag"]

        # if item["MaterialKey"] + " " + item["Key"] in explicites:
        # 	item["ExplicitKey"] = ex_cvs[explicites.index(item["MaterialKey"] + " " + item["Key"])][0]

        if "Burnable" in material:
            item["description_parts"].append(
                [
                    "burnable",
                    "common",
                    material["Burnable"]["BurnTime"]
                    * material["Burnable"]["HeatPerTick"],
                ]
            )
            item["description_parts"].append(
                ["power_output", "common", material["Burnable"]["HeatPerTick"] * 20]
            )

        objects_array.append(item)

        images.append(
            {
                "NewName": "T_" + material["name"] + "",
                "Base": "T_" + "",
                "MulMask": "T_" + material["name"],
                "AddMask": "T_" + "" + additive_ico,
            }
        )

        if "UnitMul" in material:
            item["UnitMul"] = material["UnitMul"]

        if "Color" in material:
            item["Color"] = material["Color"]

        if "Burnable" in material:
            recipes_gasfurn.append(
                {
                    "Input": {
                        "Items": [{"name": material["name"] + "", "Count": 1000}]
                    },
                    "Output": {
                        "Items": [],
                    },
                    "ResourceOutput": {
                        "name": "Heat",
                        "Count": material["Burnable"]["HeatPerTick"],
                    },
                    "Ticks": material["Burnable"]["BurnTime"],
                    "name": material["name"] + "",
                }
            )

        recipes_liq_dump.append(
            {
                "name": material["name"] + "Dumping",
                "Input": {
                    "Items": [
                        {
                            "name": material["name"] + "",
                            "Count": 1000 if material["name"] != "Steam" else 10000,
                        }
                    ]
                },
                "Output": {"Items": []},
                "Ticks": 200,
            }
        )

    # gas
    if "IsGas" in material:
        cvs.append([material["name"], material["Label"]])
        item = {
            "class": static_item,
            "name": material["name"] + "",
            "image": "T_" + material["name"] + "",
            "max_count": 1,
            "category": "",
            "tag": "Misc",
            "label_parts": [[material["name"], "parts"]],
            "UnitMul": 1.0 / 1000.0,
            "category": "Fluid",
            "description_parts": [["Gas", "common"], ["ByPipes", "common"]],
            "Solid": False,
        }

        if "category" in material:
            item["category"] = material["category"]

        if "tag" in material:
            item["tag"] = material["tag"]

        # if item["MaterialKey"] + " " + item["Key"] in explicites:
        # 	item["ExplicitKey"] = ex_cvs[explicites.index(item["MaterialKey"] + " " + item["Key"])][0]

        if "Burnable" in material:
            item["description_parts"].append(
                [
                    "burnable",
                    "common",
                    material["Burnable"]["BurnTime"]
                    * material["Burnable"]["HeatPerTick"],
                ]
            )
            item["description_parts"].append(
                ["power_output", "common", material["Burnable"]["HeatPerTick"] * 20]
            )

        objects_array.append(item)

        images.append(
            {
                "NewName": "T_" + material["name"] + "",
                "Base": "T_" + "",
                "MulMask": "T_" + material["name"],
                "AddMask": "T_" + "" + additive_ico,
            }
        )

        if "UnitMul" in material:
            item["UnitMul"] = material["UnitMul"]

        if "Color" in material:
            item["Color"] = material["Color"]

        if "Burnable" in material:
            recipes_gasfurn.append(
                {
                    "Input": {
                        "Items": [{"name": material["name"] + "", "Count": 1000}]
                    },
                    "Output": {
                        "Items": [],
                    },
                    "ResourceOutput": {
                        "name": "Heat",
                        "Count": material["Burnable"]["HeatPerTick"],
                    },
                    "Ticks": material["Burnable"]["BurnTime"],
                    "name": material["name"],
                }
            )

        recipes_gas_dump.append(
            {
                "name": material["name"],
                "Input": {
                    "Items": [
                        {
                            "name": material["name"] + "",
                            "Count": 1000 if material["name"] != "Steam" else 10000,
                        }
                    ]
                },
                "Output": {"Items": []},
                "Ticks": 1,
            }
        )

    # dust
    if "IsDust" in material:
        cvs.append([material["name"] + "Dust", material["Label"] + " Dust"])
        item = {
            "class": static_item,
            "name": material["name"] + "Dust",
            "image": "T_" + material["name"] + "Dust",
            "max_count": 32,
            "label_parts": [[material["name"] + "Dust", "parts"]],
            "tag": "Misc",
            "Mesh": "Models/Dust",
            "Materials": ["Materials/" + material["name"] + "Dust"],
            "UnitMul": 1,
            "category": "Dust",
        }

        if "category" in material:
            item["category"] = material["category"]

        if "tag" in material:
            item["tag"] = material["tag"]

        objects_array.append(item)

        images.append(
            {
                "NewName": "T_" + material["name"] + "Dust",
                "Base": "T_" + "Dust",
                "MulMask": "T_" + material["name"],
                "AddMask": "T_" + "Dust" + additive_ico,
            }
        )
        if "Burnable" in material:
            recipes_furnace.append(
                {
                    "Input": {
                        "Items": [{"name": material["name"] + "Dust", "Count": 1}]
                    },
                    "Output": {
                        "Items": [
                            # {
                            # 	"name": "AshDust",
                            # 	"Count": material["Burnable"]["TotalAsh"]
                            # },
                        ],
                    },
                    "ResourceOutput": {
                        "name": "Heat",
                        "Count": material["Burnable"]["HeatPerTick"],
                    },
                    "Ticks": material["Burnable"]["BurnTime"],
                    "name": material["name"] + "Dust",
                }
            )

# tools
for tool in tools:
    cvs.append([tool["name"], tool["Label"]])
    for tier in tiers_numlist:
        if tool["StartTier"] <= tier and tool["EndTier"] >= tier:
            item_name = tier_material[tier] + tool["name"]
            item = {
                "class": static_item,
                "name": item_name,
                "image": "T_" + item_name,
                "item_logic": tool["item_logic"],
                "logic_json": {
                    "RecipeDictionary": tool["name"],
                    "Tier": tier,
                },
                "max_count": 1,
                "label_parts": [
                    [tier_material[tier], "common"],
                    [tool["name"], "parts"],
                ],
                "tag": "Misc",
                "label_format": ["machines_label_format", "common"],
            }

            objects_array.append(item)

            images.append(
                {
                    "NewName": "T_" + item_name,
                    "Base": "T_" + tool["name"],
                    "MulMask": "T_" + tier_material[tier],
                    "AddMask": "T_" + tool["name"] + additive_ico,
                }
            )

            if tool["name"] == "Screwdriver" and "IsIngot" in named_material(
                tier_material[tier]
            ):
                recipes_hand.append(
                    {
                        "name": tier_material[tier] + "Screwdriver",
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Parts", "Count": 1},
                                {"name": "Plank", "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Screwdriver",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Ticks": 40,
                    }
                )

            if tool["name"] == "Multitool" and "IsIngot" in named_material(
                tier_material[tier]
            ):
                recipes_hand.append(
                    {
                        "name": tier_material[tier] + "Multitool",
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Pipe", "Count": 2},
                                {"name": tier_material[tier] + "Plate", "Count": 2},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": tier * 5 + 10,
                                },
                                {"name": circuits[tier], "Count": 10},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Multitool", "Count": 1}
                            ]
                        },
                        "Ticks": 40,
                    }
                )

            if tool["name"] == "PaintTool" and "IsIngot" in named_material(
                tier_material[tier]
            ):
                recipes_hand.append(
                    {
                        "name": tier_material[tier] + "PaintTool",
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Pipe", "Count": 2},
                                {"name": tier_material[tier] + "Plate", "Count": 2},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": tier * 5 + 10,
                                },
                                {"name": circuits[tier], "Count": 10},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "PaintTool", "Count": 1}
                            ]
                        },
                        "Ticks": 40,
                    }
                )

data = {"Objects": objects_array}

write_file("Generated/Mixed/parts.json", data)

objects_array = []

objects_array.append(
    {"class": ico_generator, "name": "Parts" + ico_generator, "Images": images}
)

data = {"Objects": objects_array}

write_file("Generated/Resources/parts.json", data)

objects_array = []

objects_array.append(
    {"class": recipe_dictionary, "name": "CuttingMachine", "Recipes": recipes_cutter}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "AutomaticHammer", "Recipes": recipes_hammer}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Macerator", "Recipes": recipes_macerator}
)

for r in recipes_hand:
    r["Locked"] = True

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Hand",
        "Recipes": recipes_hand,
        "UsedIn": [
            {
                "Item": "Hand",
            }
        ],
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Press", "Recipes": recipes_press}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Furnace", "Recipes": recipes_furnace}
)


used_in = []
for tier in range(tools[0]["StartTier"], tools[0]["EndTier"]):
    used_in.append(
        {
            "Item": tier_material[tier] + "Multitool",
        }
    )

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Multitool",
        "Recipes": recipes_wrench,
        "UsedIn": used_in,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Smelter", "Recipes": recipes_smelt}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Assembler", "Recipes": recipes_assembler}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "FluidDump", "Recipes": recipes_liq_dump}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "GasDump", "Recipes": recipes_gas_dump}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "FluidFurnace", "Recipes": recipes_gasfurn}
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/parts.json", data)

data = {"Objects": researches}

write_file("Generated/Researches/parts.json", data)

write_file("Loc/source/parts.json", cvs)
