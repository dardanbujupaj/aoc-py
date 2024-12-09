# Advent of Code

[Advent of Code](https://adventofcode.com) solutions in python.

## Setup

1. Get [uv](https://docs.astral.sh/uv/)

2. Create an `.env` file with your adventofcode.com session token.

```.env
AOC_SESSION="yoursessiontoken"
```

This is needed to automatically download the puzzle inputs.

## Run solutions

- `uv run aoc` to run the solutions of the current day.
- `uv run p1` to run part 1
- `uv run p2` to run part 2

The `day` and `year` can be supplied to run a solution for another day. 
- `uv run aoc 1` for the first day of this year.
- `uv run aoc 1 2023` for the first day of 2023.

> [!NOTE]  
> The file for the solution will be created if it doesn't exist yet.
