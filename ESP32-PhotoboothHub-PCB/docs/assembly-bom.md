# Purchasing BOM and assembly items

Reconciled 13 September 2026 against the native KiCad 10.0.0
`current-20260913.xml` netlist, exported at 19:26:37 from the current schematic.
This includes the C8/C9 100 nF bypass selection and the selected JP1 header/shunt.
Quantities are **per completed carrier assembly**, before purchasing spares or
assembly attrition. Grouping uses manufacturer part number, independent of the
schematic's display value: C8/C9/C10/C11/C12/C17 form the 100 nF group;
C19/C20 form the 1 µF group.

The schematic has **56 physical references: 40 fitted SMT, 14 fitted THT,
one fitted Olimex module assembly, and one DNP resistor**. The 55 fitted
references do not equal the final purchased-item count: U2 needs mating
connectors, F1–F4 need fuse cartridges, and JP1 needs a separate shunt.

Supplier codes below are recorded identifiers, not a current-stock guarantee.
`Not selected` means the exact MPN is known but a distributor/order code is not
recorded. The assembly quote must confirm sourcing, package orientation,
attrition and manual-part handling. No production purchasing release is implied.

## Fitted SMT components

All rows in this table are **SMT assembly**. Total: **40 pieces, 19 MPN groups**.

| Qty | References | Component | Manufacturer | Exact MPN | Supplier / code |
|---:|---|---|---|---|---|
| 4 | C7, C14, C15, C16 | 470 µF, 16 V, ±20%, aluminum electrolytic | Honor Elec | `RVT1C471M0810` | LCSC `C3341` |
| 2 | C19, C20 | 1 µF, 50 V, ±10%, X5R, 0603 | Samsung | `CL10A105KB8NNNC` | LCSC `C15849` |
| 6 | C8, C9, C10, C11, C12, C17 | 100 nF, 50 V, ±10%, X7R, 0603 | Yageo | `CC0603KRX7R9BB104` | LCSC `C14663` |
| 1 | C13 | 4.7 µF, 16 V, ±10%, X5R, 0603 | Samsung | `CL10A475KO8NNNC` | LCSC `C19666` |
| 1 | C18 | 10 µF, 25 V, ±10%, X5R, 0805 | Samsung | `CL21A106KAYNNNE` | LCSC `C15850` |
| 2 | D1, D3 | Red 0805 indicator LED | Nationstar / 国星光电 | `NCD0805R1` | LCSC `C84256` |
| 1 | D2 | Switching diode, SOD-123 | ST / 先科 (Semtech) | `1N4148W` | LCSC `C81598` |
| 1 | Q1 | NPN transistor, SOT-23 | CJ / 江苏长电/长晶 | `MMBT2222A 1P` | LCSC `C8512` |
| 1 | R6 | 470 Ω, ±1%, 0.1 W, 0603 | UNI-ROYAL | `0603WAF4700T5E` | LCSC `C23179` |
| 2 | R7, R8 | 680 Ω, ±1%, 0.1 W, 0603 | UNI-ROYAL | `0603WAF6800T5E` | LCSC `C23228` |
| 3 | R13, R27, R28 | 10 kΩ, ±1%, 0.1 W, 0603 | UNI-ROYAL | `0603WAF1002T5E` | LCSC `C25804` |
| 3 | R14, R15, R16 | 1 kΩ, ±1%, 0.1 W, 0603 | UNI-ROYAL | `0603WAF1001T5E` | LCSC `C21190` |
| 6 | R17, R18, R19, R20, R21, R22 | 100 Ω, ±1%, 0.1 W, 0603 | UNI-ROYAL | `0603WAF1000T5E` | LCSC `C22775` |
| 1 | R26 | 360 Ω, ±1%, 0.1 W, 0603 | UNI-ROYAL | `0603WAF3600T5E` | LCSC `C25194` |
| 1 | U4 | 5 V RS-485 transceiver, SOIC-8 | Texas Instruments | `THVD1500DR` | Not selected |
| 1 | U7 | High-speed optocoupler, SMDIP-8 | UMW | `6N137S` | LCSC `C5123515` |
| 2 | U9, U10 | Quad AHCT buffer, SOIC-14 | Texas Instruments | `SN74AHCT125DR` | LCSC `C155176` |
| 1 | U11 | Open-drain buffer, SOT-23-5 | Texas Instruments | `SN74LVC1G07DBVR` | Not selected |
| 1 | U12 | Ideal diode, SOT-23-5 | Analog Devices | `MAX40200AUK+T` | Not selected |

