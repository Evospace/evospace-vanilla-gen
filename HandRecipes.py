from Common import *
from MachinesList import *
from MiscGen import *
import copy

objects_array = []

recipes_hand = []

recipes_hand.append(
    {
        "name": "ClayBlock",
        "input": {"items": [{"name": "Clay", "count": 1}]},
        "output": {"items": [{"name": "ClayBlock", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Bricks",
        "input": {"items": [{"name": "StoneSurface", "count": 1}]},
        "output": {"items": [{"name": "Bricks", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "RedBricks",
        "input": {"items": [{"name": "RedStoneSurface", "count": 1}]},
        "output": {"items": [{"name": "RedBricks", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "DarkBricks",
        "input": {"items": [{"name": "DarkStoneSurface", "count": 1}]},
        "output": {"items": [{"name": "DarkBricks", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "SandSurface",
        "input": {
            "items": [
                {"name": "GravelSurface", "count": 1},
            ]
        },
        "output": {"items": [{"name": "SandSurface", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "GravelSurface",
        "input": {
            "items": [
                {"name": "StoneSurface", "count": 1},
            ]
        },
        "output": {"items": [{"name": "GravelSurface", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "StoneTiles",
        "input": {"items": [{"name": "StoneSurface", "count": 1}]},
        "output": {"items": [{"name": "StoneTiles", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "DarkTiles",
        "input": {"items": [{"name": "DarkStoneSurface", "count": 1}]},
        "output": {"items": [{"name": "DarkTiles", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "RedTiles",
        "input": {"items": [{"name": "RedStoneSurface", "count": 1}]},
        "output": {"items": [{"name": "RedTiles", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "TerracottaTiles",
        "input": {"items": [{"name": "Terracotta", "count": 1}]},
        "output": {"items": [{"name": "TerracottaTiles", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "TerracottaBricks",
        "input": {"items": [{"name": "TerracottaTiles", "count": 1}]},
        "output": {"items": [{"name": "TerracottaBricks", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "CircuitBoard",
        "input": {
            "items": [
                {"name": "Plank", "count": 1},
            ]
        },
        "output": {"items": [{"name": "CircuitBoard", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "GoldWire",
        "input": {
            "items": [
                {"name": "GoldIngot", "count": 1},
            ]
        },
        "output": {"items": [{"name": "GoldWire", "count": 2}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "CopperWire",
        "input": {
            "items": [
                {"name": "CopperIngot", "count": 1},
            ]
        },
        "output": {"items": [{"name": "CopperWire", "count": 2}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Circuit",
        "input": {
            "items": [
                {"name": "CopperWire", "count": 6},
                {"name": "CircuitBoard", "count": 1},
            ]
        },
        "output": {"items": [{"name": "Circuit", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "AdvancedCircuit",
        "input": {
            "items": [{"name": "Silicon", "count": 1}, {"name": "Circuit", "count": 1}]
        },
        "output": {"items": [{"name": "AdvancedCircuit", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Processor",
        "input": {
            "items": [
                {"name": "SiliconWafer", "count": 1},
                {"name": "AdvancedCircuit", "count": 1},
            ]
        },
        "output": {"items": [{"name": "Processor", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "QuantumCircuit",
        "input": {
            "items": [
                {"name": "QuantumCore", "count": 2},
                {"name": "Processor", "count": 1},
            ]
        },
        "output": {"items": [{"name": "QuantumCircuit", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "QuantumProcessor",
        "input": {
            "items": [
                {"name": "QuantumCircuit", "count": 2},
                {"name": "Processor", "count": 1},
            ]
        },
        "output": {"items": [{"name": "QuantumProcessor", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "WoodenChest",
        "input": {"items": [{"name": "Plank", "count": 6}]},
        "output": {"items": [{"name": "WoodenChest", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "WoodenPlanks",
        "input": {"items": [{"name": "Plank", "count": 1}]},
        "output": {"items": [{"name": "WoodenPlanks", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Steampack",
        "input": {
            "items": [
                {"name": "CopperParts", "count": 6},
                {"name": "CopperPlate", "count": 2},
                {"name": "CopperPipe", "count": 4},
                {"name": "Circuit", "count": 10},
            ]
        },
        "output": {"items": [{"name": "Steampack", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Jetpack",
        "input": {
            "items": [
                {"name": "AluminiumParts", "count": 10},
                {"name": "AluminiumPlate", "count": 3},
                {"name": "AluminiumPipe", "count": 6},
                {"name": "AdvancedCircuit", "count": 10},
                {"name": "AluminiumElectricEngine", "count": 2},
            ]
        },
        "output": {"items": [{"name": "Jetpack", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Torch",
        "input": {
            "items": [
                {"name": "Plank", "count": 1},
                {"name": "Organics", "count": 10},
            ]
        },
        "output": {"items": [{"name": "Torch", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "AdvancedJetpack",
        "input": {
            "items": [
                {"name": "StainlessSteelParts", "count": 10},
                {"name": "StainlessSteelPlate", "count": 3},
                {"name": "StainlessSteelPipe", "count": 6},
                {"name": "Processor", "count": 10},
                {"name": "StainlessSteelEngine", "count": 2},
            ]
        },
        "output": {"items": [{"name": "AdvancedJetpack", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Scanner",
        "input": {
            "items": [
                {"name": "SteelPlate", "count": 1},
                {"name": "AdvancedCircuit", "count": 2},
                {"name": "CopperConnector", "count": 5},
            ]
        },
        "output": {"items": [{"name": "Scanner", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "AntigravityUnit",
        "input": {
            "items": [
                {"name": "HardMetalParts", "count": 20},
                {"name": "HardMetalPlate", "count": 2},
                {"name": "HardMetalPipe", "count": 6},
                {"name": "QuantumProcessor", "count": 10},
                {"name": "Catalyst", "count": 4},
                {"name": "HardMetalElectricEngine", "count": 8},
            ]
        },
        "output": {"items": [{"name": "AntigravityUnit", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Plank",
        "input": {"items": [{"name": "Log", "count": 1}]},
        "output": {"items": [{"name": "Plank", "count": 2}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Chair",
        "input": {"items": [{"name": "Plank", "count": 4}]},
        "output": {"items": [{"name": "Chair", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "CopperChair",
        "input": {
            "items": [
                {"name": "Chair", "count": 1},
                {"name": "CopperPlate", "count": 1},
            ]
        },
        "output": {"items": [{"name": "CopperChair", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Ladder",
        "input": {"items": [{"name": "Plank", "count": 4}]},
        "output": {"items": [{"name": "Ladder", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Door",
        "input": {"items": [{"name": "Plank", "count": 8}]},
        "output": {"items": [{"name": "Door", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Window",
        "input": {
            "items": [{"name": "Glass", "count": 2}, {"name": "Plank", "count": 2}]
        },
        "output": {"items": [{"name": "Window", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "PlasticWindow",
        "input": {
            "items": [{"name": "Glass", "count": 2}, {"name": "Plastic", "count": 2}]
        },
        "output": {"items": [{"name": "PlasticWindow", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Table",
        "input": {"items": [{"name": "Plank", "count": 6}]},
        "output": {"items": [{"name": "Table", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Bed",
        "input": {"items": [{"name": "Plank", "count": 8}]},
        "output": {"items": [{"name": "Bed", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Rack",
        "input": {"items": [{"name": "Plank", "count": 4}]},
        "output": {"items": [{"name": "Rack", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "WoodenStairs",
        "input": {"items": [{"name": "WoodenPlanks", "count": 1}]},
        "output": {"items": [{"name": "WoodenStairs", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Stairs",
        "input": {"items": [{"name": "Bricks", "count": 1}]},
        "output": {"items": [{"name": "Stairs", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Fence",
        "input": {"items": [{"name": "Plank", "count": 3}]},
        "output": {"items": [{"name": "Fence", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "SteelFence",
        "input": {"items": [{"name": "SteelParts", "count": 3}]},
        "output": {"items": [{"name": "SteelFence", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "StainlessSteelFence",
        "input": {"items": [{"name": "StainlessSteelParts", "count": 3}]},
        "output": {"items": [{"name": "StainlessSteelFence", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "Flashlight",
        "input": {
            "items": [
                {"name": "SteelPipe", "count": 1},
                {"name": "SteelLamp", "count": 1},
            ]
        },
        "output": {"items": [{"name": "Flashlight", "count": 1}]},
        "ticks": 20,
    }
)

recipes_hand.append(
    {
        "name": "ConcreteTiles",
        "input": {
            "items": [
                {"name": "Concrete", "count": 1},
            ]
        },
        "output": {"items": [{"name": "ConcreteTiles", "count": 1}]},
        "ticks": 20,
    }
)
recipes_hand.append(
    {
        "name": "ConcreteSmallTiles",
        "input": {
            "items": [
                {"name": "Concrete", "count": 1},
            ]
        },
        "output": {"items": [{"name": "ConcreteSmallTiles", "count": 1}]},
        "ticks": 20,
    }
)
recipes_hand.append(
    {
        "name": "ConcreteBricks",
        "input": {
            "items": [
                {"name": "Concrete", "count": 1},
            ]
        },
        "output": {"items": [{"name": "ConcreteBricks", "count": 1}]},
        "ticks": 20,
    }
)
recipes_hand.append(
    {
        "name": "ReinforcedConcreteTiles",
        "input": {
            "items": [
                {"name": "ReinforcedConcrete", "count": 1},
            ]
        },
        "output": {"items": [{"name": "ReinforcedConcreteTiles", "count": 1}]},
        "ticks": 20,
    }
)
recipes_hand.append(
    {
        "name": "ReinforcedConcreteSmallTiles",
        "input": {
            "items": [
                {"name": "ReinforcedConcrete", "count": 1},
            ]
        },
        "output": {"items": [{"name": "ReinforcedConcreteSmallTiles", "count": 1}]},
        "ticks": 20,
    }
)
recipes_hand.append(
    {
        "name": "ReinforcedConcreteBricks",
        "input": {
            "items": [
                {"name": "ReinforcedConcrete", "count": 1},
            ]
        },
        "output": {"items": [{"name": "ReinforcedConcreteBricks", "count": 1}]},
        "ticks": 20,
    }
)

for r in recipes_hand:
    r["Locked"] = True

objects_array.append(
    {
        "class": recipe_dictionary,
        "name": "Hand" + recipe_dictionary,
        "recipes": recipes_hand,
    }
)

data = {"Objects": objects_array}

write_file("Generated/Recipes/misc_hand.json", data)
