def gauss(n: int):
    return (n * (n + 1)) / 2


def grid_contains(grid: list[list], position: tuple[int, int]):
    return (
        position[0] >= 0
        and position[0] < len(grid[0])
        and position[1] >= 0
        and position[1] < len(grid)
    )


def griderator(x: int | range, y: int | range):
    x_iter = x if isinstance(x, range) else range(x)
    y_iter = y if isinstance(y, range) else range(y)

    for x in x_iter:
        for y in y_iter:
            yield (x, y)
