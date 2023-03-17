from Common import *

cvs = []

variation_helper = [
    "",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
]

props = [
    {
        "name": "Cactus",
        "scale_min": [0.5, 0.5, 0.5],
        "scale_max": [2, 2, 2],
        "variations": 2,
        "project_to_terrain_power": 1,
        "is_big": True,
        "drops": "Organics",
        "additive_elevation": 0,
        "TimeMul": 1,
    },
    {
        "name": "Dandaleon",
        "scale_min": [2, 2, 2],
        "scale_max": [4, 4, 4],
        "variations": 3,
        "project_to_terrain_power": 1,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
    },
    {
        "name": "Fern",
        "scale_min": [4, 4, 4],
        "scale_max": [6, 6, 6],
        "variations": 3,
        "project_to_terrain_power": 1,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
    },
    {
        "name": "LongGrass",
        "scale_min": [2, 2, 2],
        "scale_max": [4, 4, 4],
        "variations": 1,
        "project_to_terrain_power": 1,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
    },
    {
        "name": "SeaPlant",
        "scale_min": [2, 2, 2],
        "scale_max": [4, 4, 4],
        "variations": 22,
        "project_to_terrain_power": 0,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
        "maximum_height": -1,
    },
    {
        "name": "SeaGrass",
        "scale_min": [2, 2, 2],
        "scale_max": [4, 4, 4],
        "variations": 5,
        "project_to_terrain_power": 0,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
        "maximum_height": -1,
    },
    {
        "name": "TallGrass",
        "scale_min": [1, 1, 1],
        "scale_max": [3, 3, 3],
        "variations": 1,
        "project_to_terrain_power": 1,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
    },
    {
        "name": "Broadleaf",
        "scale_min": [1, 1, 1],
        "scale_max": [3, 3, 3],
        "variations": 3,
        "project_to_terrain_power": 0,
        "is_big": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Noleafes",
        "scale_min": [1, 1, 1],
        "scale_max": [3, 3, 3],
        "variations": 1,
        "project_to_terrain_power": 0,
        "is_big": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Shrub",
        "scale_min": [1.5, 1.5, 1.5],
        "scale_max": [2.5, 2.5, 2.5],
        "variations": 1,
        "project_to_terrain_power": 1,
        "is_big": True,
        "drops": "Log",
        "cull_begin": 10000,
        "cull_end": 12000,
        "TimeMul": 1,
    },
    {
        "name": "Rock",
        "scale_min": [0.6, 0.6, 0.6],
        "scale_max": [3, 3, 3],
        "variations": 2,
        "project_to_terrain_power": 1,
        "is_big": True,
        "drops": "StoneSurface",
        "DropCount": 10,
        "additive_elevation": 0,
        "TimeMul": 1,
    },
    {
        "name": "Pine",
        "scale_min": [0.6, 0.6, 0.6],
        "scale_max": [1.4, 1.4, 1.4],
        "variations": 3,
        "project_to_terrain_power": 0,
        "is_big": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "SnowyPine",
        "scale_min": [0.6, 0.6, 0.6],
        "scale_max": [1.2, 1.2, 1.2],
        "variations": 3,
        "project_to_terrain_power": 0,
        "is_big": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Birch",
        "scale_min": [0.6, 0.6, 0.6],
        "scale_max": [1.4, 1.4, 1.4],
        "variations": 2,
        "project_to_terrain_power": 0,
        "is_big": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Palm",
        "scale_min": [0.6, 0.6, 0.6],
        "scale_max": [1.4, 1.4, 1.4],
        "variations": 2,
        "project_to_terrain_power": 0,
        "is_big": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Rogoz",
        "scale_min": [1, 1, 1],
        "scale_max": [3, 3, 3],
        "variations": 5,
        "project_to_terrain_power": 0,
        "drops": "Organics",
        "cull_begin": 7000,
        "cull_end": 8000,
        "additive_elevation": 0,
    },
    {
        "name": "Lily",
        "scale_min": [1, 1, 1],
        "scale_max": [3, 3, 3],
        "variations": 1,
        "project_to_terrain_power": 0,
        "drops": "Organics",
        "cull_begin": 7000,
        "cull_end": 8000,
        "additive_elevation": 70,
        "floating": True,
    },
    {
        "name": "LilyFlower",
        "scale_min": [1, 1, 1],
        "scale_max": [3, 3, 3],
        "variations": 2,
        "project_to_terrain_power": 0,
        "drops": "Organics",
        "cull_begin": 7000,
        "cull_end": 8000,
        "additive_elevation": 70,
        "floating": True,
    },
    {
        "name": "Shroom",
        "scale_min": [1, 1, 1],
        "scale_max": [2, 2, 2],
        "variations": 6,
        "project_to_terrain_power": 0,
        "drops": "Organics",
        "additive_elevation": 20,
        "cull_begin": 10000,
        "cull_end": 12000,
    },
    {
        "name": "YellowFlower",
        "scale_min": [1, 1, 1],
        "scale_max": [2, 2, 2],
        "variations": 1,
        "project_to_terrain_power": 1,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
    },
    {
        "name": "RedFlower",
        "scale_min": [1, 1, 1],
        "scale_max": [2, 2, 2],
        "variations": 1,
        "project_to_terrain_power": 1,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
    },
    {
        "name": "WhiteFlower",
        "scale_min": [1, 1, 1],
        "scale_max": [2, 2, 2],
        "variations": 1,
        "project_to_terrain_power": 1,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
    },
    {
        "name": "BigBush",
        "scale_min": [1.5, 1.5, 1.5],
        "scale_max": [3, 3, 3],
        "variations": 1,
        "project_to_terrain_power": 1,
        "HandInteraction": True,
        "drops": "Plank",
        "additive_elevation": 0,
        "cull_begin": 10000,
        "cull_end": 12000,
    },
    {
        "name": "SmallRock",
        "scale_min": [1, 1, 1],
        "scale_max": [3, 3, 3],
        "variations": 1,
        "project_to_terrain_power": 1,
        "HandInteraction": True,
        "drops": "StoneSurface",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
    },
    {
        "name": "Diptero",
        "scale_min": [0.8, 0.8, 0.8],
        "scale_max": [1.3, 1.3, 1.3],
        "variations": 2,
        "project_to_terrain_power": 0,
        "HandInteraction": False,
        "additive_elevation": 0,
        "is_big": True,
        "drops": "StoneLog",
        "TimeMul": 6,
    },
    {
        "name": "DryGrass",
        "scale_min": [1, 1, 1],
        "scale_max": [4, 4, 4],
        "variations": 1,
        "project_to_terrain_power": 1,
        "HandInteraction": False,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
    },
    {
        "name": "VolcanicRock",
        "scale_min": [0.5, 0.5, 0.5],
        "scale_max": [1, 1, 1],
        "variations": 4,
        "project_to_terrain_power": 1,
        "HandInteraction": False,
        "drops": "BasaltSurface",
        "DropCount": 10,
        "is_big": True,
        "additive_elevation": 0,
        "TimeMul": 1,
    },
    {
        "name": "SnowyRock",
        "scale_min": [0.5, 0.5, 0.5],
        "scale_max": [1, 1, 1],
        "variations": 4,
        "project_to_terrain_power": 1,
        "HandInteraction": False,
        "drops": "BasaltSurface",
        "DropCount": 10,
        "cull_begin": 10000,
        "cull_end": 12000,
        "is_big": True,
        "additive_elevation": 0,
        "TimeMul": 1,
    },
    {
        "name": "SnowyGrass",
        "scale_min": [2, 2, 2],
        "scale_max": [4, 4, 4],
        "variations": 3,
        "project_to_terrain_power": 1,
        "HandInteraction": False,
        "drops": "Organics",
        "cull_begin": 10000,
        "cull_end": 12000,
        "additive_elevation": 0,
    },
]


