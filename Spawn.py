#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common import *

data = {
    "PlayerStartInventory": {
        "items": [
            {"name": "CopperMultitool", "count": 1},
            {"name": "StoneSurface", "count": 99},
            {"name": "Log", "count": 15},
            {"name": "BasicPlatform", "count": 99},
        ]
    }
}

write_file("Generated/Spawn/player.json", data)
