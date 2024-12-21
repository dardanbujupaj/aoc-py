from functools import cache, lru_cache
from itertools import permutations
import math
from api import get_input

input = get_input(2024, 21)

example_input = """029A
980A
179A
456A
379A"""


numeric_keypad = {
    "0": (1, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "A": (2, 3),
}

directional_keypad = {
    "A": (2, 0),
    "^": (1, 0),
    ">": (2, 1),
    "v": (1, 1),
    "<": (0, 1),
}

direction_keys = {
    (1, 0): ">",
    (0, -1): "^",
    (0, 1): "v",
    (-1, 0): "<",
}


@cache
def move_possible(
    start: tuple[int, int], moves: tuple[tuple[int, int], ...], numeric: bool
):
    keypad = numeric_keypad if numeric else directional_keypad

    position = start

    for move in moves:
        position = position[0] + move[0], position[1] + move[1]

        if position not in keypad.values():
            return False

    return True


@cache
def get_keypad_input(output: str, level: int = 0, max_level: int = 2) -> str:
    keypad = numeric_keypad if level == 0 else directional_keypad

    input_length = 0
    position = keypad["A"]

    for char in output:
        target = keypad[char]
        offset = target[0] - position[0], target[1] - position[1]

        needed_directions = []

        for direction in direction_keys.keys():
            multiplier = direction[0] * offset[0] + direction[1] * offset[1]

            for _ in range(multiplier):
                needed_directions.append(direction)

        possible_paths = [
            [direction_keys[move] for move in possible_path]
            for possible_path in filter(
                lambda path: move_possible(position, path, level == 0),
                set(permutations(needed_directions)),
            )
        ]

        if level >= max_level:
            input_length += len("".join(possible_paths[0]) + "A")
        else:
            shortest_path = math.inf

            for path in possible_paths:
                path_input = get_keypad_input("".join(path) + "A", level + 1, max_level)
                if path_input < shortest_path:
                    shortest_path = path_input

            input_length += shortest_path

        position = target

    return input_length


def part1():
    print("part1")
    codes = input.splitlines()

    complexity = 0

    for code in codes:
        steps = get_keypad_input(code)
        value = int(code[0:3])

        complexity += steps * value

    print(complexity)


def part2():
    print("part2")

    codes = input.splitlines()

    complexity = 0

    for code in codes:
        steps = get_keypad_input(code, max_level=25)
        value = int(code[0:3])

        complexity += steps * value

    print(complexity)
