import json
import os
import errno
import sys
import csv
import re
import shutil

our_path = os.path.dirname(sys.argv[0])

generated_files = {}
generated_text_files = {}

def res_cost(level, mul = 1):
	arr = []
	arr.append({"Name": "Computations", "Count": tiers_base_cost[level] * mul})
		
	return arr

def FixMinTier(recipes, tier):
	for recipe in recipes:
		if "Tier" in recipe and recipe["Tier"] >= tier:
			continue
		else:
			recipe["Tier"] = tier

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


def round_25(x):
    return round(x*4)/4

def write_file(filename, data):
	generated_files[filename] = data

def order_items_blocks(objects):
	items = [obj for obj in objects if obj.get("Class") == "StaticItem"]
	blocks = [obj for obj in objects if obj.get("Class") == "StaticBlock"]
	rest = [obj for obj in objects if obj.get("Class") not in ("StaticItem", "StaticBlock")]
	return items + blocks + rest

def write_text_file(filename, data):
	generated_text_files[filename] = data

def get_generated_files():
	return generated_files

def flush_generated_files():
	for filename, data in generated_files.items():
		full_path = os.path.join(our_path, "..", "Content", filename)
		if not os.path.exists(os.path.dirname(full_path)):
			try:
				os.makedirs(os.path.dirname(full_path))
			except OSError as exc:
				if exc.errno != errno.EEXIST:
					raise
		with open(full_path, "w") as data_file:
			data_file.write(json.dumps(data, indent=4, sort_keys=True))

	for filename, data in generated_text_files.items():
		full_path = os.path.join(our_path, "..", "Content", filename)
		if not os.path.exists(os.path.dirname(full_path)):
			try:
				os.makedirs(os.path.dirname(full_path))
			except OSError as exc:
				if exc.errno != errno.EEXIST:
					raise
		with open(full_path, "w", newline="", encoding="utf-8") as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=",")
			spamwriter.writerow(["Key", "SourceString"])
			for x in data:
				spamwriter.writerow(x)
			
def CamelToSpaces(name):
	return re.sub(r"([a-z])([A-Z])", r"\g<1> \g<2>", name)
	
def simple_in_out_recipe(name):
	if not hasattr(simple_in_out_recipe, "counter"):
		simple_in_out_recipe.counter = -1
		
	simple_in_out_recipe.counter += 1
	
	return {
		"Name": "SimpleInOutRecipe" + str(simple_in_out_recipe.counter),
		"Input":{
			"Items":[
				{
					"Name": name,
					"Count": 1
				}
			]
		},
		"Output":{
			"Items":[
				{
					"Name": name,
					"Count": 1
				}
			]
		},
		"Ticks": 20
	}
	
level_labels = [
	"I",
	"II",
	"III",
	"IV",
	"V",
	"VI",
	"VII",
	"VIII",
	"IX",
	"X"
]

tiers_name_helper = [
	"",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
	"10",
	"11",
	"12"
]

tbcm = 1.0

tiers_base_cost = [
 	20, # stone
 	200 * tbcm**1, # copper
 	2000 * tbcm**2, # steel
 	20000 * tbcm**3, # alum
 	200000 * tbcm**4, # ss
 	2000000 * tbcm**5, # tita
 	20000000 * tbcm**6, # hm
 	80000000 * tbcm**7, # neu
 	80000000*2 * tbcm**7,
 	80000000*4 * tbcm**7,
 	80000000*6 * tbcm**7,
 	80000000*8 * tbcm**7,
 	80000000*10 * tbcm**7,
 	80000000*12 * tbcm**7
 ]

tiers_energy_level = [
	10*20*1,
	10*20*4,
	10*20*4**2,
	10*20*4**3,
	10*20*4**4,
	10*20*4**5,
	10*20*4**6,
	10*20*4**7,
	10*20*4**8,
	10*20*4**9,
	10*20*4**10,
	10*20*4**11,
]

tiers_adv_cost = [
	0,
	0,
	8,
	16,
	32,
	32,
	32,
	16,
	32,
	36,
	38,
	40,
	42,
	44,
	46,
	48,
]

def clamp(val, _min, _max):
	return max(_min, min(val, _max))

def has_hand_recipe(recipes_hand, result):
	for r in recipes_hand:
		if not r["Output"]["Items"][0]["Name"].find(result) == -1:
			return True
			
	return False
	
