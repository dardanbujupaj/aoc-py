import functools
from api import get_input

input = get_input(2024, 5)


def parse_input(input: str):
    rules_str, updates_str = input.split("\n\n")
    return set(rules_str.splitlines()), [
        line.split(",") for line in updates_str.splitlines()
    ]


rules, updates = parse_input(input)


def sort_fn(a: str, b: str):
    if (f"{a}|{b}") in rules:
        return -1
    elif (f"{b}|{a}") in rules:
        return 1
    else:
        return 0


def part1():
    count = 0

    for update in updates:
        sorted_update = sorted(update, key=functools.cmp_to_key(sort_fn))
        if sorted_update == update:
            count += int(update[(len(update) - 1) // 2])

    print(count)


def part2():
    count = 0

    for update in updates:
        sorted_update = sorted(update, key=functools.cmp_to_key(sort_fn))
        if sorted_update != update:
            count += int(sorted_update[(len(update) - 1) // 2])

    print(count)
