from Common import *

# Specify meshes in Content. Name will be derived from the last path segment
# Optionally, provide a dict with explicit Name/Image/Materials

cover_meshes = [
    # Examples:
    # "/Game/Covers/PipeCenter",
    # {"Mesh": "/Game/Covers/PipeSide", "Name": "PipeSide", "Materials": ["/Game/Materials/Steel"]},

    {"Mesh": "/Game/Covers/WireCover", "Name": "WireCover", "Materials": []},    
    {"Mesh": "/Game/Covers/GlassPipeCover", "Name": "GlassPipeCover", "Materials": []},    
]

def derive_name(path: str) -> str:
    return path.split('/')[-1]

objects = []

for entry in cover_meshes:
    if isinstance(entry, str):
        mesh = entry
        name = derive_name(mesh)
        materials = None
        image = "T_" + name
    else:
        mesh = entry["Mesh"]
        name = entry.get("Name", derive_name(mesh))
        materials = entry.get("Materials", None)
        image = entry.get("Image", "T_" + name)

    # StaticCover definition (avoid shadowing the Common.static_cover constant)
    cover_proto = {
        "Class": static_cover,
        "Name": name,
        "Mesh": mesh,
        "NumCustomData": 3
    }
    if materials:
        cover_proto["Materials"] = materials

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
    objects.append(cover_proto)

data = {"Objects": objects}
write_file("Generated/Mixed/cover_items.json", data)


