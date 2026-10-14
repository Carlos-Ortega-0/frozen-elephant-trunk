"""Measure every body in the exported STL.

Prints bounding box, volume and watertightness per body, largest first.
Usage:
    pip install trimesh manifold3d shapely
    python scripts/measure.py stl/Aortic_Arch_FET.stl
"""
import sys

import trimesh

path = sys.argv[1] if len(sys.argv) > 1 else "stl/Aortic_Arch_FET.stl"
mesh = trimesh.load(path)

print(f"Triangles: {len(mesh.faces)}")
print(f"Envelope (mm): {mesh.extents.round(1).tolist()}")

bodies = sorted(mesh.split(only_watertight=False), key=lambda b: -abs(b.volume))
print(f"Bodies: {len(bodies)}")
for i, b in enumerate(bodies):
    print(
        f"{i:>2}  bbox {b.extents.round(1).tolist()} mm  "
        f"vol {abs(b.volume) / 1000:.2f} cm3  watertight={b.is_watertight}"
    )