D1/D3 use the project footprint's **pad 1 anode / pad 2 cathode** convention;
check placement polarity against that footprint. D2's supplier branding must
not be interpreted as STMicroelectronics. Preserve the exact U12 `+T` ordering
suffix and other recorded package suffixes when placing an order.

The four C3341 electrolytics are standard catalog SMT parts but were verified
as **JLCPCB Extended**, so additional loading fees may apply. Other recorded
LCSC codes do not imply Basic classification, current stock, or automatic
availability at PCBWay/Aisler. Component sources and dimensions are in
[remaining-component-footprints.md](remaining-component-footprints.md).

## Fitted through-hole components and module

The first seven rows total **14 THT pieces**. U2 is a separate assembled module,
installed after carrier soldering; its two carrier sockets are additional
purchased items in the accessory table.

| Qty | References | Component | Manufacturer | Exact MPN | Supplier / code | Assembly |
|---:|---|---|---|---|---|---|
| 4 | F1, F2, F3, F4 | Vertical MICRO2-style **holder only**, 15 A holder rating | OptiFuse | `CNT-06` | OptiFuse `CNT-06` | Manual THT; insert separate fuse afterward |
| 3 | J1, J2, J7 | 2-pole vertical spring terminal | Phoenix Contact | `1990850` — SPT 1,5/2-V-3,5 | Phoenix Contact `1990850` | THT |
| 1 | J6 | 3-pole vertical spring terminal | Phoenix Contact | `1990863` — SPT 1,5/3-V-3,5 | Phoenix Contact `1990863` | THT |
| 3 | J3, J4, J5 | 4-pole vertical spring terminal | Phoenix Contact | `1990876` — SPT 1,5/4-V-3,5 | Phoenix Contact `1990876` | THT |
| 1 | JP1 | 1×2, 2.54 mm vertical header; shunt separate | Harwin | `M20-9990246` | Distributor not selected | THT |
| 1 | K3 | 5 V SPDT relay | QLRELAY | `BRD-SS-105L` | LCSC `C22384955` | THT |
| 1 | U3 | Regulated isolated 5 V / 200 mA converter | TRACO POWER | `TMR 1-0511` | LCSC `C7362907` | THT SIP |
| 1 | U2 | 98 mm ESP32 module board | Olimex | `ESP32-POE-ISO` | LCSC `C19104183` | Module installation; mating hardware separate |

The `CNT-06` supplier entry is the manufacturer's order identifier, not an
LCSC code. The same applies to Phoenix order numbers. Manufacturer availability
and through-hole assembly must be confirmed with the chosen supplier/assembler.

## Do not populate

| Fitted qty | References | Component | Manufacturer | Exact MPN | Supplier / code | Assembly |
|---:|---|---|---|---|---|---|
| 0 | R9 | 120 Ω, ±1%, 0.1 W, 0603; optional DMX termination | UNI-ROYAL | `0603WAF1200T5E` | LCSC `C22787` | **DNP**; one PCB position exists |

Do not let a generic exporter turn R9 into a fitted purchasing quantity of one.
Its PCB pads remain available for an explicitly chosen termination configuration.

## Additional purchased items

These lines supplement the schematic BOM; they do not add electrical references
or duplicate the header/holder/module already counted above.

| Qty per assembly | Associated reference | Item / proposed MPN | Selection and assembly status |
|---:|---|---|---|
| 1 | JP1 | Harwin **`M7566-46`** red removable shunt | Selected matching accessory; purchase separately from JP1 header. Distributor code not selected. |
| 1 | F1 | OptiFuse ANT/APT main-supply fuse, exact suffix **TBD** | Select current/time-current behavior from load, inrush, wiring and copper. CNT-06 is only the holder. |
| 1 | F2 | OptiFuse ANT/APT front-light fuse, exact suffix **TBD** | Branch load/inrush not yet specified. |
| 1 | F3 | OptiFuse ANT/APT printer-light fuse, exact suffix **TBD** | Branch load/inrush not yet specified. |
| 1 | F4 | OptiFuse ANT/APT down-light fuse, exact suffix **TBD** | Branch load/inrush not yet specified. |
| 2 | U2 carrier connection | 1×10 female THT socket strips, 2.54 mm pitch, nominal 8.5 mm body height; MPN **TBD** | Intended removable mounting. Rows are 25.40 mm apart. Select pin acceptance, insertion depth, tail geometry and plating together with the module headers. Solder these sockets to the carrier. |
| 0 or 2 | U2 module connection | 1×10 downward-facing male headers, 2.54 mm pitch; MPN **TBD** | Inspect the actual Olimex module: buy two only if suitable headers are not already fitted. Solder to the module if required; do not solder the module directly to the carrier. |
| TBD | U2 mounting guides | Module standoffs, screws and related hardware | Select after socket stack height and fastening arrangement are fixed; do not infer a fastener kit from the drawing guides alone. |
| TBD | Carrier mounting | Enclosure/DIN mounting hardware and carrier fasteners | Board mounting arrangement and enclosure not finalized. No screw length or spacer height selected. |
| 1 | Carrier | Fabricated bare PCB | Supply approved layout/stackup and fabrication files when ready; artwork is not a purchased schematic component. |

