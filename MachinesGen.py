from Common import *
from MachinesList import *
from PartsList import *
import copy

images = []
objects_array = []
objects_wiki_array = {}
recipes_hand = []
recipes_wrench = []
recipes_deconstructor = []
recipes_constructor = []
researches = []

cvs = []
desc_csv = []

researches.append(
    {
        "name": "Core" + static_research,
        "UnlokedItems": ["Core"],
    }
)


def append_recipe(recipe):
    item_count = 0
    for item in recipe["input"]["items"]:
        item_count = item_count + item["count"]

    con_recipe = copy.deepcopy(recipe)
    con_recipe["ticks"] = max(min(item_count * 10, 1200), 20)
    con_recipe["res_input"] = {"name": "Electricity", "count": 20}
    recipes_constructor.append(con_recipe)

    dec_recipe = copy.deepcopy(recipe)

    recipes_hand.append(recipe)

    output = copy.deepcopy(dec_recipe["input"])

    dec_recipe["input"] = copy.deepcopy(dec_recipe["output"])
    dec_recipe["ticks"] = max(min(item_count * 10, 1200), 20)
    dec_recipe["res_input"] = {"name": "Electricity", "count": 20}
    dec_recipe["output"] = copy.deepcopy(output)
    recipes_deconstructor.append(dec_recipe)


