from api import get_input

input = get_input(2024, 4)


def parse_input(input: str):
    return [list(line) for line in input.splitlines()]


def part1():
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    grid = parse_input(input)

    word = list("XMAS")

    count = 0
    for n in range(len(grid)):
        for m in range(len(grid[n])):
            for direction in directions:
                try:
                    for i, c in enumerate(word):
                        row = n + direction[0] * i
                        col = m + direction[1] * i

                        if (
                            row < 0
                            or row >= len(grid)
                            or col < 0
                            or col >= len(grid[0])
                        ):
                            raise Exception()

                        if not grid[row][col] == c:
                            raise Exception()

                    count += 1
                except Exception:
                    pass

    print(count)


def part2():
    grid = parse_input(input)

    words = ["MAS", "SAM"]

    count = 0
    for n in range(1, len(grid) - 1):
        for m in range(1, len(grid[n]) - 1):
            axis_1 = "".join(
                [
                    grid[n - 1][m - 1],
                    grid[n][m],
                    grid[n + 1][m + 1],
                ]
            )
            axis_2 = "".join(
                [
                    grid[n - 1][m + 1],
                    grid[n][m],
                    grid[n + 1][m - 1],
                ]
            )

            if axis_1 in words and axis_2 in words:
                count += 1

    print(count)
