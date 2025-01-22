from Common import *

paint_colors = ("PaintYellow",)
paint_metals = ("Copper", "Steel", "Aluminium", "StainlessSteel", "Titanium", "HardMetal", "Neutronium")
paint_tiers = ("Stone", "Copper", "Steel", "Aluminium", "StainlessSteel", "Titanium", "HardMetal", "Neutronium")
tier_materials = ("/Game/Materials/Stone", "/Game/Materials/Copper", "/Game/Materials/Steel", "/Game/Materials/Aluminium", "/Game/Materials/StainlessSteel", "/Game/Materials/Titanium", "/Game/Materials/HardMetal", "/Game/Materials/Neutronium")

covers = [
    {
        "Name": "CableSide",
        "Mesh": "/Game/Covers/PipeSide",
        "Materials": ["/Game/Materials/Rubber2"]
    },
    {
        "Name": "CableCenter",
        "Mesh": "/Game/Covers/PipeCenter",
        "Materials": ["/Game/Materials/Rubber2"]
    },{
        "Name": "HeatSide",
        "Mesh": "/Game/Covers/HeatSide",
        "Materials": ["/Game/Materials/HeatingCopper"]
    },{
        "Name": "HeatCenter",
        "Mesh": "/Game/Covers/HeatCenter",
        "Materials": ["/Game/Materials/HeatingCopper"]
    },{
		"Name": "Cover",
		"Mesh": "/Game/Covers/SimpleCover",
        "Materials": [""]
	},{
		"Name": "StoneFurnace",
		"Mesh": "/Game/019/FurnaceRound",
        "Materials": ["/Game/019/StoneFurnaceMaterial"]
	},{
		"Name": "RobotArmBase",
		"Mesh": "/Game/019/RobotArmBase",
        "Materials": []
	},{
		"Name": "BuildingBox",
		"Mesh": "/Game/BoxStaticMesh",
        "Materials": [],
        "NoCollision": True
	},{
		"Name": "ElectricityInput",
		"Mesh": "/Game/Covers/ElectricityIn",
        "NoCollision": True
	},{
		"Name": "ElectricityOutput",
		"Mesh": "/Game/Covers/ElectricityOut",
        "NoCollision": True
	},{
		"Name": "KineticInput",
		"Mesh": "/Game/Covers/KineticIn",
        "NoCollision": True
	},{
		"Name": "KineticOutput",
		"Mesh": "/Game/Covers/KineticOut",
        "NoCollision": True
	},{
		"Name": "HeatInput",
		"Mesh": "/Game/Covers/HeatIn",
        "NoCollision": True
	},{
		"Name": "HeatOutput",
		"Mesh": "/Game/Covers/HeatOut",
        "NoCollision": True
	},{
		"Name": "FluidInput",
		"Mesh": "/Game/Covers/FluidIn",
        "NoCollision": True
	},{
		"Name": "FluidOutput",
		"Mesh": "/Game/Covers/FluidOut",
        "NoCollision": True
	}
]

objects_array = []

for mat in paint_colors + paint_tiers:
	covers.append({
		"Name": "Cover" + mat,
		"Mesh": "/Game/Covers/SimpleCover",
        "Materials": [mat]
	})
     
for mat, num in zip(paint_tiers, range(0,7+1)):
    covers.append({
        "Name": mat+"PipeCenter",
        "Mesh": "/Game/Covers/PipeCenter",
        "Materials": ["/Game/Materials/"+mat]
    })
    covers.append({
        "Name": mat+"PipeSide",
        "Mesh": "/Game/Covers/PipeSide",
        "Materials": ["/Game/Materials/"+mat],
        "Item": mat+"Pipe"
    })
    covers.append({
        "Name": mat+"Corner",
        "Mesh": "/Game/CoreContent/Corner",
        "Materials": ["/Game/Materials/"+mat]
    })
    covers.append({
        "Name": mat+"Scaffold",
        "Mesh": "/Game/Models/Scafold",
        "Materials": ["/Game/Materials/"+mat]
    })

for mat, num in zip(paint_metals, range(1,7+1)):
    covers.append({
		"Name": mat+"Furnace",
		"Mesh": "/Game/019Content/FurnaceRound",
        "Materials": ["/Game/019/FurnaceMaterial"],
        "Tier": num
	})
    covers.append({
		"Name": mat+"Conveyor",
		"Mesh": "/Game/019/conveyor_end",
        "Materials": ["/Game/Materials/RubberWithTierParam", tier_materials[num]],
        "Tier": num
	})
    covers.append({
		"Name": mat+"ConveyorBox",
		"Mesh": "/Game/019/conveyor_box",
        "Materials": [tier_materials[num]],
        "Tier": num
	})
    covers.append({
		"Name": mat+"ElectricEngine",
		"Mesh": "/Game/019/ElectricEngine",
        "Materials": ["/Game/019/ElectricEngineMaterial"],
        "Tier": num
	})
	
for cover in covers:
    if "HasItem" in cover:
        objects_array.append({ "Class": "StaticItem",
            "Name": cover["Name"],
            
            "StackSize": 32,
            "Image": "T_" + cover["Name"],
            "ItemLogic": cover_item_logic,
            "Category": "Terrain",
            
            "LabelParts": [[cover["Name"], "props"]],
            "DescriptionParts":[["WorldObject","common"]],
        })
    staticCover = { "Class": static_cover,
        "Name": cover["Name"],
        "Mesh": cover["Mesh"]
    }
    if "Materials" in cover:
         staticCover["Materials"] = cover["Materials"]

    if "Tier" in cover:
        staticCover["Tier"] = cover["Tier"]

    if "NoCollision" in cover:
        staticCover["NoCollision"] = cover["NoCollision"]

    objects_array.append(staticCover)


data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/covers.json", data)