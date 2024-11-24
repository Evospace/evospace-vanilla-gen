from Common import *

cvs = []

cvs.append(["ActiveSlot_0", "Hotbar 0"])
cvs.append(["ActiveSlot_1", "Hotbar 1"])
cvs.append(["ActiveSlot_2", "Hotbar 2"])
cvs.append(["ActiveSlot_3", "Hotbar 4"])
cvs.append(["ActiveSlot_4", "Hotbar 4"])
cvs.append(["ActiveSlot_5", "Hotbar 5"])
cvs.append(["ActiveSlot_6", "Hotbar 6"])
cvs.append(["ActiveSlot_7", "Hotbar 7"])
cvs.append(["ActiveSlot_8", "Hotbar 8"])
cvs.append(["ActiveSlot_9", "Hotbar 9"])

cvs.append(["ActionPrimary", "Use item"])
cvs.append(["ActionSecondary", "Use block"])
cvs.append(["ActionTernary", "Hovered object info"])
cvs.append(["ChangeMovementMode", "Sprint"])
cvs.append(["Crouch", "Crouch"])
cvs.append(["EmptyHand", "Empty hand"])
cvs.append(["Researches", "Researches"])

cvs.append(["EssentialResearchDescription", "This ressearch is essential for game progress"])

cvs.append(["BasicMachinesDescription", "First step in resource processing for better yield"])

write_file("Loc/source/ui.json", cvs)

