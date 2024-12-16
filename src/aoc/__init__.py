import sys
from datetime import date
from importlib import import_module
from pathlib import Path


def both():
    module = get_module()
    module.part1()
    module.part2()


def part1():
    module = get_module()
    module.part1()


def part2():
    module = get_module()
    module.part2()


def get_module():
    day = int(sys.argv[1]) if len(sys.argv) > 1 else date.today().day
    year = int(sys.argv[2]) if len(sys.argv) > 2 else date.today().year

    print(f"AOC {year} day {day}")

    try:
        return import_module(f"{year}.{day}")
    except ModuleNotFoundError:
        print("Bootstrap solution")
        file = Path(f"src/{year}/{day}.py")
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(get_template(year, day))

        return import_module(f"{year}.{day}")


def get_template(year: int, day: int):
    return f"""
from api import get_input

input = get_input({year}, {day})

def part1():
    print("part1")

def part2():
    print("part2")
"""
