from Common import *

def get_parts_unlocks(material):
    return [
        ["Hand" + r_dict, material + "Parts"],
        ["Hand" + r_dict, material + "Pipe"],
        ["Constructor" + r_dict, material + "Pipe"]
    ]