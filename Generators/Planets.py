# StaticPlanet prototypes per playable surface (name matches ADimension::SurfaceFolderName for DB lookup).

from Common import write_file

# Temperate: default surface folder; day length and anchors in world tick space (evo::WorldDayCycle).
objects_array = [
	{
		"Class": "StaticPlanet",
		"Name": "Temperate",
		# 24000 ticks / 20 TickRate = 1200 s = 20 min real-time day.
		"DayLengthTicks": 24000,
		# Epoch shift so game tick 0 lands at 07:00 morning (7/24 * 24000). No per-save offset / time skip needed.
		"PhaseOffsetTicks": 7000,
		"DawnPhaseTicks": 4000,
		"SolarNoonPhaseTicks": 12000,
		"SunsetPhaseTicks": 20000,
		"LatitudeDeg": 52.0,
		"DayOfYear": 172,
		"OvercastInsolation01": 0.15,
		"RadiusMeters": 600000.0,
		"OrbitAltitudeMeters": 100000.0,
		# Seen from the platform: GPU-baked noise planet, colours are linear albedo.
		"OrbitLook": {
			"Seed": 7347,
			"Ocean": True,
			"SeaLevel": 0.02,
			"LandHeight": 900.0,
			"MountainHeight": 3500.0,
			"SeaDepth": 5000.0,
			"Warmth": 0.0,
			"Sand": [0.46, 0.40, 0.29],
			"Desert": [0.52, 0.38, 0.24],
			"Savanna": [0.30, 0.27, 0.13],
			"Grass": [0.10, 0.17, 0.05],
			"Forest": [0.035, 0.075, 0.028],
			"Taiga": [0.045, 0.065, 0.045],
			"Tundra": [0.20, 0.20, 0.16],
			"Rock": [0.19, 0.17, 0.15],
			"Snow": [0.86, 0.88, 0.92],
			"ShallowSea": [0.020, 0.085, 0.095],
			"DeepSea": [0.006, 0.020, 0.045],
			"Ice": [0.70, 0.78, 0.86],
			"Atmosphere": True,
			"AirTint": [0.175287, 0.409607, 1.0],
			"AirDensity": 0.5,
			"AirHeightInRadii": 0.12,
			"Clouds": True,
			"CloudCover": 0.45,
			"StormInRadii": 0.35,
		},
		"FarMap": {
			"Material": "/Game/Materials/FarMap/M_FarMap.M_FarMap",
			"Layers": ["L_BasaltTop", "L_Bog", "L_DarkStone", "L_DesertSand", "L_DryGrass", "L_Grass",
			           "L_Gravel", "L_Peat", "L_PineForest", "L_Sand", "L_Snow", "L_Stone"],
			"Materials": {
				"BasaltMaterial": "L_BasaltTop",
				"BogMaterial": "L_Bog",
				"DarkStoneMaterial": "L_DarkStone",
				"DesertSandMaterial": "L_DesertSand",
				"DryGrassMaterial": "L_DryGrass",
				"GrassMaterial": "L_Grass",
				"GravelMaterial": "L_Gravel",
				"PeatMaterial": "L_Peat",
				"PineForestMaterial": "L_PineForest",
				"SandMaterial": "L_Sand",
				"SnowMaterial": "L_Snow",
				"StoneMaterial": "L_Stone",
				"ClayMaterial": "L_Peat",
				"DirtMaterial": "L_Peat",
			},
		},
	},
	{
		"Class": "StaticPlanet",
		"Name": "Moon",
		"DayLengthTicks": 708000,
		"PhaseOffsetTicks": 0,
		"DawnPhaseTicks": 118000,
		"SolarNoonPhaseTicks": 354000,
		"SunsetPhaseTicks": 590000,
		"LatitudeDeg": 0.0,
		"DayOfYear": 172,
		# No atmosphere: cloud cover never dims the sun.
		"OvercastInsolation01": 1.0,
		"GeneratorName": "WorldGeneratorMoon",
		"MusicPlaylist": "cosmos",
		"RadiusMeters": 170000.0,
		"OrbitAltitudeMeters": 30000.0,
		# Airless grey body: craters and maria baked by their own shader, no water, no air.
		"OrbitLook": {
			"BakeMaterial": "/Game/Materials/M_MoonSurfaceBake.M_MoonSurfaceBake",
			"Seed": 5507,
			"Ocean": False,
			"Regolith": True,
			"Atmosphere": False,
			"Clouds": False,
		},
		"FarMap": {
			"Material": "/Game/Materials/FarMap/Moon/MI_FarMapMoon.MI_FarMapMoon",
			"Layers": ["L_MoonHighland", "L_MoonMare"],
			"Materials": {
				"LimestoneMaterial": "L_MoonHighland",
				"BasaltMaterial": "L_MoonMare",
			},
		},
	},
	{
		"Class": "StaticPlanet",
		"Name": "Orbit",
		"DayLengthTicks": 24000,
		"PhaseOffsetTicks": 7000,
		"DawnPhaseTicks": 4000,
		"SolarNoonPhaseTicks": 12000,
		"SunsetPhaseTicks": 20000,
		"LatitudeDeg": 52.0,
		"DayOfYear": 172,
		"OvercastInsolation01": 1.0,
		"WeatherSeverityMin": 0.0,
		"WeatherSeverityMax": 0.0,
		"GeneratorName": "WorldGeneratorOrbit",
		"MusicPlaylist": "cosmos",
	},
]

data = {"Objects": objects_array}

write_file("Generated/Resources/planets.json", data)
