# Schematic changes and release checks

Updated 2026-09-14 against imported baseline commit `b2cbc42` and placement checkpoint `ed387a4`.

The fixes are implemented. KiCad 10 ERC reports **zero errors and zero warnings**
with the existing rule configuration. All 56 physical component instances,
including DNP R9, have loadable footprints with matching electrical pad numbers.
The **116 × 113.5 mm PCB is fully routed**, with Ethernet on the right. Native PCB
DRC after filling and saving all zones reports **zero violations, zero unconnected
items and zero schematic-parity issues**. The layout and actual filled copper
have also been visually and independently reviewed. Prototype thermal testing,
mechanical fit and fuse qualification remain before production.

Design inputs: external 5 V supply, 40 W maximum total load (8 A at 5 V),
bare stranded 1.5 mm² wire without ferrules, and the 98 mm Olimex ESP32-POE-ISO.
The external DIN rail camera converter is outside this review.

## Implemented changes

| Area | Current implementation |
| --- | --- |
| Controller power | U12 MAX40200AUK+T ideal diode and removable JP1 shunt separate the module's 5 V rail from the lighting rail. |
| Controller 3.3 V | U2 pin 2 is correctly modeled as a power output and supplies the primary-side 3.3 V loads, including the new buffer. |
| DMX supply | U3 TRACO TMR 1-0511 provides regulated, isolated 5 V. |
| DMX transceiver | U4 TI THVD1500DR, SOIC-8, replaces the incorrectly supplied 3.3 V part. |
| Optocoupler drive | U11 SN74LVC1G07DBVR, R26 = 360 Ω, input pull-up and decoupling provide defined ON/OFF behavior. U7 enable is tied high. |
| Bulk capacitors | C7/C14/C15/C16 are 470 µF, 16 V SMD electrolytics, Honor Elec RVT1C471M0810 / C3341. |
| Buffer bypass | C8/C9 are 100 nF Yageo CC0603KRX7R9BB104 / C14663 in 0603, with short supply spurs and local ground vias. |
| Connectors | Seven Phoenix Contact SPT vertical wire-entry terminal blocks with verified project-local footprints. |
| Fuses | F1–F4 use compact vertical OptiFuse CNT-06 holders; actual fuse current ratings remain TBD. |
| Module footprint | Olimex header spacing, pin mapping, outline and mounting guides verified from manufacturer files. |
| Compact stacked placement | C19/C20 (0603) and U12 (SOT-23-5) moved under the raised U2 carrier; all SMDs remain on F.Cu and no SMD is placed on B.Cu. |
| Carrier compaction | USB service-access band removed for the confirmed pre-install USB flashing workflow; lower block compressed by 15 mm to a 116 × 113.5 mm carrier, with local +5 V/3.3 V/reset rerouting validated by DRC. |
| Import cleanup | Footprints, pin types, intentional NCs, references and overlapping drawing frames repaired. |

## Controller power and 3.3 V

The controller feed is now:

`J1 → F1 → primary +5 V → U12 ideal diode → JP1 → MCU_5V → U2 pin 1`

The lighting branches connect upstream of U12. Their maximum system load does
not flow through the ideal diode. U12 blocks the reverse path from the module
toward the primary rail, subject to its specified leakage and switching behavior.
C19/C20 are 1 µF local input/output capacitors.

A conventional series diode could provide reverse isolation, but its voltage
drop consumes more of the 5 V margin. MAX40200 provides a lower-drop alternative
on this low-current module feed. It is not a USB power-source selector.
[MAX40200 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX40200.pdf).

| Use | JP1 setting |
| --- | --- |
| Power the controller from external 5 V | Fit the shunt. |
| Power the controller only from PoE | Remove the shunt. External 5 V may still power lighting and DMX. |
| Connect powered USB for programming or operation | **Remove the shunt before connecting USB.** |

**Olimex prohibits simultaneous powered USB and external power through its
extension header.** The upstream diode does not remove that internal restriction;
JP1 provides manual disconnection. The PSU model/tolerance has not been confirmed.
The design requires **4.75–5.25 V at the primary board rail**, including cable
and fuse drops.

