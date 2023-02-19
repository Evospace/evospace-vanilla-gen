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
    gas2["input"]["items"].append(
        {"name": "Oxygen", "count": gas2["input"]["items"][0]["count"]}
    )
    gas2["output"]["items"][0]["count"] = gas2["output"]["items"][0]["count"] * 2
    gas2["output"]["items"] = [gas2["output"]["items"][0]]
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
                "max_count": part["max_count"],
                "logic_json": {"Block": material + part["name"]},
                "tag": "Misc",
                "Materials": ["Materials/" + material],
                "category": "Parts",
            }
            if "logic" in part:
                item["logic"] = part["logic"]

            if "mesh" in part:
                item["mesh"] = part["mesh"]

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
                    "new_name": "T_" + material + part["name"],
                    "base": "T_" + part["name"],
                    "mul": "T_" + material,
                    "add": "T_" + part["name"] + additive_ico,
                }
            )

            if "Volume" in part:
                recipes_macerator.append(
                    {
                        "name": material + part["name"],
                        "input": {
                            "items": [
                                {"name": material + part["name"], "count": 1},
                            ]
                        },
                        "res_input": {
                            "name": "Kinetic",
                            "count": 10 * 1.5**level,
                        },
                        "output": {
                            "items": [
                                {"name": material + "Dust", "count": part["Volume"]}
                            ]
                        },
                        "ticks": 80 * part["Volume"] * 1.5**level,
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
                        "input": {"items": [{"name": material + "Plate", "count": 3}]},
                        "output": {
                            "items": [{"name": material + "Casing", "count": 1}]
                        },
                        "ticks": 40,
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
                        "input": {
                            "items": [
                                {
                                    "name": material
                                    + ("Ingot" if material != "Stone" else "Surface"),
                                    "count": 1,
                                },
                            ]
                        },
                        "res_input": {
                            "name": "Kinetic",
                            "count": 10 * 1.5**level,
                        },
                        "output": {"items": [{"name": material + "Plate", "count": 1}]},
                        "ticks": 80 * 1.5**level,
                    }
                )
                recipes_hand.append(
                    {
                        "name": material + "Plate",
                        "input": {
                            "items": [
                                {
                                    "name": material
                                    + ("Ingot" if material != "Stone" else "Surface"),
                                    "count": 1,
                                }
                            ]
                        },
                        "output": {"items": [{"name": material + "Plate", "count": 1}]},
                        "ticks": 20,
                    }
                )

            if part["name"] == "Parts":
                recipes_hand.append(
                    {  # parts recipe
                        "name": material + "Parts",
                        "input": {"items": [{"name": material + "Plate", "count": 1}]},
                        "output": {"items": [{"name": material + "Parts", "count": 1}]},
                        "ticks": 20,
                    }
                )
                recipes_cutter.append(
                    {
                        "name": material + "Parts",
                        "input": {
                            "items": [
                                {"name": material + "Plate", "count": 1},
                            ]
                        },
                        "res_input": {
                            "name": "Kinetic",
                            "count": 10 * 1.5**level,
                        },
                        "output": {"items": [{"name": material + "Parts", "count": 1}]},
                        "ticks": 80 * 1.5**level,
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

        if "craftable" in material:
            item["craftable"] = False

        if "category" in material:
            item["category"] = material["category"]

        if "Description" in material:
            item["description_parts"] = material["Description"]

        if "tag" in material:
            item["tag"] = material["tag"]

        if "Unit" in material:
            item["Unit"] = material["Unit"]

        if "max_count" in material:
            item["max_count"] = material["max_count"]

        if "mesh" in material:
            item["mesh"] = material["mesh"]
            item["Materials"] = ["Materials/" + material["name"]]

        if "Materials" in material:
            item["Materials"] = material["Materials"]

        if "Burnable" in material:
            recipes_furnace.append(
                {
                    "name": material["name"],
                    "input": {"items": [{"name": material["name"], "count": 1}]},
                    "output": {
                        "items": [
                            # {
                            # 	"name": "AshDust",
                            # 	"count": material["Burnable"]["TotalAsh"],
                            # }
                        ],
                    },
                    "res_output": {
                        "name": "Heat",
                        "count": material["Burnable"]["HeatPerTick"],
                    },
                    "ticks": material["Burnable"]["BurnTime"],
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
            "mesh": "Models/Ingot",
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
                "new_name": "T_" + material["name"] + "Ingot",
                "base": "T_" + "Ingot",
                "mul": "T_" + material["name"],
                "add": "T_" + "Ingot" + additive_ico,
            }
        )

        if "SmeltLevel" in material and material["SmeltLevel"] <= 0:
            recipes_smelt.append(
                {
                    "name": material["name"] + "Ingot",
                    "input": {
                        "items": [{"name": material["name"] + "Dust", "count": 1}],
                    },
                    "res_input": {
                        "name": "Heat",
                        "count": 10,
                    },
                    "output": {
                        "items": [{"name": material["name"] + "Ingot", "count": 1}]
                    },
                    "ticks": 200,
                }
            )

        recipes_macerator.append(
            {
                "name": material["name"] + "Ingot",
                "input": {
                    "items": [
                        {"name": material["name"] + "Ingot", "count": 1},
                    ]
                },
                "res_input": {"name": "Kinetic", "count": 15},
                "output": {"items": [{"name": material["name"] + "Dust", "count": 1}]},
                "ticks": 120,
            }
        )

    if "IsBlock" in material:
        cvs.append([material["name"] + "Block", material["Label"] + " Block"])
        item = {
            "class": static_item,
            "name": material["name"] + "Block",
            "image": "T_" + material["name"] + "Block",
            "max_count": 999,
            # "mesh": "Models/Ingot",
            "Materials": ["Materials/" + material["name"]],
            "label_parts": [[material["name"] + "Block", "parts"]],
            "tag": "Decoration",
            "category": "Block",
            "logic": building_cube_logic,
            "logic_json": {"Block": material["name"] + "Block"},
        }

        if "category" in material:
            item["category"] = material["category"]

        if "tag" in material:
            item["tag"] = material["tag"]

        objects_array.append(item)

        images.append(
            {
                "new_name": "T_" + material["name"] + "Block",
                "base": "T_" + "Block",
                "mul": "T_" + material["name"],
                "add": "T_" + "Block" + additive_ico,
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
                "input": {
                    "items": [{"name": material["name"] + "Dust", "count": 4}],
                },
                "res_input": {
                    "name": "Kinetic",
                    "count": 10,
                },
                "output": {"items": [{"name": material["name"] + "Block", "count": 1}]},
                "ticks": 200,
            }
        )

        recipes_wrench.append(
            {
                "name": material["name"] + "Block" + "Wrenching",
                "ticks": 20,
                "input": {"items": [{"name": material["name"] + "Block", "count": 1}]},
                "output": {"items": [{"name": material["name"] + "Block", "count": 1}]},
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
            "solid": False,
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
                "new_name": "T_" + material["name"] + "",
                "base": "T_" + "",
                "mul": "T_" + material["name"],
                "add": "T_" + "" + additive_ico,
            }
        )

        if "UnitMul" in material:
            item["UnitMul"] = material["UnitMul"]

        if "color" in material:
            item["color"] = material["color"]

        if "Burnable" in material:
            recipes_gasfurn.append(
                {
                    "input": {
                        "items": [{"name": material["name"] + "", "count": 1000}]
                    },
                    "output": {
                        "items": [],
                    },
                    "res_output": {
                        "name": "Heat",
                        "count": material["Burnable"]["HeatPerTick"],
                    },
                    "ticks": material["Burnable"]["BurnTime"],
                    "name": material["name"] + "",
                }
            )

        recipes_liq_dump.append(
            {
                "name": material["name"] + "Dumping",
                "input": {
                    "items": [
                        {
                            "name": material["name"] + "",
                            "count": 1000 if material["name"] != "Steam" else 10000,
                        }
                    ]
                },
                "output": {"items": []},
                "ticks": 200,
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
            "solid": False,
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
                "new_name": "T_" + material["name"] + "",
                "base": "T_" + "",
                "mul": "T_" + material["name"],
                "add": "T_" + "" + additive_ico,
            }
        )

        if "UnitMul" in material:
            item["UnitMul"] = material["UnitMul"]

        if "color" in material:
            item["color"] = material["color"]

        if "Burnable" in material:
            recipes_gasfurn.append(
                {
                    "input": {
                        "items": [{"name": material["name"] + "", "count": 1000}]
                    },
                    "output": {
                        "items": [],
                    },
                    "res_output": {
                        "name": "Heat",
                        "count": material["Burnable"]["HeatPerTick"],
                    },
                    "ticks": material["Burnable"]["BurnTime"],
                    "name": material["name"],
                }
            )

        recipes_gas_dump.append(
            {
                "name": material["name"],
                "input": {
                    "items": [
                        {
                            "name": material["name"] + "",
                            "count": 1000 if material["name"] != "Steam" else 10000,
                        }
                    ]
                },
                "output": {"items": []},
                "ticks": 1,
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
            "mesh": "Models/Dust",
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
                "new_name": "T_" + material["name"] + "Dust",
                "base": "T_" + "Dust",
                "mul": "T_" + material["name"],
                "add": "T_" + "Dust" + additive_ico,
            }
        )
        if "Burnable" in material:
            recipes_furnace.append(
                {
                    "input": {
                        "items": [{"name": material["name"] + "Dust", "count": 1}]
                    },
                    "output": {
                        "items": [
                            # {
                            # 	"name": "AshDust",
                            # 	"count": material["Burnable"]["TotalAsh"]
                            # },
                        ],
                    },
                    "res_output": {
                        "name": "Heat",
                        "count": material["Burnable"]["HeatPerTick"],
                    },
                    "ticks": material["Burnable"]["BurnTime"],
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
                "logic": tool["logic"],
                "logic_json": {
                    "RecipeDictionary": tool["name"],
                    "tier": tier,
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
                    "new_name": "T_" + item_name,
                    "base": "T_" + tool["name"],
                    "mul": "T_" + tier_material[tier],
                    "add": "T_" + tool["name"] + additive_ico,
                }
            )

            if tool["name"] == "Screwdriver" and "IsIngot" in named_material(
                tier_material[tier]
            ):
                recipes_hand.append(
                    {
                        "name": tier_material[tier] + "Screwdriver",
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Parts", "count": 1},
                                {"name": "Plank", "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Screwdriver",
                                    "count": 1,
                                }
                            ]
                        },
                        "ticks": 40,
                    }
                )

            if tool["name"] == "Multitool" and "IsIngot" in named_material(
                tier_material[tier]
            ):
                recipes_hand.append(
                    {
                        "name": tier_material[tier] + "Multitool",
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Pipe", "count": 2},
                                {"name": tier_material[tier] + "Plate", "count": 2},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": tier * 5 + 10,
                                },
                                {"name": circuits[tier], "count": 10},
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Multitool", "count": 1}
                            ]
                        },
                        "ticks": 40,
                    }
                )

            if tool["name"] == "PaintTool" and "IsIngot" in named_material(
                tier_material[tier]
            ):
                recipes_hand.append(
                    {
                        "name": tier_material[tier] + "PaintTool",
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Pipe", "count": 2},
                                {"name": tier_material[tier] + "Plate", "count": 2},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": tier * 5 + 10,
                                },
                                {"name": circuits[tier], "count": 10},
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "PaintTool", "count": 1}
                            ]
                        },
                        "ticks": 40,
                    }
                )

