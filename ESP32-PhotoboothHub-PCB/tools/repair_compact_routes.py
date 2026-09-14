"""Repair the two route necks created by lower-block compression."""

from __future__ import annotations

import argparse
from pathlib import Path

import pcbnew


MICRONS = 1_000_000


def vec(x_mm: float, y_mm: float) -> pcbnew.VECTOR2I:
    return pcbnew.VECTOR2I(round(x_mm * MICRONS), round(y_mm * MICRONS))


def mm(value: int) -> float:
    return pcbnew.ToMM(value)


def same_point(point: pcbnew.VECTOR2I, xy: tuple[float, float], tol: float = 0.01) -> bool:
    return abs(mm(point.x) - xy[0]) <= tol and abs(mm(point.y) - xy[1]) <= tol


def is_segment_between(
    track: pcbnew.PCB_TRACK,
    net: str,
    layer: int,
    start: tuple[float, float],
    end: tuple[float, float],
) -> bool:
    if isinstance(track, pcbnew.PCB_VIA):
        return False
    if track.GetNetname() != net or track.GetLayer() != layer:
        return False
    return (
        (same_point(track.GetStart(), start) and same_point(track.GetEnd(), end))
        or (same_point(track.GetStart(), end) and same_point(track.GetEnd(), start))
    )


def remove_segment(
    board: pcbnew.BOARD,
    net: str,
    layer: int,
    start: tuple[float, float],
    end: tuple[float, float],
) -> pcbnew.PCB_TRACK:
    matches = [
        track
        for track in board.GetTracks()
        if is_segment_between(track, net, layer, start, end)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"expected one {net} segment {start}->{end}, found {len(matches)}")
    track = matches[0]
    board.Remove(track)
    return track


def add_segment(
    board: pcbnew.BOARD,
    net: str,
    layer: int,
    start: tuple[float, float],
    end: tuple[float, float],
    width: int,
) -> None:
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(vec(*start))
    track.SetEnd(vec(*end))
    track.SetWidth(width)
    track.SetLayer(layer)
    track.SetNet(board.FindNet(net))
    board.Add(track)


def add_via(
    board: pcbnew.BOARD,
    template: pcbnew.PCB_VIA,
    net: str,
    position: tuple[float, float],
) -> None:
    via = pcbnew.PCB_VIA(board)
    via.SetPosition(vec(*position))
    via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    via.SetWidth(pcbnew.F_Cu, template.GetWidth(pcbnew.F_Cu))
    via.SetWidth(pcbnew.B_Cu, template.GetWidth(pcbnew.B_Cu))
    via.SetDrill(template.GetDrill())
    via.SetNet(board.FindNet(net))
    board.Add(via)