The Olimex 3.3 V pin is an output and powers the primary-side 3.3 V loads.
Do not use it for U4 or U7's output side: doing so would defeat DMX galvanic
isolation. The module's peripheral power allowance under PoE is far below the
40 W lighting load.
[Olimex manual, power and extension-header sections](https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-ISO/resources/ESP32-POE-user-manual.pdf).

The reviewed Olimex Rev L/M/N1 schematics have three 22 µF capacitors on the
module 5 V rail. Their conservative +20% total, plus C20, remains below the
MAX40200's 100 µF output-capacitance stability limit. The four 470 µF bulk
capacitors remain upstream. Recheck this if another module revision or additional
downstream bulk capacitance is fitted.

### What changes if the ideal diode is omitted?

Ideal-diode ICs are an established power-management approach: an internal
MOSFET and control circuit emulate one-way diode conduction with less voltage
loss. This circuit is useful because the module can be powered independently
of the external lighting supply.

- **Replace U12 with a wire, JP1 fitted:** external-only operation can work.
  If external 5 V disappears while PoE (or USB) powers the module, current can
  flow back into the lighting/DMX rail and the unpowered PSU output. Overload,
  rail collapse or repeated resets are possible; permanent damage is not assumed.
- **Leave the controller's external 5 V feed open:** the module requires PoE
  or USB, while the external supply powers lighting/DMX independently. This is
  a valid simpler architecture if external-supply controller operation is unnecessary.
- **Use a conventional Schottky diode:** reverse blocking remains possible,
  but its larger voltage drop must be checked against the module's input limits.

