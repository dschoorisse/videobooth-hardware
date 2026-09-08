# Schematic reference mapping

The imported descriptive references were replaced with conventional numbered KiCad references. Symbol UUIDs, pin numbers, and connections were preserved. Each renamed symbol retains its old reference in the hidden `Previous Reference` field. Connector roles remain visible in `Value`, with the catalog model retained in `Model` and manufacturer fields.

| Previous reference | Reference | Function | Sheet |
|---|---|---|---|
| `FUSE_LIGHT_PRINTER` | `F3` | Printer lighting fuse | `1_P1.kicad_sch` |
| `FUSE_PSU` | `F1` | Main supply fuse | `1_P1.kicad_sch` |
| `FUSE_LIGHT_TRUSS` | `F4` | Down lighting fuse | `1_P1.kicad_sch` |
| `CON_LIGHT_FRONT` | `J3` | Front lighting | `1_P1.kicad_sch` |
| `CON_LIGHT_PRINTER` | `J4` | Printer lighting | `1_P1.kicad_sch` |
| `CON_CMD_BTN` | `J2` | Command button | `1_P1.kicad_sch` |
| `FUSE_LIGHT_FRONT` | `F2` | Front lighting fuse | `1_P1.kicad_sch` |
| `PWR_LED` | `D1` | Power indicator | `1_P1.kicad_sch` |
| `CON_PSU` | `J1` | 5 V supply | `1_P1.kicad_sch` |
| `CON_LIGHT_DOWN` | `J5` | Down lighting | `1_P1.kicad_sch` |
| `CON_DMX1` | `J6` | DMX output | `2_P2.kicad_sch` |
| `P1` | `J7` | Camera power relay | `2_P2.kicad_sch` |
| `CAMERA_RESET_LED1` | `D3` | Camera relay indicator | `2_P2.kicad_sch` |

`D2` remains the relay flyback diode. `JP1` remains the removable external 5 V enable jumper.

Both schematic sheets use a 330.2 × 235 mm native page. Drawing coordinates were translated uniformly by +15.24 mm X and +12.70 mm Y; embedded symbol geometry and electrical connectivity were preserved. The GPIO0 and external camera-supply notes were repositioned for readability.
