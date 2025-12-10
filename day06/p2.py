import sys
from math import prod


def main() -> None:
    *num_lists, ops = open(sys.argv[1]).read().splitlines()
    num_lists = [list(num_list) for num_list in num_lists]
    ops = ops.split()

    rows, width = len(num_lists), len(num_lists[0])
    blocks = []  # [start, end)
    in_block = False

    for c in range(width):
        col_has_char = any(num_lists[r][c] != ' ' for r in range(rows))
        if col_has_char and not in_block:
            in_block = True
            start = c
        elif not col_has_char and in_block:
            in_block = False
            blocks.append((start, c))

    if in_block:
        blocks.append((start, width))

    total = 0

    for (start, end), op in zip(blocks, ops):
        digit_row = [
            ''.join(num_lists[r][start:end])
            for r in range(rows)
        ]
        digit_row = [int(''.join(digit)) for digit in list(zip(*digit_row))]

        if op == "+":
            total += sum(digit_row)
        elif op == "*":
            total += prod(digit_row)

    print(total)


if __name__ == "__main__":
    main()
