from Common import *

paint_colors = ("PaintYellow",)
paint_metals = ("Stone", "Copper", "Steel", "Aluminium", "StainlessSteel", "Titanium", "HardMetal", "Neutronium")

covers = [
    {
        "Name": "CableSide",
        "Mesh": "Covers/PipeSide",
        "Materials": ["Materials/Rubber2"],
        "Item": "CopperConnector"
    },
    {
        "Name": "CableCenter",
        "Mesh": "Covers/PipeCenter",
        "Materials": ["Materials/Rubber2"],
        "Item": "CopperConnector"
    },{
        "Name": "HeatSide",
        "Mesh": "Covers/HeatSide",
        "Materials": ["Materials/HeatingCopper"],
        "Item": "CopperHeatPipe"
    },{
        "Name": "HeatCenter",
        "Mesh": "Covers/HeatCenter",
        "Materials": ["Materials/HeatingCopper"],
        "Item": "CopperHeatPipe"
    },{
		"Name": "Cover",
		"Mesh": "Cover",
        "Materials": [""],
        "Item": "Cover"
	}
]

objects_array = []

for mat in paint_colors + paint_metals:
	covers.append({
		"Name": "Cover" + mat,
		"Mesh": "Cover",
        "Materials": [mat]
	})
     
for mat, num in zip(paint_metals, range(0,7)):
    covers.append({
        "Name": mat+"PipeCenter",
        "Mesh": "Covers/PipeCenter",
        "Materials": ["Materials/"+mat],
        "Item": mat+"Pipe"
    })
    covers.append({
        "Name": mat+"PipeSide",
        "Mesh": "Covers/PipeSide",
        "Materials": ["Materials/"+mat],
        "Item": mat+"Pipe"
    })
    covers.append({
        "Name": mat+"Corner",
        "Mesh": "CoreContent/Corner",
        "Materials": ["Materials/"+mat],
        "Item": mat+"Corner"
    })
    covers.append({
        "Name": mat+"Scaffold",
        "Mesh": "Models/Scafold",
        "Materials": ["Materials/"+mat],
        "Item": mat+"Scaffold"
    })
    covers.append({
		"Name": mat+"Furnace",
		"Mesh": "019Content/FurnaceRound",
        "Materials": ["019Content/FurnaceMaterial"],
        "Item": mat+"Furnace",
        "TierTint": num
	})
	
for cover in covers:
    if "HasItem" in cover:
        objects_array.append({ "Class": static_item,
            "Name": cover["Name"] + static_item,
            
            "MaxCount": 32,
            "Image": "T_" + cover["Name"],
            "ItemLogic": cover_item_logic,
            "Category": "Terrain",
            
            "LabelParts": [[cover["Name"], "props"]],
            "DescriptionParts":[["WorldObject","common"]],
        })
    staticCover = { "Class": static_cover,
        "Name": cover["Name"] + static_cover,
        "Mesh": cover["Mesh"],
        "Materials": cover["Materials"]
    }
    if "TierTint" in cover:
         staticCover["TierTint"] = cover["TierTint"]

    if "Item" in cover:
        staticCover["Minable"] = {"MiningTime": 20, "Result": cover["Item"] + static_item}
        staticCover["Item"] = cover["Item"] + static_item
    objects_array.append(staticCover)


data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/covers.json", data)