def named_prop(name):
    return [x for x in props if x["name"] == name][0]


proplists = [
    {
        "name": "PrairieDryPropList",
        "array": [
            {"props": ["SmallRock"], "chance": 0.01},
            {"props": ["DryGrass"], "chance": 0.5},
            {
                "props": ["Broadleaf", "Broadleaf", "Birch", "BigBush", "Noleafes"],
                "chance": 0.0001,
            },
        ],
    },
    {
        "name": "PrairiePropList",
        "array": [
            {"props": ["SmallRock"], "chance": 0.01},
            {"props": ["DryGrass"], "chance": 0.35},
            {"props": ["LongGrass"], "chance": 0.35},
            {
                "props": ["Broadleaf", "Broadleaf", "Birch", "BigBush", "Noleafes"],
                "chance": 0.0004,
            },
        ],
    },
    {
        "name": "DipteroPropList",
        "array": [
            {"props": ["Diptero"], "chance": 0.001},
            {
                "props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
                "chance": 0.01,
            },
            {"props": ["SmallRock"], "chance": 0.01},
            {"props": ["Fern"], "chance": 0.05},
            {"props": ["LongGrass"], "chance": 0.9},
        ],
    },
    {
        "name": "SmallRocksProps",
        "array": [
            {"props": ["SmallRock"], "chance": 0.06},
            {"props": ["VolcanicRock"], "chance": 0.01},
        ],
    },
    {"name": "SnowProps", "array": [{"props": ["SnowyRock"], "chance": 0.01}]},
    {
        "name": "BushlandProps",
        "array": [
            {"props": ["Shrub", "BigBush"], "chance": 0.05},
            {"props": ["LongGrass"], "chance": 0.5},
            {"props": ["TallGrass"], "chance": 0.1},
        ],
    },
    {
        "name": "GrasslandProps",
        "array": [
            {"props": ["Rock"], "chance": 0.005},
            {"props": ["Dandaleon"], "chance": 0.05},
            {"props": ["LongGrass"], "chance": 0.9},
            {"props": ["TallGrass"], "chance": 0.3},
        ],
    },
    {
        "name": "RedFlowersProps",
        "array": [
            {"props": ["RedFlower"], "chance": 0.5},
            {"props": ["LongGrass"], "chance": 0.9},
            {"attaches": ["Butterfly"], "chance": 0.001},
            {"attaches": ["Flies"], "chance": 0.001},
        ],
    },
    {
        "name": "YellowFlowersProps",
        "array": [
            {"props": ["YellowFlower"], "chance": 0.5},
            {"props": ["LongGrass"], "chance": 0.9},
            {"attaches": ["Butterfly"], "chance": 0.001},
        ],
    },
    {
        "name": "WhiteFlowersProps",
        "array": [
            {"props": ["WhiteFlower"], "chance": 0.5},
            {"props": ["LongGrass"], "chance": 0.9},
            {"attaches": ["Butterfly"], "chance": 0.001},
        ],
    },
    {
        "name": "DenseForestProps",
        "array": [
            {"props": ["Noleafes"], "chance": 0.001},
            {
                "props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
                "chance": 0.02,
            },
            {"props": ["SmallRock"], "chance": 0.01},
            {"props": ["Fern"], "chance": 0.03},
            {"props": ["Dandaleon"], "chance": 0.3},
            {"props": ["LongGrass"], "chance": 0.7},
            {"props": ["Shroom"], "chance": 0.01},
            {"attaches": ["Birds"], "chance": 0.001},
            {"attaches": ["Leafes"], "chance": 0.001},
        ],
    },
    {
        "name": "ForestProps",
        "array": [
            {"props": ["Noleafes"], "chance": 0.001},
            {
                "props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
                "chance": 0.01,
            },
            {"props": ["SmallRock"], "chance": 0.01},
            {"props": ["Fern"], "chance": 0.05},
            {"props": ["Dandaleon"], "chance": 0.5},
            {"props": ["LongGrass"], "chance": 0.9},
            {"props": ["Shroom"], "chance": 0.01},
            {"attaches": ["Birds"], "chance": 0.001},
            {"attaches": ["Leafes"], "chance": 0.001},
            {"attaches": ["Flies"], "chance": 0.002},
        ],
    },
    {
        "name": "DensePineForestProps",
        "array": [
            {"props": ["Rock"], "chance": 0.001},
            {"props": ["SmallRock"], "chance": 0.01},
            {"props": ["Pine"], "chance": 0.02},
            {"props": ["LongGrass"], "chance": 0.03},
            {"props": ["Shroom"], "chance": 0.01},
            {"attaches": ["Birds"], "chance": 0.001},
            {"attaches": ["Flies"], "chance": 0.001},
        ],
    },
    {
        "name": "PineForestProps",
        "array": [
            {"props": ["Rock"], "chance": 0.002},
            {"props": ["SmallRock"], "chance": 0.01},
            {"props": ["Pine"], "chance": 0.01},
            {"props": ["LongGrass"], "chance": 0.07},
            {"props": ["Shroom"], "chance": 0.01},
            {"attaches": ["Birds"], "chance": 0.001},
            {"attaches": ["Bugs"], "chance": 0.001},
            {"attaches": ["Flies"], "chance": 0.001},
        ],
    },
    {"name": "UnimplementedProps", "array": [{"props": ["Rock"], "chance": 0.01}]},
    {
        "name": "DesertProps",
        "array": [
            {"props": ["Cactus"], "chance": 0.01},
            {"props": ["Palm"], "chance": 0.002},
            {"attaches": ["DesertSound"], "chance": 0.002},
        ],
    },
    {
        "name": "IslandProps",
        "array": [
            {"props": ["SmallRock"], "chance": 0.01},
            {"props": ["SeaPlant"], "chance": 0.07},
        ],
    },
    {
        "name": "SeagrassProps",
        "array": [
            {"props": ["SmallRock"], "chance": 0.01},
            {"props": ["SeaGrass"], "chance": 0.15},
        ],
    },
    {"name": "EmptySeaProps", "array": [{"props": ["SmallRock"], "chance": 0.05}]},
    {
        "name": "SwampProps",
        "array": [
            {"props": ["SmallRock"], "chance": 0.01},
            {"props": ["LongGrass"], "chance": 0.7},
            {"props": ["Fern"], "chance": 0.05},
            {"props": ["Rogoz"], "chance": 0.5},
            {"props": ["Lily"], "chance": 0.5},
            {"props": ["LilyFlower"], "chance": 0.05},
            {"attaches": ["SwampSound"], "chance": 0.002},
            {"attaches": ["Firefly", "Flies"], "chance": 0.005},
        ],
    },
    {
        "name": "SwampForestProps",
        "array": [
            {"props": ["LongGrass"], "chance": 0.7},
            {"props": ["Fern"], "chance": 0.05},
            {"props": ["Birch", "BigBush"], "chance": 0.01},
            {"props": ["Shroom"], "chance": 0.01},
            {"attaches": ["Firefly", "Flies"], "chance": 0.005},
        ],
    },
    {
        "name": "OreProps",
        "array": [
            {"props": ["LongGrass"], "chance": 0.07},
            {"props": ["Birch", "BigBush"], "chance": 0.01},
            {"props": ["Shroom"], "chance": 0.01},
        ],
    },
    {
        "name": "SnowGrassProps",
        "array": [
            {"props": ["SnowyGrass"], "chance": 0.2},
            {"props": ["SnowyRock"], "chance": 0.01},
        ],
    },
    {
        "name": "SnowForestProps",
        "array": [
            {"props": ["SnowyGrass"], "chance": 0.2},
            {"props": ["SnowyPine"], "chance": 0.005},
        ],
    },
]

