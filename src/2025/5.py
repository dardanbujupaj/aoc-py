from api import get_input

input = get_input(2025, 5)

raw_ranges, raw_ingredients = input.split("\n\n")
ranges = [
    range(int(start), int(end) + 1)
    for start, end in [line.split("-") for line in raw_ranges.splitlines()]
]
ingredients = [int(ingredient) for ingredient in raw_ingredients.splitlines()]


def ranges_overlap(r1: range, r2: range) -> bool:
    return r1.start in r2 or r1.stop in r2 or r2.start in r1 or r2.stop in r1


def part1() -> None:
    print("part1")
    fresh = 0

    for ingredient in ingredients:
        for r in ranges:
            if ingredient in r:
                fresh += 1
                break

    print(fresh)


def part2() -> None:
    print("part2")

    normalized_ranges: list[range] = list()
    remaining_ranges = ranges.copy()

    while len(remaining_ranges) > 0:
        current = remaining_ranges.pop()

        for r in remaining_ranges:
            if ranges_overlap(current, r):
                combined = range(min(current.start, r.start), max(current.stop, r.stop))
                remaining_ranges.remove(r)
                remaining_ranges.append(combined)
                break
        else:
            normalized_ranges.append(current)

    print(sum(len(r) for r in normalized_ranges))
