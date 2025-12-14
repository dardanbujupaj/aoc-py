from math import prod, sqrt


from api import get_input

input = get_input(2025, 8)

Vector = tuple[int, int, int]


def distance(a: Vector, b: Vector) -> float:
    return sqrt(sum(pow(x - y, 2) for x, y in zip(a, b)))


coordinates: list[Vector] = [
    Vector(map(int, line.split(","))) for line in input.splitlines()
]

distances = sorted(
    [
        (
            distance(a, b),
            set([a, b]),
        )
        for a_index, a in enumerate(coordinates)
        for b in coordinates[a_index + 1 :]
    ]
)


def part1() -> None:
    print("part1")

    sets: list[set[Vector]] = []

    for _, nodes in distances[:1000]:
        current = nodes.copy()
        for s in sets:
            if current & s:
                current |= s
                sets.remove(s)

        sets.append(current)

    print(prod(sorted([len(s) for s in sets], reverse=True)[:3]))


def part2() -> None:
    print("part2")
    sets: list[set[Vector]] = []

    for _, nodes in distances:
        current = nodes.copy()
        for s in sets.copy():
            if current & s:
                current |= s
                sets.remove(s)

        sets.append(current)

        if len(sorted(sets, key=len, reverse=True)[0]) == len(coordinates):
            print(prod(x for x, _, _ in nodes))
            break
