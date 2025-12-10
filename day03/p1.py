import sys


def main() -> None:
    banks = open(sys.argv[1]).read().splitlines()
    banks = [list(map(int, bank)) for bank in banks]
    total = 0

    for bank in banks:
        best = 0
        max_left_digit = -1

        for d in bank:
            if max_left_digit != -1:
                best = max(best, max_left_digit * 10 + d)
            max_left_digit = max(max_left_digit, d)

        total += best

    print(total)


if __name__ == "__main__":
    main()