def get_hand_recipe(recipes_hand, result):
	for r in recipes_hand:
		if not r["Output"]["Items"][0]["Name"].find(result) == -1:
			return r
			
	return None

def create_item(name, count=1):
    return {"Name": name, "Count": count}

def one_item(item_name, count=1):
    return {"Items": [create_item(item_name, count)]}

def no_items():
	return { "Items":[] }

def items(array, tier=0):
	items = []
	for entry in array:
		chance = 100  # reset chance per entry
		if len(entry) == 0:
			continue
		elif len(entry) == 1:
			item, count_fn = entry[0], 1
		elif len(entry) == 3:
			item, count_fn = entry[0], entry[1]
			chance = entry[2]
		else:
			item, count_fn = entry
		count = count_fn(tier) if callable(count_fn) else count_fn

		if count > 0 and chance != 100:
			items.append({
				"Name": item,
				"Count": count,
				"Probability": chance
			})
		elif count > 0:
			items.append({
				"Name": item,
				"Count": count
			})

	return {"Items": items}

single_battery_cell_charge = 100000

single_canister_capacity = 10000

def battery_mul(level):
	return 4 * pow(5, level)
	
f_machine_bonus = 1.5

tiers_numlist = [0,1,2,3,4,5,6,7]

static_item = ""

int32max = 2147483647

static_research = ""
static_chapter = "StaticChapter"
static_block = ""
static_surface = ""

static_cover = "StaticCover"

slot_logic = "ItemLogic"

research_recipe = "StaticResearchRecipe"
building_cube_logic = "BuildingSurfaceBlockItemLogic"
building_single_logic = "BuildingSingleBlockItemLogic"
building_drill_logic = "BuildingDrillBlockItemLogic"
building_plane_logic = "BuildingPlaneBlockItemLogic"

cover_item_logic = "CoverItemLogic"

ic_reactor_r_dict = "IndustrialChemReactorRecipeDictionary"
building_brush_slot_logic = "BuildingBrushItemLogic"
assembler_r_dict = "AssemblerRecipeDictionary"
h_r_dict = "HandRecipeDictionary"
r_dict = "RecipeDictionary"
breaking_recipe = "RecipeDictionary"
ico_generator = "IcoGenerator"

tesselator = "Tesselator"
tesselator_cube = "TesselatorCube"
tesselator_static_mesh = "TesselatorStaticMesh"

item_data = "ItemData"
basic_slot_widget_c = "Gui/BasicStackedSlotWidget.BasicStackedSlotWidget_C"

ico = ""
additive_ico = "Additive"


def parts_ramp(level, factor = 5):
	if level == 0:
		return 0
	if level < 3:
		return level * factor
	else:
		return factor * 3
	
def exp_ramp(level, factor = 2):
	return factor ** level

tiers_res_item = [
	"Computations",
	"Circuit",
	"AdvancedCircuit",
	"Processor",
	"QuantumCircuit",
	"QuantumProcessor",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
]

euler = 2.718281

def fuel_tags():
	return "FuelBurn"

def fluid_furnace_output():
	return 200

def furnace_output():
	return 50

def fission_output():
	return 200 * 20 * 8

def uranium_rod_output():
	return fission_output() * 2000

def fuel_value(material):
	return material["Burnable"]["BurnTime"] * 50

def fuel_burn_time(material, machine_output):
	return fuel_value(material) / machine_output 

def oil_crack_array(input_count):
	return [
		{
			"Name": "HeavyOil",
			"Count": 2000 * (input_count / 15000.0)
		},
		{
			"Name": "Diesel",
			"Count": 5000 * (input_count / 15000.0)
		},
		{
			"Name": "Gasoline",
			"Count": 3000 * (input_count / 15000.0)
		},
		{
			"Name": "Ethylene",
			"Count": 3000 * (input_count / 15000.0)
		}]

def fluid_furnace_pair(material):
	duration = fuel_burn_time(material, fluid_furnace_output())
	count = 100
	if duration < 200:
		count = count * 10
		duration = duration * 10

	return duration, count

def oil_crack_recipe(index, input_count):
	outputs = oil_crack_array(input_count)
	if index == -1:
		return outputs

	return outputs[index]