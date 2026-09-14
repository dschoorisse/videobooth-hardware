"""One-off geometric compression of the post-installation lower PCB area."""

from __future__ import annotations

import argparse
from pathlib import Path

import pcbnew


MICRONS = 1_000_000
BOUNDARY_Y = 117 * MICRONS
ZONE_BOUNDARY_Y = 116.5 * MICRONS
DELTA_Y = -15 * MICRONS
USB_LEFT = 75 * MICRONS
USB_RIGHT = 92 * MICRONS
USB_TOP = 97 * MICRONS
USB_BOTTOM = 118 * MICRONS


def transform(point: pcbnew.VECTOR2I) -> pcbnew.VECTOR2I:
    y = point.y + DELTA_Y if point.y >= BOUNDARY_Y else point.y
    return pcbnew.VECTOR2I(point.x, y)


def transform_zone_point(point: pcbnew.VECTOR2I) -> pcbnew.VECTOR2I:
    y = point.y + DELTA_Y if point.y >= ZONE_BOUNDARY_Y else point.y
    return pcbnew.VECTOR2I(point.x, y)


def in_usb_access_box(item: pcbnew.PCB_SHAPE) -> bool:
    bbox = item.GetBoundingBox()
    return (
        bbox.GetLeft() >= USB_LEFT
        and bbox.GetRight() <= USB_RIGHT
        and bbox.GetTop() >= USB_TOP
        and bbox.GetBottom() <= USB_BOTTOM
    )


def transform_board(input_path: Path, output_path: Path, delta_mm: float = -15.0) -> None:
    global DELTA_Y
    DELTA_Y = round(delta_mm * MICRONS)
    board = pcbnew.LoadBoard(str(input_path))
    delta = pcbnew.VECTOR2I(0, DELTA_Y)
    zones = board.Zones()
    zone_count = len(zones)

    # Transform zone outlines before changing other board containers. Filled
    # polygons are stale after this operation and are rebuilt by KiCad DRC.
    for zone_index in range(zone_count):
        zone = zones[zone_index]
        outline = zone.Outline()
        for contour_index in range(outline.OutlineCount()):
            contour = outline.Outline(contour_index)
            for point_index in range(contour.PointCount()):
                contour.SetPoint(
                    point_index, transform_zone_point(contour.GetPoint(point_index))
                )
        zone.UnFill()
        zone.SetNeedRefill(True)

    for footprint in board.GetFootprints():
        if footprint.GetPosition().y >= BOUNDARY_Y:
            footprint.Move(delta)

    # Keep connections to the upper section attached by transforming each
    # endpoint independently at the compression boundary.
    for track in board.GetTracks():
        if isinstance(track, pcbnew.PCB_VIA):
            track.SetPosition(transform(track.GetPosition()))
        elif isinstance(track, pcbnew.PCB_TRACK):
            track.SetStart(transform(track.GetStart()))
            track.SetEnd(transform(track.GetEnd()))

    remove_text = {
        "USB cable access",
        "REMOVE JP1 FOR USB",
        "PhotoboothHub",
        "PROTOTYPE / 2 oz",
        "5 V / 8 A TOTAL MAX",
    }
    for drawing in list(board.GetDrawings()):
        if isinstance(drawing, pcbnew.PCB_TEXT):
            if drawing.GetText() in remove_text:
                board.Remove(drawing)
            elif drawing.GetPosition().y >= BOUNDARY_Y:
                drawing.Move(delta)
        elif isinstance(drawing, pcbnew.PCB_SHAPE):
            layer_name = board.GetLayerName(drawing.GetLayer())
            if layer_name == "User.Drawings" and in_usb_access_box(drawing):
                board.Remove(drawing)
            elif drawing.GetShape() == 0:
                drawing.SetStart(transform(drawing.GetStart()))
                drawing.SetEnd(transform(drawing.GetEnd()))
            elif drawing.GetShape() == 2:
                drawing.SetArcGeometry(
                    transform(drawing.GetStart()),
                    transform(drawing.GetArcMid()),
                    transform(drawing.GetEnd()),
                )

    board.Save(str(output_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pcb", type=Path)
    parser.add_argument("output_pcb", type=Path)
    parser.add_argument("--delta-mm", type=float, default=-15.0)
    args = parser.parse_args()
    transform_board(args.input_pcb, args.output_pcb, args.delta_mm)