for machine in machines:
    cvs.append([machine["name"], machine["Label"]])
    desc_csv.append([machine["name"], ""])
    for tier in tiers_numlist:
        if machine["StartTier"] <= tier and machine["EndTier"] >= tier:
            item_name = tier_material[tier] + machine["name"]
            block_name = tier_material[tier] + machine["name"]

            image = machine["name"] if "image" not in machine else machine["image"]

            level = tier - machine["StartTier"]

            item = {
                "class": static_item,
                "name": item_name,
                "image": "T_" + tier_material[tier] + image,
                "logic_json": {
                    "Block": block_name,
                },
                "max_count": 32,
                "tag": "Machines",
                "label_parts": [
                    [tier_material[tier], "common"],
                    [machine["name"], "machines"],
                ],
                "label_format": ["machines_label_format", "common"],
                "description_parts": [[machine["name"], "description_machines"]],
                "logic": building_single_logic,
                "category": CamelToSpaces(tier_material[tier]),
            }

            conv_speed_d = [1.66, 2.5, 3.33, 5, 6.66, 10, 20]
            arm_speed_d = [
                300 / 2,
                450 / 2,
                600 / 2,
                900 / 2,
                1200 / 2,
                1800 / 2,
                3600 / 2,
            ]

            if "PathFinding" in machine:
                item["logic_json"]["BuildingMode"] = "PathFinding"

            if "Description" in machine:
                for ss in machine["Description"]:
                    if ss == "SpeedBonus":
                        if level != 0:
                            item["description_parts"].append(
                                ["speedbonus", "common", round(1.5**level * 10) / 10]
                            )
                    elif ss == "PowerOutput":
                        item["description_parts"].append(
                            [
                                "power_output",
                                "common",
                                machine["PowerOutput"] * 20 * 2**level,
                            ]
                        )
                    else:
                        item["description_parts"].append([ss, "common"])

            if machine["name"] == "RobotArm" or machine["name"] == "FilteringRobotArm":
                item["description_parts"].append(["dps", "common", arm_speed_d[level]])

            if (
                machine["name"] == "FluidFurnace"
                or machine["name"] == "Furnace"
                or machine["name"] == "FissionReactor"
            ):
                item["description_parts"].append(
                    ["furnace_desc", "common", round(1.5**level)]
                )
                item["description_parts"].append(
                    ["furnace_desc2", "common", round(2.0**level)]
                )

            if machine["name"] == "GasTurbine" or machine["name"] == "CombustionEngine":
                item["description_parts"].append(
                    ["furnace_desc", "common", round(1.5**level)]
                )
                item["description_parts"].append(
                    ["furnace_desc3", "common", round(2.0**level)]
                )

            if machine["name"] == "Conveyor":
                item["description_parts"].append(["ips", "common", conv_speed_d[level]])

            if machine["name"] == "QuantumComputer":
                item["description_parts"].append(
                    ["computations", "common", 2**level * 150 * 10 / 20.0]
                )
                item["description_parts"].append(
                    ["power_input", "common", 2**level * 400 * 20 * 10]
                )
                item["description_parts"].append(
                    ["electric_drain", "common", 2**level * 400 * 20]
                )

            if machine["name"] == "Computer":
                item["description_parts"].append(
                    ["computations", "common", 2**level * 3 * 10 / 20.0]
                )
                item["description_parts"].append(
                    ["power_input", "common", 2**level * 20 * 10]
                )
                item["description_parts"].append(
                    ["electric_drain", "common", 2**level * 20]
                )

            if machine["name"] == "DrillingRig":
                item["description_parts"].append(
                    ["power_input", "common", 2**level * 20 * 30]
                )

            if machine["name"] == "FissionReactor":
                item["description_parts"].append(["heat_drain", "common", 80 * 20])

            if machine["name"] == "HeatPipe":
                item["description_parts"].append(["heat_drain", "common", 20])

            if machine["name"] == "Flywheel":
                item["description_parts"].append(["kinetic_drain", "common", 40])

            if machine["name"] == "Chest":
                item["description_parts"].append(["chest", "common", 20 + 5 * level])

            if machine["name"] == "Container":
                item["description_parts"].append(
                    ["container", "common", 30 * (level + 1)]
                )

            if machine["name"] == "BatteryBox" or machine["name"] == "SmallBattery":
                item["description_parts"].append(
                    [
                        "battery",
                        "common",
                        machine["CustomData"]["BaseCapacity"]
                        + machine["CustomData"]["BonusCapacity"] * level,
                    ]
                )

            if "tag" in machine:
                item["tag"] = machine["tag"]

            if "craftable" in machine:
                item["craftable"] = False

            # wiki json generation ------------------------------------------------
            objects_array.append(item)

            wiki_item = {}
            wiki_item["description_parts"] = item["description_parts"]
            wiki_item["level"] = level

            objects_wiki_array[tier_material[tier] + machine["name"]] = wiki_item

            # wiki json generation

            images.append(
                {
                    "new_name": "T_" + tier_material[tier] + image,
                    "base": "T_" + image,
                    "mul": "T_" + named_material(tier_material[tier])["name"],
                    "add": "T_" + image + additive_ico,
                }
            )

            block = {
                "name": block_name,
                "Item": item_name,
                "class": static_block,
                "logic": machine["name"],
                "replace_tag": machine["name"],
            }

            block["Actor"] = (
                "/Game/Blocks/" + machine["name"] + "BP." + machine["name"] + "BP_C"
            )

            if "Selector" in machine:
                block["Selector"] = machine["Selector"]

            if "Positions" in machine:
                block["Positions"] = machine["Positions"]

            objects_array.append(block)

            if "Unbreakable" not in machine:
                recipes_wrench.append(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "ticks": 20,
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                    }
                )

            objects_array.append(
                {
                    "class": recipe_dictionary,
                    "name": machine["name"],
                    "UsedIn": [
                        {"Item": tier_material[tier] + machine["name"], "tier": tier}
                    ],
                }
            )

            if machine["name"] == "Beam":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 3}
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Beam", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Corner":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 1}
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Corner", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Sign":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Plate"
                                    if tier != 0
                                    else "StoneSurface",
                                    "count": 1,
                                }
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Sign", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "AdvancedSign":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Sign", "count": 1},
                                {"name": electric_isolators[tier], "count": 1},
                                {"name": circuits[tier], "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "AdvancedSign",
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "LogicWire":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": wires[tier], "count": 2},
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "LogicWire", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if (
                machine["name"] == "LogicCircuit"
                or machine["name"] == "LogicDisplay"
                or machine["name"] == "LogicController"
                or machine["name"] == "LogicInterface"
            ):
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": "SteelPlate", "count": 2},
                                {"name": circuits[tier], "count": 1},
                                {"name": "SteelLogicWire", "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Scaffold":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Parts", "count": 4}
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Scaffold", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Container":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 3}
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Container", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "IndustrialSmelter":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": wires[tier], "count": 32 + level * 16},
                                {"name": tier_material[tier] + "Parts", "count": 12},
                                {"name": heat_isolators[tier], "count": 12},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "IndustrialSmelter",
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "PyrolysisUnit":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 5},
                                {
                                    "name": tier_material[tier] + "Pipe",
                                    "count": 5 + parts_ramp(level, 5),
                                },
                                {"name": tier_material[tier] + "Container", "count": 3},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "PyrolysisUnit",
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Smelter":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Plate"
                                    if tier > 0
                                    else "StoneSurface",
                                    "count": 4,
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Smelter", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "InductionCoil":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 3},
                                {"name": "CopperPipe", "count": 15 + 15 * level},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "InductionCoil",
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "PneumaticInput":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 3},
                                {"name": tier_material[tier] + "Parts", "count": 1},
                                {"name": "Glass", "count": 1},
                                {"name": "BrassDetails", "count": 1},
                                {"name": "BrassReductor", "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "PneumaticInput",
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Electrolyzer":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 3},
                                {"name": "Coal", "count": 2},
                                {"name": cables[tier], "count": 2},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Electrolyzer",
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "ChemReactor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 3},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 4 + parts_ramp(level),
                                },
                                {
                                    "name": tier_material[tier] + "ElectricEngine",
                                    "count": 1,
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "ChemReactor",
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Mixer":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 6},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 6 + parts_ramp(level),
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Mixer", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Press":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 1 + parts_ramp(level),
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Press", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "ElectricalSwitch":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 1},
                                {"name": tier_material[tier] + "Parts", "count": 1},
                                {"name": cables[tier], "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "ElectricalSwitch",
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Tank":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 12}
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Tank", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Terminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 3},
                                {"name": cables[tier], "count": 4},
                                {"name": "Glass", "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {"name": tier_material[tier] + "Terminal", "count": 1}
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "FlatTerminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Terminal", "count": 1}
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "FlatTerminal",
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "BigTerminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 6},
                                {"name": cables[tier], "count": 6},
                                {"name": "Glass", "count": 4},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "BigTerminal",
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "BigFlatTerminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "BigTerminal",
                                    "count": 1,
                                }
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "HugeTerminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 9},
                                {"name": cables[tier], "count": 8},
                                {"name": "Glass", "count": 9},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "HugeFlatTerminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "HugeTerminal",
                                    "count": 1,
                                }
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "SolarPanel":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 6 + parts_ramp(level),
                                },
                                {
                                    "name": tier_material[tier] + "ElectricEngine",
                                    "count": 1,
                                },
                                {"name": "Glass", "count": 3},
                                {"name": "Silicon", "count": 3},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "StirlingEngine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 2 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Pipe", "count": 2},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Generator":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": wires[tier], "count": 12 + level * 6},
                                {"name": tier_material[tier] + "Plate", "count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 2 + parts_ramp(level),
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "CompactGenerator":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": "CopperIngot", "count": 2 + parts_ramp(level)},
                                {"name": tier_material[tier] + "Plate", "count": 1},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 2 + parts_ramp(level),
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "AutomaticHammer":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 1 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Plate", "count": 4},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Macerator":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 3 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Plate", "count": 3},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Chest":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Plate"
                                    if tier != 0
                                    else "StoneSurface",
                                    "count": 5,
                                }
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Boiler":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Pipe",
                                    "count": 1 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Plate", "count": 3},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "IndustrialBoiler":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Pipe", "count": 25},
                                {"name": tier_material[tier] + "Plate", "count": 30},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 10 + level * 5,
                                },
                                {"name": circuits[tier], "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 100,
                    }
                )

            if machine["name"] == "Oven":
                r = {
                    "name": tier_material[tier] + machine["name"],
                    "input": {"items": [{"name": "StoneSurface", "count": 10}]},
                    "output": {
                        "items": [
                            {"name": tier_material[tier] + machine["name"], "count": 1}
                        ]
                    },
                    "tier": tier,
                    "ticks": 20,
                }
                if tier != 0:
                    r["input"]["items"].append(
                        {
                            "name": tier_material[tier] + "Pipe",
                            "count": 6 + parts_ramp(level),
                        }
                    )
                append_recipe(r)

            if machine["name"] == "BlastFurnace":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Pipe",
                                    "count": 8 + parts_ramp(level),
                                },
                                {"name": "StoneSurface", "count": 20},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "ElectricFurnace":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 3},
                                {"name": wires[tier], "count": 6 + level * 3},
                                {"name": heat_isolators[tier], "count": 6},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Furnace":
                recipe = {
                    "name": tier_material[tier] + machine["name"],
                    "input": {
                        "items": [
                            {
                                "name": tier_material[tier] + "Plate"
                                if tier > 0
                                else "StoneSurface",
                                "count": 4,
                            }
                        ]
                    },
                    "output": {
                        "items": [
                            {"name": tier_material[tier] + machine["name"], "count": 1}
                        ]
                    },
                    "tier": tier,
                    "ticks": 20,
                }
                if tier > 0:
                    recipe["input"]["items"].append(
                        {"name": "StoneFurnace", "count": 1}
                    )
                append_recipe(recipe)

            if machine["name"] == "DrillingRig":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Plate",
                                    "count": 4 + level,
                                },
                                {
                                    "name": tier_material[tier] + "Pipe",
                                    "count": 1 + level,
                                },
                                {
                                    "name": tier_material[tier] + "RobotArm",
                                    "count": 1 + level,
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "FluidFurnace":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Furnace", "count": 1},
                                {
                                    "name": tier_material[tier] + "Pipe",
                                    "count": 2 + parts_ramp(level),
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Separator":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Pipe", "count": 2},
                                {"name": tier_material[tier] + "Plate", "count": 9},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 4 + parts_ramp(level),
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "IndustrialSeparator":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Pipe", "count": 6},
                                {"name": tier_material[tier] + "Plate", "count": 6},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 10 + parts_ramp(level) * 2,
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Assembler":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "RobotArm", "count": 4},
                                {"name": tier_material[tier] + "Plate", "count": 3},
                                {"name": circuits[tier], "count": 3 + level},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Pumpjack":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 5},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 5 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Pipe", "count": 5},
                                {"name": circuits[tier], "count": 3},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Flywheel":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 1},
                                {"name": tier_material[tier] + "Parts", "count": 4},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Deconstructor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "FilteringRobotArm",
                                    "count": 4,
                                },
                                {"name": tier_material[tier] + "Plate", "count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 10 + parts_ramp(level, 10),
                                },
                                {"name": circuits[tier], "count": 3 + level},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Constructor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "FilteringRobotArm",
                                    "count": 4,
                                },
                                {"name": tier_material[tier] + "Plate", "count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 10 + parts_ramp(level, 5),
                                },
                                {"name": circuits[tier], "count": 3 + level},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "FissionReactor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": "CopperHeatPipe", "count": 25},
                                {"name": tier_material[tier] + "Plate", "count": 100},
                                {"name": tier_material[tier] + "Parts", "count": 100},
                                {"name": circuits[tier], "count": 20 + 5 * level},
                                {"name": heat_isolators[tier], "count": 100},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 200,
                    }
                )

            if machine["name"] == "FusionReactor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": "CopperHeatPipe", "count": 25},
                                {"name": tier_material[tier] + "Plate", "count": 40},
                                {"name": tier_material[tier] + "Parts", "count": 100},
                                {"name": wires[tier], "count": 100},
                                {"name": circuits[tier], "count": 40 + 10 * level},
                                {"name": heat_isolators[tier], "count": 50},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 300,
                    }
                )

            if machine["name"] == "Portal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": "UltimateCatalyst", "count": 10},
                                {"name": tier_material[tier] + "Plate", "count": 40},
                                {"name": tier_material[tier] + "Parts", "count": 100},
                                {"name": wires[tier], "count": 100},
                                {"name": circuits[tier], "count": 40 + 10 * level},
                                {"name": heat_isolators[tier], "count": 50},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 300,
                    }
                )

            if machine["name"] == "Riteg":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": "PlutoniumCell",
                                    "count": 1,
                                },
                                {
                                    "name": tier_material[tier] + "Plate",
                                    "count": 8,
                                },
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 20 + 5 * level,
                                },
                                {"name": heat_isolators[tier], "count": 10},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 100,
                    }
                )

            if machine["name"] == "RobotArm":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 2 + parts_ramp(level, 3),
                                },
                                {"name": tier_material[tier] + "Plate", "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "FilteringRobotArm":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": circuits[tier], "count": 1},
                                {"name": tier_material[tier] + "RobotArm", "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "FilteringPump":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": circuits[tier], "count": 1},
                                {"name": tier_material[tier] + "Pump", "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Pump":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "RobotArm", "count": 1},
                                {"name": tier_material[tier] + "Pipe", "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "CuttingMachine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 1 + parts_ramp(level),
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "OreWasher":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 7},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 10 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Pipe", "count": 2},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Pipe":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 1}
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Vent":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Pipe", "count": 1},
                                {"name": tier_material[tier] + "Parts", "count": 2},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Computer":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 2},
                                {"name": "Glass", "count": 1},
                                {"name": circuits[tier], "count": 5},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "QuantumComputer":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Computer", "count": 20},
                                {"name": cables[tier], "count": 50},
                                {"name": circuits[tier], "count": 20},
                                {"name": tier_material[tier] + "Plate", "count": 20},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Conveyor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Plate",
                                    "count": 1,
                                },
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 1 + parts_ramp(level, 2),
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Splitter":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Conveyor",
                                    "count": 4,
                                },
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 5 + parts_ramp(level, 5),
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Sorter":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Splitter",
                                    "count": 1,
                                },
                                {
                                    "name": circuits[tier],
                                    "count": 6,
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "FluidDump":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 10},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 2 + parts_ramp(level),
                                },
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "ArcSmelter":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": heat_isolators[tier], "count": 6},
                                {"name": tier_material[tier] + "Parts", "count": 4},
                                {"name": wires[tier], "count": 5 + level * 5},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Connector":
                append_recipe(
                    {
                        "name": "CopperConnector",
                        "input": {"items": [{"name": "CopperIngot", "count": 1}]},
                        "output": {"items": [{"name": "CopperConnector", "count": 1}]},
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "ElectricEngine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": wires[tier], "count": 5 + level * 3},
                                {"name": tier_material[tier] + "Pipe", "count": 2},
                                {"name": tier_material[tier] + "Parts", "count": 2},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "IndustrialElectricEngine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": wires[tier], "count": 50},
                                {"name": tier_material[tier] + "Plate", "count": 30},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 20 + level * 5,
                                },
                                {"name": circuits[tier], "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 100,
                    }
                )

            if machine["name"] == "BatteryBox":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": cables[tier], "count": 2},
                                {"name": tier_material[tier] + "Plate", "count": 2},
                                {"name": circuits[tier], "count": 1},
                                {"name": "Battery", "count": 5 * level + 10},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "SmallBattery":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": cables[tier], "count": 2},
                                {"name": tier_material[tier] + "Plate", "count": 2},
                                {"name": "AluminiumParts", "count": 5 * level + 10},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "Diode":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": cables[tier], "count": 2},
                                {
                                    "name": "Silicon",
                                    "count": parts_ramp(level, 3),
                                },
                                {"name": tier_material[tier] + "Plate", "count": 1},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "SteamTurbine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 8},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 4 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Pipe", "count": 4},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "IndustrialSteamTurbine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 50},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 50 + level * 10,
                                },
                                {"name": tier_material[tier] + "Pipe", "count": 10},
                                {"name": circuits[tier], "count": 5},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "GasTurbine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 8},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "count": 8 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Pipe", "count": 4},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "HeatExchanger":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": tier_material[tier] + "Plate", "count": 3},
                                {"name": "CopperPipe", "count": 10},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "AutomaticFarm":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": "DirtSurface", "count": 4},
                                {"name": tier_material[tier] + "RobotArm", "count": 2},
                                {"name": tier_material[tier] + "Plate", "count": 6},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if machine["name"] == "ItemRack":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {"name": "Plank", "count": 8},
                                {"name": tier_material[tier] + "Parts", "count": 8},
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

            if "craftable" not in machine and not has_hand_recipe(
                recipes_hand, tier_material[tier] + machine["name"]
            ):
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "input": {
                            "items": [
                                {
                                    "name": tier_material[tier] + "Plate",
                                    "count": 4,
                                }
                            ]
                        },
                        "output": {
                            "items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "count": 1,
                                }
                            ]
                        },
                        "tier": tier,
                        "ticks": 20,
                    }
                )

data = {"Objects": objects_array}

write_file("Generated/Mixed/machines.json", data)

objects_array = []

objects_array.append(
    {"class": ico_generator, "name": "Macerator" + ico_generator, "mul": images}
)

data = {"Objects": objects_array}

write_file("Generated/Resources/machines.json", data)

objects_array = []

objects_array.append(
    {"class": recipe_dictionary, "name": "Hand", "recipes": recipes_hand}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Deconstructor",
        "recipes": recipes_deconstructor,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Constructor", "recipes": recipes_constructor}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Multitool", "recipes": recipes_wrench}
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/machines.json", data)

data = {"Objects": researches}

write_file("Generated/Researches/machines.json", data)

data = {"Objects": objects_wiki_array}

write_file("Generated/Wiki/machines_wiki.json", data)

write_file("Loc/source/machines.json", cvs)
write_file("Loc/source/description_machines.json", desc_csv)
