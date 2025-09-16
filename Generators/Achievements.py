from Common import *

ach = [
    {
        "Name": "CopperPlate",
        "Steam": True
    },
    {
        "Name": "SteelPlate",
        "Steam": True
    },
    {
        "Name": "TitaniumPlate",
        "Steam": True
    },
    {
        "Name": "StainlessSteelPlate",
        "Steam": True
    },
    {
        "Name": "AluminiumPlate",
        "Steam": True
    },
    {
        "Name": "MalachiteOre",
        "Steam": True
    },
    {
        "Name": "MagnetiteOre",
        "Steam": True
    },
    {
        "Name": "BauxiteOre",
        "Steam": True
    },
    {
        "Name": "ThorianiteOre",
        "Steam": True
    },
    {
        "Name": "CoalOre",
        "Steam": True
    },
    {
        "Name": "NeutroniumPlate",
        "Steam": True
    },
    {
        "Name": "CompositePlate",
        "Steam": True
    },  
    {
        "Name": "GoldPlate",
        "Steam": True
    },
    {
        "Name": "YttriumDust",
        "Steam": True
    },
    {
        "Name": "Battery",
        "Steam": True
    },
    {
        "Name": "NeutroniumPortal",
        "Steam": True
    },
    {
        "Name": "CompositeFusionReactor",
        "Steam": True
    },
    {
        "Name": "TitaniumFissionReactor",
        "Steam": True
    },
    {
        "Name": "SteelLogicCircuit",
        "Steam": True
    },
    {
        "Name": "Torch",
        "Steam": True
    },
    {
        "Name": "Ping",
        "Steam": True
    },
    {
        "Name": "PolyethyleneSheet",
        "Steam": True
    },
    {
        "Name": "SilverGod",
        "Steam": True
    },
    {
        "Name": "GoldenGod",
        "Steam": True
    },
    {
        "Name": "RubyOre",
        "Steam": True
    },
    {
        "Name": "CinnabarOre",
        "Steam": True
    },
    {
        "Name": "PyroplatiteOre",
        "Steam": True
    },
    {
        "Name": "PyriteOre",
        "Steam": True
    },
    {
        "Name": "ChalcopyriteOre",
        "Steam": True
    },
]

converted = []

for a in ach:
    record = {
        "Class": "StaticAchievement",
        "Name": a["Name"],
    }
    if "Image" in a:
        record["Image"] = a["Image"]
    if "Steam" in a:
        record["SteamKey"] = a["Name"]
    converted.append(record)

data = {
	"Objects": converted
}

write_file("Generated/Mixed/achievements.json", data)