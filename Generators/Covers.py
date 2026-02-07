from Common import *

paint_colors = ("PaintYellow",)
paint_metals = ("Copper", "Steel", "Aluminium", "StainlessSteel", "Titanium", "Composite", "Neutronium")
paint_tiers = ("Stone", "Copper", "Steel", "Aluminium", "StainlessSteel", "Titanium", "Composite", "Neutronium")
tier_materials = ("/Game/Materials/Stone", "/Game/Materials/Copper", "/Game/Materials/Steel", "/Game/Materials/Aluminium", "/Game/Materials/StainlessSteel", "/Game/Materials/Titanium", "/Game/Materials/Composite", "/Game/Materials/Neutronium")

covers = [
    {
        "Name": "CableSide",
        "Mesh": "/Game/Covers/CableSide",
        "Materials": ["/Game/Materials/Rubber2", "/Game/Materials/Copper"]
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
		"Mesh": "/Game/Models/FurnaceRound",
        "Materials": ["/Game/Materials/StoneFurnaceMaterial"]
	},{
		"Name": "RobotArmBase",
		"Mesh": "/Game/Models/RobotArmBase",
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
	},{
		"Name": "FluidOutput1",
		"Mesh": "/Game/Covers/FluidOut1",
        "NoCollision": True
	},{
		"Name": "FluidOutput2",
		"Mesh": "/Game/Covers/FluidOut2",
        "NoCollision": True
	},{
		"Name": "FluidOutput3",
		"Mesh": "/Game/Covers/FluidOut3",
        "NoCollision": True
	},{
		"Name": "FluidOutput4",
		"Mesh": "/Game/Covers/FluidOut4",
        "NoCollision": True
	},{
		"Name": "FluidInput1",
		"Mesh": "/Game/Covers/FluidIn1",
        "NoCollision": True
	},{
		"Name": "FluidInput2",
		"Mesh": "/Game/Covers/FluidIn2",
        "NoCollision": True
	},{
		"Name": "Stairs",
		"Mesh": "/Game/Covers/Stairs",
        "NumCustomData": 3,
	},{
        "Name": "Corner",
        "Mesh": "/Game/Covers/Corner",
        "Materials": ["/Game/Materials/Steel_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "PaintedCorner",
        "Mesh": "/Game/Covers/Corner",
        "Materials": ["/Game/Materials/Paint_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "Beam",
        "Mesh": "/Game/Covers/Beam",
        "Materials": ["/Game/Materials/Steel_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "PaintedBeam",
        "Mesh": "/Game/Covers/Beam",
        "Materials": ["/Game/Materials/Paint_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "Scaffold",
        "Mesh": "/Game/Covers/Scaffold",
        "Materials": ["/Game/Materials/Steel_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "PaintedScaffold",
        "Mesh": "/Game/Covers/Scaffold",
        "Materials": ["/Game/Materials/Paint_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "Chair",
        "Mesh": "/Game/Covers/Chair",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "Table",
        "Mesh": "/Game/Covers/Table",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "StairsGridLamp",
        "Mesh": "/Game/Covers/StairsGridLamp",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "StairsGrid",
        "Mesh": "/Game/Covers/StairsGrid",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "StairsFancy",
        "Mesh": "/Game/Covers/StairsFancy",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "StairsTech",
        "Mesh": "/Game/Covers/StairsTech",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "StairsMinimal",
        "Mesh": "/Game/Covers/StairsMinimal",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "FenceHalf",
        "Mesh": "/Game/Covers/FenceHalf",
        "NumCustomData": 3,
    },{
        "Name": "FenceCenter",
        "Mesh": "/Game/Covers/FenceCenter",
        "NumCustomData": 3,
    },{
        "Name": "MetalFenceSideLamp",
        "Mesh": "/Game/Covers/MetalFenceSideLamp",
        "NumCustomData": 3,
    },{
        "Name": "Column",
        "Mesh": "/Game/Covers/Column",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "WideColumn",
        "Mesh": "/Game/Covers/WideColumn",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "ThinColumn",
        "Mesh": "/Game/Covers/ThinColumn",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "WideToNormalColumn",
        "Mesh": "/Game/Covers/WideToNormalColumn",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "NormalToThinColumn",
        "Mesh": "/Game/Covers/NormalToThinColumn",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "ThinWireFloor",
        "Mesh": "/Game/Covers/ThinWireFloor",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "WireCover",
        "Mesh": "/Game/Covers/WireCover",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "Polycarbo",
        "Mesh": "/Game/Covers/polycarbo",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "RoofMetal",
        "Mesh": "/Game/Covers/polycarbo",
        "Materials": ["/Game/Materials/RoofMetal"],
        "NumCustomData": 3,
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

for mat, num in zip(paint_metals, range(1,7+1)):
    covers.append({
		"Name": mat+"Furnace",
		"Mesh": "/Game/Models/FurnaceRound",
        "Materials": ["/Game/Models/FurnaceMaterial"]
	})
    covers.append({
		"Name": mat+"Conveyor",
		"Mesh": "/Game/Models/conveyor_end",
        "Materials": ["/Game/Materials/RubberWithTierParam", tier_materials[num]]
	})
    covers.append({
		"Name": mat+"ConveyorBox",
		"Mesh": "/Game/Models/conveyor_box",
        "Materials": [tier_materials[num]]
	})
    covers.append({
		"Name": mat+"ElectricEngine",
		"Mesh": "/Game/Models/ElectricEngine",
        "Materials": ["/Game/Materials/ElectricEngineMaterial"]
	})
	
for cover in covers:
    if "HasItem" in cover:
        objects_array.append({ "Class": "StaticItem",
            "Name": cover["Name"],
            "StackSize": 32,
            "Image": "T_" + cover["Name"],
            "ItemLogic": cover_item_logic,
            "Category": "Terrain",
            "Label": [cover["Name"], "props"],
            "DescriptionParts":[["WorldObject","common"]],
        })
    staticCover = { "Class": static_cover,
        "Name": cover["Name"],
        "Mesh": cover["Mesh"]
    }
    
    if "Materials" in cover:
         staticCover["Materials"] = cover["Materials"]

    if "NumCustomData" in cover:
         staticCover["NumCustomData"] = cover["NumCustomData"]
         # Auto-fill DefaultColors if not specified: one white RGB per slot
         if "DefaultColors" in cover:
             staticCover["DefaultColors"] = cover["DefaultColors"]
         else:
             slots = max(1, int(cover["NumCustomData"] // 3))
             staticCover["DefaultColors"] = [[1,1,1] for _ in range(slots)]

    if "NoCollision" in cover:
        staticCover["NoCollision"] = cover["NoCollision"]

    objects_array.append(staticCover)


data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/covers.json", data)