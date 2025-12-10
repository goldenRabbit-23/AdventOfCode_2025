import sys


def main() -> None:
    grid = open(sys.argv[1]).read().splitlines()
    h, w = len(grid), len(grid[0])
    removed = 0

    while True:
        found = []
        for r, row in enumerate(grid):
            for c, p in enumerate(row):
                if p == ".":
                    continue

                adjacent_rolls = sum(grid[r + dr][c + dc] == "@"
                                     for dr in [-1, 0, 1]
                                     for dc in [-1, 0, 1]
                                     if 0 <= r + dr < h and 0 <= c + dc < w
                                                        and (dr != 0 or dc != 0))

                if adjacent_rolls < 4:
                    found.append((r, c))

        if not found:
            break

        removed += len(found)
        for r, c in found:
            grid[r] = grid[r][:c] + "." + grid[r][c+1:]

    print(removed)


if __name__ == "__main__":
    main()
