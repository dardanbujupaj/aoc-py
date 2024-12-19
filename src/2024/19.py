from functools import cache
from api import get_input

input = get_input(2024, 19)


def parse_input(input: str):
    towels_string, designs_string = input.strip().split("\n\n")

    towels = towels_string.split(", ")
    designs = designs_string.split("\n")

    return towels, designs


def count_possibilities(design: str, towels: list[str]):
    @cache
    def recursive_count_possibilities(design: str):
        possibilities = 0

        for towel in towels:
            if design == towel:
                possibilities += 1
            elif design.startswith(towel):
                possibilities += recursive_count_possibilities(design[len(towel) :])
            else:
                possibilities += 0

        return possibilities

    return recursive_count_possibilities(design)


def part1():
    print("part1")
    towels, designs = parse_input(input)

    possible_designs = list(
        filter(lambda design: count_possibilities(design, towels) > 0, designs)
    )
    print(len(possible_designs))


def part2():
    print("part2")
    towels, designs = parse_input(input)

    possible_designs = sum(
        map(lambda design: count_possibilities(design, towels), designs)
    )
    print(possible_designs)
