from Common import *

FirstItemAcq = ["FirstItemAcquired", "ui"]

ach = [
    {
        "Name": "CopperPlate",
        "Steam": True,
        "Label": ["CopperPlate","parts"],
        "Description": FirstItemAcq
    },
    {
        "Name": "SteelPlate",
        "Steam": True,
        "Label": ["SteelPlate","parts"],
        "Description": FirstItemAcq
    },
    {
        "Name": "TitaniumPlate",
        "Steam": True,
        "Label": ["TitaniumPlate","parts"],
        "Description": FirstItemAcq
    },
    {
        "Name": "StainlessSteelPlate",
        "Steam": True,
        "Label": ["StainlessSteelPlate","parts"],
        "Description": FirstItemAcq
    },
    {
        "Name": "AluminiumPlate",
        "Steam": True,
        "Label": ["AluminiumPlate","parts"],
        "Description": FirstItemAcq
    },
    {
        "Name": "MalachiteOre",
        "Steam": True,
        "Label": ["MalachiteOre","ores"],
        "Description": FirstItemAcq
    },
    {
        "Name": "MagnetiteOre",
        "Steam": True,
        "Label": ["MagnetiteOre","ores"],
        "Description": FirstItemAcq
    },
    {
        "Name": "BauxiteOre",
        "Steam": True,
        "Label": ["BauxiteOre","ores"],
        "Description": FirstItemAcq
    },
    {
        "Name": "ThorianiteOre",
        "Steam": True,
        "Label": ["ThorianiteOre","ores"],
        "Description": FirstItemAcq
    },
    {
        "Name": "CoalOre",
        "Steam": True,
        "Label": ["CoalOre","ores"],
        "Description": FirstItemAcq
    },
    {
        "Name": "NeutroniumPlate",
        "Steam": True,
        "Label": ["NeutroniumPlate","parts"],
        "Description": FirstItemAcq
    },
    {
        "Name": "CompositePlate",
        "Steam": True,
        "Label": ["CompositePlate","parts"],
        "Description": FirstItemAcq
    },  
    {
        "Name": "GoldPlate",
        "Steam": True,
        "Label": ["GoldPlate","parts"],
        "Description": FirstItemAcq
    },
    {
        "Name": "YttriumDust",
        "Steam": True,
        "Label": ["YttriumDust","parts"],
        "Description": FirstItemAcq
    },
    {
        "Name": "Battery",
        "Steam": True,
        "Label": ["Battery","parts"],
        "Description": FirstItemAcq
    },
    {
        "Name": "NeutroniumPortal",
        "Steam": True,
        "Label": ["NeutroniumPortal","machines"],
        "Description": FirstItemAcq
    },
    {
        "Name": "CompositeFusionReactor",
        "Steam": True,
        "Label": ["CompositeFusionReactor","machines"],
        "Description": FirstItemAcq
    },
    {
        "Name": "TitaniumFissionReactor",
        "Steam": True,
        "Label": ["TitaniumFissionReactor","machines"],
        "Description": FirstItemAcq
    },
    {
        "Name": "SteelLogicCircuit",
        "Steam": True,
        "Label": ["SteelLogicCircuit","machines"],
        "Description": FirstItemAcq
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
        "Description": FirstItemAcq
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
        "Description": FirstItemAcq
    },
    {
        "Name": "CinnabarOre",
        "Steam": True,
        "Label": ["CinnabarOre","ores"],
        "Description": FirstItemAcq
    },
    {
        "Name": "PyroplatiteOre",
        "Steam": True,
        "Label": ["PyroplatiteOre","ores"],
        "Description": FirstItemAcq
    },
    {
        "Name": "ChalcopyriteOre",
        "Steam": True,
        "Label": ["ChalcopyriteOre","ores"],
        "Description": FirstItemAcq
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
    if "Description" in a:
        record["Description"] = a["Description"]
    if "Steam" in a:
        record["SteamKey"] = a["Name"]
        record["Image"] = "T_"+a["Name"]
    converted.append(record)

data = {
	"Objects": converted
}

write_file("Generated/Mixed/achievements.json", data)