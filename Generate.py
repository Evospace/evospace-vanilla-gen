import platform
import subprocess
import shutil
import os
import os.path
import sys

our_path = os.path.dirname(os.path.abspath(sys.argv[0]))
print(our_path)

for dirpath, dirnames, filenames in os.walk(our_path + "/Generators/"):
  for filename in [f for f in filenames if f.endswith(".py")]:
    fullname = os.path.join(dirpath, filename)
    print(fullname + " is runned")
    if platform.system() == "Windows":
      popen = subprocess.call(["python ", fullname])
    else:
      popen = subprocess.call(["python3", fullname])
    print("Done")
