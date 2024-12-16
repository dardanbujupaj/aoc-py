from api import get_input
from heapq import heappush, heappop

input = get_input(2024, 16)

example_input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


def parse_input(input: str):
    start = (0, 0)
    end = (0, 0)
    cells: set[tuple[int, int]] = set()

    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            if char != "#":
                cells.add((x, y))

            if char == "S":
                start = (x, y)
            if char == "E":
                end = (x, y)

    return start, end, cells


def find_path(
    start: tuple[int, int], end: tuple[int, int], cells: set[tuple[int, int]]
):
    unvisited: tuple[int, tuple[int, int], tuple[int, int], list[tuple[int, int]]] = []

    visited = set((start, (1, 0)))
    heappush(unvisited, (0, start, (1, 0), []))

    path_cells: set[tuple[int, int]] = set([end])

    solutions_score = None

    while True:
        score, cell, direction, path = heappop(unvisited)

        if solutions_score is not None and score > solutions_score:
            break

        if cell == end:
            solutions_score = score
            for path_cell in path:
                path_cells.add(path_cell)

        visited.add((cell, direction))

        x, y = cell

        forward = (x + direction[0], y + direction[1])

        if forward in cells and (forward, direction) not in visited:
            heappush(unvisited, (score + 1, forward, direction, path + [cell]))

        turns = [
            (-1 if direction[0] == 0 else 0, -1 if direction[1] == 0 else 0),
            (1 if direction[0] == 0 else 0, 1 if direction[1] == 0 else 0),
        ]

        for turn in turns:
            if (cell, turn) not in visited:
                heappush(unvisited, (score + 1000, cell, turn, path))

    return solutions_score, path_cells


def part1():
    print("part1")
    start, end, cells = parse_input(input)

    score, cells = find_path(start, end, cells)

    print(score)


def part2():
    print("part2")
    start, end, cells = parse_input(input)

    _, cells = find_path(start, end, cells)

    print(len(cells))
