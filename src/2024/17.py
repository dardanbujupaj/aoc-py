import re
from api import get_input

input = get_input(2024, 17)


def parse_input(input_str: str):
    a, b, c, *program = list(map(int, re.findall(r"(\d+)", input_str)))

    return a, b, c, program


def get_combo_operand(operand, a, b, c):
    match operand:
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case 7:
            raise Exception("Invalid operand")
        case _:
            return operand


def run_program(program, initial_a, initial_b, initial_c):
    output: list[int] = []

    a, b, c = initial_a, initial_b, initial_c

    instruction_pointer = 0

    while instruction_pointer < len(program):
        instruction, operand = program[instruction_pointer : instruction_pointer + 2]
        # print(f"{instruction_pointer}: [{a}, {b}, {c}] {instruction} {operand}")

        literal = operand
        combo_operand = None

        try:
            combo_operand = get_combo_operand(operand, a, b, c)
        except Exception:
            pass

        match instruction:
            case 0:
                a = a // 2**combo_operand
            case 1:
                b = b ^ literal
            case 2:
                b = combo_operand % 8
            case 3:
                if a == 0:
                    pass
                else:
                    instruction_pointer = literal
                    continue
            case 4:
                b = b ^ c
            case 5:
                output.append(combo_operand % 8)
            case 6:
                b = a // 2**combo_operand
            case 7:
                c = a // 2**combo_operand

        instruction_pointer += 2

    return output, a, b, c


# tests for pogram correctness
#
# def test_program(program, a, b, c, expected_output, expected_a, expected_b, expected_c):
#     output, out_a, out_b, out_c = run_program(program, a, b, c)
#
#     if expected_output is not None and output != expected_output:
#         raise Exception(f"Output mismatch. Expected {expected_output}, got {output}")
#     if expected_a is not None and out_a != expected_a:
#         raise Exception(f"a mismatch. Expected {expected_a}, got {out_a}")
#     if expected_b is not None and out_b != expected_b:
#         raise Exception(f"b mismatch. Expected {expected_b}, got {out_b}")
#     if expected_c is not None and out_c != expected_c:
#         raise Exception(f"c mismatch. Expected {expected_c}, got {out_c}")
#
#
# def test_suite():
#     test_program([2, 6], 0, 0, 9, None, None, 1, None)
#     test_program([5, 0, 5, 1, 5, 4], 10, 0, 0, [0, 1, 2], None, None, None)
#     test_program(
#         [0, 1, 5, 4, 3, 0], 2024, 0, 0, [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0], 0, None, None
#     )
#     test_program([1, 7], 0, 29, 0, None, None, 26, None)
#     test_program([4, 0], 0, 2024, 43690, None, None, 44354, None)


def part1():
    print("part1")
    a, b, c, program = parse_input(input)

    output, *_ = run_program(program, a, b, c)

    print(",".join(str(x) for x in output))


def get_replicating_program_input(program: list[int], a: int, b: int, c: int):
    for i in range(8):
        output, *_ = run_program(program, a + i, b, c)

        if output == program:
            # print(output)
            return a + i

        if output == program[-len(output) :]:
            # print(output)
            try:
                return get_replicating_program_input(program, (a + i) * 8, b, c)
            except Exception:
                pass

    raise Exception("Not possible")


def part2():
    print("part2")
    _, b, c, program = parse_input(input)

    print(get_replicating_program_input(program, 0, b, c))
