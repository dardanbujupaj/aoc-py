from api import get_input
from utils import grid_contains

input = get_input(2024, 10)


def parse_input(input: str):
    return [[int(character) for character in line] for line in input.splitlines()]


def part1():
    grid = parse_input(input)
    trailheads: list[tuple[int, int]] = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 0:
                trailheads.append((x, y))

    total = 0

    for trailhead in trailheads:
        count = 0
        queue = [trailhead]

        visited = set()

        while queue:
            x, y = queue.pop(0)
            cell = grid[y][x]

            visited.add((x, y))

            if cell == 9:
                count += 1

            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if not grid_contains(grid, (dx, dy)):
                    continue

                if (
                    (dx, dy) not in visited
                    and (dx, dy) not in queue
                    and grid[dy][dx] == cell + 1
                ):
                    queue.append((dx, dy))

        total += count

    print(total)


def part2():
    grid = parse_input(input)
    trailheads: list[tuple[int, int]] = []

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 0:
                trailheads.append((x, y))

    total = 0

    for trailhead in trailheads:
        count = 0
        queue = [trailhead]

        while queue:
            x, y = queue.pop(0)
            cell = grid[y][x]

            if cell == 9:
                count += 1

            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if not grid_contains(grid, (dx, dy)):
                    continue

                if grid[dy][dx] == cell + 1:
                    queue.append((dx, dy))

        total += count

    print(total)
