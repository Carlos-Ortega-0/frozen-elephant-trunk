# Design Notes

## Goal

Model a frozen elephant trunk hybrid graft as a full assembly, with each real component as its own body and material, so it can be measured, resized and studied.

## Parts and materials

Material names come from the Fusion/STEP file.

| Body | Material in model | Count |
|---|---|---|
| Arch graft | Arch_graft_wovenPET_gelatin | 2 bodies (main arch + junction piece) |
| Stented trunk | Stent_graft_fabric_PET | 1 |
| Sewing collar | Sewing_collar_PET | 1 |
| Z-stents | Zstents_Nitinol | 6 |
| Markers | Markers_PtIr | 4 |

## Measured dimensions (mm)

From `scripts/measure.py` and cross-sections of the STL.

### Arch graft
- Main lumen: 28.0 ID, 29.2 OD (0.6 mm wall)
- Length along the arch: 134.4
- Head-vessel branches: one 10.9 ID (about 12.8 OD), two 8.7 ID (about 10.6 OD)
- Perfusion side arm: 15.6 ID
- Openings: proximal end, distal end at the collar, three branches, one side arm

### Stented trunk
- 28.0 ID, 28.6 OD (0.3 mm fabric)
- 118.0 long

### Sewing collar
- 45.2 OD, 29.2 ID, 3.0 thick

### Z-stents
- 6 rings, 30.6 OD, 10.5 tall
- Wire about 0.6 mm
- Spaced every 20 mm along the trunk

### Markers
- 4 beads, 1.6 mm diameter

### Junction piece
- Arch graft material, 24.3 diameter, 6.5 thick, coaxial with the trunk at the collar

## How parts connect

1. Arch graft replaces the ascending aorta and arch. Its three branches go to the head vessels.
2. The distal end of the arch meets the sewing collar.
3. The stented trunk runs from the collar down into the descending aorta.
4. Z-stents sit along the trunk and hold it open.
5. Markers show the trunk position on imaging: three at the distal end of the trunk, one near the collar.

## Open questions

- Purpose of the junction piece in the final design
- Target patient size range for future variants
