import sys
from collections import deque


def main() -> None:
    grid = open(sys.argv[1]).read().splitlines()
    h = len(grid)
    split_count = 0

    for c, ch in enumerate(grid[0]):
        if ch == "S":
            sc = c
            break

    q = deque([(0, sc)])
    visited = {(0, sc)}

    while q:
        cr, cc = q.popleft()

        if cr >= h - 1:
            continue  # Reached the bottom row

        nr = cr + 1
        below = grid[nr][cc]

        if below == ".":
            if (nr, cc) not in visited:
                visited.add((nr, cc))
                q.append((nr, cc))  # Move down
        elif below == "^":
            split_count += 1  # Split occurs
            if (nr, cc - 1) not in visited:
                visited.add((nr, cc - 1))
                q.append((nr, cc - 1))  # Move down-left
            if (nr, cc + 1) not in visited:
                visited.add((nr, cc + 1))
                q.append((nr, cc + 1))  # Move down-right

    print(split_count)


if __name__ == "__main__":
    main()
