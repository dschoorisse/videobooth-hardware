# Phoenix Contact SPT 1.5 vertical footprint sources

The selected **SPT 1,5/..-V-3,5** terminals have **90° wire entry perpendicular
to the PCB**. These replace the previously selected horizontal -H variants.
The spring clamp is opened with a screwdriver when inserting bare stranded
wire; ferrules are not required. Phoenix specifies flexible conductors from
0.2 to 1.5 mm², a 10 mm strip length, 17.5 A IEC nominal current and 10 A
cULus current. Current capability depends on temperature and conductor size.

| References | Poles | Part number | Manufacturer designation | Body width |
| --- | --- | --- | --- | --- |
| J1, J2, J7 | 2 | 1990850 | SPT 1,5/ 2-V-3,5 | 8.4 mm |
| J6 | 3 | 1990863 | SPT 1,5/ 3-V-3,5 | 11.9 mm |
| J3, J4, J5 | 4 | 1990876 | SPT 1,5/ 4-V-3,5 | 15.4 mm |

## Geometry and orientation

Checked on 2026-09-08 against the manufacturer's dimensioned/drilling drawing
in the 1990876 datasheet, page 5, and current Phoenix product specifications.
The family drawing applies across these pole counts; the catalog independently
confirms the three widths and order numbers.

- Terminal pitch is 3.5 mm. Each pole has **two solder pins 8.2 mm apart**;
  both pads carry the same electrical number.
- Body depth is **13.5 mm** and installed height is **14.4 mm**. Solder pins
  project 2.5 mm below the seating plane; overall height including pins is 16.9 mm.
- With `a = (pole count - 1) × 3.5 mm`, body width is `a + 4.9 mm`.
- Origin is the first pole's rear pad in the component-side view. Pad centers
  are `(3.5 × (pole - 1), 0)` and `(3.5 × (pole - 1), 8.2)` mm.
- The body extends from `x = -1.3` to `a + 3.6 mm`, and from `y = -2.75`
  to `10.75 mm`. The drawing's 2.75 mm body-edge offset locates the first row.
- Wire entry and clamp operation are from **above the PCB (+Z)**. The F.Fab
  label `TOP ENTRY` records this; it is not a dimensioned opening outline.
- The manufacturer drawing does not assign electrical pole numbers. This
  project numbers along +X and marks pole 1 with a rectangular rear pad and
  silkscreen triangle. Follow the schematic wire assignments.
- Finished plated holes are **1.2 mm**, per the current manufacturer specification.
  The 2012 drawing's older 1.1 mm recommendation is not used.
- Copper lands are 2.4 mm, a project choice. Courtyards extend 0.5 mm beyond
  the body. Allow additional overhead space for wire insertion, bending and
  screwdriver operation; that space is not represented by the planar courtyard.

The three footprints contain 4, 6 and 8 physical pads for 2, 3 and 4 poles.
The paired-pad positions are retained from the horizontal family, but body,
height and access information were corrected for the vertical parts. The old
horizontal footprints were removed from the project library. No 3D model is bundled.

## Primary sources

- [Phoenix 1990850 specifications](https://www.phoenixcontact.com/en-gb/products/pcb-terminal-block-spt-15-2-v-35-1990850): 90° entry, flexible wire range, current ratings, current drill and dimensions.
- [Phoenix 1990863 product](https://www.phoenixcontact.com/en-gb/products/pcb-terminal-block-spt-15-3-v-35-1990863).
- [Phoenix 1990876 specifications](https://www.phoenixcontact.com/en-gb/products/pcb-terminal-block-spt-15-4-v-35-1990876): independent 4-pole dimensions, pin spacing and current approvals.
- [Phoenix manufacturer drawing, distributor mirror](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/365/1990876.pdf): page 5 dimensioned/drilling views; page 1 instructions for stranded wire without ferrules.
- [Phoenix 2024 PCB connector catalog](https://www.phoenixcontact.com/assets/2018/interactive_ed/101_977104/epaper/CAT_8_2024_EN_LoRes.pdf): printed page 48, vertical SPT 1.5 family order numbers and widths.

Validation: KiCad footprint loading and geometry checks verify pad count,
numbering, pitch, row spacing, drills, body and courtyard dimensions. Native
netlist comparison confirms all circuit connections are unchanged by this swap.
