from Common import *

# Specify meshes in Content. Name will be derived from the last path segment
# Optionally, provide a dict with explicit Name/Image/Materials

cover_meshes = [
    # Examples:
    # "/Game/Covers/PipeCenter",
    # {"Mesh": "/Game/Covers/PipeSide", "Name": "PipeSide", "Materials": ["/Game/Materials/Steel"]},

    {"Name": "WireCover"},   
]

objects = []

for entry in cover_meshes:
    name = entry.get("Name", entry["Name"])
    image = entry.get("Image", "T_" + name)

    # StaticItem with CoverItemLogic and link to the cover
    static_item = {
        "Class": "StaticItem",
        "Name": name,
        "StackSize": 32,
        "Image": image,
        "ItemLogic": cover_item_logic,
        "Category": "Terrain",
        "Label": [name, "props"],
        "DescriptionParts": [["WorldObject", "common"]],
        "Cover": name
    }

    objects.append(static_item)

data = {"Objects": objects}
write_file("Generated/Mixed/cover_items.json", data)