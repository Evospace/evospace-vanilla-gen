import importlib.util
import os

MAX_TIER = 7


def iter_objects(data):
	objects = data.get("Objects", [])
	if isinstance(objects, list):
		for obj in objects:
			if isinstance(obj, dict):
				yield obj


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


def collect_dictionary_start_tiers(generated_files):
	start_tiers = {}
	for data in generated_files.values():
		if not isinstance(data, dict):
			continue
		for obj in iter_objects(data):
			if obj.get("Class") != "RecipeDictionary":
				continue
			name = obj.get("Name")
			start_tier = obj.get("StartTier")
			if name is None or start_tier is None:
				continue
			declared = start_tiers.setdefault(name, start_tier)
			if declared != start_tier:
				raise RuntimeError(f"{name} declares StartTier {declared} and {start_tier}")
	return start_tiers


def validate_recipes(generated_files, start_tiers):
	errors = []
	clamped = 0
	checked = 0
	for data in generated_files.values():
		if not isinstance(data, dict):
			continue
		for obj in iter_objects(data):
			if obj.get("Class") != "RecipeDictionary":
				continue
			recipes = obj.get("Recipes")
			if not isinstance(recipes, list) or not recipes:
				continue
			dictionary_name = obj.get("Name")
			start_tier = start_tiers.get(dictionary_name)
			for recipe in recipes:
				if not isinstance(recipe, dict):
					continue
				checked += 1
				tier = recipe.get("Tier")
				if tier is None:
					continue
				recipe_name = recipe.get("Name", "UnnamedRecipe")
				if start_tier is None:
					errors.append(f"{dictionary_name}:{recipe_name} has Tier {tier} but the dictionary declares no StartTier")
				elif tier > MAX_TIER:
					errors.append(f"{dictionary_name}:{recipe_name} Tier {tier} above {MAX_TIER}")
				elif tier < start_tier:
					clamped += 1
	return errors, clamped, checked

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

	start_tiers = collect_dictionary_start_tiers(generated_files)
	if not start_tiers:
		raise RuntimeError("No dictionary start tiers found in generated files")

	errors = []
	warnings = []
	clamped = 0
	checked = 0
	if validate_tiers:
		recipe_errors, clamped, checked = validate_recipes(generated_files, start_tiers)
		errors.extend(recipe_errors)
	if validate_machine_recipes:
		warnings.extend(validate_machine_hand_recipes(generated_files))
	if errors:
		errors_text = "\n".join(errors)
		raise RuntimeError(f"Tier validation failed:\n{errors_text}")

	return len(start_tiers), checked, clamped, warnings


if __name__ == "__main__":
	raise RuntimeError("Run validation from Generate.py to avoid file IO")
