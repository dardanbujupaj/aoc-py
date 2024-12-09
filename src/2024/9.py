from api import get_input

input = get_input(2024, 9)


example_input = "2333133121414131402"


def parse_input(input: str):
    return [
        (int(size), index // 2 if index % 2 == 0 else None)
        for index, size in enumerate(input.strip())
    ]


def part1():
    blocks = parse_input(input)
    compacted_blocks: list[tuple[int, int]] = []

    while len(blocks) > 0:
        current = blocks.pop(0)

        if current[1] is None:
            capacity = current[0]
            while capacity > 0 and len(blocks) > 0:
                next = blocks.pop()
                if next[1] is None:
                    next = blocks.pop()

                amount = min(capacity, next[0])
                compacted_blocks.append((amount, next[1]))

                if next[0] > amount:
                    blocks.append((next[0] - amount, next[1]))

                capacity -= amount
        else:
            compacted_blocks.append(current)

    print(calculate_checksum(compacted_blocks))


def part2():
    blocks = parse_input(input)

    for size, id in reversed(blocks):
        if id is None:
            continue

        # print(format_blocks(blocks))

        try:
            index = blocks.index((size, id))

            # will raise StopIteration if no fitting slot is available
            slot_index, slot = next(
                (i, s)
                for i, s in enumerate(blocks)
                if (i < index and s[1] is None and s[0] >= size)
            )

            # print(f"move {index}: {(size, id)} > {slot_index}: {slot}")

            # switch blocks
            blocks[index] = (size, None)
            blocks[slot_index] = (size, id)

            # add filler blocks if slot was larger than compacted block
            if size < slot[0]:
                blocks.insert(slot_index + 1, (slot[0] - size, None))

        except StopIteration:
            pass

    # print(format_blocks(blocks))

    print(calculate_checksum(blocks))


def format_blocks(blocks: list[tuple[int, int]]):
    output = ""
    for size, id in blocks:
        output += ("." if id is None else str(id)) * size

    return output


def calculate_checksum(blocks: list[tuple[int, int]]):
    checksum = 0
    offset = 0

    for size, index in blocks:
        if index is not None:
            checksum += int((offset + (size - 1) / 2) * size * index)
        offset += size

    return checksum
