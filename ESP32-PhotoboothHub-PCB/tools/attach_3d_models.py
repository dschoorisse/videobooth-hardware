"""Attach project-local STEP files to placed custom footprints.

Run with KiCad's bundled Python:
    "C:/Program Files/KiCad/10.0/bin/python.exe" tools/attach_3d_models.py
"""

from pathlib import Path

import pcbnew


PROJECT = Path(__file__).resolve().parents[1]
BOARD = PROJECT / "ProPrj_New Project_2025-09-22_16-04-54_2026-09-08.kicad_pcb"

MODELS = {
    "Fuseholder_OptiFuse_CNT-06_MICRO2": [
        ("${KIPRJMOD}/Photobooth.3dshapes/OptiFuse_CNT-06_MICRO2.step", (0.0, 0.0, 0.0)),
    ],
    "Olimex_ESP32-POE-ISO": [
        ("${KICAD10_3DMODEL_DIR}/Connector_PinSocket_2.54mm.3dshapes/PinSocket_1x10_P2.54mm_Vertical.step", (0.0, 0.0, 0.0)),
        ("${KICAD10_3DMODEL_DIR}/Connector_PinSocket_2.54mm.3dshapes/PinSocket_1x10_P2.54mm_Vertical.step", (25.4, 0.0, 0.0)),
        ("${KIPRJMOD}/Photobooth.3dshapes/ESP32-PoE-ISO_Rev_L.step", (-1.29, -64.93, 8.5)),
    ],
    "PhoenixContact_SPT_1.5_2-V-3.5_1990850": [
        ("${KIPRJMOD}/Photobooth.3dshapes/PhoenixContact_SPT_1.5_2-V-3.5_1990850.step", (0.0, 0.0, 0.0)),
    ],
    "PhoenixContact_SPT_1.5_3-V-3.5_1990863": [
        ("${KIPRJMOD}/Photobooth.3dshapes/PhoenixContact_SPT_1.5_3-V-3.5_1990863.step", (0.0, 0.0, 0.0)),
    ],
    "PhoenixContact_SPT_1.5_4-V-3.5_1990876": [
        ("${KIPRJMOD}/Photobooth.3dshapes/PhoenixContact_SPT_1.5_4-V-3.5_1990876.step", (0.0, 0.0, 0.0)),
    ],
    "Relay_SPDT_QLRELAY_BRD-SS-105L": [
        ("${KIPRJMOD}/Photobooth.3dshapes/QLRELAY_BRD-SS-105L.step", (0.0, 0.0, 0.0)),
    ],
}


board = pcbnew.LoadBoard(str(BOARD))
attached = []
for footprint in board.GetFootprints():
    item_name = str(footprint.GetFPID().GetLibItemName())
    if item_name not in MODELS:
        continue
    if len(footprint.Models()) != 0:
        raise RuntimeError(f"{footprint.GetReference()} already has a 3D model")

    for filename, offset in MODELS[item_name]:
        model = pcbnew.FP_3DMODEL()
        model.m_Filename = filename
        model.m_Offset = pcbnew.VECTOR3D(*offset)
        model.m_Scale = pcbnew.VECTOR3D(1.0, 1.0, 1.0)
        model.m_Rotation = pcbnew.VECTOR3D(0.0, 0.0, 0.0)
        footprint.Add3DModel(model)
    attached.append(footprint.GetReference())

pcbnew.SaveBoard(str(BOARD), board)
print(f"Attached project models to {len(attached)} footprints: {', '.join(sorted(attached))}")
