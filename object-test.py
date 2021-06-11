#!/usr/bin/python3

import os
import sys
import traceback
from pathlib import Path
from typing import List

freecad_paths = [
    '/usr/lib/freecad/lib/',  # For CI
    '/usr/lib/freecad-daily-python3/lib/',  # For Ubuntu
    '/usr/lib64/freecad/lib64/',  # For Fedora
    '/Applications/FreeCAD.app/Contents/Resources/lib',  # For Mac OS X
    'c:/Program Files/FreeCAD 0.18/bin/',  # For Windows
    'c:/Program Files/FreeCAD 0.19/bin/',  # For Windows
]

for path in freecad_paths:
    if os.path.exists(path):
        print(f"Added possible FreeCAD path: {path}")
        sys.path.append(path)

import FreeCAD
import MeshPart

print('Python version:')
print(sys.version)

print('FreeCAD version:')
print(FreeCAD.Version())


def process_file(cad_file: Path):
    print("Processing " + cad_file.name)

    doc = FreeCAD.open(str(cad_file.absolute()))
    
    for obj in doc.Objects:
        print(f"- {obj.Label}")


if __name__ == '__main__':
    process_file(Path('FDM-0015_down-light-mount.FCStd'))
