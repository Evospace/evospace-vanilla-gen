import importlib.util
import os
import sys


def iter_objects(data):
	objects = data.get("Objects", [])
	if isinstance(objects, list):
		for obj in objects:
			if isinstance(obj, dict):
				yield obj


def collect_item_tiers(generated_files):
	item_tiers = {}
	for data in generated_files.values():
		if not isinstance(data, dict):
			continue
		for obj in iter_objects(data):
			name = obj.get("Name")
			tier = obj.get("Tier")
			if name is None or tier is None:
				continue
			item_tiers[name] = tier
	return item_tiers


def extract_item_names(io_block):
	if not isinstance(io_block, dict):
		return []
	items = io_block.get("Items")
	if not isinstance(items, list):
		return []
	names = []
	for entry in items:
		if not isinstance(entry, dict):
			continue
		name = entry.get("Name")
		if name is not None:
			names.append(name)
	return names

def collect_hand_recipes(generated_files):
	data = generated_files.get("Generated/Recipes/machines.json")
	if data is None:
		raise RuntimeError("Generated/Recipes/machines.json not found")
	recipes_hand = []
	for obj in iter_objects(data):
		recipes = obj.get("Recipes")
		if isinstance(recipes, list):
			recipes_hand.extend(recipes)
	if not recipes_hand:
		raise RuntimeError("No hand recipes found in Generated/Recipes/machines.json")
	return recipes_hand

def has_hand_recipe(recipes_hand, result):
	for recipe in recipes_hand:
		output = recipe.get("Output")
		for name in extract_item_names(output):
			if name.find(result) != -1:
				return True
	return False

def load_generators_module(filename, module_name):
	our_path = os.path.dirname(os.path.abspath(__file__))
	generators_path = os.path.join(our_path, "Generators")
	module_path = os.path.join(generators_path, filename)
	spec = importlib.util.spec_from_file_location(module_name, module_path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	return module


def validate_recipes(generated_files, item_tiers):
	errors = []
	checked = 0
	for filename, data in generated_files.items():
		if not filename.startswith("Generated/Recipes/"):
			continue
		if not isinstance(data, dict):
			continue
		for obj in iter_objects(data):
			recipes = obj.get("Recipes")
			if not isinstance(recipes, list):
				continue
			dictionary_name = obj.get("Name", filename)
			for recipe in recipes:
				if not isinstance(recipe, dict):
					continue
				checked += 1
				recipe_name = recipe.get("Name", "UnnamedRecipe")
				recipe_tier = recipe.get("Tier")
				item_tier = -1
				for item_name in extract_item_names(recipe.get("Input")) + extract_item_names(recipe.get("Output")):
					if item_name in item_tiers:
						item_tier = max(item_tier, item_tiers[item_name])
				if item_tier <= 0:
					continue
				if recipe_tier is None:
					errors.append(
						f"{dictionary_name}:{recipe_name} missing Tier (min {item_tier})"
					)
					continue
				if recipe_tier < item_tier:
					errors.append(
						f"{dictionary_name}:{recipe_name} Tier {recipe_tier} < item tier {item_tier}"
					)
	return errors, checked

def validate_machine_hand_recipes(generated_files):
	machines_module = load_generators_module("MachinesList.py", "validate_machines_list")
	materials_module = load_generators_module("Materials.py", "validate_materials")
	machines = machines_module.machines
	tier_material = materials_module.tier_material
	recipes_hand = collect_hand_recipes(generated_files)
	errors = []
	for machine in machines:
		for tier in range(machine["StartTier"], machine["EndTier"] + 1):
			name = tier_material[tier] + machine["Name"]
			if not has_hand_recipe(recipes_hand, name):
				errors.append(f"No recipe for {machine['Name']}")
	return errors


def validate_generated(generated_files, validate_tiers=True, validate_machine_recipes=True):
	if not generated_files:
		raise RuntimeError("Generated files map is empty")

	item_tiers = collect_item_tiers(generated_files)
	if not item_tiers:
		raise RuntimeError("No item tiers found in generated files")

	errors = []
	checked = 0
	if validate_tiers:
		recipe_errors, checked = validate_recipes(generated_files, item_tiers)
		errors.extend(recipe_errors)
	if validate_machine_recipes:
		errors.extend(validate_machine_hand_recipes(generated_files))
	if errors:
		errors_text = "\n".join(errors)
		raise RuntimeError(f"Tier validation failed:\n{errors_text}")

	return len(item_tiers), checked


if __name__ == "__main__":
	raise RuntimeError("Run validation from Generate.py to avoid file IO")
