from pathlib import Path

import os

oldfilename = "./hello"
newfilename = oldfilename + "2" + ".txt"
filename = oldfilename + (".txt")

with open(filename, "r") as f:
    content = f.read()

with open(newfilename, "w") as f:
    f.write(content)
