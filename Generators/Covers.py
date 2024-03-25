from Common import *

paint_colors = ("PaintYellow",)
paint_metals = ("Steel", "Copper", "StainlessSteel", "Aluminium", "HardMetal", "Titanium" , "Neutronium")

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
     
for mat in paint_metals:
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
    cover = { "Class": "StaticCover",
        "Name": cover["Name"] + "StaticCover",
        "Mesh": cover["Mesh"],
        "Materials": cover["Materials"]
    }
    if "Item" in cover:
        cover["Minable"] = {"MiningTime": 20, "Result": cover["Item"] + static_item}
        cover["Item"] = cover["Item"] + static_item
    objects_array.append(cover)


data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/covers.json", data)