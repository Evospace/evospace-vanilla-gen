from Common import *

designables = [
	{
		"Name": "Stairs",
		"Category": "Decoration",
		"Label": ["Stairs", "misc"],
		"Selector": "Blocks/StairsBP.StairsBP_C",
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
		"Selector": "Blocks/ScaffoldBP.ScaffoldBP_C",
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
		"Selector": "Blocks/FenceBP.FenceBP_C",
		"Label": ["Fence", "misc"],
		"Tier": 0,
		"BlockLogic": "DesignableFenceBlockLogic",
		"Covers": [
			"FenceHalf",
			"MetalFenceSideLamp"
		]
	}
]

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

objects_array = cover_sets + items + blocks

data = { "Objects": objects_array }

write_file("Generated/Mixed/designable_blocks.json", data)


