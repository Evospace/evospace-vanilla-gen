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
        "Drops": "Organics",
        "AdditiveElevation": 0,
        "TimeMul": 1,
    },
    {
        "name": "Dandaleon",
        "ScaleMin": [2, 2, 2],
        "ScaleMax": [4, 4, 4],
        "Variations": 3,
        "ProjectToTerrainPower": 1,
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Noleafes",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [3, 3, 3],
        "Variations": 1,
        "ProjectToTerrainPower": 0,
        "IsBig": True,
        "Drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Shrub",
        "ScaleMin": [1.5, 1.5, 1.5],
        "ScaleMax": [2.5, 2.5, 2.5],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "IsBig": True,
        "Drops": "Log",
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
        "Drops": "StoneSurface",
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
        "Drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "SnowyPine",
        "ScaleMin": [0.6, 0.6, 0.6],
        "ScaleMax": [1.2, 1.2, 1.2],
        "Variations": 3,
        "ProjectToTerrainPower": 0,
        "IsBig": True,
        "Drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Birch",
        "ScaleMin": [0.6, 0.6, 0.6],
        "ScaleMax": [1.4, 1.4, 1.4],
        "Variations": 2,
        "ProjectToTerrainPower": 0,
        "IsBig": True,
        "Drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Palm",
        "ScaleMin": [0.6, 0.6, 0.6],
        "ScaleMax": [1.4, 1.4, 1.4],
        "Variations": 2,
        "ProjectToTerrainPower": 0,
        "IsBig": True,
        "Drops": "Log",
        "TimeMul": 1,
    },
    {
        "name": "Rogoz",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [3, 3, 3],
        "Variations": 5,
        "ProjectToTerrainPower": 0,
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Organics",
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
        "Drops": "Plank",
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
        "Drops": "StoneSurface",
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
        "Drops": "StoneLog",
        "TimeMul": 6,
    },
    {
        "name": "DryGrass",
        "ScaleMin": [1, 1, 1],
        "ScaleMax": [4, 4, 4],
        "Variations": 1,
        "ProjectToTerrainPower": 1,
        "HandInteraction": False,
        "Drops": "Organics",
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
        "Drops": "BasaltSurface",
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
        "Drops": "BasaltSurface",
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
        "Drops": "Organics",
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
            {"Props": ["SmallRock"], "Chance": 0.01},
            {"Props": ["DryGrass"], "Chance": 0.5},
            {
                "Props": ["Broadleaf", "Broadleaf", "Birch", "BigBush", "Noleafes"],
                "Chance": 0.0001,
            },
        ],
    },
    {
        "name": "PrairiePropList",
        "Array": [
            {"Props": ["SmallRock"], "Chance": 0.01},
            {"Props": ["DryGrass"], "Chance": 0.35},
            {"Props": ["LongGrass"], "Chance": 0.35},
            {
                "Props": ["Broadleaf", "Broadleaf", "Birch", "BigBush", "Noleafes"],
                "Chance": 0.0004,
            },
        ],
    },
    {
        "name": "DipteroPropList",
        "Array": [
            {"Props": ["Diptero"], "Chance": 0.001},
            {
                "Props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
                "Chance": 0.01,
            },
            {"Props": ["SmallRock"], "Chance": 0.01},
            {"Props": ["Fern"], "Chance": 0.05},
            {"Props": ["LongGrass"], "Chance": 0.9},
        ],
    },
    {
        "name": "SmallRocksProps",
        "Array": [
            {"Props": ["SmallRock"], "Chance": 0.06},
            {"Props": ["VolcanicRock"], "Chance": 0.01},
        ],
    },
    {"name": "SnowProps", "Array": [{"Props": ["SnowyRock"], "Chance": 0.01}]},
    {
        "name": "BushlandProps",
        "Array": [
            {"Props": ["Shrub", "BigBush"], "Chance": 0.05},
            {"Props": ["LongGrass"], "Chance": 0.5},
            {"Props": ["TallGrass"], "Chance": 0.1},
        ],
    },
    {
        "name": "GrasslandProps",
        "Array": [
            {"Props": ["Rock"], "Chance": 0.005},
            {"Props": ["Dandaleon"], "Chance": 0.05},
            {"Props": ["LongGrass"], "Chance": 0.9},
            {"Props": ["TallGrass"], "Chance": 0.3},
        ],
    },
    {
        "name": "RedFlowersProps",
        "Array": [
            {"Props": ["RedFlower"], "Chance": 0.5},
            {"Props": ["LongGrass"], "Chance": 0.9},
            {"Attaches": ["Butterfly"], "Chance": 0.001},
            {"Attaches": ["Flies"], "Chance": 0.001},
        ],
    },
    {
        "name": "YellowFlowersProps",
        "Array": [
            {"Props": ["YellowFlower"], "Chance": 0.5},
            {"Props": ["LongGrass"], "Chance": 0.9},
            {"Attaches": ["Butterfly"], "Chance": 0.001},
        ],
    },
    {
        "name": "WhiteFlowersProps",
        "Array": [
            {"Props": ["WhiteFlower"], "Chance": 0.5},
            {"Props": ["LongGrass"], "Chance": 0.9},
            {"Attaches": ["Butterfly"], "Chance": 0.001},
        ],
    },
    {
        "name": "DenseForestProps",
        "Array": [
            {"Props": ["Noleafes"], "Chance": 0.001},
            {
                "Props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
                "Chance": 0.02,
            },
            {"Props": ["SmallRock"], "Chance": 0.01},
            {"Props": ["Fern"], "Chance": 0.03},
            {"Props": ["Dandaleon"], "Chance": 0.3},
            {"Props": ["LongGrass"], "Chance": 0.7},
            {"Props": ["Shroom"], "Chance": 0.01},
            {"Attaches": ["Birds"], "Chance": 0.001},
            {"Attaches": ["Leafes"], "Chance": 0.001},
        ],
    },
    {
        "name": "ForestProps",
        "Array": [
            {"Props": ["Noleafes"], "Chance": 0.001},
            {
                "Props": ["Broadleaf", "Broadleaf", "Birch", "Shrub", "BigBush"],
                "Chance": 0.01,
            },
            {"Props": ["SmallRock"], "Chance": 0.01},
            {"Props": ["Fern"], "Chance": 0.05},
            {"Props": ["Dandaleon"], "Chance": 0.5},
            {"Props": ["LongGrass"], "Chance": 0.9},
            {"Props": ["Shroom"], "Chance": 0.01},
            {"Attaches": ["Birds"], "Chance": 0.001},
            {"Attaches": ["Leafes"], "Chance": 0.001},
            {"Attaches": ["Flies"], "Chance": 0.002},
        ],
    },
    {
        "name": "DensePineForestProps",
        "Array": [
            {"Props": ["Rock"], "Chance": 0.001},
            {"Props": ["SmallRock"], "Chance": 0.01},
            {"Props": ["Pine"], "Chance": 0.02},
            {"Props": ["LongGrass"], "Chance": 0.03},
            {"Props": ["Shroom"], "Chance": 0.01},
            {"Attaches": ["Birds"], "Chance": 0.001},
            {"Attaches": ["Flies"], "Chance": 0.001},
        ],
    },
    {
        "name": "PineForestProps",
        "Array": [
            {"Props": ["Rock"], "Chance": 0.002},
            {"Props": ["SmallRock"], "Chance": 0.01},
            {"Props": ["Pine"], "Chance": 0.01},
            {"Props": ["LongGrass"], "Chance": 0.07},
            {"Props": ["Shroom"], "Chance": 0.01},
            {"Attaches": ["Birds"], "Chance": 0.001},
            {"Attaches": ["Bugs"], "Chance": 0.001},
            {"Attaches": ["Flies"], "Chance": 0.001},
        ],
    },
    {"name": "UnimplementedProps", "Array": [{"Props": ["Rock"], "Chance": 0.01}]},
    {
        "name": "DesertProps",
        "Array": [
            {"Props": ["Cactus"], "Chance": 0.01},
            {"Props": ["Palm"], "Chance": 0.002},
            {"Attaches": ["DesertSound"], "Chance": 0.002},
        ],
    },
    {
        "name": "IslandProps",
        "Array": [
            {"Props": ["SmallRock"], "Chance": 0.01},
            {"Props": ["SeaPlant"], "Chance": 0.07},
        ],
    },
    {
        "name": "SeagrassProps",
        "Array": [
            {"Props": ["SmallRock"], "Chance": 0.01},
            {"Props": ["SeaGrass"], "Chance": 0.15},
        ],
    },
    {"name": "EmptySeaProps", "Array": [{"Props": ["SmallRock"], "Chance": 0.05}]},
    {
        "name": "SwampProps",
        "Array": [
            {"Props": ["SmallRock"], "Chance": 0.01},
            {"Props": ["LongGrass"], "Chance": 0.7},
            {"Props": ["Fern"], "Chance": 0.05},
            {"Props": ["Rogoz"], "Chance": 0.5},
            {"Props": ["Lily"], "Chance": 0.5},
            {"Props": ["LilyFlower"], "Chance": 0.05},
            {"Attaches": ["SwampSound"], "Chance": 0.002},
            {"Attaches": ["Firefly", "Flies"], "Chance": 0.005},
        ],
    },
    {
        "name": "SwampForestProps",
        "Array": [
            {"Props": ["LongGrass"], "Chance": 0.7},
            {"Props": ["Fern"], "Chance": 0.05},
            {"Props": ["Birch", "BigBush"], "Chance": 0.01},
            {"Props": ["Shroom"], "Chance": 0.01},
            {"Attaches": ["Firefly", "Flies"], "Chance": 0.005},
        ],
    },
    {
        "name": "OreProps",
        "Array": [
            {"Props": ["LongGrass"], "Chance": 0.07},
            {"Props": ["Birch", "BigBush"], "Chance": 0.01},
            {"Props": ["Shroom"], "Chance": 0.01},
        ],
    },
    {
        "name": "SnowGrassProps",
        "Array": [
            {"Props": ["SnowyGrass"], "Chance": 0.2},
            {"Props": ["SnowyRock"], "Chance": 0.01},
        ],
    },
    {
        "name": "SnowForestProps",
        "Array": [
            {"Props": ["SnowyGrass"], "Chance": 0.2},
            {"Props": ["SnowyPine"], "Chance": 0.005},
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
                "item_logic": building_prop_logic
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
            "Mesh": "Props/"
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
                "Ticks": 40,
                "Input": {
                    "Items": [
                        {"name": prop["name"] + variation_helper[variation], "Count": 1}
                    ]
                },
                "Output": {
                    "Items": [
                        {
                            "name": prop["Drops"],
                            "Count": 1
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
        if "Props" in subitem:
            for prop_name in subitem["Props"]:
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
        proplist_datas.append({"Props": props_array, "Chance": subitem["Chance"] * 0.5})
    objects_array.append(
        {"class": prop_list, "name": proplist["name"], "Array": proplist_datas}
    )

data = {"Objects": objects_array}

write_file("Generated/Mixed/props.json", data)

objects_array = []

objects_array.append(
    {"class": recipe_dictionary, "name": "Multitool", "Recipes": breaking_hand}
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/props.json", data)

write_file("Loc/source/props.json", cvs)
