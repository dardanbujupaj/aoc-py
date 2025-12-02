from api import get_input

input = get_input(2025, 1)

parsed = [-int(x[1:]) if x[:1] == "L" else int(x[1:]) for x in input.splitlines()]


def part1() -> None:
    print("part1")

    count = 0
    dial = 50

    for direction in parsed:
        dial += direction
        if dial % 100 == 0:
            count += 1

    print(count)


def part2() -> None:
    print("part2")

    count = 0
    dial = 50

    for direction in parsed:
        count += len(clicks_range(dial, dial + direction))
        dial = dial + direction

    print(count)


def sign(x: int) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def clicks_range(start: int, end: int) -> range:
    direction = sign(end - start)

    corrected_end = (
        end
        if end % 100 == 0
        else (end // 100) * 100
        if direction == 1
        else (end // 100 + 1) * 100
    )

    return range(corrected_end, start, -direction * 100)


def test_clicks_in_range():
    assert set(clicks_range(100, 200)) == set([200])
    assert set(clicks_range(99, 200)) == set([100, 200])
    assert set(clicks_range(-100, 200)) == set([0, 100, 200])
    assert set(clicks_range(-50, 200)) == set([0, 100, 200])
    assert set(clicks_range(300, 100)) == set([200, 100])
    assert set(clicks_range(299, 99)) == set([200, 100])
    assert set(clicks_range(200, 20)) == set([100])
    assert set(clicks_range(-30, -110)) == set([-100])
    assert set(clicks_range(-100, -120)) == set([])
    assert set(clicks_range(-90, -100)) == set([-100])
