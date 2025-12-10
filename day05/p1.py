import sys


def main() -> None:
    ranges, ids = open(sys.argv[1]).read().split("\n\n")
    ranges = [tuple(map(int, rng.split("-"))) for rng in ranges.splitlines()]
    ids = [int(id) for id in ids.splitlines()]
    fresh = 0

    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                fresh += 1
                break

    print(fresh)


if __name__ == "__main__":
    main()
