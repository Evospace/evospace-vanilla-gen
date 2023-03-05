from Common import *
from MachinesList import *
from MiscGen import *
import copy

objects_array = []

recipes_wrench = []
recipes_blast_furnace = []
recipes_oven = []
recipes_smelter = []
recipes_arc_furnace = []
recipes_macerator = []
recipes_boiler = []
recipes_farm = []
recipes_condens = []
recipes_generator = []
recipes_electric_engine = []
recipes_compact_generator = []
recipes_steam_engine = []
recipes_steam_turbine = []
recipes_pump = []
recipes_electrolyzer = []
recipes_cutter = []
recipes_furnace = []
recipes_ferm = []
recipes_toolarm = []
recipes_hammer = []
recipes_mixer = []
recipes_chem = []

recipes_sep = []
recipes_sep2 = []
recipes_press = []

recipes_elfurn = []

recipes_radiator = []
recipes_solar = []
recipes_fission = []

recipes_coil = []

recipes_indu = []

recipes_exch = []
recipes_iexch = []

recipes_freezer = []

recipes_combustion = []

recipes_pyro = []

recipes_computer = []
recipes_q_computer = []

recipes_assembler = []

recipes_gasturb = []

recipes_filtering_unit = []

recipes_chemical_bath = []

recipes_centrifuge = []

recipes_riteg = []

recipes_industrial_steam_turbine = []

recipes_fusion_reactor = []

recipes_industrial_boiler = []

recipes_industrial_electric_engine = []

recipes_portal = []

recipes_kinetic_heater = []

recipes_hand = []


def append_recipe(recipe):
    item_count = 0
    for item in recipe["input"]["items"]:
        item_count = item_count + item["count"]

    level = extract_tier(recipe["output"]["items"][0]["name"]) + 1

    dec_recipe = copy.deepcopy(recipe)

    recipes_hand.append(recipe)

    output = copy.deepcopy(dec_recipe["input"])

    dec_recipe["ticks"] = max(min(item_count * 10, 400), 20)
    dec_recipe["res_input"] = {"name": "Electricity", "count": 20 * level}
    recipes_assembler.append(dec_recipe)


def append_recipe_hand_press(recipe):
    item_count = 0
    for item in recipe["input"]["items"]:
        item_count = item_count + item["count"]

    dec_recipe = copy.deepcopy(recipe)

    recipes_hand.append(recipe)

    output = copy.deepcopy(dec_recipe["input"])

    dec_recipe["ticks"] = 60
    dec_recipe["res_input"] = {"name": "Kinetic", "count": 100}
    recipes_press.append(dec_recipe)


# wrenching

recipes_industrial_steam_turbine.append(
    {
        "name": "Rotating",
        "input": {"items": []},
        "res_input": {"name": "Steam", "count": fission_fullpower * 0.9},
        "output": {"items": []},
        "res_output": {
            "name": "Electricity",
            "count": fission_fullpower * 0.9 * 0.9,
        },
        "ticks": 200,
        "loss": 10,
    }
)

recipes_industrial_boiler.append(
    {
        "name": "Boiling",
        "input": {
            "items": [
                {"name": "Water", "count": 2000},
            ]
        },
        "res_input": {"name": "Heat", "count": fission_fullpower},
        "output": {"items": []},
        "res_output": {"name": "Steam", "count": fission_fullpower * 0.9},
        "ticks": 200,
    }
)

recipes_fusion_reactor.append(
    {
        "name": "HotNeutroniumIngot1",
        "input": {"items": [{"name": "ProducerGas", "count": 1000}]},
        "res_input": {
            "name": "Electricity",
            "count": fission_fullpower * 0.9 * 0.9,
        },
        "output": {"items": [{"name": "HotNeutroniumIngot", "count": 1}]},
        "ticks": 200,
    }
)

recipes_fusion_reactor.append(
    {
        "name": "HotNeutroniumIngot2",
        "input": {"items": [{"name": "ProducerGas", "count": 3000}]},
        "res_input": {
            "name": "Electricity",
            "count": 2 * fission_fullpower * 0.9 * 0.9,
        },
        "output": {"items": [{"name": "HotNeutroniumIngot", "count": 1 * 3}]},
        "ticks": 200 * 2,
    }
)

recipes_fusion_reactor.append(
    {
        "name": "HotNeutroniumIngot4",
        "input": {"items": [{"name": "UltimateCatalyst", "count": 1, "split": 0}]},
        "res_input": {
            "name": "Electricity",
            "count": fission_fullpower * 0.9 * 0.9,
        },
        "output": {"items": [{"name": "HotNeutroniumIngot", "count": 1}]},
        "ticks": 200,
    }
)

recipes_fusion_reactor.append(
    {
        "name": "HotNeutroniumIngot3",
        "input": {"items": [{"name": "UltimateCatalyst", "count": 3, "split": 0}]},
        "res_input": {
            "name": "Electricity",
            "count": 2 * fission_fullpower * 0.9 * 0.9,
        },
        "output": {"items": [{"name": "HotNeutroniumIngot", "count": 1 * 3}]},
        "ticks": 200 * 2,
    }
)

recipes_smelter.append(
    {
        "name": "Glass",
        "input": {
            "items": [
                {"name": "SandSurface", "count": 1},
            ]
        },
        "res_input": {"name": "Heat", "count": 10},
        "output": {"items": [{"name": "Glass", "count": 1}]},
        "ticks": 200,
    }
)

for list in (simple_deco, wooden_misc, simple_single, simple_blocks, static_mesh_block):
    for one in list:
        recipes_wrench.append(
            {
                "name": one["name"] + "Wrenching",
                "ticks": 20,
                "input": {"items": [{"name": one["name"], "count": 1}]},
                "output": {"items": [{"name": one["name"], "count": 1}]},
            }
        )

# other

append_recipe(
    {
        "name": "Cell",
        "input": {
            "items": [
                {"name": "StainlessSteelPlate", "count": 1},
                {"name": "StainlessSteelParts", "count": 1},
            ]
        },
        "output": {"items": [{"name": "Cell", "count": 1}]},
        "ticks": 200,
    }
)

append_recipe(
    {
        "name": "Cell2",
        "input": {
            "items": [
                {"name": "DepletedUraniumCell", "count": 1},
            ]
        },
        "output": {"items": [{"name": "Cell", "count": 1}]},
        "ticks": 200,
    }
)

append_recipe(
    {
        "name": "UraniumCell",
        "input": {
            "items": [
                {"name": "Uranium235Dust", "count": 3},
                {"name": "UraniumDust", "count": 20},
                {"name": "Cell", "count": 1},
            ]
        },
        "output": {"items": [{"name": "UraniumCell", "count": 1}]},
        "ticks": 200,
    }
)

append_recipe(
    {
        "name": "ThoriumCell",
        "input": {
            "items": [
                {"name": "ThoriumDust", "count": 20},
                {"name": "Cell", "count": 1},
            ]
        },
        "output": {"items": [{"name": "ThoriumCell", "count": 1}]},
        "ticks": 200,
    }
)

append_recipe(
    {
        "name": "Uranium233Cell",
        "input": {
            "items": [
                {"name": "Uranium233Dust", "count": 3},
                {"name": "Cell", "count": 1},
            ]
        },
        "output": {"items": [{"name": "Uranium233Cell", "count": 1}]},
        "ticks": 200,
    }
)

append_recipe(
    {
        "name": "PlutoniumCell",
        "input": {
            "items": [
                {"name": "PlutoniumDust", "count": 3},
                {"name": "Cell", "count": 1},
            ]
        },
        "output": {"items": [{"name": "PlutoniumCell", "count": 1}]},
        "ticks": 200,
    }
)

