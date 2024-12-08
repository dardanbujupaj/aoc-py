from dataclasses import dataclass
from api import get_input
from typing import Literal

input = get_input(2024, 7)


def split_equation(equation: str):
    left, right = equation.split(": ")
    return (int(left), list(map(int, right.split(" "))))


def parse_input(input: str):
    return [split_equation(line) for line in input.splitlines()]


def part1():
    equations = parse_input(input)

    count = 0

    for result, components in equations:
        for i in range(1 << len(components) - 1):
            actual_result = components[0]

            for j in range(len(components) - 1):
                if (1 << j) & i:
                    actual_result += components[j + 1]
                else:
                    actual_result *= components[j + 1]

            if actual_result == result:
                count += result
                break

    print(count)


def part2():
    equations = parse_input(input)

    count = 0

    for result, components in equations:
        if check_equation(result, components):
            count += result

    print(count)


def check_equation(result: int, components: list[int]):
    queue: list[tuple[int, int]] = [(0, components[0])]

    while len(queue) > 0:
        index, value = queue.pop(0)

        if value > result:
            continue

        if index + 1 < len(components):
            next = components[index + 1]

            queue.append((index + 1, value + next))
            queue.append((index + 1, value * next))
            queue.append((index + 1, int(str(value) + str(next))))
        elif value == result:
            return True

    return False
