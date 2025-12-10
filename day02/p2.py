import sys


def main() -> None:
    ranges = open(sys.argv[1]).read().split(",")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    total = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            s = str(num)
            l = len(s)

            for p in range(1, l // 2 + 1):
                if l % p != 0:
                    continue

                pattern = s[:p]
                if pattern * (l // p) == s:
                    total += num
                    break

    print(total)


if __name__ == "__main__":
    main()
