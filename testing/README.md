# Testing

## 1. Geometry check (done)

`scripts/measure.py` splits the STL into bodies and reports size and volume.

Result: 14 bodies, all watertight on their own. The combined mesh is not one watertight solid, which is expected for a multi-body assembly.

## 2. Display print (to do)

- [ ] Thicken walls to 1.2 mm or use resin
- [ ] Print arch and trunk separately
- [ ] Trunk seats in collar without gaps

## 3. Flow study (to do)

- [ ] Export fluid domain from the arch lumen
- [ ] CFD run at resting cardiac output
- [ ] Compare flow split across the three branches

## 4. Review (to do)

- [ ] Feedback from a cardiovascular surgeon
