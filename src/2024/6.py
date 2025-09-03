from api import get_input
from utils import grid_contains

input = get_input(2024, 6)


def parse_input(input: str):
    grid = [list(line) for line in input.splitlines()]
    start = (0, 0)

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "^":
                start = (x, y)

    return grid, start


# directions in right turn order
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def is_obstacle(grid: list[list[str]], position: tuple[int, int]):
    if not grid_contains(grid, position):
        return False

    return grid[position[1]][position[0]] == "#"


class LoopException(Exception):
    pass


def get_visited_cells(grid: list[list[str]], position: tuple[int, int]):
    visited: set[tuple[int, int]] = set()
    direction = (0, -1)

    previous_directions: set[tuple[tuple[int, int], tuple[int, int]]] = set()

    while grid_contains(grid, position):
        visited.add(position)

        if (position, direction) in previous_directions:
            raise LoopException()

        previous_directions.add((position, direction))

        while is_obstacle(
            grid, (position[0] + direction[0], position[1] + direction[1])
        ):
            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]

        position = (position[0] + direction[0], position[1] + direction[1])

    return visited


def part1():
    grid, position = parse_input(input)
    visited = get_visited_cells(grid, position)
    print(len(visited))


def part2():
    grid, position = parse_input(input)
    visited = get_visited_cells(grid, position)
    visited.remove(position)

    loops = 0
    for obstacle in visited:
        modified_grid = [[cell for cell in row] for row in grid]
        modified_grid[obstacle[1]][obstacle[0]] = "#"

        try:
            visited = get_visited_cells(modified_grid, position)
        except LoopException:
            loops += 1

    print(loops)
