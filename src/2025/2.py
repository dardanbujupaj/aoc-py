from math import ceil

from api import get_input

input = get_input(2025, 2)

Range = tuple[int, int]

ranges: list[Range] = [
    (int(r.split("-")[0]), int(r.split("-")[1])) for r in input.split(",")
]


def invalid_ids(id_range: Range, split=2) -> list[int]:
    invalid_ids = []
    (start, end) = id_range

    base: int

    start_str = str(start)

    if len(start_str) % split == 0:
        base = int(start_str[0 : len(start_str) // split])
    else:
        base = pow(10, int(len(start_str) / split))

    for i in range(base, ceil(end / pow(10, len(str(end)) // split))):
        id = 0
        for n in range(split):
            id += i * pow(10, len(str(i)) * n)

        if id < start:
            pass
        elif id > end:
            break
        else:
            invalid_ids.append(id)

    return invalid_ids


def part1() -> None:
    print("part1")

    ids: list[int] = []
    for r in ranges:
        ids.extend(invalid_ids(r))

    print(sum(ids))


def part2() -> None:
    print("part2")

    ids: set[int] = set()
    for r in ranges:
        _, end = r
        for i in range(2, len(str(end)) + 1):
            ids.update(invalid_ids(r, i))

    print(sum(ids))
