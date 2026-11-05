from Common import *

designables = [
	{
		"Name": "Stairs",
		"Category": "Decoration",
		"Label": ["Stairs", "misc"],
		"Selector": "Blocks/Stairs/BP_Stairs.BP_Stairs_C",
		"Covers": [
			"Stairs",
			"StairsGridLamp",
			"StairsGrid",
			"StairsFancy",
			"StairsTech",
			"StairsMinimal"
		]
	},{
		"Name": "Corner",
		"Category": "Decoration",
		"Label": ["Corner", "misc"],
		"Selector": "Blocks/Corner/BP_Corner.BP_Corner_C",
		"Covers": [
			"Corner",
			"PaintedCorner"
		]
	},{
		"Name": "Beam",
		"Category": "Decoration",
		"Label": ["Beam", "misc"],
		"Selector": "Blocks/Beam/BP_Beam.BP_Beam_C",
		"Covers": [
			"Beam",
			"PaintedBeam"
		]
	},{
		"Name": "Scaffold",
		"Category": "Decoration",
		"Label": ["Scaffold", "misc"],
		"Selector": "Blocks/Scaffold/BP_Scaffold.BP_Scaffold_C",
		"Covers": [
			"Scaffold",
			"PaintedScaffold"
		]
	},{
		"Name": "Column",
		"Category": "Decoration",
		"Label": ["Column", "misc"],
		"Selector": "Blocks/Column/BP_Column.BP_Column_C",
		"Covers": [
			"Column",
			"ThinColumn",
			"WideColumn",
			"NormalToThinColumn",
			"WideToNormalColumn"
		]
	},{
		"Name": "Floor",
		"Category": "Decoration",
		"Label": ["Floor", "misc"],
		"Selector": "Blocks/Floor/BP_Floor.BP_Floor_C",
		"Covers": [
			"ThinWireFloor",
			"Polycarbo",
			"RoofMetal"
		]
	},
	{
		"Name": "Chair",
		"Category": "Decoration",
		"Label": ["Chair", "misc"],
		"Selector": "Blocks/Chair/BP_Chair.BP_Chair_C",
		"Covers": [
			"Chair"
		]
	},
	{
		"Name": "Table",
		"Category": "Decoration",
		"Label": ["Table", "misc"],
		"Selector": "Blocks/Table/BP_Table.BP_Table_C",
		"Covers": [
			"Table"
		],
		"Positions": [[0,0,0], [-1,0,0]]
	},
	{
		"Name": "Fence",
		"Category": "Decoration",
		"Selector": "Blocks/Fence/BP_Fence.BP_Fence_C",
		"Label": ["Fence", "misc"],
		"Tier": 0,
		"BlockLogic": "DesignableFenceBlockLogic",
		"Covers": [
			"FenceHalf",
			"MetalFenceSideLamp"
		]
	}
]

ruins = [
	("AncientGate", (3, 1, 5), ["AncientGate"]),
	("AncientAltar", (2, 2, 2), ["AncientAltar"]),
	("AncientStele", (1, 1, 4), ["AncientStele"]),
	("AncientPillar", (1, 1, 4), ["AncientPillar"]),
]

design_covers = []

for name, (sx, sy, sz), meshes in ruins:
	cells = [[x - (sx - 1) // 2, y - (sy - 1) // 2, z] for z in range(sz) for y in range(sy) for x in range(sx)]
	cells.sort(key=lambda c: c != [0, 0, 0])
	offset = [0.5 if sx % 2 == 0 else 0, 0.5 if sy % 2 == 0 else 0, -0.5]
	for mesh in meshes:
		design_covers.append({
			"Class": "StaticCover",
			"Name": mesh,
			"Mesh": "/Game/Props/AncientRuin/" + mesh,
			"Offset": offset,
		})
	designables.append({
		"Name": name,
		"BlockLogic": "DesignPieceBlockLogic",
		"Covers": meshes,
		"Positions": cells,
	})

cover_sets = []
items = []
blocks = []

for d in designables:
	name = d["Name"]
	category = d.get("Category", "Decoration")
	label = d.get("Label", [name, "misc"])
	tier = d.get("Tier", 0)
	covers = d.get("Covers")
	block_logic = d.get("BlockLogic", "DesignableCoverBlockLogic")

	if covers:
		cover_sets.append({
			"Class": "StaticCoverSet",
			"Name": name,
			"Covers": covers
		})

	items.append({
		"Class": "StaticItem",
		"Name": name,
		"Block": name,
		"StackSize": 32,
		"ItemLogic": building_single_logic,
		"Category": category,
		"Label": label,
		"Image": "T_" + name,
		"Tier": tier
	})

	block = {
		"Class": "StaticBlock",
		"Name": name,
		"Item": name,
		"BlockLogic": block_logic,
		"NoActorRenderable": True,
		"Minable": decor_minable(3),
		"Tier": tier,
		"Level": 0
	}
	if covers:
		block["CoverSet"] = name
	if "Selector" in d:
		block["Selector"] = d["Selector"]
	if "Actor" in d:
		block["Actor"] = d["Actor"]
	if "Positions" in d:
		block["Positions"] = d["Positions"]

	blocks.append(block)

objects_array = design_covers + cover_sets + items + blocks

data = { "Objects": objects_array }

write_file("Generated/Mixed/designable_blocks.json", data)


