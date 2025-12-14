from functools import cache

from api import get_input

input = get_input(2025, 11)

parsed = {
    line.split(": ")[0]: set(map(str, line.split(": ")[1].split(" ")))
    for line in input.splitlines()
}


@cache
def find_paths(start: str, dac=True, fft=True) -> int:
    paths = 0
    if start == "dac":
        dac = True
    if start == "fft":
        fft = True

    for next in parsed[start]:
        if next == "out":
            if dac and fft:
                paths += 1
        else:
            paths += find_paths(next, dac, fft)
    return paths


def part1() -> None:
    print("part1")
    print(find_paths("you"))


def part2() -> None:
    print("part2")
    print(find_paths("svr", False, False))
