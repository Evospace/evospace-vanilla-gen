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
    for item in recipe["Input"]["Items"]:
        item_count = item_count + item["Count"]

    con_recipe = copy.deepcopy(recipe)
    con_recipe["Ticks"] = max(min(item_count * 10, 1200), 20)
    con_recipe["ResourceInput"] = {"name": "Electricity", "Count": 20}
    recipes_constructor.append(con_recipe)

    dec_recipe = copy.deepcopy(recipe)

    recipes_hand.append(recipe)

    output = copy.deepcopy(dec_recipe["Input"])

    dec_recipe["Input"] = copy.deepcopy(dec_recipe["Output"])
    dec_recipe["Ticks"] = max(min(item_count * 10, 1200), 20)
    dec_recipe["ResourceInput"] = {"name": "Electricity", "Count": 20}
    dec_recipe["Output"] = copy.deepcopy(output)
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
                "item_logic": building_single_logic,
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

            if "Craftable" in machine:
                item["Craftable"] = False

            # wiki json generation ------------------------------------------------
            objects_array.append(item)

            wiki_item = {}
            wiki_item["description_parts"] = item["description_parts"]
            wiki_item["Level"] = level

            objects_wiki_array[tier_material[tier] + machine["name"]] = wiki_item

            # wiki json generation

            images.append(
                {
                    "NewName": "T_" + tier_material[tier] + image,
                    "Base": "T_" + image,
                    "MulMask": "T_" + named_material(tier_material[tier])["name"],
                    "AddMask": "T_" + image + additive_ico,
                }
            )

            logic = {
                "Recipes": machine["Recipes"]
                if "Recipes" in machine
                else machine["name"],
                "Tier": tier,
                "Level": level,
            }

            if "CustomData" in machine:
                dict = copy.deepcopy(machine["CustomData"])
                for key, value in dict.items():
                    if str(value).find("%Material%") != -1:
                        dict[key] = value.replace("%Material%", tier_material[tier])
                    if key == "StorageCapacity":
                        dict[key] = value * 2**level

                logic.update(dict)

            if "BlockCreation" in machine:
                logic["BlockCreation"] = machine["BlockCreation"]
                if logic["BlockCreation"].find("%Material%") != -1:
                    logic["BlockCreation"] = logic["BlockCreation"].replace(
                        "%Material%", tier_material[tier]
                    )

                if logic["BlockCreation"].find("%Level%") != -1:
                    logic["BlockCreation"] = logic["BlockCreation"].replace(
                        "%Level%", str(tier - machine["StartTier"])
                    )

                if logic["BlockCreation"].find("%Tier%") != -1:
                    logic["BlockCreation"] = logic["BlockCreation"].replace(
                        "%Tier%", str(tier)
                    )

            logic["ActorCreation"] = ""

            block = {
                "name": block_name,
                "Item": item_name,
                "logic_json": logic,
                "class": static_block,
                "BlockLogic": machine["name"],
                "replace_tag": machine["name"],
            }

            if "BlockLogic" in machine:
                block["BlockLogic"] = machine["BlockLogic"]

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
                        "Ticks": 20,
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
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
                        {"Item": tier_material[tier] + machine["name"], "Tier": tier}
                    ],
                }
            )

            if machine["name"] == "Beam":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 3}
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Beam", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Corner":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 1}
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Corner", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Sign":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Plate"
                                    if tier != 0
                                    else "StoneSurface",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Sign", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "AdvancedSign":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Sign", "Count": 1},
                                {"name": electric_isolators[tier], "Count": 1},
                                {"name": circuits[tier], "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "AdvancedSign",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "LogicWire":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": wires[tier], "Count": 2},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "LogicWire", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
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
                        "Input": {
                            "Items": [
                                {"name": "SteelPlate", "Count": 2},
                                {"name": circuits[tier], "Count": 1},
                                {"name": "SteelLogicWire", "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Scaffold":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Parts", "Count": 4}
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Scaffold", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Container":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 3}
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Container", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "IndustrialSmelter":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": wires[tier], "Count": 32 + level * 16},
                                {"name": tier_material[tier] + "Parts", "Count": 12},
                                {"name": heat_isolators[tier], "Count": 12},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "IndustrialSmelter",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "PyrolysisUnit":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 5},
                                {
                                    "name": tier_material[tier] + "Pipe",
                                    "Count": 5 + parts_ramp(level, 5),
                                },
                                {"name": tier_material[tier] + "Container", "Count": 3},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "PyrolysisUnit",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Smelter":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Plate"
                                    if tier > 0
                                    else "StoneSurface",
                                    "Count": 4,
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Smelter", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "InductionCoil":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 3},
                                {"name": "CopperPipe", "Count": 15 + 15 * level},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "InductionCoil",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "PneumaticInput":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 3},
                                {"name": tier_material[tier] + "Parts", "Count": 1},
                                {"name": "Glass", "Count": 1},
                                {"name": "BrassDetails", "Count": 1},
                                {"name": "BrassReductor", "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "PneumaticInput",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Electrolyzer":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 3},
                                {"name": "Coal", "Count": 2},
                                {"name": cables[tier], "Count": 2},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Electrolyzer",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "ChemReactor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 3},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 4 + parts_ramp(level),
                                },
                                {
                                    "name": tier_material[tier] + "ElectricEngine",
                                    "Count": 1,
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "ChemReactor",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Mixer":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 6},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 6 + parts_ramp(level),
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Mixer", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Press":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 1 + parts_ramp(level),
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Press", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "ElectricalSwitch":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 1},
                                {"name": tier_material[tier] + "Parts", "Count": 1},
                                {"name": cables[tier], "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "ElectricalSwitch",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Tank":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 12}
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Tank", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Terminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 3},
                                {"name": cables[tier], "Count": 4},
                                {"name": "Glass", "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {"name": tier_material[tier] + "Terminal", "Count": 1}
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "FlatTerminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Terminal", "Count": 1}
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "FlatTerminal",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "BigTerminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 6},
                                {"name": cables[tier], "Count": 6},
                                {"name": "Glass", "Count": 4},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "BigTerminal",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "BigFlatTerminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "BigTerminal",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "HugeTerminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 9},
                                {"name": cables[tier], "Count": 8},
                                {"name": "Glass", "Count": 9},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "HugeFlatTerminal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "HugeTerminal",
                                    "Count": 1,
                                }
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "SolarPanel":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 6 + parts_ramp(level),
                                },
                                {
                                    "name": tier_material[tier] + "ElectricEngine",
                                    "Count": 1,
                                },
                                {"name": "Glass", "Count": 3},
                                {"name": "Silicon", "Count": 3},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "StirlingEngine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 2 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Pipe", "Count": 2},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Generator":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": wires[tier], "Count": 12 + level * 6},
                                {"name": tier_material[tier] + "Plate", "Count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 2 + parts_ramp(level),
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "CompactGenerator":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": "CopperIngot", "Count": 2 + parts_ramp(level)},
                                {"name": tier_material[tier] + "Plate", "Count": 1},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 2 + parts_ramp(level),
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "AutomaticHammer":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 1 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Plate", "Count": 4},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Macerator":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 3 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Plate", "Count": 3},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Chest":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Plate"
                                    if tier != 0
                                    else "StoneSurface",
                                    "Count": 5,
                                }
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Boiler":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Pipe",
                                    "Count": 1 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Plate", "Count": 3},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "IndustrialBoiler":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Pipe", "Count": 25},
                                {"name": tier_material[tier] + "Plate", "Count": 30},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 10 + level * 5,
                                },
                                {"name": circuits[tier], "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 100,
                    }
                )

            if machine["name"] == "Oven":
                r = {
                    "name": tier_material[tier] + machine["name"],
                    "Input": {"Items": [{"name": "StoneSurface", "Count": 10}]},
                    "Output": {
                        "Items": [
                            {"name": tier_material[tier] + machine["name"], "Count": 1}
                        ]
                    },
                    "Tier": tier,
                    "Ticks": 20,
                }
                if tier != 0:
                    r["Input"]["Items"].append(
                        {
                            "name": tier_material[tier] + "Pipe",
                            "Count": 6 + parts_ramp(level),
                        }
                    )
                append_recipe(r)

            if machine["name"] == "BlastFurnace":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Pipe",
                                    "Count": 8 + parts_ramp(level),
                                },
                                {"name": "StoneSurface", "Count": 20},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "ElectricFurnace":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 3},
                                {"name": wires[tier], "Count": 6 + level * 3},
                                {"name": heat_isolators[tier], "Count": 6},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Furnace":
                recipe = {
                    "name": tier_material[tier] + machine["name"],
                    "Input": {
                        "Items": [
                            {
                                "name": tier_material[tier] + "Plate"
                                if tier > 0
                                else "StoneSurface",
                                "Count": 4,
                            }
                        ]
                    },
                    "Output": {
                        "Items": [
                            {"name": tier_material[tier] + machine["name"], "Count": 1}
                        ]
                    },
                    "Tier": tier,
                    "Ticks": 20,
                }
                if tier > 0:
                    recipe["Input"]["Items"].append(
                        {"name": "StoneFurnace", "Count": 1}
                    )
                append_recipe(recipe)

            if machine["name"] == "DrillingRig":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Plate",
                                    "Count": 4 + level,
                                },
                                {
                                    "name": tier_material[tier] + "Pipe",
                                    "Count": 1 + level,
                                },
                                {
                                    "name": tier_material[tier] + "RobotArm",
                                    "Count": 1 + level,
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "FluidFurnace":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Furnace", "Count": 1},
                                {
                                    "name": tier_material[tier] + "Pipe",
                                    "Count": 2 + parts_ramp(level),
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Separator":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Pipe", "Count": 2},
                                {"name": tier_material[tier] + "Plate", "Count": 9},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 4 + parts_ramp(level),
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "IndustrialSeparator":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Pipe", "Count": 6},
                                {"name": tier_material[tier] + "Plate", "Count": 6},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 10 + parts_ramp(level) * 2,
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Assembler":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "RobotArm", "Count": 4},
                                {"name": tier_material[tier] + "Plate", "Count": 3},
                                {"name": circuits[tier], "Count": 3 + level},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Pumpjack":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 5},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 5 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Pipe", "Count": 5},
                                {"name": circuits[tier], "Count": 3},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Flywheel":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 1},
                                {"name": tier_material[tier] + "Parts", "Count": 4},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Deconstructor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "FilteringRobotArm",
                                    "Count": 4,
                                },
                                {"name": tier_material[tier] + "Plate", "Count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 10 + parts_ramp(level, 10),
                                },
                                {"name": circuits[tier], "Count": 3 + level},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Constructor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "FilteringRobotArm",
                                    "Count": 4,
                                },
                                {"name": tier_material[tier] + "Plate", "Count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 10 + parts_ramp(level, 5),
                                },
                                {"name": circuits[tier], "Count": 3 + level},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "FissionReactor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": "CopperHeatPipe", "Count": 25},
                                {"name": tier_material[tier] + "Plate", "Count": 100},
                                {"name": tier_material[tier] + "Parts", "Count": 100},
                                {"name": circuits[tier], "Count": 20 + 5 * level},
                                {"name": heat_isolators[tier], "Count": 100},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 200,
                    }
                )

            if machine["name"] == "FusionReactor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": "CopperHeatPipe", "Count": 25},
                                {"name": tier_material[tier] + "Plate", "Count": 40},
                                {"name": tier_material[tier] + "Parts", "Count": 100},
                                {"name": wires[tier], "Count": 100},
                                {"name": circuits[tier], "Count": 40 + 10 * level},
                                {"name": heat_isolators[tier], "Count": 50},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 300,
                    }
                )

            if machine["name"] == "Portal":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": "UltimateCatalyst", "Count": 10},
                                {"name": tier_material[tier] + "Plate", "Count": 40},
                                {"name": tier_material[tier] + "Parts", "Count": 100},
                                {"name": wires[tier], "Count": 100},
                                {"name": circuits[tier], "Count": 40 + 10 * level},
                                {"name": heat_isolators[tier], "Count": 50},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 300,
                    }
                )

            if machine["name"] == "Riteg":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": "PlutoniumCell",
                                    "Count": 1,
                                },
                                {
                                    "name": tier_material[tier] + "Plate",
                                    "Count": 8,
                                },
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 20 + 5 * level,
                                },
                                {"name": heat_isolators[tier], "Count": 10},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 100,
                    }
                )

            if machine["name"] == "RobotArm":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 2 + parts_ramp(level, 3),
                                },
                                {"name": tier_material[tier] + "Plate", "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "FilteringRobotArm":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": circuits[tier], "Count": 1},
                                {"name": tier_material[tier] + "RobotArm", "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "FilteringPump":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": circuits[tier], "Count": 1},
                                {"name": tier_material[tier] + "Pump", "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Pump":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "RobotArm", "Count": 1},
                                {"name": tier_material[tier] + "Pipe", "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "CuttingMachine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 4},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 1 + parts_ramp(level),
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "OreWasher":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 7},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 10 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Pipe", "Count": 2},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Pipe":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 1}
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Vent":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Pipe", "Count": 1},
                                {"name": tier_material[tier] + "Parts", "Count": 2},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Computer":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 2},
                                {"name": "Glass", "Count": 1},
                                {"name": circuits[tier], "Count": 5},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "QuantumComputer":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Computer", "Count": 20},
                                {"name": cables[tier], "Count": 50},
                                {"name": circuits[tier], "Count": 20},
                                {"name": tier_material[tier] + "Plate", "Count": 20},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Conveyor":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Plate",
                                    "Count": 1,
                                },
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 1 + parts_ramp(level, 2),
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Splitter":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Conveyor",
                                    "Count": 4,
                                },
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 5 + parts_ramp(level, 5),
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Sorter":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Splitter",
                                    "Count": 1,
                                },
                                {
                                    "name": circuits[tier],
                                    "Count": 6,
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "FluidDump":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 10},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 2 + parts_ramp(level),
                                },
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "ArcSmelter":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": heat_isolators[tier], "Count": 6},
                                {"name": tier_material[tier] + "Parts", "Count": 4},
                                {"name": wires[tier], "Count": 5 + level * 5},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Connector":
                append_recipe(
                    {
                        "name": "CopperConnector",
                        "Input": {"Items": [{"name": "CopperIngot", "Count": 1}]},
                        "Output": {"Items": [{"name": "CopperConnector", "Count": 1}]},
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "ElectricEngine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": wires[tier], "Count": 5 + level * 3},
                                {"name": tier_material[tier] + "Pipe", "Count": 2},
                                {"name": tier_material[tier] + "Parts", "Count": 2},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "IndustrialElectricEngine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": wires[tier], "Count": 50},
                                {"name": tier_material[tier] + "Plate", "Count": 30},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 20 + level * 5,
                                },
                                {"name": circuits[tier], "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 100,
                    }
                )

            if machine["name"] == "BatteryBox":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": cables[tier], "Count": 2},
                                {"name": tier_material[tier] + "Plate", "Count": 2},
                                {"name": circuits[tier], "Count": 1},
                                {"name": "Battery", "Count": 5 * level + 10},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "SmallBattery":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": cables[tier], "Count": 2},
                                {"name": tier_material[tier] + "Plate", "Count": 2},
                                {"name": "AluminiumParts", "Count": 5 * level + 10},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "Diode":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": cables[tier], "Count": 2},
                                {
                                    "name": "Silicon",
                                    "Count": parts_ramp(level, 3),
                                },
                                {"name": tier_material[tier] + "Plate", "Count": 1},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "SteamTurbine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 8},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 4 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Pipe", "Count": 4},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "IndustrialSteamTurbine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 50},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 50 + level * 10,
                                },
                                {"name": tier_material[tier] + "Pipe", "Count": 10},
                                {"name": circuits[tier], "Count": 5},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "GasTurbine":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 8},
                                {
                                    "name": tier_material[tier] + "Parts",
                                    "Count": 8 + parts_ramp(level),
                                },
                                {"name": tier_material[tier] + "Pipe", "Count": 4},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "HeatExchanger":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": tier_material[tier] + "Plate", "Count": 3},
                                {"name": "CopperPipe", "Count": 10},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "AutomaticFarm":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": "DirtSurface", "Count": 4},
                                {"name": tier_material[tier] + "RobotArm", "Count": 2},
                                {"name": tier_material[tier] + "Plate", "Count": 6},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if machine["name"] == "ItemRack":
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {"name": "Plank", "Count": 8},
                                {"name": tier_material[tier] + "Parts", "Count": 8},
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

            if "Craftable" not in machine and not has_hand_recipe(
                recipes_hand, tier_material[tier] + machine["name"]
            ):
                append_recipe(
                    {
                        "name": tier_material[tier] + machine["name"],
                        "Input": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + "Plate",
                                    "Count": 4,
                                }
                            ]
                        },
                        "Output": {
                            "Items": [
                                {
                                    "name": tier_material[tier] + machine["name"],
                                    "Count": 1,
                                }
                            ]
                        },
                        "Tier": tier,
                        "Ticks": 20,
                    }
                )

data = {"Objects": objects_array}

write_file("Generated/Mixed/machines.json", data)

objects_array = []

objects_array.append(
    {"class": ico_generator, "name": "Macerator" + ico_generator, "Images": images}
)

data = {"Objects": objects_array}

write_file("Generated/Resources/machines.json", data)

objects_array = []

objects_array.append(
    {"class": recipe_dictionary, "name": "Hand", "Recipes": recipes_hand}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Deconstructor",
        "Recipes": recipes_deconstructor,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Constructor", "Recipes": recipes_constructor}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Multitool", "Recipes": recipes_wrench}
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/machines.json", data)

data = {"Objects": researches}

write_file("Generated/Researches/machines.json", data)

data = {"Objects": objects_wiki_array}

write_file("Generated/Wiki/machines_wiki.json", data)

write_file("Loc/source/machines.json", cvs)
write_file("Loc/source/description_machines.json", desc_csv)