Fuses are **not yet orderable as final selections**. ANT starts at 3 A and APT
at 5 A; a branch requiring a smaller protection rating needs another fuse family
and possibly another holder. Do not round a required protective rating upward
to fit the chosen package. See [compact-fuses.md](compact-fuses.md).

The Olimex footprint represents the complete module envelope and the two carrier
header rows. A placement/BOM exporter must not instruct an assembler to solder
the Olimex module as one ordinary 20-pin component. The official reference CAD
uses `NS(HN1x10)` for EXT1/EXT2; this is reason to inspect the delivered module,
not proof that a particular purchased unit includes fitted headers. Socket
height, module underside clearance, Ethernet-right placement and fastening remain
mechanical layout decisions. See [FOOTPRINTS.md](../FOOTPRINTS.md) and the
[Olimex product specification](https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-ISO/open-source-hardware).

Phoenix terminals take stripped wire directly, so no mating cable plugs are
required. The user specified bare stranded wire without ferrules. External
PSU, button, lighting, camera supply, DMX cable/interface and enclosure wiring
belong to the system assembly list; their exact products are not selected by
this carrier BOM. The external DIN rail camera converter is outside this work.

## JP1 checked header and shunt

Selected header **Harwin M20-9990246** has two tin-plated 0.64 mm square posts
at 2.54 mm pitch, 3.0 mm solder tails and 6.1 mm mating length. The manufacturer
lists a 3 A maximum contact rating and 8.64 mm nominal height above the PCB.
The existing `PinHeader_1x02_P2.54mm_Vertical` footprint has 2.54 mm pitch and
1.00 mm nominal holes. Harwin recommends **1.02 ±0.05 mm finished holes**;
1.00 mm falls within that interval, but specify/verify the resulting
**0.97–1.07 mm finished-hole range** with the board fabricator.
[Header product](https://www.harwin.com/products/M20-9990246),
[M20-999 manufacturer drawing](https://content.harwin.com/asset/640f59f4-1860-40fe-82ef-f2a104ffa7d8/DRG-00479-Technical-Drawing-Datasheet-M20-999-pdf.pdf).

Selected shunt **Harwin M7566-46** has matching tin contacts for 0.64 mm square
posts at 2.54 mm pitch. Its open red body is 5.0 × 2.3 × 6.3 mm; the manufacturer
specifies 3 A at 25 °C and 50 mating operations. The header/shunt drawings were
visually checked for pitch, pin size, mating length and finish. This is the
controller feed downstream of U12, not the 8 A lighting path. Leave access
to remove it; it is not a power switch or an unlimited-cycle service connector.
[Shunt product](https://www.harwin.com/products/M7566-46),
[M7565–M7571 manufacturer drawing](https://content.harwin.com/asset/d9daf8e1-20bf-4188-93ed-5f35af5e78e6/DRG-00743-Technical-Drawing-Datasheet-M7565-M7571-pdf.pdf).

Fit the shunt for external 5 V controller power. **Remove JP1 before connecting
powered USB**, and remove it for PoE-only controller power. Follow the power
instructions in [REVIEW.md](../REVIEW.md). No JLCPCB Basic classification or
distributor stock claim has been made for this header/shunt pair.

## Before a fabrication/assembly purchase

- Resolve the four fuse cartridge MPNs and module mating/mechanical hardware.
- Choose supplier order codes for U4, U11, U12 and the Harwin parts; recheck all stock and assembly fees at quotation time.
- Separate 40 fitted SMT placements from THT/manual assembly, module installation and accessory insertion; keep R9 DNP.
- Review polarity/orientation, JP1 finished-hole tolerance, CNT-06 plated slots and routed retention openings in manufacturing output.
- Check physical module socket height, Ethernet/USB access, antenna clearance, fuse extraction access and vertical terminal wire/tool access.
- Re-export the native netlist after schematic changes and reconcile every fitted reference, DNP flag, quantity and MPN against this document before release.
