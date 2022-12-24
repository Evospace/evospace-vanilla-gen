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
        named_mat = named_material(ore_type["Name"])

        tier = extract_tier(ore_type)

        recipes_hammer.append(
            {
                "Name": ore_type["Name"] + "Ore",
                "Input": {
                    "Items": [
                        {"Name": ore_type["Name"] + "Ore", "Count": 1},
                    ]
                },
                "ResourceInput": {"Name": "Kinetic", "Count": 8 * ore_type["Hardness"]},
                "Output": {
                    "Items": [
                        {"Name": ore_type["Name"] + "ImpureOreGravel", "Count": 1},
                        {
                            "Name": ore_type["Name"] + "ImpureOreGravel",
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
                    "Name": ore_type["Name"] + "Ore",
                    "Input": {
                        "Items": [
                            {"Name": ore_type["Name"] + "Ore", "Count": 1},
                        ]
                    },
                    "ResourceInput": {"Name": "Heat", "Count": 10},
                    "Output": {
                        "Items": [{"Name": ore_type["Name"] + "Ingot", "Count": 1}]
                    },
                    "Tier": extract_tier(ore_type) - 1,
                    "Ticks": 400,
                }
            )

        out_items = []
        out_items.append({"Name": ore_type["Name"] + "OreDust", "Count": 1})
        out_items.append(
            {
                "Name": ore_type["Name"] + "OreDust",
                "Count": 1,
                "split": 2,
            }
        )
        recipes_mac.append(
            {
                "Name": ore_type["Name"] + "ImpureOreGravel",
                "Input": {
                    "Items": [
                        {"Name": ore_type["Name"] + "ImpureOreGravel", "Count": 1},
                    ]
                },
                "ResourceInput": {"Name": "Kinetic", "Count": 10},
                "Output": {"Items": out_items},
                "Tier": extract_tier(ore_type),
                "Ticks": 200,
            }
        )

        recipes_mac.append(
            {
                "Name": ore_type["Name"] + "OreGravel",
                "Input": {
                    "Items": [
                        {"Name": ore_type["Name"] + "OreGravel", "Count": 1},
                    ]
                },
                "ResourceInput": {"Name": "Kinetic", "Count": 10},
                "Output": {
                    "Items": [
                        {"Name": ore_type["Name"] + "OreDust", "Count": 1},
                        {"Name": ore_type["Name"] + "OreDust", "Count": 1, "split": 2},
                    ]
                },
                "Tier": extract_tier(ore_type),
                "Ticks": 200,
            }
        )

        if "SmeltLevel" in named_mat and named_mat["SmeltLevel"] <= 0:
            recipes_smelt.append(
                {
                    "Name": ore_type["Name"] + "OreDust",
                    "Input": {
                        "Items": [
                            {"Name": ore_type["Name"] + "OreDust", "Count": 1},
                        ]
                    },
                    "ResourceInput": {"Name": "Heat", "Count": 10},
                    "Output": {
                        "Items": [{"Name": ore_type["Name"] + "Ingot", "Count": 1}]
                    },
                    "Ticks": 200,
                    "Tier": extract_tier(ore_type),
                }
            )
            recipes_smelt.append(
                {
                    "Name": ore_type["Name"] + "ImpureOreGravel",
                    "Input": {
                        "Items": [
                            {"Name": ore_type["Name"] + "ImpureOreGravel", "Count": 1},
                        ]
                    },
                    "ResourceInput": {"Name": "Heat", "Count": 10},
                    "Output": {
                        "Items": [{"Name": ore_type["Name"] + "Ingot", "Count": 1}]
                    },
                    "Ticks": 300,
                    "Tier": extract_tier(ore_type),
                }
            )
            recipes_smelt.append(
                {
                    "Name": ore_type["Name"] + "OreGravel",
                    "Input": {
                        "Items": [
                            {"Name": ore_type["Name"] + "OreGravel", "Count": 1},
                        ]
                    },
                    "ResourceInput": {"Name": "Heat", "Count": 10},
                    "Output": {
                        "Items": [{"Name": ore_type["Name"] + "Ingot", "Count": 1}]
                    },
                    "Ticks": 300,
                    "Tier": extract_tier(ore_type),
                }
            )

        out_items = []
        out_items.append({"Name": ore_type["Name"] + "OreGravel", "Count": 1})
        if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
            oi = {
                "Name": ore_type["Byproducts"][0],
                "Count": 1,
                "split": 10,
            }

            if "ByproductChanse" in ore_type:
                oi["split"] = ore_type["ByproductChanse"][0]

            out_items.append(oi)

        out_items.append(
            {
                "Name": "OreWater",
                "Count": 50,
                "Capacity": 32000,
            }
        )
        recipes_ore_washer.append(
            {
                "Name": ore_type["Name"] + "ImpureOreGravel",
                "Input": {
                    "Items": [
                        {"Name": ore_type["Name"] + "ImpureOreGravel", "Count": 1},
                        {"Name": "Water", "Count": 250},
                    ]
                },
                "ResourceInput": {"Name": "Kinetic", "Count": 10},
                "Output": {"Items": out_items},
                "Tier": extract_tier(ore_type),
                "Ticks": 130,
            }
        )

        out_items = []
        out_items.append(
            {
                "Name": (ore_type["Name"] + "Dust")
                if "Oxide" not in ore_type
                else (ore_type["Name"] + "OxideDust"),
                "Count": 1,
            }
        )
        if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
            oi = {
                "Name": ore_type["Byproducts"][0],
                "Count": 1,
                "split": 10,
            }
            if "ByproductChanse" in ore_type:
                oi["split"] = ore_type["ByproductChanse"][0]

            out_items.append(oi)

        recipes_sep2.append(
            {
                "Name": ore_type["Name"] + "OreDust",
                "Input": {
                    "Items": [
                        {"Name": ore_type["Name"] + "OreDust", "Count": 1},
                    ]
                },
                "ResourceInput": {"Name": "Kinetic", "Count": 50 * 4},
                "Output": {"Items": out_items},
                "Ticks": 200,
                "Tier": extract_tier(ore_type),
            }
        )

        out_items = []
        if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
            oi = {
                "Name": (ore_type["Name"] + "Dust")
                if "Oxide" not in ore_type
                else (ore_type["Name"] + "OxideDust"),
                "Count": 1,
            }

            if "ByproductChanse" in ore_type:
                oi["split"] = ore_type["ByproductChanse"][0]

            out_items.append(oi)

        recipes_sep.append(
            {
                "Name": ore_type["Name"] + "OreDust",
                "Input": {
                    "Items": [
                        {"Name": ore_type["Name"] + "OreDust", "Count": 1},
                    ]
                },
                "ResourceInput": {"Name": "Kinetic", "Count": 20},
                "Output": {"Items": out_items},
                "Ticks": 100,
                "Tier": extract_tier(ore_type),
            }
        )

        for i in {"OreGravel", "ImpureOreGravel"}:
            recipes_sifter.append(
                {
                    "Name": ore_type["Name"] + i,
                    "Input": {
                        "Items": [
                            {"Name": ore_type["Name"] + i, "Count": 1},
                        ]
                    },
                    "ResourceInput": {"Name": "Kinetic", "Count": 200},
                    "Output": {
                        "Items": [
                            {
                                "Name": ore_type["Byproducts"][1][0],
                                "Count": 1,
                                "split": 2,
                            },
                            {
                                "Name": ore_type["Byproducts"][1][1],
                                "Count": 1,
                                "split": 5,
                            },
                            {
                                "Name": ore_type["Byproducts"][1][2],
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
        # 	"Name": (ore_type["Name"] + "Dust") if "Oxide" not in ore_type else (ore_type["Name"] + "OxideDust"),
        # 	"Count": 8
        # })
        # if "Byproducts" in ore_type and len(ore_type["Byproducts"]) > 0:
        # 	for byp in ore_type["Byproducts"]:
        # 		out_items.append({
        # 			"Name": byp + "Dust",
        # 			"Count": 1,
        # 		})
        # recipes_sep2.append({
        # 	"Name": ore_type["Name"] + "ImpureOreDustSeparating",
        # 	"Input":{
        # 		"Items":[
        # 			{
        # 				"Name": ore_type["Name"] + "OreDust",
        # 				"Count": 7
        # 			},
        # 		]
        # 	},
        # 	"ResourceInput":{
        # 		"Name": "Kinetic",
        # 		"Count": 3000 * 8
        # 	},
        # 	"Output":{
        # 		"Items": out_items
        # 	},
        # 	"Ticks" : 200 * 8,
        # 	"Tier": extract_tier(ore_type),
        # })

objects_array.append(
    {"Class": recipe_dictionary, "Name": "Macerator", "Recipes": recipes_mac}
)

objects_array.append(
    {"Class": recipe_dictionary, "Name": "Smelter", "Recipes": recipes_smelt}
)

objects_array.append(
    {"Class": recipe_dictionary, "Name": "OreWasher", "Recipes": recipes_ore_washer}
)

objects_array.append(
    {"Class": recipe_dictionary, "Name": "Separator", "Recipes": recipes_sep}
)

objects_array.append(
    {"Class": recipe_dictionary, "Name": "IndustrialSeparator", "Recipes": recipes_sep2}
)


objects_array.append(
    {"Class": recipe_dictionary, "Name": "AutomaticHammer", "Recipes": recipes_hammer}
)

objects_array.append(
    {"Class": recipe_dictionary, "Name": "ArcSmelter", "Recipes": recipes_arc}
)

objects_array.append(
    {"Class": recipe_dictionary, "Name": "Sifter", "Recipes": recipes_sifter}
)

recipes_break = []

for ore_type in ore_types:
    recipes_break.append(
        {
            "Name": ore_type["Name"] + "OreBreaking",
            "Ticks": ore_type["Hardness"] * 20,
            "Input": {"Items": [{"Name": ore_type["Name"] + "Ore", "Count": 1}]},
            "Output": {"Items": [{"Name": ore_type["Drops"], "Count": 1}]},
        }
    )

objects_array.append(
    {
        "Class": recipe_dictionary,
        "Name": "Multitool",
        "Recipes": recipes_break,
        "UsedIn": [{"Item": "Multitool", "Tier": 0}],
        "Ticks": 20,
    }
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/ores.json", data)
