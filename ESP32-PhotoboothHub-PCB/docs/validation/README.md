# Routing validation — 13 September 2026

KiCad 10.0.0 checked the saved project after the final zone refill.

| Check | Result |
|---|---|
| [PCB DRC](pcb-drc.json) | 0 violations, 0 unconnected items, 0 schematic-parity issues |
| [Schematic ERC](schematic-erc.json) | 0 errors, 0 warnings |
| Physical inventory | 56 schematic components, including DNP R9; four additional mounting holes |
| Routed copper | 391 track segments, 85 through vias, five copper zones |
| Manufacturing rules | Minimum track/ordinary clearance 0.25 mm; vias 0.9/0.3 mm; copper-to-edge 0.5 mm |
| Netlist comparison | All 59 nets and 185 electrical pin nodes match the placement checkpoint; only C8/C9 part metadata/value changed |
| Visual review | Final native assembly/copper renderings checked for placement, legends, polarity, service access and routed geometry |

Reports include their configured ignored checks. The existing ERC configuration
and board severity settings were preserved; no finding was excluded to obtain
these results. The isolation rule and added main-bus guard remain enabled.
[Input hashes](input-sha256.json) identify the checked native design files.

## Filled-copper review

- The front +5 V bus is **one filled polygon**, 622.22 mm². Cross-sections sampled
  every 0.01 mm along the F1-to-F4 feed span have a minimum width of **7.525 mm**.
  F1, all branch fuse feeds and the C7/controller spur are connected to it.
- The bottom primary GND zone is **one filled polygon**. Native polygon-membership
  checks confirm the Q1, U11, U9/U10 and C8/C9 ground vias connect to it. The two
  smaller front GND regions are stitched at (72, 134) and (72.5, 130.0669) mm;
  the smaller front DMX-GND region is stitched at (94.9, 122.05) mm.
- The six lighting outputs cross the bus on short back-layer bridges, totaling
  66.84 mm of back-layer track. Upper connector routes use the front layer.
- Native local copper polygons, with 0.002 mm conversion tolerance, give about
  **3.00 mm minimum primary-to-DMX separation** on both faces. The nearest pair
  is the ground-zone perimeter (3.0016 mm in the polygon calculation).
- J7.1→K3.2 (NC) and J7.2→K3.5 (common) each use four 2 mm segments per face.
  These contact nets remain separate from both ground systems.
- The final project tracks/vias and filled polygons were compared with the
  independently reviewed candidate and found geometrically identical.

The bus resistance integral is approximately **2.05 mΩ**, using 70 µm copper
and 20 °C resistivity of 1.724×10⁻⁸ Ωm. A resistor-sheet model of bottom GND alone
gave the following coarse return estimates; pad-contact boundary conditions
used both solder pins of each terminal pole:

| Return from J1 to | 0.5 mm mesh | 0.25 mm mesh |
|---|---:|---:|
| J3 | 0.531 mΩ | 0.537 mΩ |
| J4 | 0.787 mΩ | 0.819 mΩ |
| J5 | 1.041 mΩ | 1.154 mΩ |

The far return is approximately **1.1 mΩ**, or 8–9 mV at 8 A. Its roughly 10%
mesh variation is not a demonstrated error bound or a converged simulation.
These estimates exclude fuse/contact/cable resistance and heating, and do not
establish temperature rise, relay ratings or fuse-clearing behavior.

Two temporary witness boards separately checked the custom rules. The DMX
isolation witness detected all five deliberately invalid clearances. The bus
guard detected four foreign front-track/through-via intrusions while allowing
+5 V copper and back-layer signal tracks. Neither witness was merged into the
project.

## Reproduce the native checks

From the project directory, in PowerShell with KiCad 10 installed:

```powershell
$board = '.\ProPrj_New Project_2025-09-22_16-04-54_2026-09-08.kicad_pcb'
$schematic = [IO.Path]::ChangeExtension($board, '.kicad_sch')
& 'C:\Program Files\KiCad\10.0\bin\kicad-cli.exe' pcb drc --refill-zones --save-board --schematic-parity --format json --output '.\docs\validation\pcb-drc.json' $board
& 'C:\Program Files\KiCad\10.0\bin\kicad-cli.exe' sch erc --format json --output '.\docs\validation\schematic-erc.json' $schematic
```

Zone refill updates the PCB; save or close the editor first. After any design
change, rerun the checks and refresh the input hashes and previews. Remaining
physical, load and manufacturing qualification is listed in
[PCB layout review](../pcb-layout.md) and [schematic review](../../REVIEW.md).
