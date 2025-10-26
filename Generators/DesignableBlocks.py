from Common import *

# Universal generator for designable blocks (use UDesignableCoverBlockLogic).
# Configure blocks below; each entry may specify a custom covers list.

designables = [
	{
		"Name": "Stairs",
		"Category": "Terrain",
		"Label": ["Stairs", "blocks"],
		"Selector": "Blocks/StairsBP.StairsBP_C",
		"Covers": [
			"Stairs",
			"WireCover",
			"WireCover"
		]
	},
	{
		"Name": "Ladder",
		"Category": "Terrain",
		"Label": ["Ladder", "blocks"],
		"Selector": "Blocks/StairsBP.StairsBP_C",
		"Covers": [
			"WireCover"
		]
	},
	{
		"Name": "Chair",
		"Category": "Terrain",
		"Label": ["Chair", "blocks"],
		"Selector": "Blocks/StairsBP.StairsBP_C",
		"Covers": [
			"WireCover"
		]
	},
	{
		"Name": "Table",
		"Category": "Terrain",
		"Label": ["Table", "blocks"],
		"Selector": "Blocks/StairsBP.StairsBP_C",
		"Covers": [
			"WireCover"
		]
	}
]

objects_array = []

for d in designables:
	name = d["Name"]
	covers = d.get("Covers", ["Cover"])  # fallback to basic cover
	category = d.get("Category", "Terrain")
	label = d.get("Label", [name, "misc"])

	# StaticCoverSet defining the available designs
	objects_array.append({
		"Class": "StaticCoverSet",
		"Name": name,
		"Covers": covers
	})

	# Placement item stub
	objects_array.append({
		"Class": "StaticItem",
		"Name": name,
		"Block": name,
		"StackSize": 32,
		"ItemLogic": building_single_logic,
		"Category": category,
		"Label": label
	})

	# Block prototype with designable cover logic
	block = {
		"Class": "StaticBlock",
		"Name": name,
		"Item": name,
		"BlockLogic": "DesignableCoverBlockLogic",
		"CoverSet": name,
		"NoActorRenderable": True,
		"Minable": { "Result": name },
		"Tier": 0,
		"Level": 0
	}
	if "Selector" in d:
		block["Selector"] = d["Selector"]
	objects_array.append(block)

data = { "Objects": objects_array }

# Single consolidated output; extend 'designables' above to add more blocks.
write_file("Generated/Mixed/designable_blocks.json", data)


