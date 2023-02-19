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
        "ScaleMin": [0.5, 0.5, 0.5],
        "ScaleMax": [2, 2, 2],
        "Variations": 2,
        "ProjectToTerrainPower": 1,
        "IsBig": True,
        "drops": "Organics",
        "AdditiveElevation": 0,
        "TimeMul": 1,
    },
    {
        "name": "Dandaleon",
        "ScaleMin": [2, 2, 2],
        "ScaleMax": [4, 4, 4],
        "Variations": 3,
        "ProjectToTerrainPower": 1,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
    },
    {
        "name": "Fern",
        "ScaleMin": [4, 4, 4],
        "ScaleMax": [6, 6, 6],
        "Variations": 3,
        "ProjectToTerrainPower": 1,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
    },
    {
        "name": "LongGrass",
        "ScaleMin": [2, 2, 2],
        "ScaleMax": [4, 4, 4],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
    },
    {
        "name": "SeaPlant",
        "ScaleMin": [2, 2, 2],
        "ScaleMax": [4, 4, 4],
        "Variations": 22,
        "ProjectToTerrainPower": 0,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
        "MaximumHeight": -1,
    },
    {
        "name": "SeaGrass",
        "ScaleMin": [2, 2, 2],
        "ScaleMax": [4, 4, 4],
        "Variations": 5,
        "ProjectToTerrainPower": 0,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
        "MaximumHeight": -1,
    },
    {
        "name": "TallGrass",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [3, 3, 3],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
    },
    {
        "name": "Broadleaf",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [3, 3, 3],
        "Variations": 3,
        "ProjectToTerrainPower": 0,
        "IsBig": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Noleafes",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [3, 3, 3],
        "Variations": 1,
        "ProjectToTerrainPower": 0,
        "IsBig": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Shrub",
        "ScaleMin": [1.5, 1.5, 1.5],
        "ScaleMax": [2.5, 2.5, 2.5],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "IsBig": True,
        "drops": "Log",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "TimeMul": 1,
    },
    {
        "name": "Rock",
        "ScaleMin": [0.6, 0.6, 0.6],
        "ScaleMax": [3, 3, 3],
        "Variations": 2,
        "ProjectToTerrainPower": 1,
        "IsBig": True,
        "drops": "StoneSurface",
        "DropCount": 10,
        "AdditiveElevation": 0,
        "TimeMul": 1,
    },
    {
        "name": "Pine",
        "ScaleMin": [0.6, 0.6, 0.6],
        "ScaleMax": [1.4, 1.4, 1.4],
        "Variations": 3,
        "ProjectToTerrainPower": 0,
        "IsBig": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "SnowyPine",
        "ScaleMin": [0.6, 0.6, 0.6],
        "ScaleMax": [1.2, 1.2, 1.2],
        "Variations": 3,
        "ProjectToTerrainPower": 0,
        "IsBig": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Birch",
        "ScaleMin": [0.6, 0.6, 0.6],
        "ScaleMax": [1.4, 1.4, 1.4],
        "Variations": 2,
        "ProjectToTerrainPower": 0,
        "IsBig": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Palm",
        "ScaleMin": [0.6, 0.6, 0.6],
        "ScaleMax": [1.4, 1.4, 1.4],
        "Variations": 2,
        "ProjectToTerrainPower": 0,
        "IsBig": True,
        "drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Rogoz",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [3, 3, 3],
        "Variations": 5,
        "ProjectToTerrainPower": 0,
        "drops": "Organics",
        "CullBegin": 7000,
        "CullEnd": 8000,
        "AdditiveElevation": 0,
    },
    {
        "name": "Lily",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [3, 3, 3],
        "Variations": 1,
        "ProjectToTerrainPower": 0,
        "drops": "Organics",
        "CullBegin": 7000,
        "CullEnd": 8000,
        "AdditiveElevation": 70,
        "Floating": True,
    },
    {
        "name": "LilyFlower",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [3, 3, 3],
        "Variations": 2,
        "ProjectToTerrainPower": 0,
        "drops": "Organics",
        "CullBegin": 7000,
        "CullEnd": 8000,
        "AdditiveElevation": 70,
        "Floating": True,
    },
    {
        "name": "Shroom",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [2, 2, 2],
        "Variations": 6,
        "ProjectToTerrainPower": 0,
        "drops": "Organics",
        "AdditiveElevation": 20,
        "CullBegin": 10000,
        "CullEnd": 12000,
    },
    {
        "name": "YellowFlower",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [2, 2, 2],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
    },
    {
        "name": "RedFlower",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [2, 2, 2],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
    },
    {
        "name": "WhiteFlower",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [2, 2, 2],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
    },
    {
        "name": "BigBush",
        "ScaleMin": [1.5, 1.5, 1.5],
        "ScaleMax": [3, 3, 3],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "HandInteraction": True,
        "drops": "Plank",
        "AdditiveElevation": 0,
        "CullBegin": 10000,
        "CullEnd": 12000,
    },
    {
        "name": "SmallRock",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [3, 3, 3],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "HandInteraction": True,
        "drops": "StoneSurface",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
    },
    {
        "name": "Diptero",
        "ScaleMin": [0.8, 0.8, 0.8],
        "ScaleMax": [1.3, 1.3, 1.3],
        "Variations": 2,
        "ProjectToTerrainPower": 0,
        "HandInteraction": False,
        "AdditiveElevation": 0,
        "IsBig": True,
        "drops": "StoneLog",
        "TimeMul": 6,
    },
    {
        "name": "DryGrass",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [4, 4, 4],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "HandInteraction": False,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
    },
    {
        "name": "VolcanicRock",
        "ScaleMin": [0.5, 0.5, 0.5],
        "ScaleMax": [1, 1, 1],
        "Variations": 4,
        "ProjectToTerrainPower": 1,
        "HandInteraction": False,
        "drops": "BasaltSurface",
        "DropCount": 10,
        "IsBig": True,
        "AdditiveElevation": 0,
        "TimeMul": 1,
    },
    {
        "name": "SnowyRock",
        "ScaleMin": [0.5, 0.5, 0.5],
        "ScaleMax": [1, 1, 1],
        "Variations": 4,
        "ProjectToTerrainPower": 1,
        "HandInteraction": False,
        "drops": "BasaltSurface",
        "DropCount": 10,
        "CullBegin": 10000,
        "CullEnd": 12000,
        "IsBig": True,
        "AdditiveElevation": 0,
        "TimeMul": 1,
    },
    {
        "name": "SnowyGrass",
        "ScaleMin": [2, 2, 2],
        "ScaleMax": [4, 4, 4],
        "Variations": 3,
        "ProjectToTerrainPower": 1,
        "HandInteraction": False,
        "drops": "Organics",
        "CullBegin": 10000,
        "CullEnd": 12000,
        "AdditiveElevation": 0,
    },
]


