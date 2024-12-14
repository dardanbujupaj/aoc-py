from functools import reduce
import re

from matplotlib import animation, pyplot as plt
import numpy as np
from api import get_input

input = get_input(2024, 14)

example_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

height = 103
width = 101
duration = 100

pattern = "p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)"


def parse_input(input: str):
    return list(map(parse_robot, input.splitlines()))


def parse_robot(line: str):
    px, py, vx, vy = map(int, re.match(pattern, line).groups())
    return ((px, py), (vx, vy))


def part1():
    print("part1")

    robots = parse_input(input)

    counts = [0, 0, 0, 0]

    end_positions = []
    for position, velocity in robots:
        x, y = (
            (position[0] + velocity[0] * duration) % width,
            (position[1] + velocity[1] * duration) % height,
        )

        end_positions.append((x, y))

        if x < width // 2:
            if y < height // 2:
                counts[0] += 1
            elif y > height // 2:
                counts[2] += 1
        elif x > width // 2:
            if y < height // 2:
                counts[1] += 1
            elif y > height // 2:
                counts[3] += 1

    print(reduce(lambda x, y: x * y, counts))


# generated plots of the grid, found a repetitive pattern at 98, repeating every 101 steps (width of the grid?)
# then i generated a few hundred frames, and searched for the tree
def part2():
    print("part2")

    robots = parse_input(input)

    fig, ax = plt.subplots()

    def update(duration):
        end_positions = []

        for position, velocity in robots:
            x, y = (
                (position[0] + velocity[0] * duration) % width,
                (position[1] + velocity[1] * duration) % height,
            )

            end_positions.append((x, y))

        p = np.array(end_positions)

        ax.clear()
        plt.title(f"{duration}")
        ax.scatter(p[:, 0], p[:, 1])

    ani = animation.FuncAnimation(
        fig=fig, func=update, frames=range(98, 10000, 101), interval=100
    )

    ani.save("video.mp4")
