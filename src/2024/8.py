import math
from api import get_input
from utils import grid_contains

input = get_input(2024, 8)

example_input = """......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.""".replace("#", ".")


def parse_input(input: str):
    return [list(line) for line in input.splitlines()]


def part1():
    grid = parse_input(input)
    antenna_groups: map[str, list[(int, int)]] = {}

    for y, row in enumerate(grid):
        for x, frequency in enumerate(row):
            if frequency != ".":
                if antenna_groups.get(frequency) is None:
                    antenna_groups[frequency] = list()

                antenna_groups[frequency].append((x, y))

    antinodes: set[(int, int)] = set()

    for frequency, antennas in antenna_groups.items():
        for index, antenna in enumerate(antennas):
            for other in antennas[index + 1 :]:
                distance = (antenna[0] - other[0], antenna[1] - other[1])

                node1 = (antenna[0] + distance[0], antenna[1] + distance[1])
                if grid_contains(grid, node1):
                    antinodes.add(node1)

                node2 = (other[0] - distance[0], other[1] - distance[1])
                if grid_contains(grid, node2):
                    antinodes.add(node2)

    print(len(antinodes))


def part2():
    grid = parse_input(input)
    antenna_groups: map[str, list[(int, int)]] = {}

    for y, row in enumerate(grid):
        for x, frequency in enumerate(row):
            if frequency != ".":
                if antenna_groups.get(frequency) is None:
                    antenna_groups[frequency] = list()

                antenna_groups[frequency].append((x, y))

    antinodes: set[(int, int)] = set()

    for frequency, antennas in antenna_groups.items():
        for index, antenna in enumerate(antennas):
            for other in antennas[index + 1 :]:
                distance = (antenna[0] - other[0], antenna[1] - other[1])

                factor = math.gcd(distance[0], distance[1])

                normalized_distance = (
                    distance[0] // factor,
                    distance[1] // factor,
                )

                counter = 0

                while True:
                    position = (
                        antenna[0] + normalized_distance[0] * counter,
                        antenna[1] + normalized_distance[1] * counter,
                    )
                    if grid_contains(grid, position):
                        antinodes.add(position)
                        counter += 1
                    else:
                        break

                counter = -1
                while True:
                    position = (
                        antenna[0] + normalized_distance[0] * counter,
                        antenna[1] + normalized_distance[1] * counter,
                    )
                    if grid_contains(grid, position):
                        antinodes.add(position)
                        counter -= 1
                    else:
                        break

    print(len(antinodes))
