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
                "Input": {
                    "Items": [
                        {"name": ore_type["name"] + "Ore", "Count": 1},
                    ]
                },
                "ResourceInput": {"name": "Kinetic", "Count": 8 * ore_type["Hardness"]},
                "Output": {
                    "Items": [
                        {"name": ore_type["name"] + "ImpureOreGravel", "Count": 1},
                        {
                            "name": ore_type["name"] + "ImpureOreGravel",
                            "Count": 1,
                            "split": 2,
                        },
                    ]
                },
                "Tier": tier,
                "Ticks": 150 * ore_type["Hardness"],
            }
        )

        if "SmeltLevel" in named_mat and named_mat["SmeltLevel"] <= 0:
            recipes_smelt.append(
                {
                    "name": ore_type["name"] + "Ore",
                    "Input": {
                        "Items": [
                            {"name": ore_type["name"] + "Ore", "Count": 1},
                        ]
                    },
                    "ResourceInput": {"name": "Heat", "Count": 10},
                    "Output": {
                        "Items": [{"name": ore_type["name"] + "Ingot", "Count": 1}]
                    },
                    "Tier": extract_tier(ore_type) - 1,
                    "Ticks": 400,
                }
            )

        out_items = []
        out_items.append({"name": ore_type["name"] + "OreDust", "Count": 1})
        out_items.append(
            {
                "name": ore_type["name"] + "OreDust",
                "Count": 1,
                "split": 2,
            }
        )
        recipes_mac.append(
            {
                "name": ore_type["name"] + "ImpureOreGravel",
                "Input": {
                    "Items": [
                        {"name": ore_type["name"] + "ImpureOreGravel", "Count": 1},
                    ]
                },
                "ResourceInput": {"name": "Kinetic", "Count": 10},
                "Output": {"Items": out_items},
                "Tier": extract_tier(ore_type),
                "Ticks": 200,
            }
        )

        recipes_mac.append(
            {
                "name": ore_type["name"] + "OreGravel",
                "Input": {
                    "Items": [
                        {"name": ore_type["name"] + "OreGravel", "Count": 1},
                    ]
                },
                "ResourceInput": {"name": "Kinetic", "Count": 10},
                "Output": {
                    "Items": [
                        {"name": ore_type["name"] + "OreDust", "Count": 1},
                        {"name": ore_type["name"] + "OreDust", "Count": 1, "split": 2},
                    ]
                },
                "Tier": extract_tier(ore_type),
                "Ticks": 200,
            }
        )

        if "SmeltLevel" in named_mat and named_mat["SmeltLevel"] <= 0:
            recipes_smelt.append(
                {
                    "name": ore_type["name"] + "OreDust",
                    "Input": {
                        "Items": [
                            {"name": ore_type["name"] + "OreDust", "Count": 1},
                        ]
                    },
                    "ResourceInput": {"name": "Heat", "Count": 10},
                    "Output": {
                        "Items": [{"name": ore_type["name"] + "Ingot", "Count": 1}]
                    },
                    "Ticks": 200,
                    "Tier": extract_tier(ore_type),
                }
            )
            recipes_smelt.append(
                {
                    "name": ore_type["name"] + "ImpureOreGravel",
                    "Input": {
                        "Items": [
                            {"name": ore_type["name"] + "ImpureOreGravel", "Count": 1},
                        ]
                    },
                    "ResourceInput": {"name": "Heat", "Count": 10},
                    "Output": {
                        "Items": [{"name": ore_type["name"] + "Ingot", "Count": 1}]
                    },
                    "Ticks": 300,
                    "Tier": extract_tier(ore_type),
                }
            )
            recipes_smelt.append(
                {
                    "name": ore_type["name"] + "OreGravel",
                    "Input": {
                        "Items": [
                            {"name": ore_type["name"] + "OreGravel", "Count": 1},
                        ]
                    },
                    "ResourceInput": {"name": "Heat", "Count": 10},
                    "Output": {
                        "Items": [{"name": ore_type["name"] + "Ingot", "Count": 1}]
                    },
                    "Ticks": 300,
                    "Tier": extract_tier(ore_type),
                }
            )

        out_items = []
        out_items.append({"name": ore_type["name"] + "OreGravel", "Count": 1})
        if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
            oi = {
                "name": ore_type["Byproducts"][0],
                "Count": 1,
                "split": 10,
            }

            if "ByproductChanse" in ore_type:
                oi["split"] = ore_type["ByproductChanse"][0]

            out_items.append(oi)

        out_items.append(
            {
                "name": "OreWater",
                "Count": 50,
                "Capacity": 32000,
            }
        )
        recipes_ore_washer.append(
            {
                "name": ore_type["name"] + "ImpureOreGravel",
                "Input": {
                    "Items": [
                        {"name": ore_type["name"] + "ImpureOreGravel", "Count": 1},
                        {"name": "Water", "Count": 250},
                    ]
                },
                "ResourceInput": {"name": "Kinetic", "Count": 10},
                "Output": {"Items": out_items},
                "Tier": extract_tier(ore_type),
                "Ticks": 130,
            }
        )

        out_items = []
        out_items.append(
            {
                "name": (ore_type["name"] + "Dust")
                if "Oxide" not in ore_type
                else (ore_type["name"] + "OxideDust"),
                "Count": 1,
            }
        )
        if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
            oi = {
                "name": ore_type["Byproducts"][0],
                "Count": 1,
                "split": 10,
            }
            if "ByproductChanse" in ore_type:
                oi["split"] = ore_type["ByproductChanse"][0]

            out_items.append(oi)

        recipes_sep2.append(
            {
                "name": ore_type["name"] + "OreDust",
                "Input": {
                    "Items": [
                        {"name": ore_type["name"] + "OreDust", "Count": 1},
                    ]
                },
                "ResourceInput": {"name": "Kinetic", "Count": 50 * 4},
                "Output": {"Items": out_items},
                "Ticks": 200,
                "Tier": extract_tier(ore_type),
            }
        )

        out_items = []
        if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
            oi = {
                "name": (ore_type["name"] + "Dust")
                if "Oxide" not in ore_type
                else (ore_type["name"] + "OxideDust"),
                "Count": 1,
            }

            if "ByproductChanse" in ore_type:
                oi["split"] = ore_type["ByproductChanse"][0]

            out_items.append(oi)

        recipes_sep.append(
            {
                "name": ore_type["name"] + "OreDust",
                "Input": {
                    "Items": [
                        {"name": ore_type["name"] + "OreDust", "Count": 1},
                    ]
                },
                "ResourceInput": {"name": "Kinetic", "Count": 20},
                "Output": {"Items": out_items},
                "Ticks": 100,
                "Tier": extract_tier(ore_type),
            }
        )

        for i in {"OreGravel", "ImpureOreGravel"}:
            recipes_sifter.append(
                {
                    "name": ore_type["name"] + i,
                    "Input": {
                        "Items": [
                            {"name": ore_type["name"] + i, "Count": 1},
                        ]
                    },
                    "ResourceInput": {"name": "Kinetic", "Count": 200},
                    "Output": {
                        "Items": [
                            {
                                "name": ore_type["Byproducts"][1][0],
                                "Count": 1,
                                "split": 2,
                            },
                            {
                                "name": ore_type["Byproducts"][1][1],
                                "Count": 1,
                                "split": 5,
                            },
                            {
                                "name": ore_type["Byproducts"][1][2],
                                "Count": 1,
                                "split": 40,
                            },
                        ]
                    },
                    "Ticks": 40,
                    "Tier": extract_tier(ore_type),
                }
            )

        # out_items = []
        # out_items.append({
        # 	"name": (ore_type["name"] + "Dust") if "Oxide" not in ore_type else (ore_type["name"] + "OxideDust"),
        # 	"Count": 8
        # })
        # if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
        # 	for byp in ore_type["Byproducts"]:
        # 		out_items.append({
        # 			"name": byp + "Dust",
        # 			"Count": 1,
        # 		})
        # recipes_sep2.append({
        # 	"name": ore_type["name"] + "ImpureOreDustSeparating",
        # 	"Input":{
        # 		"Items":[
        # 			{
        # 				"name": ore_type["name"] + "OreDust",
        # 				"Count": 7
        # 			},
        # 		]
        # 	},
        # 	"ResourceInput":{
        # 		"name": "Kinetic",
        # 		"Count": 3000 * 8
        # 	},
        # 	"Output":{
        # 		"Items": out_items
        # 	},
        # 	"Ticks" : 200 * 8,
        # 	"Tier": extract_tier(ore_type),
        # })

objects_array.append(
    {"class": recipe_dictionary, "name": "Macerator", "Recipes": recipes_mac}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Smelter", "Recipes": recipes_smelt}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "OreWasher", "Recipes": recipes_ore_washer}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Separator", "Recipes": recipes_sep}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "IndustrialSeparator", "Recipes": recipes_sep2}
)


objects_array.append(
    {"class": recipe_dictionary, "name": "AutomaticHammer", "Recipes": recipes_hammer}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "ArcSmelter", "Recipes": recipes_arc}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Sifter", "Recipes": recipes_sifter}
)

recipes_break = []

for ore_type in ore_types:
    recipes_break.append(
        {
            "name": ore_type["name"] + "OreBreaking",
            "Ticks": ore_type["Hardness"] * 20,
            "Input": {"Items": [{"name": ore_type["name"] + "Ore", "Count": 1}]},
            "Output": {"Items": [{"name": ore_type["Drops"], "Count": 1}]},
        }
    )

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Multitool",
        "Recipes": recipes_break,
        "UsedIn": [{"Item": "Multitool", "Tier": 0}],
        "Ticks": 20,
    }
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/ores.json", data)
