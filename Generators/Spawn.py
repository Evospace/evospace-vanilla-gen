#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common import *

data = {
	"PlayerStartInventory":
	{
		"Items": [
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
				"Count": 999
			}
		]
	}
}

write_file("Generated/Spawn/player.json", data);