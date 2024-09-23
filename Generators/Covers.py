from Common import *

paint_colors = ("PaintYellow",)
paint_metals = ("Copper", "Steel", "Aluminium", "StainlessSteel", "Titanium", "HardMetal", "Neutronium")
paint_tiers = ("Stone", "Copper", "Steel", "Aluminium", "StainlessSteel", "Titanium", "HardMetal", "Neutronium")
tier_materials = ("/Game/Materials/Stone", "/Game/Materials/Copper", "/Game/Materials/Steel", "/Game/Materials/Aluminium", "/Game/Materials/StainlessSteel", "/Game/Materials/Titanium", "/Game/Materials/HardMetal", "/Game/Materials/Neutronium")

covers = [
    {
        "Name": "CableSide",
        "Mesh": "Covers/PipeSide",
        "Materials": ["/Game/Materials/Rubber2"]
    },
    {
        "Name": "CableCenter",
        "Mesh": "Covers/PipeCenter",
        "Materials": ["/Game/Materials/Rubber2"]
    },{
        "Name": "HeatSide",
        "Mesh": "Covers/HeatSide",
        "Materials": ["/Game/Materials/HeatingCopper"]
    },{
        "Name": "HeatCenter",
        "Mesh": "Covers/HeatCenter",
        "Materials": ["/Game/Materials/HeatingCopper"]
    },{
		"Name": "Cover",
		"Mesh": "Cover",
        "Materials": [""]
	},{
		"Name": "StoneFurnace",
		"Mesh": "019/FurnaceRound",
        "Materials": ["/Game/019/StoneFurnaceMaterial"]
	},{
		"Name": "RobotArmBase",
		"Mesh": "019/RobotArmBase",
        "Materials": []
	},{
		"Name": "BuilingBox",
		"Mesh": "BoxStaticMesh",
        "Materials": [],
        "NoCollision": True
	}
]

objects_array = []

for mat in paint_colors + paint_tiers:
	covers.append({
		"Name": "Cover" + mat,
		"Mesh": "Cover",
        "Materials": [mat]
	})
     
for mat, num in zip(paint_tiers, range(0,7+1)):
    covers.append({
        "Name": mat+"PipeCenter",
        "Mesh": "Covers/PipeCenter",
        "Materials": ["/Game/Materials/"+mat]
    })
    covers.append({
        "Name": mat+"PipeSide",
        "Mesh": "Covers/PipeSide",
        "Materials": ["/Game/Materials/"+mat],
        "Item": mat+"Pipe"
    })
    covers.append({
        "Name": mat+"Corner",
        "Mesh": "CoreContent/Corner",
        "Materials": ["/Game/Materials/"+mat]
    })
    covers.append({
        "Name": mat+"Scaffold",
        "Mesh": "Models/Scafold",
        "Materials": ["/Game/Materials/"+mat]
    })

for mat, num in zip(paint_metals, range(1,7+1)):
    covers.append({
		"Name": mat+"Furnace",
		"Mesh": "019Content/FurnaceRound",
        "Materials": ["/Game/019/FurnaceMaterial"],
        "Tier": num
	})
    covers.append({
		"Name": mat+"Conveyor",
		"Mesh": "019/conveyor_end",
        "Materials": ["/Game/Materials/RubberWithTierParam", tier_materials[num]],
        "Tier": num
	})
    covers.append({
		"Name": mat+"ConveyorBox",
		"Mesh": "019/conveyor_box",
        "Materials": [tier_materials[num]],
        "Tier": num
	})
    covers.append({
		"Name": mat+"ElectricEngine",
		"Mesh": "019/ElectricEngine",
        "Materials": ["/Game/019/ElectricEngineMaterial"],
        "Tier": num
	})
	
for cover in covers:
    if "HasItem" in cover:
        objects_array.append({ "Class": "StaticItem",
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
    if "Tier" in cover:
        staticCover["Tier"] = cover["Tier"]

    if "NoCollision" in cover:
        staticCover["NoCollision"] = cover["NoCollision"]

    objects_array.append(staticCover)


data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/covers.json", data)