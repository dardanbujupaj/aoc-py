from functools import cache
from api import get_input

input = get_input(2024, 11)


def parse_input(input: str):
    return list(map(int, input.split(" ")))


def apply_rules(items: list[int]):
    output = []
    for item in items:
        if item == 0:
            output.append(1)
        elif len(str(item)) % 2 == 0:
            item_string = str(item)
            output += [
                int(item_string[: len(item_string) // 2]),
                int(item_string[len(item_string) // 2 :]),
            ]
        else:
            output.append(item * 2024)
    return output


def part1():
    print("part1")
    elements = parse_input(input)
    print(elements)

    for _ in range(25):
        elements = apply_rules(elements)
        print(elements[0], len(elements))
    print(len(elements))


@cache
def count_stones(item: int, blinks: int):
    descendants = apply_rules([item])

    if blinks > 1:
        return sum(map(lambda x: count_stones(x, blinks - 1), descendants))
    else:
        return len(descendants)


def part2():
    print("part2")
    elements = parse_input(input)
    print(sum(map(lambda x: count_stones(x, 75), elements)))
