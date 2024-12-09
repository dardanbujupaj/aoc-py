from re import split
import numpy as np
from api import get_input

input = get_input(2024, 1)


def parse_input(input: str):
    return np.array(
        [[int(n) for n in split(r"\s+", line)] for line in input.splitlines()]
    )


def part1():
    numbers = np.sort(parse_input(input), axis=0)
    print(np.abs((numbers[:, 1] - numbers[:, 0])).sum())


def part2():
    numbers = parse_input(input)
    left = numbers[:, 0]
    right = numbers[:, 1]

    similarities = [
        current_left * np.argwhere(right == current_left).size for current_left in left
    ]
    print(sum(similarities))
