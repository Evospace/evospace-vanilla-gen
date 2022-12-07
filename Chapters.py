from Common import *
from Materials import *

chapters = []
csv = []

# chapters.append({
	# "Class": static_chapter,
	# "Name": "Materials",
	# "LabelParts": [["Materials", "chapters"]],
	# "DescriptionParts": [["MaterialsDescription", "chapters"]],
# })
# csv.append(["Materials", "Materials"])
# csv.append(["MaterialsDescription", ""])

chapters.append({
	"Class": static_chapter,
	"Name": "Production",
	"LabelParts": [["Production", "chapters"]],
	"DescriptionParts": [["ProductionDescription", "chapters"]],
})
csv.append(["Production", "Production"])
csv.append(["ProductionDescription", ""])

chapters.append({
	"Class": static_chapter,
	"Name": "Decorations",
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