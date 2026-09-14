# Project footprint sources

## Olimex_ESP32-POE-ISO

Carrier footprint for the user's confirmed **ESP32-POE-ISO (98 mm board)**.
The carrier uses **two separate 1×10 female through-hole socket strips** at
2.54 mm pitch, so the module remains removable. Fit two matching downward-facing
1×10 male pin headers to the Olimex module if they are not already populated.
Header coordinates and mounting positions were checked against the official
[Rev N1 PCB](https://github.com/OLIMEX/ESP32-POE-ISO/blob/master/HARDWARE/ESP32-PoE-ISO-Rev.N1/ESP32-PoE-ISO_Rev_N1.kicad_pcb)
and the official
[revision J and newer mechanical drawing](https://github.com/OLIMEX/ESP32-POE-ISO/blob/master/HARDWARE/Dimensions/Revision%20J%20and%20newer/ESP32-POE-ISO-revision-J-dimensions.pdf).
The [Olimex product page](https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-ISO/open-source-hardware)
independently specifies 1 inch row spacing.

Coordinates are millimetres, viewed from above the module with the antenna at
the top. The footprint origin is EXT1 pin 1, which is U2 pin 1 (+5V).
The old EasyEDA footprint had 20.420 mm between rows. This footprint uses the
verified **25.400 mm** spacing and retains the schematic's pad numbering.

| Item | Geometry |
| --- | --- |
| U2 pads 1 through 10 | x = 0; y = 0 through 22.86 in 2.54 mm steps |
| U2 pads 20 through 11 | x = 25.4; y = 0 through 22.86 in 2.54 mm steps |
| Header plated holes | 1.0 mm drill; 1.8 mm copper diameter; pad 1 rectangular |
| Carrier connector | 2 × 1×10 female THT socket strip, 2.54 mm pitch |
| Module connector | 2 × 1×10 downward-facing male pin header, 2.54 mm pitch |
| Nominal socket body height used by 3D assembly | 8.50 mm above carrier PCB |
| PCB outline bounds | x = -1.29 through 26.71; y = -33.22 through 64.93 |
| PCB dimensions | 28.00 x 98.15 mm |
| Module mounting holes, diameter 2.2 mm | (1.27, -5.745), (24.13, -5.745), (6.35, 62.200) |

The module's own mounting holes are drawing guides on **Dwgs.User**, not
automatic holes in the carrier PCB. Choose carrier hole sizes, standoffs and
clearance for the actual fastening arrangement during PCB layout. They are not
electrical pads.

**F.Fab** and **Dwgs.User** show the module PCB perimeter, including its USB notch.
The perimeter is an assembly guide: its overhang must not print beyond the
carrier board edge on the silkscreen.
**Dwgs.User** shows antenna/module and RJ45 overhang, plus mounting guides.
For this stacked-carrier layout the large assembly envelope is intentionally kept
on `Dwgs.User` rather than `F.CrtYd`: C19/C20 and U12 are low-profile SMD parts
under the raised carrier, so a same-plane courtyard would report a false overlap.
The upper overhang allows for the larger module outline in that reference CAD:
U6 uses the selectable WROOM/WROVER module footprint named
`ESP32-WROVER_MODULE`, whose drawing bounds extend 6.386 mm above the PCB
(including the drawing stroke). The RJ45 body on F.Fab extends 8.143 mm below the
PCB. Both projections are also visible in the official J+ mechanical drawing.
Confirm the fitted ESP32 module variant, physical socket/header height, underside
component clearance, access to the USB connector, RJ45 plug/cable access and
antenna clearance during placement. No carrier copper keepout or connector
insertion envelope is implied by these drawing guides.

The non-isolated ESP32-POE has the same header pad geometry and connector pin
mapping in the official Rev M2 CAD, but an 80 mm body and a different lower
mounting hole. It must not use this ISO mechanical outline without review.

The footprint references the official Olimex
[`ESP32-PoE-ISO_Rev_L.step`](https://ftp.olimex.com/TEMP/ESP32-PoE-ISO-step-export/ESP32-PoE-ISO_Rev_L.step)
assembly export, stored locally in `Photobooth.3dshapes`. Its 28 × 98.15 mm
PCB is aligned to the verified footprint outline. The model is shown 8.5 mm
above the carrier as a representative socket height; replace that Z offset with
the selected socket/standoff stack before enclosure sign-off. Olimex explicitly
notes that individual component heights in this export were not fully checked,
so use the physical module for final clearance qualification.
