from Common import *
from Materials import *

chapters = []
csv = []

# chapters.append({
	# "Class": static_chapter,
	# "Name": "Materials" + static_chapter,
	# "LabelParts": [["Materials", "chapters"]],
	# "DescriptionParts": [["MaterialsDescription", "chapters"]],
# })
# csv.append(["Materials", "Materials"])
# csv.append(["MaterialsDescription", ""])

chapters.append({
	"Class": static_chapter,
	"Name": "Production" + static_chapter,
	"LabelParts": [["Production", "chapters"]],
	"DescriptionParts": [["ProductionDescription", "chapters"]],
})
csv.append(["Production", "Production"])
csv.append(["ProductionDescription", ""])

chapters.append({
	"Class": static_chapter,
	"Name": "Decorations" + static_chapter,
	"LabelParts": [["Decorations", "chapters"]],
	"DescriptionParts": [["DecorationsDescription", "chapters"]],
})
csv.append(["Decorations", "Decorations"])
csv.append(["DecorationsDescription", ""])


data = {
	"Objects": chapters
}

write_file("Generated/Researches/chapters.json", data);
write_file("Loc/source/chapters.json", csv)