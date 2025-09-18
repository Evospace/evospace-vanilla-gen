from Common import *

ach = [
    {
        "Name": "CopperPlate",
        "Steam": True,
        "Label": ["CopperPlate","parts"],
    },
    {
        "Name": "SteelPlate",
        "Steam": True,
        "Label": ["SteelPlate","parts"],
    },
    {
        "Name": "TitaniumPlate",
        "Steam": True,
        "Label": ["TitaniumPlate","parts"],
    },
    {
        "Name": "StainlessSteelPlate",
        "Steam": True,
        "Label": ["StainlessSteelPlate","parts"],
    },
    {
        "Name": "AluminiumPlate",
        "Steam": True,
        "Label": ["AluminiumPlate","parts"],
    },
    {
        "Name": "MalachiteOre",
        "Steam": True,
        "Label": ["MalachiteOre","ores"],
    },
    {
        "Name": "MagnetiteOre",
        "Steam": True,
        "Label": ["MagnetiteOre","ores"],
    },
    {
        "Name": "BauxiteOre",
        "Steam": True,
        "Label": ["BauxiteOre","ores"],
    },
    {
        "Name": "ThorianiteOre",
        "Steam": True,
        "Label": ["ThorianiteOre","ores"],
    },
    {
        "Name": "CoalOre",
        "Steam": True,
        "Label": ["CoalOre","ores"],
    },
    {
        "Name": "NeutroniumPlate",
        "Steam": True,
        "Label": ["NeutroniumPlate","parts"],
    },
    {
        "Name": "CompositePlate",
        "Steam": True,
        "Label": ["CompositePlate","parts"],
    },  
    {
        "Name": "GoldPlate",
        "Steam": True,
        "Label": ["GoldPlate","parts"],
    },
    {
        "Name": "YttriumDust",
        "Steam": True,
        "Label": ["YttriumDust","parts"],
    },
    {
        "Name": "Battery",
        "Steam": True,
        "Label": ["Battery","parts"],
    },
    {
        "Name": "NeutroniumPortal",
        "Steam": True,
        "Label": ["NeutroniumPortal","machines"],
    },
    {
        "Name": "CompositeFusionReactor",
        "Steam": True,
        "Label": ["CompositeFusionReactor","machines"],
    },
    {
        "Name": "TitaniumFissionReactor",
        "Steam": True,
        "Label": ["TitaniumFissionReactor","machines"],
    },
    {
        "Name": "SteelLogicCircuit",
        "Steam": True,
        "Label": ["SteelLogicCircuit","machines"],
    },
    {
        "Name": "Torch",
        "Steam": True,
        "Label": ["",""],
    },
    {
        "Name": "Ping",
        "Steam": True,
        "Label": ["",""],
    },
    {
        "Name": "PolyethyleneSheet",
        "Steam": True,
        "Label": ["PolyethyleneSheet","parts"],
    },
    {
        "Name": "SilverGod",
        "Steam": True,
        "Label": ["",""],
    },
    {
        "Name": "GoldenGod",
        "Steam": True,
        "Label": ["",""],
    },
    {
        "Name": "RubyOre",
        "Steam": True,
        "Label": ["RubyOre","ores"],
    },
    {
        "Name": "CinnabarOre",
        "Steam": True,
        "Label": ["CinnabarOre","ores"],
    },
    {
        "Name": "PyroplatiteOre",
        "Steam": True,
        "Label": ["PyroplatiteOre","ores"],
    },
    {
        "Name": "PyriteOre",
        "Steam": True,
        "Label": ["PyriteOre","ores"],
    },
    {
        "Name": "ChalcopyriteOre",
        "Steam": True,
        "Label": ["ChalcopyriteOre","ores"],
    },
]

converted = []

for a in ach:
    record = {
        "Class": "StaticAchievement",
        "Name": a["Name"],
        "Label": a["Label"]
    }
    if "Image" in a:
        record["Image"] = a["Image"]
    if "Steam" in a:
        record["SteamKey"] = a["Name"]
        record["Image"] = "T_"+a["Name"]
    converted.append(record)

data = {
	"Objects": converted
}

write_file("Generated/Mixed/achievements.json", data)