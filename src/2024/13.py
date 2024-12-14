import re
from dataclasses import dataclass

import numpy as np

from api import get_input

input = get_input(2024, 13)

example_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

pattern = ".*?(\\d+).*?(\\d+)"


@dataclass
class Configuration:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]


def parse_input(input: str):
    return list(map(parse_config, input.split("\n\n")))


def parse_config(config: str):
    lines = config.splitlines()
    button_a = tuple(map(int, re.match(pattern, lines[0]).groups()))
    button_b = tuple(map(int, re.match(pattern, lines[1]).groups()))
    prize = tuple(map(int, re.match(pattern, lines[2]).groups()))
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
