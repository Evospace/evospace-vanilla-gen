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
	},
	{
		"Class": "StaticPlanet",
		"Name": "Moon",
		"DayLengthTicks": 708000,
		"PhaseOffsetTicks": 0,
		"DawnPhaseTicks": 118000,
		"SolarNoonPhaseTicks": 354000,
		"SunsetPhaseTicks": 590000,
	},
]

data = {"Objects": objects_array}

write_file("Generated/Resources/planets.json", data)
