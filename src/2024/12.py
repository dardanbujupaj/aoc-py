from api import get_input

input = get_input(2024, 12)


def parse_input(input: str):
    return [list(line) for line in input.splitlines()]


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def part1():
    print("part1")
    grid = parse_input(input)
    visited = set()

    total = 0

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x, y) in visited:
                continue

            area = 0
            fence = 0

            stack = [(x, y)]

            while len(stack) > 0:
                current = stack.pop()

                area += 1

                visited.add(current)

                for direction in directions:
                    dx, dy = current[0] + direction[0], current[1] + direction[1]

                    if (
                        not 0 <= dx < len(grid[0])
                        or not 0 <= dy < len(grid)
                        or grid[dy][dx] != cell
                    ):
                        fence += 1
                        continue

                    if (dx, dy) not in visited and (dx, dy) not in stack:
                        stack.append((dx, dy))

            # print(f"{cell} area: {area}, fence: {fence}")
            total += area * fence

    print(total)


fence_offsets = [
    ((1, 0), (1, 1)),
    ((0, 1), (0, 0)),
    ((0, 1), (1, 1)),
    ((1, 0), (0, 0)),
]


def sign(x: int):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def fence_orientation(fence: tuple[tuple[int, int], tuple[int, int]]):
    return sign(fence[0][0] - fence[1][0]), sign(fence[0][1] - fence[1][1])


def optimize_fences(fences: list[tuple[tuple[int, int], tuple[int, int]]]):
    last_fence_amount = len(fences)

    while True:
        for i, fence in enumerate(fences):
            for j, other_fence in enumerate(fences):
                if i == j or fence_orientation(fence) != fence_orientation(other_fence):
                    continue
                if fence[0] == other_fence[1]:
                    fences[i] = (other_fence[0], fence[1])
                    fences.remove(other_fence)
                    break
                elif fence[1] == other_fence[0]:
                    fences[i] = (fence[0], other_fence[1])
                    fences.remove(other_fence)
                    break
        if len(fences) == last_fence_amount:
            break
        last_fence_amount = len(fences)

    return fences


def part2():
    print("part2")
    grid = parse_input(input)
    visited = set()

    total = 0

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x, y) in visited:
                continue

            area = 0
            fences: list[tuple[tuple[int, int], tuple[int, int]]] = list()

            stack = [(x, y)]

            while len(stack) > 0:
                current = stack.pop()

                area += 1

                visited.add(current)

                for direction_index, direction in enumerate(directions):
                    dx, dy = current[0] + direction[0], current[1] + direction[1]

                    if (
                        not 0 <= dx < len(grid[0])
                        or not 0 <= dy < len(grid)
                        or grid[dy][dx] != cell
                    ):
                        fence_offset = fence_offsets[direction_index]
                        fences.append(
                            (
                                (fence_offset[0][0] + dx, fence_offset[0][1] + dy),
                                (fence_offset[1][0] + dx, fence_offset[1][1] + dy),
                            )
                        )
                        continue

                    if (dx, dy) not in visited and (dx, dy) not in stack:
                        stack.append((dx, dy))

            fences = optimize_fences(fences)

            # print(f"{cell} area: {area}, fence: {len(fences)}")
            total += area * len(fences)

    print(total)
