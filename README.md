# Advent of Code

[Advent of Code](https://adventofcode.com) solutions in python.

## Setup

1. Get [poetry](https://python-poetry.org/)

2. Install dependencies
```
poetry install
```

3. Create an `.env` file with your adventofcode.com session token.

```.env
AOC_SESSION="yoursessiontoken"
```

This is needed to automatically download the puzzle inputs.

## Run solutions

- `poetry run aoc` to run the solutions of the current day.
- `poetry run p1` to run part 1
- `poetry run p2` to run part 2

The `day` and `year` can be supplied to run a solution for another day. 
- `poetry run aoc 1` for the first day of this year.
- `poetry run aoc 1 2023` for the first day of 2023.

> [!NOTE]  
> The file for the solution will be created if it doesn't exist yet.
