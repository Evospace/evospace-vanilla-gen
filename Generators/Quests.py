from Common import *

objects = [
    {
        "Class": "StaticChapter",
        "Name": "Tutorial",
        "Label": ["TutorialChapter", "quests"],
        "DescriptionParts": [["TutorialChapterDescription", "quests"]],
        "Quests": ["PlaceFirstBlock"],
    },
    {
        "Class": "StaticQuest",
        "Name": "PlaceFirstBlock",
        "Chapter": "Tutorial",
        "Label": ["PlaceFirstBlock", "quests"],
        "DescriptionParts": [["PlaceFirstBlockDescription", "quests"]],
        "AutoUnlock": True,
    },
]

write_file("Generated/Mixed/quests.json", {"Objects": objects})
