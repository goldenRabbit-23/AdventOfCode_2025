import sys


def main() -> None:
    ranges = open(sys.argv[1]).read().split(",")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    total = 0

    for start, end in ranges:
        if len(str(start)) % 2 == 1 and len(str(end)) % 2 == 1:
            continue

        for num in range(start, end + 1):
            s = str(num)
            l = len(s)

            if l % 2 == 0 and s[:l // 2] == s[l // 2:]:
                total += num

    print(total)


if __name__ == "__main__":
    main()
