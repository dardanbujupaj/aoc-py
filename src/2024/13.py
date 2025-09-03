import re
from dataclasses import dataclass

import numpy as np

from api import get_input

input = get_input(2024, 13)


pattern = ".*?(\\d+).*?(\\d+)"


@dataclass
class Configuration:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]


def parse_input(input: str):
    return list(map(parse_config, input.split("\n\n")))


def parse_line(line: str) -> tuple[int, int]:
    match = re.match(pattern, line)

    if not match:
        raise Exception(f"invalid line: {line}")

    groups = match.groups()
    left = int(groups[0])
    right = int(groups[1])
    return (left, right)


def parse_config(config: str):
    lines = config.splitlines()

    button_a = parse_line(lines[0])
    button_b = parse_line(lines[1])
    prize = parse_line(lines[2])

    return Configuration(button_a, button_b, prize)


def is_possible(a: float, b: float):
    return round(a) == round(a, 2) and round(b) == round(b, 2)


def part1():
    print("part1")
    configs = parse_input(input)

    cost = 0

    for config in configs:
        A = np.array(
            [
                [config.button_a[0], config.button_b[0]],
                [config.button_a[1], config.button_b[1]],
            ]
        )
        b = np.array(config.prize)

        v = np.linalg.solve(A, b)

        a, b = v[0], v[1]

        if is_possible(a, b):
            cost += 3 * round(a) + round(b)

    print(cost)


def part2():
    print("part2")
    configs = parse_input(input)

    cost = 0

    for config in configs:
        A = np.array(
            [
                [config.button_a[0], config.button_b[0]],
                [config.button_a[1], config.button_b[1]],
            ]
        )
        b = np.array(config.prize) + 10000000000000

        v = np.linalg.solve(A, b)

        a, b = v[0], v[1]

        if is_possible(a, b):
            cost += 3 * round(a) + round(b)

    print(cost)
