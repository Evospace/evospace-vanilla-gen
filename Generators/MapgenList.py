def triplanar_material(name):
	return "/Game/Materials/Triplanar/" + name + "Material"


mapgen_objects = [
	{
		"Name": "Sand",
		"Drops": "Sand",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/SandBreakEffect.SandBreakEffect_C"
	},{
		"Name": "Sandstone",
		"Drops": "Sand",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/SandBreakEffect.SandBreakEffect_C"
	},{
		"Name": "Stone",
		"Drops": "Stone",
		"Hardness": 2
	},{
		"Name": "DesertSand",
		"Drops": "Sand",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/SandBreakEffect.SandBreakEffect_C"
	},{
		"Name": "Grass",
		"Drops": "Dirt",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/DirtBreakEffect.DirtBreakEffect_C"
	},{
		"Name": "Lava",
		"Drops": "Basalt",
		"Hardness": 5
	},{
		"Name": "Basalt",
		"Drops": "Basalt",
		"Hardness": 2
	},{
		"Name": "Bog",
		"Drops": "Dirt",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/DirtBreakEffect.DirtBreakEffect_C"
	},{
		"Name": "PineForest",
		"Drops": "Dirt",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/DirtBreakEffect.DirtBreakEffect_C"
	},{
		"Name": "Dirt",
		"Drops": "Dirt",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/DirtBreakEffect.DirtBreakEffect_C"
	},{
		"Name": "Gravel",
		"Drops": "Gravel",
		"Hardness": 1
	},{
		"Name": "DryGrass",
		"Drops": "Dirt",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/DirtBreakEffect.DirtBreakEffect_C"
	},{
		"Name": "SandyDryGrass",
		"Drops": "Sand",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/SandBreakEffect.SandBreakEffect_C"
	},{
		"Name": "Clay",
		"Drops": "Sand",
		"Hardness": 1.0,
		"BreakEffect": "/Game/EffectActors/ClayBreakEffect.ClayBreakEffect_C"
	},{
		"Name": "Limestone",
		"Drops": "Gravel",
		"Hardness": 1.5
	},{
		"Name": "RedStone",
		"Drops": "RedStone",
		"Hardness": 2
	},{
		"Name": "DarkStone",
		"Drops": "DarkStone",
		"Hardness": 2
	},{
		"Name": "Snow",
		"Drops": "Snow",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/SnowBreakEffect.SnowBreakEffect_C"
	},{
		"Name": "Granite",
		"Drops": "Granite",
		"Hardness": 4,
		"Unbreakable": True
	},{
		"Name": "Peat",
		"Drops": "Peat",
		# Drop the material StaticItem (fuel/tooltip from PartsGen), not PeatSurface
		"MineResult": "Peat",
		"Hardness": 1,
		"BreakEffect": "/Game/EffectActors/PeatBreakEffect.PeatBreakEffect_C"
	},
]
