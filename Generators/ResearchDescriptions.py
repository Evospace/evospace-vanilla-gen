import os
import re

from Common import *

table = "research_descriptions"
loc_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Evospace-Localization", "en", "base.ini")

def section_keys(path, section):
	keys = set()
	current = None
	with open(path, encoding="utf-8-sig") as ini:
		for line in ini:
			header = re.match(r"^\[(.+)\]\s*$", line)
			if header:
				current = header.group(1)
			elif current == section and "=" in line:
				keys.add(line.split("=", 1)[0])
	return keys

written = section_keys(loc_path, table) if os.path.exists(loc_path) else None

researches = get_generated_files()["Generated/Researches/basic.json"]["Objects"]
missing = []
for research in researches:
	label = research.get("Label")
	if research.get("DescriptionParts") or not isinstance(label, list) or len(label) < 2 or label[1] != "researches":
		continue
	research["DescriptionParts"] = [[label[0], table]]
	if written is not None and label[0] not in written:
		missing.append(label[0])

for key in sorted(set(missing)):
	print(f"ResearchDescriptions warning: no [{table}] {key} in en/base.ini")
