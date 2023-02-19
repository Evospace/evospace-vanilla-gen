from MachinesList import *
from Common import *
from OresGen import *

recipes_mac = []
recipes_smelt = []
recipes_ore_washer = []
recipes_sep = []
recipes_hammer = []
recipes_arc = []

recipes_sep2 = []

recipes_sifter = []

objects_array = []

for ore_type in ore_types:
    if "NotOre" not in ore_type:
        named_mat = named_material(ore_type["name"])

        tier = extract_tier(ore_type)

        recipes_hammer.append(
            {
                "name": ore_type["name"] + "Ore",
                "input": {
                    "items": [
                        {"name": ore_type["name"] + "Ore", "count": 1},
                    ]
                },
                "res_input": {"name": "Kinetic", "count": 8 * ore_type["Hardness"]},
                "output": {
                    "items": [
                        {"name": ore_type["name"] + "ImpureOreGravel", "count": 1},
                        {
                            "name": ore_type["name"] + "ImpureOreGravel",
                            "count": 1,
                            "split": 2,
                        },
                    ]
                },
                "tier": tier,
                "ticks": 150 * ore_type["Hardness"],
            }
        )

        if "SmeltLevel" in named_mat and named_mat["SmeltLevel"] <= 0:
            recipes_smelt.append(
                {
                    "name": ore_type["name"] + "Ore",
                    "input": {
                        "items": [
                            {"name": ore_type["name"] + "Ore", "count": 1},
                        ]
                    },
                    "res_input": {"name": "Heat", "count": 10},
                    "output": {
                        "items": [{"name": ore_type["name"] + "Ingot", "count": 1}]
                    },
                    "tier": extract_tier(ore_type) - 1,
                    "ticks": 400,
                }
            )

        out_items = []
        out_items.append({"name": ore_type["name"] + "OreDust", "count": 1})
        out_items.append(
            {
                "name": ore_type["name"] + "OreDust",
                "count": 1,
                "split": 2,
            }
        )
        recipes_mac.append(
            {
                "name": ore_type["name"] + "ImpureOreGravel",
                "input": {
                    "items": [
                        {"name": ore_type["name"] + "ImpureOreGravel", "count": 1},
                    ]
                },
                "res_input": {"name": "Kinetic", "count": 10},
                "output": {"items": out_items},
                "tier": extract_tier(ore_type),
                "ticks": 200,
            }
        )

        recipes_mac.append(
            {
                "name": ore_type["name"] + "OreGravel",
                "input": {
                    "items": [
                        {"name": ore_type["name"] + "OreGravel", "count": 1},
                    ]
                },
                "res_input": {"name": "Kinetic", "count": 10},
                "output": {
                    "items": [
                        {"name": ore_type["name"] + "OreDust", "count": 1},
                        {"name": ore_type["name"] + "OreDust", "count": 1, "split": 2},
                    ]
                },
                "tier": extract_tier(ore_type),
                "ticks": 200,
            }
        )

        if "SmeltLevel" in named_mat and named_mat["SmeltLevel"] <= 0:
            recipes_smelt.append(
                {
                    "name": ore_type["name"] + "OreDust",
                    "input": {
                        "items": [
                            {"name": ore_type["name"] + "OreDust", "count": 1},
                        ]
                    },
                    "res_input": {"name": "Heat", "count": 10},
                    "output": {
                        "items": [{"name": ore_type["name"] + "Ingot", "count": 1}]
                    },
                    "ticks": 200,
                    "tier": extract_tier(ore_type),
                }
            )
            recipes_smelt.append(
                {
                    "name": ore_type["name"] + "ImpureOreGravel",
                    "input": {
                        "items": [
                            {"name": ore_type["name"] + "ImpureOreGravel", "count": 1},
                        ]
                    },
                    "res_input": {"name": "Heat", "count": 10},
                    "output": {
                        "items": [{"name": ore_type["name"] + "Ingot", "count": 1}]
                    },
                    "ticks": 300,
                    "tier": extract_tier(ore_type),
                }
            )
            recipes_smelt.append(
                {
                    "name": ore_type["name"] + "OreGravel",
                    "input": {
                        "items": [
                            {"name": ore_type["name"] + "OreGravel", "count": 1},
                        ]
                    },
                    "res_input": {"name": "Heat", "count": 10},
                    "output": {
                        "items": [{"name": ore_type["name"] + "Ingot", "count": 1}]
                    },
                    "ticks": 300,
                    "tier": extract_tier(ore_type),
                }
            )

        out_items = []
        out_items.append({"name": ore_type["name"] + "OreGravel", "count": 1})
        if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
            oi = {
                "name": ore_type["Byproducts"][0],
                "count": 1,
                "split": 10,
            }

            if "ByproductChanse" in ore_type:
                oi["split"] = ore_type["ByproductChanse"][0]

            out_items.append(oi)

        out_items.append(
            {
                "name": "OreWater",
                "count": 50,
                "Capacity": 32000,
            }
        )
        recipes_ore_washer.append(
            {
                "name": ore_type["name"] + "ImpureOreGravel",
                "input": {
                    "items": [
                        {"name": ore_type["name"] + "ImpureOreGravel", "count": 1},
                        {"name": "Water", "count": 250},
                    ]
                },
                "res_input": {"name": "Kinetic", "count": 10},
                "output": {"items": out_items},
                "tier": extract_tier(ore_type),
                "ticks": 130,
            }
        )

        out_items = []
        out_items.append(
            {
                "name": (ore_type["name"] + "Dust")
                if "Oxide" not in ore_type
                else (ore_type["name"] + "OxideDust"),
                "count": 1,
            }
        )
        if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
            oi = {
                "name": ore_type["Byproducts"][0],
                "count": 1,
                "split": 10,
            }
            if "ByproductChanse" in ore_type:
                oi["split"] = ore_type["ByproductChanse"][0]

            out_items.append(oi)

        recipes_sep2.append(
            {
                "name": ore_type["name"] + "OreDust",
                "input": {
                    "items": [
                        {"name": ore_type["name"] + "OreDust", "count": 1},
                    ]
                },
                "res_input": {"name": "Kinetic", "count": 50 * 4},
                "output": {"items": out_items},
                "ticks": 200,
                "tier": extract_tier(ore_type),
            }
        )

        out_items = []
        if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
            oi = {
                "name": (ore_type["name"] + "Dust")
                if "Oxide" not in ore_type
                else (ore_type["name"] + "OxideDust"),
                "count": 1,
            }

            if "ByproductChanse" in ore_type:
                oi["split"] = ore_type["ByproductChanse"][0]

            out_items.append(oi)

        recipes_sep.append(
            {
                "name": ore_type["name"] + "OreDust",
                "input": {
                    "items": [
                        {"name": ore_type["name"] + "OreDust", "count": 1},
                    ]
                },
                "res_input": {"name": "Kinetic", "count": 20},
                "output": {"items": out_items},
                "ticks": 100,
                "tier": extract_tier(ore_type),
            }
        )

        for i in {"OreGravel", "ImpureOreGravel"}:
            recipes_sifter.append(
                {
                    "name": ore_type["name"] + i,
                    "input": {
                        "items": [
                            {"name": ore_type["name"] + i, "count": 1},
                        ]
                    },
                    "res_input": {"name": "Kinetic", "count": 200},
                    "output": {
                        "items": [
                            {
                                "name": ore_type["Byproducts"][1][0],
                                "count": 1,
                                "split": 2,
                            },
                            {
                                "name": ore_type["Byproducts"][1][1],
                                "count": 1,
                                "split": 5,
                            },
                            {
                                "name": ore_type["Byproducts"][1][2],
                                "count": 1,
                                "split": 40,
                            },
                        ]
                    },
                    "ticks": 40,
                    "tier": extract_tier(ore_type),
                }
            )

        # out_items = []
        # out_items.append({
        # 	"name": (ore_type["name"] + "Dust") if "Oxide" not in ore_type else (ore_type["name"] + "OxideDust"),
        # 	"count": 8
        # })
        # if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
        # 	for byp in ore_type["Byproducts"]:
        # 		out_items.append({
        # 			"name": byp + "Dust",
        # 			"count": 1,
        # 		})
        # recipes_sep2.append({
        # 	"name": ore_type["name"] + "ImpureOreDustSeparating",
        # 	"input":{
        # 		"items":[
        # 			{
        # 				"name": ore_type["name"] + "OreDust",
        # 				"count": 7
        # 			},
        # 		]
        # 	},
        # 	"res_input":{
        # 		"name": "Kinetic",
        # 		"count": 3000 * 8
        # 	},
        # 	"output":{
        # 		"items": out_items
        # 	},
        # 	"ticks" : 200 * 8,
        # 	"tier": extract_tier(ore_type),
        # })

objects_array.append(
    {"class": recipe_dictionary, "name": "Macerator", "recipes": recipes_mac}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Smelter", "recipes": recipes_smelt}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "OreWasher", "recipes": recipes_ore_washer}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Separator", "recipes": recipes_sep}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "IndustrialSeparator", "recipes": recipes_sep2}
)


objects_array.append(
    {"class": recipe_dictionary, "name": "AutomaticHammer", "recipes": recipes_hammer}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "ArcSmelter", "recipes": recipes_arc}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Sifter", "recipes": recipes_sifter}
)

recipes_break = []

for ore_type in ore_types:
    recipes_break.append(
        {
            "name": ore_type["name"] + "OreBreaking",
            "ticks": ore_type["Hardness"] * 20,
            "input": {"items": [{"name": ore_type["name"] + "Ore", "count": 1}]},
            "output": {"items": [{"name": ore_type["drops"], "count": 1}]},
        }
    )

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Multitool",
        "recipes": recipes_break,
        "UsedIn": [{"Item": "Multitool", "tier": 0}],
        "ticks": 20,
    }
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/ores.json", data)
