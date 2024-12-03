from api import get_input
import re

input = get_input(2024, 3)


def part1():
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, input)

    print(sum([int(a) * int(b) for a, b in matches]))


def part2():
    pattern = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"

    matches = re.findall(pattern, input)

    enabled = True
    result = 0

    for match in matches:
        match match:
            case ("do()", _, _):
                enabled = True
            case ("don't()", _, _):
                enabled = False
            case (m, a, b):
                if enabled:
                    result += int(a) * int(b)

    print(result)
