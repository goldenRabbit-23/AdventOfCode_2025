import sys


def main() -> None:
    insts = open(sys.argv[1]).read().splitlines()
    dial = 50
    password = 0

    for inst in insts:
        dir, val = inst[0], int(inst[1:])

        if dir == "L":
            first = 100 if dial == 0 else dial
            dial = (dial - val) % 100
        else:
            first = 100 if dial == 0 else 100 - dial
            dial = (dial + val) % 100

        if val >= first:
            password += 1 + (val - first) // 100

    print(password)


if __name__ == "__main__":
    main()
