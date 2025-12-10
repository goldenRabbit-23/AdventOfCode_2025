import sys


def main() -> None:
    insts = open(sys.argv[1]).read().splitlines()
    dial = 50
    password = 0

    for inst in insts:
        dir, val = inst[0], int(inst[1:])
        dial += (-1 if dir == "L" else 1) * val
        dial %= 100
        if dial == 0:
            password += 1

    print(password)


if __name__ == "__main__":
    main()
