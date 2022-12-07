#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common import *

data = {
	"PlayerStartInventory":
	{
		"Items": [
			{
				"Name": "CopperMultitool",
				"Count": 1
			},
			{
				"Name": "StoneSurface",
				"Count": 99
			},
			{
				"Name": "Log",
				"Count": 15
			},
			{
				"Name": "BasicPlatform",
				"Count": 99
			}
		]
	}
}

write_file("Generated/Spawn/player.json", data);