def named_prop(name):
    return [x for x in props if x["name"] == name][0]


proplists = [
    {
        "name": "PrairieDryPropList",
        "Array": [
            {"props": ["SmallRock"], "Chance": 0.01},
            {"props": ["DryGrass"], "Chance": 0.5},
            {
                "props": ["Broadleaf", "Broadleaf", "Birch", "BigBush", "Noleafes"],
                "Chance": 0.0001,
            },
        ],
    },
    {
        "name": "PrairiePropList",
        "Array": [
            {"props": ["SmallRock"], "Chance": 0.01},
            {"props": ["DryGrass"], "Chance": 0.35},
            {"props": ["LongGrass"], "Chance": 0.35},
            {
                "props": ["Broadleaf", "Broadleaf", "Birch", "BigBush", "Noleafes"],
                "Chance": 0.0004,
            },
        ],
    },
    {
        "name": "DipteroPropList",
        "Array": [
            {"props": ["Diptero"], "Chance": 0.001},
            {
                "props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
                "Chance": 0.01,
            },
            {"props": ["SmallRock"], "Chance": 0.01},
            {"props": ["Fern"], "Chance": 0.05},
            {"props": ["LongGrass"], "Chance": 0.9},
        ],
    },
    {
        "name": "SmallRocksProps",
        "Array": [
            {"props": ["SmallRock"], "Chance": 0.06},
            {"props": ["VolcanicRock"], "Chance": 0.01},
        ],
    },
    {"name": "SnowProps", "Array": [{"props": ["SnowyRock"], "Chance": 0.01}]},
    {
        "name": "BushlandProps",
        "Array": [
            {"props": ["Shrub", "BigBush"], "Chance": 0.05},
            {"props": ["LongGrass"], "Chance": 0.5},
            {"props": ["TallGrass"], "Chance": 0.1},
        ],
    },
    {
        "name": "GrasslandProps",
        "Array": [
            {"props": ["Rock"], "Chance": 0.005},
            {"props": ["Dandaleon"], "Chance": 0.05},
            {"props": ["LongGrass"], "Chance": 0.9},
            {"props": ["TallGrass"], "Chance": 0.3},
        ],
    },
    {
        "name": "RedFlowersProps",
        "Array": [
            {"props": ["RedFlower"], "Chance": 0.5},
            {"props": ["LongGrass"], "Chance": 0.9},
            {"Attaches": ["Butterfly"], "Chance": 0.001},
            {"Attaches": ["Flies"], "Chance": 0.001},
        ],
    },
    {
        "name": "YellowFlowersProps",
        "Array": [
            {"props": ["YellowFlower"], "Chance": 0.5},
            {"props": ["LongGrass"], "Chance": 0.9},
            {"Attaches": ["Butterfly"], "Chance": 0.001},
        ],
    },
    {
        "name": "WhiteFlowersProps",
        "Array": [
            {"props": ["WhiteFlower"], "Chance": 0.5},
            {"props": ["LongGrass"], "Chance": 0.9},
            {"Attaches": ["Butterfly"], "Chance": 0.001},
        ],
    },
    {
        "name": "DenseForestProps",
        "Array": [
            {"props": ["Noleafes"], "Chance": 0.001},
            {
                "props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
                "Chance": 0.02,
            },
            {"props": ["SmallRock"], "Chance": 0.01},
            {"props": ["Fern"], "Chance": 0.03},
            {"props": ["Dandaleon"], "Chance": 0.3},
            {"props": ["LongGrass"], "Chance": 0.7},
            {"props": ["Shroom"], "Chance": 0.01},
            {"Attaches": ["Birds"], "Chance": 0.001},
            {"Attaches": ["Leafes"], "Chance": 0.001},
        ],
    },
    {
        "name": "ForestProps",
        "Array": [
            {"props": ["Noleafes"], "Chance": 0.001},
            {
                "props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
                "Chance": 0.01,
            },
            {"props": ["SmallRock"], "Chance": 0.01},
            {"props": ["Fern"], "Chance": 0.05},
            {"props": ["Dandaleon"], "Chance": 0.5},
            {"props": ["LongGrass"], "Chance": 0.9},
            {"props": ["Shroom"], "Chance": 0.01},
            {"Attaches": ["Birds"], "Chance": 0.001},
            {"Attaches": ["Leafes"], "Chance": 0.001},
            {"Attaches": ["Flies"], "Chance": 0.002},
        ],
    },
    {
        "name": "DensePineForestProps",
        "Array": [
            {"props": ["Rock"], "Chance": 0.001},
            {"props": ["SmallRock"], "Chance": 0.01},
            {"props": ["Pine"], "Chance": 0.02},
            {"props": ["LongGrass"], "Chance": 0.03},
            {"props": ["Shroom"], "Chance": 0.01},
            {"Attaches": ["Birds"], "Chance": 0.001},
            {"Attaches": ["Flies"], "Chance": 0.001},
        ],
    },
    {
        "name": "PineForestProps",
        "Array": [
            {"props": ["Rock"], "Chance": 0.002},
            {"props": ["SmallRock"], "Chance": 0.01},
            {"props": ["Pine"], "Chance": 0.01},
            {"props": ["LongGrass"], "Chance": 0.07},
            {"props": ["Shroom"], "Chance": 0.01},
            {"Attaches": ["Birds"], "Chance": 0.001},
            {"Attaches": ["Bugs"], "Chance": 0.001},
            {"Attaches": ["Flies"], "Chance": 0.001},
        ],
    },
    {"name": "UnimplementedProps", "Array": [{"props": ["Rock"], "Chance": 0.01}]},
    {
        "name": "DesertProps",
        "Array": [
            {"props": ["Cactus"], "Chance": 0.01},
            {"props": ["Palm"], "Chance": 0.002},
            {"Attaches": ["DesertSound"], "Chance": 0.002},
        ],
    },
    {
        "name": "IslandProps",
        "Array": [
            {"props": ["SmallRock"], "Chance": 0.01},
            {"props": ["SeaPlant"], "Chance": 0.07},
        ],
    },
    {
        "name": "SeagrassProps",
        "Array": [
            {"props": ["SmallRock"], "Chance": 0.01},
            {"props": ["SeaGrass"], "Chance": 0.15},
        ],
    },
    {"name": "EmptySeaProps", "Array": [{"props": ["SmallRock"], "Chance": 0.05}]},
    {
        "name": "SwampProps",
        "Array": [
            {"props": ["SmallRock"], "Chance": 0.01},
            {"props": ["LongGrass"], "Chance": 0.7},
            {"props": ["Fern"], "Chance": 0.05},
            {"props": ["Rogoz"], "Chance": 0.5},
            {"props": ["Lily"], "Chance": 0.5},
            {"props": ["LilyFlower"], "Chance": 0.05},
            {"Attaches": ["SwampSound"], "Chance": 0.002},
            {"Attaches": ["Firefly", "Flies"], "Chance": 0.005},
        ],
    },
    {
        "name": "SwampForestProps",
        "Array": [
            {"props": ["LongGrass"], "Chance": 0.7},
            {"props": ["Fern"], "Chance": 0.05},
            {"props": ["Birch", "BigBush"], "Chance": 0.01},
            {"props": ["Shroom"], "Chance": 0.01},
            {"Attaches": ["Firefly", "Flies"], "Chance": 0.005},
        ],
    },
    {
        "name": "OreProps",
        "Array": [
            {"props": ["LongGrass"], "Chance": 0.07},
            {"props": ["Birch", "BigBush"], "Chance": 0.01},
            {"props": ["Shroom"], "Chance": 0.01},
        ],
    },
    {
        "name": "SnowGrassProps",
        "Array": [
            {"props": ["SnowyGrass"], "Chance": 0.2},
            {"props": ["SnowyRock"], "Chance": 0.01},
        ],
    },
    {
        "name": "SnowForestProps",
        "Array": [
            {"props": ["SnowyGrass"], "Chance": 0.2},
            {"props": ["SnowyPine"], "Chance": 0.005},
        ],
    },
]

