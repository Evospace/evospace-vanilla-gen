from Common import *

def get_parts_unlocks(material, with_pipe = True):
    unlocks = [["Hand" + r_dict, material + "Parts"]]
    if with_pipe:
        unlocks += [
            ["Hand" + r_dict, material + "Pipe"],
            ["Constructor" + r_dict, material + "Pipe"]
        ]
    return unlocks
