#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common import *

data = {
	"PlayerStartInventory":
	{
		"Items": [
			{
				"Name": "StoneSurface" + static_item,
				"Count": 99
			},
			{
				"Name": "Log" + static_item,
				"Count": 15
			},
			{
				"Name": "BasicPlatform" + static_item,
				"Count": 99
			}
		]
	}
}

write_file("Generated/Spawn/player.json", data);