"""Generate the project-local mechanical-envelope STEP models.

Run with FreeCAD 1.1:
    freecadcmd.exe tools/generate_3d_models.py

The models deliberately represent verified body, pin and installed-height
geometry.  Fine cosmetic features that are not dimensioned by the suppliers
are omitted.
"""

from pathlib import Path

import FreeCAD as App
import Import
import Part


PROJECT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT / "Photobooth.3dshapes"
OUTPUT.mkdir(parents=True, exist_ok=True)


def feature(doc, name, shape, color):
    obj = doc.addObject("PartDesign::Feature", name)
    obj.Shape = shape
    # FreeCADCmd has no GUI ViewObject; keep the color argument as design intent
    # for a future GUI export while producing portable AP214 geometry headlessly.
    return obj


def export_document(doc, filename):
    doc.recompute()
    objects = [obj for obj in doc.Objects if hasattr(obj, "Shape") and not obj.Shape.isNull()]
    Import.export(objects, str(OUTPUT / filename))
    App.closeDocument(doc.Name)


def phoenix_spt(poles):
    pitch = 3.5
    width = (poles - 1) * pitch + 4.9
    x_min = -1.3
    y_min = -2.75
    depth = 13.5
    height = 14.4

    doc = App.newDocument(f"Phoenix_SPT_{poles}")
    body = Part.makeBox(width, depth, height, App.Vector(x_min, y_min, 0))

    # Dimensionally representative top-entry openings.
    for pole in range(poles):
        x = pole * pitch
        opening = Part.makeCylinder(1.0, 1.2, App.Vector(x, 1.15, height - 1.2))
        body = body.cut(opening)
    feature(doc, "Green_housing", body, (0.12, 0.55, 0.24))

    for pole in range(poles):
        x = pole * pitch
        button = Part.makeBox(1.8, 2.2, 0.5, App.Vector(x - 0.9, 6.0, height))
        feature(doc, f"Actuator_{pole + 1}", button, (0.94, 0.48, 0.08))
        for row, y in enumerate((0.0, 8.2), start=1):
            pin = Part.makeBox(0.8, 0.8, 2.5, App.Vector(x - 0.4, y - 0.4, -2.5))
            feature(doc, f"Pin_{pole + 1}_{row}", pin, (0.78, 0.78, 0.75))

    part_number = {2: "1990850", 3: "1990863", 4: "1990876"}[poles]
    export_document(doc, f"PhoenixContact_SPT_1.5_{poles}-V-3.5_{part_number}.step")


def optifuse_cnt06():
    doc = App.newDocument("OptiFuse_CNT_06")
    body = Part.makeBox(11.6, 4.8, 9.6, App.Vector(-5.8, -3.6, 0))
    # Show the two blade-entry slots without asserting an undimensioned internal profile.
    for x in (-2.45, 2.45):
        slot = Part.makeBox(1.9, 0.7, 1.2, App.Vector(x - 0.95, -1.2, 8.8))
        body = body.cut(slot)
    feature(doc, "Insulating_housing", body, (0.10, 0.10, 0.11))

    for number, x in enumerate((-2.45, 2.45), start=1):
        pin = Part.makeBox(1.6, 0.3, 4.6, App.Vector(x - 0.8, -0.15, -4.6))
        feature(doc, f"Terminal_{number}", pin, (0.78, 0.78, 0.74))
    peg = Part.makeBox(2.7, 1.4, 2.0, App.Vector(-1.35, -3.4, -2.0))
    feature(doc, "Retention_peg", peg, (0.10, 0.10, 0.11))
    export_document(doc, "OptiFuse_CNT-06_MICRO2.step")


def qlrelay_brd_ss_105l():
    doc = App.newDocument("QLRELAY_BRD_SS_105L")
    body = Part.makeBox(19.0, 15.4, 15.5, App.Vector(-9.5, -7.7, 0))
    feature(doc, "Relay_case", body, (0.10, 0.24, 0.43))
    marking = Part.makeBox(11.0, 0.04, 0.04, App.Vector(-5.5, -0.02, 15.5))
    feature(doc, "Top_mark", marking, (0.86, 0.88, 0.90))

    pin_data = (
        (1, -7.1, -6.0, 1.3),
        (2, -7.1, 6.0, 1.3),
        (3, 5.1, -6.0, 1.0),
        (4, 5.1, 6.0, 1.0),
        (5, 7.1, 0.0, 1.3),
    )
    for number, x, y, diameter in pin_data:
        pin = Part.makeCylinder(diameter / 2, 3.5, App.Vector(x, y, -3.5))
        feature(doc, f"Pin_{number}", pin, (0.78, 0.78, 0.74))
    export_document(doc, "QLRELAY_BRD-SS-105L.step")


for pole_count in (2, 3, 4):
    phoenix_spt(pole_count)
optifuse_cnt06()
qlrelay_brd_ss_105l()

print(f"Generated project STEP models in {OUTPUT}")
