import sys


def main() -> None:
    ranges = open(sys.argv[1]).read().split("\n\n")[0]
    ranges = [tuple(map(int, rng.split("-"))) for rng in ranges.splitlines()]
    fresh = 0

    ranges.sort()
    cur_start, cur_end = ranges[0]
    for start, end in ranges[1:]:
        if start > cur_end:
            fresh += cur_end - cur_start + 1
            cur_start, cur_end = start, end
        else:
            cur_end = max(cur_end, end)

    fresh += cur_end - cur_start + 1
    print(fresh)


if __name__ == "__main__":
    main()
