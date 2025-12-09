from api import get_input

input = get_input(2025, 7)

cells = [list(line) for line in input.splitlines()]


def part1() -> None:
    print("part1")
    splits = 0
    beams = set([cells[0].index("S")])

    for row in cells[1:]:
        for beam in beams.copy():
            if row[beam] == "^":
                splits += 1
                beams.add(beam + 1)
                beams.add(beam - 1)
                beams.remove(beam)

    print(splits)


def part2() -> None:
    print("part2")
    columns = [1 if s == "S" else 0 for s in cells[0]]

    for row in cells[1:]:
        new_columns = [0] * len(columns)

        for beam, timelines in enumerate(columns):
            if row[beam] == "^":
                new_columns[beam - 1] += timelines
                new_columns[beam + 1] += timelines
            else:
                new_columns[beam] += timelines

        columns = new_columns

    print(sum(columns))
