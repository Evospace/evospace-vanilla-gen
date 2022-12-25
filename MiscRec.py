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

recipes_hand = []


def append_recipe(recipe):
    item_count = 0
    for item in recipe["Input"]["Items"]:
        item_count = item_count + item["Count"]

    level = extract_tier(recipe["Output"]["Items"][0]["name"]) + 1

    dec_recipe = copy.deepcopy(recipe)

    recipes_hand.append(recipe)

    output = copy.deepcopy(dec_recipe["Input"])

    dec_recipe["Ticks"] = max(min(item_count * 10, 400), 20)
    dec_recipe["ResourceInput"] = {"name": "Electricity", "Count": 20 * level}
    recipes_assembler.append(dec_recipe)


def append_recipe_hand_press(recipe):
    item_count = 0
    for item in recipe["Input"]["Items"]:
        item_count = item_count + item["Count"]

    dec_recipe = copy.deepcopy(recipe)

    recipes_hand.append(recipe)

    output = copy.deepcopy(dec_recipe["Input"])

    dec_recipe["Ticks"] = 60
    dec_recipe["ResourceInput"] = {"name": "Kinetic", "Count": 100}
    recipes_press.append(dec_recipe)


# wrenching

recipes_industrial_steam_turbine.append(
    {
        "name": "Rotating",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Steam", "Count": fission_fullpower * 0.9},
        "Output": {"Items": []},
        "ResourceOutput": {
            "name": "Electricity",
            "Count": fission_fullpower * 0.9 * 0.9,
        },
        "Ticks": 200,
        "Loss": 10,
    }
)

recipes_industrial_boiler.append(
    {
        "name": "Boiling",
        "Input": {
            "Items": [
                {"name": "Water", "Count": 2000},
            ]
        },
        "ResourceInput": {"name": "Heat", "Count": fission_fullpower},
        "Output": {"Items": []},
        "ResourceOutput": {"name": "Steam", "Count": fission_fullpower * 0.9},
        "Ticks": 200,
    }
)

