from math import ceil

from api import get_input

input = get_input(2025, 2)

# input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

Range = tuple[int, int]

ranges: list[Range] = [
    (int(r.split("-")[0]), int(r.split("-")[1])) for r in input.split(",")
]


def invalid_ids(id_range: Range) -> list[int]:
    invalid_ids = []
    (start, end) = id_range

    base: int

    start_str = str(start)

    if len(start_str) % 2 == 0:
        base = int(start_str[0 : len(start_str) // 2])
    else:
        base = pow(10, int(len(start_str) / 2))

    for i in range(base, ceil(end / pow(10, len(str(end)) // 2))):
        id = i + i * pow(10, len(str(i)))

        if (id < start):
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