def repair(input_path: Path, output_path: Path, delta_mm: float) -> None:
    board = pcbnew.LoadBoard(str(input_path))

    # The long +5 V B.Cu leg is taken around the compressed 3.3 V branch,
    # the JP1 via, and the low-profile LED vias.
    plus5 = remove_segment(
        board,
        "+5V",
        pcbnew.B_Cu,
        (52.5, 112.5),
        (61.4, 121.4 + delta_mm),
    )
    plus5_upper = remove_segment(
        board,
        "+5V",
        pcbnew.B_Cu,
        (61.4, 121.4 + delta_mm),
        (79.81, 121.4 + delta_mm),
    )
    plus5_width = plus5.GetWidth()
    add_segment(board, "+5V", pcbnew.B_Cu, (52.5, 112.5), (77.0, 112.5), plus5_width)
    add_segment(board, "+5V", pcbnew.B_Cu, (77.0, 112.5), (77.0, 105.0), plus5_width)
    add_segment(board, "+5V", pcbnew.B_Cu, (77.0, 105.0), (79.81, 105.0), plus5_upper.GetWidth())
    add_segment(board, "+5V", pcbnew.B_Cu, (79.81, 105.0), (79.81, 106.4), plus5_upper.GetWidth())

    # D3 is deliberately left a few millimetres lower than the rest of the
    # compressed block so its two pads clear the JP1 service-power route.
    d3 = next(footprint for footprint in board.GetFootprints() if footprint.GetReference() == "D3")
    old_d3_y = 122.0 + delta_mm
    d3_target_y = 110.0
    d3.Move(vec(0.0, d3_target_y - old_d3_y))
    d3_plus_via1_y = 123.1951 + delta_mm
    d3_plus_via2_y = 123.4343 + delta_mm
    d3_plus = remove_segment(
        board,
        "Net-(D3-+)",
        pcbnew.F_Cu,
        (64.938, d3_plus_via2_y),
        (64.938, old_d3_y),
    )
    d3_plus.SetStart(vec(64.938, d3_plus_via2_y))
    d3_plus.SetEnd(vec(64.938, d3_target_y))
    board.Add(d3_plus)
    d2_a = remove_segment(
        board,
        "Net-(D2-A)",
        pcbnew.F_Cu,
        (63.0625, 126.9625 + delta_mm),
        (63.0625, old_d3_y),
    )
    d2_a.SetStart(vec(63.0625, 126.9625 + delta_mm))
    d2_a.SetEnd(vec(63.0625, d3_target_y))
    board.Add(d2_a)

    # Put a small service-route notch around JP1 pad 2 instead of carrying
    # the compressed 3.3 V bus straight through its solder mask aperture.
    three3_y = 122.3455 + delta_mm
    three3 = remove_segment(
        board,
        "3.3V",
        pcbnew.B_Cu,
        (59.4613, three3_y),
        (41.674, three3_y),
    )
    three3_width = three3.GetWidth()
    add_segment(board, "3.3V", pcbnew.B_Cu, (59.4613, three3_y), (50.0, three3_y), three3_width)
    add_segment(board, "3.3V", pcbnew.B_Cu, (50.0, three3_y), (50.0, 109.0), three3_width)
    add_segment(board, "3.3V", pcbnew.B_Cu, (50.0, 109.0), (42.5, 109.0), three3_width)
    add_segment(board, "3.3V", pcbnew.B_Cu, (42.5, 109.0), (42.5, three3_y), three3_width)
    add_segment(board, "3.3V", pcbnew.B_Cu, (42.5, three3_y), (41.674, three3_y), three3_width)

    # The B.Cu high-current detour leaves a small isolated ground island at
    # the transformer module's GND pin.  A solid zone connection is robust
    # here and avoids creating a thermally starved island.
    u3 = next(footprint for footprint in board.GetFootprints() if footprint.GetReference() == "U3")
    u3_gnd = next(pad for pad in u3.Pads() if pad.GetNumber() == "1")
    u3_gnd.SetLocalZoneConnection(pcbnew.ZONE_CONNECTION_FULL)

    # The compressed reset branch no longer needs to run through the D3/D2
    # pads on F.Cu.  Drop to B.Cu at the existing vertical leg and return at
    # the lower join point of the unchanged route.
    reset_segments = [
        remove_segment(
            board,
            "CAMERA_RESET_RELAY",
            pcbnew.F_Cu,
            (69.3919, 114.0918),
            (62.141, 121.343 + delta_mm),
        ),
        remove_segment(
            board,
            "CAMERA_RESET_RELAY",
            pcbnew.F_Cu,
            (62.141, 121.343 + delta_mm),
            (62.141, 127.884 + delta_mm),
        ),
        remove_segment(
            board,
            "CAMERA_RESET_RELAY",
            pcbnew.F_Cu,
            (62.141, 127.884 + delta_mm),
            (66.08, 131.823 + delta_mm),
        ),
    ]
    reset_width = reset_segments[0].GetWidth()
    reset_via = next(
        track
        for track in board.GetTracks()
        if isinstance(track, pcbnew.PCB_VIA)
        and track.GetNetname() == "CAMERA_RESET_RELAY"
    )
    lower_join = (66.182, 131.823 + delta_mm)
    add_via(board, reset_via, "CAMERA_RESET_RELAY", (69.3919, 114.0918))
    add_via(board, reset_via, "CAMERA_RESET_RELAY", lower_join)
    add_segment(
        board,
        "CAMERA_RESET_RELAY",
        pcbnew.B_Cu,
        (69.3919, 114.0918),
        lower_join,
        reset_width,
    )

    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    board.Save(str(output_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pcb", type=Path)
    parser.add_argument("output_pcb", type=Path)
    parser.add_argument("--delta-mm", type=float, required=True)
    args = parser.parse_args()
    repair(args.input_pcb, args.output_pcb, args.delta_mm)