data = {"Objects": objects_array}

write_file("Generated/Mixed/parts.json", data)

objects_array = []

objects_array.append(
    {"class": ico_generator, "name": "Parts" + ico_generator, "images": images}
)

data = {"Objects": objects_array}

write_file("Generated/Resources/parts.json", data)

objects_array = []

objects_array.append(
    {"class": recipe_dictionary, "name": "CuttingMachine", "recipes": recipes_cutter}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "AutomaticHammer", "recipes": recipes_hammer}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Macerator", "recipes": recipes_macerator}
)

for r in recipes_hand:
    r["Locked"] = True

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Hand",
        "recipes": recipes_hand,
        "UsedIn": [
            {
                "Item": "Hand",
            }
        ],
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Press", "recipes": recipes_press}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Furnace", "recipes": recipes_furnace}
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
        "recipes": recipes_wrench,
        "UsedIn": used_in,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Smelter", "recipes": recipes_smelt}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Assembler", "recipes": recipes_assembler}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "FluidDump", "recipes": recipes_liq_dump}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "GasDump", "recipes": recipes_gas_dump}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "FluidFurnace", "recipes": recipes_gasfurn}
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/parts.json", data)

data = {"Objects": researches}

write_file("Generated/Researches/parts.json", data)

write_file("Loc/source/parts.json", cvs)
