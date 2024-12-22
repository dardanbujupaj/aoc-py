
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

    price_maps: list[dict[tuple[int, int, int, int], int]] = []

    for seed in seeds:
        secret = seed

        changes = []

        possible_prices: dict[tuple[int, int, int, int], int] = {}

        for _ in range(2000):
            new_secret = get_next_secret(secret)

            change = new_secret % 10 - secret % 10
            changes.append(change)

            if tuple(changes[-4:]) not in possible_prices:
                sequences.add(tuple(changes[-4:]))
                possible_prices[tuple(changes[-4:])] = new_secret % 10

            secret = new_secret
        
        price_maps.append(possible_prices)

    print(f"{len(sequences)} sequences")

    print(max(map(lambda seq: reduce(lambda previous, price_map: previous + price_map.get(seq, 0), price_maps, 0), sequences)))



