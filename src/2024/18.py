from collections import deque
from api import get_input

input = get_input(2024, 18)


def parse_input(input: str) -> list[tuple[int, int]]:
    return [tuple(map(int, line.split(","))) for line in input.splitlines()]


def find_path(size: int, corrupted_bytes: list[tuple[int, int]]):
    queue: deque[tuple[int, tuple[int, int]]] = deque()
    queue.append((0, (0, 0)))

    visited: set[tuple[int, int]] = set()

    while queue:
        step, (x, y) = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if (x, y) == (size - 1, size - 1):
            # for x in range(size):
            #     for y in range(size):
            #         if (x, y) in visited:
            #             print("0", end="")
            #         elif (x, y) in corrupted_bytes:
            #             print("#", end="")
            #         else:
            #             print(".", end="")
            #     print("")
            # print("")
            return step

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_x, next_y = x + dx, y + dy

            if (next_x, next_y) in corrupted_bytes:
                continue

            if (next_x, next_y) in visited:
                continue

            if 0 <= next_x < size and 0 <= next_y < size:
                queue.append((step + 1, (next_x, next_y)))

    raise Exception("No path found")


def part1():
    print("part1")
    corrupted_bytes = parse_input(input)

    print(find_path(71, corrupted_bytes[:1024]))


def part2():
    corrupted_bytes = parse_input(input)

    # binary search to find first blocking byte
    lower = 1024
    upper = len(corrupted_bytes)

    while True:
        if lower == upper:
            x, y = corrupted_bytes[lower - 1]
            print(f"{x},{y}")
            return

        mid = (lower + upper) // 2

        try:
            find_path(71, corrupted_bytes[:mid])
            lower = mid + 1
        except Exception:
            upper = mid
