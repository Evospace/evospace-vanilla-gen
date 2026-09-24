#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common import *

data = {
	"PlayerStartInventory":
	{
		"Items": [
			{
				"Name": "BuildingMaterial",
				"Count": 100
			}
		]
	}
}

write_file("Generated/Spawn/player.json", data);