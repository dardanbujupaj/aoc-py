from math import prod

from api import get_input

input = get_input(2025, 12)

parts = input.strip().split("\n\n")

Size = tuple[int, int]
Counts = tuple[int, int, int, int, int, int]

shapes = []
regions: list[tuple[Size, Counts]] = [
    (
        Size(map(int, region.split(": ")[0].split("x"))),
        Counts(map(int, region.split(": ")[1].split(" "))),
    )
    for region in parts[-1].split("\n")
]


def part1() -> None:
    print("part1")
    valid_regions = [
        region for region in regions if prod(region[0]) >= sum(region[1]) * 9
    ]
    print(len(valid_regions))


def part2() -> None:
    print("part2")
