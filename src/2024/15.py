from api import get_input

input = get_input(2024, 15)


def parse_input(input: str, scaled: bool = False):
    grid_string, movment_string = input.split("\n\n")

    if scaled:
        grid_string = grid_string.replace(".", "..")
        grid_string = grid_string.replace("#", "##")
        grid_string = grid_string.replace("@", "@.")
        grid_string = grid_string.replace("O", "[]")

    grid = [list(line) for line in grid_string.splitlines()]
    moves = list(movment_string.replace("\n", ""))

    robot = (0, 0)
    boxes: set[tuple[int, int]] = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                robot = (x, y)
                grid[y][x] = "."
            elif cell == "O":
                boxes.add((x, y))
                grid[y][x] = "."

    return grid, moves, robot, boxes


def get_direction(move: str):
    match move:
        case "<":
            return -1, 0
        case ">":
            return 1, 0
        case "^":
            return 0, -1
        case "v":
            return 0, 1
        case _:
            raise ValueError(f"Invalid move: {move}")


def draw_grid(grid: list[list[str]], boxes, robot):
    output = ""

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if robot == (x, y):
                output += "@"
            elif (x, y) in boxes:
                output += "O"
            else:
                output += cell
        output += "\n"

    return output


def part1():
    print("part1")
    grid, moves, robot, boxes = parse_input(input)

    for move in moves:
        direction = get_direction(move)

        target_position = robot[0] + direction[0], robot[1] + direction[1]

        next_position = target_position

        while True:
            if grid[next_position[1]][next_position[0]] == "#":
                break
            elif next_position in boxes:
                next_position = (
                    next_position[0] + direction[0],
                    next_position[1] + direction[1],
                )
            else:
                if target_position != next_position:
                    boxes.remove(target_position)
                    boxes.add(next_position)
                robot = target_position
                break

    print(draw_grid(grid, boxes, robot))

    print(sum(map(lambda box: box[1] * 100 + box[0], boxes)))


def get_connected_cells(
    grid: list[list[str]], start: tuple[int, int], direction: tuple[int, int]
):
    connected: set[tuple[int, int]] = set()
    visited: set[tuple[int, int]] = set()
    queue = [start]

    while len(queue) > 0:
        position = queue.pop()

        if position in visited:
            continue

        visited.add(position)

        cell = grid[position[1]][position[0]]
        if cell == "#" or cell == ".":
            continue

        connected.add(position)

        if cell == "[":
            queue.append((position[0] + 1, position[1]))
        elif cell == "]":
            queue.append((position[0] - 1, position[1]))

        queue.append((position[0] + direction[0], position[1] + direction[1]))

    return connected


def can_move(
    grid: list[list[str]], position: tuple[int, int], direction: tuple[int, int]
):
    return grid[position[1] + direction[1]][position[0] + direction[0]] != "#"


def part2():
    print("part2")
    grid, moves, robot, _ = parse_input(input, scaled=True)

    for move in moves:
        direction = get_direction(move)

        target_position = robot[0] + direction[0], robot[1] + direction[1]

        if grid[target_position[1]][target_position[0]] == "#":
            continue

        connected_cells = list(get_connected_cells(grid, target_position, direction))

        if all(map(lambda cell: can_move(grid, cell, direction), connected_cells)):
            types = list(map(lambda cell: grid[cell[1]][cell[0]], connected_cells))

            for cell in connected_cells:
                grid[cell[1]][cell[0]] = "."

            for i, cell in enumerate(connected_cells):
                grid[cell[1] + direction[1]][cell[0] + direction[0]] = types[i]

            robot = target_position

    print(draw_grid(grid, set(), robot))

    count = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "[":
                count += 100 * y + x

    print(count)
