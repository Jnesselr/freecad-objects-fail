# Introduction

This is a simple test repo used to reproduce a bug in FreeCAD. The issue is that on some installations, running the included python script will show a part called "Body" but on other installations (like Ubuntu 20.04 LTS in GitHub actions or a Digital Ocean server) will only show things like sketch planes and datums.

The included setup shell script is only designed to work on Ubuntu. Run the python script with python3. The part included here is from Stephen Hawes' Index PnP project where this bug was first identified.

# Examples
The script spits out the python version, the FreeCAD version, and all objects that it can see. Here's an example where the "Good" case was run on my Mac and the "Bad" case was run on an Ubuntu 20.04 LTS server running in Digital Ocean.

## Good

```
Added possible FreeCAD path: /Applications/FreeCAD.app/Contents/Resources/lib
Python version:
3.9.2 (default, Feb 24 2021, 13:26:09)
[Clang 12.0.0 (clang-1200.0.32.29)]
FreeCAD version:
['0', '19', '24291 (Git)', '/Users/runner/miniforge3/conda-bld/git_cache/github.com/FreeCAD/FreeCAD', '2021/04/15 09:17:08', '(HEAD detached at 0.19.2)', '7b5e18a0759de778b74d3a5c17eba9cb815035ac']
Processing FDM-0015_down-light-mount.FCStd
- Body
- Origin
- X_Axis
- Y_Axis
- Z_Axis
- XY_Plane
- XZ_Plane
- YZ_Plane
- Sketch
- Pad
- Sketch001
- Pad001
- DatumPlane
- Sketch002
- Pocket
- Sketch003
- Pocket001
- Chamfer
- Sketch004
- Pocket002
```

## Bad

```
Added possible FreeCAD path: /usr/lib/freecad-daily-python3/lib/
Python version:
3.8.5 (default, May 27 2021, 13:30:53)
[GCC 9.3.0]
FreeCAD version:
['0', '19', '', 'git://github.com/FreeCAD/FreeCAD.git unknown', '2021/03/04 07:28:00', 'unknown', 'e8566f22bbeb0b7204e3c45519d0963e8881100b']
Processing FDM-0015_down-light-mount.FCStd
- Origin
- X_Axis
- Y_Axis
- Z_Axis
- XY_Plane
- XZ_Plane
- YZ_Plane
- Sketch
- Sketch001
- Sketch002
- Sketch003
- Sketch004
```
