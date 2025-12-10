import sys


def main() -> None:
    grid = open(sys.argv[1]).read().splitlines()
    h, w = len(grid), len(grid[0])

    for c, ch in enumerate(grid[0]):
        if ch == "S":
            sc = c
            break

    ways = [[0] * w for _ in range(h)]
    ways[0][sc] = 1

    for r in range(h - 1):
        for c in range(w):
            if ways[r][c] == 0:
                continue  # No way to reach this cell

            below = grid[r + 1][c]

            if below == ".":
                ways[r + 1][c] += ways[r][c]
            elif below == "^":
                # split into left and right timelines
                ways[r + 1][c - 1] += ways[r][c]
                ways[r + 1][c + 1] += ways[r][c]

    print(sum(ways[h - 1]))


if __name__ == "__main__":
    main()
