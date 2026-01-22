import importlib.util
import os
import sys

our_path = os.path.dirname(os.path.abspath(__file__))
generators_path = os.path.join(our_path, "Generators")

sys.path.insert(0, generators_path)

from Common import get_generated_files, flush_generated_files
from ValidateTiers import validate_generated

print(our_path)

def run_generator(file_path):
	rel_path = os.path.relpath(file_path, generators_path)
	module_name = "gen_" + rel_path.replace(os.sep, "_").replace(".", "_")
	spec = importlib.util.spec_from_file_location(module_name, file_path)
	module = importlib.util.module_from_spec(spec)
	sys.modules[module_name] = module
	spec.loader.exec_module(module)

generator_files = [
	"Achievements.py",
	"Biomes.py",
	"CoverItemsGen.py",
	"Covers.py",
	"DesignableBlocks.py",
	"HandRecipes.py",
	"LogicExport.py",
	"MachinesGen.py",
	"MapgenCore.py",
	"MiscGen.py",
	"MiscRec.py",
	"Modifiers.py",
	"OresGen.py",
	"OresRec.py",
	"PartsGen.py",
	"Props.py",
	"Researches.py",
	"Spawn.py",
	"Weather.py",
]

for filename in generator_files:
	full_path = os.path.join(generators_path, filename)
	print(full_path + " is runned")
	run_generator(full_path)
	print("Done")

try:
	item_count, recipe_count = validate_generated(
		get_generated_files(),
		validate_tiers=True,
		validate_machine_recipes=True
	)
	print(f"ValidateTiers: ok ({item_count} item tiers, {recipe_count} recipes)")
except Exception as e:
	print(f"ValidateTiers: {e}")
flush_generated_files()
