# Project 3D models

All fitted electrical footprints have a resolvable STEP model. The four M3
mounting-hole footprints intentionally have no component body.

| References | Model | Fidelity |
|---|---|---|
| U2 | `ESP32-PoE-ISO_Rev_L.step` plus two KiCad `PinSocket_1x10` models | Official Olimex full-board assembly export on two single-row female sockets |
| J1–J7 | Three local Phoenix SPT 1.5 models | Verified body, height, pins and representative top-entry details |
| F1–F4 | `OptiFuse_CNT-06_MICRO2.step` | Verified holder envelope, terminals and retention peg; fuse not included |
| K3 | `QLRELAY_BRD-SS-105L.step` | Verified body envelope and five pin positions |
| Remaining fitted parts | KiCad 10 standard models | Model supplied by the installed footprint library |

The U2 source is Olimex's official
[`ESP32-PoE-ISO_Rev_L.step`](https://ftp.olimex.com/TEMP/ESP32-PoE-ISO-step-export/ESP32-PoE-ISO_Rev_L.step)
export. Olimex warns that individual component heights were not fully checked.
The model is aligned to the verified 28 × 98.15 mm module outline and placed at
the 8.5 mm top surface of two standard KiCad 1×10, 2.54 mm-pitch female socket
models. This represents the intended removable assembly. Confirm the final
socket and male-header mating dimensions before ordering; nominally equivalent
parts can have different insertion depth, tail length and contact geometry.

The remaining project models are dimensional envelopes generated from the
manufacturer geometry documented in the related footprint notes. Regenerate
them with FreeCAD 1.1:

```powershell
& 'C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe' '.\tools\generate_3d_models.py'
```

After replacing placed footprints from the library, reattach the local models
with KiCad's bundled Python:

```powershell
& 'C:\Program Files\KiCad\10.0\bin\python.exe' '.\tools\attach_3d_models.py'
```

The checked renders are [socket-side isometric](pcb-3d-sockets.png),
[opposite-side isometric](pcb-3d-sockets-opposite.png) and
[top view](pcb-3d-top.png).
They verify placement and coarse enclosure envelopes, not undocumented internal
features, tolerances, wire-bend space or removal access.