objects_array = []
breaking_hand = []

for prop in props:
    cvs.append([prop["name"], CamelToSpaces(prop["name"])])
    for variation in range(0, prop["Variations"]):
        prop_class = static_big_prop if "IsBig" in prop else static_prop

        objects_array.append(
            {
                "class": static_item,
                "name": prop["name"] + variation_helper[variation],
                "max_count": 32,
                "image": "T_" + prop["name"],
                "logic_json": {"Block": prop["name"] + variation_helper[variation]},
                "logic": building_prop_logic
                if "IsBig" in prop
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
            "ScaleMin": prop["ScaleMin"],
            "ScaleMax": prop["ScaleMax"],
            "ProjectToTerrainPower": prop["ProjectToTerrainPower"],
            "Item": prop["name"],
        }

        if "CullBegin" in prop:
            temp_prop["CullBegin"] = prop["CullBegin"]

        if "Floating" in prop:
            temp_prop["Floating"] = prop["Floating"]

        if "CullEnd" in prop:
            temp_prop["CullEnd"] = prop["CullEnd"]

        if "AdditiveElevation" in prop:
            temp_prop["AdditiveElevation"] = prop["AdditiveElevation"]

        if "MaximumHeight" in prop:
            temp_prop["MaximumHeight"] = prop["MaximumHeight"]

        if "MinimumHeight" in prop:
            temp_prop["MinimumHeight"] = prop["MinimumHeight"]

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
    for subitem in proplist["Array"]:
        props_array = []
        if "props" in subitem:
            for prop_name in subitem["props"]:
                for variation in range(0, named_prop(prop_name)["Variations"]):
                    prop_class = (
                        static_big_prop
                        if "IsBig" in named_prop(prop_name)
                        else static_prop
                    )
                    props_array.append(prop_name + variation_helper[variation])
        if "Attaches" in subitem:
            for attach_name in subitem["Attaches"]:
                props_array.append(attach_name)
        proplist_datas.append({"props": props_array, "Chance": subitem["Chance"] * 0.5})
    objects_array.append(
        {"class": prop_list, "name": proplist["name"], "Array": proplist_datas}
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
