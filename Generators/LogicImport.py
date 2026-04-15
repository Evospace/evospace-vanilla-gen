from Common import *

logic_imports = []

objects_array = []

for logic_import in logic_imports:
    logic_import["Class"] = "LogicImportOption"
    objects_array.append(logic_import)

data = {
    "Objects": objects_array
}

write_file("Generated/Mixed/logic_import.json", data)
