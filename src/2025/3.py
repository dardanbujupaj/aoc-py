from api import get_input

input = get_input(2025, 3)

parsed = [[int(digit) for digit in list(line)] for line in input.splitlines()]


def max_joltage(bank: list[int], digits=2) -> int:
    for i in range(9, 0, -1):
        candidates = bank[: len(bank) - (digits - 1)]

        for index, d in enumerate(candidates):
            if d == i:
                sub = max_joltage(bank[index + 1 :], digits - 1) if digits > 1 else 0
                return d * pow(10, digits - 1) + sub

    return 0


def part1() -> None:
    print("part1")

    total = sum([max_joltage(bank) for bank in parsed])

    print(f"total: {total}")


def part2() -> None:
    print("part2")

    total = sum([max_joltage(bank, 12) for bank in parsed])

    print(f"total: {total}")


if __name__ == "__main__":
    part1()