objects_array = []
breaking_hand = []

for prop in props:
    cvs.append([prop["name"], CamelToSpaces(prop["name"])])
    for variation in range(0, prop["variations"]):
        prop_class = static_big_prop if "is_big" in prop else static_prop

        objects_array.append(
            {
                "class": static_item,
                "name": prop["name"] + variation_helper[variation],
                "max_count": 32,
                "image": "T_" + prop["name"],
                "logic_json": {"Block": prop["name"] + variation_helper[variation]},
                "logic": building_prop_logic
                if "is_big" in prop
                else building_prop_logic,
                "category": "Terrain",
                "label_parts": [[prop["name"], "props"]],
                "description_parts": [["WorldObject", "common"]],
            }
        )

        temp_prop = {
            "class": prop_class,
            "name": prop["name"] + variation_helper[variation],
            "mesh": "Props/"
            + prop["name"]
            + "/"
            + prop["name"]
            + variation_helper[variation],
            "scale_min": prop["scale_min"],
            "scale_max": prop["scale_max"],
            "project_to_terrain_power": prop["project_to_terrain_power"],
            "item": prop["name"],
        }

        if "cull_begin" in prop:
            temp_prop["cull_begin"] = prop["cull_begin"]

        if "floating" in prop:
            temp_prop["floating"] = prop["floating"]

        if "cull_end" in prop:
            temp_prop["cull_end"] = prop["cull_end"]

        if "additive_elevation" in prop:
            temp_prop["additive_elevation"] = prop["additive_elevation"]

        if "maximum_height" in prop:
            temp_prop["maximum_height"] = prop["maximum_height"]

        if "minimum_height" in prop:
            temp_prop["minimum_height"] = prop["minimum_height"]

        objects_array.append(temp_prop)
        breaking_hand.append(
            {
                "name": prop["name"] + variation_helper[variation],
                "ticks": 40,
                "input": {
                    "items": [
                        {"name": prop["name"] + variation_helper[variation], "count": 1}
                    ]
                },
                "output": {
                    "items": [
                        {
                            "name": prop["drops"],
                            "count": 1
                            if "DropCount" not in prop
                            else prop["DropCount"],
                        }
                    ]
                },
            }
        )


for proplist in proplists:
    proplist_datas = []
    for subitem in proplist["array"]:
        props_array = []
        if "props" in subitem:
            for prop_name in subitem["props"]:
                for variation in range(0, named_prop(prop_name)["variations"]):
                    prop_class = (
                        static_big_prop
                        if "is_big" in named_prop(prop_name)
                        else static_prop
                    )
                    props_array.append(prop_name + variation_helper[variation])
        if "attaches" in subitem:
            for attach_name in subitem["attaches"]:
                props_array.append(attach_name)
        proplist_datas.append({"props": props_array, "chance": subitem["chance"] * 0.5})
    objects_array.append(
        {"class": prop_list, "name": proplist["name"], "array": proplist_datas}
    )

data = {"Objects": objects_array}

write_file("Generated/Mixed/props.json", data)

objects_array = []

objects_array.append(
    {"class": recipe_dictionary, "name": "Multitool", "recipes": breaking_hand}
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/props.json", data)

write_file("Loc/source/props.json", cvs)
