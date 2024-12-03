from api import get_input


input = get_input(2024, 2)


def parse_input(input: str):
    return [[int(c) for c in line.split(" ")] for line in input.splitlines()]


def check_report(report: list[int]):
    if not (sorted(report) == report or sorted(report, reverse=True) == report):
        return False

    for i, v in enumerate(report[1:]):
        previous = report[i]
        diff = abs(previous - v)

        if not 1 <= diff <= 3:
            return False

    return True


def part1():
    reports = parse_input(input)
    safe = list(filter(check_report, reports))
    print(len(safe))


def dampen_check(report: list[str]):
    if check_report(report):
        return True

    for i in range(len(report)):
        dampener = report[:i] + report[i + 1 :]

        if check_report(dampener):
            return True

    return False


def part2():
    reports = parse_input(input)
    safe = list(filter(dampen_check, reports))
    print(len(safe))
