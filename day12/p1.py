import sys


def main() -> None:
    *_, query_data = open(sys.argv[1]).read().split("\n\n")
    valid = 0

    for query in query_data.splitlines():
        dim, nums = query.split(": ")
        w, h = map(int, dim.split("x"))
        nums = list(map(int, nums.split()))
        valid += 1 if sum(nums) * 9 <= w * h else 0

    print(valid)


if __name__ == "__main__":
    main()
