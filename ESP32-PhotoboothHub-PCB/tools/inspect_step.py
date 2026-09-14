import FreeCAD as App
import Import
import sys


for path in sys.argv[2:]:
    Import.open(path)
    doc = App.ActiveDocument
    boxes = []
    for obj in doc.Objects:
        if not hasattr(obj, "Shape") or obj.Shape.isNull():
            continue
        candidate = obj.Shape.BoundBox
        if candidate.isValid() and max(candidate.XLength, candidate.YLength, candidate.ZLength) < 1e6:
            boxes.append(candidate)
    box = boxes[0]
    for other in boxes[1:]:
        box.add(other)
    print(
        f"{path}: objects={len(boxes)} "
        f"min=({box.XMin:.6f},{box.YMin:.6f},{box.ZMin:.6f}) "
        f"max=({box.XMax:.6f},{box.YMax:.6f},{box.ZMax:.6f}) "
        f"size=({box.XLength:.6f},{box.YLength:.6f},{box.ZLength:.6f})"
    )
    candidates = []
    for obj in doc.Objects:
        if not hasattr(obj, "Shape") or obj.Shape.isNull():
            continue
        candidate = obj.Shape.BoundBox
        if candidate.isValid() and max(candidate.XLength, candidate.YLength, candidate.ZLength) < 1e6:
            candidates.append((candidate.XLength * candidate.YLength, obj.Label, candidate))
    for _, label, candidate in sorted(candidates, reverse=True)[:12]:
        print(
            f"  {label}: min=({candidate.XMin:.3f},{candidate.YMin:.3f},{candidate.ZMin:.3f}) "
            f"max=({candidate.XMax:.3f},{candidate.YMax:.3f},{candidate.ZMax:.3f}) "
            f"size=({candidate.XLength:.3f},{candidate.YLength:.3f},{candidate.ZLength:.3f})"
        )
    App.closeDocument(doc.Name)
