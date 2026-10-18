from Common import *

cover_meshes = [
    {"Name": "WireCover"},
]

objects = []

for entry in cover_meshes:
    name = entry.get("Name", entry["Name"])
    image = entry.get("Image", "T_" + name)

    static_item = {
        "Class": "StaticItem",
        "Name": name,
        "StackSize": 32,
        "Image": image,
        "ItemLogic": cover_item_logic,
        "Category": "Decoration",
        "Label": [name, "props"],
        "DescriptionParts": [["WorldObject", "common"]],
        "Cover": name
    }

    objects.append(static_item)

data = {"Objects": objects}
write_file("Generated/Mixed/cover_items.json", data)