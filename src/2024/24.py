from collections import deque
from functools import reduce
import re
from api import get_input
from graphviz import Digraph


input = get_input(2024, 24)

example_input = """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z00
x01 AND y01 -> z01
x02 AND y02 -> z02
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z05"""


def parse_input(input: str):
    inputs_str, gates_str = input.split("\n\n")

    inputs = [
        (line.split(": ")[0], int(line.split(": ")[1]))
        for line in inputs_str.splitlines()
    ]

    gate_pattern = r"(\w+) (\w+) (\w+) -> (\w+)"
    gates = [re.match(gate_pattern, line).groups() for line in gates_str.splitlines()]

    return inputs, gates


def simulate_gates(inputs, gates):
    state = dict(inputs)

    queue = deque(gates)

    last_modification = 0
    while queue:
        left, operation, right, output = queue.popleft()

        if left in state and right in state:
            match operation:
                case "AND":
                    state[output] = state[left] & state[right]
                case "OR":
                    state[output] = state[left] | state[right]
                case "XOR":
                    state[output] = state[left] ^ state[right]
            last_modification = 0
        else:
            queue.append((left, operation, right, output))
            last_modification += 1

        if last_modification > len(queue):
            raise Exception("Circuit is not deterministic")

    return state


def part1():
    print("part1")

    inputs, gates = parse_input(example_input)
    state = simulate_gates(inputs, gates)

    value = 0

    for i, z in enumerate(sorted(filter(lambda x: x.startswith("z"), state.keys()))):
        value |= state[z] << i

    print(value)


def check_faulty_outputs(inputs, gates):
    state = simulate_gates(inputs, gates)

    value_x = 0
    value_y = 0
    value_z = 0

    for i, x in enumerate(sorted(filter(lambda a: a.startswith("x"), state.keys()))):
        value_x |= state[x] << i

    for i, y in enumerate(sorted(filter(lambda a: a.startswith("y"), state.keys()))):
        value_y |= state[y] << i

    for i, z in enumerate(sorted(filter(lambda a: a.startswith("z"), state.keys()))):
        value_z |= state[z] << i

    faulty_outputs = set()

    for i, z in enumerate(sorted(filter(lambda a: a.startswith("z"), state.keys()))):
        if state[z] << i != (value_x + value_y) & (1 << i):
            faulty_outputs.add(z)

    return faulty_outputs


def get_dependencies(gates: tuple[str, str, str, str], output: str):
    dependencies = list()

    stack: list[str] = [output]

    while stack:
        current = stack.pop()
        dependencies.append(current)

        try:
            gate = next(filter(lambda gate: gate[3] == current, gates))
            left, operator, right, output = gate
            stack.append(right)
            stack.append(left)
        except StopIteration:
            continue

    return dependencies


def part2():
    print("part2")
    inputs, gates = parse_input(input)

    switches = {
        ("dhq", "z18"),
        ("pdg", "z22"),
        ("hbs", "kfp"),
        ("jcp", "z27"),
    }

    for left, right in switches:
        left_gate = next(filter(lambda gate: gate[3] == left, gates))
        right_gate = next(filter(lambda gate: gate[3] == right, gates))

        gates.remove(left_gate)
        gates.remove(right_gate)

        gates.append((left_gate[0], left_gate[1], left_gate[2], right_gate[3]))
        gates.append((right_gate[0], right_gate[1], right_gate[2], left_gate[3]))

    faulty_outputs = check_faulty_outputs(inputs, gates)
    if faulty_outputs:
        print(sorted(faulty_outputs))
        print("Printing debugging graph...")

    else:
        flattened_switches = reduce(lambda a, b: a + list(b), switches, list())
        print(f"Result\n{",".join(sorted(flattened_switches))}")
        return

    # print operations graph to manually spot wrong connections
    dot = Digraph()
    with dot.subgraph() as s:
        s.attr(rank="same")
        for x in list(filter(lambda x: x.startswith("x"), map(lambda x: x[0], inputs))):
            s.node(x)

    with dot.subgraph() as s:
        s.attr(rank="same")
        for y in list(filter(lambda y: y.startswith("y"), map(lambda x: x[0], inputs))):
            s.node(y)

    with dot.subgraph() as s:
        s.attr(rank="same")
        for z in list(filter(lambda z: z.startswith("z"), map(lambda x: x[3], gates))):
            s.node(z)

    for a, operator, b, output in gates:
        dot.edge(a, output, label=operator)
        dot.edge(b, output, label=operator)

    dot.render("unidirectional_graph", view=True)
