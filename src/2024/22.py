
from functools import reduce
from api import get_input

input = get_input(2024, 22)

# create bitmask for modulo 16777216
mod_mask = (2 << 23) - 1

def get_next_secret(seed: int) -> int:
    secret = seed

    secret = (secret ^ (secret << 6)) & mod_mask # * 64
    secret = (secret ^ (secret >> 5)) & mod_mask # // 32
    secret = (secret ^ (secret << 11)) & mod_mask # * 2048

    return secret


def part1():
    print("part1")

    seeds = [int(seed) for seed in input.splitlines()]

    total = 0
    for seed in seeds:
        secret = seed
        for _ in range(2000):
            secret = get_next_secret(secret)

        total += secret

    print(total)

def part2():
    print("part2")

    seeds = [int(seed) for seed in input.splitlines()]

    sequences: tuple[int, int, int, int] = set()

    price_map: dict[tuple[int, int, int, int], int] = {}

    for seed in seeds:
        secret = seed

        changes = []

        seen_sequences: set[tuple[int, int, int, int]] = set()

        for _ in range(2000):
            new_secret = get_next_secret(secret)

            change = new_secret % 10 - secret % 10
            changes.append(change)

            sequence = tuple(changes[-4:])

            if sequence not in seen_sequences:
                sequences.add(tuple(changes[-4:]))
                price_map[sequence] =  price_map.get(sequence, 0) + (new_secret % 10)

            secret = new_secret

    print(f"{len(sequences)} sequences")

    print(max(price_map.values()))



