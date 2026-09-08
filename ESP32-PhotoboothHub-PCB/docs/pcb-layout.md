# Draft PCB layout constraints

**Draft placement only: the PCB is unrouted and is not ready for fabrication.**
These are initial layout assumptions, not evidence of current capacity, thermal performance, isolation certification or enclosure fit. Updated 8 September 2026.

![Top-side placement, Ethernet on the right](pcb-placement.png)

The board contains all 56 schematic components (R9 DNP) and four board-only
mounting holes. Native KiCad 10 DRC reports **0 placement violations,
0 schematic-parity issues, and 147 unconnected items**. Schematic ERC remains
**0 errors / 0 warnings**, with its verified rule configuration preserved.

## Board and fabrication assumptions

- Proposed carrier outline: **100 × 130 mm**, X=20…120 mm and Y=20…150 mm.
- Proposed M3 carrier-hole centres: (24, 24), (116, 24), (24, 146), (116, 146) mm. Verify screw, washer and standoff envelopes; keep mounting hardware clear of copper on both layers, especially the lower-right hole within the DMX island.
- Two copper layers, **1.6 mm FR-4**, **2 oz finished copper on both sides**; components on the top side. Keep the bottom mostly available for return copper.
  The initial stackup records 0.07 mm copper per side and a 1.44 mm core;
  confirm the fabricator's finished stackup before ordering.
- Initial ordinary routing: 0.25 mm signal width/clearance, 0.9/0.3 mm via
  diameter/drill, and 0.5 mm copper clearance from board edges and routed cutouts.
  Power and isolation constraints override these ordinary values.
