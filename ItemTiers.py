INF = 1 << 30


def iter_objects(generated_files):
	for data in generated_files.values():
		if not isinstance(data, dict):
			continue
		objects = data.get("Objects", [])
		if not isinstance(objects, list):
			continue
		for obj in objects:
			if isinstance(obj, dict):
				yield obj


def item_names(io_block):
	if not isinstance(io_block, dict):
		return []
	return [entry["Name"] for entry in io_block.get("Items") or [] if isinstance(entry, dict) and entry.get("Name")]


def complete_item_tiers(generated_files):
	objects = list(iter_objects(generated_files))
	items = {obj["Name"]: obj for obj in objects if obj.get("Class") == "StaticItem"}
	groups = {obj["Name"]: obj.get("Members") or [] for obj in objects if obj.get("Class") == "ItemGroup"}
	researches = {obj["Name"]: obj for obj in objects if obj.get("Class", "").startswith("StaticResearch")}
	player = next(obj for obj in objects if obj.get("Class") == "StaticPlayer")

	derived = {name for name, item in items.items() if item.get("Tier") is None}
	max_tier = max(item["Tier"] for name, item in items.items() if name not in derived)

	def tier_of(name):
		if name in groups:
			return min([tier_of(member) for member in groups[name]] or [INF])
		item = items.get(name)
		if item is None or item.get("Tier") is None:
			return INF
		return item["Tier"]

	routes = []
	recipe_gates = {}
	start = set(player.get("StartResearches") or [])

	def unlock(name, tier):
		if name:
			routes.append((tier, [], [name]))

	for name, research in researches.items():
		tier = 0 if name in start else research.get("Tier", 0)
		for pair in research.get("Unlocks") or []:
			key = (pair[0], pair[1])
			recipe_gates[key] = min(recipe_gates.get(key, INF), tier)
		for decoration in research.get("Decorations") or []:
			unlock(decoration, tier)
		unlock(research.get("Tool"), tier)
		for version in research.get("Versions") or []:
			technology = researches.get(version.get("Technology"), {})
			version_tier = max(tier, technology.get("Tier", 0))
			for pair in version.get("Unlocks") or []:
				key = (pair[0], pair[1])
				recipe_gates[key] = min(recipe_gates.get(key, INF), version_tier)
			for decoration in version.get("Decorations") or []:
				unlock(decoration, version_tier)

	for name in (player.get("Tools") or []) + (player.get("Hotbar") or []) + [player.get("Light"), player.get("BlueprintItem")]:
		unlock(name, 0)
	for name in item_names(player.get("StartInventory")):
		unlock(name, 0)

	dictionaries = {}
	for obj in objects:
		if obj.get("Class") != "RecipeDictionary":
			continue
		dictionary = dictionaries.setdefault(obj["Name"], {"Recipes": [], "UsedIn": [], "StartTier": 0})
		dictionary["Recipes"] += obj.get("Recipes") or []
		dictionary["UsedIn"] += [use["Item"] for use in obj.get("UsedIn") or [] if isinstance(use, dict) and use.get("Item")]
		if obj.get("StartTier") is not None:
			dictionary["StartTier"] = obj["StartTier"]

	hand = player.get("HandRecipes")
	for name, dictionary in dictionaries.items():
		machines = [tier_of(machine) for machine in dictionary["UsedIn"]]
		machine_tier = min([tier for tier in machines if tier < INF] or [0])
		for recipe in dictionary["Recipes"]:
			gate = recipe_gates.get((name, recipe.get("Name")), 0)
			if name != hand:
				gate = max(gate, machine_tier, recipe.get("Tier", 0), dictionary["StartTier"])
			routes.append((gate, item_names(recipe.get("Input")), item_names(recipe.get("Output"))))

	def propagate():
		changed = True
		while changed:
			changed = False
			for gate, inputs, outputs in routes:
				tier = max([gate] + [tier_of(name) for name in inputs])
				if tier >= INF:
					continue
				tier = min(tier, max_tier)
				for name in outputs:
					if name in derived and tier < tier_of(name):
						items[name]["Tier"] = tier
						changed = True

	propagate()

	produced = {name for _, _, outputs in routes for name in outputs}
	first_use = {}
	for gate, inputs, _ in routes:
		for name in inputs:
			for member in groups.get(name) or [name]:
				first_use[member] = min(first_use.get(member, INF), gate)
	seeded = False
	for name in derived:
		if tier_of(name) == INF and name not in produced and name in first_use:
			items[name]["Tier"] = min(first_use[name], max_tier)
			seeded = True
	if seeded:
		propagate()

	untiered = sorted(name for name in derived if tier_of(name) == INF)
	return len(derived) - len(untiered), untiered
