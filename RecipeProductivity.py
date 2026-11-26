from ItemTiers import iter_objects, item_names

BUILTIN_PRODUCTIVITY = {
	"AutomaticHammerRecipeDictionary",
	"OreWasherRecipeDictionary",
	"SifterRecipeDictionary",
	"SeparatorRecipeDictionary",
	"MaceratorRecipeDictionary",
	"ArcSmelterRecipeDictionary",
}

INTERMEDIATE_CATEGORIES = {"Parts", "Plate", "Dust", "Ore", "Chemical"}

GROUND_BACK_CATEGORIES = {"Parts", "Plate"}


def mark_allow_productivity(generated_files):
	objects = list(iter_objects(generated_files))
	category = {obj["Name"]: obj.get("Category") for obj in objects if obj.get("Class") == "StaticItem"}

	def intermediate(recipe):
		outputs = item_names(recipe.get("Output"))
		return bool(outputs) and all(category.get(name) in INTERMEDIATE_CATEGORIES for name in outputs)

	def grinds_back(recipe):
		inputs = item_names(recipe.get("Input"))
		outputs = item_names(recipe.get("Output"))
		return (bool(outputs) and all(category.get(name) == "Dust" for name in outputs)
			and any(category.get(name) in GROUND_BACK_CATEGORIES for name in inputs))

	marked = total = 0
	for obj in objects:
		if obj.get("Class") != "RecipeDictionary":
			continue
		builtin = obj["Name"] in BUILTIN_PRODUCTIVITY
		for recipe in obj.get("Recipes") or []:
			total += 1
			if "AllowProductivity" not in recipe and not grinds_back(recipe) and (builtin or intermediate(recipe)):
				recipe["AllowProductivity"] = True
			if recipe.get("AllowProductivity"):
				marked += 1
	return marked, total
