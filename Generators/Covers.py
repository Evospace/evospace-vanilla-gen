from Common import *

paint_colors = ("PaintYellow",)
paint_metals = ("Copper", "Steel", "Aluminium", "StainlessSteel", "Titanium", "Composite", "Neutronium")
paint_tiers = ("Stone", "Copper", "Steel", "Aluminium", "StainlessSteel", "Titanium", "Composite", "Neutronium")
tier_materials = ("/Game/Materials/Stone", "/Game/Materials/Copper", "/Game/Materials/Steel", "/Game/Materials/Aluminium", "/Game/Materials/StainlessSteel", "/Game/Materials/Titanium", "/Game/Materials/Composite", "/Game/Materials/Neutronium")

covers = [
    {
        "Name": "CableSide",
        "Mesh": "/Game/Blocks/CopperConnector/SM_CopperConnector_Side",
        "Materials": ["/Game/Materials/Rubber2", "/Game/Materials/Copper"],
        "MergedShadow": True
    },
    {
        "Name": "CableCenter",
        "Mesh": "/Game/Shared/Blocks/SM_Connector_Center",
        "Materials": ["/Game/Materials/Rubber2"],
        "MergedShadow": True
    },{
        "Name": "HeatSide",
        "Mesh": "/Game/Blocks/HeatPipe/SM_HeatPipe_Side",
        "Materials": ["/Game/Materials/HeatingCopper"]
    },{
        "Name": "HeatCenter",
        "Mesh": "/Game/Blocks/HeatPipe/SM_HeatPipe_Center",
        "Materials": ["/Game/Materials/HeatingCopper"]
    },{
		"Name": "Cover",
		"Mesh": "/Game/Shared/Covers/SM_Cover_Simple",
        "Materials": [""]
	},{
		"Name": "StoneFurnace",
		"Mesh": "/Game/Blocks/Furnace/SM_Furnace",
        "Materials": ["/Game/Blocks/Furnace/M_Furnace_Stone"]
	},{
		"Name": "RobotArmBase",
		"Mesh": "/Game/Shared/Blocks/SM_RobotArm_Base",
        "Materials": []
	},{
		"Name": "ElectricityInput",
		"Mesh": "/Game/Shared/Covers/SM_Port_ElectricityIn",
        "NoCollision": True
	},{
		"Name": "ElectricityOutput",
		"Mesh": "/Game/Shared/Covers/SM_Port_ElectricityOut",
        "NoCollision": True
	},{
		"Name": "KineticInput",
		"Mesh": "/Game/Shared/Covers/SM_Port_KineticIn",
        "NoCollision": True
	},{
		"Name": "KineticOutput",
		"Mesh": "/Game/Shared/Covers/SM_Port_KineticOut",
        "NoCollision": True
	},{
		"Name": "HeatInput",
		"Mesh": "/Game/Shared/Covers/SM_Port_HeatIn",
        "NoCollision": True
	},{
		"Name": "HeatOutput",
		"Mesh": "/Game/Shared/Covers/SM_Port_HeatOut",
        "NoCollision": True
	},{
		"Name": "ItemOutput",
		"Mesh": "/Game/Shared/Covers/SM_Port_ItemOut",
        "NoCollision": True
	},{
		"Name": "FluidInput",
		"Mesh": "/Game/Shared/Covers/SM_Port_FluidIn",
        "NoCollision": True
	},{
		"Name": "FluidOutput",
		"Mesh": "/Game/Shared/Covers/SM_Port_FluidOut",
        "NoCollision": True
	},{
		"Name": "FluidOutput1",
		"Mesh": "/Game/Shared/Covers/SM_Port_FluidOut1",
        "NoCollision": True
	},{
		"Name": "FluidOutput2",
		"Mesh": "/Game/Shared/Covers/SM_Port_FluidOut2",
        "NoCollision": True
	},{
		"Name": "FluidOutput3",
		"Mesh": "/Game/Shared/Covers/SM_Port_FluidOut3",
        "NoCollision": True
	},{
		"Name": "FluidOutput4",
		"Mesh": "/Game/Shared/Covers/SM_Port_FluidOut4",
        "NoCollision": True
	},{
		"Name": "FluidInput1",
		"Mesh": "/Game/Shared/Covers/SM_Port_FluidIn1",
        "NoCollision": True
	},{
		"Name": "FluidInput2",
		"Mesh": "/Game/Shared/Covers/SM_Port_FluidIn2",
        "NoCollision": True
	},{
		"Name": "Stairs",
		"Mesh": "/Game/Shared/Blocks/SM_Stairs",
        "NumCustomData": 3,
	},{
        "Name": "Corner",
        "Mesh": "/Game/Blocks/Corner/SM_Corner",
        "Materials": ["/Game/Materials/Steel_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "PaintedCorner",
        "Mesh": "/Game/Blocks/Corner/SM_Corner",
        "Materials": ["/Game/Materials/Paint_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "Beam",
        "Mesh": "/Game/Blocks/Beam/SM_Beam",
        "Materials": ["/Game/Materials/Steel_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "PaintedBeam",
        "Mesh": "/Game/Blocks/Beam/SM_Beam",
        "Materials": ["/Game/Materials/Paint_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "Scaffold",
        "Mesh": "/Game/Blocks/Scaffold/SM_Scaffold",
        "Materials": ["/Game/Materials/Steel_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "PaintedScaffold",
        "Mesh": "/Game/Blocks/Scaffold/SM_Scaffold",
        "Materials": ["/Game/Materials/Paint_InstanceColor_0"],
        "NumCustomData": 3,
    },{
        "Name": "Chair",
        "Mesh": "/Game/Blocks/Chair/SM_Chair",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "Table",
        "Mesh": "/Game/Blocks/Table/SM_Table",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "StairsGridLamp",
        "Mesh": "/Game/Blocks/Stairs/SM_Stairs_GridLamp",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "StairsGrid",
        "Mesh": "/Game/Blocks/Stairs/SM_Stairs_Grid",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "StairsFancy",
        "Mesh": "/Game/Blocks/Stairs/SM_Stairs_Fancy",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "StairsTech",
        "Mesh": "/Game/Blocks/Stairs/SM_Stairs_Tech",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "StairsMinimal",
        "Mesh": "/Game/Blocks/Stairs/SM_Stairs_Minimal",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "FenceHalf",
        "Mesh": "/Game/Blocks/Fence/SM_Fence_Half",
        "NumCustomData": 3,
    },{
        "Name": "FenceCenter",
        "Mesh": "/Game/Blocks/Fence/SM_Fence_Center",
        "NumCustomData": 3,
    },{
        "Name": "MetalFenceSideLamp",
        "Mesh": "/Game/Blocks/Fence/SM_Fence_SideLamp",
        "NumCustomData": 3,
    },{
        "Name": "Column",
        "Mesh": "/Game/Blocks/Column/SM_Column_Normal",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "WideColumn",
        "Mesh": "/Game/Blocks/Column/SM_Column_Wide",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "ThinColumn",
        "Mesh": "/Game/Blocks/Column/SM_Column_Thin",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "WideToNormalColumn",
        "Mesh": "/Game/Blocks/Column/SM_Column_WideToNormal",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "NormalToThinColumn",
        "Mesh": "/Game/Blocks/Column/SM_Column_NormalToThin",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "ThinWireFloor",
        "Mesh": "/Game/Blocks/Floor/SM_Floor_ThinWire",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "RailNode",
        "Mesh": "/Game/Blocks/RailNode/SM_RailNode",
    },{
        "Name": "FoundationTop",
        "Mesh": "/Game/Shared/Stands/SM_Stand_Top",
    },{
        "Name": "FoundationColumn",
        "Mesh": "/Game/Shared/Stands/SM_Stand_Column",
    },{
        "Name": "FoundationHeavyTop",
        "Mesh": "/Game/Shared/Stands/SM_Stand_HeavyTop",
    },{
        "Name": "FoundationHeavyColumn",
        "Mesh": "/Game/Shared/Stands/SM_Stand_HeavyColumn",
    },{
        "Name": "FoundationPipeHolder",
        "Mesh": "/Game/Shared/Stands/SM_Stand_PipeHolder",
    },{
        "Name": "FoundationPipePost",
        "Mesh": "/Game/Shared/Stands/SM_Stand_PipePost",
    },{
        "Name": "WireCover",
        "Mesh": "/Game/Shared/Covers/SM_Cover_Wire",
        "Materials": [""],
        "NumCustomData": 3,
        "Minable": decor_minable(1),
    },{
        "Name": "Polycarbo",
        "Mesh": "/Game/Blocks/Floor/SM_Floor_Polycarbo",
        "Materials": [""],
        "NumCustomData": 3,
    },{
        "Name": "RoofMetal",
        "Mesh": "/Game/Blocks/Floor/SM_Floor_Polycarbo",
        "Materials": ["/Game/Blocks/Floor/M_Floor_RoofMetal"],
        "NumCustomData": 3,
    },{
        "Name": "DataSide",
        "Mesh": "/Game/Blocks/LogicWire/SM_LogicWire_Side",
        "Materials": [""],
        "NumCustomData": 0,
        "MergedShadow": True,
    },{
        "Name": "DataCenter",
        "Mesh": "/Game/Blocks/LogicWire/SM_LogicWire_Center",
        "Materials": [""],
        "NumCustomData": 0,
        "MergedShadow": True,
    }
]

objects_array = []

for mat in paint_colors + paint_tiers:
	covers.append({
		"Name": "Cover" + mat,
		"Mesh": "/Game/Shared/Covers/SM_Cover_Simple",
        "Materials": [mat]
	})
     
battery_pieces = {
    "Single": ["Body", "Frame", "Copper", "Insulator"],
    "Top": ["Body", "Frame", "Copper", "Insulator"],
    "Bottom": ["Body", "Frame", "Insulator"],
    "Middle": ["Body", "Frame", "Insulator"],
}

for mat in paint_tiers[3:]:
    for piece, slots in battery_pieces.items():
        covers.append({
            "Name": mat + "BatteryBox" + piece,
            "Mesh": "/Game/Blocks/BatteryBox/SM_BatteryBox_" + piece,
            "Materials": ["", "/Game/Materials/" + mat, "", ""]
        })

tank_pieces = {
    "Single": ["Body", "Frame", "Fitting", "Insulator"],
    "Top": ["Body", "Frame", "Fitting", "Insulator"],
    "Bottom": ["Body", "Frame", "Fitting", "Insulator"],
    "Middle": ["Body", "Frame"],
}

for mat in paint_tiers[1:]:
    for piece, slots in tank_pieces.items():
        covers.append({
            "Name": mat + "Container" + piece,
            "Mesh": "/Game/Blocks/Container/SM_Container_" + piece,
            "Materials": ["/Game/Materials/" + mat, ""]
        })

pipe_fitting_material = "/Game/Materials/GraySteel"
pipe_pieces = ("Arm", "Center", "StraightSingleFlange", "StraightNoFlanges", "Elbow", "DeadEnd", "Isolated")

for mat, num in zip(paint_tiers, range(0,7+1)):
    for piece in pipe_pieces:
        covers.append({
            "Name": mat+"Pipe"+piece,
            "Mesh": "/Game/Blocks/Pipe/SM_Pipe_"+piece,
            "Materials": ["/Game/Materials/"+mat, pipe_fitting_material],
            "MergedShadow": True
        })

conveyor_node_pieces = ("Core", "Input", "Output", "Window")

for mat, num in zip(paint_metals, range(1,7+1)):
    for piece in conveyor_node_pieces:
        covers.append({
            "Name": mat+"ConveyorNode"+piece,
            "Mesh": "/Game/Blocks/Conveyor/SM_Conveyor_Node"+piece,
            "Materials": [tier_materials[num]],
            "MergedShadow": True
        })

for mat, num in zip(paint_metals, range(1,7+1)):
    covers.append({
		"Name": mat+"Furnace",
		"Mesh": "/Game/Blocks/Furnace/SM_Furnace",
        "Materials": ["/Game/Models/FurnaceMaterial"]
	})
    covers.append({
		"Name": mat+"Conveyor",
		"Mesh": "/Game/Blocks/Conveyor/SM_Conveyor_End",
        "Materials": ["/Game/Blocks/Conveyor/M_Conveyor_RubberTier", tier_materials[num]],
        "MergedShadow": True
	})
    covers.append({
		"Name": mat+"ConveyorSide",
		"Mesh": "/Game/Blocks/Conveyor/SM_Conveyor_Side",
        "Materials": ["/Game/Blocks/Conveyor/M_Conveyor_RubberTier", tier_materials[num]],
        "MergedShadow": True
	})
    covers.append({
		"Name": mat+"ElectricEngine",
		"Mesh": "/Game/Blocks/ElectricEngine/SM_ElectricEngine",
        "Materials": ["/Game/Blocks/ElectricEngine/M_ElectricEngine"]
	})

for mat, num in zip(paint_metals, range(1,7+1)):
    covers.append({
		"Name": mat+"SolarPanelBase",
		"Mesh": "/Game/Blocks/SolarPanel/SM_SolarPanel_Base",
        "Materials": ["/Game/Materials/PaintDarkGray", tier_materials[num], "/Game/Materials/PaintYellow", "/Game/Materials/Accessor"],
        "NoCollision": True
	})
    covers.append({
		"Name": mat+"SolarPanelCell",
		"Mesh": "/Game/Blocks/SolarPanel/SM_SolarPanel_Cell",
        "Materials": ["/Game/Blocks/SolarPanel/M_SolarPanel_Tracking"],
        "NoCollision": True,
        "WorldPositionOffsetDisableDistance": 20000
	})
    covers.append({
		"Name": mat+"SmallSolarPanelCell",
		"Mesh": "/Game/Blocks/SmallSolarPanel/SM_SmallSolarPanel",
        "Materials": ["/Game/Materials/PaintYellow", "/Game/Materials/solar", tier_materials[num], "/Game/Materials/Accessor", "/Game/Materials/Rubber2"],
        "NoCollision": True
	})
    covers.append({
		"Name": mat+"WindTurbineMast",
		"Mesh": "/Game/Blocks/WindTurbine/SM_WindTurbine_Mast",
        "Materials": [tier_materials[num]],
        "NoCollision": True
	})
    covers.append({
		"Name": mat+"WindTurbineRotor",
		"Mesh": "/Game/Blocks/WindTurbine/SM_WindTurbine_Rotor",
        "Materials": ["/Game/Materials/WindTurbineRotorSpin", tier_materials[num]],
        "NoCollision": True,
        "WorldPositionOffsetDisableDistance": 40000
	})
    covers.append({
		"Name": mat+"WindTurbineStator",
		"Mesh": "/Game/Blocks/WindTurbine/SM_WindTurbine_Stator",
        "Materials": ["/Game/Blocks/WindTurbine/M_WindTurbine_Stator"],
        "NoCollision": True,
        "WorldPositionOffsetDisableDistance": 40000
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
         if "DefaultColors" in cover:
             staticCover["DefaultColors"] = cover["DefaultColors"]
         else:
             slots = max(1, int(cover["NumCustomData"] // 3))
             staticCover["DefaultColors"] = [[1,1,1] for _ in range(slots)]

    if "NoCollision" in cover:
        staticCover["NoCollision"] = cover["NoCollision"]

    if "MergedShadow" in cover:
        staticCover["MergedShadow"] = cover["MergedShadow"]

    if "WorldPositionOffsetDisableDistance" in cover:
        staticCover["WorldPositionOffsetDisableDistance"] = cover["WorldPositionOffsetDisableDistance"]

    if "Minable" in cover:
        staticCover["Minable"] = cover["Minable"]

    objects_array.append(staticCover)


data = {
	"Objects": objects_array
}

write_file("Generated/Mixed/covers.json", data)