append_recipe(
    {
        "name": "FilteringCell",
        "input": {
            "items": [
                {"name": "Coal", "count": 10},
                {"name": "Cell", "count": 1},
            ]
        },
        "output": {"items": [{"name": "FilteringCell", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "Circuit",
        "input": {
            "items": [
                {"name": "CircuitBoard", "count": 1},
                {"name": "CopperWire", "count": 6},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "Circuit", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "AdvancedCircuit",
        "input": {
            "items": [{"name": "Silicon", "count": 1}, {"name": "Circuit", "count": 1}]
        },
        "res_input": {"name": "Electricity", "count": 30},
        "output": {"items": [{"name": "AdvancedCircuit", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "SiliconWafer",
        "input": {
            "items": [
                {"name": "Silicon", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 100},
        "output": {"items": [{"name": "SiliconWafer", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "Processor",
        "input": {
            "items": [
                {"name": "SiliconWafer", "count": 1},
                {"name": "AdvancedCircuit", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 80},
        "output": {"items": [{"name": "Processor", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "QuantumBrain",
        "input": {
            "items": [
                {"name": "QuantumProcessor", "count": 2},
                {"name": "UltimateCatalyst", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 1000},
        "output": {"items": [{"name": "QuantumBrain", "count": 1}]},
        "ticks": 200,
    }
)

append_recipe(
    {
        "name": "Catalyst",
        "input": {
            "items": [
                {"name": "Cell", "count": 1},
                {"name": "GoldWire", "count": 10},
                {"name": "Coal", "count": 4},
            ]
        },
        "output": {"items": [{"name": "Catalyst", "count": 1}]},
        "ticks": 200,
    }
)

append_recipe(
    {
        "name": "UltimateCatalyst",
        "input": {
            "items": [
                {"name": "Cell", "count": 1},
                {"name": "NeutroniumParts", "count": 8},
                {"name": "Coke", "count": 10},
            ]
        },
        "output": {"items": [{"name": "UltimateCatalyst", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "AdvancedCircuitBoard",
        "input": {
            "items": [
                {"name": "Plastic", "count": 1},
                {"name": "GoldWire", "count": 3},
            ]
        },
        "res_input": {"name": "Electricity", "count": 20},
        "output": {"items": [{"name": "AdvancedCircuitBoard", "count": 1}]},
        "ticks": 80,
    }
)

recipes_assembler.append(
    {
        "name": "Processor2",
        "input": {
            "items": [
                {"name": "SiliconWafer", "count": 1},
                {"name": "AdvancedCircuitBoard", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 80},
        "output": {"items": [{"name": "Processor", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "QuantumCore",
        "input": {
            "items": [
                {"name": "RareEarthElement", "count": 1},
                {"name": "CopperParts", "count": 2},
            ]
        },
        "res_input": {"name": "Electricity", "count": 1000},
        "output": {"items": [{"name": "QuantumCore", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "QuantumCircuit",
        "input": {
            "items": [
                {"name": "QuantumCore", "count": 2},
                {"name": "AdvancedCircuitBoard", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 1000 / 7},
        "output": {"items": [{"name": "QuantumCircuit", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "QuantumProcessor",
        "input": {
            "items": [
                {"name": "QuantumCircuit", "count": 1},
                {"name": "Processor", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 2000 / 13},
        "output": {"items": [{"name": "QuantumProcessor", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "CopperWire",
        "input": {
            "items": [
                {"name": "CopperIngot", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "CopperWire", "count": 2}]},
        "ticks": 100,
    }
)

recipes_assembler.append(
    {
        "name": "SuperconductorWire",
        "input": {
            "items": [
                {"name": "SuperconductorIngot", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 100},
        "output": {"items": [{"name": "SuperconductorWire", "count": 2}]},
        "ticks": 100,
    }
)

recipes_assembler.append(
    {
        "name": "Battery",
        "input": {
            "items": [
                {"name": "SulfuricAcid", "count": 100},
                {"name": "CopperParts", "count": 1},
                {"name": "StainlessSteelPlate", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "Battery", "count": 1}]},
        "ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "GoldWire",
        "input": {
            "items": [
                {"name": "GoldIngot", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "GoldWire", "count": 2}]},
        "ticks": 100,
    }
)

append_recipe(
    {
        "name": "ReflectorCell",
        "input": {
            "items": [
                {"name": "Cell", "count": 1},
                {"name": "BerylliumDust", "count": 3},
            ]
        },
        "output": {"items": [{"name": "ReflectorCell", "count": 1}]},
        "ticks": 100,
    }
)

append_recipe(
    {
        "name": "ControlCell",
        "input": {
            "items": [
                {"name": "Cell", "count": 1},
                {"name": "BoronDust", "count": 3},
            ]
        },
        "res_input": {"name": "Electricity", "count": 1000 / 9},
        "output": {"items": [{"name": "ControlCell", "count": 1}]},
        "ticks": 100,
    }
)

recipes_condens.append(
    {
        "name": "Water",
        "input": {"items": []},
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "Water", "count": 250}]},
        "ticks": 200,
    }
)

recipes_condens.append(
    {
        "name": "Oxygen",
        "input": {"items": []},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": [{"name": "Oxygen", "count": 250}]},
        "ticks": 200,
    }
)

recipes_condens.append(
    {
        "name": "Nitrogen",
        "input": {"items": []},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": [{"name": "Nitrogen", "count": 1000}]},
        "ticks": 200,
    }
)

recipes_condens.append(
    {
        "name": "Helium",
        "input": {"items": []},
        "res_input": {"name": "Kinetic", "count": 40},
        "output": {"items": [{"name": "Helium", "count": 100}]},
        "ticks": 200,
    }
)

recipes_condens.append(
    {
        "name": "Methane",
        "input": {"items": []},
        "res_input": {"name": "Kinetic", "count": 40},
        "output": {"items": [{"name": "Methane", "count": 80}]},
        "ticks": 200,
    }
)

recipes_condens.append(
    {
        "name": "Hydrogen",
        "input": {"items": []},
        "res_input": {"name": "Kinetic", "count": 40},
        "output": {"items": [{"name": "Hydrogen", "count": 50}]},
        "ticks": 200,
    }
)

recipes_farm.append(
    {
        "name": "Logs",
        "input": {"items": [{"name": "Water", "count": 625}]},
        "output": {"items": [{"name": "Log", "count": 15}]},
        "ticks": 2000,
    }
)

recipes_farm.append(
    {
        "name": "Pumpkin",
        "input": {"items": [{"name": "Water", "count": 625}]},
        "output": {"items": [{"name": "Pumpkin", "count": 10}]},
        "ticks": 1000,
    }
)

recipes_centrifuge.append(
    {
        "name": "DepletedUraniumCell",
        "input": {"items": [{"name": "DepletedUraniumCell", "count": 1}]},
        "output": {
            "items": [
                {
                    "name": "PlutoniumDust",
                    "count": 1,
                    "split": 10,
                }
            ]
        },
        "res_input": {"name": "Kinetic", "count": 100},
        "ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "UraniumCell",
        "input": {"items": [{"name": "UraniumCell", "count": 1}]},
        "output": {"items": [{"name": "DepletedUraniumCell", "count": 1}]},
        "res_output": {"name": "Heat", "count": 7100},
        "ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "UraniumCell2",
        "input": {
            "items": [
                {"name": "UraniumCell", "count": 2},
                {
                    "name": "ControlCell",
                    "count": 1,
                    "split": 0,
                },
            ]
        },
        "output": {"items": [{"name": "DepletedUraniumCell", "count": 2}]},
        "res_output": {"name": "Heat", "count": 7100 * 2.2},
        "ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "UraniumCell3",
        "input": {
            "items": [
                {"name": "UraniumCell", "count": 3},
                {
                    "name": "ControlCell",
                    "count": 1,
                    "split": 0,
                },
            ]
        },
        "output": {"items": [{"name": "DepletedUraniumCell", "count": 3}]},
        "res_output": {"name": "Heat", "count": 7100 * 3.3},
        "ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "UraniumCell4",
        "input": {
            "items": [
                {"name": "UraniumCell", "count": 3},
                {
                    "name": "ControlCell",
                    "count": 5,
                    "split": 0,
                },
            ]
        },
        "output": {"items": [{"name": "DepletedUraniumCell", "count": 3}]},
        "res_output": {"name": "Heat", "count": 7100 * 3.3 / 2},
        "ticks": 2000 * 2,
    }
)

recipes_fission.append(
    {
        "name": "ControlCell3",
        "input": {
            "items": [
                {"name": "UraniumCell", "count": 1},
                {
                    "name": "ControlCell",
                    "count": 3,
                    "split": 0,
                },
            ]
        },
        "output": {"items": [{"name": "DepletedUraniumCell", "count": 1}]},
        "res_output": {"name": "Heat", "count": 7100 / 4},
        "ticks": 8000 * 0.9 * 0.9,
    }
)

recipes_fission.append(
    {
        "name": "ThoriumCell",
        "input": {
            "items": [
                {
                    "name": "UraniumCell",
                    "count": 3,
                },
                {
                    "name": "ReflectorCell",
                    "count": 1,
                    "split": 0,
                },
                {
                    "name": "ThoriumCell",
                    "count": 2,
                },
            ]
        },
        "output": {
            "items": [
                {"name": "DepletedUraniumCell", "count": 3},
                {
                    "name": "Uranium233Cell",
                    "count": 2,
                },
            ]
        },
        "res_output": {"name": "Heat", "count": 200},
        "ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "PlutoniumCell",
        "input": {
            "items": [
                {
                    "name": "PlutoniumCell",
                    "count": 1,
                },
                {
                    "name": "ReflectorCell",
                    "count": 1,
                    "split": 0,
                },
                {
                    "name": "ThoriumCell",
                    "count": 3,
                },
            ]
        },
        "output": {
            "items": [
                {
                    "name": "Uranium233Cell",
                    "count": 3,
                },
                {"name": "DepletedUraniumCell", "count": 1},
            ]
        },
        "res_output": {"name": "Heat", "count": 200},
        "ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "PlutoniumCell2",
        "input": {
            "items": [
                {
                    "name": "PlutoniumCell",
                    "count": 1,
                },
                {
                    "name": "ReflectorCell",
                    "count": 2,
                    "split": 0,
                },
                {
                    "name": "ThoriumCell",
                    "count": 6,
                },
            ]
        },
        "output": {
            "items": [
                {
                    "name": "Uranium233Cell",
                    "count": 6,
                },
                {"name": "DepletedUraniumCell", "count": 1},
            ]
        },
        "res_output": {"name": "Heat", "count": 200},
        "ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "ControlCell",
        "input": {
            "items": [
                {"name": "UraniumCell", "count": 1},
                {
                    "name": "ControlCell",
                    "count": 1,
                    "split": 0,
                },
            ]
        },
        "output": {"items": [{"name": "DepletedUraniumCell", "count": 1}]},
        "res_output": {"name": "Heat", "count": 7100 / 2},
        "ticks": 4000 * 0.9,
    }
)

recipes_fission.append(
    {
        "name": "Uranium233Cell",
        "input": {
            "items": [
                {
                    "name": "Uranium233Cell",
                    "count": 1,
                },
                {
                    "name": "ControlCell",
                    "count": 1,
                    "split": 0,
                },
            ]
        },
        "output": {
            "items": [
                {
                    "name": "DepletedUraniumCell",
                    "count": 1,
                }
            ]
        },
        "res_output": {"name": "Heat", "count": 7100 * 3.3},
        "ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "Uranium233Cell2",
        "input": {
            "items": [
                {
                    "name": "Uranium233Cell",
                    "count": 2,
                },
                {
                    "name": "ControlCell",
                    "count": 1,
                    "split": 0,
                },
            ]
        },
        "output": {
            "items": [
                {
                    "name": "DepletedUraniumCell",
                    "count": 2,
                }
            ]
        },
        "res_output": {"name": "Heat", "count": fission_fullpower / 2},
        "ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "Uranium233Cell3",
        "input": {
            "items": [
                {
                    "name": "Uranium233Cell",
                    "count": 4,
                },
                {
                    "name": "ControlCell",
                    "count": 1,
                    "split": 0,
                },
            ]
        },
        "output": {
            "items": [
                {
                    "name": "DepletedUraniumCell",
                    "count": 4,
                }
            ]
        },
        "res_output": {"name": "Heat", "count": fission_fullpower},
        "ticks": 2000,
    }
)

recipes_chem.append(
    {
        "name": "AluminothermicChromiumDust",
        "input": {
            "items": [
                {"name": "AluminiumDust", "count": 1},
                {"name": "ChromiumOxideDust", "count": 1},
            ]
        },
        "output": {
            "items": [{"name": "ChromiumDust", "count": 1}],
        },
        "res_input": {
            "name": "Electricity",
            "count": 10,
        },
        "ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "CinnabarDust",
        "input": {"items": [{"name": "CinnabarDust", "count": 2}]},
        "output": {
            "items": [
                {"name": "Mercury", "count": 1000},
                {"name": "Sulfur", "count": 1},
            ],
        },
        "res_input": {
            "name": "Electricity",
            "count": 10,
        },
        "ticks": 200,
    }
)

recipes_boiler.append(
    {
        "name": "Boiling",
        "input": {
            "items": [{"name": "Water", "count": 50}],
        },
        "res_input": {
            "name": "Heat",
            "count": 110,
        },
        "output": {"items": []},
        "res_output": {
            "name": "Steam",
            "count": 100,
            # "Capacity": 32000,
        },
        "ticks": 200,
        "loss": 10,
    }
)

recipes_steam_turbine.append(
    {
        "name": "Rotating",
        "input": {"items": []},
        "res_input": {"name": "Steam", "count": 300},
        "output": {"items": []},
        "res_output": {"name": "Kinetic", "count": 270},
        "ticks": 200,
        "loss": 10,
    }
)

recipes_generator.append(
    {
        "name": "Generating",
        "input": {"items": []},
        "res_input": {"name": "Kinetic", "count": 270},
        "output": {"items": []},
        "res_output": {"name": "Electricity", "count": 243},
        "ticks": 200,
        "loss": 10,
    }
)

recipes_kinetic_heater.append(
    {
        "name": "Heating",
        "input": {"items": []},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": []},
        "res_output": {"name": "Heat", "count": 18},
        "ticks": 200,
        "loss": 10,
    }
)

recipes_electric_engine.append(
    {
        "name": "Rotating",
        "input": {"items": []},
        "res_input": {"name": "Electricity", "count": 55},
        "output": {"items": []},
        "res_output": {"name": "Kinetic", "count": 50},
        "loss": 10,
        "ticks": 200,
    }
)

recipes_industrial_electric_engine.append(
    {
        "name": "Rotating",
        "input": {"items": []},
        "res_input": {"name": "Electricity", "count": 55 * 50},
        "output": {"items": []},
        "res_output": {"name": "Kinetic", "count": 50 * 50},
        "loss": 10,
        "ticks": 200,
    }
)

recipes_compact_generator.append(
    {
        "name": "Rotating",
        "input": {"items": []},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": []},
        "res_output": {"name": "Electricity", "count": 18},
        "loss": 10,
        "ticks": 200,
    }
)

recipes_steam_engine.append(
    {
        "name": "Rotating",
        "input": {"items": []},
        "res_input": {"name": "Heat", "count": 11},
        "output": {"items": []},
        "res_output": {"name": "Kinetic", "count": 10},
        "ticks": 200,
        "loss": 10,
    }
)

recipes_oven.append(
    {
        "name": "CoalPieceToCoke",
        "input": {"items": [{"name": "Coal", "count": 10}]},
        "output": {
            "items": [
                {"name": "Coke", "count": 10},
                {
                    "name": "Creosote",
                    "count": 250,
                    "Capacity": 32000,
                },
            ]
        },
        "ticks": 2000,
    }
)

recipes_oven.append(
    {
        "name": "LogToCoal",
        "input": {"items": [{"name": "Log", "count": 10}]},
        "output": {
            "items": [
                {"name": "Coal", "count": 10},
                {
                    "name": "Creosote",
                    "count": 100,
                    "Capacity": 32000,
                },
            ]
        },
        "ticks": 2000,
    }
)

recipes_oven.append(
    {
        "name": "PlankToCoal",
        "input": {"items": [{"name": "Plank", "count": 10}]},
        "output": {
            "items": [
                {"name": "Coal", "count": 3},
                {
                    "name": "Creosote",
                    "count": 30,
                    "Capacity": 32000,
                },
            ]
        },
        "ticks": 500,
    }
)

recipes_oven.append(
    {
        "name": "OrgToCoal",
        "input": {"items": [{"name": "Organics", "count": 10}]},
        "output": {
            "items": [
                {"name": "Coal", "count": 2},
                {
                    "name": "Creosote",
                    "count": 20,
                    "Capacity": 32000,
                },
            ]
        },
        "ticks": 500,
    }
)

recipes_oven.append(
    {
        "name": "Terracotta",
        "input": {"items": [{"name": "Clay", "count": 10}]},
        "output": {
            "items": [
                {"name": "Terracotta", "count": 10},
            ]
        },
        "ticks": 1000,
    }
)

for fuel_type, bonus in zip(["Coke"], [1.0]):
    recipes_blast_furnace.append(
        {
            "name": "IronIngotSmelting",
            "input": {
                "items": [
                    {"name": fuel_type, "count": 15},
                    {"name": "IronIngot", "count": 10},
                ]
            },
            "output": {"items": [{"name": "SteelIngot", "count": 10}]},
            "ticks": 2000,
        }
    )

    recipes_blast_furnace.append(
        {
            "name": "IronDustSmelting",
            "input": {
                "items": [
                    {"name": fuel_type, "count": 10},
                    {"name": "IronDust", "count": 10},
                ]
            },
            "output": {"items": [{"name": "SteelIngot", "count": 10}]},
            "ticks": 2000,
        }
    )

    recipes_blast_furnace.append(
        {
            "name": "IronOreDustSmelting",
            "input": {
                "items": [
                    {"name": fuel_type, "count": 20},
                    {"name": "IronOreDust", "count": 10},
                ]
            },
            "output": {"items": [{"name": "SteelIngot", "count": 10}]},
            "ticks": 2000,
        }
    )

    recipes_blast_furnace.append(
        {
            "name": "IronOreDustSmelting" + fuel_type,
            "input": {
                "items": [
                    {"name": fuel_type, "count": 1},
                    {"name": "SteelDust", "count": 10},
                ]
            },
            "output": {"items": [{"name": "SteelIngot", "count": 10}]},
            "ticks": 2000,
        }
    )

recipes_mixer.append(
    {
        "name": "ReinforcedConcrete",
        "input": {
            "items": [
                {"name": "Concrete", "count": 10},
                {"name": "SteelParts", "count": 8},
                {"name": "Water", "count": 100},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "ReinforcedConcrete", "count": 5}]},
        "ticks": 300,
    }
)
recipes_mixer.append(
    {
        "name": "Concrete",
        "input": {
            "items": [
                {"name": "StoneSurface", "count": 5},
                {"name": "Water", "count": 100},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "Concrete", "count": 10}]},
        "ticks": 300,
    }
)
recipes_mixer.append(
    {
        "name": "SSCraft",
        "input": {
            "items": [
                {"name": "IronDust", "count": 10},
                {"name": "ChromiumDust", "count": 3},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "StainlessSteelDust", "count": 10}]},
        "ticks": 400,
    }
)
recipes_mixer.append(
    {
        "name": "SSCraft2",
        "input": {
            "items": [
                {"name": "IronOreDust", "count": 10},
                {"name": "ChromiumDust", "count": 3},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 40},
        "output": {"items": [{"name": "StainlessSteelDust", "count": 10}]},
        "ticks": 500,
    }
)

recipes_mixer.append(
    {
        "name": "PreparedTitaniumOxideCraft",
        "input": {
            "items": [
                {"name": "TitaniumOxideDust", "count": 1},
                {"name": "Coke", "count": 2},
            ],
        },
        "res_input": {
            "name": "Kinetic",
            "count": 10,
        },
        "output": {"items": [{"name": "PreparedTitaniumOxideDust", "count": 1}]},
        "ticks": 200,
        "Scaled": False,
    }
)

# recipes_sep2.append({
# 	"name": "RareSeparating",
# 	"input":{
# 		"items":[
# 			{
# 				"name": "RareEarthDust",
# 				"count": 10
# 			},
#
# 		]
# 	},
# 	"res_input":{
# 		"name": "Kinetic",
# 		"count": 50000
# 	},
# 	"output":{
# 		"items": [
# 			{
# 				"name": "RareMetalsDust",
# 				"count": 1
# 			},
# 			{
# 				"name": "YttriumDust",
# 				"count": 1
# 			},
# 			{
# 				"name": "LutetiumDust",
# 				"count": 1
# 			},
# 			{
# 				"name": "DysprosiumDust",
# 				"count": 1
# 			}
# 		]
# 	},
#
# 	"ticks": 1000,
# })

# recipes_sep2.append({
# "name": "OreWater",
# "input":{
# "items":[
# {
# "name": "OreWater",
# "count": 1000
# },
# ]
# },
# "res_input":{
# "name": "Kinetic",
# "count": 30
# },
# "output":{
# "items": [
# {
# "name": "Clay",
# "count": 1
# },
# ]
# },

# "ticks": 200,
# })

recipes_sep2.append(
    {
        "name": "PlutoniumDust",
        "input": {
            "items": [
                {"name": "DepletedUraniumCell", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 30 * 90},
        "output": {
            "items": [
                {"name": "Cell", "count": 1},
                {"name": "PlutoniumDust", "count": 1, "split": 2},
            ]
        },
        "ticks": 400,
    }
)

recipes_sep2.append(
    {
        "name": "Granite",
        "input": {
            "items": [
                {"name": "GraniteSurface", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 30 * 90},
        "output": {
            "items": [
                {"name": "SandSurface", "count": 1},
                {
                    "name": "TungstenOxideDust",
                    "count": 1,
                    "split": 10,
                },
            ]
        },
        "ticks": 40,
    }
)

recipes_sep2.append(
    {
        "name": "Stone",
        "input": {
            "items": [
                {"name": "StoneSurface", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 30},
        "output": {
            "items": [
                {"name": "SandSurface", "count": 1},
                {
                    "name": "AluminiumOxideDust",
                    "count": 1,
                    "split": 10,
                },
            ]
        },
        "ticks": 100,
    }
)

recipes_sep2.append(
    {
        "name": "Basalt",
        "input": {
            "items": [
                {"name": "BasaltSurface", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 30 * 25},
        "output": {
            "items": [
                {"name": "SandSurface", "count": 1},
                {
                    "name": "AluminiumOxideDust",
                    "count": 1,
                    "split": 5,
                },
                {
                    "name": "TitaniumOxideDust",
                    "count": 1,
                    "split": 10,
                },
            ]
        },
        "ticks": 40,
    }
)

recipes_sep2.append(
    {
        "name": "Sand",
        "input": {
            "items": [
                {"name": "SandSurface", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 30},
        "output": {
            "items": [
                {
                    "name": "SiliconOxide",
                    "count": 1,
                    "split": 2,
                }
            ]
        },
        "ticks": 100,
    }
)

recipes_arc_furnace.append(
    {
        "name": "CopperOreDust",
        "input": {
            "items": [
                {"name": "CopperOreDust", "count": 1},
            ]
        },
        "res_input": {
            "name": "Electricity",
            "count": 20,
        },
        "output": {"items": [{"name": "CopperIngot", "count": 1}]},
        "ticks": 200,
    }
)

recipes_arc_furnace.append(
    {
        "name": "SandSurfaceSmelting",
        "input": {
            "items": [
                {"name": "SandSurface", "count": 1},
            ],
        },
        "res_input": {
            "name": "Electricity",
            "count": 20,
        },
        "output": {"items": [{"name": "Glass", "count": 1}]},
        "ticks": 100,
    }
)

for material in materials:
    if "IsIngot" in material:
        if "SmeltLevel" in material and material["SmeltLevel"] <= 3:
            recipes_arc_furnace.append(
                {
                    "name": material["name"] + "Ingot",
                    "input": {
                        "items": [
                            {"name": material["name"] + "Dust", "count": 1},
                        ]
                    },
                    "res_input": {
                        "name": "Electricity",
                        "count": 20 if material["name"] != "StainlessSteel" else 100,
                    },
                    "output": {
                        "items": [{"name": material["name"] + "Ingot", "count": 1}]
                    },
                    "tier": extract_tier(material),
                    "ticks": 200,
                }
            )

recipes_macerator.append(
    {
        "name": "Pumpkin",
        "input": {
            "items": [
                {"name": "Pumpkin", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "Organics", "count": 1}]},
        "tier": 0,
        "ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "Emerald",
        "input": {
            "items": [
                {"name": "Emerald", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 50},
        "output": {"items": [{"name": "EmeraldDust", "count": 1}]},
        "tier": 0,
        "ticks": 100,
    }
)

recipes_macerator.append(
    {
        "name": "MalachiteCrystal",
        "input": {
            "items": [
                {"name": "MalachiteCrystal", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "CopperOreDust", "count": 2}]},
        "tier": 0,
        "ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "MalachiteCluster",
        "input": {
            "items": [
                {"name": "MalachiteCluster", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "CopperOreDust", "count": 5}]},
        "tier": 0,
        "ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "RutileCrystal",
        "input": {
            "items": [
                {"name": "RutileCrystal", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "TitaniumOxideDust", "count": 2}]},
        "tier": 0,
        "ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "CinnabarCrystal",
        "input": {
            "items": [
                {"name": "CinnabarCrystal", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "CinnabarDust", "count": 2}]},
        "tier": 0,
        "ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "CinnabarCluster",
        "input": {
            "items": [
                {"name": "CinnabarCluster", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "CinnabarDust", "count": 5}]},
        "tier": 0,
        "ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "UraniniteCrystal",
        "input": {
            "items": [
                {"name": "UraniniteCrystal", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "UraniumDust", "count": 2}]},
        "tier": 0,
        "ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "UraniniteCluster",
        "input": {
            "items": [
                {"name": "UraniniteCluster", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {
            "items": [
                {"name": "UraniumDust", "count": 5},
                {"name": "Uranium235Dust", "count": 1},
            ]
        },
        "tier": 0,
        "ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "GravelToSand",
        "input": {
            "items": [
                {"name": "GravelSurface", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "SandSurface", "count": 1}]},
        "tier": 0,
        "ticks": 200,
    }
)

recipes_hammer.append(
    {
        "name": "StoneToGravel",
        "input": {
            "items": [
                {"name": "StoneSurface", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "GravelSurface", "count": 1}]},
        "tier": 0,
        "ticks": 100,
    }
)

recipes_pump.append(
    {
        "name": "Water",
        "input": {"items": []},
        "output": {"items": []},
        "res_output": {"name": "Water", "count": 600},
        "ticks": 6 * 20,
    }
)

recipes_indu.append(
    {
        "name": "SpongeToIngot",
        "input": {
            "items": [
                {"name": "TitaniumSponge", "count": 1},
            ],
        },
        "res_input": {
            "name": "Heat",
            "count": 350,
        },
        "output": {
            "items": [
                {"name": "TitaniumIngot", "count": 1},
            ]
        },
        "tier": 5,
        "ticks": 200,
    }
)

recipes_indu.append(
    {
        "name": "SuperconductorDust",
        "input": {
            "items": [
                {"name": "SuperconductorDust", "count": 1},
            ],
        },
        "res_input": {
            "name": "Heat",
            "count": 100,
        },
        "output": {
            "items": [
                {"name": "SuperconductorIngot", "count": 1},
            ]
        },
        "tier": 5,
        "ticks": 200,
    }
)

recipes_indu.append(
    {
        "name": "TDustToIngot",
        "input": {
            "items": [
                {"name": "TitaniumDust", "count": 1},
            ],
        },
        "res_input": {
            "name": "Heat",
            "count": 350,
        },
        "output": {
            "items": [
                {"name": "TitaniumIngot", "count": 1},
            ]
        },
        "tier": 5,
        "ticks": 200,
    }
)

recipes_indu.append(
    {
        "name": "HardMetalDustToIngot",
        "input": {
            "items": [
                {"name": "HardMetalDust", "count": 1},
            ],
        },
        "res_input": {
            "name": "Heat",
            "count": 900,
        },
        "output": {
            "items": [
                {"name": "HotHardMetalIngot", "count": 1},
            ]
        },
        "ticks": 200,
    }
)

recipes_sep.append(
    {
        "name": "SiliconOxide",
        "input": {"items": [{"name": "SandSurface", "count": 2}]},
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "SiliconOxide", "count": 1}]},
        "ticks": 1000,
    }
)

recipes_mixer.append(
    {
        "name": "Organics",
        "input": {
            "items": [
                {"name": "Organics", "count": 1},
                {"name": "Water", "count": 500},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "Biomass", "count": 500}]},
        "ticks": 200,
    }
)

recipes_mixer.append(
    {
        "name": "HardMetalDust",
        "input": {
            "items": [
                {"name": "TungstenCarbideDust", "count": 4},
                {"name": "CobaltDust", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 100},
        "output": {"items": [{"name": "HardMetalDust", "count": 5}]},
        "ticks": 1000,
    }
)

recipes_mixer.append(
    {
        "name": "SuperconductorDust",
        "input": {
            "items": [
                {"name": "GoldDust", "count": 3},
                {"name": "RareEarthElement", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 100},
        "output": {"items": [{"name": "SuperconductorDust", "count": 3}]},
        "ticks": 300,
    }
)

recipes_electrolyzer.append(
    {
        "name": "AluminiumOxideDust",
        "input": {
            "items": [
                {"name": "AluminiumOxideDust", "count": 1},
            ]
        },
        "res_input": {
            "name": "Electricity",
            "count": 50,
        },
        "output": {"items": [{"name": "AluminiumDust", "count": 1}]},
        "ticks": 200,
    }
)

recipes_electrolyzer.append(
    {
        "name": "EmeraldDust",
        "input": {
            "items": [
                {"name": "EmeraldDust", "count": 2},
            ]
        },
        "res_input": {
            "name": "Electricity",
            "count": 70,
        },
        "output": {
            "items": [
                {"name": "BerylliumDust", "count": 1},
                {"name": "AluminiumOxideDust", "count": 1},
            ]
        },
        "ticks": 200,
    }
)

recipes_electrolyzer.append(
    {
        "name": "AluminiumOreDust",
        "input": {
            "items": [
                {"name": "AluminiumOreDust", "count": 1},
            ]
        },
        "res_input": {
            "name": "Electricity",
            "count": 30,
        },
        "output": {"items": [{"name": "AluminiumDust", "count": 1}]},
        "ticks": 500,
    }
)

recipes_electrolyzer.append(
    {
        "name": "Clay",
        "input": {
            "items": [
                {"name": "Clay", "count": 6},
            ]
        },
        "res_input": {
            "name": "Electricity",
            "count": 1300,
        },
        "output": {
            "items": [
                {"name": "SandSurface", "count": 4},
                {"name": "AluminiumOxideDust", "count": 1},
                {"name": "SodiumDust", "count": 1},
            ]
        },
        "ticks": 40,
    }
)

recipes_electrolyzer.append(
    {
        "name": "SandElectrolyze",
        "input": {"items": [{"name": "SiliconOxide", "count": 1}]},
        "res_input": {"name": "Electricity", "count": 60},
        "output": {"items": [{"name": "Silicon", "count": 1}]},
        "ticks": 200,
    }
)

recipes_electrolyzer.append(
    {
        "name": "WaterElectrolyze",
        "input": {"items": [{"name": "Water", "count": 100}]},
        "res_input": {"name": "Electricity", "count": 280},
        "output": {
            "items": [
                {"name": "Hydrogen", "count": 100},
                {"name": "Oxygen", "count": 200},
            ]
        },
        "ticks": 100,
    }
)

recipes_electrolyzer.append(
    {
        "name": "SaltElectrolyze",
        "input": {
            "items": [
                {"name": "SaltDust", "count": 1},
            ]
        },
        "res_input": {
            "name": "Electricity",
            "count": 10,
        },
        "output": {
            "items": [
                {"name": "SodiumDust", "count": 1},
                {"name": "Chlorine", "count": 1000},
            ]
        },
        "ticks": 200,
    }
)

recipes_electrolyzer.append(
    {
        "name": "PotassiumChloride",
        "input": {
            "items": [
                {"name": "PotassiumChlorideDust", "count": 1},
            ]
        },
        "res_input": {
            "name": "Electricity",
            "count": 10,
        },
        "output": {
            "items": [
                {"name": "PotassiumDust", "count": 1},
                {"name": "Chlorine", "count": 1000},
            ]
        },
        "ticks": 200,
    }
)

recipes_electrolyzer.append(
    {
        "name": "Borax",
        "input": {
            "items": [
                {"name": "BoraxDust", "count": 2},
            ]
        },
        "res_input": {
            "name": "Electricity",
            "count": 50,
        },
        "output": {
            "items": [
                {"name": "SodiumDust", "count": 1},
                {"name": "BoronDust", "count": 1},
            ]
        },
        "ticks": 200,
    }
)

# wood

recipes_cutter.append(
    {
        "name": "LogCutting",
        "input": {
            "items": [
                {"name": "Log", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "Plank", "count": 4}]},
        "ticks": 80,
    }
)
recipes_cutter.append(
    {
        "name": "StoneLogCutting",
        "input": {
            "items": [
                {"name": "StoneLog", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "Plank", "count": 4}]},
        "ticks": 200,
    }
)
recipes_cutter.append(
    {
        "name": "CircuitBoard",
        "input": {
            "items": [
                {"name": "Plank", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "CircuitBoard", "count": 1}]},
        "ticks": 80,
    }
)
recipes_cutter.append(
    {
        "name": "StoneTiles",
        "input": {"items": [{"name": "StoneSurface", "count": 1}]},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": [{"name": "StoneTiles", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "DarkTiles",
        "input": {"items": [{"name": "DarkStoneSurface", "count": 1}]},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": [{"name": "DarkTiles", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "RedTiles",
        "input": {"items": [{"name": "RedStoneSurface", "count": 1}]},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": [{"name": "RedTiles", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "Bricks",
        "input": {"items": [{"name": "StoneTiles", "count": 1}]},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": [{"name": "Bricks", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "RedBricks",
        "input": {"items": [{"name": "RedTiles", "count": 1}]},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": [{"name": "RedBricks", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "DarkBricks",
        "input": {"items": [{"name": "DarkTiles", "count": 1}]},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": [{"name": "DarkBricks", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "TerracottaTiles",
        "input": {"items": [{"name": "Terracotta", "count": 1}]},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": [{"name": "TerracottaTiles", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "TerracottaBricks",
        "input": {"items": [{"name": "TerracottaTiles", "count": 1}]},
        "res_input": {"name": "Kinetic", "count": 20},
        "output": {"items": [{"name": "TerracottaBricks", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ConcreteTiles",
        "input": {
            "items": [
                {"name": "Concrete", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "ConcreteTiles", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ConcreteSmallTiles",
        "input": {
            "items": [
                {"name": "ConcreteTiles", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "ConcreteSmallTiles", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ConcreteBricks",
        "input": {
            "items": [
                {"name": "ConcreteSmallTiles", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "ConcreteBricks", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ReinforcedConcreteTiles",
        "input": {
            "items": [
                {"name": "ReinforcedConcrete", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "ReinforcedConcreteTiles", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ReinforcedConcreteSmallTiles",
        "input": {
            "items": [
                {"name": "ReinforcedConcreteTiles", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "ReinforcedConcreteSmallTiles", "count": 1}]},
        "ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ReinforcedConcreteBricks",
        "input": {
            "items": [
                {"name": "ReinforcedConcreteSmallTiles", "count": 1},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {"items": [{"name": "ReinforcedConcreteBricks", "count": 1}]},
        "ticks": 100,
    }
)
# burning

recipes_elfurn.append(
    {
        "name": "Working",
        "input": {"items": []},
        "res_input": {
            "name": "Electricity",
            "count": 55,
        },
        "output": {
            "items": [],
        },
        "res_output": {
            "name": "Heat",
            "count": 50,
        },
        "ticks": 200,
        "loss": 10,
    }
)

recipes_coil.append(
    {
        "name": "Working",
        "input": {"items": []},
        "res_input": {"name": "Electricity", "count": 380},
        "output": {
            "items": [],
        },
        "res_output": {
            "name": "Heat",
            "count": 342,
        },
        "ticks": 200,
        "loss": 10,
    }
)

recipes_ferm.append(
    {
        "name": "MethaneFromBiomass",
        "input": {
            "items": [
                {"name": "Biomass", "count": 500},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "Methane", "count": 500}]},
        "ticks": 200,
    }
)

recipes_ferm.append(
    {
        "name": "MethaneFromPumpkin",
        "input": {
            "items": [
                {"name": "Pumpkin", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "Methane", "count": 200}]},
        "ticks": 200,
    }
)

recipes_radiator.append(
    {
        "name": "Working",
        "input": {
            "items": [],
        },
        "res_input": {
            "name": "Heat",
            "count": 500,
        },
        "output": {"items": []},
        "ticks": 200,
    }
)

recipes_solar.append(
    {
        "name": "Working",
        "input": {"items": []},
        "output": {"items": []},
        "res_output": {
            "name": "Electricity",
            "count": 50,
        },
        "ticks": 60,
    }
)

recipes_riteg.append(
    {
        "name": "Working",
        "input": {"items": []},
        "output": {"items": []},
        "res_output": {
            "name": "Heat",
            "count": 500,
        },
        "ticks": 60,
    }
)

recipes_chem.append(
    {
        "name": "MineralWater",
        "input": {
            "items": [
                {"name": "MineralWater", "count": 1000},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "SaltDust", "count": 1}]},
        "ticks": 400,
    }
)

recipes_chem.append(
    {
        "name": "MineralWater3",
        "input": {
            "items": [
                {"name": "MineralWater", "count": 1000},
            ]
        },
        "res_input": {"name": "Electricity", "count": 60},
        "output": {"items": [{"name": "BoraxDust", "count": 1, "split": 10}]},
        "ticks": 100,
    }
)

recipes_chem.append(
    {
        "name": "MineralWater2",
        "input": {
            "items": [
                {"name": "MineralWater", "count": 1000},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "PotassiumChlorideDust", "count": 1}]},
        "ticks": 400,
    }
)

recipes_chem.append(
    {
        "name": "TungstenCarbideDust",
        "input": {
            "items": [
                {"name": "TungstenDust", "count": 1},
                {"name": "Coke", "count": 2},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "TungstenCarbideDust", "count": 1}]},
        "ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "TitaniumTetrachloride",
        "input": {
            "items": [
                {"name": "PreparedTitaniumOxideDust", "count": 1},
                {"name": "Chlorine", "count": 1000},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "TitaniumTetrachloride", "count": 1000}]},
        "ticks": 200,
        "Scaled": False,
    }
)

recipes_chem.append(
    {
        "name": "TitaniumSponge",
        "input": {
            "items": [
                {"name": "TitaniumTetrachloride", "count": 1000},
                {"name": "AluminiumDust", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {
            "items": [
                {"name": "TitaniumSponge", "count": 1},
            ],
        },
        "ticks": 200,
        "Scaled": False,
    }
)

recipes_chem.append(
    {
        "name": "TungstenOxide",
        "input": {
            "items": [
                {"name": "TungstenOxideDust", "count": 1},
                {"name": "Hydrogen", "count": 1000},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "TungstenDust", "count": 1}]},
        "ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "CobaltOxide",
        "input": {
            "items": [
                {"name": "CobaltOxideDust", "count": 1},
                {"name": "Hydrogen", "count": 1000},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "CobaltDust", "count": 1}]},
        "ticks": 200,
        "Scaled": False,
    }
)

for i in {"ProducerGas", "Methane", "Hydrogen", "Gasoline"}:
    recipes_gasturb.append(
        {
            "input": {"items": [{"name": i, "count": 14 * 1000}]},
            "output": {"items": []},
            "res_output": {
                "name": "Kinetic",
                "count": named_material(i)["Burnable"]["HeatPerTick"] * 14,
            },
            "ticks": named_material(i)["Burnable"]["BurnTime"],
            "name": i,
        }
    )

    recipes_combustion.append(
        {
            "name": i,
            "input": {"items": [{"name": i, "count": 1000}]},
            "output": {"items": []},
            "res_output": {
                "name": "Kinetic",
                "count": named_material(i)["Burnable"]["HeatPerTick"],
            },
            "ticks": named_material(i)["Burnable"]["BurnTime"],
        }
    )

recipes_pyro.append(
    {
        "name": "Coal",
        "input": {
            "items": [
                {"name": "Coal", "count": 1},
            ]
        },
        "res_input": {"name": "Heat", "count": 10},
        "output": {
            "items": [
                {"name": "Coke", "count": 1},
                {"name": "RawOil", "count": 100},
                {"name": "ProducerGas", "count": 100},
            ]
        },
        "ticks": 400,
    }
)

recipes_pyro.append(
    {
        "name": "CoalSteam",
        "input": {
            "items": [
                {"name": "Coal", "count": 1},
                {"name": "Steam", "count": 200},
            ]
        },
        "res_input": {"name": "Heat", "count": 10},
        "output": {
            "items": [
                {"name": "Coke", "count": 1},
                {"name": "ProducerGas", "count": 500},
            ]
        },
        "ticks": 400,
    }
)

recipes_pyro.append(
    {
        "name": "RawOil",
        "input": {
            "items": [
                {"name": "RawOil", "count": 2000},
            ]
        },
        "res_input": {"name": "Heat", "count": 15},
        "output": {
            "items": [
                {"name": "HeavyOil", "count": 500},
                {"name": "Gasoline", "count": 100},
                {"name": "Methane", "count": 500},
            ]
        },
        "ticks": 200,
    }
)

recipes_pyro.append(
    {
        "name": "RawOilSteam",
        "input": {
            "items": [
                {"name": "RawOil", "count": 1000 * 5},
                {"name": "Steam", "count": 1000},
            ]
        },
        "res_input": {"name": "Heat", "count": 100},
        "output": {
            "items": [
                {"name": "HeavyOil", "count": 150 * 2},
                {"name": "Gasoline", "count": 400 * 2},
                {"name": "Methane", "count": 500 * 2},
            ]
        },
        "ticks": 200,
    }
)

recipes_pyro.append(
    {
        "name": "HeavyOil",
        "input": {
            "items": [
                {"name": "HeavyOil", "count": 1000},
                {"name": "Steam", "count": 200},
            ]
        },
        "res_input": {"name": "Heat", "count": 10},
        "output": {
            "items": [
                {"name": "Gasoline", "count": 750},
            ]
        },
        "ticks": 200,
    }
)

recipes_pyro.append(
    {
        "name": "Gasoline",
        "input": {
            "items": [
                {"name": "Gasoline", "count": 1000},
                {"name": "Steam", "count": 200},
            ]
        },
        "res_input": {"name": "Heat", "count": 10},
        "output": {
            "items": [
                {"name": "Methane", "count": 750},
            ]
        },
        "ticks": 200,
    }
)

recipes_pyro.append(
    {
        "name": "Methane",
        "input": {
            "items": [
                {"name": "Methane", "count": 800 * 5},
                {"name": "Steam", "count": 200 * 20},
            ]
        },
        "res_input": {"name": "Heat", "count": 100},
        "output": {
            "items": [
                {"name": "ProducerGas", "count": 1000 * 5},
            ]
        },
        "ticks": 200,
    }
)

recipes_pyro.append(
    {
        "name": "Methane2",
        "input": {"items": [{"name": "Methane", "count": 800 * 5}]},
        "res_input": {"name": "Heat", "count": 50},
        "output": {
            "items": [
                {"name": "ProducerGas", "count": 500 * 5},
            ]
        },
        "ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "Ethylene",
        "input": {
            "items": [
                {"name": "ProducerGas", "count": 1000},
                {
                    "name": "Catalyst",
                    "count": 1,
                    "split": 0,
                },
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {
            "items": [
                {
                    "name": "Ethylene",
                    "count": 1000,
                },
            ]
        },
        "ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "Sulfur",
        "input": {
            "items": [
                {"name": "HeavyOil", "count": 150},
                {"name": "Water", "count": 250},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {
            "items": [
                {"name": "Sulfur", "count": 1},
            ]
        },
        "ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "SulfuricAcid",
        "input": {
            "items": [
                {"name": "Sulfur", "count": 1},
                {"name": "Oxygen", "count": 250},
                {"name": "Water", "count": 250},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {
            "items": [
                {"name": "SulfuricAcid", "count": 1000},
            ]
        },
        "ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "Plastic1",
        "input": {
            "items": [
                {"name": "Ethylene", "count": 1000},
                {"name": "Coal", "count": 1},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {
            "items": [
                {"name": "Plastic", "count": 1},
            ]
        },
        "ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "Plastic2",
        "input": {
            "items": [
                {"name": "Ethylene", "count": 1000},
                {"name": "HeavyOil", "count": 150},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {
            "items": [
                {"name": "Plastic", "count": 1},
            ]
        },
        "ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "ProducerGas",
        "input": {
            "items": [
                {"name": "ProducerGas", "count": 1000},
            ]
        },
        "res_input": {"name": "Electricity", "count": 10},
        "output": {
            "items": [
                {"name": "Hydrogen", "count": 750},
            ]
        },
        "ticks": 200,
    }
)

recipes_filtering_unit.append(
    {
        "name": "OreWater",
        "input": {
            "items": [
                {"name": "OreWater", "count": 500},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {
            "items": [
                {"name": "Clay", "count": 1},
            ]
        },
        "ticks": 200,
    }
)

recipes_filtering_unit.append(
    {
        "name": "OreWater2",
        "input": {
            "items": [
                {"name": "OreWater", "count": 500},
                {"name": "FilteringCell", "count": 1, "split": 10},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {
            "items": [
                {"name": "AluminiumOreDust", "count": 1, "split": 2},
            ]
        },
        "ticks": 200,
    }
)

recipes_filtering_unit.append(
    {
        "name": "OreWater3",
        "input": {
            "items": [
                {"name": "OreWater", "count": 500},
                {"name": "FilteringCell", "count": 1, "split": 10},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {
            "items": [
                {"name": "CopperOreDust", "count": 1, "split": 2},
            ]
        },
        "ticks": 200,
    }
)

recipes_filtering_unit.append(
    {
        "name": "OreWater4",
        "input": {
            "items": [
                {"name": "OreWater", "count": 500},
                {"name": "FilteringCell", "count": 1, "split": 10},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {
            "items": [
                {"name": "UraniumOreDust", "count": 1, "split": 2},
            ]
        },
        "ticks": 200,
    }
)

recipes_filtering_unit.append(
    {
        "name": "OreWater5",
        "input": {
            "items": [
                {"name": "OreWater", "count": 500},
                {"name": "FilteringCell", "count": 1, "split": 10},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 10},
        "output": {
            "items": [
                {"name": "IronOreDust", "count": 1, "split": 2},
            ]
        },
        "ticks": 200,
    }
)

for i in {"IronOreDust", "CopperOreDust"}:
    recipes_chemical_bath.append(
        {
            "name": i,
            "input": {
                "items": [
                    {"name": "Mercury", "count": 500},
                    {
                        "name": i,
                        "count": 2,
                    },
                ]
            },
            "res_input": {"name": "Kinetic", "count": 10},
            "output": {
                "items": [
                    {
                        "name": "GoldDust",
                        "count": 1,
                    },
                ]
            },
            "ticks": 200,
        }
    )

recipes_chemical_bath.append(
    {
        "name": "RareEarthElement",
        "input": {
            "items": [
                {"name": "AluminiumOreDust", "count": 10},
                {"name": "SulfuricAcid", "count": 1000},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 30},
        "output": {"items": [{"name": "RareEarthElement", "count": 1}]},
        "ticks": 1000,
    }
)

recipes_chemical_bath.append(
    {
        "name": "CobaltOxideDust",
        "input": {
            "items": [
                {"name": "IronOreDust", "count": 10},
                {"name": "SulfuricAcid", "count": 1000},
            ]
        },
        "res_input": {"name": "Kinetic", "count": 30},
        "output": {"items": [{"name": "CobaltOxideDust", "count": 1}]},
        "ticks": 1000,
    }
)

recipes_freezer.append(
    {
        "name": "HotHardmetalIngot",
        "input": {"items": [{"name": "HotHardMetalIngot", "count": 1}]},
        "res_input": {"name": "Kinetic", "count": 100},
        "output": {"items": [{"name": "HardMetalIngot", "count": 1}]},
        "ticks": 200,
    }
)

recipes_freezer.append(
    {
        "name": "HotNeutroniumIngot",
        "input": {"items": [{"name": "HotNeutroniumIngot", "count": 1}]},
        "res_input": {"name": "Kinetic", "count": 1000},
        "output": {"items": [{"name": "NeutroniumIngot", "count": 1}]},
        "ticks": 200,
    }
)

recipes_computer.append(
    {
        "name": "Computations",
        "input": {"items": []},
        "res_input": {"name": "Electricity", "count": 10},
        "output": {"items": [{"name": "Computations", "count": 1}]},
        "ticks": 40,
    }
)

recipes_q_computer.append(
    {
        "name": "QuantumComputations",
        "input": {"items": []},
        "res_input": {"name": "Electricity", "count": 100},
        "output": {"items": [{"name": "Computations", "count": 40}]},
        "ticks": 40,
    }
)

recipes_portal.append(
    {
        "name": "Ping",
        "input": {"items": []},
        "res_input": {
            "name": "Electricity",
            "count": 2 * fission_fullpower * 0.9 * 0.9,
        },
        "output": {"items": [{"name": "MothershipPing", "count": 1}]},
        "ticks": 1000,
    }
)

append_recipe_hand_press(
    {
        "name": "Column",
        "input": {"items": [{"name": "StoneSurface", "count": 1}]},
        "output": {"items": [{"name": "Column", "count": 1}]},
        "ticks": 20,
    }
)

append_recipe_hand_press(
    {
        "name": "FluetedColumn",
        "input": {"items": [{"name": "Column", "count": 1}]},
        "output": {"items": [{"name": "FluetedColumn", "count": 1}]},
        "ticks": 20,
    }
)

append_recipe_hand_press(
    {
        "name": "GlassBlock",
        "input": {"items": [{"name": "Glass", "count": 1}]},
        "output": {"items": [{"name": "GlassBlock", "count": 1}]},
        "ticks": 10,
    }
)

append_recipe_hand_press(
    {
        "name": "PlasticBlock",
        "input": {"items": [{"name": "Plastic", "count": 1}]},
        "output": {"items": [{"name": "PlasticBlock", "count": 1}]},
        "ticks": 10,
    }
)

append_recipe_hand_press(
    {
        "name": "DangerBlock",
        "input": {"items": [{"name": "Concrete", "count": 1}]},
        "output": {"items": [{"name": "DangerBlock", "count": 1}]},
        "ticks": 20,
    }
)

append_recipe_hand_press(
    {
        "name": "BasicPlatform",
        "input": {"items": [{"name": "SandSurface", "count": 1}]},
        "output": {"items": [{"name": "BasicPlatform", "count": 1}]},
        "ticks": 10,
    }
)

append_recipe_hand_press(
    {
        "name": "RustyCopperCasing",
        "input": {"items": [{"name": "CopperCasing", "count": 1}]},
        "output": {"items": [{"name": "RustyCopperCasing", "count": 1}]},
        "ticks": 20,
    }
)

append_recipe_hand_press(
    {
        "name": "RustyIronCasing",
        "input": {"items": [{"name": "SteelCasing", "count": 1}]},
        "output": {"items": [{"name": "RustyIronCasing", "count": 1}]},
        "ticks": 20,
    }
)

for i in [
    "Circuit",
    "AdvancedCircuit",
    "Processor",
    "QuantumCircuit",
    "QuantumProcessor",
    "QuantumBrain",
]:
    recipes_computer.append(
        {
            "name": i,
            "input": {"items": [{"name": i, "count": 1}]},
            "res_input": {"name": "Electricity", "count": 40},
            "output": {"items": [{"name": i, "count": 1}]},
            "ticks": 40,
        }
    )

objects_array.append(
    {"class": recipe_dictionary, "name": "Multitool", "recipes": recipes_wrench}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "BlastFurnace",
        "recipes": recipes_blast_furnace,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Oven", "recipes": recipes_oven}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Smelter", "recipes": recipes_smelter}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Macerator", "recipes": recipes_macerator}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Boiler", "recipes": recipes_boiler}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Generator", "recipes": recipes_generator}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "ElectricEngine",
        "recipes": recipes_electric_engine,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "StirlingEngine",
        "recipes": recipes_steam_engine,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Pump", "recipes": recipes_pump}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Separator", "recipes": recipes_sep}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "IndustrialSeparator", "recipes": recipes_sep2}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Press", "recipes": recipes_press}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "ArcSmelter", "recipes": recipes_arc_furnace}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "SteamTurbine",
        "recipes": recipes_steam_turbine,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Electrolyzer",
        "recipes": recipes_electrolyzer,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "CuttingMachine", "recipes": recipes_cutter}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Furnace", "recipes": recipes_furnace}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "ElectricFurnace", "recipes": recipes_elfurn}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Fermenter", "recipes": recipes_ferm}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "MultitoolRobotArm",
        "recipes": recipes_toolarm,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "AutomaticHammer", "recipes": recipes_hammer}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Mixer", "recipes": recipes_mixer}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Radiator", "recipes": recipes_radiator}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "SolarPanel", "recipes": recipes_solar}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "ChemReactor", "recipes": recipes_chem}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "InductionCoil", "recipes": recipes_coil}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "IndustrialSmelter", "recipes": recipes_indu}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "HeatExchanger", "recipes": recipes_exch}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "InverseHeatExchanger",
        "recipes": recipes_iexch,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Freezer", "recipes": recipes_freezer}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "CombustionEngine",
        "recipes": recipes_combustion,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "PyrolysisUnit", "recipes": recipes_pyro}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Computer", "recipes": recipes_computer}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "CompactGenerator",
        "recipes": recipes_compact_generator,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "FissionReactor", "recipes": recipes_fission}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "AutomaticFarm", "recipes": recipes_farm}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "AtmosphericCondenser",
        "recipes": recipes_condens,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Assembler", "recipes": recipes_assembler}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "GasTurbine", "recipes": recipes_gasturb}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "FilteringUnit",
        "recipes": recipes_filtering_unit,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Portal", "recipes": recipes_portal}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "ChemicalBath",
        "recipes": recipes_chemical_bath,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Riteg", "recipes": recipes_riteg}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "IndustrialSteamTurbine",
        "recipes": recipes_industrial_steam_turbine,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "FusionReactor",
        "recipes": recipes_fusion_reactor,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "IndustrialBoiler",
        "recipes": recipes_industrial_boiler,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "IndustrialElectricEngine",
        "recipes": recipes_industrial_electric_engine,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "KineticHeater",
        "recipes": recipes_kinetic_heater,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Hand", "recipes": recipes_hand}
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/misc.json", data)
