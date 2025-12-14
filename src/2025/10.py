from dataclasses import dataclass

import numpy as np
from scipy.optimize import LinearConstraint, milp

from api import get_input

input = get_input(2025, 10)


@dataclass
class Configuration:
    diagram: int
    wirings: set[int]
    requirements: list[int]


configurations: list[Configuration] = []

for line in input.splitlines():
    parts: list[str] = str(line).split(" ")
    diagram = sum(
        [1 << index for index, b in enumerate(parts[0].strip("[]")) if b == "#"]
    )

    wirings = set(
        [
            sum([1 << int(w) for w in wiring_str.strip("()").split(",")])
            for wiring_str in parts[1:-1]
        ]
    )

    joltages = list(map(int, parts[-1].strip("{}").split(",")))

    configurations.append(
        Configuration(
            diagram=diagram,
            wirings=wirings,
            requirements=joltages,
        )
    )


def part1() -> None:
    print("part1")

    total_presses = 0

    for configuration in configurations:
        queue = list(map(lambda w: (int(0), w, int(1)), configuration.wirings))
        visited: set[tuple[int, int]] = set()

        while queue:
            state, wiring, count = queue.pop(0)
            if (state, wiring) in visited:
                continue
            visited.add((state, wiring))

            new_state = state ^ wiring

            if new_state == configuration.diagram:
                total_presses += count
                break

            for wiring in configuration.wirings:
                if (new_state, wiring) not in visited:
                    queue.append((new_state, wiring, count + 1))

    print(total_presses)


def is_int(n):
    return abs(n - round(n)) < 0.1


def part2() -> None:
    print("part2")

    total_presses = 0

    for configuration in configurations:
        wirings = []
        for w in configuration.wirings:
            wiring = [0] * len(configuration.requirements)
            for i in range(len(wiring)):
                if w & (1 << i):
                    wiring[i] = 1
            wirings.append(tuple(wiring))

        constraints = [
            LinearConstraint(
                np.array(wirings).T,
                lb=np.array(configuration.requirements),  # pyright: ignore[reportArgumentType]
                ub=np.array(configuration.requirements),  # pyright: ignore[reportArgumentType]
            )
        ]
        integrality = np.ones(len(wirings), dtype=int)
        r = milp(
            c=np.ones(len(wirings)), constraints=constraints, integrality=integrality
        )

        total_presses += round(sum(r.x))

    print(total_presses)
