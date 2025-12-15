from dataclasses import dataclass

import cvxpy as cp
import numpy as np

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


def part2() -> None:
    print("part2")

    total_presses = 0

    for configuration in configurations:
        wirings = np.array(
            [
                w >> np.arange(len(configuration.requirements)) & 1
                for w in configuration.wirings
            ]
        ).T
        requirements = np.array(configuration.requirements)

        x = cp.Variable(wirings.shape[1], integer=True)
        obj = cp.Minimize(cp.sum(x))
        constraints = [
            wirings @ x == requirements,
            x >= 0,
        ]

        problem = cp.Problem(obj, constraints)
        problem.solve()

        if problem.status != cp.OPTIMAL:
            print("No solution found")
            continue

        total_presses += round(problem.value)  # pyright: ignore[reportArgumentType]

    print(total_presses)
