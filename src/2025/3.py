from api import get_input

input = get_input(2025, 3)

# input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

parsed = [[int(digit) for digit in list(line)] for line in input.splitlines()]


def part1() -> None:
    print("part1")
    total = 0
    for bank in parsed:
        first = max(bank[:-1])
        index = bank.index(first)
        second = max(bank[index+1:])
        print(f"first: {first}, index: {index}, second: {second}")
        total += first * 10 + second

    print(f"total: {total}")



def part2() -> None:
    print("part2")
