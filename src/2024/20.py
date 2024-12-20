from collections import deque
from api import get_input

input = get_input(2024, 20)


def parse_input(input: str):
    cells: set[tuple[int, int]] = set()
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (0, 0)

    for y, row in enumerate(input.split("\n")):
        for x, char in enumerate(row):
            if char == "#":
                continue
            elif char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)

            cells.add((x, y))

    return cells, start, end


def part1():
    print("part1")

    cells, start, end = parse_input(input)

    cheats = find_cheats(cells, start, end)

    cheat_count = sum(cheats.values())

    print(cheat_count)


def part2():
    print("part2")

    cells, start, end = parse_input(input)

    cheats = find_cheats(cells, start, end, 20, threshold=100)

    # for score, count in sorted(cheats.items(), key=lambda x: x[0] * 1000 - x[1]):
    #     print(f"- There are {count} cheats that save {score} picoseconds.")

    cheat_count = sum(cheats.values())

    print(cheat_count)


def find_cheats(
    cells: set[tuple[int, int]],
    start: tuple[int, int],
    end: tuple[int, int],
    max_duration=2,
    threshold=100,
):
    distances_from_start = get_distances(cells, start)
    distances_from_end = get_distances(cells, end)

    baseline = distances_from_start[end]

    # print(f"baseline: {baseline}")

    cheats: dict[int, int] = {}

    for cell, distance in distances_from_start.items():
        for y in range(-max_duration, max_duration + 1):
            for x in range(-max_duration, max_duration + 1):
                duration = abs(x) + abs(y)

                if not 1 < duration <= max_duration:
                    continue

                # print(f"checking {cell} with distance {distance} and direction {direction}")

                target = (cell[0] + x, cell[1] + y)

                if target not in distances_from_end:
                    continue

                target_score = distances_from_end[target]

                saved_time = baseline - (target_score + distance + duration)

                if saved_time >= threshold:
                    cheats[saved_time] = cheats.get(saved_time, 0) + 1

                    # print(f"found cheat that saves {saved_time} picoseconds")

    return cheats


def get_distances(cells: set[tuple[int, int]], start: tuple[int, int]):
    queue: deque[tuple[int, tuple[int, int]]] = deque()
    queue.append((0, start))

    distances: dict[tuple[int, int], int] = {}

    while queue:
        distance, cell = queue.popleft()

        if cell in distances:
            continue

        distances[cell] = distance

        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (cell[0] + direction[0], cell[1] + direction[1])

            if neighbor not in cells:
                continue

            queue.append((distance + 1, neighbor))

    return distances
