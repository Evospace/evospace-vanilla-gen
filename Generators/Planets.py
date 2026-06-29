# StaticPlanet prototypes per playable surface (name matches ADimension::SurfaceFolderName for DB lookup).

from Common import write_file

# Temperate: default surface folder; day length and anchors in world tick space (evo::WorldDayCycle).
objects_array = [
	{
		"Class": "StaticPlanet",
		"Name": "Temperate",
		"DayLengthTicks": 144000,
		# Epoch shift so game tick 0 lands at 07:00 morning (7/24 * 144000). No per-save offset / time skip needed.
		"PhaseOffsetTicks": 42000,
		"DawnPhaseTicks": 24000,
		"SolarNoonPhaseTicks": 72000,
		"SunsetPhaseTicks": 120000,
	},
]

data = {"Objects": objects_array}

write_file("Generated/Resources/planets.json", data)
