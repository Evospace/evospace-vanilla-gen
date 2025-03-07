from Common import *

def get_parts_unlocks(material):
    return [
        ["Hand" + r_dict, material + "Parts"],
        ["Hand" + r_dict, material + "Plate"],
        ["Hand" + r_dict, material + "Pipe"],
        ["Hand" + r_dict, material + "Gearbox"],
        [assembler_r_dict, material + "Gearbox"],
        ["Constructor" + r_dict, material + "Pipe"]
    ]