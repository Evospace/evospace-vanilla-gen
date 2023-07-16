from Common import *

cvs = []

cvs.append(["I", "I"])
cvs.append(["II", "II"])
cvs.append(["III", "III"])
cvs.append(["IV", "IV"])
cvs.append(["V", "V"])
cvs.append(["VI", "VI"])
cvs.append(["VII", "VII"])
cvs.append(["VIII", "VIII"])
cvs.append(["IX", "IX"])
cvs.append(["X", "X"])

cvs.append(["Organics", "Mixed organics mass"])
cvs.append(["BuildingBlock", "Building block"])
cvs.append(["NuclearFuel","Fuel for Fission Reactor"])
cvs.append(["Fluid","Fluid"]) 
cvs.append(["Gas","Gas"])
cvs.append(["ByPipes","""Can be transported by pipes
Can be injected/extracted from machines by pumps"""])
cvs.append(["WorldObject","""Can't be crafted
Appears in world"""])
cvs.append(["Circuit","""Part of smart devices
Used by computers to produce science points"""])

cvs.append(["ItemInput", "<img id=\"ItemInput\"></>Has item input"])
cvs.append(["ItemOutput", "<img id=\"ItemOutput\"></>Has item ouput"])

cvs.append(["FluidInput", "<img id=\"FluidInput\"></>Has fluid input"])
cvs.append(["FluidOutput", "<img id=\"FluidOutput\"></>Has fluid ouput"])
cvs.append(["FluidConductor", "Conducts fluids"])
cvs.append(["FluidStorage", "Stores fluids"])

cvs.append(["KineticInput", "<img id=\"Kinetic\"></>Consumes kinetic energy<img id=\"Kinetic2\"></>"])
cvs.append(["KineticOutput", "<img id=\"Kinetic\"></>Produces kinetic energy<img id=\"Kinetic2\"></>"])
cvs.append(["KineticConductor", "<img id=\"Kinetic\"></>Conducts kinetic energy<img id=\"Kinetic2\"></>"])
cvs.append(["KineticStorage", "Stores kinetic energy<img id=\"Kinetic2\"></>"])

cvs.append(["HeatInput", "<img id=\"Heat\"></>Consumes heat energy<img id=\"Heat2\"></>"])
cvs.append(["HeatOutput", "<img id=\"Heat\"></>Produces heat energy<img id=\"Heat2\"></>"])
cvs.append(["HeatConductor", "<img id=\"Heat\"></>Conducts heat energy<img id=\"Heat2\"></>"])
cvs.append(["HeatStorage", "Stores heat energy<img id=\"Heat2\"></>"])

cvs.append(["ElectricInput", "<img id=\"Electricity\"></>Consumes electricity<img id=\"Electricity2\"></>"])
cvs.append(["ElectricOutput", "<img id=\"Electricity\"></>Produces electricity<img id=\"Electricity2\"></>"])
cvs.append(["ElectricConductor", "<img id=\"Electricity\"></>Conducts electricity<img id=\"Electricity2\"></>"])
cvs.append(["ElectricStorage", "Stores electricity<img id=\"Electricity2\"></>"])

cvs.append(["MachineColumn", "Have more item output slots with more stacked layers"])

cvs.append(["DataInput", "Read data"])
cvs.append(["DataOutput", "Write data"])
cvs.append(["DataConductor", "Conducts data"])

cvs.append(["Stone", "Stone"])
cvs.append(["Copper", "Copper"])
cvs.append(["Steel", "Steel"])
cvs.append(["Aluminium", "Aluminium"])
cvs.append(["StainlessSteel", "Stainless Steel"])
cvs.append(["Titanium", "Titanium"])
cvs.append(["HardMetal", "Hard Metal"])
cvs.append(["Neutronium", "Neutronium"])

cvs.append(["Splitter", "Can divide item flow into parts."])
cvs.append(["Sorter", "Allowing to set white filter."])

cvs.append(["ips", "Items per second: {0}"])
cvs.append(["dps", "Degrees per second: {0}"])
cvs.append(["power_limit", "Power limit: {0}W"])
cvs.append(["power_output", "Power output: {0}W"])
cvs.append(["power_input", "Power input: {0}W"])
cvs.append(["container", "Capacity: {0} L"])
cvs.append(["battery", "Capacity: {0} J"])
cvs.append(["chest", "Capacity: {0} stacks"])
cvs.append(["item_rack", "Capacity: {0} items"])
cvs.append(["burnable", "Burnable"])
cvs.append(["speedbonus", "Speed bonus: x{0}"])
cvs.append(["furnace_desc", "Burning speed: x{0}"])
cvs.append(["furnace_desc2", "Heat output: x{0}"])
cvs.append(["furnace_desc3", "Kinetic output: x{0}"])

cvs.append(["electric_drain", "Electricity drain: {0}W"])
cvs.append(["heat_drain", "Heat drain: {0}W"])
cvs.append(["kinetic_drain", "Kinetic drain: {0}W"])

cvs.append(["computations", "Computations per second: {0}"])

cvs.append(["calculations", """Produced by computers
Build Computer and power it with electricity to produce Computations"""])

cvs.append(["WorldGeneratorRivers", "Rivers and isles"])
cvs.append(["WorldGeneratorBiome", "Rocky islands"])
cvs.append(["FlatWorldGenerator", "Concrete world"])
cvs.append(["WorldGeneratorPlains", "Plains and coast"])

cvs.append(["machines_label_format", "{0} {1}"])


write_file("Loc/source/common.json", cvs)

