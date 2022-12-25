from Common import *
from Materials import *

chapters = []
csv = []

# chapters.append({
# "class": static_chapter,
# "name": "Materials",
# "label_parts": [["Materials", "chapters"]],
# "description_parts": [["MaterialsDescription", "chapters"]],
# })
# csv.append(["Materials", "Materials"])
# csv.append(["MaterialsDescription", ""])

chapters.append(
    {
        "class": static_chapter,
        "name": "Production",
        "label_parts": [["Production", "chapters"]],
        "description_parts": [["ProductionDescription", "chapters"]],
    }
)
csv.append(["Production", "Production"])
csv.append(["ProductionDescription", ""])

chapters.append(
    {
        "class": static_chapter,
        "name": "Decorations",
        "label_parts": [["Decorations", "chapters"]],
        "description_parts": [["DecorationsDescription", "chapters"]],
    }
)
csv.append(["Decorations", "Decorations"])
csv.append(["DecorationsDescription", ""])


data = {"Objects": chapters}

write_file("Generated/Researches/chapters.json", data)
write_file("Loc/source/chapters.json", csv)
