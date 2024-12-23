from functools import cmp_to_key
from api import get_input

input = get_input(2024, 23)

example_input = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def get_neighbors(links: list[tuple[str, str]], from_node: str):
    connected: set[str] = set()

    for a, b in links:
        # print(from_node, a, b)
        if a == from_node:
            connected.add(b)
        elif b == from_node:
            connected.add(a)

    return set(connected)


def part1():
    print("part1")

    links = [tuple(line.split("-")) for line in input.splitlines()]

    starting_nodes = set()

    for from_node, to_node in links:
        if from_node.startswith("t"):
            starting_nodes.add(from_node)
        if to_node.startswith("t"):
            starting_nodes.add(to_node)

    stack: list[tuple[str, ...]] = [(node,) for node in starting_nodes]

    visited: set[tuple[str, ...]] = set()
    triplets: set[tuple[str, ...]] = set()

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        last = current[-1]

        if len(current) == 3:
            if current[0] in get_neighbors(links, last):
                triplets.add(tuple(sorted(current)))

            continue

        for connected in get_neighbors(links, last):
            if connected not in current:
                stack.append(current + (connected,))

    print(len(triplets))


def find_cliques(
    links: list[tuple[str, str]], r: set[str], p: set[str] = set(), x: set[str] = set()
):
    if not p and not x:
        return [r]

    cliques = []

    for v in list(p):
        neighbors = get_neighbors(links, v)
        cliques += find_cliques(links, r | {v}, p & neighbors, x & neighbors)

        p.remove(v)
        x.add(v)

    return cliques


def part2():
    print("part2")

    links = [tuple(line.split("-")) for line in input.splitlines()]

    starting_nodes = set()

    for from_node, to_node in links:
        starting_nodes.add(from_node)
        starting_nodes.add(to_node)

    cliques = find_cliques(links, set(), starting_nodes, set())

    largest = sorted(
        cliques, key=cmp_to_key(lambda a, b: len(a) - len(b)), reverse=True
    )[0]

    print(",".join(sorted(largest)))
