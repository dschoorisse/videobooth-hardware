# Compact vertical fuse holder

The selected mechanical option is **OptiFuse CNT-06**, a 15 A rated through-hole holder for the manufacturer's **ANT / APT MICRO2-style blade fuses**. Each fuse remains a separate purchased part; its current rating is **TBD**. The holder rating is not the fuse rating. Do not fit fuses over the holder's 15 A rating even though the compatible fuse families include larger values.

Primary sources, checked 8 September 2026:

- [CNT-06 manufacturer drawing, Rev C 09/2018](https://www.optifuse.com/optifuse_ecommerce_tools/datasheets/CNT-06.pdf): 15 A, 500 VAC holder rating; ANT and APT explicitly named as compatible; tin-plated brass contacts and 94V-0 thermoplastic.
- [ANT manufacturer drawing, Rev D 07/2024](https://www.optifuse.com/optifuse_ecommerce_tools/datasheets/ANT.pdf): 32 VDC fuse family, 1000 A interrupt rating at 32 VDC; available from 3 A. Ratings are selected from the time/current curves and actual load/inrush, not maximum system power alone.
- [APT manufacturer drawing, Rev C 03/2025](https://www.optifuse.com/optifuse_ecommerce_tools/datasheets/APT.pdf): 48 VDC fuse family, 1000 A interrupt rating at 48 VDC; available from 5 A.

Use ANT as the default family for this low-voltage design, with the exact suffix held open. Cross-brand MICRO2 interchangeability has not been verified. If a branch needs protection below 3 A, choose a different fuse family/holder for that branch rather than rounding its protection upward.

## Footprint and dimensions

`Photobooth:Fuseholder_OptiFuse_CNT-06_MICRO2` follows the manufacturer's mounting drawing. Coordinates below are a top-side PCB view with the two electrical terminals along Y=0 and the retention peg toward negative Y. The nonpolar holder has no manufacturer-assigned terminal numbers; project pads 1 and 2 preserve the two existing electrical connections.

| Feature | Implementation / drawing dimension |
|---|---|
| Molded body | 11.6 × 4.8 mm, X=-5.8…5.8; Y=-3.6…1.2 |
| Body height | 9.6 mm nominal, including the molded feet shown in the drawing |
| Terminal centers | Pad 1 at (-2.45, 0), pad 2 at (+2.45, 0): 4.9 mm pitch |
| Plated terminal slots | 2.0 × 0.6 mm, long axis along X, as recommended by manufacturer |
| Copper lands | 3.0 × 1.6 mm, giving 0.5 mm nominal annulus around slots |
| Terminal dimensions | 1.6 × 0.3 mm; 4.6 mm projection below body |
| Retention peg | 2.7 × 1.4 mm cross-section; 2.0 mm projection below body |
| Retention opening | 3.2 × 1.8 mm at (0, -2.7), **nonplated routed opening on Edge.Cuts** |
| Opening corner treatment | R0.5 mm for a standard 1.0 mm routing tool, a project fabrication choice; the manufacturer's drawing shows square corners |
| Courtyard | 12.6 × 5.8 mm, 0.5 mm beyond nominal body on each side |

The body placement uses the side-view 1.2 mm terminal-to-body-edge offset. The retention opening uses the mounting drawing's 2.7 mm center-to-center offset from the terminal row. Its rounded corners clear the nominal 2.7 × 1.4 mm rectangular peg. A simple 3.2 × 1.8 mm oval drill would remove too little material at the peg corners, so it is deliberately **not** used. No copper pad is assigned to the retention opening. Ensure PCB routing exports include the footprint's closed Edge.Cuts loop.

The R0.5 mm corners accommodate a standard 1.0 mm routing tool. For the opening centered at the origin, its upper-right corner center is (1.1, 0.4) mm and the nominal peg corner is (1.35, 0.7) mm. Their distance is 0.390512 mm, leaving **0.109488 mm nominal corner clearance** inside the 0.5 mm arc. The straight sides leave 0.25 mm and 0.20 mm clearance per side. The footprint retains the specified 3.2 × 1.8 mm opening dimensions and terminal-to-opening offset.

The hole sizes and placement come from the manufacturer's drawing; land sizes, courtyard, reference orientation, and routable corner treatment are project choices. [JLCPCB's published capabilities](https://jlcpcb.com/capabilities/pcb-capabilities) include 0.5 mm minimum plated slots and 1.0 mm minimum nonplated routed slots, so the 0.6 mm terminal slots and 1.0 mm routing tool use standard listed capabilities. This does not qualify the assembled fit: the holder drawing gives no peg tolerance, and routing tolerances can consume the nominal corner margin. Obtain a holder sample, confirm fabrication tolerances, and check a routed coupon before ordering production boards. Do not allow substitution with an oval NPTH hole of the same outer dimensions.

## Area, height, and assembly

The holder body occupies about **55.7 mm²**, versus 229.4 mm² for the documented 24.4 × 9.4 mm PTF-77 horizontal option: approximately **76% less body area**. The local footprints' courtyards are approximately 73.1 versus 271.4 mm², about **73% less courtyard area**. These are holder/assembly plan envelopes, not a comparison against a bare fuse. The ANT/APT fuse body fits within the holder's nominal 11.6 × 4.8 mm plan envelope.

The fuse drawing gives 15.3 mm total nominal height with 7.4 mm exposed blade length, leaving a 7.9 mm plastic body. If fully seated to its plastic shoulder at the holder top, the combined height is therefore approximately **17.5 mm above the PCB**. This is an estimate: neither source specifies the seated insertion depth or a combined maximum assembly height, and CNT-06 lacks a dimension tolerance table. **Maximum enclosure fit is not qualified from these drawings.** Check a real assembly and leave overhead access for a fuse puller; clearance merely equal to the installed height is insufficient for replacement.

Treat the holders as **manually fitted through-hole parts**, and insert the fuses after soldering. Current JLCPCB stock/Basic classification for CNT-06 has not been established; no automatic-assembly or zero-extra-fee claim is made. Confirm availability and assembly handling when requesting the fabrication quote.

A project-local STEP model reproduces the 11.6 × 4.8 × 9.6 mm holder body,
terminal positions/projection and retention peg. Its blade-entry slots are
representative because the manufacturer does not dimension the internal contact
shape. The separately purchased fuse is not included in this holder model.

The verified local `Fuseholder_XFCN_PTF-77_P22.50mm` remains a legacy mechanical alternative, documented in `remaining-component-footprints.md`. Its presence in the footprint library does not mean it is assigned to the current design.

## Release checks

The ANT time/current table was rechecked on 13 September 2026. It permits
110% rated current for at least 100 hours, up to 120 seconds at 135%, and up to
5 seconds at 200%. A 10 A fuse therefore does not make an 8 A current limiter.
Coordinate supply fault/current-limit behavior, wiring, copper and the selected
fuse curve; the 8 A design load alone is insufficient to finalize protection.
[ANT manufacturer data](https://www.optifuse.com/optifuse_ecommerce_tools/datasheets/ANT.pdf).

- Resolve the main and each branch fuse current from steady load, startup/inrush, wire ampacity, PCB copper, and the fuse time/current curve; all four `Fitted Fuse` values remain TBD until then.
- Confirm holder temperature rise/current derating for the actual enclosure and ambient. An 8 A total load does not itself select a fuse rating.
- Fit a CNT-06 and selected ANT/APT sample into a board coupon; verify plated slots, retention opening, solder access, seated height, and removal clearance.
- Check exported plated-slot drill data and the nonplated retention cutout in the board manufacturer's preview.
- Order the holder and the selected fuse as separate BOM items and document manual assembly.
