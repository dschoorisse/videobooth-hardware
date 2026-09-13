# Remaining component footprints and sourcing

Footprints and supplier sources checked on 2026-09-08. Capacitor assignments
reconciled on 2026-09-13 against the native KiCad `current-20260913.xml` netlist
(KiCad 10.0.0, exported at 19:26:37); supplier availability was not rechecked.
Standard footprint names below refer to installed KiCad 10 libraries.

## Bulk SMD capacitors

Use **Honor Elec RVT1C471M0810**, JLC/LCSC **C3341**, for C7, C14, C15 and C16:
470 uF, +/-20%, 16 V, aluminum electrolytic SMD, -55 to +105 C, 2000 h at 105 C.
The manufacturer's table specifies 240 mA RMS ripple at 120 Hz/105 C. Keep 470 uF;
there is no demonstrated reason to reduce the bulk capacitance to obtain another assembly classification.

Use `Capacitor_SMD:CP_Elec_8x10.5`, pad 1 positive and pad 2 negative. The
manufacturer's nominal body is diameter 8 mm, height 10.2 mm (10.7 mm maximum),
with 8.3 mm square base, 9.1 mm outer terminal span, 3.1 mm inner terminal gap,
and 0.8-1.1 mm terminal width. The standard footprint's 4.4 x 2.5 mm lands at
x = +/-3.7 mm provide a 3.0 mm inner gap and cover those terminals. Its 3D model
is representative; use the selected part's 10.7 mm maximum height for enclosure clearance.

At the 2026-09-08 check, the JLCPCB product page marked this part **Extended**, and its public
component data reported `overseasStockCount = 13902` at the check. This is a
catalog SMT component, but it does not guarantee zero loading fees at JLCPCB,
PCBWay or Aisler. Recheck availability, handling and quote at ordering time.

