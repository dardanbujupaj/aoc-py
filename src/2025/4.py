from api import get_input
from utils import grid_contains, griderator

input = get_input(2025, 4)

# input = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

parsed = [list(line) for line in input.splitlines()]

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]



def is_free_space(x: int, y: int) -> bool:
    if not grid_contains(parsed, (x, y)):
        return True

    return parsed[x][y] == "."

def removable_rolls(map: list[list[str]]) -> set[tuple[int, int]]:
    removable: set[tuple[int, int]] = set()

    for x, y in griderator(len(parsed[0]), len(parsed)):
        if not parsed[x][y] == "@":
            continue

        blocked_neighbors = len(
            [
                neighbor
                for neighbor in NEIGHBORS
                if not is_free_space(x + neighbor[0], y + neighbor[1])
            ]
        )

        if blocked_neighbors < 4:
            removable.add((x, y))

    return removable


def part1() -> None:
    print("part1")

    print(len(removable_rolls(parsed)))



def part2() -> None:
    print("part2")
    total = 0
    map = parsed

    while True:
        removable = removable_rolls(map)

        if (len(removable) == 0):
            break

        total += len(removable)

        for x, y in removable:
            map[x][y] = "."


    print(total)
