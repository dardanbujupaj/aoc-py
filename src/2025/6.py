from functools import reduce
from math import prod

from api import get_input

input = get_input(2025, 6)


def part1() -> None:
    print("part1")
    cells = [line.strip().split() for line in input.splitlines()]

    values = [list(map(int, row)) for row in cells[:-1]]
    operators = cells[-1:][0]

    total = 0
    for index, operator in enumerate(operators):
        result = reduce(
            lambda x, y: x * y if operator == "*" else x + y,
            [line[index] for line in values],
        )
        total += result

    print(total)


def part2() -> None:
    print("part2")

    total = 0
    cells = [list(line) for line in input.splitlines()]

    nums: list[int] = []
    operator = "+"
    for col in reversed(range(len(cells[0]))):
        if all(line[col] == " " for line in cells):
            continue

        nums.append(int("".join([line[col] for line in cells[:-1]]).strip()))

        operator = cells[-1][col]
        if operator != " ":
            print(operator, nums)
            total += sum(nums) if operator == "+" else prod(nums)
            nums = []

    print(total)
