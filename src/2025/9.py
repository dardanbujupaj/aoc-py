from shapely import Polygon, box

from api import get_input

input = get_input(2025, 9)

Point = tuple[int, int]

parsed = [Point(map(int, line.split(","))) for line in input.splitlines()]


def part1() -> None:
    print("part1")
    surfaces = [
        abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)
        for offset, a in enumerate(parsed)
        for b in parsed[offset + 1 :]
    ]
    print(max(surfaces))


def part2() -> None:
    print("part2")
    poly = Polygon(parsed)

    surfaces = [
        (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        for offset, a in enumerate(parsed)
        for b in parsed[offset + 1 :]
        if poly.contains(box(a[0], a[1], b[0], b[1]))
    ]

    print(max(surfaces))