- [JLCPCB capabilities](https://jlcpcb.com/capabilities/pcb-capabilities) list
  0.16 mm minimum width/spacing for two-layer 2 oz boards, 0.5 mm minimum plated
  slots and 1.0 mm minimum nonplated routed slots. Confirm the actual order options.
- Preserve the four fuse-holder retention openings as closed **Edge.Cuts** loops. Their R0.5 corners accommodate a 1 mm router; they are not oval drill holes.

The four M3 carrier holes are 3.2 mm NPTH. Both copper layers have hardware
keepouts: 4 mm radius at H1–H3 and 6.5 mm at H4. The complete hardware envelope,
including possible offset and positioning tolerance, must stay within 3.5 mm
of each hole centre. That leaves 3 mm to isolated copper at H4; a nominal
7 mm washer alone does not guarantee it. Confirm fastener dimensions and fit;
these holes are excluded from the
electrical BOM and placement-file output.

## Power distribution

The design input is **8 A maximum total from the external 5 V supply**. Place J1,
F1 and the distribution junction together, with short routes to the branch fuses
and output connectors. The main lighting current must not pass through U12 or U2.

- Reserve **8–10 mm wide copper paths** for the main feed and return. These are
  initial placement allowances; inspect every pad neck, thermal spoke and transition.
- As a resistance estimate, a 100 mm long, 8 mm wide, 70 µm thick copper path
  gives approximately 3.1 mΩ, 25 mV drop and 0.20 W at 8 A at room temperature.
  A similar return doubles the loop drop. This excludes copper tolerances, heating,
  fuse/contact resistance and local necks; it is **not a temperature-rise rating**.
- Prefer pours and short same-layer paths. Avoid carrying 8 A through one via or
  default narrow thermal spokes. If a layer change is necessary, reserve a broad
  via array and verify its finished plating and current distribution.
- Connect both solder pins of each Phoenix terminal pole with substantial copper. Keep lighting returns near their feeds and away from narrow MCU return paths.
  J1, the lighting power/return poles and F1–F4 already have solid zone-connection
  overrides; final pours and pad necks still require routing review.
- Put F2/F3/F4 and their bulk capacitors near J3/J4/J5 respectively. Final branch
  widths and actual fuse ratings depend on branch current, startup and fuse curves.
- Keep primary +5 V within the specified 4.75–5.25 V at the board under load.
  Place U12/C19/C20 on the separate controller feed and leave JP1 accessible.

## Isolated DMX region

The isolated DMX island occupies the lower-right region. Its proposed **L-shaped copper keepout** consists of a vertical strip **X=82.85…85.85, Y=116.5…150 mm** and a horizontal strip **X=82.85…120, Y=116.5…119.5 mm**, on both copper layers. U3 and U7 straddle the vertical boundary at X=84.35 mm, with primary connections on the left.

- Use **3.0 mm minimum primary-to-DMX copper separation** as the initial
  functional-isolation layout assumption. Keep the separation on every copper layer;
  no primary traces, vias, pours or mounting hardware may bridge into the island.
- Enforce 3 mm between the `DMX_Isolated` netclass and other connected nets; retain 0.25 mm ordinary clearance within the island. Empty-net NC pads retain ordinary clearance. The horizontal keepout closes the upper end so a pour cannot wrap around the vertical strip.
- Primary GND and DMX-GND are separate copper regions. Never pour primary ground
  beneath the isolated supply output, optocoupler output, U4 or J6.
- U3's native footprint has only **3.58 mm** between the closest input/output pad
  edges; U7 has **7.53 mm** between pad rows. The 3 mm assumption fits these parts;
  a greater specified insulation requirement would need another review.
- Group U4, its bypass capacitor, bias resistors and J6 within the isolated island.
  Route A/B adjacent on the same layer, short and without long stubs. Leave R9 DNP.

## Local decoupling and signal placement

| Components | Placement constraint |
|---|---|
| C10 / U7 | At U7 pins 8 and 5, entirely on the isolated side. |
| C11 / U4 | At U4 pins 8 and 5, with the shortest practical supply/return loop. |
| C12, C18 / U3 | Immediately beside the isolated output pins. |
| C13 / U3 | Immediately beside the primary input pins. |
| C17 / U11 | At U11 supply/ground; keep R26 and the optocoupler LED loop short. |
| C19, C20 / U12 | Beside input/output and ground pins on the controller feed. |
| U9/U10 bypass capacitors | At each device's supply pins; preserve nearby ground return. |

[TI's THVD1500 layout guidance](https://www.ti.com/lit/ds/symlink/thvd1500.pdf)
calls for local 100 nF bypassing and low-inductance supply/ground connections.
Use short ground connections and multiple vias when a bypass loop changes layers. If external transient protection is added later, place it at J6 in the signal path.

## Module and service access

U2 is rotated 90°, with origin (53.22, 96.71) mm: **antenna left, Ethernet right**.
The module PCB occupies **X=20…118.15, Y=70…98 mm**. Its antenna assembly extends left to **X=13.614 mm** and RJ45 body right to **X=126.293 mm**: the assembly spans approximately **112.7 mm**, before enclosure and cable clearances. These overhangs extend beyond the carrier outline.
[Espressif recommends](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/pcb-layout-design.html)
antenna overhang and at least 15 mm antenna clearance in the finished product.
Keep copper, components, cabling and enclosure metal away from the antenna region.

The board reserves a copper-free antenna rectangle at X=20…35 mm,
Y=59.46…108.56 mm on both layers. A second copper keepout under the module's
power/Ethernet end, X=78…119.5 mm and Y=69.5…99.5 mm, conservatively avoids
carrier copper below that area until socket/standoff separation is confirmed.
It is a project layout precaution, not a certified module insulation rating.

Reserve **X=76…91, Y=98…117 mm** for USB service access; confirm the actual plug and cable fit. Keep the right-hand RJ45 plug/latch approach accessible. The module hole marks are guides, not carrier holes. Select socket height and standoffs before
placing components underneath the module. Top-entry terminals need wire-bend and
screwdriver access; fuse holders need overhead clearance for removal, not merely
the estimated 17.5 mm installed height. Terminal installed height is 14.4 mm.

## Before fabrication

The custom isolation rule was also checked on a separate temporary witness
board with the same project settings: all four isolated-net patterns enforced
3 mm to primary copper, while internal isolated pairs accepted 0.25 mm.
All five deliberately introduced clearance violations were detected. This
checks the rule configuration, not the insulation performance of an assembly.

- Complete routing and zone fills; check connectivity, isolation clearances, all
  power-path necks and copper continuity, then run board DRC.
- Confirm branch currents/fuses, copper temperature rise, supply drop and startup
  behavior; test the assembled prototype at the maximum intended load.
- Check sockets, standoffs, antenna/connector access and enclosure dimensions with
  physical parts. Test a fuse-holder coupon for retention fit and routing tolerances.
- Inspect fabrication previews for every plated slot, routed opening and board edge.
  Confirm through-hole soldering access, assembly handling and part availability.

Related records: [assembly BOM](assembly-bom.md), [module footprint](../FOOTPRINTS.md),
[terminal footprints](phoenix-spt-footprints.md), [compact fuses](compact-fuses.md),
[remaining footprints](remaining-component-footprints.md), [schematic review](../REVIEW.md).