Sources: [JLCPCB C3341](https://jlcpcb.com/partdetail/HonorElec-RVT1C471M0810/C3341),
[Honor RVT manufacturer datasheet, pp. 1-3](https://wmsc.lcsc.com/wmsc/upload/file/pdf/v2/lcsc/2304140030_Honor-Elec-RVT1C471M0810_C3341.pdf).

## Standard assignments

| Source components | Footprint | Mapping |
| --- | --- | --- |
| Existing 0603 resistors | `Resistor_SMD:R_0603_1608Metric` | 1/2 passive |
| C8-C13 | `Capacitor_SMD:C_0603_1608Metric` | 1/2 nonpolar |
| Both NCD0805R1 LEDs | `Photobooth:LED_0805_2012Metric_A1K2` | 1 anode, 2 cathode |
| D2, Semtech 1N4148W C81598 | `Diode_SMD:D_SOD-123` | 1 cathode, 2 anode |
| Q1, CJ MMBT2222A 1P C8512 | `Package_TO_SOT_SMD:SOT-23` | 1 base, 2 emitter, 3 collector |
| U9/U10, TI SN74AHCT125DR | `Package_SO:SOIC-14_3.9x8.7mm_P1.27mm` | Numbering unchanged |

The imported NCD0805R1 symbol has pad 1 anode and pad 2 cathode, opposite the
standard KiCad LED footprint. The project-local LED footprint derives from
KiCad 10 `LED_0805_2012Metric` with pad numbers swapped; its geometry and cathode
mark stay unchanged, preserving source symbol numbering and wiring.

D2's old axial DO-35 assignment is wrong; its supplier part is SOD-123.
Q1's source device metadata and symbol agree on the standard SOT-23 pinout.
[Current D2 listing](https://jlcpcb.com/partdetail/C81598),
[current Q1 listing](https://jlcpcb.com/partdetail/C8512),
[TI AHCT125 datasheet](https://www.ti.com/lit/ds/symlink/sn74ahct125.pdf).

## XFCN PTF-77 fuse holder (legacy alternative)

This footprint is retained as a documented alternative. F1-F4 currently use the
[OptiFuse CNT-06 vertical holder](compact-fuses.md).

Local footprint: `Photobooth:Fuseholder_XFCN_PTF-77_P22.50mm`.
The manufacturer Rev A2 drawing supersedes the source's 22.6 mm pad spacing:
use 22.50 mm pitch and two 1.60 mm plated holes. Body 24.4 x 9.4 mm,
11.6 mm installed height, 3.4 mm pin length. Local copper lands are 3.0 mm,
and courtyard allows 0.5 mm beyond maximum body tolerance. Clearance for
removing the cover/fuse must be added during placement.

The drawing lists UL 20 A and VDE 6.3 A/1.6 W ratings; the old supplier field's
unqualified 10 A is not the full rating information. No fuse current is selected
by this footprint. Confirm holder approvals, thermal limits and selected fuse
for the actual 8 A input and each branch before manufacture.

[XFCN PTF-77 Rev A2 drawing](https://atta.szlcsc.com/upload/public/pdf/source/20241204/2C5BCE3FA349D3ADCF55CB0838B92C4A.pdf).

## QLRELAY BRD-SS-105L

Local footprint: `Photobooth:Relay_SPDT_QLRELAY_BRD-SS-105L`.
Manufacturer 1C pattern: contact-to-coil column 12.2 mm; coil-to-common column
2.0 mm; top/bottom rows 12.0 mm apart; contact holes 1.3 mm; coil holes 1.0 mm.
Body 19.0 x 15.4 mm, height 15.5 mm. The manufacturer's pattern is a **bottom
view**; the footprint is mirrored vertically into a top view. Body position
and schematic pad numbers follow the source device convention. The manufacturer
drawing does not assign numbers.

| Pad | Function | Top-view x, y (mm) |
| --- | --- | --- |
| 1 | NO | -7.1, -6.0 |
| 2 | NC | -7.1, +6.0 |
| 3 | Coil | +5.1, -6.0 |
| 4 | Coil | +5.1, +6.0 |
| 5 | Common | +7.1, 0 |

The original EasyEDA footprint had one coil pad displaced by 0.127 mm from the
other. Both coil pads now align on the manufacturer's 12.2 mm column spacing.
Copper lands are 2.3 mm for contact pads and 1.8 mm for coil pads. Courtyard
includes 0.5 mm beyond the stated undimensioned +/-0.4 mm body tolerance.
No 3D model is referenced by either recovered footprint.

[QLRELAY manufacturer datasheet, p. 3](https://www.lcsc.com/datasheet/lcsc_datasheet_2407031731_QLRELAY-BRD-SS-105L_C22384955.pdf).

Both local footprints load with KiCad 10's pcbnew API, with pad positions,
numbering and drill sizes checked. KiCad CLI SVG export also succeeds.

## Additional passive selections

| Position | Manufacturer part | JLC/LCSC | Specification | Standard footprint |
| --- | --- | --- | --- | --- |
| R26 | UNI-ROYAL 0603WAF3600T5E | C25194 | 360 ohm, 1%, 0.1 W | `Resistor_SMD:R_0603_1608Metric` |
| R28 | UNI-ROYAL 0603WAF1002T5E | C25804 | 10 kohm, 1%, 0.1 W | `Resistor_SMD:R_0603_1608Metric` |
| C8/C9/C10/C11/C12/C17 | Yageo CC0603KRX7R9BB104 | C14663 | 100 nF, 50 V, X7R, 10% | `Capacitor_SMD:C_0603_1608Metric` |
| C18 | Samsung CL21A106KAYNNNE | C15850 | 10 uF, 25 V, X5R, 10% | `Capacitor_SMD:C_0805_2012Metric` |
| C19/C20 | Samsung CL10A105KB8NNNC | C15849 | 1 uF, 50 V, X5R, 10% | `Capacitor_SMD:C_0603_1608Metric` |

C8/C9 now use the same 100 nF Yageo part as C10-C12/C17: six fitted pieces.
C19/C20 retain the 1 uF Samsung part: two fitted pieces, with **X5R** dielectric.
All eight use the same 0603 footprint. R28 reuses R13/R27. The JLCPCB pages
retrieved on 2026-09-08 classified C15849/C15850 as Basic and C25194 as Extended. These are sourcing
observations, not a guarantee of order-time prices or fees. No capacitor change
removes the need to account for MLCC capacitance under operating DC bias.

Sources: [R26](https://jlcpcb.com/partdetail/25937-0603WAF3600T5E/C25194),
[C18](https://jlcpcb.com/partdetail/C15850),
[C19/C20](https://jlcpcb.com/partdetail/C15849).
