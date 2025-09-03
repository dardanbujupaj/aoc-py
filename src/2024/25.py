import numpy as np
from api import get_input

input = get_input(2024, 25)


def parse_pins(input: str) -> tuple[int, int, int, int, int]:
    layout = np.array(
        [[0 if char == "." else 1 for char in line] for line in input.splitlines()]
    )

    return layout.sum(axis=0) - 1


def parse_input(input: str):
    all_layouts = input.split("\n\n")

    locks = list(
        map(parse_pins, filter(lambda layout: layout.startswith("#####"), all_layouts))
    )
    keys = list(
        map(
            parse_pins,
            filter(lambda layout: not layout.startswith("#####"), all_layouts),
        )
    )

    return locks, keys


def part1():
    print("part1")
    locks, keys = parse_input(input)

    matches = 0
    for lock in locks:
        for key in keys:
            if np.all((lock + key) <= 5):
                matches += 1

    print(matches)


def part2():
    print("part2")
    print("⭐️")
