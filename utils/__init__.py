def gauss(n: int):
    return (n * (n + 1)) / 2


def grid_contains(grid: list[list], position: tuple[int, int]):
    return (
        position[0] >= 0
        and position[0] < len(grid[0])
        and position[1] >= 0
        and position[1] < len(grid)
    )