recipes_fusion_reactor.append(
    {
        "name": "HotNeutroniumIngot1",
        "Input": {"Items": [{"name": "ProducerGas", "Count": 1000}]},
        "ResourceInput": {
            "name": "Electricity",
            "Count": fission_fullpower * 0.9 * 0.9,
        },
        "Output": {"Items": [{"name": "HotNeutroniumIngot", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_fusion_reactor.append(
    {
        "name": "HotNeutroniumIngot2",
        "Input": {"Items": [{"name": "ProducerGas", "Count": 3000}]},
        "ResourceInput": {
            "name": "Electricity",
            "Count": 2 * fission_fullpower * 0.9 * 0.9,
        },
        "Output": {"Items": [{"name": "HotNeutroniumIngot", "Count": 1 * 3}]},
        "Ticks": 200 * 2,
    }
)

recipes_fusion_reactor.append(
    {
        "name": "HotNeutroniumIngot4",
        "Input": {"Items": [{"name": "UltimateCatalyst", "Count": 1, "split": 0}]},
        "ResourceInput": {
            "name": "Electricity",
            "Count": fission_fullpower * 0.9 * 0.9,
        },
        "Output": {"Items": [{"name": "HotNeutroniumIngot", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_fusion_reactor.append(
    {
        "name": "HotNeutroniumIngot3",
        "Input": {"Items": [{"name": "UltimateCatalyst", "Count": 3, "split": 0}]},
        "ResourceInput": {
            "name": "Electricity",
            "Count": 2 * fission_fullpower * 0.9 * 0.9,
        },
        "Output": {"Items": [{"name": "HotNeutroniumIngot", "Count": 1 * 3}]},
        "Ticks": 200 * 2,
    }
)

recipes_smelter.append(
    {
        "name": "Glass",
        "Input": {
            "Items": [
                {"name": "SandSurface", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Heat", "Count": 10},
        "Output": {"Items": [{"name": "Glass", "Count": 1}]},
        "Ticks": 200,
    }
)

for list in (simple_deco, wooden_misc, simple_single, simple_blocks, static_mesh_block):
    for one in list:
        recipes_wrench.append(
            {
                "name": one["name"] + "Wrenching",
                "Ticks": 20,
                "Input": {"Items": [{"name": one["name"], "Count": 1}]},
                "Output": {"Items": [{"name": one["name"], "Count": 1}]},
            }
        )

# other

append_recipe(
    {
        "name": "Cell",
        "Input": {
            "Items": [
                {"name": "StainlessSteelPlate", "Count": 1},
                {"name": "StainlessSteelParts", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "Cell", "Count": 1}]},
        "Ticks": 200,
    }
)

append_recipe(
    {
        "name": "Cell2",
        "Input": {
            "Items": [
                {"name": "DepletedUraniumCell", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "Cell", "Count": 1}]},
        "Ticks": 200,
    }
)

append_recipe(
    {
        "name": "UraniumCell",
        "Input": {
            "Items": [
                {"name": "Uranium235Dust", "Count": 3},
                {"name": "UraniumDust", "Count": 20},
                {"name": "Cell", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "UraniumCell", "Count": 1}]},
        "Ticks": 200,
    }
)

append_recipe(
    {
        "name": "ThoriumCell",
        "Input": {
            "Items": [
                {"name": "ThoriumDust", "Count": 20},
                {"name": "Cell", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "ThoriumCell", "Count": 1}]},
        "Ticks": 200,
    }
)

append_recipe(
    {
        "name": "Uranium233Cell",
        "Input": {
            "Items": [
                {"name": "Uranium233Dust", "Count": 3},
                {"name": "Cell", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "Uranium233Cell", "Count": 1}]},
        "Ticks": 200,
    }
)

append_recipe(
    {
        "name": "PlutoniumCell",
        "Input": {
            "Items": [
                {"name": "PlutoniumDust", "Count": 3},
                {"name": "Cell", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "PlutoniumCell", "Count": 1}]},
        "Ticks": 200,
    }
)

append_recipe(
    {
        "name": "FilteringCell",
        "Input": {
            "Items": [
                {"name": "Coal", "Count": 10},
                {"name": "Cell", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "FilteringCell", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "Circuit",
        "Input": {
            "Items": [
                {"name": "CircuitBoard", "Count": 1},
                {"name": "CopperWire", "Count": 6},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "Circuit", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "AdvancedCircuit",
        "Input": {
            "Items": [{"name": "Silicon", "Count": 1}, {"name": "Circuit", "Count": 1}]
        },
        "ResourceInput": {"name": "Electricity", "Count": 30},
        "Output": {"Items": [{"name": "AdvancedCircuit", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "SiliconWafer",
        "Input": {
            "Items": [
                {"name": "Silicon", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 100},
        "Output": {"Items": [{"name": "SiliconWafer", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "Processor",
        "Input": {
            "Items": [
                {"name": "SiliconWafer", "Count": 1},
                {"name": "AdvancedCircuit", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 80},
        "Output": {"Items": [{"name": "Processor", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "QuantumBrain",
        "Input": {
            "Items": [
                {"name": "QuantumProcessor", "Count": 2},
                {"name": "UltimateCatalyst", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 1000},
        "Output": {"Items": [{"name": "QuantumBrain", "Count": 1}]},
        "Ticks": 200,
    }
)

append_recipe(
    {
        "name": "Catalyst",
        "Input": {
            "Items": [
                {"name": "Cell", "Count": 1},
                {"name": "GoldWire", "Count": 10},
                {"name": "Coal", "Count": 4},
            ]
        },
        "Output": {"Items": [{"name": "Catalyst", "Count": 1}]},
        "Ticks": 200,
    }
)

append_recipe(
    {
        "name": "UltimateCatalyst",
        "Input": {
            "Items": [
                {"name": "Cell", "Count": 1},
                {"name": "NeutroniumParts", "Count": 8},
                {"name": "Coke", "Count": 10},
            ]
        },
        "Output": {"Items": [{"name": "UltimateCatalyst", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "AdvancedCircuitBoard",
        "Input": {
            "Items": [
                {"name": "Plastic", "Count": 1},
                {"name": "GoldWire", "Count": 3},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 20},
        "Output": {"Items": [{"name": "AdvancedCircuitBoard", "Count": 1}]},
        "Ticks": 80,
    }
)

recipes_assembler.append(
    {
        "name": "Processor2",
        "Input": {
            "Items": [
                {"name": "SiliconWafer", "Count": 1},
                {"name": "AdvancedCircuitBoard", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 80},
        "Output": {"Items": [{"name": "Processor", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "QuantumCore",
        "Input": {
            "Items": [
                {"name": "RareEarthElement", "Count": 1},
                {"name": "CopperParts", "Count": 2},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 1000},
        "Output": {"Items": [{"name": "QuantumCore", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "QuantumCircuit",
        "Input": {
            "Items": [
                {"name": "QuantumCore", "Count": 2},
                {"name": "AdvancedCircuitBoard", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 1000 / 7},
        "Output": {"Items": [{"name": "QuantumCircuit", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "QuantumProcessor",
        "Input": {
            "Items": [
                {"name": "QuantumCircuit", "Count": 1},
                {"name": "Processor", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 2000 / 13},
        "Output": {"Items": [{"name": "QuantumProcessor", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "CopperWire",
        "Input": {
            "Items": [
                {"name": "CopperIngot", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "CopperWire", "Count": 2}]},
        "Ticks": 100,
    }
)

recipes_assembler.append(
    {
        "name": "SuperconductorWire",
        "Input": {
            "Items": [
                {"name": "SuperconductorIngot", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 100},
        "Output": {"Items": [{"name": "SuperconductorWire", "Count": 2}]},
        "Ticks": 100,
    }
)

recipes_assembler.append(
    {
        "name": "Battery",
        "Input": {
            "Items": [
                {"name": "SulfuricAcid", "Count": 100},
                {"name": "CopperParts", "Count": 1},
                {"name": "StainlessSteelPlate", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "Battery", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_assembler.append(
    {
        "name": "GoldWire",
        "Input": {
            "Items": [
                {"name": "GoldIngot", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "GoldWire", "Count": 2}]},
        "Ticks": 100,
    }
)

append_recipe(
    {
        "name": "ReflectorCell",
        "Input": {
            "Items": [
                {"name": "Cell", "Count": 1},
                {"name": "BerylliumDust", "Count": 3},
            ]
        },
        "Output": {"Items": [{"name": "ReflectorCell", "Count": 1}]},
        "Ticks": 100,
    }
)

append_recipe(
    {
        "name": "ControlCell",
        "Input": {
            "Items": [
                {"name": "Cell", "Count": 1},
                {"name": "BoronDust", "Count": 3},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 1000 / 9},
        "Output": {"Items": [{"name": "ControlCell", "Count": 1}]},
        "Ticks": 100,
    }
)

recipes_condens.append(
    {
        "name": "Water",
        "Input": {"Items": []},
        "Output": {"Items": [{"name": "Water", "Count": 250}]},
        "Ticks": 200,
    }
)

recipes_condens.append(
    {
        "name": "Oxygen",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": [{"name": "Oxygen", "Count": 250}]},
        "Ticks": 200,
    }
)

recipes_condens.append(
    {
        "name": "Nitrogen",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": [{"name": "Nitrogen", "Count": 1000}]},
        "Ticks": 200,
    }
)

recipes_condens.append(
    {
        "name": "Helium",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Kinetic", "Count": 40},
        "Output": {"Items": [{"name": "Helium", "Count": 100}]},
        "Ticks": 200,
    }
)

recipes_condens.append(
    {
        "name": "Methane",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Kinetic", "Count": 40},
        "Output": {"Items": [{"name": "Methane", "Count": 80}]},
        "Ticks": 200,
    }
)

recipes_condens.append(
    {
        "name": "Hydrogen",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Kinetic", "Count": 40},
        "Output": {"Items": [{"name": "Hydrogen", "Count": 50}]},
        "Ticks": 200,
    }
)

recipes_farm.append(
    {
        "name": "Logs",
        "Input": {"Items": [{"name": "Water", "Count": 625}]},
        "Output": {"Items": [{"name": "Log", "Count": 15}]},
        "Ticks": 2000,
    }
)

recipes_farm.append(
    {
        "name": "Pumpkin",
        "Input": {"Items": [{"name": "Water", "Count": 625}]},
        "Output": {"Items": [{"name": "Pumpkin", "Count": 10}]},
        "Ticks": 1000,
    }
)

recipes_centrifuge.append(
    {
        "name": "DepletedUraniumCell",
        "Input": {"Items": [{"name": "DepletedUraniumCell", "Count": 1}]},
        "Output": {
            "Items": [
                {
                    "name": "PlutoniumDust",
                    "Count": 1,
                    "split": 10,
                }
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 100},
        "Ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "UraniumCell",
        "Input": {"Items": [{"name": "UraniumCell", "Count": 1}]},
        "Output": {"Items": [{"name": "DepletedUraniumCell", "Count": 1}]},
        "ResourceOutput": {"name": "Heat", "Count": 7100},
        "Ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "UraniumCell2",
        "Input": {
            "Items": [
                {"name": "UraniumCell", "Count": 2},
                {
                    "name": "ControlCell",
                    "Count": 1,
                    "split": 0,
                },
            ]
        },
        "Output": {"Items": [{"name": "DepletedUraniumCell", "Count": 2}]},
        "ResourceOutput": {"name": "Heat", "Count": 7100 * 2.2},
        "Ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "UraniumCell3",
        "Input": {
            "Items": [
                {"name": "UraniumCell", "Count": 3},
                {
                    "name": "ControlCell",
                    "Count": 1,
                    "split": 0,
                },
            ]
        },
        "Output": {"Items": [{"name": "DepletedUraniumCell", "Count": 3}]},
        "ResourceOutput": {"name": "Heat", "Count": 7100 * 3.3},
        "Ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "UraniumCell4",
        "Input": {
            "Items": [
                {"name": "UraniumCell", "Count": 3},
                {
                    "name": "ControlCell",
                    "Count": 5,
                    "split": 0,
                },
            ]
        },
        "Output": {"Items": [{"name": "DepletedUraniumCell", "Count": 3}]},
        "ResourceOutput": {"name": "Heat", "Count": 7100 * 3.3 / 2},
        "Ticks": 2000 * 2,
    }
)

recipes_fission.append(
    {
        "name": "ControlCell3",
        "Input": {
            "Items": [
                {"name": "UraniumCell", "Count": 1},
                {
                    "name": "ControlCell",
                    "Count": 3,
                    "split": 0,
                },
            ]
        },
        "Output": {"Items": [{"name": "DepletedUraniumCell", "Count": 1}]},
        "ResourceOutput": {"name": "Heat", "Count": 7100 / 4},
        "Ticks": 8000 * 0.9 * 0.9,
    }
)

recipes_fission.append(
    {
        "name": "ThoriumCell",
        "Input": {
            "Items": [
                {
                    "name": "UraniumCell",
                    "Count": 3,
                },
                {
                    "name": "ReflectorCell",
                    "Count": 1,
                    "split": 0,
                },
                {
                    "name": "ThoriumCell",
                    "Count": 2,
                },
            ]
        },
        "Output": {
            "Items": [
                {"name": "DepletedUraniumCell", "Count": 3},
                {
                    "name": "Uranium233Cell",
                    "Count": 2,
                },
            ]
        },
        "ResourceOutput": {"name": "Heat", "Count": 200},
        "Ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "PlutoniumCell",
        "Input": {
            "Items": [
                {
                    "name": "PlutoniumCell",
                    "Count": 1,
                },
                {
                    "name": "ReflectorCell",
                    "Count": 1,
                    "split": 0,
                },
                {
                    "name": "ThoriumCell",
                    "Count": 3,
                },
            ]
        },
        "Output": {
            "Items": [
                {
                    "name": "Uranium233Cell",
                    "Count": 3,
                },
                {"name": "DepletedUraniumCell", "Count": 1},
            ]
        },
        "ResourceOutput": {"name": "Heat", "Count": 200},
        "Ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "PlutoniumCell2",
        "Input": {
            "Items": [
                {
                    "name": "PlutoniumCell",
                    "Count": 1,
                },
                {
                    "name": "ReflectorCell",
                    "Count": 2,
                    "split": 0,
                },
                {
                    "name": "ThoriumCell",
                    "Count": 6,
                },
            ]
        },
        "Output": {
            "Items": [
                {
                    "name": "Uranium233Cell",
                    "Count": 6,
                },
                {"name": "DepletedUraniumCell", "Count": 1},
            ]
        },
        "ResourceOutput": {"name": "Heat", "Count": 200},
        "Ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "ControlCell",
        "Input": {
            "Items": [
                {"name": "UraniumCell", "Count": 1},
                {
                    "name": "ControlCell",
                    "Count": 1,
                    "split": 0,
                },
            ]
        },
        "Output": {"Items": [{"name": "DepletedUraniumCell", "Count": 1}]},
        "ResourceOutput": {"name": "Heat", "Count": 7100 / 2},
        "Ticks": 4000 * 0.9,
    }
)

recipes_fission.append(
    {
        "name": "Uranium233Cell",
        "Input": {
            "Items": [
                {
                    "name": "Uranium233Cell",
                    "Count": 1,
                },
                {
                    "name": "ControlCell",
                    "Count": 1,
                    "split": 0,
                },
            ]
        },
        "Output": {
            "Items": [
                {
                    "name": "DepletedUraniumCell",
                    "Count": 1,
                }
            ]
        },
        "ResourceOutput": {"name": "Heat", "Count": 7100 * 3.3},
        "Ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "Uranium233Cell2",
        "Input": {
            "Items": [
                {
                    "name": "Uranium233Cell",
                    "Count": 2,
                },
                {
                    "name": "ControlCell",
                    "Count": 1,
                    "split": 0,
                },
            ]
        },
        "Output": {
            "Items": [
                {
                    "name": "DepletedUraniumCell",
                    "Count": 2,
                }
            ]
        },
        "ResourceOutput": {"name": "Heat", "Count": fission_fullpower / 2},
        "Ticks": 2000,
    }
)

recipes_fission.append(
    {
        "name": "Uranium233Cell3",
        "Input": {
            "Items": [
                {
                    "name": "Uranium233Cell",
                    "Count": 4,
                },
                {
                    "name": "ControlCell",
                    "Count": 1,
                    "split": 0,
                },
            ]
        },
        "Output": {
            "Items": [
                {
                    "name": "DepletedUraniumCell",
                    "Count": 4,
                }
            ]
        },
        "ResourceOutput": {"name": "Heat", "Count": fission_fullpower},
        "Ticks": 2000,
    }
)

recipes_chem.append(
    {
        "name": "AluminothermicChromiumDust",
        "Input": {
            "Items": [
                {"name": "AluminiumDust", "Count": 1},
                {"name": "ChromiumOxideDust", "Count": 1},
            ]
        },
        "Output": {
            "Items": [{"name": "ChromiumDust", "Count": 1}],
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 10,
        },
        "Ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "CinnabarDust",
        "Input": {"Items": [{"name": "CinnabarDust", "Count": 2}]},
        "Output": {
            "Items": [
                {"name": "Mercury", "Count": 1000},
                {"name": "Sulfur", "Count": 1},
            ],
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 10,
        },
        "Ticks": 200,
    }
)

recipes_boiler.append(
    {
        "name": "Boiling",
        "Input": {
            "Items": [{"name": "Water", "Count": 50}],
        },
        "ResourceInput": {
            "name": "Heat",
            "Count": 110,
        },
        "Output": {"Items": []},
        "ResourceOutput": {
            "name": "Steam",
            "Count": 100,
            # "Capacity": 32000,
        },
        "Ticks": 200,
        "Loss": 10,
    }
)

recipes_steam_turbine.append(
    {
        "name": "Rotating",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Steam", "Count": 300},
        "Output": {"Items": []},
        "ResourceOutput": {"name": "Kinetic", "Count": 270},
        "Ticks": 200,
        "Loss": 10,
    }
)

recipes_generator.append(
    {
        "name": "Generating",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Kinetic", "Count": 270},
        "Output": {"Items": []},
        "ResourceOutput": {"name": "Electricity", "Count": 243},
        "Ticks": 200,
        "Loss": 10,
    }
)

recipes_electric_engine.append(
    {
        "name": "Rotating",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Electricity", "Count": 55},
        "Output": {"Items": []},
        "ResourceOutput": {"name": "Kinetic", "Count": 50},
        "Loss": 10,
        "Ticks": 200,
    }
)

recipes_industrial_electric_engine.append(
    {
        "name": "Rotating",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Electricity", "Count": 55 * 50},
        "Output": {"Items": []},
        "ResourceOutput": {"name": "Kinetic", "Count": 50 * 50},
        "Loss": 10,
        "Ticks": 200,
    }
)

recipes_compact_generator.append(
    {
        "name": "Rotating",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": []},
        "ResourceOutput": {"name": "Electricity", "Count": 18},
        "Loss": 10,
        "Ticks": 200,
    }
)

recipes_steam_engine.append(
    {
        "name": "Rotating",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Heat", "Count": 11},
        "Output": {"Items": []},
        "ResourceOutput": {"name": "Kinetic", "Count": 10},
        "Ticks": 200,
        "Loss": 10,
    }
)

recipes_oven.append(
    {
        "name": "CoalPieceToCoke",
        "Input": {"Items": [{"name": "Coal", "Count": 10}]},
        "Output": {
            "Items": [
                {"name": "Coke", "Count": 10},
                {
                    "name": "Creosote",
                    "Count": 250,
                    "Capacity": 32000,
                },
            ]
        },
        "Ticks": 2000,
    }
)

recipes_oven.append(
    {
        "name": "LogToCoal",
        "Input": {"Items": [{"name": "Log", "Count": 10}]},
        "Output": {
            "Items": [
                {"name": "Coal", "Count": 10},
                {
                    "name": "Creosote",
                    "Count": 100,
                    "Capacity": 32000,
                },
            ]
        },
        "Ticks": 2000,
    }
)

recipes_oven.append(
    {
        "name": "PlankToCoal",
        "Input": {"Items": [{"name": "Plank", "Count": 10}]},
        "Output": {
            "Items": [
                {"name": "Coal", "Count": 3},
                {
                    "name": "Creosote",
                    "Count": 30,
                    "Capacity": 32000,
                },
            ]
        },
        "Ticks": 500,
    }
)

recipes_oven.append(
    {
        "name": "OrgToCoal",
        "Input": {"Items": [{"name": "Organics", "Count": 10}]},
        "Output": {
            "Items": [
                {"name": "Coal", "Count": 2},
                {
                    "name": "Creosote",
                    "Count": 20,
                    "Capacity": 32000,
                },
            ]
        },
        "Ticks": 500,
    }
)

recipes_oven.append(
    {
        "name": "Terracotta",
        "Input": {"Items": [{"name": "Clay", "Count": 10}]},
        "Output": {
            "Items": [
                {"name": "Terracotta", "Count": 10},
            ]
        },
        "Ticks": 1000,
    }
)

for fuel_type, bonus in zip(["Coke"], [1.0]):
    recipes_blast_furnace.append(
        {
            "name": "IronIngotSmelting",
            "Input": {
                "Items": [
                    {"name": fuel_type, "Count": 15},
                    {"name": "IronIngot", "Count": 10},
                ]
            },
            "Output": {"Items": [{"name": "SteelIngot", "Count": 10}]},
            "Ticks": 2000,
        }
    )

    recipes_blast_furnace.append(
        {
            "name": "IronDustSmelting",
            "Input": {
                "Items": [
                    {"name": fuel_type, "Count": 10},
                    {"name": "IronDust", "Count": 10},
                ]
            },
            "Output": {"Items": [{"name": "SteelIngot", "Count": 10}]},
            "Ticks": 2000,
        }
    )

    recipes_blast_furnace.append(
        {
            "name": "IronOreDustSmelting",
            "Input": {
                "Items": [
                    {"name": fuel_type, "Count": 20},
                    {"name": "IronOreDust", "Count": 10},
                ]
            },
            "Output": {"Items": [{"name": "SteelIngot", "Count": 10}]},
            "Ticks": 2000,
        }
    )

    recipes_blast_furnace.append(
        {
            "name": "IronOreDustSmelting" + fuel_type,
            "Input": {
                "Items": [
                    {"name": fuel_type, "Count": 1},
                    {"name": "SteelDust", "Count": 10},
                ]
            },
            "Output": {"Items": [{"name": "SteelIngot", "Count": 10}]},
            "Ticks": 2000,
        }
    )

recipes_mixer.append(
    {
        "name": "ReinforcedConcrete",
        "Input": {
            "Items": [
                {"name": "Concrete", "Count": 10},
                {"name": "SteelParts", "Count": 8},
                {"name": "Water", "Count": 100},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "ReinforcedConcrete", "Count": 5}]},
        "Ticks": 300,
    }
)
recipes_mixer.append(
    {
        "name": "Concrete",
        "Input": {
            "Items": [
                {"name": "StoneSurface", "Count": 5},
                {"name": "Water", "Count": 100},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "Concrete", "Count": 10}]},
        "Ticks": 300,
    }
)
recipes_mixer.append(
    {
        "name": "SSCraft",
        "Input": {
            "Items": [
                {"name": "IronDust", "Count": 10},
                {"name": "ChromiumDust", "Count": 3},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "StainlessSteelDust", "Count": 10}]},
        "Ticks": 400,
    }
)
recipes_mixer.append(
    {
        "name": "SSCraft2",
        "Input": {
            "Items": [
                {"name": "IronOreDust", "Count": 10},
                {"name": "ChromiumDust", "Count": 3},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 40},
        "Output": {"Items": [{"name": "StainlessSteelDust", "Count": 10}]},
        "Ticks": 500,
    }
)

recipes_mixer.append(
    {
        "name": "PreparedTitaniumOxideCraft",
        "Input": {
            "Items": [
                {"name": "TitaniumOxideDust", "Count": 1},
                {"name": "Coke", "Count": 2},
            ],
        },
        "ResourceInput": {
            "name": "Kinetic",
            "Count": 10,
        },
        "Output": {"Items": [{"name": "PreparedTitaniumOxideDust", "Count": 1}]},
        "Ticks": 200,
        "Scaled": False,
    }
)

# recipes_sep2.append({
# 	"name": "RareSeparating",
# 	"Input":{
# 		"Items":[
# 			{
# 				"name": "RareEarthDust",
# 				"Count": 10
# 			},
#
# 		]
# 	},
# 	"ResourceInput":{
# 		"name": "Kinetic",
# 		"Count": 50000
# 	},
# 	"Output":{
# 		"Items": [
# 			{
# 				"name": "RareMetalsDust",
# 				"Count": 1
# 			},
# 			{
# 				"name": "YttriumDust",
# 				"Count": 1
# 			},
# 			{
# 				"name": "LutetiumDust",
# 				"Count": 1
# 			},
# 			{
# 				"name": "DysprosiumDust",
# 				"Count": 1
# 			}
# 		]
# 	},
#
# 	"Ticks": 1000,
# })

# recipes_sep2.append({
# "name": "OreWater",
# "Input":{
# "Items":[
# {
# "name": "OreWater",
# "Count": 1000
# },
# ]
# },
# "ResourceInput":{
# "name": "Kinetic",
# "Count": 30
# },
# "Output":{
# "Items": [
# {
# "name": "Clay",
# "Count": 1
# },
# ]
# },

# "Ticks": 200,
# })

recipes_sep2.append(
    {
        "name": "PlutoniumDust",
        "Input": {
            "Items": [
                {"name": "DepletedUraniumCell", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 30 * 90},
        "Output": {
            "Items": [
                {"name": "Cell", "Count": 1},
                {"name": "PlutoniumDust", "Count": 1, "split": 2},
            ]
        },
        "Ticks": 400,
    }
)

recipes_sep2.append(
    {
        "name": "Granite",
        "Input": {
            "Items": [
                {"name": "GraniteSurface", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 30 * 90},
        "Output": {
            "Items": [
                {"name": "SandSurface", "Count": 1},
                {
                    "name": "TungstenOxideDust",
                    "Count": 1,
                    "split": 10,
                },
            ]
        },
        "Ticks": 40,
    }
)

recipes_sep2.append(
    {
        "name": "Stone",
        "Input": {
            "Items": [
                {"name": "StoneSurface", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 30},
        "Output": {
            "Items": [
                {"name": "SandSurface", "Count": 1},
                {
                    "name": "AluminiumOxideDust",
                    "Count": 1,
                    "split": 10,
                },
            ]
        },
        "Ticks": 100,
    }
)

recipes_sep2.append(
    {
        "name": "Basalt",
        "Input": {
            "Items": [
                {"name": "BasaltSurface", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 30 * 25},
        "Output": {
            "Items": [
                {"name": "SandSurface", "Count": 1},
                {
                    "name": "AluminiumOxideDust",
                    "Count": 1,
                    "split": 5,
                },
                {
                    "name": "TitaniumOxideDust",
                    "Count": 1,
                    "split": 10,
                },
            ]
        },
        "Ticks": 40,
    }
)

recipes_sep2.append(
    {
        "name": "Sand",
        "Input": {
            "Items": [
                {"name": "SandSurface", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 30},
        "Output": {
            "Items": [
                {
                    "name": "SiliconOxide",
                    "Count": 1,
                    "split": 2,
                }
            ]
        },
        "Ticks": 100,
    }
)

recipes_arc_furnace.append(
    {
        "name": "CopperOreDust",
        "Input": {
            "Items": [
                {"name": "CopperOreDust", "Count": 1},
            ]
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 20,
        },
        "Output": {"Items": [{"name": "CopperIngot", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_arc_furnace.append(
    {
        "name": "SandSurfaceSmelting",
        "Input": {
            "Items": [
                {"name": "SandSurface", "Count": 1},
            ],
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 20,
        },
        "Output": {"Items": [{"name": "Glass", "Count": 1}]},
        "Ticks": 100,
    }
)

for material in materials:
    if "IsIngot" in material:
        if "SmeltLevel" in material and material["SmeltLevel"] <= 3:
            recipes_arc_furnace.append(
                {
                    "name": material["name"] + "Ingot",
                    "Input": {
                        "Items": [
                            {"name": material["name"] + "Dust", "Count": 1},
                        ]
                    },
                    "ResourceInput": {
                        "name": "Electricity",
                        "Count": 20 if material["name"] != "StainlessSteel" else 100,
                    },
                    "Output": {
                        "Items": [{"name": material["name"] + "Ingot", "Count": 1}]
                    },
                    "Tier": extract_tier(material),
                    "Ticks": 200,
                }
            )

recipes_macerator.append(
    {
        "name": "Pumpkin",
        "Input": {
            "Items": [
                {"name": "Pumpkin", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "Organics", "Count": 1}]},
        "Tier": 0,
        "Ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "Emerald",
        "Input": {
            "Items": [
                {"name": "Emerald", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 50},
        "Output": {"Items": [{"name": "EmeraldDust", "Count": 1}]},
        "Tier": 0,
        "Ticks": 100,
    }
)

recipes_macerator.append(
    {
        "name": "MalachiteCrystal",
        "Input": {
            "Items": [
                {"name": "MalachiteCrystal", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "CopperOreDust", "Count": 2}]},
        "Tier": 0,
        "Ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "MalachiteCluster",
        "Input": {
            "Items": [
                {"name": "MalachiteCluster", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "CopperOreDust", "Count": 5}]},
        "Tier": 0,
        "Ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "RutileCrystal",
        "Input": {
            "Items": [
                {"name": "RutileCrystal", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "TitaniumOxideDust", "Count": 2}]},
        "Tier": 0,
        "Ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "CinnabarCrystal",
        "Input": {
            "Items": [
                {"name": "CinnabarCrystal", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "CinnabarDust", "Count": 2}]},
        "Tier": 0,
        "Ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "CinnabarCluster",
        "Input": {
            "Items": [
                {"name": "CinnabarCluster", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "CinnabarDust", "Count": 5}]},
        "Tier": 0,
        "Ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "UraniniteCrystal",
        "Input": {
            "Items": [
                {"name": "UraniniteCrystal", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "UraniumDust", "Count": 2}]},
        "Tier": 0,
        "Ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "UraniniteCluster",
        "Input": {
            "Items": [
                {"name": "UraniniteCluster", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {
            "Items": [
                {"name": "UraniumDust", "Count": 5},
                {"name": "Uranium235Dust", "Count": 1},
            ]
        },
        "Tier": 0,
        "Ticks": 200,
    }
)

recipes_macerator.append(
    {
        "name": "GravelToSand",
        "Input": {
            "Items": [
                {"name": "GravelSurface", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "SandSurface", "Count": 1}]},
        "Tier": 0,
        "Ticks": 200,
    }
)

recipes_hammer.append(
    {
        "name": "StoneToGravel",
        "Input": {
            "Items": [
                {"name": "StoneSurface", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "GravelSurface", "Count": 1}]},
        "Tier": 0,
        "Ticks": 100,
    }
)

recipes_pump.append(
    {
        "name": "Water",
        "Input": {"Items": []},
        "Output": {"Items": []},
        "ResourceOutput": {"name": "Water", "Count": 600},
        "Ticks": 6 * 20,
    }
)

recipes_indu.append(
    {
        "name": "SpongeToIngot",
        "Input": {
            "Items": [
                {"name": "TitaniumSponge", "Count": 1},
            ],
        },
        "ResourceInput": {
            "name": "Heat",
            "Count": 350,
        },
        "Output": {
            "Items": [
                {"name": "TitaniumIngot", "Count": 1},
            ]
        },
        "Tier": 5,
        "Ticks": 200,
    }
)

recipes_indu.append(
    {
        "name": "SuperconductorDust",
        "Input": {
            "Items": [
                {"name": "SuperconductorDust", "Count": 1},
            ],
        },
        "ResourceInput": {
            "name": "Heat",
            "Count": 100,
        },
        "Output": {
            "Items": [
                {"name": "SuperconductorIngot", "Count": 1},
            ]
        },
        "Tier": 5,
        "Ticks": 200,
    }
)

recipes_indu.append(
    {
        "name": "TDustToIngot",
        "Input": {
            "Items": [
                {"name": "TitaniumDust", "Count": 1},
            ],
        },
        "ResourceInput": {
            "name": "Heat",
            "Count": 350,
        },
        "Output": {
            "Items": [
                {"name": "TitaniumIngot", "Count": 1},
            ]
        },
        "Tier": 5,
        "Ticks": 200,
    }
)

recipes_indu.append(
    {
        "name": "HardMetalDustToIngot",
        "Input": {
            "Items": [
                {"name": "HardMetalDust", "Count": 1},
            ],
        },
        "ResourceInput": {
            "name": "Heat",
            "Count": 900,
        },
        "Output": {
            "Items": [
                {"name": "HotHardMetalIngot", "Count": 1},
            ]
        },
        "Ticks": 200,
    }
)

recipes_sep.append(
    {
        "name": "SiliconOxide",
        "Input": {"Items": [{"name": "SandSurface", "Count": 2}]},
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "SiliconOxide", "Count": 1}]},
        "Ticks": 1000,
    }
)

recipes_mixer.append(
    {
        "name": "Organics",
        "Input": {
            "Items": [
                {"name": "Organics", "Count": 1},
                {"name": "Water", "Count": 500},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "Biomass", "Count": 500}]},
        "Ticks": 200,
    }
)

recipes_mixer.append(
    {
        "name": "HardMetalDust",
        "Input": {
            "Items": [
                {"name": "TungstenCarbideDust", "Count": 4},
                {"name": "CobaltDust", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 100},
        "Output": {"Items": [{"name": "HardMetalDust", "Count": 5}]},
        "Ticks": 1000,
    }
)

recipes_mixer.append(
    {
        "name": "SuperconductorDust",
        "Input": {
            "Items": [
                {"name": "GoldDust", "Count": 3},
                {"name": "RareEarthElement", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 100},
        "Output": {"Items": [{"name": "SuperconductorDust", "Count": 3}]},
        "Ticks": 300,
    }
)

recipes_electrolyzer.append(
    {
        "name": "AluminiumOxideDust",
        "Input": {
            "Items": [
                {"name": "AluminiumOxideDust", "Count": 1},
            ]
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 50,
        },
        "Output": {"Items": [{"name": "AluminiumDust", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_electrolyzer.append(
    {
        "name": "EmeraldDust",
        "Input": {
            "Items": [
                {"name": "EmeraldDust", "Count": 2},
            ]
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 70,
        },
        "Output": {
            "Items": [
                {"name": "BerylliumDust", "Count": 1},
                {"name": "AluminiumOxideDust", "Count": 1},
            ]
        },
        "Ticks": 200,
    }
)

recipes_electrolyzer.append(
    {
        "name": "AluminiumOreDust",
        "Input": {
            "Items": [
                {"name": "AluminiumOreDust", "Count": 1},
            ]
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 30,
        },
        "Output": {"Items": [{"name": "AluminiumDust", "Count": 1}]},
        "Ticks": 500,
    }
)

recipes_electrolyzer.append(
    {
        "name": "Clay",
        "Input": {
            "Items": [
                {"name": "Clay", "Count": 6},
            ]
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 1300,
        },
        "Output": {
            "Items": [
                {"name": "SandSurface", "Count": 4},
                {"name": "AluminiumOxideDust", "Count": 1},
                {"name": "SodiumDust", "Count": 1},
            ]
        },
        "Ticks": 40,
    }
)

recipes_electrolyzer.append(
    {
        "name": "SandElectrolyze",
        "Input": {"Items": [{"name": "SiliconOxide", "Count": 1}]},
        "ResourceInput": {"name": "Electricity", "Count": 60},
        "Output": {"Items": [{"name": "Silicon", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_electrolyzer.append(
    {
        "name": "WaterElectrolyze",
        "Input": {"Items": [{"name": "Water", "Count": 100}]},
        "ResourceInput": {"name": "Electricity", "Count": 280},
        "Output": {
            "Items": [
                {"name": "Hydrogen", "Count": 100},
                {"name": "Oxygen", "Count": 200},
            ]
        },
        "Ticks": 100,
    }
)

recipes_electrolyzer.append(
    {
        "name": "SaltElectrolyze",
        "Input": {
            "Items": [
                {"name": "SaltDust", "Count": 1},
            ]
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 10,
        },
        "Output": {
            "Items": [
                {"name": "SodiumDust", "Count": 1},
                {"name": "Chlorine", "Count": 1000},
            ]
        },
        "Ticks": 200,
    }
)

recipes_electrolyzer.append(
    {
        "name": "PotassiumChloride",
        "Input": {
            "Items": [
                {"name": "PotassiumChlorideDust", "Count": 1},
            ]
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 10,
        },
        "Output": {
            "Items": [
                {"name": "PotassiumDust", "Count": 1},
                {"name": "Chlorine", "Count": 1000},
            ]
        },
        "Ticks": 200,
    }
)

recipes_electrolyzer.append(
    {
        "name": "Borax",
        "Input": {
            "Items": [
                {"name": "BoraxDust", "Count": 2},
            ]
        },
        "ResourceInput": {
            "name": "Electricity",
            "Count": 50,
        },
        "Output": {
            "Items": [
                {"name": "SodiumDust", "Count": 1},
                {"name": "BoronDust", "Count": 1},
            ]
        },
        "Ticks": 200,
    }
)

# wood

recipes_cutter.append(
    {
        "name": "LogCutting",
        "Input": {
            "Items": [
                {"name": "Log", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "Plank", "Count": 4}]},
        "Ticks": 80,
    }
)
recipes_cutter.append(
    {
        "name": "StoneLogCutting",
        "Input": {
            "Items": [
                {"name": "StoneLog", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "Plank", "Count": 4}]},
        "Ticks": 200,
    }
)
recipes_cutter.append(
    {
        "name": "CircuitBoard",
        "Input": {
            "Items": [
                {"name": "Plank", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "CircuitBoard", "Count": 1}]},
        "Ticks": 80,
    }
)
recipes_cutter.append(
    {
        "name": "StoneTiles",
        "Input": {"Items": [{"name": "StoneSurface", "Count": 1}]},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": [{"name": "StoneTiles", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "DarkTiles",
        "Input": {"Items": [{"name": "DarkStoneSurface", "Count": 1}]},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": [{"name": "DarkTiles", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "RedTiles",
        "Input": {"Items": [{"name": "RedStoneSurface", "Count": 1}]},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": [{"name": "RedTiles", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "Bricks",
        "Input": {"Items": [{"name": "StoneTiles", "Count": 1}]},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": [{"name": "Bricks", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "RedBricks",
        "Input": {"Items": [{"name": "RedTiles", "Count": 1}]},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": [{"name": "RedBricks", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "DarkBricks",
        "Input": {"Items": [{"name": "DarkTiles", "Count": 1}]},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": [{"name": "DarkBricks", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "TerracottaTiles",
        "Input": {"Items": [{"name": "Terracotta", "Count": 1}]},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": [{"name": "TerracottaTiles", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "TerracottaBricks",
        "Input": {"Items": [{"name": "TerracottaTiles", "Count": 1}]},
        "ResourceInput": {"name": "Kinetic", "Count": 20},
        "Output": {"Items": [{"name": "TerracottaBricks", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ConcreteTiles",
        "Input": {
            "Items": [
                {"name": "Concrete", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "ConcreteTiles", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ConcreteSmallTiles",
        "Input": {
            "Items": [
                {"name": "ConcreteTiles", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "ConcreteSmallTiles", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ConcreteBricks",
        "Input": {
            "Items": [
                {"name": "ConcreteSmallTiles", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "ConcreteBricks", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ReinforcedConcreteTiles",
        "Input": {
            "Items": [
                {"name": "ReinforcedConcrete", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "ReinforcedConcreteTiles", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ReinforcedConcreteSmallTiles",
        "Input": {
            "Items": [
                {"name": "ReinforcedConcreteTiles", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "ReinforcedConcreteSmallTiles", "Count": 1}]},
        "Ticks": 100,
    }
)
recipes_cutter.append(
    {
        "name": "ReinforcedConcreteBricks",
        "Input": {
            "Items": [
                {"name": "ReinforcedConcreteSmallTiles", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {"Items": [{"name": "ReinforcedConcreteBricks", "Count": 1}]},
        "Ticks": 100,
    }
)
# burning

recipes_elfurn.append(
    {
        "name": "Working",
        "Input": {"Items": []},
        "ResourceInput": {
            "name": "Electricity",
            "Count": 55,
        },
        "Output": {
            "Items": [],
        },
        "ResourceOutput": {
            "name": "Heat",
            "Count": 50,
        },
        "Ticks": 200,
        "Loss": 10,
    }
)

recipes_coil.append(
    {
        "name": "Working",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Electricity", "Count": 380},
        "Output": {
            "Items": [],
        },
        "ResourceOutput": {
            "name": "Heat",
            "Count": 342,
        },
        "Ticks": 200,
        "Loss": 10,
    }
)

recipes_ferm.append(
    {
        "name": "MethaneFromBiomass",
        "Input": {
            "Items": [
                {"name": "Biomass", "Count": 500},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "Methane", "Count": 500}]},
        "Ticks": 200,
    }
)

recipes_ferm.append(
    {
        "name": "MethaneFromPumpkin",
        "Input": {
            "Items": [
                {"name": "Pumpkin", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "Methane", "Count": 200}]},
        "Ticks": 200,
    }
)

recipes_radiator.append(
    {
        "name": "Working",
        "Input": {
            "Items": [],
        },
        "ResourceInput": {
            "name": "Heat",
            "Count": 500,
        },
        "Output": {"Items": []},
        "Ticks": 200,
    }
)

recipes_solar.append(
    {
        "name": "Working",
        "Input": {"Items": []},
        "Output": {"Items": []},
        "ResourceOutput": {
            "name": "Electricity",
            "Count": 50,
        },
        "Ticks": 60,
    }
)

recipes_riteg.append(
    {
        "name": "Working",
        "Input": {"Items": []},
        "Output": {"Items": []},
        "ResourceOutput": {
            "name": "Heat",
            "Count": 500,
        },
        "Ticks": 60,
    }
)

recipes_chem.append(
    {
        "name": "MineralWater",
        "Input": {
            "Items": [
                {"name": "MineralWater", "Count": 1000},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "SaltDust", "Count": 1}]},
        "Ticks": 400,
    }
)

recipes_chem.append(
    {
        "name": "MineralWater3",
        "Input": {
            "Items": [
                {"name": "MineralWater", "Count": 1000},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 60},
        "Output": {"Items": [{"name": "BoraxDust", "Count": 1, "split": 10}]},
        "Ticks": 100,
    }
)

recipes_chem.append(
    {
        "name": "MineralWater2",
        "Input": {
            "Items": [
                {"name": "MineralWater", "Count": 1000},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "PotassiumChlorideDust", "Count": 1}]},
        "Ticks": 400,
    }
)

recipes_chem.append(
    {
        "name": "TungstenCarbideDust",
        "Input": {
            "Items": [
                {"name": "TungstenDust", "Count": 1},
                {"name": "Coke", "Count": 2},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "TungstenCarbideDust", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "TitaniumTetrachloride",
        "Input": {
            "Items": [
                {"name": "PreparedTitaniumOxideDust", "Count": 1},
                {"name": "Chlorine", "Count": 1000},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "TitaniumTetrachloride", "Count": 1000}]},
        "Ticks": 200,
        "Scaled": False,
    }
)

recipes_chem.append(
    {
        "name": "TitaniumSponge",
        "Input": {
            "Items": [
                {"name": "TitaniumTetrachloride", "Count": 1000},
                {"name": "AluminiumDust", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {
            "Items": [
                {"name": "TitaniumSponge", "Count": 1},
            ],
        },
        "Ticks": 200,
        "Scaled": False,
    }
)

recipes_chem.append(
    {
        "name": "TungstenOxide",
        "Input": {
            "Items": [
                {"name": "TungstenOxideDust", "Count": 1},
                {"name": "Hydrogen", "Count": 1000},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "TungstenDust", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "CobaltOxide",
        "Input": {
            "Items": [
                {"name": "CobaltOxideDust", "Count": 1},
                {"name": "Hydrogen", "Count": 1000},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "CobaltDust", "Count": 1}]},
        "Ticks": 200,
        "Scaled": False,
    }
)

for i in {"ProducerGas", "Methane", "Hydrogen", "Gasoline"}:
    recipes_gasturb.append(
        {
            "Input": {"Items": [{"name": i, "Count": 14 * 1000}]},
            "Output": {"Items": []},
            "ResourceOutput": {
                "name": "Kinetic",
                "Count": named_material(i)["Burnable"]["HeatPerTick"] * 14,
            },
            "Ticks": named_material(i)["Burnable"]["BurnTime"],
            "name": i,
        }
    )

    recipes_combustion.append(
        {
            "name": i,
            "Input": {"Items": [{"name": i, "Count": 1000}]},
            "Output": {"Items": []},
            "ResourceOutput": {
                "name": "Kinetic",
                "Count": named_material(i)["Burnable"]["HeatPerTick"],
            },
            "Ticks": named_material(i)["Burnable"]["BurnTime"],
        }
    )

recipes_pyro.append(
    {
        "name": "Coal",
        "Input": {
            "Items": [
                {"name": "Coal", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Heat", "Count": 10},
        "Output": {
            "Items": [
                {"name": "Coke", "Count": 1},
                {"name": "RawOil", "Count": 100},
                {"name": "ProducerGas", "Count": 100},
            ]
        },
        "Ticks": 400,
    }
)

recipes_pyro.append(
    {
        "name": "CoalSteam",
        "Input": {
            "Items": [
                {"name": "Coal", "Count": 1},
                {"name": "Steam", "Count": 200},
            ]
        },
        "ResourceInput": {"name": "Heat", "Count": 10},
        "Output": {
            "Items": [
                {"name": "Coke", "Count": 1},
                {"name": "ProducerGas", "Count": 500},
            ]
        },
        "Ticks": 400,
    }
)

recipes_pyro.append(
    {
        "name": "RawOil",
        "Input": {
            "Items": [
                {"name": "RawOil", "Count": 2000},
            ]
        },
        "ResourceInput": {"name": "Heat", "Count": 15},
        "Output": {
            "Items": [
                {"name": "HeavyOil", "Count": 500},
                {"name": "Gasoline", "Count": 100},
                {"name": "Methane", "Count": 500},
            ]
        },
        "Ticks": 200,
    }
)

recipes_pyro.append(
    {
        "name": "RawOilSteam",
        "Input": {
            "Items": [
                {"name": "RawOil", "Count": 1000 * 5},
                {"name": "Steam", "Count": 1000},
            ]
        },
        "ResourceInput": {"name": "Heat", "Count": 100},
        "Output": {
            "Items": [
                {"name": "HeavyOil", "Count": 150 * 2},
                {"name": "Gasoline", "Count": 400 * 2},
                {"name": "Methane", "Count": 500 * 2},
            ]
        },
        "Ticks": 200,
    }
)

recipes_pyro.append(
    {
        "name": "HeavyOil",
        "Input": {
            "Items": [
                {"name": "HeavyOil", "Count": 1000},
                {"name": "Steam", "Count": 200},
            ]
        },
        "ResourceInput": {"name": "Heat", "Count": 10},
        "Output": {
            "Items": [
                {"name": "Gasoline", "Count": 750},
            ]
        },
        "Ticks": 200,
    }
)

recipes_pyro.append(
    {
        "name": "Gasoline",
        "Input": {
            "Items": [
                {"name": "Gasoline", "Count": 1000},
                {"name": "Steam", "Count": 200},
            ]
        },
        "ResourceInput": {"name": "Heat", "Count": 10},
        "Output": {
            "Items": [
                {"name": "Methane", "Count": 750},
            ]
        },
        "Ticks": 200,
    }
)

recipes_pyro.append(
    {
        "name": "Methane",
        "Input": {
            "Items": [
                {"name": "Methane", "Count": 800 * 5},
                {"name": "Steam", "Count": 200 * 20},
            ]
        },
        "ResourceInput": {"name": "Heat", "Count": 100},
        "Output": {
            "Items": [
                {"name": "ProducerGas", "Count": 1000 * 5},
            ]
        },
        "Ticks": 200,
    }
)

recipes_pyro.append(
    {
        "name": "Methane2",
        "Input": {"Items": [{"name": "Methane", "Count": 800 * 5}]},
        "ResourceInput": {"name": "Heat", "Count": 50},
        "Output": {
            "Items": [
                {"name": "ProducerGas", "Count": 500 * 5},
            ]
        },
        "Ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "Ethylene",
        "Input": {
            "Items": [
                {"name": "ProducerGas", "Count": 1000},
                {
                    "name": "Catalyst",
                    "Count": 1,
                    "split": 0,
                },
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {
            "Items": [
                {
                    "name": "Ethylene",
                    "Count": 1000,
                },
            ]
        },
        "Ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "Sulfur",
        "Input": {
            "Items": [
                {"name": "HeavyOil", "Count": 150},
                {"name": "Water", "Count": 250},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {
            "Items": [
                {"name": "Sulfur", "Count": 1},
            ]
        },
        "Ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "SulfuricAcid",
        "Input": {
            "Items": [
                {"name": "Sulfur", "Count": 1},
                {"name": "Oxygen", "Count": 250},
                {"name": "Water", "Count": 250},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {
            "Items": [
                {"name": "SulfuricAcid", "Count": 1000},
            ]
        },
        "Ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "Plastic1",
        "Input": {
            "Items": [
                {"name": "Ethylene", "Count": 1000},
                {"name": "Coal", "Count": 1},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {
            "Items": [
                {"name": "Plastic", "Count": 1},
            ]
        },
        "Ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "Plastic2",
        "Input": {
            "Items": [
                {"name": "Ethylene", "Count": 1000},
                {"name": "HeavyOil", "Count": 150},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {
            "Items": [
                {"name": "Plastic", "Count": 1},
            ]
        },
        "Ticks": 200,
    }
)

recipes_chem.append(
    {
        "name": "ProducerGas",
        "Input": {
            "Items": [
                {"name": "ProducerGas", "Count": 1000},
            ]
        },
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {
            "Items": [
                {"name": "Hydrogen", "Count": 750},
            ]
        },
        "Ticks": 200,
    }
)

recipes_filtering_unit.append(
    {
        "name": "OreWater",
        "Input": {
            "Items": [
                {"name": "OreWater", "Count": 500},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {
            "Items": [
                {"name": "Clay", "Count": 1},
            ]
        },
        "Ticks": 200,
    }
)

recipes_filtering_unit.append(
    {
        "name": "OreWater2",
        "Input": {
            "Items": [
                {"name": "OreWater", "Count": 500},
                {"name": "FilteringCell", "Count": 1, "split": 10},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {
            "Items": [
                {"name": "AluminiumOreDust", "Count": 1, "split": 2},
            ]
        },
        "Ticks": 200,
    }
)

recipes_filtering_unit.append(
    {
        "name": "OreWater3",
        "Input": {
            "Items": [
                {"name": "OreWater", "Count": 500},
                {"name": "FilteringCell", "Count": 1, "split": 10},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {
            "Items": [
                {"name": "CopperOreDust", "Count": 1, "split": 2},
            ]
        },
        "Ticks": 200,
    }
)

recipes_filtering_unit.append(
    {
        "name": "OreWater4",
        "Input": {
            "Items": [
                {"name": "OreWater", "Count": 500},
                {"name": "FilteringCell", "Count": 1, "split": 10},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {
            "Items": [
                {"name": "UraniumOreDust", "Count": 1, "split": 2},
            ]
        },
        "Ticks": 200,
    }
)

recipes_filtering_unit.append(
    {
        "name": "OreWater5",
        "Input": {
            "Items": [
                {"name": "OreWater", "Count": 500},
                {"name": "FilteringCell", "Count": 1, "split": 10},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 10},
        "Output": {
            "Items": [
                {"name": "IronOreDust", "Count": 1, "split": 2},
            ]
        },
        "Ticks": 200,
    }
)

for i in {"IronOreDust", "CopperOreDust"}:
    recipes_chemical_bath.append(
        {
            "name": i,
            "Input": {
                "Items": [
                    {"name": "Mercury", "Count": 500},
                    {
                        "name": i,
                        "Count": 2,
                    },
                ]
            },
            "ResourceInput": {"name": "Kinetic", "Count": 10},
            "Output": {
                "Items": [
                    {
                        "name": "GoldDust",
                        "Count": 1,
                    },
                ]
            },
            "Ticks": 200,
        }
    )

recipes_chemical_bath.append(
    {
        "name": "RareEarthElement",
        "Input": {
            "Items": [
                {"name": "AluminiumOreDust", "Count": 10},
                {"name": "SulfuricAcid", "Count": 1000},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 30},
        "Output": {"Items": [{"name": "RareEarthElement", "Count": 1}]},
        "Ticks": 1000,
    }
)

recipes_chemical_bath.append(
    {
        "name": "CobaltOxideDust",
        "Input": {
            "Items": [
                {"name": "IronOreDust", "Count": 10},
                {"name": "SulfuricAcid", "Count": 1000},
            ]
        },
        "ResourceInput": {"name": "Kinetic", "Count": 30},
        "Output": {"Items": [{"name": "CobaltOxideDust", "Count": 1}]},
        "Ticks": 1000,
    }
)

recipes_freezer.append(
    {
        "name": "HotHardmetalIngot",
        "Input": {"Items": [{"name": "HotHardMetalIngot", "Count": 1}]},
        "ResourceInput": {"name": "Kinetic", "Count": 100},
        "Output": {"Items": [{"name": "HardMetalIngot", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_freezer.append(
    {
        "name": "HotNeutroniumIngot",
        "Input": {"Items": [{"name": "HotNeutroniumIngot", "Count": 1}]},
        "ResourceInput": {"name": "Kinetic", "Count": 1000},
        "Output": {"Items": [{"name": "NeutroniumIngot", "Count": 1}]},
        "Ticks": 200,
    }
)

recipes_computer.append(
    {
        "name": "Computations",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Electricity", "Count": 10},
        "Output": {"Items": [{"name": "Computations", "Count": 1}]},
        "Ticks": 40,
    }
)

recipes_q_computer.append(
    {
        "name": "QuantumComputations",
        "Input": {"Items": []},
        "ResourceInput": {"name": "Electricity", "Count": 100},
        "Output": {"Items": [{"name": "Computations", "Count": 40}]},
        "Ticks": 40,
    }
)

recipes_portal.append(
    {
        "name": "Ping",
        "Input": {"Items": []},
        "ResourceInput": {
            "name": "Electricity",
            "Count": 2 * fission_fullpower * 0.9 * 0.9,
        },
        "Output": {"Items": [{"name": "MothershipPing", "Count": 1}]},
        "Ticks": 1000,
    }
)

append_recipe_hand_press(
    {
        "name": "Column",
        "Input": {"Items": [{"name": "StoneSurface", "Count": 1}]},
        "Output": {"Items": [{"name": "Column", "Count": 1}]},
        "Ticks": 20,
    }
)

append_recipe_hand_press(
    {
        "name": "FluetedColumn",
        "Input": {"Items": [{"name": "Column", "Count": 1}]},
        "Output": {"Items": [{"name": "FluetedColumn", "Count": 1}]},
        "Ticks": 20,
    }
)

append_recipe_hand_press(
    {
        "name": "GlassBlock",
        "Input": {"Items": [{"name": "Glass", "Count": 1}]},
        "Output": {"Items": [{"name": "GlassBlock", "Count": 1}]},
        "Ticks": 10,
    }
)

append_recipe_hand_press(
    {
        "name": "PlasticBlock",
        "Input": {"Items": [{"name": "Plastic", "Count": 1}]},
        "Output": {"Items": [{"name": "PlasticBlock", "Count": 1}]},
        "Ticks": 10,
    }
)

append_recipe_hand_press(
    {
        "name": "DangerBlock",
        "Input": {"Items": [{"name": "Concrete", "Count": 1}]},
        "Output": {"Items": [{"name": "DangerBlock", "Count": 1}]},
        "Ticks": 20,
    }
)

append_recipe_hand_press(
    {
        "name": "BasicPlatform",
        "Input": {"Items": [{"name": "SandSurface", "Count": 1}]},
        "Output": {"Items": [{"name": "BasicPlatform", "Count": 1}]},
        "Ticks": 10,
    }
)

append_recipe_hand_press(
    {
        "name": "RustyCopperCasing",
        "Input": {"Items": [{"name": "CopperCasing", "Count": 1}]},
        "Output": {"Items": [{"name": "RustyCopperCasing", "Count": 1}]},
        "Ticks": 20,
    }
)

append_recipe_hand_press(
    {
        "name": "RustyIronCasing",
        "Input": {"Items": [{"name": "SteelCasing", "Count": 1}]},
        "Output": {"Items": [{"name": "RustyIronCasing", "Count": 1}]},
        "Ticks": 20,
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
            "Input": {"Items": [{"name": i, "Count": 1}]},
            "ResourceInput": {"name": "Electricity", "Count": 40},
            "Output": {"Items": [{"name": i, "Count": 1}]},
            "Ticks": 40,
        }
    )

objects_array.append(
    {"class": recipe_dictionary, "name": "Multitool", "Recipes": recipes_wrench}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "BlastFurnace",
        "Recipes": recipes_blast_furnace,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Oven", "Recipes": recipes_oven}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Smelter", "Recipes": recipes_smelter}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Macerator", "Recipes": recipes_macerator}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Boiler", "Recipes": recipes_boiler}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Generator", "Recipes": recipes_generator}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "ElectricEngine",
        "Recipes": recipes_electric_engine,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "StirlingEngine",
        "Recipes": recipes_steam_engine,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Pump", "Recipes": recipes_pump}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Separator", "Recipes": recipes_sep}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "IndustrialSeparator", "Recipes": recipes_sep2}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Press", "Recipes": recipes_press}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "ArcSmelter", "Recipes": recipes_arc_furnace}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "SteamTurbine",
        "Recipes": recipes_steam_turbine,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Electrolyzer",
        "Recipes": recipes_electrolyzer,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "CuttingMachine", "Recipes": recipes_cutter}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Furnace", "Recipes": recipes_furnace}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "ElectricFurnace", "Recipes": recipes_elfurn}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Fermenter", "Recipes": recipes_ferm}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "MultitoolRobotArm",
        "Recipes": recipes_toolarm,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "AutomaticHammer", "Recipes": recipes_hammer}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Mixer", "Recipes": recipes_mixer}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Radiator", "Recipes": recipes_radiator}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "SolarPanel", "Recipes": recipes_solar}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "ChemReactor", "Recipes": recipes_chem}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "InductionCoil", "Recipes": recipes_coil}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "IndustrialSmelter", "Recipes": recipes_indu}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "HeatExchanger", "Recipes": recipes_exch}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "InverseHeatExchanger",
        "Recipes": recipes_iexch,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Freezer", "Recipes": recipes_freezer}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "CombustionEngine",
        "Recipes": recipes_combustion,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "PyrolysisUnit", "Recipes": recipes_pyro}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Computer", "Recipes": recipes_computer}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "CompactGenerator",
        "Recipes": recipes_compact_generator,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "FissionReactor", "Recipes": recipes_fission}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "AutomaticFarm", "Recipes": recipes_farm}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "AtmosphericCondenser",
        "Recipes": recipes_condens,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Assembler", "Recipes": recipes_assembler}
)

objects_array.append(
    {"class": recipe_dictionary, "name": "GasTurbine", "Recipes": recipes_gasturb}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "FilteringUnit",
        "Recipes": recipes_filtering_unit,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Portal", "Recipes": recipes_portal}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "ChemicalBath",
        "Recipes": recipes_chemical_bath,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Riteg", "Recipes": recipes_riteg}
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "IndustrialSteamTurbine",
        "Recipes": recipes_industrial_steam_turbine,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "FusionReactor",
        "Recipes": recipes_fusion_reactor,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "IndustrialBoiler",
        "Recipes": recipes_industrial_boiler,
    }
)

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "IndustrialElectricEngine",
        "Recipes": recipes_industrial_electric_engine,
    }
)

objects_array.append(
    {"class": recipe_dictionary, "name": "Hand", "Recipes": recipes_hand}
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/misc.json", data)
