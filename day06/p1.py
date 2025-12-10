import sys
from math import prod


def main() -> None:
    *num_lists, ops = open(sys.argv[1]).read().splitlines()
    num_lists = [list(map(int, num_list.split())) for num_list in num_lists]
    num_lists = list(zip(*num_lists))
    ops = ops.split()
    total = 0

    for num_list, op in zip(num_lists, ops):
        if op == "+":
            total += sum(num_list)
        elif op == "*":
            total += prod(num_list)

    print(total)


if __name__ == "__main__":
    main()
