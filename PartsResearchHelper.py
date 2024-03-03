from Common import *

def get_parts_unlocks(material):
    return [
        ["Hand" + base_recipe, material + "Parts"],
        ["Hand" + base_recipe, material + "Plate"],
        ["Hand" + base_recipe, material + "Pipe"],
        ["Hand" + base_recipe, material + "Gearbox"],
        ["Assembler" + base_recipe, material + "Gearbox"],
        ["Constructor" + base_recipe, material + "Pipe"]
    ]