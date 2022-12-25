#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common import *

data = {
    "PlayerStartInventory": {
        "Items": [
            {"name": "CopperMultitool", "Count": 1},
            {"name": "StoneSurface", "Count": 99},
            {"name": "Log", "Count": 15},
            {"name": "BasicPlatform", "Count": 99},
        ]
    }
}

write_file("Generated/Spawn/player.json", data)