Olimex permits PoE together with external header power on the ISO module.
U12 protects this carrier's heavy-load rail against reverse feed; it does not
exist because that combination is universally prohibited. Powered USB plus
header power remains prohibited: remove JP1 first.
[Olimex technical-support clarification](https://www.olimex.com/forum/index.php?topic=9335.0).

The user confirmed retaining U12 on 2026-09-08. The external supply can power
the controller while PoE remains available as an independent source.

## Isolated DMX corrections

U4 is **TI THVD1500DR**, a 4.5–5.5 V, 500 kbps transceiver in the requested
surface-mount SOIC-8 package (`SOIC-8_3.9x4.9mm_P1.27mm`). Its receiver
output is intentionally unused; /RE and DE are high for a transmit-only output.
[TI datasheet](https://www.ti.com/lit/ds/symlink/thvd1500.pdf).

U3 is **TRACO TMR 1-0511**, a regulated 5 V / 200 mA isolated converter
with a 4.5–9 V input range and no minimum load requirement. This addresses
the original unregulated converter's light-load voltage uncertainty. It remains
a through-hole SIP part and costs more than the original converter.
[TRACO datasheet](https://www.tracopower.com/tmr1-datasheet).

U7 remains UMW 6N137S, with its correct SMDIP-8 footprint and enable tied to
isolated +5 V. U11 is a 3.3 V open-drain SN74LVC1G07 buffer: TX drives its
input; its output sinks the optocoupler LED current through R26. R28 holds
TX high while the controller pin is inactive. C17 decouples U11 and C18
adds 10 µF to the isolated supply.

For primary 4.75–5.25 V, MCU 3.3 V at least 3.0 V, and R26 = 360 Ω ±1%:

- Minimum LED current: `(4.75 − 1.8 − 0.4) / 363.6 = 7.01 mA`.
- Conservative maximum: `5.25 / 356.4 = 14.73 mA`.
- These bounds fit U7's recommended 6.3–15 mA ON range. U11's powered-off
  leakage is also below U7's guaranteed OFF-current limit.

Sources: [TI buffer](https://www.ti.com/lit/ds/symlink/sn74lvc1g07.pdf),
[UMW electrical characteristics](https://www.umw-ic.com/static/pdf/c1968ca39ec59a4c94f047020458d86b.pdf),
[UMW package drawing](https://www.umw-ic.com/static/pdf/8dd488e060a7a08c56c10ae434142a12.pdf).

R9, the local 120 Ω termination, is **DNP** by default. Terminate at the final
receiver in the intended controller-at-start daisy chain.
[TI DMX application guidance](https://e2e.ti.com/cfs-file/__key/telligent-evolution-components-attachments/00-138-01-00-01-20-65-60/DMX512-Application.pdf).

## SMD capacitors and assembly cost

C7/C14/C15/C16 retain **470 µF**. That capacitance is available in a normal
SMD aluminum-electrolytic package; reducing it just to obtain SMD is unnecessary.
The selected **Honor Elec RVT1C471M0810 / C3341** is 16 V, ±20%, 105 °C,
2000 h, with an 8 mm diameter body and 10.7 mm maximum height.
`Capacitor_SMD:CP_Elec_8x10.5` has pin 1 positive and pin 2 negative.

JLCPCB currently lists C3341 as **Extended**. It is a catalog component, but
that does not guarantee zero assembly loading fees. PCBWay and Aisler have
separate sourcing/pricing policies; obtain an actual assembly quote before
treating any selection as fee-free.
[JLCPCB C3341](https://jlcpcb.com/partdetail/HonorElec-RVT1C471M0810/C3341).

Its specified ripple rating is 240 mA RMS at 120 Hz / 105 °C. Check the real
lighting load's transient response and capacitor ripple heating on the prototype;
40 W total power alone does not establish those quantities.
[Manufacturer datasheet](https://wmsc.lcsc.com/wmsc/upload/file/pdf/v2/lcsc/2304140030_Honor-Elec-RVT1C471M0810_C3341.pdf).
Additional passive MPNs, catalog codes and footprint dimensions are in
[component sourcing](docs/remaining-component-footprints.md).

## Connectors, module and compact fuses

| References | Connection | Phoenix order number / designation |
| --- | --- | --- |
| J1, J2, J7 | PSU, command button, camera relay | 1990850 / SPT 1,5/2-V-3,5 |
| J6 | DMX | 1990863 / SPT 1,5/3-V-3,5 |
| J3, J4, J5 | Front, printer, down lighting | 1990876 / SPT 1,5/4-V-3,5 |

These **-V terminals have 90° wire entry, perpendicular to the PCB**. They
accept bare flexible 0.2–1.5 mm² wire. Open the clamp with
a screwdriver for stranded wire; strip 10 mm. Ratings are 17.5 A IEC / 10 A
cULus. Each pole has two PCB solder pins, both included in the local footprints.
Allow overhead wire and screwdriver access during placement. The installed
connector height is 14.4 mm, before allowing for wire bends and tool access.
[Phoenix specifications](https://www.phoenixcontact.com/en-gb/products/pcb-terminal-block-spt-15-4-v-35-1990876),
[footprint documentation](docs/phoenix-spt-footprints.md).

U2 uses `Photobooth:Olimex_ESP32-POE-ISO`, with **25.40 mm between header
rows**, replacing the imported 20.42 mm spacing. All 20 pads and the symbol/header
mapping were checked against Olimex's native PCB. The outline includes the USB
notch; mounting-hole guides support carrier standoff placement.
See [Olimex sources and dimensions](FOOTPRINTS.md).

F1–F4 use **OptiFuse CNT-06**, a 15 A rated vertical holder compatible with
OptiFuse ANT/APT MICRO2-style fuses. Its 11.6 × 4.8 mm body occupies about
**76% less plan area** than the previous horizontal holder. The holder rating
is not the fitted fuse rating: every `Fitted Fuse` field remains **TBD**.
ANT starts at 3 A; branches needing lower protection require another fuse family.

The holder needs plated slots and a separate routed retention opening, and is
intended for manual through-hole assembly. Nominal seated height is estimated
at 17.5 mm; maximum height and mating fit require a sample check. See
[compact-fuse dimensions, sources and checks](docs/compact-fuses.md).

## Import repair and verification

- Replaced missing imported footprint links with 19 loadable standard or
  project-local footprints. Corrected D2's SOD-123 package, Q1's SOT-23 mapping,
  U7's SMDIP package and K3's mirrored relay pattern.
- Preserved the imported LEDs' pin 1 anode / pin 2 cathode convention using
  a dedicated footprint; a standard KiCad LED assignment would reverse it.
- Corrected cached/library pin types, added intentional NCs, fixed the dangling
  relay stub, and provided appropriate supply power flags.
- Replaced descriptive connector/fuse/LED references with J/F/D references.
  Function labels and hidden `Previous Reference` fields preserve traceability:
  see [reference mapping](docs/ref-mapping.md).
- Removed duplicate drawing frames, annotated power symbols and separated
  overlapping labels. Corrected GPIO4's label typo.

Validation performed:

1. Native KiCad netlist export succeeds without annotation warnings.
2. Native KiCad ERC: **0 errors, 0 warnings**. The project's rule configuration
   was not changed to obtain this result.
3. Connectivity comparison preserves every baseline connection outside four
   deliberately rewired pins: U2.1, R26.1, U4.1 and U7.7. It accounts for reference
   changes and the replacement converter's pin numbering.
4. Separate assertions verify supply separation, JP1 and ideal-diode connections,
   optocoupler drive, transceiver A/B mapping, capacitor polarity, selected parts,
   DNP termination and intentional unused pins.
5. All **56 physical instances / 19 unique footprints** load in KiCad, with
   electrical pad numbers matching their symbols.
6. Exported drawings and new mechanical footprint geometry were visually checked.
7. Native PCB DRC after final zone refill: **0 violations, 0 unconnected items,
   0 schematic-parity issues**. Reports and reproduction commands are in
   [validation](docs/validation/README.md).
8. Actual filled copper has a continuous 5 V bus, short back-layer lighting
   crossings, broad ground return, explicit Q1/U11 ground connections, and
   separate primary/DMX ground regions. The custom bus guard was checked with
   deliberately invalid witness geometry. See [layout review](docs/pcb-layout.md).

The six lighting data/clock connections still match `PhotoboothHub.yaml`.
AHCT125 enables, unused inputs and supplies retain the reviewed wiring. The camera
reset relay retains its low-side transistor drive and flyback diode.

## Work required before production

- Select actual main and branch fuse ratings from branch currents, startup
  behavior, fuse curves, wiring and planned copper. Only total power is known.
- Confirm the PSU maintains 4.75–5.25 V at the board under load.
- Qualify the routed power paths at maximum load and ambient temperature. The
  continuous bus, dual-face input/output tracks, isolation spacing and local
  bypass layout are recorded in [PCB layout review](docs/pcb-layout.md), the
  [assembly preview](docs/pcb-placement.png) and [copper preview](docs/pcb-routing.png).
- Check K3's **NC-contact DC capability** against camera voltage, current and
  inrush. Its datasheet lists 7 A/250 VAC for NC; the 15 A headline is not a
  general DC-contact rating. The camera port uses 2 mm copper on both sides, but
  that does not qualify the relay. Verify coil pickup under low-supply/hot
  conditions; the specified maximum pickup threshold is 3.75 V at 23 °C.
  [Relay manufacturer datasheet](https://datasheet.lcsc.com/datasheet/pdf/3ac744019be974ff562e0a8cea7c80c4.pdf).
- Check Olimex sockets/standoffs, fuse slots/retention openings, enclosure height
  and tool access with physical samples and fabrication previews.
- Test startup, power-source transitions, lighting transients, DMX signaling and
  temperature rise on the prototype. Follow the JP1 USB instruction above.
- Confirm stock, assembly fees and manual-part handling in the fabrication quote.

The imported baseline is `b2cbc42`; verified schematic fixes and the decision
to retain the ideal diode were committed as `f0294b7`. The subsequent PCB
placement was committed as `ed387a4`. The routed board preserves its connectivity,
R9's DNP state and the selected JP1 header/shunt; C8/C9 were changed to 100 nF and
the purchasing BOM was reconciled. No fabrication output has been released.
