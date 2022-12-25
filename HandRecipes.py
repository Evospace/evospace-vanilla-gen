from Common import *
from MachinesList import *
from MiscGen import *
import copy

objects_array = []

recipes_hand = []

recipes_hand.append(
    {
        "name": "ClayBlock",
        "Input": {"Items": [{"name": "Clay", "Count": 1}]},
        "Output": {"Items": [{"name": "ClayBlock", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Bricks",
        "Input": {"Items": [{"name": "StoneSurface", "Count": 1}]},
        "Output": {"Items": [{"name": "Bricks", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "RedBricks",
        "Input": {"Items": [{"name": "RedStoneSurface", "Count": 1}]},
        "Output": {"Items": [{"name": "RedBricks", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "DarkBricks",
        "Input": {"Items": [{"name": "DarkStoneSurface", "Count": 1}]},
        "Output": {"Items": [{"name": "DarkBricks", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "SandSurface",
        "Input": {
            "Items": [
                {"name": "GravelSurface", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "SandSurface", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "GravelSurface",
        "Input": {
            "Items": [
                {"name": "StoneSurface", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "GravelSurface", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "StoneTiles",
        "Input": {"Items": [{"name": "StoneSurface", "Count": 1}]},
        "Output": {"Items": [{"name": "StoneTiles", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "DarkTiles",
        "Input": {"Items": [{"name": "DarkStoneSurface", "Count": 1}]},
        "Output": {"Items": [{"name": "DarkTiles", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "RedTiles",
        "Input": {"Items": [{"name": "RedStoneSurface", "Count": 1}]},
        "Output": {"Items": [{"name": "RedTiles", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "TerracottaTiles",
        "Input": {"Items": [{"name": "Terracotta", "Count": 1}]},
        "Output": {"Items": [{"name": "TerracottaTiles", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "TerracottaBricks",
        "Input": {"Items": [{"name": "TerracottaTiles", "Count": 1}]},
        "Output": {"Items": [{"name": "TerracottaBricks", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "CircuitBoard",
        "Input": {
            "Items": [
                {"name": "Plank", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "CircuitBoard", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "GoldWire",
        "Input": {
            "Items": [
                {"name": "GoldIngot", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "GoldWire", "Count": 2}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "CopperWire",
        "Input": {
            "Items": [
                {"name": "CopperIngot", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "CopperWire", "Count": 2}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Circuit",
        "Input": {
            "Items": [
                {"name": "CopperWire", "Count": 6},
                {"name": "CircuitBoard", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "Circuit", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "AdvancedCircuit",
        "Input": {
            "Items": [{"name": "Silicon", "Count": 1}, {"name": "Circuit", "Count": 1}]
        },
        "Output": {"Items": [{"name": "AdvancedCircuit", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Processor",
        "Input": {
            "Items": [
                {"name": "SiliconWafer", "Count": 1},
                {"name": "AdvancedCircuit", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "Processor", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "QuantumCircuit",
        "Input": {
            "Items": [
                {"name": "QuantumCore", "Count": 2},
                {"name": "Processor", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "QuantumCircuit", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "QuantumProcessor",
        "Input": {
            "Items": [
                {"name": "QuantumCircuit", "Count": 2},
                {"name": "Processor", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "QuantumProcessor", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "WoodenChest",
        "Input": {"Items": [{"name": "Plank", "Count": 6}]},
        "Output": {"Items": [{"name": "WoodenChest", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "WoodenPlanks",
        "Input": {"Items": [{"name": "Plank", "Count": 1}]},
        "Output": {"Items": [{"name": "WoodenPlanks", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Steampack",
        "Input": {
            "Items": [
                {"name": "CopperParts", "Count": 6},
                {"name": "CopperPlate", "Count": 2},
                {"name": "CopperPipe", "Count": 4},
                {"name": "Circuit", "Count": 10},
            ]
        },
        "Output": {"Items": [{"name": "Steampack", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Jetpack",
        "Input": {
            "Items": [
                {"name": "AluminiumParts", "Count": 10},
                {"name": "AluminiumPlate", "Count": 3},
                {"name": "AluminiumPipe", "Count": 6},
                {"name": "AdvancedCircuit", "Count": 10},
                {"name": "AluminiumElectricEngine", "Count": 2},
            ]
        },
        "Output": {"Items": [{"name": "Jetpack", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Torch",
        "Input": {
            "Items": [
                {"name": "Plank", "Count": 1},
                {"name": "Organics", "Count": 10},
            ]
        },
        "Output": {"Items": [{"name": "Torch", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "AdvancedJetpack",
        "Input": {
            "Items": [
                {"name": "StainlessSteelParts", "Count": 10},
                {"name": "StainlessSteelPlate", "Count": 3},
                {"name": "StainlessSteelPipe", "Count": 6},
                {"name": "Processor", "Count": 10},
                {"name": "StainlessSteelEngine", "Count": 2},
            ]
        },
        "Output": {"Items": [{"name": "AdvancedJetpack", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Scanner",
        "Input": {
            "Items": [
                {"name": "SteelPlate", "Count": 1},
                {"name": "AdvancedCircuit", "Count": 2},
                {"name": "CopperConnector", "Count": 5},
            ]
        },
        "Output": {"Items": [{"name": "Scanner", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "AntigravityUnit",
        "Input": {
            "Items": [
                {"name": "HardMetalParts", "Count": 20},
                {"name": "HardMetalPlate", "Count": 2},
                {"name": "HardMetalPipe", "Count": 6},
                {"name": "QuantumProcessor", "Count": 10},
                {"name": "Catalyst", "Count": 4},
                {"name": "HardMetalElectricEngine", "Count": 8},
            ]
        },
        "Output": {"Items": [{"name": "AntigravityUnit", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Plank",
        "Input": {"Items": [{"name": "Log", "Count": 1}]},
        "Output": {"Items": [{"name": "Plank", "Count": 2}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Chair",
        "Input": {"Items": [{"name": "Plank", "Count": 4}]},
        "Output": {"Items": [{"name": "Chair", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "CopperChair",
        "Input": {
            "Items": [
                {"name": "Chair", "Count": 1},
                {"name": "CopperPlate", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "CopperChair", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Ladder",
        "Input": {"Items": [{"name": "Plank", "Count": 4}]},
        "Output": {"Items": [{"name": "Ladder", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Door",
        "Input": {"Items": [{"name": "Plank", "Count": 8}]},
        "Output": {"Items": [{"name": "Door", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Window",
        "Input": {
            "Items": [{"name": "Glass", "Count": 2}, {"name": "Plank", "Count": 2}]
        },
        "Output": {"Items": [{"name": "Window", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "PlasticWindow",
        "Input": {
            "Items": [{"name": "Glass", "Count": 2}, {"name": "Plastic", "Count": 2}]
        },
        "Output": {"Items": [{"name": "PlasticWindow", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Table",
        "Input": {"Items": [{"name": "Plank", "Count": 6}]},
        "Output": {"Items": [{"name": "Table", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Bed",
        "Input": {"Items": [{"name": "Plank", "Count": 8}]},
        "Output": {"Items": [{"name": "Bed", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Rack",
        "Input": {"Items": [{"name": "Plank", "Count": 4}]},
        "Output": {"Items": [{"name": "Rack", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "WoodenStairs",
        "Input": {"Items": [{"name": "WoodenPlanks", "Count": 1}]},
        "Output": {"Items": [{"name": "WoodenStairs", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Stairs",
        "Input": {"Items": [{"name": "Bricks", "Count": 1}]},
        "Output": {"Items": [{"name": "Stairs", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Fence",
        "Input": {"Items": [{"name": "Plank", "Count": 3}]},
        "Output": {"Items": [{"name": "Fence", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "SteelFence",
        "Input": {"Items": [{"name": "SteelParts", "Count": 3}]},
        "Output": {"Items": [{"name": "SteelFence", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "StainlessSteelFence",
        "Input": {"Items": [{"name": "StainlessSteelParts", "Count": 3}]},
        "Output": {"Items": [{"name": "StainlessSteelFence", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Flashlight",
        "Input": {
            "Items": [
                {"name": "SteelPipe", "Count": 1},
                {"name": "SteelLamp", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "Flashlight", "Count": 1}]},
        "Ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "ConcreteTiles",
        "Input": {
            "Items": [
                {"name": "Concrete", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "ConcreteTiles", "Count": 1}]},
        "Ticks": 20,
    }
)
recipes_hand.append(
    {
        "name": "ConcreteSmallTiles",
        "Input": {
            "Items": [
                {"name": "Concrete", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "ConcreteSmallTiles", "Count": 1}]},
        "Ticks": 20,
    }
)
recipes_hand.append(
    {
        "name": "ConcreteBricks",
        "Input": {
            "Items": [
                {"name": "Concrete", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "ConcreteBricks", "Count": 1}]},
        "Ticks": 20,
    }
)
recipes_hand.append(
    {
        "name": "ReinforcedConcreteTiles",
        "Input": {
            "Items": [
                {"name": "ReinforcedConcrete", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "ReinforcedConcreteTiles", "Count": 1}]},
        "Ticks": 20,
    }
)
recipes_hand.append(
    {
        "name": "ReinforcedConcreteSmallTiles",
        "Input": {
            "Items": [
                {"name": "ReinforcedConcrete", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "ReinforcedConcreteSmallTiles", "Count": 1}]},
        "Ticks": 20,
    }
)
recipes_hand.append(
    {
        "name": "ReinforcedConcreteBricks",
        "Input": {
            "Items": [
                {"name": "ReinforcedConcrete", "Count": 1},
            ]
        },
        "Output": {"Items": [{"name": "ReinforcedConcreteBricks", "Count": 1}]},
        "Ticks": 20,
    }
)

for r in recipes_hand:
    r["Locked"] = True

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Hand" + recipe_dictionary,
        "Recipes": recipes_hand,
    }
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/misc_hand.json", data)
