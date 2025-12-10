import sys
from functools import cache


def main() -> None:
    banks = open(sys.argv[1]).read().splitlines()
    banks = [list(map(int, bank)) for bank in banks]
    total = 0

    for bank in banks:
        n = len(bank)

        @cache
        def dp(i: int, t: int) -> int:
            if t == 0:
                return 0

            if i == n:
                return -1

            skip = dp(i + 1, t)
            rest = dp(i + 1, t - 1)
            take = -1 if rest == -1 else bank[i] * 10**(t - 1) + rest

            return max(skip, take)

        total += dp(0, 12)

    print(total)


if __name__ == "__main__":
    main()
